---
aliases: 
    - S0220
    
mitre-attack: https://attack.mitre.org/software/S0220
---

## S0220

[Chaos](https://attack.mitre.org/software/S0220) is Linux malware that compromises systems by brute force attacks against SSH services. Once installed, it provides a reverse shell to its controllers, triggered by unsolicited packets. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Chaos](https://attack.mitre.org/software/S0220) provides a reverse shell connection on 8338/TCP, encrypted via AES.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Chaos](https://attack.mitre.org/software/S0220) provides a reverse shell connection on 8338/TCP, encrypted via AES.[^1]  |
| [[Brute Force\|T1110]] | Brute Force | [Chaos](https://attack.mitre.org/software/S0220) conducts brute force attacks against SSH services to gain initial access.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Chaos](https://attack.mitre.org/software/S0220) provides a reverse shell is triggered upon receipt of a packet with a special string, sent to any port.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | After initial compromise, [Chaos](https://attack.mitre.org/software/S0220) will download a second stage to establish a more permanent presence on the affected system.[^1]  |




## References

[^1]: [Chaos Stolen Backdoor](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)


[^2]: Chaos


