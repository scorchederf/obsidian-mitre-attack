---
aliases: 
    - ZIRCONIUM
    - APT31
    - Violet Typhoon
mitre-attack: https://attack.mitre.org/groups/G0128
---

## G0128

[ZIRCONIUM](https://attack.mitre.org/groups/G0128) is a threat group operating out of China, active since at least 2017, that has targeted individuals associated with the 2020 US presidential election and prominent leaders in the international affairs community.[^8] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the processor architecture of a compromised host in order to register it with C2.[^7]  |
| [[Phishing for Information\|T1598]] | Phishing for Information | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) targeted presidential campaign staffers with credential phishing e-mails.[^9]  |
| [[Query Registry\|T1012]] | Query Registry | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to query the Registry for proxy settings.[^7]  |
| [[Hide Infrastructure\|T1665]] | Hide Infrastructure | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has utilized an ORB (operational relay box) network – consisting compromised devices such as small office and home office (SOHO) routers, IoT devices, and leased virtual private servers (VPS) – to obfuscate the origin of C2 traffic.[^3]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to open a Windows Command Shell on a remote host.[^7]  |
| [[Web Services\|T1583.006]] | Web Services | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used GitHub to host malware linked in spearphishing e-mails.[^9] [^7]  |
| [[Network Devices\|T1584.008]] | Network Devices | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has compromised network devices such as small office and home office (SOHO) routers and IoT devices for ORB (operational relay box) [Proxy](https://attack.mitre.org/techniques/T1090) networks.[^1] [^3]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to steal credentials from installed web browsers including Microsoft Internet Explorer and Google Chrome.[^7]  |
| [[Python\|T1059.006]] | Python | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used Python-based implants to interact with compromised hosts.[^9] [^7]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has created a Registry Run key named `Dropbox Update Setup` to establish persistence for a malicious Python binary.[^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used AES encrypted communications in C2.[^7]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the time on a compromised host in order to register it with C2.[^7]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used the AES256 algorithm with a SHA1 derived key to decrypt exploit code.[^2]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used web beacons in e-mails to track hits to attacker-controlled URL's.[^8]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used malicious links in e-mails to deliver malware.[^8] [^9] [^7]  |
| [[Domains\|T1583.001]] | Domains | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has purchased domains for use in targeted campaigns.[^8]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the username on a compromised host in order to register it with C2.[^7]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has utilized an ORB (operational relay box) network – consisting compromised devices such as small office and home office (SOHO) routers, IoT devices, and leased virtual private servers (VPS) – to proxy traffic.[^3]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exfiltrated files via the Dropbox API C2.[^7]  |
| [[Masquerading\|T1036]] | Masquerading | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has spoofed legitimate applications in phishing lures and changed file extensions to conceal  installation of malware.[^9] [^7]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exfiltrated stolen data to Dropbox.[^7]  |
| [[Software Packing\|T1027.002]] | Software Packing | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used multi-stage packers for exploit code.[^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used malicious links in e-mails to lure victims into downloading malware.[^9] [^7]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has created a run key named `Dropbox Update Setup` to mask a persistence mechanism for a malicious binary.[^7]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exploited CVE-2017-0005 for local privilege escalation.[^2]  |
| [[Msiexec\|T1218.007]] | Msiexec | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used the msiexec.exe command-line utility to download and execute malicious MSI files.[^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used tools to download malicious files to compromised hosts.[^7]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to enumerate proxy settings in the target environment.[^7]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used Dropbox for C2 allowing upload and download of files as well as execution of arbitrary commands.[^9] [^7]  |




## References

[^1]: [ORB APT31](https://therecord.media/chinese-hacking-group-apt31-uses-mesh-of-home-routers-to-disguise-attacks)


[^2]: [Check Point APT31 February 2021](https://research.checkpoint.com/2021/the-story-of-jian/)


[^3]: [ORB Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks)


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: Violet Typhoon


[^6]: APT31


[^7]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^8]: [Microsoft Targeting Elections September 2020](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)


[^9]: [Google Election Threats October 2020](https://blog.google/threat-analysis-group/how-were-tackling-evolving-online-threats/)


