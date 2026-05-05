---
aliases: 
    - Lazarus Group
    - Labyrinth Chollima
    - HIDDEN COBRA
    - Guardians of Peace
    - ZINC
    - NICKEL ACADEMY
    - Diamond Sleet
mitre-attack: https://attack.mitre.org/groups/G0032
---

## G0032

[Lazarus Group](https://attack.mitre.org/groups/G0032) is a North Korean state-sponsored cyber threat group attributed to the Reconnaissance General Bureau (RGB). [^7]  [^48]  [Lazarus Group](https://attack.mitre.org/groups/G0032) has been active since at least 2009 and is reportedly responsible for the November 2014 destructive wiper attack on Sony Pictures Entertainment, identified by Novetta as part of Operation Blockbuster. Malware used by [Lazarus Group](https://attack.mitre.org/groups/G0032) correlates to other reported campaigns, including Operation Flame, Operation 1Mission, Operation Troy, DarkSeoul, and Ten Days of Rain.[^38] <br><br>North Korea’s cyber operations have shown a consistent pattern of adaptation, forming and reorganizing units as national priorities shift. These units frequently share personnel, infrastructure, malware, and tradecraft, making it difficult to attribute specific operations with high confidence. Public reporting often uses “Lazarus Group” as an umbrella term for multiple North Korean cyber operators conducting espionage, destructive attacks, and financially motivated campaigns.[^33] [^6] [^45] <br><br>

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware uses cmd.exe to execute commands on a compromised host.[^38] [^55] [^54] [^28] [^27]  A Destover-like variant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) uses a batch file mechanism to delete its binaries from the system.[^46]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Lazarus Group](https://attack.mitre.org/groups/G0032) has targeted victims with spearphishing emails containing malicious Microsoft Word documents.[^22] [^10] [^9] [^27]  |
| [[Indirect Command Execution\|T1202]] | Indirect Command Execution | [Lazarus Group](https://attack.mitre.org/groups/G0032) persistence mechanisms have used `forfiles.exe` to execute .htm files.[^27]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SierraBravo-Two generates an email message via SMTP containing information about newly infected victims.[^38] [^58]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware also uses a unique form of communication encryption known as FakeTLS that mimics TLS but uses a different encryption method, potentially evading SSL traffic inspection/decryption.[^38] [^55] [^54] [^29]  |
| [[Server\|T1584.004]] | Server | [Lazarus Group](https://attack.mitre.org/groups/G0032) has compromised servers to stage malicious tools.[^10]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Lazarus Group](https://attack.mitre.org/groups/G0032) has downloaded files, malware, and tools from its C2 onto a compromised host.[^38] [^55] [^23] [^41] [^12] [^10] [^19] [^9] [^27] [^3]  |
| [[Mshta\|T1218.005]] | Mshta | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used `mshta.exe` to execute HTML pages downloaded by initial access documents.[^9] [^27]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia obtains and sends to its C2 server the title of the window for each running process. The KilaAlfa keylogger also reports the title of the window in the foreground.[^38] [^23] [^4]  |
| [[Malware\|T1587.001]] | Malware | [Lazarus Group](https://attack.mitre.org/groups/G0032) has developed custom malware for use in their operations.[^57] [^19]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Lazarus Group](https://attack.mitre.org/groups/G0032) keylogger KiloAlfa obtains user tokens from interactive sessions to execute itself with API call `CreateProcessAsUserA` under that user's context.[^38] [^4]  |
| [[SSH\|T1021.004]] | SSH | [Lazarus Group](https://attack.mitre.org/groups/G0032) used SSH and the PuTTy PSCP utility to gain access to a restricted segment of a compromised network.[^10]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware WhiskeyDelta-Two contains a function that attempts to rename the administrator’s account.[^38] [^55]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used a VBA Macro to set its file attributes to System and Hidden and has named files with a dot prefix to hide them from the Finder application.[^54] [^41] [^12] [^9]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used a custom secure delete function to overwrite file contents with data from heap memory.[^38]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [Lazarus Group](https://attack.mitre.org/groups/G0032) has studied publicly available information about a targeted organization to tailor spearphishing efforts against specific departments and/or individuals.[^10]  |
| [[Native API\|T1106]] | Native API | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used the Windows API `ObtainUserAgentString` to obtain the User-Agent from a compromised host to connect to a C2 server.[^39]  [Lazarus Group](https://attack.mitre.org/groups/G0032) has also used various, often lesser known, functions to perform various types of Discovery and [Process Injection](https://attack.mitre.org/techniques/T1055).[^9] [^27]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used administrator credentials to gain access to restricted network segments.[^10]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Lazarus Group](https://attack.mitre.org/groups/G0032) has distributed malicious payloads embedded in PNG files.[^36]  |
| [[Query Registry\|T1012]] | Query Registry | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia checks Registry keys within HKCU and HKLM to determine if certain applications are present, including SecureCRT, Terminal Services, RealVNC, TightVNC, UltraVNC, Radmin, mRemote, TeamViewer, FileZilla, pcAnyware, and Remote Desktop. Another [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample checks for the presence of the following Registry key:`HKEY_CURRENT_USER\Software\Bitcoin\Bitcoin-Qt`.[^38] [^23] [^54]  |
| [[External Proxy\|T1090.002]] | External Proxy | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used multiple proxies to obfuscate network traffic from victims.[^25] [^12]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used multiple types of encryption and encoding for their payloads, including AES, Caracachs, RC4, XOR, Base64, and other tricks such as creating aliases in code for [Native API](https://attack.mitre.org/techniques/T1106) function names.[^38] [^23] [^58] [^54] [^12] [^9] [^27]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used multi-stage malware components that inject later stages into separate processes.[^9]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used nmap from a router VM to scan ports on systems within the restricted segment of an enterprise network.[^10]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Lazarus Group](https://attack.mitre.org/groups/G0032) has collected data and files from compromised networks.[^38] [^23] [^58] [^10]  |
| [[Service Stop\|T1489]] | Service Stop | [Lazarus Group](https://attack.mitre.org/groups/G0032) has stopped the MSExchangeIS service to render Exchange contents inaccessible to users.[^55]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia obtains and sends to its C2 server information about the first network interface card’s configuration, including IP address, gateways, subnet mask, DHCP information, and whether WINS is available.[^38] [^23]  |
| [[Digital Certificates\|T1588.004]] | Digital Certificates | [Lazarus Group](https://attack.mitre.org/groups/G0032) has obtained SSL certificates for their C2 domains.[^57]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families encrypt C2 traffic using custom code that uses XOR with an ADD operation and XOR with a SUB operation. Another [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample XORs C2 traffic. Other [Lazarus Group](https://attack.mitre.org/groups/G0032) malware uses Caracachs encryption to encrypt C2 payloads. [Lazarus Group](https://attack.mitre.org/groups/G0032) has also used AES to encrypt C2 traffic.[^38] [^55] [^54] [^46]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families collect information on the type and version of the victim OS, as well as the victim computer name and CPU information.[^38] [^55] [^23] [^54] [^46] [^9]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | Various [Lazarus Group](https://attack.mitre.org/groups/G0032) malware enumerates logged-on users.[^38] [^55] [^23] [^58] [^54] [^41] [^9]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Lazarus Group](https://attack.mitre.org/groups/G0032) has changed memory protection permissions then overwritten in memory DLL function code with shellcode, which was later executed via [KernelCallbackTable](https://attack.mitre.org/techniques/T1574/013) hijacking. [Lazarus Group](https://attack.mitre.org/groups/G0032) has also used shellcode within macros to decrypt and manually map DLLs into memory at runtime.[^9] [^27]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Lazarus Group](https://attack.mitre.org/groups/G0032) has exfiltrated data and files over a C2 channel through its various tools and malware.[^38] [^23] [^54]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used GitHub as C2, pulling hosted image payloads then committing command execution output to files in specific directories.[^9]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Lazarus Group](https://attack.mitre.org/groups/G0032) has compressed exfiltrated data with RAR and used RomeoDelta malware to archive specified directories in .zip format, encrypt the .zip file, and upload it to C2. [^23] [^58] [^54]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Lazarus Group](https://attack.mitre.org/groups/G0032) has exploited Adobe Flash vulnerability CVE-2018-4878 for execution.[^22]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used PowerShell to execute commands and malicious code.[^19]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Lazarus Group](https://attack.mitre.org/groups/G0032) has sent malicious links to victims via email.[^10]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia saves information gathered about the victim to a file that is saved in the %TEMP% directory, then compressed, encrypted, and uploaded to a C2 server.[^38] [^23]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [Lazarus Group](https://attack.mitre.org/groups/G0032) has renamed system utilities such as `wscript.exe` and `mshta.exe`.[^27]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used WMIC for discovery as well as to execute payloads for persistence and lateral movement.[^38] [^58] [^10] [^27]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Lazarus Group](https://attack.mitre.org/groups/G0032) has conducted C2 over HTTP and HTTPS.[^54] [^41] [^12] [^9] [^27] [^3]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Lazarus Group](https://attack.mitre.org/groups/G0032) executed [Responder](https://attack.mitre.org/software/S0174) using the command `[Responder file path] -i [IP address] -rPv` on a compromised host to harvest credentials and move laterally.[^10]  |
| [[Process Discovery\|T1057]] | Process Discovery | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families gather a list of running processes on a victim system and send it to their C2 server. A Destover-like variant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) also gathers process times.[^38] [^23] [^54] [^46] [^12] [^9]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Lazarus Group](https://attack.mitre.org/groups/G0032) has maintained persistence by loading malicious code into a startup folder or by adding a Registry Run key.[^38] [^58] [^54] [^9]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware TangoDelta attempts to terminate various processes associated with McAfee. Additionally, [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SHARPKNOT disables the Microsoft Windows System Event Notification and Alerter services.[^38] [^23] [^4] [^28] .  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Lazarus Group](https://attack.mitre.org/groups/G0032) collected email addresses belonging to various departments of a targeted organization which were used in follow-on phishing campaigns.[^10]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used malware like WhiskeyAlfa to overwrite the first 64MB of every drive with a mix of static and random buffers. A similar process is then used to wipe content in logical drives and, finally, attempt to wipe every byte of every sector on every drive. WhiskeyBravo can be used to overwrite the first 4.9MB of physical drives. WhiskeyDelta can overwrite the first 132MB or 1.5MB of each drive with random data from heap memory.[^55]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [Lazarus Group](https://attack.mitre.org/groups/G0032) replaced the background wallpaper of systems with a threatening image after rendering the system unbootable with a [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002).[^55]  |
| [[Tool\|T1588.002]] | Tool | [Lazarus Group](https://attack.mitre.org/groups/G0032) has obtained a variety of tools for their operations, including [Responder](https://attack.mitre.org/software/S0174) and PuTTy PSCP.[^10]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware has maintained persistence on a system by creating a LNK shortcut in the user’s Startup folder.[^54]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used VBA and embedded macros in Word documents to execute malicious code.[^9] [^27]  |
| [[Bootkit\|T1542.003]] | Bootkit | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware WhiskeyAlfa-Three modifies sector 0 of the Master Boot Record (MBR) to ensure that the malware will persist even if a victim machine shuts down.[^38] [^55]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used rundll32 to execute malicious payloads on a compromised host.[^3]  |
| [[Web Services\|T1583.006]] | Web Services | [Lazarus Group](https://attack.mitre.org/groups/G0032) has hosted malicious downloads on Github.[^57]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware KiloAlfa contains keylogging functionality.[^38] [^4]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | Some [Lazarus Group](https://attack.mitre.org/groups/G0032) malware uses a list of ordered port numbers to choose a port for C2 traffic, creating port-protocol mismatches.[^38] [^58]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | A [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample encodes data with base64.[^54]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Lazarus Group](https://attack.mitre.org/groups/G0032) delivered [RATANKBA](https://attack.mitre.org/software/S0241) and other malicious code to victims via a compromised legitimate website.[^13] [^19]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware attempts to connect to Windows shares for lateral movement by using a generated list of usernames, which center around permutations of the username Administrator, and weak passwords.[^38] [^58]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Lazarus Group](https://attack.mitre.org/groups/G0032) has attempted to get users to launch a malicious Microsoft Word attachment delivered via a spearphishing email.[^22] [^10] [^9] [^27]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Lazarus Group](https://attack.mitre.org/groups/G0032) has digitally signed malware and utilities to evade detection.[^9]  |
| [[System Binary Proxy Execution\|T1218]] | System Binary Proxy Execution | [Lazarus Group](https://attack.mitre.org/groups/G0032) lnk files used for persistence have abused the Windows Update Client (`wuauclt.exe`) to execute a malicious DLL.[^9] [^27]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia saves information gathered about the victim to a file that is compressed with Zlib, encrypted, and uploaded to a C2 server.[^58] [^54]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used a custom hashing method to resolve APIs used in shellcode.[^9]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware has deleted files in various ways, including "suicide scripts" to delete malware binaries from the victim. [Lazarus Group](https://attack.mitre.org/groups/G0032) also uses secure file deletion to delete files from the victim.[^38] [^46]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used a compromised router to serve as a proxy between a victim network's corporate and restricted segments.[^10]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SierraAlfa sends data to one of the hard-coded C2 servers chosen at random, and if the transmission fails, chooses a new C2 server to attempt the transmission again.[^38] [^58]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used shellcode within macros to decrypt and manually map DLLs and shellcode into memory at runtime.[^9] [^27]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | A Destover-like variant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) collects disk space information and sends it to its C2 server.[^38] [^55] [^23] [^54] [^46] [^9]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SHARPKNOT overwrites and deletes the Master Boot Record (MBR) on the victim's machine and has possessed MBR wiper malware since at least 2009.[^28] [^38]  |
| [[Domains\|T1583.001]] | Domains | [Lazarus Group](https://attack.mitre.org/groups/G0032) has acquired domains related to their campaigns to act as distribution points and C2 channels.[^57] [^19]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used `schtasks` for persistence including through the periodic execution of a remote XSL script or a dropped VBS payload.[^27] [^3]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used social media platforms, including LinkedIn and Twitter, to send spearphishing messages.[^19]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Lazarus Group](https://attack.mitre.org/groups/G0032) has renamed malicious code to disguise it as Microsoft's narrator and other legitimate files.[^56] [^27]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Lazarus Group](https://attack.mitre.org/groups/G0032) has restored malicious [KernelCallbackTable](https://attack.mitre.org/techniques/T1574/013) code to its original state after the process execution flow has been hijacked.[^9]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware can use a common function to identify target files by their extension, and some also enumerate files and directories, including a Destover-like variant that lists files and gathers information for all drives.[^38] [^46] [^9] [^27]  |
| [[KernelCallbackTable\|T1574.013]] | KernelCallbackTable | [Lazarus Group](https://attack.mitre.org/groups/G0032) has abused the `KernelCallbackTable` to hijack process control flow and execute shellcode.[^9] [^27]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | A [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample performs reflective DLL injection.[^54] [^9]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Lazarus Group](https://attack.mitre.org/groups/G0032) has created new Twitter accounts to conduct social engineering against potential victims.[^19]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SierraCharlie uses RDP for propagation.[^38] [^58]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Lazarus Group](https://attack.mitre.org/groups/G0032) has rebooted systems after destroying files and wiping the MBR on infected systems.[^28]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | A Destover-like implant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) can obtain the current system time and send it to the C2 server.[^46]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used a scheduled task named `SRCheck` to mask the execution of a malicious .dll.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families use timestomping, including modifying the last write timestamp of a specified Registry key to a random date, as well as copying the timestamp for legitimate .exe files (such as calc.exe or mspaint.exe) to its dropped files.[^38] [^55] [^23] [^46]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Lazarus Group](https://attack.mitre.org/groups/G0032) has routinely deleted log files on a compromised router, including automatic log deletion through the use of the logrotate utility.[^10]   |
| [[DLL\|T1574.001]] | DLL | [Lazarus Group](https://attack.mitre.org/groups/G0032) has replaced `win_fw.dll`, an internal component that is executed during IDA Pro installation, with a malicious DLL to download and execute a payload.[^3]  [Lazarus Group](https://attack.mitre.org/groups/G0032) utilized DLL side-loading to execute malicious payloads through abuse of the legitimate processes `wsmprovhost.exe` and `dfrgui.exe`.[^49]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | Various [Lazarus Group](https://attack.mitre.org/groups/G0032) malware modifies the Windows firewall to allow incoming connections or disable it entirely using [netsh](https://attack.mitre.org/software/S0108). [^38] [^23] [^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families install themselves as new services.[^38] [^55]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware SierraAlfa accesses the `ADMIN$` share via SMB to conduct lateral movement.[^38] [^58]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Lazarus Group](https://attack.mitre.org/groups/G0032) has created new email accounts for spearphishing operations.[^10]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used `net use` to identify and establish a network connection with a remote host.[^10]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | A [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample encrypts data using a simple byte based XOR operation prior to exfiltration.[^38] [^23] [^58] [^54]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[RawDisk\|S0364]] | RawDisk | [^38] [^55]  |
| [[netsh\|S0108]] | netsh | [^23]  |
| [[Responder\|S0174]] | Responder | [^26]  |
| [[route\|S0103]] | route | [^10]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [^42]  |
| [[Proxysvc\|S0238]] | Proxysvc | [^46]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [^51]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [^10]  |
| [[Bankshot\|S0239]] | Bankshot | [^22]  |
| [[AuditCred\|S0347]] | AuditCred | [^47]  |
| [[Dacls\|S0497]] | Dacls | [^41] [^12]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [^50]  |
| [[Volgmer\|S0180]] | Volgmer | [^52]  |
| [[WannaCry\|S0366]] | WannaCry | [^40] [^20] [^14] [^5]  |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [^16]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [^56]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) is exclusively associated with [Lazarus Group](https://attack.mitre.org/groups/G0032) operations in 2022.[^15]  |
| [[RATANKBA\|S0241]] | RATANKBA | [^43]  |
| [[BADCALL\|S0245]] | BADCALL | [^37]  |
| [[Cryptoistic\|S0498]] | Cryptoistic | [^41]  |
| [[HotCroissant\|S0431]] | HotCroissant | [^24]  |
| [[HARDRAIN\|S0246]] | HARDRAIN | [^30]  |
| [[AppleJeus\|S0584]] | AppleJeus | [^57]  |
| [[ECCENTRICBANDWAGON\|S0593]] | ECCENTRICBANDWAGON | [^11]  |
| [[Dtrack\|S0567]] | Dtrack | [^44]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [^25]  |



## References

[^1]: Lazarus Group


[^2]: Diamond Sleet


[^3]: [ESET Twitter Ida Pro Nov 2021](https://x.com/ESETresearch/status/1458438155149922312)


[^4]: [Novetta Blockbuster Tools](https://web.archive.org/web/20220425194457/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Tools-Report.pdf)


[^5]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)


[^6]: [Mandiant DPRK Groups 2023](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023)


[^7]: [US-CERT HIDDEN COBRA June 2017](https://www.us-cert.gov/ncas/alerts/TA17-164A)


[^8]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^9]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^10]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^11]: [CISA EB Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)


[^12]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


[^13]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^14]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)


[^15]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^16]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^17]: HIDDEN COBRA


[^18]: ZINC


[^19]: [Google TAG Lazarus Jan 2021](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/)


[^20]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)


[^21]: [Secureworks NICKEL ACADEMY Dec 2017](https://www.secureworks.com/about/press/media-alert-secureworks-discovers-north-korean-cyber-threat-group-lazarus-spearphishing)


[^22]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^23]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^24]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)


[^25]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^26]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^27]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^28]: [US-CERT SHARPKNOT June 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536.11.WHITE.pdf)


[^29]: [McAfee-GhostSecret-fixurl](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^30]: [US-CERT HARDRAIN March 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)


[^31]: Guardians of Peace


[^32]: [CrowdStrike Labyrinth Chollima Feb 2022](https://web.archive.org/web/20210723190317/https://adversary.crowdstrike.com/en-US/adversary/labyrinth-chollima/)


[^33]: [Mandiant DPRK Laz Org Breakdown 2022](https://cloud.google.com/blog/topics/threat-intelligence/mapping-dprk-groups-to-government/)


[^34]: NICKEL ACADEMY


[^35]: [Microsoft ZINC disruption Dec 2017](https://blogs.microsoft.com/on-the-issues/2017/12/19/microsoft-facebook-disrupt-zinc-malware-attack-protect-customers-internet-ongoing-cyberthreats/)


[^36]: [Microsoft DiamondSleet 2023](https://www.microsoft.com/en-us/security/blog/2023/11/22/diamond-sleet-supply-chain-compromise-distributes-a-modified-cyberlink-installer/)


[^37]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^38]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^39]: [McAfee Lazarus Jul 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-a-job-offer-thats-too-good-to-be-true/?hilite=%27Operation%27%2C%27North%27%2C%27Star%27)


[^40]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^41]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^42]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^43]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^44]: [Kaspersky Dtrack](https://usa.kaspersky.com/about/press-releases/2019_dtrack-previously-unknown-spy-tool-hits-financial-institutions-and-research-centers)


[^45]: [JPCert Blog Laz Subgroups 2025](https://blogs.jpcert.or.jp/en/2025/03/classifying-lazaruss-subgroup.html)


[^46]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^47]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^48]: [Treasury North Korean Cyber Groups September 2019](https://home.treasury.gov/news/press-releases/sm774)


[^49]: [ASEC Lazarus 2022](https://asec.ahnlab.com/en/39828/)


[^50]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^51]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^52]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^53]: Labyrinth Chollima


[^54]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^55]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^56]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^57]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^58]: [Novetta Blockbuster RATs](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)


