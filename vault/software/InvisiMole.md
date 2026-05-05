---
aliases: 
    - S0260
    
mitre-attack: https://attack.mitre.org/software/S0260
---

## S0260

[InvisiMole](https://attack.mitre.org/software/S0260) is a modular spyware program that has been used by the InvisiMole Group since at least 2013. [InvisiMole](https://attack.mitre.org/software/S0260) has two backdoor modules called RC2FM and RC2CL that are used to perform post-exploitation activities. It has been discovered on compromised victims in the Ukraine and Russia. [Gamaredon Group](https://attack.mitre.org/groups/G0047) infrastructure has been used to download and execute [InvisiMole](https://attack.mitre.org/software/S0260) against a small number of victims.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [InvisiMole](https://attack.mitre.org/software/S0260) uses variations of a simple XOR encryption routine for C&C communications.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [InvisiMole](https://attack.mitre.org/software/S0260) has a command to disable routing and the Firewall on the victim’s machine.[^1]  |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [InvisiMole](https://attack.mitre.org/software/S0260) can collect jpeg files from connected MTP devices.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [InvisiMole](https://attack.mitre.org/software/S0260) has used rundll32.exe for execution.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [InvisiMole](https://attack.mitre.org/software/S0260) can can remove all system restore points.[^1]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [InvisiMole](https://attack.mitre.org/software/S0260) can inject its backdoor as a portable executable into a target process.[^2] 	 |
| [[System Checks\|T1497.001]] | System Checks | [InvisiMole](https://attack.mitre.org/software/S0260) can check for artifacts of VirtualBox, Virtual PC and VMware environment, and terminate itself if they are detected.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [InvisiMole](https://attack.mitre.org/software/S0260) has used Windows services as a way to execute its malicious payload.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [InvisiMole](https://attack.mitre.org/software/S0260) has deleted files and directories including XML and files successfully uploaded to C2 servers.[^1] [^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [InvisiMole](https://attack.mitre.org/software/S0260) has been configured with several servers available for alternate C2 communications.[^1] [^2]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [InvisiMole](https://attack.mitre.org/software/S0260) can use the `ITaskService`, `ITaskDefinition` and `ITaskSettings` COM interfaces to schedule a task.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [InvisiMole](https://attack.mitre.org/software/S0260) can place a lnk file in the Startup Folder to achieve persistence.[^2]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [InvisiMole](https://attack.mitre.org/software/S0260) can inject its code into a trusted process via the APC queue.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [InvisiMole](https://attack.mitre.org/software/S0260) has used TCP to download additional modules.[^2]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [InvisiMole](https://attack.mitre.org/software/S0260) can use zlib to compress and decompress data.[^1] [^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [InvisiMole](https://attack.mitre.org/software/S0260) uses WinRAR to compress data that is intended to be exfiltrated.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [InvisiMole](https://attack.mitre.org/software/S0260) can capture screenshots of not only the entire screen, but of each separate window open, in case they are overlapping.[^1] [^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can enumerate windows and child windows on a compromised host.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [InvisiMole](https://attack.mitre.org/software/S0260) can capture keystrokes on a compromised host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) lists local users and session information.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [InvisiMole](https://attack.mitre.org/software/S0260) determines a working directory where it stores all the gathered data about the compromised machine.[^1] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [InvisiMole](https://attack.mitre.org/software/S0260) can collect data from the system, and can monitor changes in specified directories.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [InvisiMole](https://attack.mitre.org/software/S0260) can create hidden system directories.[^2]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [InvisiMole](https://attack.mitre.org/software/S0260) has exploited CVE-2007-5633 vulnerability in the speedfan.sys driver to obtain kernel mode privileges.[^2]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [InvisiMole](https://attack.mitre.org/software/S0260) can use a modified base32 encoding to encode data within the subdomain of C2 requests.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [InvisiMole](https://attack.mitre.org/software/S0260) has a command to create, set, copy, or delete a specified Registry key or value.[^1] [^2]  |
| [[Control Panel\|T1218.002]] | Control Panel | [InvisiMole](https://attack.mitre.org/software/S0260) can register itself for execution and persistence via the Control Panel.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [InvisiMole](https://attack.mitre.org/software/S0260) can use a JavaScript file as part of its execution chain.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can obtain running services on the victim.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) gathers information on the IP forwarding table, MAC address, configured proxy, and network SSID.[^1] [^2]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [InvisiMole](https://attack.mitre.org/software/S0260) can use Data Protection API to encrypt its components on the victim’s computer, to evade detection, and to make sure the payload can only be decrypted and loaded on one specific compromised computer.[^2]  |
| [[ListPlanting\|T1055.015]] | ListPlanting | [InvisiMole](https://attack.mitre.org/software/S0260) has used ListPlanting to inject code into a trusted process.[^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [InvisiMole](https://attack.mitre.org/software/S0260) can function as a proxy to create a server that relays communication between the client and C&C server, or between two clients.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [InvisiMole](https://attack.mitre.org/software/S0260) can inject itself into another process to avoid detection including use of a technique called ListPlanting that customizes the sorting algorithm in a ListView structure.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can gather information on the OS version, computer name, DEP policy, and memory size.[^1] [^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [InvisiMole](https://attack.mitre.org/software/S0260) can launch a remote shell to execute commands.[^1] [^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can gather information on the mapped drives and system volume serial number.[^1] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [InvisiMole](https://attack.mitre.org/software/S0260) can register a Windows service named CsPower as part of its execution chain, and a Windows service named clr_optimization_v2.0.51527_X86 to achieve persistence.[^2]  |
| [[DNS\|T1071.004]] | DNS | [InvisiMole](https://attack.mitre.org/software/S0260) has used a custom implementation of DNS tunneling to embed C2 communications in DNS requests and replies.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [InvisiMole](https://attack.mitre.org/software/S0260) avoids analysis by encrypting all strings, internal files, configuration data and by using a custom executable format.[^1] [^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [InvisiMole](https://attack.mitre.org/software/S0260) can record sound using input audio devices.[^1] [^2]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [InvisiMole](https://attack.mitre.org/software/S0260) can spread within a network via the BlueKeep (CVE-2019-0708) and EternalBlue (CVE-2017-0144) vulnerabilities in RDP and SMB respectively.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | [InvisiMole](https://attack.mitre.org/software/S0260) has a command to list account information on the victim’s machine.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can list information about files in a directory and recently opened or used documents. [InvisiMole](https://attack.mitre.org/software/S0260) can also search for specific files by supplied file mask.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can collect information about installed software used by specific users, software executed on user login, and software executed by each system.[^1] [^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [InvisiMole](https://attack.mitre.org/software/S0260) uses a variation of the XOR cipher to encrypt files before exfiltration.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [InvisiMole](https://attack.mitre.org/software/S0260) samples were timestomped by the authors by setting the PE timestamps to all zero values. [InvisiMole](https://attack.mitre.org/software/S0260) also has a built-in command to modify file times.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [InvisiMole](https://attack.mitre.org/software/S0260) can decrypt, unpack and load a DLL from its resources, or from blobs encrypted with Data Protection API, two-key triple DES, and variations of the XOR cipher.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [InvisiMole](https://attack.mitre.org/software/S0260) can upload files to the victim's machine for operations.[^1] [^2]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [InvisiMole](https://attack.mitre.org/software/S0260) can mimic HTTP protocol with custom HTTP “verbs” HIDE, ZVVP, and NOP.[^1] [^2]  |
| [[Network Share Connection Removal\|T1070.005]] | Network Share Connection Removal | <br>[InvisiMole](https://attack.mitre.org/software/S0260) can disconnect previously connected remote drives.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [InvisiMole](https://attack.mitre.org/software/S0260) can sort and collect specific documents as well as generate a list of all files on a newly inserted drive and store them in an encrypted file.[^1] [^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [InvisiMole](https://attack.mitre.org/software/S0260) can use fileless UAC bypass and create an elevated COM object to escalate privileges.[^1] [^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [InvisiMole](https://attack.mitre.org/software/S0260) has executed legitimate tools in hidden windows.[^2]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [InvisiMole](https://attack.mitre.org/software/S0260) can replace legitimate software or documents in the compromised network with their trojanized versions, in an attempt to propagate itself within the network.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [InvisiMole](https://attack.mitre.org/software/S0260) can remotely activate the victim’s webcam to capture content.[^1] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can check for the presence of network sniffers, AV, and BitDefender firewall.[^2]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [InvisiMole](https://attack.mitre.org/software/S0260) can use a .lnk shortcut for the Control Panel to establish persistence.[^2]  |
| [[DLL\|T1574.001]] | DLL | [InvisiMole](https://attack.mitre.org/software/S0260) can be launched by using DLL search order hijacking in which the wrapper DLL is placed in the same folder as explorer.exe and loaded during startup into the Windows Explorer process instead of the legitimate library.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can scan the network for open ports and vulnerable instances of RDP and SMB protocols.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [InvisiMole](https://attack.mitre.org/software/S0260) can deliver trojanized versions of software and documents, relying on user execution.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) gathers the local system time from the victim’s machine.[^1] [^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [InvisiMole](https://attack.mitre.org/software/S0260) has used scheduled tasks named `MSST` and `\Microsoft\Windows\Autochk\Scheduled` to establish persistence.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [InvisiMole](https://attack.mitre.org/software/S0260) uses HTTP for C2 communications.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can gather network share information.[^1]  |
| [[External Proxy\|T1090.002]] | External Proxy | [InvisiMole](https://attack.mitre.org/software/S0260) InvisiMole can identify proxy servers used by the victim and use them for C2 communication.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [InvisiMole](https://attack.mitre.org/software/S0260) can obtain a list of running processes.[^1] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [InvisiMole](https://attack.mitre.org/software/S0260) has attempted to disguise itself by registering under a seemingly legitimate service name.[^2]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [InvisiMole](https://attack.mitre.org/software/S0260) has undergone regular technical improvements in an attempt to evade detection.[^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [InvisiMole](https://attack.mitre.org/software/S0260) has installed legitimate but vulnerable Total Video Player software and wdigest.dll library drivers on compromised hosts to exploit stack overflow and input validation vulnerabilities for code execution.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [InvisiMole](https://attack.mitre.org/software/S0260) has disguised its droppers as legitimate software or documents, matching their original names and locations, and saved its files as mpr.dll in the Windows folder.[^1] [^2]  |
| [[Native API\|T1106]] | Native API | [InvisiMole](https://attack.mitre.org/software/S0260) can use winapiexec tool for indirect execution of  `ShellExecuteW` and `CreateProcessA`.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [InvisiMole](https://attack.mitre.org/software/S0260) can enumerate Registry values, keys, and data.[^1]  |




## References

[^1]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^2]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^3]: InvisiMole


