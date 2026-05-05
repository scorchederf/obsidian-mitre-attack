---
aliases: {% for alias in aliases %}
    - {{alias}}{% endfor %}
tags: {% for tag in tags %}
    - {{tag}}{% endfor %}
mitre-attack: {{mitre_attack}}
---

## Description

{{description | parse_description(references)}}

## Techniques Used
| ID | Name | Description |
| --- | --- | --- |
{% for technique in techniques %}| {{technique['link']}} | {{technique['name']}} | {{ technique['description'] | parse_description(references) }} |
{% endfor %}

{% if software %}
## Software
| ID | Name | Description |
| --- | --- | --- |
{% for sw in software %}| {{sw['link']}} | {{sw['name']}} | {{sw['description'] | parse_description(references) }} |
{% endfor %}
{% endif %}

{% if references %}
> [!info]- References
{% for ref in references %}{% if ref['url'] %}> [^{{ref['id']}}]: [{{ref['source_name']}}]({{ref['url']}})
{% else %}> [^{{ref['id']}}]: {{ref['source_name']}}
{% endif %}
{% endfor %}
{% endif %}
