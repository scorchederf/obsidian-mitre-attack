---
aliases: 
    - Molerats
    - Operation Molerats
    - Gaza Cybergang
mitre-attack: https://attack.mitre.org/groups/G0021
---

## G0021

[Molerats](https://attack.mitre.org/groups/G0021) is an Arabic-speaking, politically-motivated threat group that has been operating since 2012. The group's victims have primarily been in the Middle East, Europe, and the United States.[^6] [^8] [^4] [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Msiexec\|T1218.007]] | Msiexec | [Molerats](https://attack.mitre.org/groups/G0021) has used msiexec.exe to execute an MSI payload.[^5]   |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Molerats](https://attack.mitre.org/groups/G0021) has sent malicious links via email trick users into opening a RAR archive and running an executable.[^4] [^5]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Molerats](https://attack.mitre.org/groups/G0021) used executables to download malicious files from different sources.[^4] [^5]   |
| [[Code Signing\|T1553.002]] | Code Signing | [Molerats](https://attack.mitre.org/groups/G0021) has used forged Microsoft code-signing certificates on malware.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Molerats](https://attack.mitre.org/groups/G0021) has delivered compressed executables within ZIP files to victims.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Molerats](https://attack.mitre.org/groups/G0021) has created scheduled tasks to persistently run VBScripts.[^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Molerats](https://attack.mitre.org/groups/G0021) decompresses ZIP files once on the victim machine.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Molerats](https://attack.mitre.org/groups/G0021) has sent phishing emails with malicious Microsoft Word and PDF attachments.[^4] [^5] [^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Molerats](https://attack.mitre.org/groups/G0021) actors obtained a list of active processes on the victim and sent them to C2 servers.[^6]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Molerats](https://attack.mitre.org/groups/G0021) has sent phishing emails with malicious links included.[^4]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Molerats](https://attack.mitre.org/groups/G0021) used the public tool BrowserPasswordDump10 to dump passwords saved in browsers on victims.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Molerats](https://attack.mitre.org/groups/G0021) saved malicious files within the AppData and Startup folders to maintain persistence.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Molerats](https://attack.mitre.org/groups/G0021) used PowerShell implants on target machines.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Molerats](https://attack.mitre.org/groups/G0021) used various implants, including those built with VBScript, on target machines.[^4] [^5]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Molerats](https://attack.mitre.org/groups/G0021) used various implants, including those built with JS, on target machines.[^4] 	 |
| [[Malicious File\|T1204.002]] | Malicious File | [Molerats](https://attack.mitre.org/groups/G0021) has sent malicious files via email that tricked users into clicking Enable Content to run an embedded macro and to download malicious archives.[^4] [^5] [^7]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Spark\|S0543]] | Spark | [^5]  [^7]  |
| [[SharpStage\|S0546]] | SharpStage | [^7]  |
| [[DropBook\|S0547]] | DropBook | [^7]  |
| [[DustySky\|S0062]] | DustySky | [^6] [^8] [^4]  |
| [[MoleNet\|S0553]] | MoleNet | [^7]   |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^6] [^8] [^1]  |



## References

[^1]: [FireEye Operation Molerats](https://web.archive.org/web/20201031075438/https://www.fireeye.com/blog/threat-research/2013/08/operation-molerats-middle-east-cyber-attacks-using-poison-ivy.html)


[^2]: Gaza Cybergang


[^3]: Molerats


[^4]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^5]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^6]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


[^7]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^8]: [DustySky2](http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf)


[^9]: Operation Molerats


