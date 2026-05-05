---
aliases: 
    - S0534
    
mitre-attack: https://attack.mitre.org/software/S0534
---

## S0534

[Bazar](https://attack.mitre.org/software/S0534) is a downloader and backdoor that has been used since at least April 2020, with infections primarily against professional services, healthcare, manufacturing, IT, logistics and travel companies across the US and Europe. [Bazar](https://attack.mitre.org/software/S0534) reportedly has ties to [TrickBot](https://attack.mitre.org/software/S0266) campaigns and can be used to deploy additional malware, including ransomware, and to steal sensitive data.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Bazar](https://attack.mitre.org/software/S0534) can enumerate the victim's desktop.[^1] [^7]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Bazar](https://attack.mitre.org/software/S0534) can use [Nltest](https://attack.mitre.org/software/S0359) tools to obtain information about the domain.[^1] [^7]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Bazar](https://attack.mitre.org/software/S0534) can use TLS in C2 communications.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Bazar](https://attack.mitre.org/software/S0534) has the ability to identify domain administrator accounts.[^7] [^8]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Bazar](https://attack.mitre.org/software/S0534) can enumerate remote systems using ` Net View`.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Bazar](https://attack.mitre.org/software/S0534) can gain execution after a user clicks on a malicious link to decoy landing pages hosted on Google Docs.[^1] [^2] [^11]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Bazar](https://attack.mitre.org/software/S0534) can enumerate shared drives on the domain.[^7]  |
| [[Process Injection\|T1055]] | Process Injection | [Bazar](https://attack.mitre.org/software/S0534) can inject code through calling `VirtualAllocExNuma`.[^1]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Bazar](https://attack.mitre.org/software/S0534) has been downloaded via Windows BITS functionality.[^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Bazar](https://attack.mitre.org/software/S0534) can launch cmd.exe to perform reconnaissance commands.[^1] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Bazar](https://attack.mitre.org/software/S0534) can execute a PowerShell script received from C2.[^7] [^11]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Bazar](https://attack.mitre.org/software/S0534) has used XOR, RSA2, and RC4 encrypted files.[^1] [^7] [^11]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Bazar](https://attack.mitre.org/software/S0534) can identify the installed antivirus engine.[^1]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Bazar](https://attack.mitre.org/software/S0534) can attempt to overload sandbox analysis by sending 1550 calls to `printf`.[^1]  |
| [[Process Doppelgänging\|T1055.013]] | Process Doppelgänging | [Bazar](https://attack.mitre.org/software/S0534) can inject into a target process using process doppelgänging.[^1] [^7]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [Bazar](https://attack.mitre.org/software/S0534)'s loader can delete scheduled tasks created by a previous instance of the malware.[^7]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Bazar](https://attack.mitre.org/software/S0534) can retrieve information from the infected machine.[^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Bazar](https://attack.mitre.org/software/S0534) can hash then resolve API calls at runtime.[^1] [^7]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Bazar](https://attack.mitre.org/software/S0534) can perform a check to ensure that the operating system's keyboard and language settings are not set to Russian.[^7]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Bazar](https://attack.mitre.org/software/S0534) can collect the time on the compromised host.[^1] [^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Bazar](https://attack.mitre.org/software/S0534) can identity the current process on a compromised host.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | The [Bazar](https://attack.mitre.org/software/S0534) loader is used to download and execute the [Bazar](https://attack.mitre.org/software/S0534) backdoor.[^1] [^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Bazar](https://attack.mitre.org/software/S0534) can query `Windows\CurrentVersion\Uninstall` for installed applications.[^1] [^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | The [Bazar](https://attack.mitre.org/software/S0534) loader has named malicious shortcuts "adobe" and mimicked communications software.[^1] [^7] [^11]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Bazar](https://attack.mitre.org/software/S0534) can query the Registry for installed applications.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Bazar](https://attack.mitre.org/software/S0534) can send C2 communications with XOR encryption.[^7]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Bazar](https://attack.mitre.org/software/S0534) can use Winlogon Helper DLL to establish persistence.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Bazar](https://attack.mitre.org/software/S0534) can create a task named to appear benign.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Bazar](https://attack.mitre.org/software/S0534) can collect the IP address and NetBIOS name of an infected machine.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Bazar](https://attack.mitre.org/software/S0534) can use a timer to delay execution of core functionality.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Bazar](https://attack.mitre.org/software/S0534) can identify the username of the infected user.[^7]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Bazar](https://attack.mitre.org/software/S0534) has been signed with fake certificates including those appearing to be from VB CORPORATE PTY. LTD.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Bazar](https://attack.mitre.org/software/S0534) can delete its loader using a batch file in the Windows temporary folder.[^7]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Bazar](https://attack.mitre.org/software/S0534) has the ability to use an alternative C2 server if the primary server fails.[^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Bazar](https://attack.mitre.org/software/S0534) can use HTTP and HTTPS over ports 80 and 443 in C2 communications.[^1] [^7] [^4]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Bazar](https://attack.mitre.org/software/S0534) has been spread via emails with embedded malicious links.[^1] [^2] [^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bazar](https://attack.mitre.org/software/S0534) can download and deploy additional payloads, including ransomware and post-exploitation frameworks such as [Cobalt Strike](https://attack.mitre.org/software/S0154).[^1] [^2] [^7] [^11]  |
| [[Local Account\|T1087.001]] | Local Account | [Bazar](https://attack.mitre.org/software/S0534) can identify administrator accounts on an infected host.[^7]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Bazar](https://attack.mitre.org/software/S0534) has manually loaded ntdll from disk in order to identity and remove API hooks set by security products.[^7] 	 |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Bazar](https://attack.mitre.org/software/S0534) can create a scheduled task for persistence.[^1] [^7]  |
| [[Web Service\|T1102]] | Web Service | [Bazar](https://attack.mitre.org/software/S0534) downloads have been hosted on Google Docs.[^1] [^2]  |
| [[Double File Extension\|T1036.007]] | Double File Extension | The [Bazar](https://attack.mitre.org/software/S0534) loader has used dual-extension executable files such as PreviewReport.DOC.exe.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bazar](https://attack.mitre.org/software/S0534) can decrypt downloaded payloads. [Bazar](https://attack.mitre.org/software/S0534) also resolves strings and other artifacts at runtime.[^1] [^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Bazar](https://attack.mitre.org/software/S0534) can execute a WMI query to gather information about the installed antivirus engine.[^1] [^8]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Bazar](https://attack.mitre.org/software/S0534) can inject into a target process including Svchost, Explorer, and cmd using process hollowing.[^1] [^7]  |
| [[Native API\|T1106]] | Native API | [Bazar](https://attack.mitre.org/software/S0534) can use various APIs to allocate memory and facilitate code execution/injection.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Bazar](https://attack.mitre.org/software/S0534) can establish persistence by writing shortcuts to the Windows Startup folder.[^1] [^7]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Bazar](https://attack.mitre.org/software/S0534) can create or add files to Registry Run Keys to establish persistence.[^1] [^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bazar](https://attack.mitre.org/software/S0534) can fingerprint architecture, computer name, and OS version on the compromised host. [Bazar](https://attack.mitre.org/software/S0534) can also check if the Russian language is installed on the infected machine and terminate if it is found.[^1] [^7]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Bazar](https://attack.mitre.org/software/S0534) has a variant with a packed payload.[^1] [^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Bazar](https://attack.mitre.org/software/S0534) can implement DGA using the current date as a seed variable.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[EXOTIC LILY\|G1011]] | EXOTIC LILY |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^2]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)


[^3]: Bazaloader


[^4]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^5]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^6]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^7]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^8]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^9]: Team9


[^10]: KEGTAP


[^11]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^12]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


