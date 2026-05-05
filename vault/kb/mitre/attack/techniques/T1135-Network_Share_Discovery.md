---
aliases: 
    - T1135
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1135-Network_Share_Discovery
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. <br><br>File sharing over a Windows network occurs over the SMB protocol. [^7]  [^2]  [[kb/mitre/attack/software/S0039-Net\|Net]] can be used to query a remote system for available shared drives using the `net view \\\\remotesystem` command. It can also be used to query shared drives on the local system using `net share`. For macOS, the `sharing -l` command lists all shared points used for smb services.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-Net\|S0039]] | Net | The `net view \\remotesystem` and `net share` commands in [[kb/mitre/attack/software/S0039-Net\|Net]] can be used to find shared drives and directories on remote and local systems respectively.[^6]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can list local and remote shared drives and folders over SMB.[^8]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can scan local network for open SMB.[^9]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can find shared drives on the local system.[^4]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can enumerate the shared folders and associated permissions for a targeted network.[^5]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate shares on a compromised host.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Enable Windows Group Policy “Do Not Allow Anonymous Enumeration of SAM Accounts and Shares” security setting to limit users who can enumerate network shares.[^1]  |






> [!info]- References
> [^1]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)

> [^2]: [TechNet Shared Folder](https://technet.microsoft.com/library/cc770880.aspx)

> [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^4]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^5]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^6]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)

> [^7]: [Wikipedia Shared Resource](https://en.wikipedia.org/wiki/Shared_resource)

> [^8]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^9]: [Github Koadic](https://github.com/offsecginger/koadic)


