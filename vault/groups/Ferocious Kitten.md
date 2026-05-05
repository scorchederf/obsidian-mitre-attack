---
aliases: 
    - Ferocious Kitten
mitre-attack: https://attack.mitre.org/groups/G0137
---

## G0137

[Ferocious Kitten](https://attack.mitre.org/groups/G0137) is a threat group that has primarily targeted Persian-speaking individuals in Iran since at least 2015.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has attempted to convince victims to enable malicious content within a spearphishing email by including an odd decoy message.[^1]  |
| [[Right-to-Left Override\|T1036.002]] | Right-to-Left Override | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has used right-to-left override to reverse executables’ names to make them appear to have different file extensions, rather than their real ones.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has named malicious files `update.exe` and loaded them into the compromise host's “Public” folder.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has conducted spearphishing campaigns containing malicious documents to lure victims to open the attachments.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has obtained open source tools for its operations, including JsonCPP and Psiphon.[^1]  |
| [[Domains\|T1583.001]] | Domains | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has acquired domains imitating legitimate sites.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^1]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [^1]  |



## References

[^1]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


