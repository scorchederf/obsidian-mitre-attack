---
aliases: 
    - T1059
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter
tactic: 
     - Execution
platforms:
     - Containers - ESXi - IaaS - Identity Provider - Linux - macOS - Network Devices - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [[kb/mitre/attack/techniques/T1059.004-Unix_Shell\|Unix Shell]] while Windows installations include the [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|Windows Command Shell]] and [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]].<br><br>There are also cross-platform interpreters such as [[kb/mitre/attack/techniques/T1059.006-Python\|Python]], as well as those commonly associated with client applications such as [[kb/mitre/attack/techniques/T1059.007-JavaScript\|JavaScript]] and [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|Visual Basic]].<br><br>Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in [[kb/mitre/attack/tactics/TA0001-Initial_Access\|Initial Access]] payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various [[kb/mitre/attack/techniques/T1021-Remote_Services\|Remote Services]] in order to achieve remote Execution.[^5] [^2] [^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] uses a command-line interface to interact with systems.[^7]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.[^10]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate shellcode outputs that execute via Ruby.[^4] 	 |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | When PowerShell is necessary, consider restricting PowerShell execution policy to administrators. Be aware that there are methods of bypassing the PowerShell execution policy, depending on environment configuration.[^6] <br><br>PowerShell JEA (Just Enough Administration) may also be used to sandbox administration and limit what commands admins/users can execute through remote PowerShell sessions.[^3]  |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Prevent user installation of unrequired command and scripting interpreters. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^8]  |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|Visual Basic]] and [[kb/mitre/attack/techniques/T1059.007-JavaScript\|JavaScript]] scripts from executing potentially malicious downloaded content [^9] . |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable or remove any unnecessary or unused shells or interpreters. |
| [[kb/mitre/attack/mitigations/M1045-Code_Signing\|M1045]] | Code Signing | Where possible, only permit execution of signed scripts. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Inventory systems for unauthorized command and scripting interpreter installations. |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically quarantine suspicious files.  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell |
| [[kb/mitre/attack/techniques/T1059.002-AppleScript\|T1059.002]] | AppleScript |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell |
| [[kb/mitre/attack/techniques/T1059.004-Unix_Shell\|T1059.004]] | Unix Shell |
| [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|T1059.005]] | Visual Basic |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python |
| [[kb/mitre/attack/techniques/T1059.007-JavaScript\|T1059.007]] | JavaScript |
| [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|T1059.008]] | Network Device CLI |
| [[kb/mitre/attack/techniques/T1059.009-Cloud_API\|T1059.009]] | Cloud API |
| [[kb/mitre/attack/techniques/T1059.010-AutoHotKey_AutoIT\|T1059.010]] | AutoHotKey & AutoIT |
| [[kb/mitre/attack/techniques/T1059.011-Lua\|T1059.011]] | Lua |
| [[kb/mitre/attack/techniques/T1059.012-Hypervisor_CLI\|T1059.012]] | Hypervisor CLI |
| [[kb/mitre/attack/techniques/T1059.013-Container_CLI_API\|T1059.013]] | Container CLI／API |




> [!info]- References
> [^1]: [Remote Shell Execution in Python](https://www.thepythoncode.com/article/executing-bash-commands-remotely-in-python)

> [^2]: [Cisco IOS Software Integrity Assurance - Command History](https://tools.cisco.com/security/center/resources/integrity_assurance.html#23)

> [^3]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)

> [^4]: [Donut Github](https://github.com/TheWover/donut)

> [^5]: [Powershell Remote Commands](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.1)

> [^6]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)

> [^7]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^8]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)

> [^9]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^10]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


