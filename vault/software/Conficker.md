---
aliases: 
    - S0608
    
mitre-attack: https://attack.mitre.org/software/S0608
---

## S0608

[Conficker](https://attack.mitre.org/software/S0608) is a computer worm first detected in October 2008 that targeted Microsoft Windows using the MS08-067 Windows vulnerability to spread.[^3]  In 2016, a variant of [Conficker](https://attack.mitre.org/software/S0608) made its way on computers and removable disk drives belonging to a nuclear power plant.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [Conficker](https://attack.mitre.org/software/S0608) adds keys to the Registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services` and various other Registry locations.[^3] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Conficker](https://attack.mitre.org/software/S0608) copies itself into the `%systemroot%\system32` directory and registers as a service.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Conficker](https://attack.mitre.org/software/S0608) uses the current UTC victim system date for domain generation and connects to time servers to determine the current date.[^3] [^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Conficker](https://attack.mitre.org/software/S0608) variants spread through NetBIOS share propagation.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Conficker](https://attack.mitre.org/software/S0608) adds Registry Run keys to establish persistence.[^1]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Conficker](https://attack.mitre.org/software/S0608) has used a DGA that seeds with the current UTC victim system date to generate domains.[^3] [^1]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Conficker](https://attack.mitre.org/software/S0608) exploited the MS08-067 Windows vulnerability for remote code execution through a crafted RPC request.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Conficker](https://attack.mitre.org/software/S0608) has obfuscated its code to prevent its removal from host machines.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Conficker](https://attack.mitre.org/software/S0608) scans for other machines to infect.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Conficker](https://attack.mitre.org/software/S0608) terminates various services related to system security and Windows.[^3]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Conficker](https://attack.mitre.org/software/S0608) resets system restore points and deletes backup files.[^3]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Conficker](https://attack.mitre.org/software/S0608) variants used the Windows AUTORUN feature to spread through USB propagation.[^3] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Conficker](https://attack.mitre.org/software/S0608) downloads an HTTP server to the infected machine.[^3]  |




## References

[^1]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)


[^2]: [Conficker Nuclear Power Plant](https://news.softpedia.com/news/on-chernobyl-s-30th-anniversary-malware-shuts-down-german-nuclear-power-plant-503429.shtml)


[^3]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)


[^4]: Downadup


[^5]: Kido


