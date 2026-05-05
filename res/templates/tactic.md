---
aliases: {% for alias in aliases %}
    - {{alias}}
    {% endfor %}
tags: {% for tag in tags %}
    - {{tag}}
    {% endfor %}
mitre-attack: {{mitre_attack}}
---

## Description

{{description | parse_description}}

{% if techniques %}
## Techniques
| ID | Name | Description |
| --- | --- | --- |
{% for technique in techniques %}| {{technique['link']}} | {{technique['name']}} | {{ technique['description'] | parse_description }} |
{% endfor %}
{% endif %}
