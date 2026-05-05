---
aliases: 
    - S0491
    
mitre-attack: https://attack.mitre.org/software/S0491
---

## S0491

[StrongPity](https://attack.mitre.org/software/S0491) is an information stealing malware used by [PROMETHIUM](https://attack.mitre.org/groups/G0056).[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [StrongPity](https://attack.mitre.org/software/S0491) can automatically exfiltrate collected documents to the C2 server.[^1] [^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [StrongPity](https://attack.mitre.org/software/S0491) has the ability to hide the console window for its document search module from the user.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | <br>[StrongPity](https://attack.mitre.org/software/S0491) has used HTTPS over port 1402 in C2 communication.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [StrongPity](https://attack.mitre.org/software/S0491) can identify the IP address of a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [StrongPity](https://attack.mitre.org/software/S0491) can exfiltrate collected documents through C2 channels.[^1] [^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [StrongPity](https://attack.mitre.org/software/S0491) can compress and encrypt archived files into multiple .sft files with a repeated xor encryption scheme.[^1] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [StrongPity](https://attack.mitre.org/software/S0491) has named services to appear legitimate.[^1] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [StrongPity](https://attack.mitre.org/software/S0491) has used encrypted strings in its dropper component.[^1] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [StrongPity](https://attack.mitre.org/software/S0491) has been executed via compromised installation files for legitimate software including compression applications, security software, browsers, file recovery applications, and other tools and utilities.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [StrongPity](https://attack.mitre.org/software/S0491) can use HTTP and HTTPS in C2 communications.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [StrongPity](https://attack.mitre.org/software/S0491) can delete previously exfiltrated files from the compromised host.[^1] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [StrongPity](https://attack.mitre.org/software/S0491) can identify if ESET or BitDefender antivirus are installed before dropping its payload.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [StrongPity](https://attack.mitre.org/software/S0491) can parse the hard drive on a compromised host to identify specific file extensions.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [StrongPity](https://attack.mitre.org/software/S0491) has a file searcher component that can automatically collect and archive files based on a predefined list of file extensions.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [StrongPity](https://attack.mitre.org/software/S0491) can use PowerShell to add files to the Windows Defender exclusions list.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [StrongPity](https://attack.mitre.org/software/S0491) has created new services and modified existing services for persistence.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [StrongPity](https://attack.mitre.org/software/S0491) has encrypted C2 traffic using SSL/TLS.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [StrongPity](https://attack.mitre.org/software/S0491) can identify the hard disk volume serial number on a compromised host.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [StrongPity](https://attack.mitre.org/software/S0491) can add directories used by the malware to the Windows Defender exclusions list to prevent detection.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [StrongPity](https://attack.mitre.org/software/S0491) can use multiple layers of proxy servers to hide terminal nodes in its infrastructure.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [StrongPity](https://attack.mitre.org/software/S0491) can download files to specified targets.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [StrongPity](https://attack.mitre.org/software/S0491) can use the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` Registry key for persistence.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [StrongPity](https://attack.mitre.org/software/S0491) can determine if a user is logged in by checking to see if explorer.exe is running.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [StrongPity](https://attack.mitre.org/software/S0491) can install a service to execute itself as a service.[^1] [^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [StrongPity](https://attack.mitre.org/software/S0491) has been signed with self-signed certificates.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [StrongPity](https://attack.mitre.org/software/S0491) has been bundled with legitimate software installation files for disguise.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[PROMETHIUM\|G0056]] | PROMETHIUM |



## References

[^1]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^2]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


