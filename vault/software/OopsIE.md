---
aliases: 
    - S0264
    
mitre-attack: https://attack.mitre.org/software/S0264
---

## S0264

[OopsIE](https://attack.mitre.org/software/S0264) is a Trojan used by [OilRig](https://attack.mitre.org/groups/G0049) to remotely execute commands as well as upload/download files to/from victims. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [OopsIE](https://attack.mitre.org/software/S0264) stages the output from command execution and collected files in specific folders before exfiltration.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [OopsIE](https://attack.mitre.org/software/S0264) exfiltrates command output and collected files to its C2 server in 1500-byte blocks.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [OopsIE](https://attack.mitre.org/software/S0264) concatenates then decompresses multiple resources to load an embedded .Net Framework assembly.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [OopsIE](https://attack.mitre.org/software/S0264) has the capability to delete files and scripts from the victim's machine.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [OopsIE](https://attack.mitre.org/software/S0264) uses WMI to perform discovery techniques.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [OopsIE](https://attack.mitre.org/software/S0264) encodes data in hexadecimal format over the C2 channel.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OopsIE](https://attack.mitre.org/software/S0264) checks for information on the CPU fan, temperature, mouse, hard disk, and motherboard as part of its anti-VM checks.[^3]  |
| [[System Checks\|T1497.001]] | System Checks | [OopsIE](https://attack.mitre.org/software/S0264) performs several anti-VM and sandbox checks on the victim's machine. One technique the group has used was to perform a WMI query `SELECT * FROM MSAcpi_ThermalZoneTemperature` to check the temperature to see if it’s running in a virtual environment.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OopsIE](https://attack.mitre.org/software/S0264) uses HTTP for C2 communications.[^1] [^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [OopsIE](https://attack.mitre.org/software/S0264) uses the command prompt to execute commands on the victim's machine.[^1] [^3]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [OopsIE](https://attack.mitre.org/software/S0264) compresses collected files with a simple character replacement scheme before sending them to its C2 server.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OopsIE](https://attack.mitre.org/software/S0264) can download files from its C2 server to the victim's machine.[^1] [^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [OopsIE](https://attack.mitre.org/software/S0264) creates and uses a VBScript as part of its persistent execution.[^1] [^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [OopsIE](https://attack.mitre.org/software/S0264) compresses collected files with GZipStream before sending them to its C2 server.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [OopsIE](https://attack.mitre.org/software/S0264) creates a scheduled task to run itself every three minutes.[^1] [^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [OopsIE](https://attack.mitre.org/software/S0264) uses the SmartAssembly obfuscator to pack an embedded .Net Framework assembly used for C2.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [OopsIE](https://attack.mitre.org/software/S0264) checks to see if the system is configured with "Daylight" time and checks for a specific region to be set for the timezone.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [OopsIE](https://attack.mitre.org/software/S0264) uses the Confuser protector to obfuscate an embedded .Net Framework assembly used for C2. [OopsIE](https://attack.mitre.org/software/S0264) also encodes collected data in hexadecimal format before writing to files on disk and obfuscates strings.[^1] [^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [OopsIE](https://attack.mitre.org/software/S0264) can upload files from the victim's machine to its C2 server.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^2]: OopsIE


[^3]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)


