---
aliases: 
    - T1690
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1690-Prevent_Command_History_Logging
tactic: 
     - Defense Impairment
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they have done.<br><br>On Linux and macOS, command history is tracked in a file pointed to by the environment variable `HISTFILE`. When a user logs off a system, this information is flushed to a file in the user's home directory called `~/.bash_history`. The `HISTCONTROL` environment variable keeps track of what should be saved by the history command and eventually into the `~/.bash_history` file when a user logs out. `HISTCONTROL` does not exist by default on macOS, but can be set by the user and will be respected. The `HISTFILE` environment variable is also used in some ESXi systems.[^1] <br><br>Adversaries may clear the history environment variable (`unset HISTFILE`) or set the command history size to zero (`export HISTFILESIZE=0`) to prevent logging of commands. Additionally, `HISTCONTROL` can be configured to ignore commands that start with a space by simply setting it to "ignorespace". `HISTCONTROL` can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that " ls" will not be saved, but "ls" would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands.<br><br>On Windows systems, the `PSReadLine` module tracks commands used in all PowerShell sessions and writes them to a file (`$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` by default). Adversaries may change where these logs are saved using `Set-PSReadLineOption -HistorySavePath {File Path}`. This will cause `ConsoleHost_history.txt` to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command `Set-PSReadlineOption -HistorySaveStyle SaveNothing`.[^4] [^2] <br><br>Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] on network devices to disable historical command logging (e.g. `no logging`).


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Make sure that the `HISTCONTROL` environment variable is set to “ignoredups” instead of “ignoreboth” or “ignorespace”. |
| [[kb/mitre/attack/mitigations/M1039-Environment_Variable_Permissions\|M1039]] | Environment Variable Permissions | Prevent users from changing the `HISTCONTROL`, `HISTFILE`, and `HISTFILESIZE` environment variables. [^5]  |






> [!info]- References
> [^1]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)

> [^2]: [Sophos PowerShell Command History Forensics](https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics)

> [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^4]: [Microsoft about_History prevent command history](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.6&viewFallbackFrom=powershell-7)

> [^5]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


