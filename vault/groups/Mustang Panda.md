---
aliases: 
    - Mustang Panda
    - TA416
    - RedDelta
    - BRONZE PRESIDENT
    - STATELY TAURUS
    - FIREANT
    - CAMARO DRAGON
    - EARTH PRETA
    - HIVE0154
    - TWILL TYPHOON
    - TANTALUM
    - LUMINOUS MOTH
    - UNC6384
    - TEMP.Hex
    - Red Lich
    - ClumsyToad
mitre-attack: https://attack.mitre.org/groups/G0129
---

## G0129

[Mustang Panda](https://attack.mitre.org/groups/G0129) is a China-based cyber espionage threat actor that has been conducting operations since at least 2012. [Mustang Panda](https://attack.mitre.org/groups/G0129) has been known to use tailored phishing lures and decoy documents to deliver malicious payloads.  [Mustang Panda](https://attack.mitre.org/groups/G0129) has targeted government, diplomatic, and non-governmental organizations, including think tanks, religious institutions, and research entities, across the United States, Europe, and Asia, with notable activity in Russia, Mongolia, Myanmar, Pakistan, and Vietnam. [^5] [^50] [^32] [^34] [^2] [^12] [^51] [^40] [^27] [^35] [^8] [^25] [^47] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `ipconfig` and `arp` to determine network configuration information.[^45]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized SharpNBTScan to scan the victim environment.[^29]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Mustang Panda](https://attack.mitre.org/groups/G0129) has hosted malicious payloads on DropBox including [PlugX](https://attack.mitre.org/software/S0013).[^41]  |
| [[Web Services\|T1583.006]] | Web Services | [Mustang Panda](https://attack.mitre.org/groups/G0129) has set up Dropbox and Google Drive to host malicious downloads.[^42]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Mustang Panda](https://attack.mitre.org/groups/G0129) has executed PowerShell scripts via WMI.[^32] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Mustang Panda](https://attack.mitre.org/groups/G0129) has encrypted C2 communications with RC4.[^50] [^15]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged encryption and compression algorithms to obfuscate the traffic between the system and C2 server, methods observed included RC4, AES, XOR with 0x5a, and LZO.[^4]  |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used open-source research to identify information about victims to use in targeting to include creating weaponized phishing lures and attachments.[^37] [^33]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Mustang Panda](https://attack.mitre.org/groups/G0129) has sent malicious links including links directing victims to a Google Drive folder.[^37] [^33] [^27] [^42] [^41] [^6]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized webpages with Javascript code that downloads malicious payloads to the victim device.[^21]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged [NBTscan](https://attack.mitre.org/software/S0590) to scan IP networks.[^31]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Mustang Panda](https://attack.mitre.org/groups/G0129) has the ability to decrypt its payload prior to execution.[^54] [^51] [^35] [^25]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized RC4 encryption for malicious payloads.[^21] [^4]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `netstat -ano` to determine network connection information.[^45]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Mustang Panda](https://attack.mitre.org/groups/G0129) has embedded VBScript components in LNK files to download additional files and automate collection.[^32] [^2] [^27]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used VBA macros in maldocs to execute malicious DLLs.[^34]  [Mustang Panda](https://attack.mitre.org/groups/G0129) also utilized a VBS Script “autorun.vbs” that created persistence through saving the VBS Script in the startup directory which would cause it to run each time the machine was turned on.[^31]  |
| [[IDE Tunneling\|T1219.001]] | IDE Tunneling | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized an established Github account to create a tunnel within the victim environment using Visual Studio Code through the `code.exe tunnel` command.[^29]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Mustang Panda](https://attack.mitre.org/groups/G0129) has also exfiltrated archived files to cloud services such as Dropbox using `curl`.[^31] [^29]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Mustang Panda](https://attack.mitre.org/groups/G0129) has created a scheduled task to execute additional malicious software, as well as maintain persistence.[^32] [^34] [^2] [^6]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also created a scheduled task that creates a reverse shell.[^29]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized [AdFind](https://attack.mitre.org/software/S0552) to identify domain users.[^31]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Mustang Panda](https://attack.mitre.org/groups/G0129) has delivered web bugs to profile their intended targets.[^41]  |
| [[Delay Execution\|T1678]] | Delay Execution | [Mustang Panda](https://attack.mitre.org/groups/G0129) has delayed the execution of payloads leveraging ping echo requests `cmd /c ping 8.8.8.8 -n 70&&"%temp%\<legitimate executable>"`.[^50] [^8]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Mustang Panda](https://attack.mitre.org/groups/G0129)'s [PlugX](https://attack.mitre.org/software/S0013) variant has created a hidden folder on USB drives named `RECYCLE.BIN` to store malicious executables and collected data.[^45]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also modified file attributes to `hidden` and `system`.[^50]  |
| [[Mshta\|T1218.005]] | Mshta | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used mshta.exe to launch collection scripts.[^2]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged obfuscated Windows API function calls that were concealed as unique names, or hashes of the Windows API.[^50]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged the legitimate email marketing service SMTP2Go for phishing campaigns.[^41]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also created fake Google accounts to distribute malware via spear-phishing emails.[^42]   [Mustang Panda](https://attack.mitre.org/groups/G0129) has also created accounts for spearphishing operations including the use of services such as Proton Mail.[^37] [^33]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Mustang Panda](https://attack.mitre.org/groups/G0129) has installed TeamViewer on targeted systems.[^2]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Mustang Panda](https://attack.mitre.org/groups/G0129) utilized “Hdump” to dump credentials from memory.[^31]  |
| [[DCSync\|T1003.006]] | DCSync | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged [Mimikatz](https://attack.mitre.org/software/S0002) DCSync feature to obtain user credentials.[^31]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `InstallUtil.exe` to execute a malicious Beacon stager.[^32]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [Mustang Panda](https://attack.mitre.org/groups/G0129) has compromised legitimate email accounts to use in their spear-phishing operations.[^42]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used RAR to create password-protected archives of collected documents prior to exfiltration.[^2] [^45]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has used WinRAR “Rar.exe” to archive stolen files before exfiltration.[^29]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used [TONESHELL](https://attack.mitre.org/software/S1239) and post-exploitation tools such as RemCom and [Impacket](https://attack.mitre.org/software/S0357) to execute WinRAR `rar.exe` to archive files for exfiltration.[^31]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Mustang Panda](https://attack.mitre.org/groups/G0129) has deleted registry keys that store data and maintained persistence.[^50]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mustang Panda](https://attack.mitre.org/groups/G0129) has communicated with its C2 via HTTP POST requests.[^32] [^2] [^15] [^4] [^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has queried Active Directory for computers using [AdFind](https://attack.mitre.org/software/S0552).[^31]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized SharpNBTScan to scan the victim environment.[^29]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged [AdFind](https://attack.mitre.org/software/S0552) to enumerate domain groups.[^31]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized TLS record headers in network packets to impersonate various versions of TLS protocols to blend in with legitimate network traffic.  [Mustang Panda](https://attack.mitre.org/groups/G0129) has used FakeTLS to communicate with its C2 servers.[^47]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used FTP to exfiltrate archive files.[^31]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Mustang Panda](https://attack.mitre.org/groups/G0129) has delivered malicious links to their intended targets.[^37] [^33] [^6]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has distributed spear-phishing emails with embedded links that direct the victim to a malicious archive hosted on Google or Dropbox.[^42]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Mustang Panda](https://attack.mitre.org/groups/G0129) has exfiltrated stolen data and files to its C2 server.[^34] [^51] [^8]  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged legitimate software tools such as AntiVirus Agents, Security Services, and App Development tools to execute scripts and to side-load dlls.[^31] [^20]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [Mustang Panda](https://attack.mitre.org/groups/G0129) leveraged a captive portal hijack that redirected the victim to a webpage that prompted the victim to download a malicious payload.[^21]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used [China Chopper](https://attack.mitre.org/software/S0020) web shells to maintain access to victims’ environments.[^31]  |
| [[IDE Extensions\|T1176.002]] | IDE Extensions | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged Visual Studio Code’s (VSCode) embedded reverse shell feature using the command `code.exe tunnel` to execute code and deliver additional payloads.[^29]  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used revoked code signing certificates for its malicious payloads.[^7]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used a customized [PlugX](https://attack.mitre.org/software/S0013) variant which could spread through USB connections.[^45]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Mustang Panda](https://attack.mitre.org/groups/G0129) has executed HTA files via cmd.exe, and used batch scripts for collection.[^32] [^45]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized cmd.exe to execute commands on an infected host such as `cmd.exe /c ping.exe 8.8.8.8 -n 70&&"%temp%\FontEDL.exe"`.[^34]  |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used a customized [PlugX](https://attack.mitre.org/software/S0013) variant which could exfiltrate documents from air-gapped networks.[^45]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Mustang Panda](https://attack.mitre.org/groups/G0129) has harvested credentials from memory of lssas.exe with [Mimikatz](https://attack.mitre.org/software/S0002).[^31]  |
| [[Tool\|T1588.002]] | Tool | [Mustang Panda](https://attack.mitre.org/groups/G0129) has obtained and leveraged publicly-available tools for intrusion activities.[^34] [^31]  |
| [[Digital Certificates\|T1588.004]] | Digital Certificates | [Mustang Panda](https://attack.mitre.org/groups/G0129) has obtained SSL certificates for their C2 domains.[^51] [^21]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Mustang Panda](https://attack.mitre.org/groups/G0129) has encrypted documents with RC4 prior to exfiltration.[^45]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Mustang Panda](https://attack.mitre.org/groups/G0129) will delete their tools and files, and kill processes after their objectives are reached.[^2] [^7]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged `LoadLibrary` to load DLLs.[^50]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `tasklist /v` to determine active process information.[^45]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used [TONESHELL](https://attack.mitre.org/software/S1239) malware to check the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler.[^42]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has gathered system information using `systeminfo`.[^45]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized TCP-based reverse shells using cmd.exe.[^34]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Mustang Panda](https://attack.mitre.org/groups/G0129) has exploited CVE-2017-0199 in Microsoft Word to execute code.[^27]  |
| [[Executable Installer File Permissions Weakness\|T1574.005]] | Executable Installer File Permissions Weakness | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged legitimate software installer executables such as Setup Factory “IRSetup.exe” to drop and execute their payload.[^20]  |
| [[Stage Capabilities\|T1608]] | Stage Capabilities | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used servers under their control to validate tracking pixels sent to phishing victims.[^41]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Mustang Panda](https://attack.mitre.org/groups/G0129) has embedded debug strings with messages to distract analysts.[^42]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also made calls to Windows API `CheckRemoteDebuggerPresent` and exits if it detects a debugger.[^25]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used spearphishing attachments to deliver initial access payloads.[^34] [^11] [^54] [^37] [^33] [^49] [^15] [^13] [^43]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also delivered archive files such as RAR and ZIP files containing legitimate EXEs and malicious DLLs.[^54] [^37] [^33]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used [Wevtutil](https://attack.mitre.org/software/S0645) to gather Windows Security Event Logs.[^31]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has searched the entire target system for DOC, DOCX, PPT, PPTX, XLS, XLSX, and PDF files.[^45] [^31]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Mustang Panda](https://attack.mitre.org/groups/G0129) has searched the victim system for the `InstallUtil.exe` program and its version.[^32]  |
| [[Domains\|T1583.001]] | Domains | [Mustang Panda](https://attack.mitre.org/groups/G0129) has acquired C2 domains prior to operations.[^2] [^11] [^54] [^15] [^20] [^21] [^4] [^35] [^6]  |
| [[DLL\|T1574.001]] | DLL | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used a legitimately signed executable to execute a malicious payload within a DLL file.[^50] [^32] [^34] [^52] [^51] [^15] [^31] [^20] [^42] [^43] [^4] [^8] [^7] [^47]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has abused legitimate executables to side-load malicious DLLs.[^11] [^54] [^37] [^33] [^21]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [Mustang Panda](https://attack.mitre.org/groups/G0129)'s custom ORat tool uses a WMI event consumer to maintain persistence.[^2]  |
| [[Native API\|T1106]] | Native API | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used various Windows API calls during execution and defense evasion.[^50] [^52] [^54] [^37] [^33] [^20] [^42] [^21] [^35] [^25] [^7] [^47]  |
| [[NTDS\|T1003.003]] | NTDS | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used vssadmin to create a volume shadow copy and retrieve the NTDS.dit file. [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used `reg save` on the SYSTEM file Registry location to help extract the NTDS.dit file.[^2] [^31]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized meterpreter shellcode.[^34]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used valid legitimate digital signatures and certificates to evade detection.[^11] [^54] [^21] [^4] [^35] [^8] [^7] [^47]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Mustang Panda](https://attack.mitre.org/groups/G0129) has delivered initial payloads hidden using archives and encoding measures.[^32] [^34] [^2] [^15] [^27] [^42] [^43] [^41] [^4]  [^8] [^7] [^47]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized opaque predicates in payloads to hinder analysis.[^50]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Mustang Panda](https://attack.mitre.org/groups/G0129) has created the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run\AdobelmdyU` to maintain persistence.[^43]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also established persistence via the registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^51] [^25]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Mustang Panda](https://attack.mitre.org/groups/G0129) used custom batch scripts to collect files automatically from a targeted system.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mustang Panda](https://attack.mitre.org/groups/G0129) has downloaded additional executables following the initial infection stage.[^50] [^34] [^15] [^8]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged Visual Studio Code `code.exe` and Dev Tunnels using `DevTunnel.exe` to propagate additional tools and payloads.[^29]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Mustang Panda](https://attack.mitre.org/groups/G0129) has stored collected credential files in `c:\windows\temp` prior to exfiltration. [Mustang Panda](https://attack.mitre.org/groups/G0129) has also stored documents for exfiltration in a hidden folder on USB drives.[^2] [^45]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Mustang Panda](https://attack.mitre.org/groups/G0129) has executed a JavaScript payload utilizing wscript.exe on the endpoint.[^34]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used malicious PowerShell scripts to enable execution.[^32] [^27] [^29]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used junk code within their DLL files to hinder analysis.[^50] [^45]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Mustang Panda](https://attack.mitre.org/groups/G0129) has modified file timestamps from the export address table (EAT) in malware to make it difficult to identify creation times.[^35]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Mustang Panda](https://attack.mitre.org/groups/G0129) has sent malicious files requiring direct victim interaction to execute.[^32] [^11] [^37] [^33] [^45] [^49] [^15] [^27] [^41] [^7]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged executable files that display decoy documents to the victim to provide a resemblance of legitimacy with customized themes related to the victim.[^50] [^34] [^54] [^51] [^13] [^20] [^42] [^4] [^35] [^8] [^25]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged OpenSSH (sshd.exe) to execute commands, transfer files and spread across the environment communicating over SMB port 445.[^29]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Mustang Panda](https://attack.mitre.org/groups/G0129) has masqueraded malicious executables as legitimate files that download [PlugX](https://attack.mitre.org/software/S0013) malware.[^51] [^8]  |
| [[Double File Extension\|T1036.007]] | Double File Extension | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used an additional filename extension to hide the true file type.[^27] [^32]  |
| [[Web Service\|T1102]] | Web Service | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used DropBox URLs to deliver variants of [PlugX](https://attack.mitre.org/software/S0013).[^41]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used Google Drive to host malicious downloads.[^37]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized a magic value in C2 communications and only executes in memory when response packets match specific values of “17 03 03” or “46 77 4d”.[^11]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used names like `adobeupdate.dat` and `PotPlayerDB.dat` to disguise [PlugX](https://attack.mitre.org/software/S0013), and a file named `OneDrive.exe` to load a [Cobalt Strike](https://attack.mitre.org/software/S0154) payload.[^15]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also masqueraded legitimate browser plugin updates to include AdobePlugins.exe.[^21]  |
| [[Malware\|T1587.001]] | Malware | [Mustang Panda](https://attack.mitre.org/groups/G0129) has developed custom malware for use in their operations.[^50] [^34]  |
| [[LNK Icon Smuggling\|T1027.012]] | LNK Icon Smuggling | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized LNK files to hide malicious scripts for execution.[^34] [^25]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged LNK files that were programmed to display a PDF icon to entice the victim to click on the file to execute an office.exe binary.[^11]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Impacket\|S0357]] | Impacket | [Mustang Panda](https://attack.mitre.org/groups/G0129) leveraged [Impacket](https://attack.mitre.org/software/S0357) to gather information about the network, discover devices, users and query directories on remote machines to identify files to exfiltrate.[^31]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^31]   |
| [[NBTscan\|S0590]] | NBTscan | [^2] [^31]  |
| [[AdFind\|S0552]] | AdFind | [Mustang Panda](https://attack.mitre.org/groups/G0129) has utilized [AdFind](https://attack.mitre.org/software/S0552) for enumerating domain groups, users, and computers.[^31]  |
| [[Wevtutil\|S0645]] | Wevtutil | [Mustang Panda](https://attack.mitre.org/groups/G0129) has leveraged [Wevtutil](https://attack.mitre.org/software/S0645) to gather information about usernames and Windows Security Event logs.[^31]  |
| [[RCSession\|S0662]] | RCSession | [^2]  |
| [[PAKLOG\|S1233]] | PAKLOG | [^7]  |
| [[TONESHELL\|S1239]] | TONESHELL | [^11] [^33] [^40] [^31] [^20] [^42] [^1] [^47] [^29]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [^52] [^35]  |
| [[STATICPLUGIN\|S1238]] | STATICPLUGIN | [^21]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [^34] [^11] [^54] [^37] [^33] [^13] [^42] [^35] [^23]  |
| [[CANONSTAGER\|S1237]] | CANONSTAGER | [^21]  |
| [[CLAIMLOADER\|S1236]] | CLAIMLOADER | [^37] [^33]  |
| [[China Chopper\|S0020]] | China Chopper | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used [China Chopper](https://attack.mitre.org/software/S0020) web shells to maintain access to victims’ environments.[^31]  |
| [[SplatDropper\|S1232]] | SplatDropper | [^7]  |
| [[PlugX\|S0013]] | PlugX | [^50] [^32] [^2] [^51] [^45] [^15] [^27] [^41] [^8]  |
| [[CorKLOG\|S1235]] | CorKLOG | [^7]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^50] [^32] [^2] [^15] [^31] [^27] [^6]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^50] [^15] [^27]  |
| [[HIUPAN\|S1230]] | HIUPAN | [^33] [^13]  |
| [[StarProxy\|S1227]] | StarProxy | [^47]  |
| [[ShadowPad\|S0596]] | ShadowPad | [^31]  |
| [[SplatCloak\|S1234]] | SplatCloak | [^7]  |



## References

[^1]: [Trend Micro Mustang Panda Earth Preta TONESHELL June 2023](https://www.trendmicro.com/en_us/research/23/f/behind-the-scenes-unveiling-the-hidden-workings-of-earth-preta.html)


[^2]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)


[^3]: Red Lich


[^4]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


[^5]: [BlackBerry MUSTANG PANDA October 2022](https://blogs.blackberry.com/en/2022/10/mustang-panda-abuses-legitimate-apps-to-target-myanmar-based-victims)


[^6]: [McAfee Dianxun March 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-dianxun.pdf)


[^7]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^8]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^9]: LUMINOUS MOTH


[^10]: STATELY TAURUS


[^11]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)


[^12]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^13]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^14]: CAMARO DRAGON


[^15]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^16]: Mustang Panda


[^17]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


[^18]: TANTALUM


[^19]: EARTH PRETA


[^20]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)


[^21]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^22]: RedDelta


[^23]: [PaloAlto MUSTANG PANDA PUBLOAD MARCH 2024](https://unit42.paloaltonetworks.com/chinese-apts-target-asean-entities/)


[^24]: HIVE0154


[^25]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)


[^26]: UNC6384


[^27]: [Crowdstrike MUSTANG PANDA June 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)


[^28]: ClumsyToad


[^29]: [Unit42 Chinese VSCode 06 September 2024](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)


[^30]: TEMP.Hex


[^31]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^32]: [Anomali MUSTANG PANDA October 2019](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)


[^33]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^34]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^35]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^36]: FIREANT


[^37]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)


[^38]: TWILL TYPHOON


[^39]: BRONZE PRESIDENT


[^40]: [ATTACKIQ MUSTANG PANDA TONESHELL March 2023](https://www.attackiq.com/2023/03/23/emulating-the-politically-motivated-chinese-apt-mustang-panda/)


[^41]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^42]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^43]: [Proofpoint TA416 November 2020](https://www.proofpoint.com/us/blog/threat-insight/ta416-goes-ground-and-returns-golang-plugx-malware-loader)


[^44]: [HorseShell](https://research.checkpoint.com/2023/the-dragon-who-sold-his-camaro-analyzing-custom-router-implant/)


[^45]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^46]: TA416


[^47]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


[^48]: [Microsoft Naming Conventions Frequently Updated](https://learn.microsoft.com/en-us/unified-secops-platform/microsoft-threat-actor-naming)


[^49]: [Google TAG Ukraine Threat Landscape March 2022](https://blog.google/threat-analysis-group/update-threat-landscape-ukraine)


[^50]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^51]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^52]: [Broadcom](https://www.broadcom.com/support/security-center/protection-bulletin/bookworm-malware-linked-to-fireant-aka-stately-tarurus-activity-observed-in-southeast-asia)


[^53]: [PWC UK MUSTANG PANDA RED LICH February 2021](https://www.pwc.co.uk/cyber-security/pdf/pwc-cyber-threats-2020-a-year-in-retrospect.pdf)


[^54]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)


