---
aliases: 
    - T1547
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1547-Boot_or_Logon_Autostart_Execution
tactic: 
     - Persistence - Privilege Escalation
platforms:
     - Linux - macOS - Windows - Network Devices
permissions required:
     - none
---

## Description

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.[^2] [^3] [^6] [^4] [^1]  These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.<br><br>Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder |
| [[kb/mitre/attack/techniques/T1547.002-Authentication_Package\|T1547.002]] | Authentication Package |
| [[kb/mitre/attack/techniques/T1547.003-Time_Providers\|T1547.003]] | Time Providers |
| [[kb/mitre/attack/techniques/T1547.004-Winlogon_Helper_DLL\|T1547.004]] | Winlogon Helper DLL |
| [[kb/mitre/attack/techniques/T1547.005-Security_Support_Provider\|T1547.005]] | Security Support Provider |
| [[kb/mitre/attack/techniques/T1547.006-Kernel_Modules_and_Extensions\|T1547.006]] | Kernel Modules and Extensions |
| [[kb/mitre/attack/techniques/T1547.007-Re-opened_Applications\|T1547.007]] | Re-opened Applications |
| [[kb/mitre/attack/techniques/T1547.008-LSASS_Driver\|T1547.008]] | LSASS Driver |
| [[kb/mitre/attack/techniques/T1547.009-Shortcut_Modification\|T1547.009]] | Shortcut Modification |
| [[kb/mitre/attack/techniques/T1547.010-Port_Monitors\|T1547.010]] | Port Monitors |
| [[kb/mitre/attack/techniques/T1547.012-Print_Processors\|T1547.012]] | Print Processors |
| [[kb/mitre/attack/techniques/T1547.013-XDG_Autostart_Entries\|T1547.013]] | XDG Autostart Entries |
| [[kb/mitre/attack/techniques/T1547.014-Active_Setup\|T1547.014]] | Active Setup |
| [[kb/mitre/attack/techniques/T1547.015-Login_Items\|T1547.015]] | Login Items |




> [!info]- References
> [^1]: [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)

> [^2]: [Microsoft Run Key](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)

> [^3]: [MSDN Authentication Packages](https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx)

> [^4]: [Cylance Reg Persistence Sept 2013](https://web.archive.org/web/20160214140250/http://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)

> [^5]: [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)

> [^6]: [Microsoft TimeProvider](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)


