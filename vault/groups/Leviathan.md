---
aliases: 
    - Leviathan
    - MUDCARP
    - Kryptonite Panda
    - Gadolinium
    - BRONZE MOHAWK
    - TEMP.Jumper
    - APT40
    - TEMP.Periscope
    - Gingham Typhoon
mitre-attack: https://attack.mitre.org/groups/G0065
---

## G0065

[Leviathan](https://attack.mitre.org/groups/G0065) is a Chinese state-sponsored cyber espionage group that has been attributed to the Ministry of State Security's (MSS) Hainan State Security Department and an affiliated front company.[^9]  Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.[^9] [^5] [^1] [^11] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Leviathan](https://attack.mitre.org/groups/G0065) has used an uploader known as LUNCHMONEY that can exfiltrate files to Dropbox.[^5] [^1]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Leviathan](https://attack.mitre.org/groups/G0065) has conducted reconnaissance against target networks of interest looking for vulnerable, end-of-life, or no longer maintainted devices against which to rapidly deploy exploits.[^11]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [Leviathan](https://attack.mitre.org/groups/G0065) has received C2 instructions from user profiles created on legitimate websites such as Github and TechNet.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Leviathan](https://attack.mitre.org/groups/G0065) has used WMI for execution.[^5]  |
| [[SSH\|T1021.004]] | SSH | [Leviathan](https://attack.mitre.org/groups/G0065) used ssh for internal reconnaissance.[^14]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Leviathan](https://attack.mitre.org/groups/G0065) has downloaded additional scripts and files from adversary-controlled servers.[^5] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Leviathan](https://attack.mitre.org/groups/G0065) has used JavaScript to create a shortcut file in the Startup folder that points to its main backdoor.[^5] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Leviathan](https://attack.mitre.org/groups/G0065) has obfuscated code using base64.[^5]  |
| [[Credentials\|T1589.001]] | Credentials | [Leviathan](https://attack.mitre.org/groups/G0065) has collected compromised credentials to use for targeting efforts.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Leviathan](https://attack.mitre.org/groups/G0065) has used publicly available tools to dump password hashes, including ProcDump and WCE.[^14]  |
| [[Social Media Accounts\|T1586.001]] | Social Media Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has compromised social media accounts to conduct social engineering attacks.[^9]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Leviathan](https://attack.mitre.org/groups/G0065) has used multi-hop proxies to disguise the source of their malicious traffic.[^9]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Leviathan](https://attack.mitre.org/groups/G0065) has inserted garbage characters into code, presumably to avoid anti-virus detection.[^5]  |
| [[Domains\|T1583.001]] | Domains | [Leviathan](https://attack.mitre.org/groups/G0065) has established domains that impersonate legitimate entities to use for targeting efforts. [^9] [^10]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has created new email accounts for targeting efforts.[^9]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing emails with links, often using a fraudulent lookalike domain and stolen branding.[^5] [^9]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Leviathan](https://attack.mitre.org/groups/G0065) has infected victims using watering holes.[^9]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Leviathan](https://attack.mitre.org/groups/G0065) has used WMI for persistence.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [Leviathan](https://attack.mitre.org/groups/G0065) has used steganography to hide stolen data inside other files stored on Github.[^9]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has created new social media accounts for targeting efforts.[^9]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Leviathan](https://attack.mitre.org/groups/G0065) has used PowerShell for execution.[^5] [^1] [^9] [^10]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Leviathan](https://attack.mitre.org/groups/G0065) has used JavaScript to create a shortcut file in the Startup folder that points to its main backdoor.[^5] [^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Leviathan](https://attack.mitre.org/groups/G0065) has utilized techniques like reflective DLL loading to write a DLL into memory and load a shell that provides backdoor access to the victim.[^10]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing emails with malicious attachments, including .rtf, .doc, and .xls files.[^5] [^9]  |
| [[Server\|T1584.004]] | Server | [Leviathan](https://attack.mitre.org/groups/G0065) has used compromised legitimate websites as command and control nodes for operations.[^11]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Leviathan](https://attack.mitre.org/groups/G0065) has exploited multiple Microsoft Office and .NET vulnerabilities for execution, including CVE-2017-0199, CVE-2017-8759, and CVE-2017-11882.[^5] [^1] [^9] [^10]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Leviathan](https://attack.mitre.org/groups/G0065) has used VBScript.[^5]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has obtained valid accounts to gain initial access.[^9] [^10] [^11]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Leviathan](https://attack.mitre.org/groups/G0065) has used stolen code signing certificates to sign malware.[^1] [^14]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Leviathan](https://attack.mitre.org/groups/G0065) has utilized OLE as a method to insert malicious content inside various phishing documents. [^10]  |
| [[Exploits\|T1587.004]] | Exploits | [Leviathan](https://attack.mitre.org/groups/G0065) has rapidly transformed and adapted public exploit proof-of-concept code for new vulnerabilities and utilized them against target networks.[^11]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Leviathan](https://attack.mitre.org/groups/G0065) has used [BITSAdmin](https://attack.mitre.org/software/S0190) to download additional tools.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Leviathan](https://attack.mitre.org/groups/G0065) has used C:\Windows\Debug and C:\Perflogs as staging directories.[^1] [^9]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing attachments attempting to get a user to click.[^5] [^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Leviathan](https://attack.mitre.org/groups/G0065) has used a DLL known as SeDll to decrypt and execute other JavaScript backdoors.[^5]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [Leviathan](https://attack.mitre.org/groups/G0065) has staged data remotely prior to exfiltration.[^9]  |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [Leviathan](https://attack.mitre.org/groups/G0065) has conducted internal spearphishing within the victim's environment for lateral movement.[^9]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Leviathan](https://attack.mitre.org/groups/G0065) has used exploits against publicly-disclosed vulnerabilities for initial access into victim networks.[^11]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Leviathan](https://attack.mitre.org/groups/G0065) has used regsvr32 for execution.[^5]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Leviathan](https://attack.mitre.org/groups/G0065) has exfiltrated data over its C2 channel.[^9]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Leviathan](https://attack.mitre.org/groups/G0065) relies on web shells for an initial foothold as well as persistence into the victim's systems.[^14] [^9] [^11]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Leviathan](https://attack.mitre.org/groups/G0065) has targeted RDP credentials and used it to move through the victim environment.[^14]   |
| [[Network Devices\|T1584.008]] | Network Devices | [Leviathan](https://attack.mitre.org/groups/G0065) has used compromised networking devices, such as small office/home office (SOHO) devices, as operational command and control infrastructure.[^11]  |
| [[Compression\|T1027.015]] | Compression | [Leviathan](https://attack.mitre.org/groups/G0065) has obfuscated code using gzip compression.[^5]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Leviathan](https://attack.mitre.org/groups/G0065) has archived victim's data prior to exfiltration.[^9]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Leviathan](https://attack.mitre.org/groups/G0065) has used protocol tunneling to further conceal C2 communications and infrastructure.[^9]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing email links attempting to get a user to click.[^5] [^9]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Leviathan](https://attack.mitre.org/groups/G0065) has used external remote services such as virtual private networks (VPN) to gain initial access.[^9]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Leviathan](https://attack.mitre.org/groups/G0065) has used publicly available tools to dump password hashes, including [HOMEFRY](https://attack.mitre.org/software/S0232).[^14]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has compromised email accounts to conduct social engineering attacks.[^9]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^14]  |
| [[at\|S0110]] | at | [^14]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^9]  |
| [[Windows Credential Editor\|S0005]] | Windows Credential Editor | [^14]  |
| [[Empire\|S0363]] | Empire | [^9]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^1]  |
| [[Tor\|S0183]] | Tor | [^9]  |
| [[MURKYTOP\|S0233]] | MURKYTOP | [^1] [^9]  |
| [[Orz\|S0229]] | Orz | [^5] [^9] [^10]  |
| [[BADFLICK\|S0642]] | BADFLICK | [^1] [^10]  |
| [[China Chopper\|S0020]] | China Chopper | [^1] [^9] [^10]  |
| [[NanHaiShu\|S0228]] | NanHaiShu | [^5] [^9]  |
| [[HOMEFRY\|S0232]] | HOMEFRY | [^1]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^9]  |
| [[Derusbi\|S0021]] | Derusbi | [^1] [^9]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^5] [^1] [^9]  |
| [[BLACKCOFFEE\|S0069]] | BLACKCOFFEE | [^1]  |



## References

[^1]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^2]: Gingham Typhoon


[^3]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^4]: [SecureWorks BRONZE MOHAWK n.d.](https://www.secureworks.com/research/threat-profiles/bronze-mohawk)


[^5]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^6]: TEMP.Jumper


[^7]: MUDCARP


[^8]: [Crowdstrike KRYPTONITE PANDA August 2018](https://www.crowdstrike.com/blog/two-birds-one-stone-panda/)


[^9]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^10]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^11]: [CISA Leviathan 2024](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)


[^12]: APT40


[^13]: Kryptonite Panda


[^14]: [FireEye APT40 March 2019](https://www.fireeye.com/blog/threat-research/2019/03/apt40-examining-a-china-nexus-espionage-actor.html)


[^15]: TEMP.Periscope


[^16]: Gadolinium


[^17]: BRONZE MOHAWK


[^18]: [MSTIC GADOLINIUM September 2020](https://www.microsoft.com/security/blog/2020/09/24/gadolinium-detecting-empires-cloud/)


[^19]: Leviathan


