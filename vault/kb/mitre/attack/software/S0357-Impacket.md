---
aliases: 
    - S0357
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0357-Impacket
---

## Description

[[kb/mitre/attack/software/S0357-Impacket\|Impacket]] is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.[^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | SecretsDump and [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] modules within [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can perform credential dumping to obtain account and password information.[^2]  |
| [[kb/mitre/attack/techniques/T1003.002-Security_Account_Manager\|T1003.002]] | Security Account Manager | SecretsDump and [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] modules within [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can perform credential dumping to obtain account and password information.[^2]  |
| [[kb/mitre/attack/techniques/T1003.003-NTDS\|T1003.003]] | NTDS | SecretsDump and [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] modules within [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can perform credential dumping to obtain account and password information from NTDS.dit.[^2]  |
| [[kb/mitre/attack/techniques/T1003.004-LSA_Secrets\|T1003.004]] | LSA Secrets | SecretsDump and [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]] modules within [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can perform credential dumping to obtain account and password information.[^2]  |
| [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can be used to sniff network traffic via an interface or raw socket.[^2]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]]'s `wmiexec` module can be used to execute commands through WMI.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] modules like ntlmrelayx and smbrelayx can be used in conjunction with [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|Network Sniffing]] and [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|Name Resolution Poisoning and SMB Relay]] to gather NetNTLM credentials for [[kb/mitre/attack/techniques/T1110-Brute_Force\|Brute Force]] or relay attacks that can gain code execution.[^2]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] modules like GetUserSPNs can be used to get Service Principal Names (SPNs) for user accounts. The output is formatted to be compatible with cracking tools like John the Ripper and Hashcat.[^2]  |
| [[kb/mitre/attack/techniques/T1558.005-Ccache_Files\|T1558.005]] | Ccache Files | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] tools – such as `getST.py` or `ticketer.py` – can be used to steal or forge Kerberos tickets using ccache files given a password, hash, aesKey, or TGT.[^4] [^3]  |
| [[kb/mitre/attack/techniques/T1569.002-Service_Execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] contains various modules emulating other service execution tools such as [[kb/mitre/attack/software/S0029-PsExec\|PsExec]].[^2]  |
| [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.[^1]  |





> [!info]- References
> [^1]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)

> [^2]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)

> [^3]: [on security kerberos linux](https://www.onsecurity.io/blog/abusing-kerberos-from-linux/)

> [^4]: [Kerberos GNU/Linux](https://adepts.of0x.cc/kerberos-thievery-linux/)


