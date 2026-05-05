---
aliases: {% for alias in aliases %}
    - {{alias}}{% endfor %}
tags: {% for tag in tags %}
    - {{tag}}{% endfor %}
mitre-attack: {{mitre_attack}}
tactic: 
    {% for tactic in tactics %} - {{tactic}}{% endfor %}
platforms:
    {% for plat in platforms %} - {{plat}}{% endfor %}
permissions required:
    {% if permissions_required %}
    {% for perm in permissions_required %} - {{perm}}{% endfor %}
    {% else %} - none{% endif %}
---

## Description

{{description | parse_description(references)}}

{% if procedures %}
## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
{% for procedure in procedures %}| {{procedure['link']}} | {{procedure['name']}} | {{ procedure['description'] | parse_description(references) }} |
{% endfor %}
{% endif %}

{% if mitigations %}
## Mitigations
| ID | Name | Description |
| --- | --- | --- |
{% for mit in mitigations %}| {{mit['link']}} | {{mit['name']}} | {{mit['description'] | parse_description(references)}} |
{% endfor %}
{% endif %}

{% if subtechniques %}
## Sub-techniques
| ID | Name |
| --- | --- |
{% for sbt in subtechniques %}| {{sbt['link']}} | {{sbt['name']}} |
{% endfor %}
{% endif %}

{% if references %}
> [!info]- References
{% for ref in references %}{% if ref['url'] %}> [^{{ref['id']}}]: [{{ref['source_name']}}]({{ref['url']}})
{% else %}> [^{{ref['id']}}]: {{ref['source_name']}}
{% endif %}
{% endfor %}
{% endif %}
