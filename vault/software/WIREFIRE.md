---
aliases: 
    - S1115
    
mitre-attack: https://attack.mitre.org/software/S1115
---

## S1115

[WIREFIRE](https://attack.mitre.org/software/S1115) is a web shell written in Python that exists as trojanized logic to the visits.py component of Ivanti Connect Secure VPN appliances. [WIREFIRE](https://attack.mitre.org/software/S1115) was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) for downloading files and command execution.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WIREFIRE](https://attack.mitre.org/software/S1115) can decode, decrypt, and decompress data received in C2 HTTP `POST` requests.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [WIREFIRE](https://attack.mitre.org/software/S1115) is a web shell that can download files to and execute arbitrary commands from compromised Ivanti Connect Secure VPNs.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WIREFIRE](https://attack.mitre.org/software/S1115) has the ability to download files to compromised devices.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [WIREFIRE](https://attack.mitre.org/software/S1115) can Base64 encode process output sent to C2.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [WIREFIRE](https://attack.mitre.org/software/S1115) can AES encrypt process output sent from compromised devices to C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WIREFIRE](https://attack.mitre.org/software/S1115) can respond to specific HTTP `POST` requests to `/api/v1/cav/client/visits`.[^1] [^3]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [WIREFIRE](https://attack.mitre.org/software/S1115) can modify the `visits.py` component of Ivanti Connect Secure VPNs for file download and arbitrary command execution.[^1] [^3]  |




## References

[^1]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^2]: GIFTEDVISITOR


[^3]: [Volexity Ivanti Zero-Day Exploitation January 2024](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)


