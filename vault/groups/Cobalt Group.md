---
aliases: 
    - Cobalt Group
    - GOLD KINGSWOOD
    - Cobalt Gang
    - Cobalt Spider
mitre-attack: https://attack.mitre.org/groups/G0080
---

## G0080

[Cobalt Group](https://attack.mitre.org/groups/G0080) is a financially motivated threat group that has primarily targeted financial institutions since at least 2016. The group has conducted intrusions to steal money via targeting ATM systems, card processing, payment systems and SWIFT systems. [Cobalt Group](https://attack.mitre.org/groups/G0080) has mainly targeted banks in Eastern Europe, Central Asia, and Southeast Asia. One of the alleged leaders was arrested in Spain in early 2018, but the group still appears to be active. The group has been known to target organizations in order to use their access to then compromise additional victims.[^18] [^17] [^9] [^6] [^5] [^12] [^3]  Reporting indicates there may be links between [Cobalt Group](https://attack.mitre.org/groups/G0080) and both the malware [Carbanak](https://attack.mitre.org/software/S0030) and the group [Carbanak](https://attack.mitre.org/groups/G0008).[^11] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent spearphishing emails with various attachment types to corporate and personal email accounts of victim organizations. Attachment types have included .rtf, .doc, .xls, archives containing LNK files, and password protected archives containing .exe and .scr executables.[^18] [^17] [^9] [^6] [^5] [^12] [^4] [^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used public sites such as github.com and sendspace.com to upload files and then download them to victim computers.[^17] [^9]  The group's JavaScript backdoor is also capable of downloading files.[^15]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Cobalt Group](https://attack.mitre.org/groups/G0080) obfuscated several scriptlets and code used on the victim’s machine, including through use of XOR and RC4.[^18] [^15]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Cobalt Group](https://attack.mitre.org/groups/G0080) has created Windows tasks to establish persistence.[^6]  |
| [[Odbcconf\|T1218.008]] | Odbcconf | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used `odbcconf` to proxy the execution of malicious DLL files.[^8]  |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | [Cobalt Group](https://attack.mitre.org/groups/G0080) has compromised legitimate web browser updates to deliver a backdoor. [^13]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Cobalt Group](https://attack.mitre.org/groups/G0080) used a JavaScript backdoor that is capable of collecting a list of the security solutions installed on the victim's machine.[^15]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent malicious Word OLE compound documents to victims.[^18]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails containing malicious attachments that require users to execute a file or macro to infect the victim machine.[^18] [^4]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used exploits to increase their levels of rights and privileges.[^6]  |
| [[CMSTP\|T1218.003]] | CMSTP | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the command `cmstp.exe /s /ns C:\Users\ADMINI~W\AppData\Local\Temp\XKNqbpzl.txt` to bypass AppLocker and launch a malicious script.[^18] [^15] [^4]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used regsvr32.exe to execute scripts.[^18] [^15] [^8]  |
| [[Process Injection\|T1055]] | Process Injection | [Cobalt Group](https://attack.mitre.org/groups/G0080) has injected code into trusted processes.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used powershell.exe to download and execute scripts.[^18] [^17] [^9] [^6] [^3] [^8]  |
| [[Tool\|T1588.002]] | Tool | [Cobalt Group](https://attack.mitre.org/groups/G0080) has obtained and used a variety of tools including [Mimikatz](https://attack.mitre.org/software/S0002), [PsExec](https://attack.mitre.org/software/S0029), [Cobalt Strike](https://attack.mitre.org/software/S0154), and [SDelete](https://attack.mitre.org/software/S0195).[^9]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used Remote Desktop Protocol to conduct lateral movement.[^6]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent Word OLE compound documents with malicious obfuscated VBA macros that will run upon user execution.[^18] [^17] [^6] [^15] [^4] [^8]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Cobalt Group](https://attack.mitre.org/groups/G0080) had exploited multiple vulnerabilities for execution, including Microsoft’s Equation Editor (CVE-2017-11882), an Internet Explorer vulnerability (CVE-2018-8174), CVE-2017-8570, CVE-2017-0199, and CVE-2017-8759.[^18] [^17] [^9] [^5] [^12] [^3] [^10] [^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Cobalt Group](https://attack.mitre.org/groups/G0080) deleted the DLL dropper from the victim’s machine to cover their tracks.[^18]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Cobalt Group](https://attack.mitre.org/groups/G0080) has bypassed UAC.[^6]  |
| [[XSL Script Processing\|T1220]] | XSL Script Processing | [Cobalt Group](https://attack.mitre.org/groups/G0080) used msxsl.exe to bypass AppLocker and to invoke Jscript code from an XSL file.[^18]  |
| [[DNS\|T1071.004]] | DNS | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used DNS tunneling for C2.[^18] [^9] [^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Cobalt Group](https://attack.mitre.org/groups/G0080) has executed JavaScript scriptlets on the victim's machine.[^18] [^17] [^6] [^15] [^4] [^8]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails with URLs pointing to malicious documents.[^18] [^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails containing malicious links that require users to execute a file or macro to infect the victim machine.[^18] [^4] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used a JavaScript backdoor that is capable of launching cmd.exe to execute shell commands.[^15]  The group has used an exploit toolkit known as Threadkit that launches .bat files.[^18] [^17] [^6] [^15] [^4] [^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used HTTPS for C2.[^18] [^9] [^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used Registry Run keys for persistence. The group has also set a Startup path to launch the PowerShell shell command and download Cobalt Strike.[^6]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the Plink utility to create SSH tunnels.[^18] [^9] [^6]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the Plink utility to create SSH tunnels.[^6]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Cobalt Group](https://attack.mitre.org/groups/G0080) has created new services to establish persistence.[^6]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Cobalt Group](https://attack.mitre.org/groups/G0080) used the Ammyy Admin tool as well as TeamViewer for remote access, including to preserve remote access if a Cobalt Strike module was lost.[^17] [^9] [^6]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Cobalt Group](https://attack.mitre.org/groups/G0080) leveraged an open-source tool called SoftPerfect Network Scanner to perform network scanning.[^17] [^9] [^6]  |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | [Cobalt Group](https://attack.mitre.org/groups/G0080) has added persistence by registering the file name for the next stage malware under `HKCU\Environment\UserInitMprLogonScript`.[^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Mimikatz\|S0002]] | Mimikatz | [^17] [^9] [^6]  |
| [[SDelete\|S0195]] | SDelete | [^9]  |
| [[PsExec\|S0029]] | PsExec | [^17] [^6]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^18] [^17] [^6] [^5]  [^12] [^3] [^10] [^8]  |
| [[More_eggs\|S0284]] | More_eggs | [^18] [^13]  |



## References

[^1]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^2]: Cobalt Gang


[^3]: [RiskIQ Cobalt Jan 2018](https://web.archive.org/web/20190508170147/https://www.riskiq.com/blog/labs/cobalt-group-spear-phishing-russian-banks/)


[^4]: [Unit 42 Cobalt Gang Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-new-techniques-uncover-attribute-cobalt-gang-commodity-builders-infrastructure-revealed/)


[^5]: [Proofpoint Cobalt June 2017](https://www.proofpoint.com/us/threat-insight/post/microsoft-word-intruder-integrates-cve-2017-0199-utilized-cobalt-group-target)


[^6]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^7]: Cobalt Group


[^8]: [TrendMicro Cobalt Group Nov 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/cobalt-spam-runs-use-macros-cve-2017-8759-exploit/)


[^9]: [PTSecurity Cobalt Dec 2016](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)


[^10]: [Crowdstrike Global Threat Report Feb 2018](https://crowdstrike.lookbookhq.com/global-threat-report-2018-web/cs-2018-global-threat-report)


[^11]: [Europol Cobalt Mar 2018](https://www.europol.europa.eu/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain)


[^12]: [RiskIQ Cobalt Nov 2017](https://web.archive.org/web/20190508170630/https://www.riskiq.com/blog/labs/cobalt-strike/)


[^13]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^14]: Cobalt Spider


[^15]: [Morphisec Cobalt Gang Oct 2018](https://blog.morphisec.com/cobalt-gang-2.0)


[^16]: GOLD KINGSWOOD


[^17]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^18]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


