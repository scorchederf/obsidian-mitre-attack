---
aliases: 
    - S1041
    
mitre-attack: https://attack.mitre.org/software/S1041
---

## S1041

[Chinoxy](https://attack.mitre.org/software/S1041) is a backdoor that has been used since at least November 2018, during the [FunnyDream](https://attack.mitre.org/campaigns/C0007) campaign, to gain persistence and drop additional payloads. According to security researchers, [Chinoxy](https://attack.mitre.org/software/S1041) has been used by Chinese-speaking threat actors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DLL\|T1574.001]] | DLL | [Chinoxy](https://attack.mitre.org/software/S1041) can use a digitally signed binary ("Logitech Bluetooth Wizard Host Process") to load its dll into memory.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | The [Chinoxy](https://attack.mitre.org/software/S1041) dropping function can initiate decryption of its config file.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Chinoxy](https://attack.mitre.org/software/S1041) has established persistence via the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` registry key and by loading a dropper to `(%COMMON_ STARTUP%\\eoffice.exe)`.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Chinoxy](https://attack.mitre.org/software/S1041) has encrypted its configuration file.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Chinoxy](https://attack.mitre.org/software/S1041) has used the name `eoffice.exe` in attempt to appear as a legitimate file.[^1]  |




## References

[^1]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


