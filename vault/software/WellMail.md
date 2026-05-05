---
aliases: 
    - S0515
    
mitre-attack: https://attack.mitre.org/software/S0515
---

## S0515

[WellMail](https://attack.mitre.org/software/S0515) is a lightweight malware written in Golang used by [APT29](https://attack.mitre.org/groups/G0016), similar in design and structure to [WellMess](https://attack.mitre.org/software/S0514).[^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WellMail](https://attack.mitre.org/software/S0515) can receive data and executable scripts from C2.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [WellMail](https://attack.mitre.org/software/S0515) has been observed using TCP port 25, without using SMTP, to leverage an open port for secure command and control communications.[^1] [^3]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [WellMail](https://attack.mitre.org/software/S0515) can archive files on the compromised host.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [WellMail](https://attack.mitre.org/software/S0515) can use TCP for C2 communications.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [WellMail](https://attack.mitre.org/software/S0515) can identify the current username on the victim system.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [WellMail](https://attack.mitre.org/software/S0515) can identify the IP address of the victim system.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WellMail](https://attack.mitre.org/software/S0515) can decompress scripts received from C2.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [WellMail](https://attack.mitre.org/software/S0515) can use hard coded client and certificate authority certificates to communicate with C2 over mutual TLS.[^1] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [WellMail](https://attack.mitre.org/software/S0515) can exfiltrate files from the victim machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^2]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^3]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)


