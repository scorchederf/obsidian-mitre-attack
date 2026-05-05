---
aliases: 
    - S0194
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0194-PowerSploit
---

## Description

[[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] is an open source, offensive security framework comprised of [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. [^6]  [^3]  [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials using [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]].[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1012-Query_Registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1027.005-Indicator_Removal_from_Tools\|T1027.005]] | Indicator Removal from Tools | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Find-AVSignature` AntivirusBypass module can be used to locate single byte anti-virus signatures.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1027.010-Command_Obfuscation\|T1027.010]] | Command Obfuscation | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of ScriptModification modules that compress and encode scripts and payloads.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-WmiCommand` CodeExecution module uses WMI to execute and retrieve the output from a PowerShell payload.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1053.005-Scheduled_Task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `New-UserPersistenceOption` Persistence argument can be used to establish via a [[kb/mitre/attack/techniques/T1053-Scheduled_Task_Job\|Scheduled Task/Job]].[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1055.001-Dynamic-link_Library_Injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of CodeExecution modules that inject code (DLL, shellcode) into a process.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-Keystrokes` Exfiltration module can log keystrokes.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] modules are written in and executed via PowerShell.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1087.001-Local_Account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-ProcessTokenGroup` Privesc-PowerUp module can enumerate all SIDs associated with its current token.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-TimedScreenshot` Exfiltration module can take screenshots at regular intervals.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1123-Audio_Capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-MicrophoneAudio` Exfiltration module can record system microphone audio.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1134-Access_Token_Manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-TokenManipulation` Exfiltration module can be used to manipulate tokens.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] has modules such as `Get-NetDomainTrust` and `Get-NetForestTrust` to enumerate domain and forest trusts.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `New-UserPersistenceOption` Persistence argument can be used to establish via the `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` Registry key.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1547.005-Security_Support_Provider\|T1547.005]] | Security Support Provider | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Install-SSP` Persistence module can be used to establish by installing a SSP DLL.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1552.002-Credentials_in_Registry\|T1552.002]] | Credentials in Registry | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] has several modules that search the Windows Registry for stored credentials: `Get-UnattendedInstallFile`, `Get-Webconfig`, `Get-ApplicationHost`, `Get-SiteListPassword`, `Get-CachedGPPPassword`, and `Get-RegistryAutoLogon`.[^4]  |
| [[kb/mitre/attack/techniques/T1552.006-Group_Policy_Preferences\|T1552.006]] | Group Policy Preferences | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials from Group Policy Preferences.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1555.004-Windows_Credential_Manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials from Windows vault credential objects.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-Kerberoast` module can request service tickets and return crackable ticket hashes.[^1] [^5]  |
| [[kb/mitre/attack/techniques/T1574.001-DLL\|T1574.001]] | DLL | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit DLL hijacking opportunities in services and processes.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1574.007-Path_Interception_by_PATH_Environment_Variable\|T1574.007]] | Path Interception by PATH Environment Variable | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit path interception opportunities in the PATH environment variable.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1574.008-Path_Interception_by_Search_Order_Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit search order hijacking vulnerabilities.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1574.009-Path_Interception_by_Unquoted_Path\|T1574.009]] | Path Interception by Unquoted Path | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit unquoted path vulnerabilities.[^6] [^2]  |
| [[kb/mitre/attack/techniques/T1620-Reflective_Code_Loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] reflectively loads a Windows PE file into a process.[^6] [^2]  |





> [!info]- References
> [^1]: [PowerSploit Invoke Kerberoast](https://powersploit.readthedocs.io/en/latest/Recon/Invoke-Kerberoast/)

> [^2]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^3]: [PowerShellMagazine PowerSploit July 2014](http://www.powershellmagazine.com/2014/07/08/powersploit/)

> [^4]: [Pentestlab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)

> [^5]: [Harmj0y Kerberoast Nov 2016](https://blog.harmj0y.net/powershell/kerberoasting-without-mimikatz/)

> [^6]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


