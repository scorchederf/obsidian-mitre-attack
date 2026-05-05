---
aliases: 
    - S0362
    
mitre-attack: https://attack.mitre.org/software/S0362
---

## S0362

[Linux Rabbit](https://attack.mitre.org/software/S0362) is malware that targeted Linux servers and IoT devices in a campaign lasting from August to October 2018. It shares code with another strain of malware known as Rabbot. The goal of the campaign was to install cryptocurrency miners onto the targeted servers and devices.[^1] <br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Linux Rabbit](https://attack.mitre.org/software/S0362) brute forces SSH passwords in order to attempt to gain access and install its malware onto the server. [^1]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Linux Rabbit](https://attack.mitre.org/software/S0362) attempts to gain access to the server via SSH.[^1]  |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | [Linux Rabbit](https://attack.mitre.org/software/S0362) maintains persistence on an infected machine through rc.local and .bashrc files. [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Linux Rabbit](https://attack.mitre.org/software/S0362) opens a socket on port 22 and if it receives a response it attempts to obtain the machine's hostname and Top-Level Domain. [^1]  |
| [[Data Encoding\|T1132]] | Data Encoding | [Linux Rabbit](https://attack.mitre.org/software/S0362) sends the payload from the C2 server as an encoded URL parameter. [^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Linux Rabbit](https://attack.mitre.org/software/S0362) acquires valid SSH accounts through brute force. [^1]  |




## References

[^1]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)


[^2]: [anomali-linux-rabbit](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)


