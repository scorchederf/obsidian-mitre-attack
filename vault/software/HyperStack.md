---
aliases: 
    - S0537
    
mitre-attack: https://attack.mitre.org/software/S0537
---

## S0537

[HyperStack](https://attack.mitre.org/software/S0537) is a RPC-based backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2018. [HyperStack](https://attack.mitre.org/software/S0537) has similarities to other backdoors used by [Turla](https://attack.mitre.org/groups/G0010) including [Carbon](https://attack.mitre.org/software/S0335).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Default Accounts\|T1078.001]] | Default Accounts | [HyperStack](https://attack.mitre.org/software/S0537) can use default credentials to connect to IPC$ shares on remote machines.[^1]  |
| [[Native API\|T1106]] | Native API | [HyperStack](https://attack.mitre.org/software/S0537) can use Windows API's `ConnectNamedPipe` and `WNetAddConnection2` to detect incoming connections and connect to remote shares.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [HyperStack](https://attack.mitre.org/software/S0537) can connect to the IPC$ share on remote machines.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [HyperStack](https://attack.mitre.org/software/S0537) can add the name of its communication pipe to `HKLM\SYSTEM\\CurrentControlSet\\Services\\lanmanserver\\parameters\NullSessionPipes`.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [HyperStack](https://attack.mitre.org/software/S0537) has used RSA encryption for C2 communications.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [HyperStack](https://attack.mitre.org/software/S0537) can enumerate all account names on a remote share.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Turla\|G0010]] | Turla |



## References

[^1]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


