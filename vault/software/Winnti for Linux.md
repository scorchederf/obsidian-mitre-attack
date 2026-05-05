---
aliases: 
    - S0430
    
mitre-attack: https://attack.mitre.org/software/S0430
---

## S0430

[Winnti for Linux](https://attack.mitre.org/software/S0430) is a trojan, seen since at least 2015, designed specifically for targeting Linux systems. Reporting indicates the winnti malware family is shared across a number of actors including [Winnti Group](https://attack.mitre.org/groups/G0044). The Windows variant is tracked separately under [Winnti for Windows](https://attack.mitre.org/software/S0141).[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used HTTP in outbound communications.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used ICMP, custom TCP, and UDP in outbound communications.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Winnti for Linux](https://attack.mitre.org/software/S0430) has decoded XOR encoded strings holding its configuration upon execution.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used a custom TCP protocol with four-byte XOR for command and control (C2).[^3]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used a passive listener, capable of identifying a specific magic value before executing tasking, as a secondary command and control (C2) mechanism.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Winnti for Linux](https://attack.mitre.org/software/S0430) can encode its configuration file with single-byte XOR encoding.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Winnti for Linux](https://attack.mitre.org/software/S0430) has the ability to deploy modules directly from command and control (C2) servers, possibly for remote command execution, file exfiltration, and socks5 proxying on the infected host. [^3]  |
| [[Rootkit\|T1014]] | Rootkit | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used a modified copy of the open-source userland rootkit Azazel, named libxselinux.so, to hide the malware's operations and network activity.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[APT41\|G0096]] | APT41 |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |



## References

[^1]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^2]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^3]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)


[^4]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


