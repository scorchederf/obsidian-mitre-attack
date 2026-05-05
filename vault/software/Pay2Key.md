---
aliases: 
    - S0556
    
mitre-attack: https://attack.mitre.org/software/S0556
---

## S0556

[Pay2Key](https://attack.mitre.org/software/S0556) is a ransomware written in C++ that has been used by [Fox Kitten](https://attack.mitre.org/groups/G0117) since at least July 2020 including campaigns against Israeli companies. [Pay2Key](https://attack.mitre.org/software/S0556) has been incorporated with a leak site to display stolen sensitive information to further pressure victims into payment.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Pay2Key](https://attack.mitre.org/software/S0556) has designated machines in the compromised network to serve as reverse proxy pivot points to channel communications with C2.[^1] [^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Pay2Key](https://attack.mitre.org/software/S0556) has used RSA encrypted communications with C2.[^2]  |
| [[Service Stop\|T1489]] | Service Stop | [Pay2Key](https://attack.mitre.org/software/S0556) can stop the MS SQL service at the end of the encryption process to release files locked by the service.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Pay2Key](https://attack.mitre.org/software/S0556) can remove its log file from disk.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Pay2Key](https://attack.mitre.org/software/S0556) has sent its public key to the C2 server over TCP.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Pay2Key](https://attack.mitre.org/software/S0556) has the ability to gather the hostname of the victim machine.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Pay2Key](https://attack.mitre.org/software/S0556) can encrypt data on victim's machines using RSA and AES algorithms in order to extort a ransom payment for decryption.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Pay2Key](https://attack.mitre.org/software/S0556) can identify the IP and MAC addresses of the compromised host.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Fox Kitten\|G0117]] | Fox Kitten |



## References

[^1]: [ClearkSky Fox Kitten February 2020](https://www.clearskysec.com/fox-kitten/)


[^2]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


