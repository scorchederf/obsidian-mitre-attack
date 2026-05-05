---
aliases: 
    - T1559
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1559-Inter-Process_Communication
tactic: 
     - Execution
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. <br><br>Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [[kb/mitre/attack/techniques/T1559.002-Dynamic_Data_Exchange\|Dynamic Data Exchange]] or [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|Component Object Model]]. Linux environments support several different IPC mechanisms, two of which being sockets and pipes.[^4]  Higher level execution mediums, such as those of [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]]s, may also leverage underlying IPC mechanisms. Adversaries may also use [[kb/mitre/attack/techniques/T1021-Remote_Services\|Remote Services]] such as [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|Distributed Component Object Model]] to facilitate remote IPC execution.[^6] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Enable the Hardened Runtime capability when developing applications. Do not include the `com.apple.security.get-task-allow` entitlement with the value set to any variation of true.  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{AppID_GUID}` associated with the process-wide security of individual COM applications.[^2] <br><br>Modify Registry settings (directly or using Dcomcnfg.exe) in `HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Ole` associated with system-wide security defaults for all COM applications that do no set their own process-wide security.[^7]  [^9]  |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs.[^5] [^11]  |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [^12] [^10] [^3]  Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel.[^1]  |
| [[kb/mitre/attack/mitigations/M1048-Application_Isolation_and_Sandboxing\|M1048]] | Application Isolation and Sandboxing | Ensure all COM alerts and Protected View are enabled.[^8]  |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Consider disabling embedded files in Office programs, such as OneNote, that do not work with Protected View.[^11] [^3]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|T1559.001]] | Component Object Model |
| [[kb/mitre/attack/techniques/T1559.002-Dynamic_Data_Exchange\|T1559.002]] | Dynamic Data Exchange |
| [[kb/mitre/attack/techniques/T1559.003-XPC_Services\|T1559.003]] | XPC Services |




> [!info]- References
> [^1]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)

> [^2]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)

> [^3]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)

> [^4]: [Linux IPC](https://www.geeksforgeeks.org/inter-process-communication-ipc/#:~:text=Inter%2Dprocess%20communication%20(IPC),of%20co%2Doperation%20between%20them.)

> [^5]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)

> [^6]: [Fireeye Hunting COM June 2019](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)

> [^7]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)

> [^8]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)

> [^9]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)

> [^10]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)

> [^11]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)

> [^12]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


