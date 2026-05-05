---
aliases: 
    - S1163
    
mitre-attack: https://attack.mitre.org/software/S1163
---

## S1163

[SnappyTCP](https://attack.mitre.org/software/S1163) is a web shell used by [Sea Turtle](https://attack.mitre.org/groups/G1041) between 2021 and 2023 against multiple victims. [SnappyTCP](https://attack.mitre.org/software/S1163) appears to be based on a public GitHub project that has since been removed from the code-sharing site. [SnappyTCP](https://attack.mitre.org/software/S1163) includes a simple reverse TCP shell for Linux and Unix environments with basic command and control capabilities.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Unix Shell\|T1059.004]] | Unix Shell | [SnappyTCP](https://attack.mitre.org/software/S1163) creates the reverse shell using a pthread spawning a bash shell.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SnappyTCP](https://attack.mitre.org/software/S1163) connects to the command and control server via a TCP socket using HTTP.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [SnappyTCP](https://attack.mitre.org/software/S1163) can use OpenSSL and TLS certificates to encrypt traffic.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [SnappyTCP](https://attack.mitre.org/software/S1163) is a reverse TCP shell with command and control capabilities used for persistence purposes.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [SnappyTCP](https://attack.mitre.org/software/S1163) spawns a reverse TCP shell following an HTTP-based negotiation.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sea Turtle\|G1041]] | Sea Turtle |



## References

[^1]: [PWC Sea Turtle 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/tortoise-and-malwahare.html)


