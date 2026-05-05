---
aliases: 
    - T1080
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1080-Taint_Shared_Content
tactic: 
     - Lateral Movement
platforms:
     - Windows - SaaS - Linux - macOS - Office Suite
permissions required:
     - none
---

## Description

<br>Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as network drives or internal code repositories. Content stored on network drives or in other shared locations may be tainted by adding malicious programs, scripts, or exploit code to otherwise valid files. Once a user opens the shared tainted content, the malicious portion can be executed to run the adversary's code on a remote system. Adversaries may use tainted shared content to move laterally.<br><br>A directory share pivot is a variation on this technique that uses several other techniques to propagate malware when users access a shared network directory. It uses [[kb/mitre/attack/techniques/T1547.009-Shortcut_Modification\|Shortcut Modification]] of directory .LNK files that use [[kb/mitre/attack/techniques/T1036-Masquerading\|Masquerading]] to look like the real directories, which are hidden through [[kb/mitre/attack/techniques/T1564.001-Hidden_Files_and_Directories\|Hidden Files and Directories]]. The malicious .LNK-based directories have an embedded command that executes the hidden malware file in the directory and then opens the real intended directory so that the user's expected action still occurs. When used with frequently used network directories, the technique may result in frequent reinfections and broad access to systems and potentially to new and higher privileged accounts. [^5] <br><br>Adversaries may also compromise shared network directories through binary infections by appending or prepending its code to the healthy binary on the shared network directory. The malware may modify the original entry point (OEP) of the healthy binary to ensure that it is executed before the legitimate code. The infection could continue to spread via the newly infected file when it is executed by a remote system. These infections may target both binary and non-binary formats that end with extensions including, but not limited to, .EXE, .DLL, .SCR, .BAT, and/or .VBS.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Protect shared folders by minimizing users who have write access. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using application control [^6]  tools, like AppLocker, [^4]  [^7]  or Software Restriction Policies [^2]  where appropriate. [^3]  |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically quarantine suspicious files.[^1]  |
| [[kb/mitre/attack/mitigations/M1050-Exploit_Protection\|M1050]] | Exploit Protection | Use utilities that detect or mitigate common features used in exploitation, such as the Microsoft Enhanced Mitigation Experience Toolkit (EMET). |






> [!info]- References
> [^1]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)

> [^2]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))

> [^3]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)

> [^4]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)

> [^5]: [Retwin Directory Share Pivot](https://rewtin.blogspot.ch/2017/11/abusing-user-shares-for-efficient.html)

> [^6]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)

> [^7]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


