---
aliases: 
    - S0042
    
mitre-attack: https://attack.mitre.org/software/S0042
---

## S0042

[LOWBALL](https://attack.mitre.org/software/S0042) is malware used by [admin@338](https://attack.mitre.org/groups/G0018). It was used in August 2015 in email messages targeting Hong Kong-based media organizations. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LOWBALL](https://attack.mitre.org/software/S0042) command and control occurs via HTTPS over port 443.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LOWBALL](https://attack.mitre.org/software/S0042) uses the Dropbox API to request two files, one of which is the same file as the one dropped by the malicious email attachment. This is most likely meant to be a mechanism to update the compromised host with a new version of the [LOWBALL](https://attack.mitre.org/software/S0042) malware.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [LOWBALL](https://attack.mitre.org/software/S0042) uses the Dropbox cloud storage service for command and control.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[admin@338\|G0018]] | admin@338 |



## References

[^1]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


