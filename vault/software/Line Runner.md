---
aliases: 
    - S1188
    
mitre-attack: https://attack.mitre.org/software/S1188
---

## S1188

[Line Runner](https://attack.mitre.org/software/S1188) is a persistent backdoor and web shell allowing threat actors to upload and execute arbitrary Lua scripts. [Line Runner](https://attack.mitre.org/software/S1188) is associated with the [ArcaneDoor](https://attack.mitre.org/campaigns/C0046) campaign.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Line Runner](https://attack.mitre.org/software/S1188) utilizes HTTP to retrieve and exfiltrate information staged using [Line Dancer](https://attack.mitre.org/software/S1186).[^1]  |
| [[Compression\|T1027.015]] | Compression | [Line Runner](https://attack.mitre.org/software/S1188) uses a ZIP payload that is automatically extracted with its contents, a LUA script, executed for initial execution via CVE-2024-20359.[^1]  |
| [[Power Settings\|T1653]] | Power Settings | [Line Runner](https://attack.mitre.org/software/S1188) used CVE-2024-20353 to trigger victim devices to reboot, in the process unzipping and installing the [Line Dancer](https://attack.mitre.org/software/S1186) payload.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Line Runner](https://attack.mitre.org/software/S1188) utilizes an HTTP-based Lua backdoor on victim machines.[^1] [^2]  |
| [[Lua\|T1059.011]] | Lua | [Line Runner](https://attack.mitre.org/software/S1188) utilizes Lua scripts for command execution.[^1] [^2]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Line Runner](https://attack.mitre.org/software/S1188) is a persistent Lua-based web shell.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Line Runner](https://attack.mitre.org/software/S1188) removes its initial ZIP delivery archive after processing the enclosed LUA script.[^1]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [Line Runner](https://attack.mitre.org/software/S1188) intercepts HTTP requests to the victim Cisco ASA, looking for a request with a 32-character, victim dependent parameter. If that parameter matches a value in the malware, a contained payload is then written to a Lua script and executed.[^1]  |




## References

[^1]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)


[^2]: [CCCS ArcaneDoor 2024](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)


