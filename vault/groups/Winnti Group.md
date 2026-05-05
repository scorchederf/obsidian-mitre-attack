---
aliases: 
    - Winnti Group
    - Blackfly
mitre-attack: https://attack.mitre.org/groups/G0044
---

## G0044

[Winnti Group](https://attack.mitre.org/groups/G0044) is a threat group with Chinese origins that has been active since at least 2010. The group has heavily targeted the gaming industry, but it has also expanded the scope of its targeting.[^3] [^2] [^4]  Some reporting suggests a number of other groups, including [Axiom](https://attack.mitre.org/groups/G0001), [APT17](https://attack.mitre.org/groups/G0025), and [Ke3chang](https://attack.mitre.org/groups/G0004), are closely linked to [Winnti Group](https://attack.mitre.org/groups/G0044).[^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Rootkit\|T1014]] | Rootkit | [Winnti Group](https://attack.mitre.org/groups/G0044) used a rootkit to modify typical server functionality.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Winnti Group](https://attack.mitre.org/groups/G0044) has downloaded an auxiliary program named ff.exe to infected machines.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Winnti Group](https://attack.mitre.org/groups/G0044) has used a program named ff.exe to search for specific documents on compromised hosts.[^3]  |
| [[Domains\|T1583.001]] | Domains | [Winnti Group](https://attack.mitre.org/groups/G0044) has registered domains for C2 that mimicked sites of their intended targets.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Winnti Group](https://attack.mitre.org/groups/G0044) looked for a specific process running on infected servers.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Winnti Group](https://attack.mitre.org/groups/G0044) used stolen certificates to sign its malware.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PlugX\|S0013]] | PlugX | [^3]  |
| [[PipeMon\|S0501]] | PipeMon | [^5]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [^3] [^2]  |



## References

[^1]: Winnti Group


[^2]: [Kaspersky Winnti June 2015](https://securelist.com/games-are-over/70991/)


[^3]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^4]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^5]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^6]: Blackfly


[^7]: [401 TRG Winnti Umbrella May 2018](https://401trg.github.io/pages/burning-umbrella.html)


[^8]: [Symantec Suckfly March 2016](http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates)


