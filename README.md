# obsidian-mitre-attack

This repository contains a Python generator that converts MITRE ATT&CK STIX data into
Markdown notes for Obsidian.

The ATT&CK data is retrieved from the MITRE ATT&CK STIX data repository:
https://github.com/mitre-attack/attack-stix-data. The generator reads the STIX 2.1
JSON collection and writes a browsable knowledge base with Obsidian links, tags,
indexes, graph settings, and ATT&CK canvas output.

The main idea behind this project is to make the MITRE ATT&CK knowledge base easily accessible and seamlessly integrable into Obsidian, along with reports or your personal notes. Utilizing Obsidian's features such as hyperlinks, tags, graph view, and more can greatly support threat intelligence analysis and investigations.

## Repository Layout

```
.
+-- config.yml              # Data source, ATT&CK version, and object type settings
+-- run.py                  # CLI entry point
+-- requirements.txt        # Runtime Python dependencies
+-- res/
|   +-- graph.json          # Obsidian graph configuration copied to generated vaults
|   +-- templates/          # Jinja2 templates for generated Markdown notes
+-- src/
|   +-- markdown_generator.py
|   +-- markdown_reader.py
|   +-- models.py
|   +-- stix_parser.py
|   +-- view.py
+-- vault/                  # Example/generated Obsidian vault content
```

Generated ATT&CK notes are written below `kb/mitre/attack` inside the output vault.
The generator currently supports tactics, techniques, mitigations, groups, and
software objects.

## Quick Start

### Installation

Clone this repository:

```
git clone https://github.com/vincenzocaputo/obsidian-mitre-attack.git
```

Create and activate a Python virtual environment:

```
cd obsidian-mitre-attack
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```
pip install -r requirements.txt
```

### Run

#### Edit the config file (Optional)

> **It is recommended to use the default config file.**

In the `config.yml` file, you can change the following options:

- **repository-url**: The base URL pointing to the mitre/attack-stix-data repository. You can define also a local file path or other URLs. However, remember that this project is intended to parse data from the MITRE ATT&CK framework. Providing different JSON files may break the script execution.
- **version**: The ATT&CK version to pull. You can remove this entry to pull the latest version. Please note that newer versions may not have been tested and some errors may occur. In case of an error, do not hesitate to open a problem.
- **mitre-object-types**: This option lists all the type of MITRE objects that are parsed by the script. You can set to `false` the options corresponding to the types of objects for which you don't want to create markdown notes in your vault.

#### Run the script

Run the application and pass the output directory path, such as an existing
Obsidian vault:

```
python run.py -o obsidian_vault_path
```

If the directory does not exist, the script creates it. Generated files are placed
under `obsidian_vault_path/kb/mitre/attack`.

### Options

```
usage: . [-h] [-d DOMAIN] [-o OUTPUT] [--generate-hyperlinks] [--generate-matrix] [--path PATH]

Download MITRE ATT&CK STIX data and parse it to Obsidian markdown notes

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain should be 'enterprise-attack', 'mobile-attack' or 'ics-attack'
  -o OUTPUT, --output OUTPUT
                        Output directory in which the notes will be saved. It should be placed inside a Obsidian
                        vault.
  --generate-hyperlinks
                        Generate techniques hyperlinks in a markdown note file
  --generate-matrix     Create ATT&CK matrix starting from a markdown note file
  --path PATH           Filepath to the markdown note file
```

### Examples

Generate the default Enterprise ATT&CK vault content:

```
python run.py -o vault
```

Generate Mobile ATT&CK content:

```
python run.py --domain mobile-attack -o vault
```

Generate an ATT&CK matrix canvas from a note containing technique IDs:

```
python run.py --generate-matrix --path path/to/note.md
```

Replace plain technique IDs in a Markdown note with Obsidian links:

```
python run.py --generate-hyperlinks --path path/to/note.md
```

## Generated Content

The Markdown generator creates:

- Tactic, technique, mitigation, group, and software notes.
- An `index.md` page linking generated ATT&CK objects.
- Obsidian tags for ATT&CK domains, object types, tactics, platforms, and permissions.
- Internal Obsidian links for supported ATT&CK object references.
- A `mitre-attack.canvas` file when tactics and techniques are enabled.
- `.obsidian/graph.json` graph settings copied from `res/graph.json`.

Treat generated vault content as reproducible output. Prefer changing parser logic
or Jinja2 templates instead of hand-editing generated notes when the same change
should survive regeneration.

## Development

This project is intentionally small and has no package metadata or configured test
runner yet. Use the following checks before opening a change:

```
python3 -m py_compile run.py src/*.py
python run.py --help
```

For changes that affect generated Markdown, run the generator against a temporary
or sample vault and inspect the resulting files in Obsidian or with `git diff`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for coding style and contribution guidance.


## Images and Examples

![immagine](https://github.com/vincenzocaputo/obsidian-mitre-attack/assets/32276363/f9e3aa4d-fdae-44b7-9036-616ed9f61d69)

![immagine](https://github.com/vincenzocaputo/obsidian-mitre-attack/assets/32276363/67b600e4-9928-494e-ac55-bd1e2e2f1ddd)

![image](https://github.com/user-attachments/assets/b34ed6fa-b799-4e53-986a-f43d9c09bd57)

![image](https://github.com/user-attachments/assets/b642d906-f280-4899-87cb-95f69db2249b)

