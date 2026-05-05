---
aliases: 
    - Moonstone Sleet
    - Storm-1789
mitre-attack: https://attack.mitre.org/groups/G1036
---

## G1036

[Moonstone Sleet](https://attack.mitre.org/groups/G1036) is a North Korean-linked threat actor executing both financially motivated attacks and espionage operations. The group previously overlapped significantly with another North Korean-linked entity, [Lazarus Group](https://attack.mitre.org/groups/G0032), but has differentiated its tradecraft since 2023. [Moonstone Sleet](https://attack.mitre.org/groups/G1036) is notable for creating fake companies and personas to interact with victim entities, as well as developing unique malware such as a variant delivered via a fully functioning game.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malware\|T1587.001]] | Malware | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has developed custom malware, including a malware delivery mechanism masquerading as a legitimate game.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) deployed various malware such as YouieLoader that can perform system user discovery actions.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used curl to connect to adversary-controlled infrastructure and retrieve additional payloads.[^2]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has created email accounts to interact with victims, including for phishing purposes.[^2]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) gathered victim email address information for follow-on phishing activity.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivered payloads using multiple rounds of obfuscation and encoding to evade defenses and analysis.[^2]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim organizations through email and social media interaction.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used scheduled tasks for program execution during initial access to victim machines.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used registry run keys for process execution during initial victim infection.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) relied on users interacting with malicious files, such as a trojanized PuTTY installer, for initial execution.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivered various payloads to victims as spearphishing attachments.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) delivers encrypted payloads in pieces that are then combined together to form a new portable executable (PE) file during installation.[^2]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) registered virtual private servers to host payloads for download.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) retrieved a final stage payload from command and control infrastructure during initial installation on victim systems.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim network configuration.[^2]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used spearphishing messages containing items such as tracking pixels to determine if users interacted with malicious messages.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) retrieved credentials from LSASS memory.[^2]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) staged malicious capabilities online for follow-on download by victims or malware.[^2]  |
| [[Phishing for Information\|T1598]] | Phishing for Information | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has interacted with victims to gather information via email.[^2]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has distributed a trojanized version of PuTTY software for initial access to victims.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) used intermediate loader malware such as YouieLoader and SplitLoader that create malicious services.[^2]  |
| [[Domains\|T1583.001]] | Domains | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) registered domains to develop effective personas for fake companies used in phishing activity.[^2]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) deployed malware such as YouieLoader capable of capturing victim system browser information.[^2]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has used social media services to spear phish victims to deliver trojainized software.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has deployed ransomware in victim environments.[^2]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has created social media accounts to interact with victims.[^2]  |
| [[Develop Capabilities\|T1587]] | Develop Capabilities | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) developed malicious npm packages for delivery to or retrieval by victims.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim systems.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has used encrypted payloads within files for follow-on execution and defense evasion.[^2]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) embedded payloads in trojanized software for follow-on execution.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Qilin\|S1242]] | Qilin | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has deployed [Qilin](https://attack.mitre.org/software/S1242) ransomware.[^3]  |



## References

[^1]: Storm-1789


[^2]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^3]: [MIcrosoft Moonstone Sleet Qilin MAR 2025](https://x.com/MsftSecIntel/status/1897738961348374621)


