---
aliases: 
    - S0065
    
mitre-attack: https://attack.mitre.org/software/S0065
---

## S0065

[4H RAT](https://attack.mitre.org/software/S0065) is malware that has been used by [Putter Panda](https://attack.mitre.org/groups/G0024) since at least 2007. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to obtain file and directory listings.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [4H RAT](https://attack.mitre.org/software/S0065) sends an OS version identifier in its beacons.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to create a remote shell.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [4H RAT](https://attack.mitre.org/software/S0065) uses HTTP for command and control.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [4H RAT](https://attack.mitre.org/software/S0065) obfuscates C2 communication using a 1-byte XOR with the key 0xBE.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to obtain a listing of running processes (including loaded modules).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Putter Panda\|G0024]] | Putter Panda |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


