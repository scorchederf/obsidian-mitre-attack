---
aliases: 
    - S1096
    
mitre-attack: https://attack.mitre.org/software/S1096
---

## S1096

[Cheerscrypt](https://attack.mitre.org/software/S1096) is a ransomware that was developed by [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) and has been used in attacks against ESXi and Windows environments since at least 2022. [Cheerscrypt](https://attack.mitre.org/software/S1096) was derived from the leaked [Babuk](https://attack.mitre.org/software/S0638) source code and has infrastructure overlaps with deployments of Night Sky ransomware, which was also derived from [Babuk](https://attack.mitre.org/software/S0638).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Stop\|T1489]] | Service Stop | [Cheerscrypt](https://attack.mitre.org/software/S1096) has the ability to terminate VM processes on compromised hosts through execution of `esxcli vm process kill`.[^1] <br> |
| [[Hypervisor CLI\|T1059.012]] | Hypervisor CLI | Cheerscrypt has leveraged `esxcli` in order to terminate running virtual machines.[^1] <br> |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Cheerscrypt](https://attack.mitre.org/software/S1096) can encrypt data on victim machines using a Sosemanuk stream cipher with an Elliptic-curve Diffie–Hellman (ECDH) generated key.[^1] [^2] <br> |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cheerscrypt](https://attack.mitre.org/software/S1096) can search for log and VMware-related files with .log, .vmdk, .vmem, .vswp, and .vmsn extensions.[^1]  |
| [[Virtual Machine Discovery\|T1673]] | Virtual Machine Discovery | Cheerscrypt has leveraged `esxcli vm process list` in order to gather a list of running virtual machines to terminate them.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |



## References

[^1]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)


[^2]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


