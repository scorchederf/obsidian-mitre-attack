---
aliases: 
    - T1106
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1106-Native_API
tactic: 
     - Execution
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes.[^12] [^16]  These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.<br><br>Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]], the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.<br><br>Native API functions (such as `NtCreateProcess`) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries.[^8] [^13] [^32]  For example, functions such as the Windows API `CreateProcess()` or GNU `fork()` will allow programs and scripts to start other processes.[^19] [^11]  This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.[^2] [^1] [^17] <br><br>Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.[^3] [^28] [^18] [^23] <br><br>Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks.[^9]  Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via [[kb/mitre/attack/techniques/T1685-Disable_or_Modify_Tools\|Disable or Modify Tools]].


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] contains a variety of enumeration modules that have an option to use API calls to carry out tasks.[^29]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has leveraged CreateProcessW() call to execute the debugger.[^31]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used several Windows API functions to gather information from the infected system.[^6]  |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.[^5]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.[^20]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] code modules use various API functions to load and inject code.[^24] 	 |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has used a variety of Windows API functions.[^21]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can call multiple Windows APIs for execution, to share memory, and defense evasion.[^15] [^30]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.[^26]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Identify and block potentially malicious software executed that may be executed through this technique by using application control [^22]  tools, like Windows Defender Application Control[^27] , AppLocker, [^14]  [^10]  or Software Restriction Policies [^4]  where appropriate. [^25]  |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office VBA macros from calling Win32 APIs. [^7]  |






> [!info]- References
> [^1]: [LIBC](https://man7.org/linux/man-pages//man7/libc.7.html)

> [^2]: [Microsoft Win32](https://docs.microsoft.com/en-us/windows/win32/api/)

> [^3]: [Microsoft NET](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet-framework)

> [^4]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))

> [^5]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)

> [^6]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^7]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^8]: [OutFlank System Calls](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)

> [^9]: [Redops Syscalls](https://redops.at/en/blog/direct-syscalls-vs-indirect-syscalls)

> [^10]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

> [^11]: [GNU Fork](https://www.gnu.org/software/libc/manual/html_node/Creating-a-Process.html)

> [^12]: [NT API Windows](https://undocumented.ntinternals.net/)

> [^13]: [CyberBit System Calls](https://www.cyberbit.com/blog/endpoint-security/malware-mitigation-when-direct-system-calls-are-used/)

> [^14]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)

> [^15]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^16]: [Linux Kernel API](https://www.kernel.org/doc/html/v4.12/core-api/kernel-api.html)

> [^17]: [GLIBC](https://www.gnu.org/software/libc/)

> [^18]: [MACOS Cocoa](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/CocoaApplicationLayer/CocoaApplicationLayer.html#//apple_ref/doc/uid/TP40001067-CH274-SW1)

> [^19]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)

> [^20]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^21]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^22]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)

> [^23]: [macOS Foundation](https://developer.apple.com/documentation/foundation)

> [^24]: [Donut Github](https://github.com/TheWover/donut)

> [^25]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)

> [^26]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^27]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)

> [^28]: [Apple Core Services](https://developer.apple.com/documentation/coreservices)

> [^29]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^30]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)

> [^31]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)

> [^32]: [MDSec System Calls](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)


