---
aliases: 
    - S0514
    
mitre-attack: https://attack.mitre.org/software/S0514
---

## S0514

[WellMess](https://attack.mitre.org/software/S0514) is lightweight malware family with variants written in .NET and Golang that has been in use since at least 2018 by [APT29](https://attack.mitre.org/groups/G0016).[^5] [^1] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [WellMess](https://attack.mitre.org/software/S0514) can collect the username on the victim machine to send to C2.[^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [WellMess](https://attack.mitre.org/software/S0514) can execute PowerShell scripts received from C2.[^1] [^5]  |
| [[Data from Local System\|T1005]] | Data from Local System | [WellMess](https://attack.mitre.org/software/S0514) can send files from the victim machine to C2.[^1] [^5]  |
| [[DNS\|T1071.004]] | DNS | [WellMess](https://attack.mitre.org/software/S0514) has the ability to use DNS tunneling for C2 communications.[^1] [^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [WellMess](https://attack.mitre.org/software/S0514) can identify the computer name of a compromised host.[^1] [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WellMess](https://attack.mitre.org/software/S0514) can write files to a compromised host.[^1] [^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [WellMess](https://attack.mitre.org/software/S0514) can communicate to C2 with mutual TLS where client and server mutually check certificates.[^1] [^2] [^5] [^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [WellMess](https://attack.mitre.org/software/S0514) has used Base64 encoding to uniquely identify communication to and from the C2.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [WellMess](https://attack.mitre.org/software/S0514) can encrypt HTTP POST data using RC6 and a dynamically generated AES key encrypted with a hard coded RSA public key.[^1] [^2] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WellMess](https://attack.mitre.org/software/S0514) can execute command line scripts received from C2.[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [WellMess](https://attack.mitre.org/software/S0514) can identify domain group membership for the current user.[^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [WellMess](https://attack.mitre.org/software/S0514) can identify the IP address and user domain on the target machine.[^1] [^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WellMess](https://attack.mitre.org/software/S0514) can decode and decrypt data received from C2.[^1] [^2] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WellMess](https://attack.mitre.org/software/S0514) can use HTTP and HTTPS in C2 communications.[^1] [^2] [^5] [^4]  |
| [[Junk Data\|T1001.001]] | Junk Data | [WellMess](https://attack.mitre.org/software/S0514) can use junk data in the Base64 string for additional obfuscation.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^2]: [PWC WellMess C2 August 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/wellmess-analysis-command-control.html)


[^3]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^4]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)


[^5]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


