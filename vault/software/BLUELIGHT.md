---
aliases: 
    - S0657
    
mitre-attack: https://attack.mitre.org/software/S0657
---

## S0657

[BLUELIGHT](https://attack.mitre.org/software/S0657) is a remote access Trojan used by [APT37](https://attack.mitre.org/groups/G0067) that was first observed in early 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect IP information from the victim’s machine.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [BLUELIGHT](https://attack.mitre.org/software/S0657) has encoded data into a binary blob using XOR.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect the username on a compromised host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) has collected the computer name and OS version from victim machines.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BLUELIGHT](https://attack.mitre.org/software/S0657) can download additional files onto the host.[^1]   |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BLUELIGHT](https://attack.mitre.org/software/S0657) has a XOR-encoded payload.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BLUELIGHT](https://attack.mitre.org/software/S0657) has exfiltrated data over its C2 channel.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect a list of anti-virus products installed on a machine.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BLUELIGHT](https://attack.mitre.org/software/S0657) can uninstall itself.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [BLUELIGHT](https://attack.mitre.org/software/S0657) can use different cloud providers for its C2.[^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [BLUELIGHT](https://attack.mitre.org/software/S0657) can harvest cookies from Internet Explorer, Edge, Chrome, and Naver Whale browsers.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect passwords stored in web browers, including Internet Explorer, Edge, Chrome, and Naver Whale.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect process filenames and SID authority level.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [BLUELIGHT](https://attack.mitre.org/software/S0657) can zip files before exfiltration.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [BLUELIGHT](https://attack.mitre.org/software/S0657) can check to see if the infected machine has VM tools running.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can enumerate files and collect associated metadata.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BLUELIGHT](https://attack.mitre.org/software/S0657) can use HTTP/S for C2 using the Microsoft Graph API.[^1]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect the local time on a compromised host.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [BLUELIGHT](https://attack.mitre.org/software/S0657) has captured a screenshot of the display every 30 seconds for the first 5 minutes after initiating a C2 loop, and then once every five minutes thereafter.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^2]: BLUELIGHT


