---
aliases: 
    - T1047
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation
tactic: 
     - Execution
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.[^3]  WMI is an administration feature that provides a uniform environment to access Windows system components.<br><br>The WMI service enables both local and remote access, though the latter is facilitated by [[kb/mitre/attack/techniques/T1021-Remote_Services\|Remote Services]] such as [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|Distributed Component Object Model]] and [[kb/mitre/attack/techniques/T1021.006-Windows_Remote_Management\|Windows Remote Management]].[^3]  Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.[^3]  [^12] <br><br>An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [[kb/mitre/attack/tactics/TA0007-Discovery\|Discovery]] as well as [[kb/mitre/attack/tactics/TA0002-Execution\|Execution]] of commands and payloads.[^12]  For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [[kb/mitre/attack/techniques/T1490-Inhibit_System_Recovery\|Inhibit System Recovery]]).[^11] <br><br>**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] as the primary WMI interface.[^13]  In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.[^13] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-WmiCommand` CodeExecution module uses WMI to execute and retrieve the output from a PowerShell payload.[^2] [^16]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can use WMI to execute commands.[^6]  |
| [[kb/mitre/attack/software/S0357-Impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]]'s `wmiexec` module can be used to execute commands through WMI.[^14] [^7]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use WMI to deliver a payload to a remote host.[^18]   |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has a number of modules that use WMI to execute tasks.[^15]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can execute remote commands using Windows Management Instrumentation.[^17] 	 |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use WMI for lateral movement.[^10]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can use WMI to move laterally.[^4]  |
| [[kb/mitre/attack/software/S1155-Covenant\|S1155]] | Covenant | [[kb/mitre/attack/software/S1155-Covenant\|Covenant]] can utilize WMI to install new Grunt listeners through XSL files or command one-liners.[^9]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | By default, only administrators are allowed to connect remotely using WMI. Restrict other users who are allowed to connect, or disallow all users to connect remotely to WMI. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Prevent credential overlap across systems of administrator and privileged accounts. [^8]  |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Use application control configured to block execution of `wmic.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `wmic.exe` application and to prevent abuse.[^5]  |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block processes created by WMI commands from running. Note: many legitimate tools and applications utilize WMI for command execution. [^1]  |






> [!info]- References
> [^1]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^2]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)

> [^3]: [WMI 1-3](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page?redirectedfrom=MSDN)

> [^4]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^5]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)

> [^6]: [Github Koadic](https://github.com/offsecginger/koadic)

> [^7]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)

> [^8]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)

> [^9]: [Github Covenant](https://github.com/cobbr/Covenant)

> [^10]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^11]: [WMI 6](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)

> [^12]: [Mandiant WMI](https://www.mandiant.com/resources/reports)

> [^13]: [WMI 7,8](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/wmi-command-line-wmic-utility-deprecation-next-steps/ba-p/4039242)

> [^14]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)

> [^15]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^16]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^17]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^18]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


