---
aliases: 
    - S1143
    
mitre-attack: https://attack.mitre.org/software/S1143
---

## S1143

[LunarLoader](https://attack.mitre.org/software/S1143) is the loader component for the [LunarWeb](https://attack.mitre.org/software/S1141) and [LunarMail](https://attack.mitre.org/software/S1142) backdoors that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including against a European ministry of foreign affairs (MFA). [LunarLoader](https://attack.mitre.org/software/S1143) has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LunarLoader](https://attack.mitre.org/software/S1143) can verify the targeted host's DNS name which is then used in the creation of a decyrption key.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [LunarLoader](https://attack.mitre.org/software/S1143) can use the DNS domain name of a compromised host to create a decryption key to ensure a malicious payload can only execute against the intended targets.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LunarLoader](https://attack.mitre.org/software/S1143) can deobfuscate files containing the next stages in the infection chain.[^1]  |
| [[Add-ins\|T1137.006]] | Add-ins | [LunarLoader](https://attack.mitre.org/software/S1143) has the ability to use Microsoft Outlook add-ins to establish persistence. [^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [LunarLoader](https://attack.mitre.org/software/S1143) can use reflective loading to decrypt and run malicious executables in a new thread.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


