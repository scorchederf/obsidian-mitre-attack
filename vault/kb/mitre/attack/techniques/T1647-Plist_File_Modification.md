---
aliases: 
    - T1647
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/macos
mitre-attack: kb/mitre/attack/techniques/T1647-Plist_File_Modification
tactic: 
     - Defense Impairment
platforms:
     - macOS
permissions required:
     - none
---

## Description

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the `info.plist` file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format.[^4]  <br><br>Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|Hidden Window]]) or running additional commands for persistence (ex: [[kb/mitre/attack/techniques/T1543.001-Launch_Agent\|Launch Agent]]/[[kb/mitre/attack/techniques/T1543.004-Launch_Daemon\|Launch Daemon]] or [[kb/mitre/attack/techniques/T1547.007-Re-opened_Applications\|Re-opened Applications]]).<br><br>For example, adversaries can add a malicious application path to the `~/Library/Preferences/com.apple.dock.plist` file, which controls apps that appear in the Dock. Adversaries can also modify the `LSUIElement` key in an application’s `info.plist` file  to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as `LSEnvironment`, to enable persistence via [[kb/mitre/attack/techniques/T1574.006-Dynamic_Linker_Hijacking\|Dynamic Linker Hijacking]].[^1] [^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Ensure applications are using Apple's developer guidance which enables hardened runtime.[^2]  |






> [!info]- References
> [^1]: [wardle chp2 persistence](https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf)

> [^2]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)

> [^3]: [eset_osx_flashback](https://www.welivesecurity.com/wp-content/uploads/200x/white-papers/osx_flashback.pdf)

> [^4]: [fileinfo plist file description](https://fileinfo.com/extension/plist)


