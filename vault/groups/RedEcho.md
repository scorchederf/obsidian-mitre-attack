---
aliases: 
    - RedEcho
mitre-attack: https://attack.mitre.org/groups/G1042
---

## G1042

[RedEcho](https://attack.mitre.org/groups/G1042) is a People’s Republic of China-related threat actor associated with long-running intrusions in Indian critical infrastructure entities. [RedEcho](https://attack.mitre.org/groups/G1042) overlaps with various other PRC-linked threat groups, such as [APT41](https://attack.mitre.org/groups/G0096), and is linked to [ShadowPad](https://attack.mitre.org/software/S0596) malware use through shared infrastructure.[^2] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [RedEcho](https://attack.mitre.org/groups/G1042) used dynamic DNS domains associated with malicious infrastructure.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RedEcho](https://attack.mitre.org/groups/G1042) network activity is associated with SSL traffic via TCP 443 and proxied HTTP traffic over non-standard ports.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [RedEcho](https://attack.mitre.org/groups/G1042) has used non-standard ports such as TCP 8080 for HTTP communication.[^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [RedEcho](https://attack.mitre.org/groups/G1042) uses SSL for network communication.[^2]  |
| [[Domains\|T1583.001]] | Domains | [RedEcho](https://attack.mitre.org/groups/G1042) has registered domains spoofing Indian critical infrastructure entities.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ShadowPad\|S0596]] | ShadowPad | [RedEcho](https://attack.mitre.org/groups/G1042) has used [ShadowPad](https://attack.mitre.org/software/S0596) during intrusions.[^2] [^1]  |



## References

[^1]: [RecordedFuture RedEcho 2022](https://go.recordedfuture.com/hubfs/reports/ta-2022-0406.pdf)


[^2]: [RecordedFuture RedEcho 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


