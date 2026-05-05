---
aliases: 
    - T1027
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1027-Obfuscated_Files_or_Information
tactic: 
     - Stealth
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. <br><br>Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and [[kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information\|Deobfuscate/Decode Files or Information]] for [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.[^6]  Adversaries may also use compressed or archived scripts, such as JavaScript. <br><br>Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery.[^2]  Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.[^18] <br><br>Adversaries may also abuse [[kb/mitre/attack/techniques/T1027.010-Command_Obfuscation\|Command Obfuscation]] to obscure commands executed from payloads or directly via [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]]. Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms.[^16] [^8] [^13]  


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] uses RC4 and base64 to obfuscate data, including Registry entries and file paths.[^1]  [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can also employ control flow flattening to hinder analysis.[^5]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.[^17]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] encrypted gathered information with a combination of shifting and XOR using a static key.[^3]  |
| [[kb/mitre/attack/software/S0465-CARROTBALL\|S0465]] | CARROTBALL | [[kb/mitre/attack/software/S0465-CARROTBALL\|CARROTBALL]] has used a custom base64 alphabet to decode files.[^12]  |
| [[kb/mitre/attack/software/S0500-MCMD\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-MCMD\|MCMD]] can Base64 encode output strings prior to sending to C2.[^11]  |
| [[kb/mitre/attack/software/S0594-Out1\|S0594]] | Out1 | [[kb/mitre/attack/software/S0594-Out1\|Out1]] has the ability to encode data.[^10]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.[^14]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has used encrypted payload files and maintains an encrypted configuration structure in memory.[^7] [^15]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Ensure that a finite amount of ingress points to a software deployment system exist with restricted access for those required to allow and enable newly deployed software. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10+, enable Attack Surface Reduction (ASR) rules to prevent execution of potentially obfuscated payloads. [^4]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data. |
| [[kb/mitre/attack/mitigations/M1049-Antivirus_Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically detect and quarantine suspicious files. Consider utilizing the Antimalware Scan Interface (AMSI) on Windows 10+ to analyze commands after being processed/interpreted. [^9]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1027.001-Binary_Padding\|T1027.001]] | Binary Padding |
| [[kb/mitre/attack/techniques/T1027.002-Software_Packing\|T1027.002]] | Software Packing |
| [[kb/mitre/attack/techniques/T1027.003-Steganography\|T1027.003]] | Steganography |
| [[kb/mitre/attack/techniques/T1027.004-Compile_After_Delivery\|T1027.004]] | Compile After Delivery |
| [[kb/mitre/attack/techniques/T1027.005-Indicator_Removal_from_Tools\|T1027.005]] | Indicator Removal from Tools |
| [[kb/mitre/attack/techniques/T1027.006-HTML_Smuggling\|T1027.006]] | HTML Smuggling |
| [[kb/mitre/attack/techniques/T1027.007-Dynamic_API_Resolution\|T1027.007]] | Dynamic API Resolution |
| [[kb/mitre/attack/techniques/T1027.008-Stripped_Payloads\|T1027.008]] | Stripped Payloads |
| [[kb/mitre/attack/techniques/T1027.009-Embedded_Payloads\|T1027.009]] | Embedded Payloads |
| [[kb/mitre/attack/techniques/T1027.010-Command_Obfuscation\|T1027.010]] | Command Obfuscation |
| [[kb/mitre/attack/techniques/T1027.011-Fileless_Storage\|T1027.011]] | Fileless Storage |
| [[kb/mitre/attack/techniques/T1027.012-LNK_Icon_Smuggling\|T1027.012]] | LNK Icon Smuggling |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File |
| [[kb/mitre/attack/techniques/T1027.014-Polymorphic_Code\|T1027.014]] | Polymorphic Code |
| [[kb/mitre/attack/techniques/T1027.015-Compression\|T1027.015]] | Compression |
| [[kb/mitre/attack/techniques/T1027.016-Junk_Code_Insertion\|T1027.016]] | Junk Code Insertion |
| [[kb/mitre/attack/techniques/T1027.017-SVG_Smuggling\|T1027.017]] | SVG Smuggling |
| [[kb/mitre/attack/techniques/T1027.018-Invisible_Unicode\|T1027.018]] | Invisible Unicode |




> [!info]- References
> [^1]: [Talos Remcos Aug 2018](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)

> [^2]: [Linux/Cdorked.A We Live Security Analysis](https://www.welivesecurity.com/2013/04/26/linuxcdorked-new-apache-backdoor-in-the-wild-serves-blackhole/)

> [^3]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^4]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

> [^5]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)

> [^6]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)

> [^7]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^8]: [FireEye Revoke-Obfuscation July 2017](https://www.blackhat.com/docs/us-17/thursday/us-17-Bohannon-Revoke-Obfuscation-PowerShell-Obfuscation-Detection-And%20Evasion-Using-Science-wp.pdf)

> [^9]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)

> [^10]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)

> [^11]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)

> [^12]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)

> [^13]: [PaloAlto EncodedCommand March 2017](https://researchcenter.paloaltonetworks.com/2017/03/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/)

> [^14]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)

> [^15]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)

> [^16]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)

> [^17]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)

> [^18]: [Carbon Black Obfuscation Sept 2016](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)


