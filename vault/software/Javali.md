---
aliases: 
    - S0528
    
mitre-attack: https://attack.mitre.org/software/S0528
---

## S0528

[Javali](https://attack.mitre.org/software/S0528) is a banking trojan that has targeted Portuguese and Spanish-speaking countries since 2017, primarily focusing on customers of financial institutions in Brazil and Mexico.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Javali](https://attack.mitre.org/software/S0528) can capture login credentials from open browsers including Firefox, Chrome, Internet Explorer, and Edge.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Javali](https://attack.mitre.org/software/S0528) can use DLL side-loading to load malicious DLLs into legitimate executables.[^1]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Javali](https://attack.mitre.org/software/S0528) can use large obfuscated libraries to hinder detection and analysis.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Javali](https://attack.mitre.org/software/S0528) has been delivered via malicious links embedded in e-mails.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Javali](https://attack.mitre.org/software/S0528) has achieved execution through victims clicking links to malicious websites.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Javali](https://attack.mitre.org/software/S0528) can monitor processes for open browsers and custom banking applications.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Javali](https://attack.mitre.org/software/S0528) has used the MSI installer to download and execute malicious payloads.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Javali](https://attack.mitre.org/software/S0528) can read C2 information from Google Documents and YouTube.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Javali](https://attack.mitre.org/software/S0528) has achieved execution through victims opening malicious attachments, including MSI files with embedded VBScript.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Javali](https://attack.mitre.org/software/S0528) has been delivered as malicious e-mail attachments.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Javali](https://attack.mitre.org/software/S0528) has used embedded VBScript to download malicious payloads from C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Javali](https://attack.mitre.org/software/S0528) can download payloads from remote C2 servers.[^1]  |




## References

[^1]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


