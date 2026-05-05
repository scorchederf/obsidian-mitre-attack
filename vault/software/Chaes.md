---
aliases: 
    - S0631
    
mitre-attack: https://attack.mitre.org/software/S0631
---

## S0631

[Chaes](https://attack.mitre.org/software/S0631) is a multistage information stealer written in several programming languages that collects login credentials, credit card numbers, and other financial information. [Chaes](https://attack.mitre.org/software/S0631) was first observed in 2020, and appears to primarily target victims in Brazil as well as other e-commerce customers in Latin America.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Msiexec\|T1218.007]] | Msiexec | [Chaes](https://attack.mitre.org/software/S0631) has used .MSI files as an initial way to start the infection chain.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Chaes](https://attack.mitre.org/software/S0631) requires the user to click on the malicious Word document to execute the next part of the attack.[^2]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Chaes](https://attack.mitre.org/software/S0631) has used Base64 to encode C2 communications.[^2]   |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Chaes](https://attack.mitre.org/software/S0631) has used encryption for its C2 channel.[^2]   |
| [[Native API\|T1106]] | Native API | [Chaes](https://attack.mitre.org/software/S0631) used the `CreateFileW()` API function with read permissions to access downloaded payloads.[^2]   |
| [[InstallUtil\|T1218.004]] | InstallUtil | [Chaes](https://attack.mitre.org/software/S0631) has used Installutill to download content.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Chaes](https://attack.mitre.org/software/S0631) has used VBscript to execute malicious code.[^2]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Chaes](https://attack.mitre.org/software/S0631) has been delivered by sending victims a phishing email containing a malicious .docx file.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Chaes](https://attack.mitre.org/software/S0631) has collected the username and UID from the infected machine.[^2]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [Chaes](https://attack.mitre.org/software/S0631) has exfiltrated its collected data from the infected machine to the C2, sometimes using the MIME protocol.[^2]   |
| [[Python\|T1059.006]] | Python | [Chaes](https://attack.mitre.org/software/S0631) has used Python scripts for execution and the installation of additional files.[^2]   |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Chaes](https://attack.mitre.org/software/S0631) has used a script that extracts the web session cookie and sends it to the C2 server.[^2]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Chaes](https://attack.mitre.org/software/S0631) has used an unsigned, crafted DLL module named `hha.dll` that was designed to look like a legitimate 32-bit Windows DLL.[^2]  |
| [[Template Injection\|T1221]] | Template Injection | [Chaes](https://attack.mitre.org/software/S0631) changed the template target of the settings.xml file embedded in the Word document and populated that field with the downloaded URL of the next payload.[^2]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Chaes](https://attack.mitre.org/software/S0631) can modify Registry values to stored information and establish persistence.[^2]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Chaes](https://attack.mitre.org/software/S0631) has added persistence via the Registry key `software\microsoft\windows\currentversion\run\microsoft windows html help`.[^2]  |
| [[Input Capture\|T1056]] | Input Capture | [Chaes](https://attack.mitre.org/software/S0631) has a module to perform any API hooking it desires.[^2]   |
| [[DLL\|T1574.001]] | DLL | [Chaes](https://attack.mitre.org/software/S0631) has used search order hijacking to load a malicious DLL.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | Some versions of [Chaes](https://attack.mitre.org/software/S0631) stored its instructions (otherwise in a `instructions.ini` file) in the Registry.[^2]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Chaes](https://attack.mitre.org/software/S0631) has used HTTP for C2 communications.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Chaes](https://attack.mitre.org/software/S0631) has used [cmd](https://attack.mitre.org/software/S0106) to execute tasks on the system.[^2]   |
| [[JavaScript\|T1059.007]] | JavaScript | [Chaes](https://attack.mitre.org/software/S0631) has used JavaScript and Node.Js information stealer script that exfiltrates data using the node process.[^2]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Chaes](https://attack.mitre.org/software/S0631) has used the Puppeteer module to hook and monitor the Chrome web browser to collect user information from infected hosts.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Chaes](https://attack.mitre.org/software/S0631) can download additional files onto an infected machine.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Chaes](https://attack.mitre.org/software/S0631) can capture screenshots of the infected machine.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Chaes](https://attack.mitre.org/software/S0631) has decrypted an AES encrypted binary file to trigger the download of other files.[^2]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Chaes](https://attack.mitre.org/software/S0631) has collected system information, including the machine name and OS version.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Chaes](https://attack.mitre.org/software/S0631) can steal login credentials and stored financial information from the browser.[^2]  |




## References

[^1]: Chaes


[^2]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


