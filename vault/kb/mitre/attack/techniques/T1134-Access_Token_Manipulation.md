---
aliases: 
    - T1134
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1134-Access_Token_Manipulation
tactic: 
     - Stealth - Privilege Escalation
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.<br><br>An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. [[kb/mitre/attack/techniques/T1134.001-Token_Impersonation_Theft\|Token Impersonation/Theft]]) or used to spawn a new process (i.e. [[kb/mitre/attack/techniques/T1134.002-Create_Process_with_Token\|Create Process with Token]]). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.[^5] <br><br>Any standard user can use the `runas` command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-TokenManipulation` Exfiltration module can be used to manipulate tokens.[^10] [^2]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can use [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Invoke-TokenManipulation` to manipulate access tokens.[^7]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can use Invoke-TokenManipulation for manipulating tokens.[^9]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has the ability to manipulate user tokens on targeted Windows systems.[^1] [^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | An adversary must already have administrator level access on the local system to make full use of this technique; be sure to restrict users and accounts to the least privileges they require.   |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [^6]  Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token.[^4] <br><br>Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command `runas`.[^8]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1134.001-Token_Impersonation_Theft\|T1134.001]] | Token Impersonation／Theft |
| [[kb/mitre/attack/techniques/T1134.002-Create_Process_with_Token\|T1134.002]] | Create Process with Token |
| [[kb/mitre/attack/techniques/T1134.003-Make_and_Impersonate_Token\|T1134.003]] | Make and Impersonate Token |
| [[kb/mitre/attack/techniques/T1134.004-Parent_PID_Spoofing\|T1134.004]] | Parent PID Spoofing |
| [[kb/mitre/attack/techniques/T1134.005-SID-History_Injection\|T1134.005]] | SID-History Injection |




> [!info]- References
> [^1]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)

> [^2]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^3]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)

> [^4]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)

> [^5]: [Pentestlab Token Manipulation](https://pentestlab.blog/2017/04/03/token-manipulation/)

> [^6]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)

> [^7]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^8]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)

> [^9]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^10]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


