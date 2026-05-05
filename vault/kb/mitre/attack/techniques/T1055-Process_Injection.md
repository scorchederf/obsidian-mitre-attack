---
aliases: 
    - T1055
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1055-Process_Injection
tactic: 
     - Stealth - Privilege Escalation
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. <br><br>There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. <br><br>More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0040-HTRAN\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-HTRAN\|HTRAN]] can inject into into running processes.[^4]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] has a command to hide itself by injecting into another process.[^6]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^11]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^13]  |
| [[kb/mitre/attack/software/S0581-IronNetInjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.[^12]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.[^5] [^9] [^1] [^2]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can inject shellcode directly into Excel.exe or a specific process.[^7]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] includes a subproject `DonutTest` to inject shellcode into a target process.[^3] 	 |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | The [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.[^8]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Utilize Yama (ex: /proc/sys/kernel/yama/ptrace_scope) to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux, grsecurity, and AppArmor. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of process injection based on common sequences of behavior that occur during the injection process. For example, on Windows 10, Attack Surface Reduction (ASR) rules may prevent Office applications from code injection. [^10]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1055.001-Dynamic-link_Library_Injection\|T1055.001]] | Dynamic-link Library Injection |
| [[kb/mitre/attack/techniques/T1055.002-Portable_Executable_Injection\|T1055.002]] | Portable Executable Injection |
| [[kb/mitre/attack/techniques/T1055.003-Thread_Execution_Hijacking\|T1055.003]] | Thread Execution Hijacking |
| [[kb/mitre/attack/techniques/T1055.004-Asynchronous_Procedure_Call\|T1055.004]] | Asynchronous Procedure Call |
| [[kb/mitre/attack/techniques/T1055.005-Thread_Local_Storage\|T1055.005]] | Thread Local Storage |
| [[kb/mitre/attack/techniques/T1055.008-Ptrace_System_Calls\|T1055.008]] | Ptrace System Calls |
| [[kb/mitre/attack/techniques/T1055.009-Proc_Memory\|T1055.009]] | Proc Memory |
| [[kb/mitre/attack/techniques/T1055.011-Extra_Window_Memory_Injection\|T1055.011]] | Extra Window Memory Injection |
| [[kb/mitre/attack/techniques/T1055.012-Process_Hollowing\|T1055.012]] | Process Hollowing |
| [[kb/mitre/attack/techniques/T1055.013-Process_Doppelg_nging\|T1055.013]] | Process Doppelgänging |
| [[kb/mitre/attack/techniques/T1055.014-VDSO_Hijacking\|T1055.014]] | VDSO Hijacking |
| [[kb/mitre/attack/techniques/T1055.015-ListPlanting\|T1055.015]] | ListPlanting |




> [!info]- References
> [^1]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)

> [^2]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)

> [^3]: [Donut Github](https://github.com/TheWover/donut)

> [^4]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)

> [^5]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)

> [^6]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)

> [^7]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^8]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^9]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)

> [^10]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^11]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^12]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)

> [^13]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


