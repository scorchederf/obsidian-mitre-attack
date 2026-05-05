---
aliases: 
    - S9011
    
mitre-attack: https://attack.mitre.org/software/S9011
---

## S9011

[BRUSHFIRE](https://attack.mitre.org/software/S9011) is a passive backdoor written in C that executes in-memory within an existing process. First reported in March 2025, [BRUSHFIRE](https://attack.mitre.org/software/S9011) has been observed in activity attributed to People's Republic of China (PRC) state-affiliated threat actors, including UNC5221 and SYLVANITE.[^3] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BRUSHFIRE](https://attack.mitre.org/software/S9011) has decrypted XOR strings prior to execution.[^2]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [BRUSHFIRE](https://attack.mitre.org/software/S9011) has the ability to exfiltrate data on-demand through executing commands obtained via monitoring for specially crafted packets and sending output back in an embedded SSL response.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [BRUSHFIRE](https://attack.mitre.org/software/S9011) has monitored inbound VPN traffic to compromised appliances until specific inbound packets contain a specific magic string/pattern instead of external beaconing.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [BRUSHFIRE](https://attack.mitre.org/software/S9011) has executed its commands within memory and is not saved on disk.[^2] [^1]  |




## References

[^1]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^2]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^3]: [Dragos SYLVANITE MuddyWater Electrum March 2026](https://hub.dragos.com/hubfs/2026_YIR_ExecutiveBriefing%20O_G.pdf?hsLang=en)


