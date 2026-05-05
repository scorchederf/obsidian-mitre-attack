---
aliases: 
    - T1132
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1132-Data_Encoding
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.[^1]  [^5]  Some data encoding systems may also result in data compression, such as gzip.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0699-Mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] provides various transform functions to encode and/or randomize C2 data.[^2] 	 |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can randomly generate and Base64 encode parameters in phishing links to defeat static detection.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [^4]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1132.001-Standard_Encoding\|T1132.001]] | Standard Encoding |
| [[kb/mitre/attack/techniques/T1132.002-Non-Standard_Encoding\|T1132.002]] | Non-Standard Encoding |




> [!info]- References
> [^1]: [Wikipedia Binary-to-text Encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)

> [^2]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^3]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)

> [^4]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

> [^5]: [Wikipedia Character Encoding](https://en.wikipedia.org/wiki/Character_encoding)


