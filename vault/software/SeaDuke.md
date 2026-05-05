---
aliases: 
    - S0053
    
mitre-attack: https://attack.mitre.org/software/S0053
---

## S0053

[SeaDuke](https://attack.mitre.org/software/S0053) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2014 to 2015. It was used primarily as a secondary backdoor for victims that were already compromised with [CozyCar](https://attack.mitre.org/software/S0046). [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of executing commands.[^2]  |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | Some [SeaDuke](https://attack.mitre.org/software/S0053) samples have a module to use pass the ticket with Kerberos for authentication.[^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SeaDuke](https://attack.mitre.org/software/S0053) C2 traffic is base64-encoded.[^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | Some [SeaDuke](https://attack.mitre.org/software/S0053) samples have a module to extract email from Microsoft Exchange servers using compromised credentials.[^5]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [SeaDuke](https://attack.mitre.org/software/S0053) compressed data with zlib prior to sending it over C2.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of uploading and downloading files.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SeaDuke](https://attack.mitre.org/software/S0053) can securely delete files, including deleting itself from the victim.[^5]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | Some [SeaDuke](https://attack.mitre.org/software/S0053) samples have a module to extract email from Microsoft Exchange servers using compromised credentials.[^5]  |
| [[Software Packing\|T1027.002]] | Software Packing | [SeaDuke](https://attack.mitre.org/software/S0053) has been packed with the UPX packer.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SeaDuke](https://attack.mitre.org/software/S0053) uses HTTP and HTTPS for C2.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of persisting via the Registry Run key or a .lnk file stored in the Startup directory.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SeaDuke](https://attack.mitre.org/software/S0053) C2 traffic has been encrypted with RC4 and AES.[^3] [^2]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of persisting via a .lnk file stored in the Startup directory.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SeaDuke](https://attack.mitre.org/software/S0053) uses a module to execute Mimikatz with PowerShell to perform [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003).[^5]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [SeaDuke](https://attack.mitre.org/software/S0053) uses an event filter in WMI code to execute a previously dropped executable shortly after system startup.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^2]: [Unit 42 SeaDuke 2015](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)


[^3]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^4]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^5]: [Symantec Seaduke 2015](http://www.symantec.com/connect/blogs/forkmeiamfamous-seaduke-latest-weapon-duke-armory)


[^6]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


