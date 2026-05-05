---
aliases: 
    - T1554
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1554-Compromise_Host_Software_Binary
tactic: 
     - Persistence
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.<br><br>Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., [[kb/mitre/attack/techniques/T1556-Modify_Authentication_Process\|Modify Authentication Process]]).[^3] <br><br>An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching)[^1]  prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.[^2] <br><br>After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).[^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1045-Code_Signing\|M1045]] | Code Signing | Ensure all application component binaries are signed by the correct application developers. |






> [!info]- References
> [^1]: [Unit42 Banking Trojans Hooking 2022](https://unit42.paloaltonetworks.com/banking-trojan-techniques/#post-125550-_rm3d6xxbk52n)

> [^2]: [ESET FontOnLake Analysis 2021](https://web-assets.esetstatic.com/wls/2021/10/eset_fontonlake.pdf)

> [^3]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


