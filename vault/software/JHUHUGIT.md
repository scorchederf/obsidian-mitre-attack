---
aliases: 
    - S0044
    
mitre-attack: https://attack.mitre.org/software/S0044
---

## S0044

[JHUHUGIT](https://attack.mitre.org/software/S0044) is malware used by [APT28](https://attack.mitre.org/groups/G0007). It is based on Carberp source code and serves as reconnaissance malware. [^1]  [^11]  [^13]  [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | A [JHUHUGIT](https://attack.mitre.org/software/S0044) variant takes screenshots by simulating the user pressing the "Take Screenshot" key (VK_SCREENSHOT), accessing the screenshot saved in the clipboard, and converting it to a JPG image.[^18] [^10]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [JHUHUGIT](https://attack.mitre.org/software/S0044) tests if it can reach its C2 server by first attempting a direct connection, and if it fails, obtaining proxy settings and sending the connection through a proxy, and finally injecting code into a running browser if the proxy method fails.[^13]  |
| [[Process Discovery\|T1057]] | Process Discovery | [JHUHUGIT](https://attack.mitre.org/software/S0044) obtains a list of running processes on the victim.[^13] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | A [JHUHUGIT](https://attack.mitre.org/software/S0044) variant gathers network interface card information.[^18]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [JHUHUGIT](https://attack.mitre.org/software/S0044) has registered itself as a scheduled task to run each time the current user logs in.[^13] [^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | A [JHUHUGIT](https://attack.mitre.org/software/S0044) variant encodes C2 POST data base64.[^18]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [JHUHUGIT](https://attack.mitre.org/software/S0044) variants have communicated with C2 servers over HTTP and HTTPS.[^13] [^2] [^18]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [JHUHUGIT](https://attack.mitre.org/software/S0044) has used a Registry Run key to establish persistence by executing JavaScript code within the rundll32.exe process.[^13]  |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | [JHUHUGIT](https://attack.mitre.org/software/S0044) has registered a Windows shell script under the Registry key `HKCU\Environment\UserInitMprLogonScript` to establish persistence.[^13] [^10]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | A [JHUHUGIT](https://attack.mitre.org/software/S0044) variant accesses a screenshot saved in the clipboard and converts it to a JPG image.[^18]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [JHUHUGIT](https://attack.mitre.org/software/S0044) uses a .bat file to execute a .dll.[^10]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [JHUHUGIT](https://attack.mitre.org/software/S0044) has exploited CVE-2015-1701 and CVE-2015-2387 to escalate privileges.[^13] [^5]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [JHUHUGIT](https://attack.mitre.org/software/S0044) has used COM hijacking to establish persistence by hijacking a class named MMDeviceEnumerator and also by registering the payload as a Shell Icon Overlay handler COM object ({3543619C-D563-43f7-95EA-4DA7E1CC396A}).[^13] [^10]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Many strings in [JHUHUGIT](https://attack.mitre.org/software/S0044) are obfuscated with a XOR algorithm.[^11] [^13] [^10]  |
| [[Windows Service\|T1543.003]] | Windows Service | [JHUHUGIT](https://attack.mitre.org/software/S0044) has registered itself as a service to establish persistence.[^13]  |
| [[Process Injection\|T1055]] | Process Injection | [JHUHUGIT](https://attack.mitre.org/software/S0044) performs code injection injecting its own functions to browser processes.[^11] [^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [JHUHUGIT](https://attack.mitre.org/software/S0044) is executed using rundll32.exe.[^11] [^10]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [JHUHUGIT](https://attack.mitre.org/software/S0044) obtains a build identifier as well as victim hard drive information from Windows registry key `HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum`. Another [JHUHUGIT](https://attack.mitre.org/software/S0044) variant gathers the victim storage volume serial number and the storage device name.[^13] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | The [JHUHUGIT](https://attack.mitre.org/software/S0044) dropper can delete itself from the victim. Another [JHUHUGIT](https://attack.mitre.org/software/S0044) variant has the capability to delete specified files.[^13] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [JHUHUGIT](https://attack.mitre.org/software/S0044) can retrieve an additional payload from its C2 server.[^13] [^2]  [JHUHUGIT](https://attack.mitre.org/software/S0044) has a command to download files to the victim’s machine.[^10]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)


[^2]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^3]: Seduploader


[^4]: [FireEye APT28 January 2017](https://www.mandiant.com/sites/default/files/2021-09/APT28-Center-of-Storm-2017.pdf)


[^5]: [ESET Sednit July 2015](http://www.welivesecurity.com/2015/07/10/sednit-apt-group-meets-hacking-team/)


[^6]: Sednit


[^7]: [US District Court Indictment GRU Oct 2018](https://www.justice.gov/opa/page/file/1098481/download)


[^8]: GAMEFISH


[^9]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^10]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^11]: [F-Secure Sofacy 2015](https://labsblog.f-secure.com/2015/09/08/sofacy-recycles-carberp-and-metasploit-code/)


[^12]: Trojan.Sofacy


[^13]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^14]: JHUHUGIT


[^15]: SofacyCarberp


[^16]: JKEYSKW


[^17]: [Symantec APT28 Oct 2018](https://www.symantec.com/blogs/election-security/apt28-espionage-military-government)


[^18]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^19]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)


