---
aliases: 
    - S0598
    
mitre-attack: https://attack.mitre.org/software/S0598
---

## S0598

[P.A.S. Webshell](https://attack.mitre.org/software/S0598) is a publicly available multifunctional PHP webshell in use since at least 2016 that provides remote access and execution on target web servers.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can use a decryption mechanism to process a user supplied password and allow execution.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to list files and file characteristics including extension, size, ownership, and permissions.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can gain remote access and execution on target web servers.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to copy files on a compromised host.[^1]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to modify file permissions.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can issue commands via HTTP POST.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to create reverse shells with Perl scripts.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can list PHP server configuration details.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can use encryption and base64 encoding to hide strings and to enforce access control once deployed.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can delete scripts from a subdirectory of /tmp after they are run.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can scan networks for open ports and listening services.[^1]  |
| [[Databases\|T1213.006]] | Databases | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to list and extract data from SQL databases.[^1]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can use predefined users and passwords to execute brute force attacks against SSH, FTP, POP3, MySQL, MSSQL, and PostgreSQL services.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can upload and download files to and from compromised hosts.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can display the /etc/passwd file on a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^2]: [NCCIC AR-17-20045 February 2017](https://us-cert.cisa.gov/sites/default/files/publications/AR-17-20045_Enhanced_Analysis_of_GRIZZLY_STEPPE_Activity.pdf)


[^3]: Fobushell


[^4]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


