---
aliases: 
    - S0565
    
mitre-attack: https://attack.mitre.org/software/S0565
---

## S0565

[Raindrop](https://attack.mitre.org/software/S0565) is a loader used by [APT29](https://attack.mitre.org/groups/G0016) that was discovered on some victim machines during investigations related to the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024). It was discovered in January 2021 and was likely used since at least May 2020.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | After initial installation, [Raindrop](https://attack.mitre.org/software/S0565) runs a computation to delay execution.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Raindrop](https://attack.mitre.org/software/S0565) encrypted its payload using a simple XOR algorithm with a single-byte key.[^2] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Raindrop](https://attack.mitre.org/software/S0565) used a custom packer for its [Cobalt Strike](https://attack.mitre.org/software/S0154) payload, which was compressed using the LZMA algorithm.[^2] [^1]  |
| [[Masquerading\|T1036]] | Masquerading | [Raindrop](https://attack.mitre.org/software/S0565) was built to include a modified version of 7-Zip source code (including associated export names) and Far Manager source code.[^2] [^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Raindrop](https://attack.mitre.org/software/S0565) was installed under names that resembled legitimate Windows file and directory names.[^2] [^1]  |
| [[Steganography\|T1027.003]] | Steganography | [Raindrop](https://attack.mitre.org/software/S0565) used steganography to locate the start of its encoded payload within legitimate 7-Zip code.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Raindrop](https://attack.mitre.org/software/S0565) decrypted its [Cobalt Strike](https://attack.mitre.org/software/S0154) payload using an AES-256 encryption algorithm in CBC mode with a unique key per sample.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^2]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)


[^3]: Raindrop


[^4]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^5]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


