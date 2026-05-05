---
aliases: 
    - S1086
    
mitre-attack: https://attack.mitre.org/software/S1086
---

## S1086

[Snip3](https://attack.mitre.org/software/S1086) is a sophisticated crypter-as-a-service that has been used since at least 2021 to obfuscate and load numerous strains of malware including [AsyncRAT](https://attack.mitre.org/software/S1087), [Revenge RAT](https://attack.mitre.org/software/S0379), [Agent Tesla](https://attack.mitre.org/software/S0331), and [NETWIRE](https://attack.mitre.org/software/S0198).[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Snip3](https://attack.mitre.org/software/S1086) can decode its second-stage PowerShell script prior to execution.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Snip3](https://attack.mitre.org/software/S1086) can download additional payloads from web services including Pastebin and top4top.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Snip3](https://attack.mitre.org/software/S1086) can use visual basic scripts for first-stage execution.[^1] [^2]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | <br>[Snip3](https://attack.mitre.org/software/S1086) can use RunPE to execute malicious payloads within a hollowed Windows process.[^1] [^2] <br> |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Snip3](https://attack.mitre.org/software/S1086) has the ability to obfuscate strings using XOR encryption.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Snip3](https://attack.mitre.org/software/S1086) can create a VBS file in startup to persist after system restarts.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Snip3](https://attack.mitre.org/software/S1086) can gain execution through the download of visual basic files.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Snip3](https://attack.mitre.org/software/S1086) has the ability to query `Win32_ComputerSystem` for system information. [^1]   |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Snip3](https://attack.mitre.org/software/S1086) has been executed through luring victims into clicking malicious links.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Snip3](https://attack.mitre.org/software/S1086) has been delivered to victims through malicious e-mail attachments.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Snip3](https://attack.mitre.org/software/S1086) can execute `WScript.Sleep` to delay execution of its second stage.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Snip3](https://attack.mitre.org/software/S1086) can query the WMI class `Win32_ComputerSystem` to gather information.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [Snip3](https://attack.mitre.org/software/S1086) can download and execute additional payloads and modules over separate communication channels.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Snip3](https://attack.mitre.org/software/S1086) can download additional payloads to compromised systems.[^1] [^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Snip3](https://attack.mitre.org/software/S1086) has been delivered to victims through e-mail links to malicious files.[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Snip3](https://attack.mitre.org/software/S1086) has been delivered to targets via downloads from malicious domains.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Snip3](https://attack.mitre.org/software/S1086) has the ability to detect Windows Sandbox, VMWare, or VirtualBox by querying `Win32_ComputerSystem` to extract the `Manufacturer` string.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Snip3](https://attack.mitre.org/software/S1086) can execute PowerShell scripts in a hidden window.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Snip3](https://attack.mitre.org/software/S1086) can obfuscate strings using junk Chinese characters.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Snip3](https://attack.mitre.org/software/S1086) can use a PowerShell script for second-stage execution.[^1] [^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


[^2]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^3]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


