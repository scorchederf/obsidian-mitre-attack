---
aliases: 
    - S0488
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0488-CrackMapExec
---

## Description

[[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]], or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] collects Active Directory information to conduct lateral movement through targeted networks.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.002-Security_Account_Manager\|T1003.002]] | Security Account Manager | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can dump usernames and hashed passwords from the SAM.[^1]  |
| [[kb/mitre/attack/techniques/T1003.003-NTDS\|T1003.003]] | NTDS | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can dump hashed passwords associated with Active Directory using Windows' Directory Replication Services API (DRSUAPI), or Volume Shadow Copy.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can dump hashed passwords from LSA secrets for the targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can collect DNS information from the targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover active IP addresses, along with the machine name, within a targeted network.[^1]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can execute remote commands using Windows Management Instrumentation.[^1] 	 |
| [[kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover active sessions for a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1053.002-At\|T1053.002]] | At | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can set a scheduled task on the target system to execute commands remotely using [[kb/mitre/attack/software/S0110-at\|at]].[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can execute PowerShell commands via WMI.[^1]  |
| [[kb/mitre/attack/techniques/T1069.002-Domain_Groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can gather the user accounts within domain groups.[^1]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover specified filetypes and log files on a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can enumerate the domain user accounts on a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1110-Brute_Force\|T1110]] | Brute Force | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can brute force supplied user credentials across a network range.[^1]  |
| [[kb/mitre/attack/techniques/T1110.001-Password_Guessing\|T1110.001]] | Password Guessing | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can brute force passwords for a specified user on a single target system or across an entire network.[^1]  |
| [[kb/mitre/attack/techniques/T1110.003-Password_Spraying\|T1110.003]] | Password Spraying | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can brute force credential authentication by using a supplied list of usernames and a single password.[^1]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can create a registry key using wdigest.[^1]  |
| [[kb/mitre/attack/techniques/T1135-Network_Share_Discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can enumerate the shared folders and associated permissions for a targeted network.[^1]  |
| [[kb/mitre/attack/techniques/T1201-Password_Policy_Discovery\|T1201]] | Password Policy Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover the password policies applied to the target system.[^1]  |
| [[kb/mitre/attack/techniques/T1550.002-Pass_the_Hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can pass the hash to authenticate via SMB.[^1]  |
| [[kb/mitre/attack/techniques/T1680-Local_Storage_Discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can enumerate the system drives and associated system name.[^1]  |





> [!info]- References
> [^1]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


