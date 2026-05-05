---
aliases: 
    - S0363
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0363-Empire
---

## Description

[[kb/mitre/attack/software/S0363-Empire\|Empire]] is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] for Windows and Python for Linux/macOS. [[kb/mitre/attack/software/S0363-Empire\|Empire]] was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.[^3] [^6] [^5] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains an implementation of [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] to gather credentials from memory.[^6]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1020-Automated_Exfiltration\|T1020]] | Automated Exfiltration | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to automatically send collected data back to the threat actors' C2.[^2]  |
| [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|T1021.003]] | Distributed Component Object Model | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can utilize `Invoke-DCOM` to leverage remote COM execution for lateral movement.[^6]  |
| [[kb/mitre/attack/techniques/T1021.004-SSH\|T1021.004]] | SSH | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains modules for executing commands over SSH as well as in-memory VNC agent injection.[^6]  |
| [[kb/mitre/attack/techniques/T1027.010-Command_Obfuscation\|T1027.010]] | Command Obfuscation | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to obfuscate commands using `Invoke-Obfuscation`.[^6]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate the username on targeted hosts.[^2]  |
| [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can be used to conduct packet captures on target hosts.[^6]  |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can send data gathered from a target through the command and control channel.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can perform port scans from an infected host.[^6]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use WMI to deliver a payload to a remote host.[^6]   |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate the current network connections of a host.[^6]  |
| [[kb/mitre/attack/techniques/T1053.005-Scheduled_Task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has modules to interact with the Windows task scheduler.[^6]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^6]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes keylogging capabilities for Windows, Linux, and macOS systems.[^6]  |
| [[kb/mitre/attack/techniques/T1056.004-Credential_API_Hooking\|T1056.004]] | Credential API Hooking | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains some modules that leverage API hooking to carry out tasks, such as netripper.[^6]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can find information about processes running on local and remote systems.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|T1059]] | Command and Scripting Interpreter | [[kb/mitre/attack/software/S0363-Empire\|Empire]] uses a command-line interface to interact with systems.[^6]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0363-Empire\|Empire]] leverages PowerShell for the majority of its client-side agent tasks. [[kb/mitre/attack/software/S0363-Empire\|Empire]] also contains the ability to conduct PowerShell remoting with the `Invoke-PSRemoting` module.[^6] [^3]  |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has modules for executing scripts.[^6]  |
| [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|T1068]] | Exploitation for Privilege Escalation | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can exploit vulnerabilities such as MS16-032 and MS16-135.[^6]  |
| [[kb/mitre/attack/techniques/T1070.006-Timestomp\|T1070.006]] | Timestomp | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can timestomp any files or payloads placed on a target machine to help them blend in.[^6]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can conduct command and control over protocols like HTTP and HTTPS.[^6]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes various modules for finding files of interest on hosts and network shares.[^6]  |
| [[kb/mitre/attack/techniques/T1087.001-Local_Account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can acquire local and domain user account information.[^6]  |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can acquire local and domain user account information.[^6] [^7]  |
| [[kb/mitre/attack/techniques/T1102.002-Bidirectional_Communication\|T1102.002]] | Bidirectional Communication | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use Dropbox and GitHub for C2.[^6]  |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can upload and download to and from a victim machine.[^6]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains a variety of enumeration modules that have an option to use API calls to carry out tasks.[^6]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0363-Empire\|Empire]] is capable of capturing screenshots on Windows and macOS systems.[^6]  |
| [[kb/mitre/attack/techniques/T1114.001-Local_Email_Collection\|T1114.001]] | Local Email Collection | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to collect emails on a target system.[^6]  |
| [[kb/mitre/attack/techniques/T1115-Clipboard_Data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can harvest clipboard data on both Windows and macOS systems.[^6]  |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can automatically gather the username, domain name, machine name, and other information from a compromised system.[^2]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can capture webcam data on Windows and macOS systems.[^6]  |
| [[kb/mitre/attack/techniques/T1127.001-MSBuild\|T1127.001]] | MSBuild | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use built-in modules to abuse trusted utilities like MSBuild.exe.[^6] <br> |
| [[kb/mitre/attack/techniques/T1134-Access_Token_Manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-TokenManipulation` to manipulate access tokens.[^6]  |
| [[kb/mitre/attack/techniques/T1134.002-Create_Process_with_Token\|T1134.002]] | Create Process with Token | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use `Invoke-RunAs` to make tokens.[^6]  |
| [[kb/mitre/attack/techniques/T1134.005-SID-History_Injection\|T1134.005]] | SID-History Injection | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can add a SID-History to a user if on a domain controller.[^6]  |
| [[kb/mitre/attack/techniques/T1135-Network_Share_Discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can find shared drives on the local system.[^6]  |
| [[kb/mitre/attack/techniques/T1136.001-Local_Account\|T1136.001]] | Local Account | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has a module for creating a local user if permissions allow.[^6]  |
| [[kb/mitre/attack/techniques/T1136.002-Domain_Account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has a module for creating a new domain user if permissions allow.[^6]  |
| [[kb/mitre/attack/techniques/T1210-Exploitation_of_Remote_Services\|T1210]] | Exploitation of Remote Services | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has a limited number of built-in modules for exploiting remote SMB, JBoss, and Jenkins servers.[^6]  |
| [[kb/mitre/attack/techniques/T1217-Browser_Information_Discovery\|T1217]] | Browser Information Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has the ability to gather browser data such as bookmarks and visited sites.[^6]  |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has modules for enumerating domain trusts.[^6]  |
| [[kb/mitre/attack/techniques/T1484.001-Group_Policy_Modification\|T1484.001]] | Group Policy Modification | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use `New-GPOImmediateTask` to modify a GPO that will install and execute a malicious [[kb/mitre/attack/techniques/T1053-Scheduled_Task_Job\|Scheduled Task/Job]].[^6]  |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate antivirus software on the target.[^6]  |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can utilize built-in modules to modify service binaries and restore them to their original state.[^6]  |
| [[kb/mitre/attack/techniques/T1546.008-Accessibility_Features\|T1546.008]] | Accessibility Features | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can leverage WMI debugging to remotely replace binaries like sethc.exe, Utilman.exe, and Magnify.exe with cmd.exe.[^6]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can modify the registry run keys `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` and `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^6]  |
| [[kb/mitre/attack/techniques/T1547.005-Security_Support_Provider\|T1547.005]] | Security Support Provider | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate Security Support Providers (SSPs) as well as utilize [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Install-SSP` and `Invoke-Mimikatz` to install malicious SSPs and log authentication events.[^6]  |
| [[kb/mitre/attack/techniques/T1547.009-Shortcut_Modification\|T1547.009]] | Shortcut Modification | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can persist by modifying a .LNK file to include a backdoor.[^6]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes various modules to attempt to bypass UAC for escalation of privileges.[^6]  |
| [[kb/mitre/attack/techniques/T1550.002-Pass_the_Hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can perform pass the hash attacks.[^6]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use various modules to search for files containing passwords.[^6]  |
| [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|T1552.004]] | Private Keys | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use modules like `Invoke-SessionGopher` to extract private key and session information.[^6]  |
| [[kb/mitre/attack/techniques/T1555.001-Keychain\|T1555.001]] | Keychain | [[kb/mitre/attack/software/S0363-Empire\|Empire]] uses the command `/usr/bin/security dump-keychain -d` to read the keychain credential.[^9]  |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use modules that extract passwords from common web browsers such as Firefox and Chrome.[^6]  |
| [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^6] [^8]  |
| [[kb/mitre/attack/techniques/T1558.001-Golden_Ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can leverage its implementation of [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] to obtain and use golden tickets.[^6]  |
| [[kb/mitre/attack/techniques/T1558.002-Silver_Ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can leverage its implementation of [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] to obtain and use silver tickets.[^6]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0363-Empire\|Empire]] uses [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-Kerberoast` to request service tickets and return crackable ticket hashes.[^6]  |
| [[kb/mitre/attack/techniques/T1560-Archive_Collected_Data\|T1560]] | Archive Collected Data | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can ZIP directories on the target system.[^6]  |
| [[kb/mitre/attack/techniques/T1567.001-Exfiltration_to_Code_Repository\|T1567.001]] | Exfiltration to Code Repository | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use GitHub for data exfiltration.[^6]  |
| [[kb/mitre/attack/techniques/T1567.002-Exfiltration_to_Cloud_Storage\|T1567.002]] | Exfiltration to Cloud Storage | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use Dropbox for data exfiltration.[^6]  |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] to execute a payload on a remote host.[^6]  |
| [[kb/mitre/attack/techniques/T1573.002-Asymmetric_Cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use TLS to encrypt its C2 channel.[^6]  |
| [[kb/mitre/attack/techniques/T1574.001-DLL\|T1574.001]] | DLL | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains modules that can discover and exploit various DLL hijacking opportunities.[^6]  |
| [[kb/mitre/attack/techniques/T1574.004-Dylib_Hijacking\|T1574.004]] | Dylib Hijacking | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has a dylib hijacker module that generates a malicious dylib given the path to a legitimate dylib of a vulnerable application.[^6]  |
| [[kb/mitre/attack/techniques/T1574.007-Path_Interception_by_PATH_Environment_Variable\|T1574.007]] | Path Interception by PATH Environment Variable | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains modules that can discover and exploit path interception opportunities in the PATH environment variable.[^6]  |
| [[kb/mitre/attack/techniques/T1574.008-Path_Interception_by_Search_Order_Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains modules that can discover and exploit search order hijacking vulnerabilities.[^6]  |
| [[kb/mitre/attack/techniques/T1574.009-Path_Interception_by_Unquoted_Path\|T1574.009]] | Path Interception by Unquoted Path | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains modules that can discover and exploit unquoted path vulnerabilities.[^6]  |
| [[kb/mitre/attack/techniques/T1615-Group_Policy_Discovery\|T1615]] | Group Policy Discovery | [[kb/mitre/attack/software/S0363-Empire\|Empire]] includes various modules for enumerating Group Policy.[^6]  |





> [!info]- References
> [^1]: EmPyre

> [^2]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^3]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)

> [^4]: PowerShell Empire

> [^5]: [GitHub ATTACK Empire](https://github.com/dstepanic/attck_empire)

> [^6]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^7]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)

> [^8]: [GitHub Inveigh](https://github.com/Kevin-Robertson/Inveigh)

> [^9]: [Empire Keychain Decrypt](https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/collection/osx/keychaindump_decrypt.py)


