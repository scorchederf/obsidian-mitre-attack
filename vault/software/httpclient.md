---
aliases: 
    - S0068
    
mitre-attack: https://attack.mitre.org/software/S0068
---

## S0068

[httpclient](https://attack.mitre.org/software/S0068) is malware used by [Putter Panda](https://attack.mitre.org/groups/G0024). It is a simple tool that provides a limited range of functionality, suggesting it is likely used as a second-stage or supplementary/backup tool. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [httpclient](https://attack.mitre.org/software/S0068) encrypts C2 content with XOR using a single byte, 0x12.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [httpclient](https://attack.mitre.org/software/S0068) uses HTTP for command and control.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [httpclient](https://attack.mitre.org/software/S0068) opens cmd.exe on the victim.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Putter Panda\|G0024]] | Putter Panda |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


