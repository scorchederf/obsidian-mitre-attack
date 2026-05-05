---
aliases: 
    - T1553
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1553-Subvert_Trust_Controls
tactic: 
     - Defense Impairment
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may undermine security controls that will either warn users of untrusted activity or prevent execution of untrusted programs. Operating systems and security products may contain mechanisms to identify programs or websites as possessing some level of trust. Examples of such features would include a program being allowed to run because it is signed by a valid code signing certificate, a program prompting the user with a warning because it has an attribute set from being downloaded from the Internet, or getting an indication that you are about to connect to an untrusted site.<br><br>Adversaries may attempt to subvert these trust mechanisms. The method adversaries use will depend on the specific mechanism they seek to subvert. Adversaries may conduct [[kb/mitre/attack/techniques/T1222-File_and_Directory_Permissions_Modification\|File and Directory Permissions Modification]] or [[kb/mitre/attack/techniques/T1112-Modify_Registry\|Modify Registry]] in support of subverting these controls.[^3]  Adversaries may also create or steal code signing certificates to acquire trust on target systems.[^5] [^2]  




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented. |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[kb/mitre/attack/mitigations/M1028-Operating_System_Configuration\|M1028]] | Operating System Configuration | Windows Group Policy can be used to manage root certificates and the `Flags` value of `HKLM\\SOFTWARE\\Policies\\Microsoft\\SystemCertificates\\Root\\ProtectedRoots` can be set to 1 to prevent non-administrator users from making further root installations into their own HKCU certificate store. [^1]  |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | System settings can prevent applications from running that haven't been downloaded through the Apple Store (or other legitimate repositories) which can help mitigate some of these issues. Also enable application control solutions such as AppLocker and/or Device Guard to block the loading of malicious content. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | HTTP Public Key Pinning (HPKP) is one method to mitigate potential [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] situations where and adversary uses a mis-issued or fraudulent certificate to intercept encrypted communications by enforcing use of an expected certificate. [^4]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1553.001-Gatekeeper_Bypass\|T1553.001]] | Gatekeeper Bypass |
| [[kb/mitre/attack/techniques/T1553.002-Code_Signing\|T1553.002]] | Code Signing |
| [[kb/mitre/attack/techniques/T1553.003-SIP_and_Trust_Provider_Hijacking\|T1553.003]] | SIP and Trust Provider Hijacking |
| [[kb/mitre/attack/techniques/T1553.004-Install_Root_Certificate\|T1553.004]] | Install Root Certificate |
| [[kb/mitre/attack/techniques/T1553.005-Mark-of-the-Web_Bypass\|T1553.005]] | Mark-of-the-Web Bypass |
| [[kb/mitre/attack/techniques/T1553.006-Code_Signing_Policy_Modification\|T1553.006]] | Code Signing Policy Modification |




> [!info]- References
> [^1]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)

> [^2]: [Symantec Digital Certificates](http://www.symantec.com/connect/blogs/how-attackers-steal-private-keys-digital-certificates)

> [^3]: [SpectorOps Subverting Trust Sept 2017](https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf)

> [^4]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)

> [^5]: [Securelist Digital Certificates](https://securelist.com/why-you-shouldnt-completely-trust-files-signed-with-digital-certificates/68593/)


