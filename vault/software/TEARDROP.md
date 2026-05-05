---
aliases: 
    - S0560
    
mitre-attack: https://attack.mitre.org/software/S0560
---

## S0560

[TEARDROP](https://attack.mitre.org/software/S0560) is a memory-only dropper that was discovered on some victim machines during investigations related to the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024). It was likely used by [APT29](https://attack.mitre.org/groups/G0016) since at least May 2020.[^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [TEARDROP](https://attack.mitre.org/software/S0560) checked that `HKU\SOFTWARE\Microsoft\CTF` existed before decoding its embedded payload.[^3] [^1]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [TEARDROP](https://attack.mitre.org/software/S0560) created and read from a file with a fake JPG header, and its payload was encrypted with a simple rotating XOR cipher.[^3] [^4] [^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [TEARDROP](https://attack.mitre.org/software/S0560) modified the Registry to create a Windows service for itself on a compromised host.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [TEARDROP](https://attack.mitre.org/software/S0560) ran as a Windows service from the `c:\windows\syswow64` folder.[^4] [^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [TEARDROP](https://attack.mitre.org/software/S0560) files had names that resembled legitimate Window file and directory names.[^3] [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [TEARDROP](https://attack.mitre.org/software/S0560) was decoded using a custom rolling XOR algorithm to execute a customized [Cobalt Strike](https://attack.mitre.org/software/S0154) payload.[^3] [^4] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^2]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^3]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^4]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)


[^5]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^6]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


