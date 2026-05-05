from jinja2 import Environment, FileSystemLoader
from stix2 import Filter
from stix2 import MemoryStore
from pathlib import Path
from loguru import logger
from . import ROOT

import requests
import os
import json
import uuid
import re

class MarkdownGenerator():

    def __init__(self, output_dir=None, tactics=[], techniques=[], mitigations=[], groups=[], software=[], domain="enterprise-attack"):
        self.vault_relative_root = "kb/mitre/attack"
        if output_dir:
            self.output_dir = os.path.join(ROOT, output_dir, self.vault_relative_root)
            os.makedirs(self.output_dir, exist_ok=True)
        self.domain = domain
        self.tactics = tactics
        self.techniques = techniques
        self.mitigations = mitigations
        self.groups = groups
        self.software = software
        self.environment = Environment(loader=FileSystemLoader(os.path.join(ROOT, "res/templates/")))
        self.objects_by_id = self._build_object_index()
        self.environment.filters["parse_description"] = self.parse_description

    @staticmethod
    def sort_by_id(rows):
        return sorted(rows, key=lambda row: row["id"])

    @staticmethod
    def tag_value(value):
        value = value.lower().replace('&', 'and')
        value = re.sub(r'[^a-z0-9]+', '_', value)
        return value.strip('_')

    @classmethod
    def tag(cls, *parts):
        return "/".join([cls.tag_value(part) for part in parts if part])

    def base_tags(self):
        return [self.tag("attack", "domain", self.domain)]

    def tactic_tags(self):
        return sorted(set(self.base_tags() + ["attack/type/tactic"]))

    def technique_tags(self, technique, tactics, procedures, mitigations, subtechniques):
        tags = self.base_tags() + ["attack/type/subtechnique" if technique.is_subtechnique else "attack/type/technique"]
        if technique.is_subtechnique:
            tags.append("attack/subtechnique")
        tags += [self.tag("attack", "tactic", tactic) for tactic in tactics]
        tags += [self.tag("platform", platform) for platform in technique.platforms]
        tags += [self.tag("attack", "permission", permission) for permission in technique.permissions_required]
        if procedures:
            tags.append("attack/has_procedures")
        if mitigations:
            tags.append("attack/mitigated")
        if subtechniques:
            tags.append("attack/has_subtechniques")
        return sorted(set(tags))

    def mitigation_tags(self):
        return sorted(set(self.base_tags() + ["attack/type/mitigation"]))

    def group_tags(self):
        return sorted(set(self.base_tags() + ["attack/type/group"]))

    def software_tags(self):
        return sorted(set(self.base_tags() + ["attack/software/tool", "attack/type/software"]))

    def _build_object_index(self):
        objects_by_id = {}
        for obj in self.tactics + self.techniques + self.mitigations + self.groups + self.software:
            if hasattr(obj, "id"):
                objects_by_id[obj.id] = obj
        return objects_by_id

    @staticmethod
    def note_filename(obj):
        name = re.sub(r'\s+', '_', obj.name)
        name = re.sub(r'[^A-Za-z0-9._-]+', '_', name)
        name = re.sub(r'_+', '_', name).strip('_.-')
        return f"{obj.id}-{name or 'Unnamed'}.md"

    def note_path(self, note_type, obj):
        return f"{self.vault_relative_root}/{note_type}/{self.note_filename(obj)}"

    def note_stem(self, note_type, obj):
        return re.sub(r'\.md$', '', self.note_path(note_type, obj))

    def note_link(self, note_type, obj, alias=None):
        alias = alias or obj.id
        return f"[[{self.note_stem(note_type, obj)}\\|{alias}]]"

    def _internal_attack_link(self, attack_id, label=None):
        obj = self.objects_by_id.get(attack_id)
        if not obj:
            return label or attack_id

        if attack_id.startswith("TA"):
            note_type = "tactics"
        elif attack_id.startswith("T"):
            note_type = "techniques"
        elif attack_id.startswith("M"):
            note_type = "mitigations"
        elif attack_id.startswith("G"):
            note_type = "groups"
        elif attack_id.startswith("S"):
            note_type = "software"
        else:
            return label or attack_id

        return self.note_link(note_type, obj, label or attack_id)

    def local_mitre_attack(self, url):
        match = re.search(r'attack\.mitre\.org/(tactics|techniques|mitigations|groups|software)/([^)/#]+)(?:/([^)/#]+))?', url or '')
        if not match:
            return ''

        attack_id = match.group(2)
        if match.group(3):
            attack_id = f"{attack_id}.{match.group(3)}"

        obj = self.objects_by_id.get(attack_id)
        if not obj:
            return attack_id

        if match.group(1) == "tactics":
            note_type = "tactics"
        elif match.group(1) == "techniques":
            note_type = "techniques"
        elif match.group(1) == "mitigations":
            note_type = "mitigations"
        elif match.group(1) == "groups":
            note_type = "groups"
        else:
            note_type = "software"

        return self.note_stem(note_type, obj)

    def parse_description(self, description, references=[]):
        description = description.replace('\n', '<br>')
        description = description.replace('</code>', '`')
        description = description.replace('<code>', '`')

        for ref in references:
            description = re.sub(fr'\(Citation: {ref["source_name"]}\)', f'[^{ref["id"]}] ', description)
        description = re.sub(
            r'\[([^\]]+)\]\(https://attack\.mitre\.org/(?:tactics|techniques|mitigations|groups|software)/([^)/#]+)(?:/([^)/#]+))?/?\)',
            lambda match: self._internal_attack_link(
                f"{match.group(2)}.{match.group(3)}" if match.group(3) else match.group(2),
                match.group(1)
            ),
            description
        )
        description = re.sub(r'\[([^\]]+)\]\(https?://[^)]+\)', r'\1', description)
        description = re.sub(r'https?://\S+', '', description)
        return description

    def create_tactic_notes(self):
        template = self.environment.get_template("tactic.md")
        tactics_dir = os.path.join(self.output_dir, "tactics")
        if not os.path.exists(tactics_dir):
            os.makedirs(tactics_dir, exist_ok=True)

        for tactic in self.tactics:
            for ref in tactic.references:
                if ref[0] == 'mitre-attack':
                    mitre_attack = ref[1]

            techniques = []
            for technique in self.techniques:
                for kill_chain in technique.kill_chain_phases:
                    if kill_chain["kill_chain_name"] in ('mitre-attack', 'mitre-mobile-attack', 'mitre-ics-attack') and tactic.name.lower().replace(' ', '-') == kill_chain["phase_name"].lower():
                        techniques.append({
                            "name": technique.name,
                            "id": technique.id,
                            "link": self.note_link("techniques", technique),
                            "description": technique.description
                        })
                        break

            content = template.render(
                    aliases = [tactic.id],
                    tags = self.tactic_tags(),
                    mitre_attack = self.local_mitre_attack(mitre_attack),
                    title = tactic.id,
                    description = tactic.description,
                    techniques = self.sort_by_id(techniques)
            )
            tactic_file = os.path.join(tactics_dir, self.note_filename(tactic))

            with open(tactic_file, 'w', encoding="utf-8") as fd:
                fd.write(content)


    def create_technique_notes(self):
        template = self.environment.get_template("technique.md")
        techniques_dir = os.path.join(self.output_dir, "techniques")
        if not os.path.exists(techniques_dir):
            os.makedirs(techniques_dir, exist_ok=True)

        for technique in self.techniques:
            footnote_id = 1
            references = {}
            for ref in technique.references:
                if ref[0] == 'mitre-attack':
                    mitre_attack = ref[1]
                    continue
                source_name = ref[0]
                if source_name not in references:
                    references[source_name] = {
                        'id': footnote_id,
                        'url': ref[1]
                    }
                    footnote_id += 1

            tactics = []
            for kill_chain in technique.kill_chain_phases:
                if kill_chain["kill_chain_name"] in ('mitre-attack', 'mitre-mobile-attack', 'mitre-ics-attack'):
                    tactics += [ t.name for t in self.tactics if t.name.lower().replace(' ', '-') == kill_chain["phase_name"].lower() ]

            procedures = self.sort_by_id([{"name": sw["software"].name,
                         "id": sw["software"].id,
                         "link": self.note_link("software", sw["software"]),
                         "description": sw["description"]} for sw in technique.software] +
                         [{"name": g["group"].name,
                         "id": g["group"].id,
                         "link": self.note_link("groups", g["group"]),
                         "description": g["description"]} for g in technique.groups])
            mitigations = self.sort_by_id([{"name": m["mitigation"].name,
                         "id": m["mitigation"].id,
                         "link": self.note_link("mitigations", m["mitigation"]),
                         "description": m["description"]} for m in technique.mitigations])
            subtechniques = self.sort_by_id([{"name": subt.name,
                              "id": subt.id,
                              "link": self.note_link("techniques", subt)}
                             for subt in self.techniques if subt.is_subtechnique and subt.id.startswith(f"{technique.id}.")])

            content = template.render(
                    aliases = [technique.id],
                    tags = self.technique_tags(technique, tactics, procedures, mitigations, subtechniques),
                    mitre_attack = self.local_mitre_attack(mitre_attack),
                    tactics = tactics,
                    platforms = technique.platforms,
                    permissions_required = technique.permissions_required,
                    title = technique.id,
                    description = technique.description,
                    procedures = procedures,
                    mitigations = mitigations,
                    subtechniques = subtechniques,
                    references = [{"id": value["id"],
                                   "source_name": source_name,
                                   "url": value["url"]} for source_name, value in references.items() ]
            )

            technique_file = os.path.join(techniques_dir, self.note_filename(technique))

            with open(technique_file, 'w', encoding="utf-8") as fd:
                fd.write(content)


    def create_mitigation_notes(self):
        template = self.environment.get_template("mitigation.md")
        
        mitigations_dir = os.path.join(self.output_dir, "mitigations")
        if not os.path.exists(mitigations_dir):
            os.makedirs(mitigations_dir, exist_ok=True)

        for mitigation in self.mitigations:
            mitigation_file = os.path.join(mitigations_dir, self.note_filename(mitigation))

            footnote_id = 1
            references = {}
            for ref in mitigation.references:
                if ref[0] == 'mitre-attack':
                    mitre_attack = ref[1]
                    continue
                source_name = ref[0]
                if source_name not in references:
                    references[source_name] = {
                        'id': footnote_id,
                        'url': ref[1]
                    }
                    footnote_id += 1

            content = template.render(
                    aliases = [mitigation.id],
                    tags = self.mitigation_tags(),
                    mitre_attack = self.local_mitre_attack(mitre_attack),
                    title = mitigation.id,
                    description = mitigation.description,
                    techniques = self.sort_by_id([{"name": t["technique"].name,
                                   "id": t["technique"].id,
                                   "link": self.note_link("techniques", t["technique"]),
                                   "description": t["description"]} for t in mitigation.mitigates ]),
                    references = [{"id": value["id"],
                                   "source_name": source_name,
                                   "url": value["url"]} for source_name, value in references.items() ]
            )
            with open(mitigation_file, 'w', encoding="utf-8") as fd:
                fd.write(content)


    def create_group_notes(self):
        template = self.environment.get_template("group.md")

        groups_dir = os.path.join(self.output_dir, "groups")
        if not os.path.exists(groups_dir):
            os.makedirs(groups_dir, exist_ok=True)

        for group in self.groups:
            group_file = os.path.join(groups_dir, self.note_filename(group))

            footnote_id = 1
            references = {}
            for ref in group.references:
                if ref[0] == 'mitre-attack':
                    mitre_attack = ref[1]
                    continue
                source_name = ref[0]
                if source_name not in references:
                    references[source_name] = {
                        'id': footnote_id,
                        'url': ref[1]
                    }
                    footnote_id += 1

            content = template.render(
                    aliases = group.aliases,
                    tags = self.group_tags(),
                    mitre_attack = self.local_mitre_attack(mitre_attack),
                    title = group.id,
                    description = group.description,
                    techniques = self.sort_by_id([{"name": t["technique"].name,
                                   "id": t["technique"].id,
                                   "link": self.note_link("techniques", t["technique"]),
                                   "description": t["description"]} for t in group.techniques_used]),
                    software = self.sort_by_id([{"name": s["software"].name,
                                 "id": s["software"].id,
                                 "link": self.note_link("software", s["software"]),
                                 "description": s["description"]} for s in group.software_used]),
                    references = [{"id": value["id"],
                                   "source_name": source_name,
                                   "url": value["url"]} for source_name, value in references.items() ]
            )
            with open(group_file, 'w', encoding="utf-8") as fd:
                fd.write(content)

    def create_software_notes(self):
        template = self.environment.get_template("software.md")

        software_dir = os.path.join(self.output_dir, "software")
        if not os.path.exists(software_dir):
            os.makedirs(software_dir, exist_ok=True)


        for software in self.software:
            footnote_id = 1
            references = {}
            for ref in software.references:
                if ref[0] == 'mitre-attack':
                    mitre_attack = ref[1]
                    continue
                source_name = ref[0]
                if source_name not in references:
                    references[source_name] = {
                        'id': footnote_id,
                        'url': ref[1]
                    }
                    footnote_id += 1

            techniques_used = []
            for tech in software.techniques_used:
                techniques_used.append({
                    'name': tech["technique"].name,
                    'id': tech["technique"].id,
                    'link': self.note_link("techniques", tech["technique"]),
                    'description': tech["description"]
                })
            groups = []
            for group in software.groups:
                groups.append({
                        'name': group["group"].name,
                        'id': group["group"].id,
                        'link': self.note_link("groups", group["group"]),
                        'description': group["description"]
                    })

            content = template.render(
                    aliases = [software.id],
                    tags = self.software_tags(),
                    mitre_attack = self.local_mitre_attack(mitre_attack),
                    title = software.id,
                    description = software.description,
                    techniques = self.sort_by_id(techniques_used),
                    groups = self.sort_by_id(groups),
                    references = [{"id": value["id"],
                                   "source_name": source_name,
                                   "url": value["url"]} for source_name, value in references.items() ]
            )
            software_file = os.path.join(software_dir, self.note_filename(software))

            with open(software_file, 'w', encoding="utf-8") as fd:
                fd.write(content)

    def create_canvas(self, canvas_name, filtered_techniques=[]):
        canvas = {
                "nodes": [],
                "edges": []
            }

        x = 0
        width = 450
        columns = {tactic.name: index * 500 for index, tactic in enumerate(self.tactics)}


        rows = dict()
        height = 144
        y = 50
        max_height = y
        for technique in self.techniques:
            if technique.id in filtered_techniques or len(filtered_techniques) == 0:
                if not technique.is_subtechnique:
                    for kill_chain in technique.kill_chain_phases:
                        if kill_chain["kill_chain_name"] in ('mitre-attack', 'mitre-mobile-attack', 'mitre-ics-attack'):
                            tactic = [ t for t in self.tactics if t.name.lower().replace(' ', '-') == kill_chain["phase_name"].lower() ]
                            if tactic and len(tactic) > 0: 
                                if tactic[0].name in rows.keys():
                                    y = rows[tactic[0].name]
                                else:
                                    y = 50
                                    rows[tactic[0].name] = y
                                x = columns[tactic[0].name] + 20

                    technique_note_path = self.note_path("techniques", technique)
                    technique_node = {
                                "type": "file",
                                "file": technique_note_path,
                                "id": uuid.uuid4().hex,
                                "x": x,
                                "y": y,
                                "width": 450,
                                "height": height
                            }
                    canvas["nodes"].append(technique_node)
                    y = y + height + 20
                    subtechniques = [ subt for subt in self.techniques if subt.is_subtechnique and subt.id.startswith(f"{technique.id}.") ]
                    if subtechniques:
                        for subt in subtechniques:
                            subtech_note_path = self.note_path("techniques", subt)
                            subtech_node = {
                                        "type": "file",
                                        "file": subtech_note_path,
                                        "id": uuid.uuid4().hex,
                                        "x": x + 50,
                                        "y": y,
                                        "width": 400,
                                        "height": height
                                    }
                            y = y + height + 20
                            canvas["nodes"].append(subtech_node)
                    
                    rows[tactic[0].name] = y
                    if y > max_height:
                        max_height = y

        for tactic in self.tactics:
            container_node = {
                        "type": "group",
                        "label": f"{tactic.name}",
                        "id": uuid.uuid4().hex,
                        "x": columns[tactic.name],
                        "y": 0,
                        "width": 500,
                        "height": max_height + 20
                    }
            canvas["nodes"].append(container_node)
                        
            
        with open(f"{canvas_name}.canvas", 'w', encoding="utf-8") as fd:
            fd.write(json.dumps(canvas, indent=2))

    def create_index(self):
        index_file = os.path.join(self.output_dir, "index.md")
        lines = [
            "---",
            "tags:",
            "    - attack/type/index",
            f"    - {self.tag('attack', 'domain', self.domain)}",
            "---",
            "",
            "# MITRE ATT&CK",
            "",
        ]

        sections = [
            ("Tactics", "tactics", self.tactics),
            ("Mitigations", "mitigations", self.mitigations),
            ("Groups", "groups", self.groups),
            ("Software", "software", self.software),
        ]

        for title, note_type, objects in sections:
            if not objects:
                continue
            lines.append(f"- {title}")
            for obj in sorted(objects, key=lambda item: item.id):
                lines.append(f"  - {self.note_link(note_type, obj, f'{obj.id} {obj.name}')}")

        if self.techniques:
            lines.append("- Techniques")
            parent_techniques = sorted(
                [technique for technique in self.techniques if not technique.is_subtechnique],
                key=lambda item: item.id
            )
            for technique in parent_techniques:
                lines.append(f"  - {self.note_link('techniques', technique, f'{technique.id} {technique.name}')}")
                subtechniques = sorted(
                    [subt for subt in self.techniques if subt.is_subtechnique and subt.id.startswith(f"{technique.id}.")],
                    key=lambda item: item.id
                )
                for subtechnique in subtechniques:
                    lines.append(f"    - {self.note_link('techniques', subtechnique, f'{subtechnique.id} {subtechnique.name}')}")

        with open(index_file, 'w', encoding="utf-8") as fd:
            fd.write("\n".join(lines) + "\n")
            
