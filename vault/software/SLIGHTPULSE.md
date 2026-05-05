---
aliases: 
    - S1110
    
mitre-attack: https://attack.mitre.org/software/S1110
---

## S1110

[SLIGHTPULSE](https://attack.mitre.org/software/S1110) is a web shell that was used by [APT5](https://attack.mitre.org/groups/G1023) as early as 2020 including against Pulse Secure VPNs at US Defense Industrial Base (DIB) entities.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) has piped the output from executed commands to `/tmp/1`.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can base64 encode all incoming and outgoing C2 messages.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) is a web shell that can read, write, and execute files on compromised servers.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RAPIDPULSE](https://attack.mitre.org/software/S1113) can transfer files to and from compromised hosts.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can deobfuscate base64 encoded and RC4 encrypted C2 messages.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can read files specified on the local system.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) contains functionality to execute arbitrary commands passed to it.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) has the ability to process HTTP GET requests as a normal web server and to insert logic that will read or write files or execute commands in response to HTTP POST requests.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can RC4 encrypt all incoming and outgoing C2 messages.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^2]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


