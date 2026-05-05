---
aliases: 
    - S1186
    
mitre-attack: https://attack.mitre.org/software/S1186
---

## S1186

[Line Dancer](https://attack.mitre.org/software/S1186) is a memory-only Lua-based shellcode loader associated with the [ArcaneDoor](https://attack.mitre.org/campaigns/C0046) campaign. [Line Dancer](https://attack.mitre.org/software/S1186) allows an adversary to upload and execute arbitrary shellcode on victim devices.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Line Dancer](https://attack.mitre.org/software/S1186) shellcode payloads are base64 encoded when transmitted to compromised devices.[^2]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [Line Dancer](https://attack.mitre.org/software/S1186) can disable syslog on compromised devices.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Line Dancer](https://attack.mitre.org/software/S1186) exfiltrates collected data via command and control channels.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Line Dancer](https://attack.mitre.org/software/S1186) uses HTTP POST requests to interact with compromised devices.[^1] [^2]  |
| [[Rootkit\|T1014]] | Rootkit | [Line Dancer](https://attack.mitre.org/software/S1186) can hook both the crash dump process and the Autehntication, Authorization, and Accounting (AAA) functions on compromised machines to evade forensic analysis and authentication mechanisms.[^1]  |
| [[Power Settings\|T1653]] | Power Settings | [Line Dancer](https://attack.mitre.org/software/S1186) can modify the crash dump process on infected machines to skip crash dump generation and proceed directly to device reboot for both persistence and forensic evasion purposes.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Line Dancer](https://attack.mitre.org/software/S1186) can create and exfiltrate packet captures from compromised environments.[^1]  |
| [[Network Device CLI\|T1059.008]] | Network Device CLI | [Line Dancer](https://attack.mitre.org/software/S1186) can execute native commands in networking device command line interfaces.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Line Dancer](https://attack.mitre.org/software/S1186) can gather system configuration information by running the native `show configuration` command.[^1]  |




## References

[^1]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)


[^2]: [CCCS ArcaneDoor 2024](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)


