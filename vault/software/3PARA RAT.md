---
aliases: 
    - S0066
    
mitre-attack: https://attack.mitre.org/software/S0066
---

## S0066

[3PARA RAT](https://attack.mitre.org/software/S0066) is a remote access tool (RAT) programmed in C++ that has been used by [Putter Panda](https://attack.mitre.org/groups/G0024). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [3PARA RAT](https://attack.mitre.org/software/S0066) command and control commands are encrypted within the HTTP C2 channel using the DES algorithm in CBC mode with a key derived from the MD5 hash of the string HYF54&%9&jkMCXuiS. [3PARA RAT](https://attack.mitre.org/software/S0066) will use an 8-byte XOR key derived from the string HYF54&%9&jkMCXuiS if the DES decoding fails[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [3PARA RAT](https://attack.mitre.org/software/S0066) uses HTTP for command and control.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [3PARA RAT](https://attack.mitre.org/software/S0066) has a command to retrieve metadata for files on disk as well as a command to list the current working directory.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [3PARA RAT](https://attack.mitre.org/software/S0066) has a command to set certain attributes such as creation/modification timestamps on files.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Putter Panda\|G0024]] | Putter Panda |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


