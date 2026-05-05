---
aliases: 
    - S1114
    
mitre-attack: https://attack.mitre.org/software/S1114
---

## S1114

[ZIPLINE](https://attack.mitre.org/software/S1114) is a passive backdoor that was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) on compromised Secure Connect VPNs for reverse shell and proxy functionality.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proxy\|T1090]] | Proxy | [ZIPLINE](https://attack.mitre.org/software/S1114) can create a proxy server on compromised hosts.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ZIPLINE](https://attack.mitre.org/software/S1114) can identify running processes and their names.[^1]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [ZIPLINE](https://attack.mitre.org/software/S1114) can identify a specific string in intercepted network traffic, `SSH-2.0-OpenSSH_0.3xx.`, to trigger its command functionality.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [ZIPLINE](https://attack.mitre.org/software/S1114) can communicate with C2 using a custom binary protocol.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [ZIPLINE](https://attack.mitre.org/software/S1114) can use AES-128-CBC to encrypt data for both upload and download.[^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [ZIPLINE](https://attack.mitre.org/software/S1114) can use `/bin/sh` to create a reverse shell and execute commands.[^1]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ZIPLINE](https://attack.mitre.org/software/S1114) can find and append specific files on Ivanti Connect Secure VPNs based upon received commands.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZIPLINE](https://attack.mitre.org/software/S1114) can download files to be saved on the compromised system.[^1] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools |  [ZIPLINE](https://attack.mitre.org/software/S1114) can add itself to the exclusion list for the Ivanti Connect Secure Integrity Checker Tool if the `--exclude` parameter is passed by the `tar` process.[^1]  |




## References

[^1]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^2]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


