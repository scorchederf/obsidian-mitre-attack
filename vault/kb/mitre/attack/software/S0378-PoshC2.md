---
aliases: 
    - S0378
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0378-PoshC2
---

## Description

[[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]]. Although [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] to gather credentials from memory.[^2]  |
| [[kb/mitre/attack/techniques/T1007-System_Service_Discovery\|T1007]] | System Service Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate service and service permission information.[^2]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate network adapter information.[^2]  |
| [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for taking packet captures on compromised hosts.[^2]  |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can perform port scans from an infected host.[^2]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has a number of modules that use WMI to execute tasks.[^2]  |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0104-netstat\|netstat]] to enumerate TCP and UDP connections.[^2]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^2]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has modules for keystroke logging and capturing credentials from spoofed Outlook authentication messages.[^2]  |
| [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|T1068]] | Exploitation for Privilege Escalation | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules for local privilege escalation exploits such as CVE-2016-9192 and CVE-2016-0099.[^2]  |
| [[kb/mitre/attack/techniques/T1069.001-Local_Groups\|T1069.001]] | Local Groups | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules, such as `Get-LocAdm` for enumerating permission groups.[^2]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use protocols like HTTP/HTTPS for command and control traffic.[^2]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^2]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^2]  |
| [[kb/mitre/attack/techniques/T1087.001-Local_Account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate local and domain user account information.[^2]  |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate local and domain user account information.[^2]  |
| [[kb/mitre/attack/techniques/T1090-Proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules that allow for use of proxies in command and control.[^2]  |
| [[kb/mitre/attack/techniques/T1110-Brute_Force\|T1110]] | Brute Force | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has modules for brute forcing local administrator and AD user accounts.[^2]  |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for recursively parsing through files and directories to gather valid credit card numbers.[^2]  |
| [[kb/mitre/attack/techniques/T1134-Access_Token_Manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use Invoke-TokenManipulation for manipulating tokens.[^2]  |
| [[kb/mitre/attack/techniques/T1134.002-Create_Process_with_Token\|T1134.002]] | Create Process with Token | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use Invoke-RunAs to make tokens.[^2]  |
| [[kb/mitre/attack/techniques/T1201-Password_Policy_Discovery\|T1201]] | Password Policy Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use `Get-PassPol` to enumerate the domain password policy.[^2]  |
| [[kb/mitre/attack/techniques/T1210-Exploitation_of_Remote_Services\|T1210]] | Exploitation of Remote Services | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for exploiting SMB via EternalBlue.[^2]  |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has modules for enumerating domain trusts.[^2]  |
| [[kb/mitre/attack/techniques/T1546.003-Windows_Management_Instrumentation_Event_Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has the ability to persist on a system using WMI events.[^2]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can utilize multiple methods to bypass UAC.[^2]  |
| [[kb/mitre/attack/techniques/T1550.002-Pass_the_Hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has a number of modules that leverage pass the hash for lateral movement.[^2]  |
| [[kb/mitre/attack/techniques/T1552.001-Credentials_In_Files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains modules for searching for passwords in local and remote files.[^2]  |
| [[kb/mitre/attack/techniques/T1555-Credentials_from_Password_Stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can decrypt passwords stored in the RDCMan configuration file.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^2]  |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for compressing data using ZIP.[^2]  |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0029-PsExec\|PsExec]] for remote execution.[^2]  |





> [!info]- References
> [^1]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)

> [^2]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


