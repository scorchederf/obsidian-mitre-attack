---
aliases: 
    - WIRTE
    - Ashen Lepus
mitre-attack: https://attack.mitre.org/groups/G0090
---

## G0090

[WIRTE](https://attack.mitre.org/groups/G0090) is a cyberespionage actor, believed to be a subgroup of the Hamas-affiliated Gaza Cybergang, that has been active since at least August 2018. [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. [WIRTE](https://attack.mitre.org/groups/G0090) has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.[^2] [^5] [^3] [^6] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [WIRTE](https://attack.mitre.org/groups/G0090) has used PowerShell for script execution.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [WIRTE](https://attack.mitre.org/groups/G0090) has used HTTPS over ports 2083 and 2087 for C2.[^5]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [WIRTE](https://attack.mitre.org/groups/G0090) has used VBScript  in its operations.[^2] 	 |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [WIRTE](https://attack.mitre.org/groups/G0090) has collected documents from victims' email accounts.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [WIRTE](https://attack.mitre.org/groups/G0090) has attempted to lure users into opening malicious documents including MS Word and Excel files, at times using a decoy document to encourage execution of malicious payloads.[^5] [^3] [^6]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [WIRTE](https://attack.mitre.org/groups/G0090) has directed victims to malicious payloads staged on file sharing services.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WIRTE](https://attack.mitre.org/groups/G0090) has used Base64 to decode malicious VBS script.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [WIRTE](https://attack.mitre.org/groups/G0090) has sent emails to intended victims with malicious MS Word and Excel attachments.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WIRTE](https://attack.mitre.org/groups/G0090) has used the Windows command line as part of infection chains to open documents.[^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [WIRTE](https://attack.mitre.org/groups/G0090) has used links embedded in emails to lure users into downloading malicious files.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [WIRTE](https://attack.mitre.org/groups/G0090) has used security service provider naming conventions such as ESET and Kasperky ("Kaspersky Update Agent") in order to appear legitimate.[^5] [^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [WIRTE](https://attack.mitre.org/groups/G0090) has staged collected documents of interest in `C:\Users\Public folder`.[^6]  |
| [[Tool\|T1588.002]] | Tool | [WIRTE](https://attack.mitre.org/groups/G0090) has obtained and used [Empire](https://attack.mitre.org/software/S0363) and [Rclone](https://attack.mitre.org/software/S1040) for post-exploitation activities.[^2] [^6]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [WIRTE](https://attack.mitre.org/groups/G0090) has used compromised emails, including one belonging to an Israel-based technology reseller, to deliver targeted spearphishing messages.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [WIRTE](https://attack.mitre.org/groups/G0090) has exfiltrated collected victim data to C2 infrastructure.[^6]  |
| [[Domains\|T1583.001]] | Domains | [WIRTE](https://attack.mitre.org/groups/G0090) has registered domains designed to mimic legitimate sites for use in phishing campaigns.[^3] [^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WIRTE](https://attack.mitre.org/groups/G0090) has used HTTP for network communication.[^2] 	 |
| [[DLL\|T1574.001]] | DLL | [WIRTE](https://attack.mitre.org/groups/G0090) has used RAR archives containing a legitimate executable and a lure document to execute malicious DLLs via sideloading.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [WIRTE](https://attack.mitre.org/groups/G0090) has configured C2 servers to check location and user-agent strings for victim endpoints to prevent sending a payload to sandboxed environments.[^6]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [WIRTE](https://attack.mitre.org/groups/G0090) has sent targeted spearphishing emails with malicious links directing victims to malware downloads.[^3]  |
| [[Impersonation\|T1684.001]] | Impersonation | [WIRTE](https://attack.mitre.org/groups/G0090) has used utilized look-alike domains and graphics of trusted security solution providers to entice victims to click on phishing links.[^3]  |
| [[Native API\|T1106]] | Native API | [WIRTE](https://attack.mitre.org/groups/G0090) has used the `RtlIpv4StringToAddressA` to convert IP-formatted string to a byte array.[^3] <br> |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [WIRTE](https://attack.mitre.org/groups/G0090) has used `regsvr32.exe` to trigger the execution of a malicious script.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WIRTE](https://attack.mitre.org/groups/G0090) has downloaded PowerShell code from the C2 server to be executed.[^2]  |
| [[Compression\|T1027.015]] | Compression | [WIRTE](https://attack.mitre.org/groups/G0090) has compressed malicious files within RAR and ZIP archives for obfuscation.  [^3] [^6]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [WIRTE](https://attack.mitre.org/groups/G0090) has XOR encrypted command line strings to conceal malware execution chains.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [^2]  |
| [[Rclone\|S1040]] | Rclone | [WIRTE](https://attack.mitre.org/groups/G0090) has used [Rclone](https://attack.mitre.org/software/S1040) for document exfiltration.[^6]  |
| [[IronWind\|S9029]] | IronWind | [^3]  |
| [[Havoc\|S1229]] | Havoc | [WIRTE](https://attack.mitre.org/groups/G0090) has used [Havoc](https://attack.mitre.org/software/S1229) to maintain access and to facilitate C2.[^3]  |
| [[SameCoin\|S9030]] | SameCoin | [^3]  |
| [[Ferocious\|S0679]] | Ferocious | [^5]  |
| [[LitePower\|S0680]] | LitePower | [^5]  |
| [[AshTag\|S9031]] | AshTag | [^6]  |



## References

[^1]: WIRTE


[^2]: [Lab52 WIRTE Apr 2019](https://lab52.io/blog/wirte-group-attacking-the-middle-east/)


[^3]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^4]: Ashen Lepus


[^5]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^6]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


