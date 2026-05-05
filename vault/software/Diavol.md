---
aliases: 
    - S0659
    
mitre-attack: https://attack.mitre.org/software/S0659
---

## S0659

[Diavol](https://attack.mitre.org/software/S0659) is a ransomware variant first observed in June 2021 that is capable of prioritizing file types to encrypt based on a pre-configured list of extensions defined by the attacker.  The [Diavol](https://attack.mitre.org/software/S0659) Ransomware-as-a Service (RaaS) program is managed by [Wizard Spider](https://attack.mitre.org/groups/G0102) and it has been observed being deployed by [Bazar](https://attack.mitre.org/software/S0534).[^4] [^5] [^1] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Destruction\|T1485]] | Data Destruction | [Diavol](https://attack.mitre.org/software/S0659) can delete specified files from a targeted system.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Diavol](https://attack.mitre.org/software/S0659) can collect the username from a compromised host.[^4]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Diavol](https://attack.mitre.org/software/S0659) has encrypted files using an RSA key though the `CryptEncrypt` API and has appended filenames with ".lock64". [^4]  |
| [[Service Stop\|T1489]] | Service Stop | [Diavol](https://attack.mitre.org/software/S0659) will terminate services using the Service Control Manager (SCM) API.[^4]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Diavol](https://attack.mitre.org/software/S0659) has a command to traverse the files and directories in a given path.[^4]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Diavol](https://attack.mitre.org/software/S0659) has used HTTP GET and POST requests for C2.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Diavol](https://attack.mitre.org/software/S0659) has used `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next` API calls to enumerate the running processes in the system.[^4]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Diavol](https://attack.mitre.org/software/S0659) has a `ENMDSKS` command to enumerates available network shares.[^4]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Diavol](https://attack.mitre.org/software/S0659) can attempt to stop security software.[^4]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Diavol](https://attack.mitre.org/software/S0659) can spread throughout a network via SMB prior to encryption.[^4]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement |  After encryption, [Diavol](https://attack.mitre.org/software/S0659) will capture the desktop background window, set the background color to black, and change the desktop wallpaper to a newly created bitmap image with the text “All your files are encrypted! For more information see “README-FOR-DECRYPT.txt".[^4]  |
| [[Steganography\|T1027.003]] | Steganography | [Diavol](https://attack.mitre.org/software/S0659) has obfuscated its main code routines within bitmap images as part of its anti-analysis techniques.[^4]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Diavol](https://attack.mitre.org/software/S0659) can enumerate victims' local and external IPs when registering with C2.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Diavol](https://attack.mitre.org/software/S0659) has Base64 encoded the RSA public key used for encrypting files.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Diavol](https://attack.mitre.org/software/S0659) can use the ARP table to find remote hosts to scan.[^4]   |
| [[Native API\|T1106]] | Native API | [Diavol](https://attack.mitre.org/software/S0659) has used several API calls like `GetLogicalDriveStrings`, `SleepEx`, `SystemParametersInfoAPI`, `CryptEncrypt`, and others to execute parts of its attack.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Diavol](https://attack.mitre.org/software/S0659) can collect the computer name and OS version from the system.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Diavol](https://attack.mitre.org/software/S0659) can receive configuration updates and additional payloads including wscpy.exe from C2.[^4]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Diavol](https://attack.mitre.org/software/S0659) can delete shadow copies using the `IVssBackupComponents` COM object to call the `DeleteSnapshots` method.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [DFIR Diavol Ransomware December 2021](https://thedfirreport.com/2021/12/13/diavol-ransomware/)


[^2]: Diavol


[^3]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^4]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^5]: [FBI Flash Diavol January 2022](https://www.ic3.gov/CSA/2022/220120.pdf)


