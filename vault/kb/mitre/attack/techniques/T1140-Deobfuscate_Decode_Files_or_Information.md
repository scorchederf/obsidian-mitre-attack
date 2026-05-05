---
aliases: 
    - T1140
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information
tactic: 
     - Stealth
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may use [[kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information\|Obfuscated Files or Information]] to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.<br><br>One such example is the use of [[kb/mitre/attack/software/S0160-certutil\|certutil]] to decode a remote access tool portable executable file that has been hidden inside a certificate file.[^1]  Another example is using the Windows `copy /b` or `type` command to reassemble binary fragments into a malicious payload.[^9] [^3] <br><br>Sometimes a user's action may be required to open it for deobfuscation or decryption as part of [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.[^2] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0160-certutil\|S0160]] | certutil | [[kb/mitre/attack/software/S0160-certutil\|certutil]] has been used to decode binaries hidden inside certificate files as Base64 information.[^1]  |
| [[kb/mitre/attack/software/S0361-Expand\|S0361]] | Expand | [[kb/mitre/attack/software/S0361-Expand\|Expand]] can be used to decompress a local or remote CAB file into an executable.[^6]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has decoded malware components that are then dropped to the system.[^8]  |
| [[kb/mitre/attack/software/S0581-IronNetInjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] has the ability to decrypt embedded .NET and PE payloads.[^7]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.[^5]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has the ability to deobfuscate its payload prior to execution.[^4]  |








> [!info]- References
> [^1]: [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)

> [^2]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)

> [^3]: [Sentinel One Tainted Love 2023](https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/)

> [^4]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^5]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^6]: [Microsoft Expand Utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)

> [^7]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)

> [^8]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)

> [^9]: [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)


