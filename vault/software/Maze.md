---
aliases: 
    - S0449
    
mitre-attack: https://attack.mitre.org/software/S0449
---

## S0449

[Maze](https://attack.mitre.org/software/S0449) ransomware, previously known as "ChaCha", was discovered in May 2019. In addition to encrypting files on victim machines for impact, [Maze](https://attack.mitre.org/software/S0449) operators conduct information stealing campaigns prior to encryption and post the information online to extort affected companies.[^4] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Maze](https://attack.mitre.org/software/S0449) has disrupted systems by encrypting files on targeted machines, claiming to decrypt files if a ransom payment is made. [Maze](https://attack.mitre.org/software/S0449) has used the ChaCha algorithm, based on Salsa20, and an RSA algorithm to encrypt files.[^4]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Maze](https://attack.mitre.org/software/S0449) has inserted large blocks of junk code, including some components to decrypt strings and other important information for later in the encryption process.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Maze](https://attack.mitre.org/software/S0449) has checked the language of the infected system using the "GetUSerDefaultUILanguage" function.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Maze](https://attack.mitre.org/software/S0449) has created a file named "startup_vrun.bat" in the Startup folder of a virtual machine to establish persistence.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Maze](https://attack.mitre.org/software/S0449) operators have created scheduled tasks masquerading as "Windows Update Security", "Windows Update Security Patches", and "Google Chrome Security Update" designed to launch the ransomware.[^1]   |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Maze](https://attack.mitre.org/software/S0449) has checked the language of the machine with function `GetUserDefaultUILanguage` and terminated execution if the language matches with an entry in the predefined list.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Maze](https://attack.mitre.org/software/S0449) has used the "WNetOpenEnumW", "WNetEnumResourceW”, “WNetCloseEnum” and “WNetAddConnection2W” functions to enumerate the network resources on the infected machine.[^2]  |
| [[Run Virtual Instance\|T1564.006]] | Run Virtual Instance | [Maze](https://attack.mitre.org/software/S0449) operators have used VirtualBox and a Windows 7 virtual machine to run the ransomware; the virtual machine's configuration file mapped the shared network drives of the target company, presumably so [Maze](https://attack.mitre.org/software/S0449) can encrypt files on the shared drives as well as the local machine.[^1]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Maze](https://attack.mitre.org/software/S0449) has injected the malware DLL into a target process.[^2] [^1] 	 |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Maze](https://attack.mitre.org/software/S0449) has issued a shutdown command on a victim machine that, upon reboot, will run the ransomware within a VM.[^1]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Maze](https://attack.mitre.org/software/S0449) has forged POST strings with a random choice from a list of possibilities including "forum", "php", "view", etc. while making connection with the C2, hindering detection efforts.[^2]  |
| [[Native API\|T1106]] | Native API | [Maze](https://attack.mitre.org/software/S0449) has used several Windows API functions throughout the encryption process including IsDebuggerPresent, TerminateProcess, Process32FirstW, among others.[^2] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Maze](https://attack.mitre.org/software/S0449) has communicated to hard-coded IP addresses via HTTP.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | The [Maze](https://attack.mitre.org/software/S0449) encryption process has used batch scripts with various commands.[^4] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Maze](https://attack.mitre.org/software/S0449) has created scheduled tasks using name variants such as "Windows Update Security", "Windows Update Security Patches", and "Google Chrome Security Update", to launch [Maze](https://attack.mitre.org/software/S0449) at a specific time.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Maze](https://attack.mitre.org/software/S0449) has disabled dynamic analysis and other security tools including IDA debugger, x32dbg, and OllyDbg.[^2]  It has also disabled Windows Defender's Real-Time Monitoring feature and attempted to disable endpoint protection services.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Maze](https://attack.mitre.org/software/S0449) has used WMI to attempt to delete the shadow volumes on a machine, and to connect a virtual machine to the network domain of the victim organization's network.[^2] [^1]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Maze](https://attack.mitre.org/software/S0449) has gathered all of the running system processes.[^2] 	 |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Maze](https://attack.mitre.org/software/S0449) has used the “Wow64RevertWow64FsRedirection” function following attempts to delete the shadow volumes, in order to leave the system in the same state as it was prior to redirection.[^2] 	 |
| [[Service Stop\|T1489]] | Service Stop | [Maze](https://attack.mitre.org/software/S0449) has stopped SQL services to ensure it can encrypt any database.[^1]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Maze](https://attack.mitre.org/software/S0449) has decrypted strings and other important information during the encryption process. [Maze](https://attack.mitre.org/software/S0449) also calls certain functions dynamically to hinder analysis.[^2] 	 |
| [[Msiexec\|T1218.007]] | Msiexec | [Maze](https://attack.mitre.org/software/S0449) has delivered components for its ransomware attacks using MSI files, some of which have been executed from the command-line using `msiexec`.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Maze](https://attack.mitre.org/software/S0449) has attempted to delete the shadow volumes of infected machines, once before and once after the encryption process.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN6\|G0037]] | FIN6 |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)


[^2]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)


[^3]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^4]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


