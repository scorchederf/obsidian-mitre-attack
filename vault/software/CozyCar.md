---
aliases: 
    - S0046
    
mitre-attack: https://attack.mitre.org/software/S0046
---

## S0046

[CozyCar](https://attack.mitre.org/software/S0046) is malware that was used by [APT29](https://attack.mitre.org/groups/G0016) from 2010 to 2015. It is a modular malware platform, and its backdoor component can be instructed to download and execute a variety of modules with different functionality. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | A module in [CozyCar](https://attack.mitre.org/software/S0046) allows arbitrary commands to be executed by invoking `C:\Windows\System32\cmd.exe`.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | A system info module in [CozyCar](https://attack.mitre.org/software/S0046) gathers information on the victim host’s configuration.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CozyCar](https://attack.mitre.org/software/S0046)'s main method of communicating with its C2 servers is using HTTP or HTTPS.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [CozyCar](https://attack.mitre.org/software/S0046) uses Twitter as a backup C2 channel to Twitter accounts specified in its configuration file.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | One persistence mechanism used by [CozyCar](https://attack.mitre.org/software/S0046) is to set itself to be executed at system startup by adding a Registry value under one of the following Registry keys: <br>`HKLM\Software\Microsoft\Windows\CurrentVersion\Run\` <br>`HKCU\Software\Microsoft\Windows\CurrentVersion\Run\` <br>`HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run` <br>`HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run`[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | The main [CozyCar](https://attack.mitre.org/software/S0046) dropper checks whether the victim has an anti-virus product installed. If the installed product is on a predetermined list, the dropper will exit.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | The [CozyCar](https://attack.mitre.org/software/S0046) dropper copies the system file rundll32.exe to the install location for the malware, then uses the copy of rundll32.exe to load and execute the main [CozyCar](https://attack.mitre.org/software/S0046) component.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [CozyCar](https://attack.mitre.org/software/S0046) has executed [Mimikatz](https://attack.mitre.org/software/S0002) to harvest stored credentials from the victim and further victim penetration.[^2]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | Some versions of [CozyCar](https://attack.mitre.org/software/S0046) will check to ensure it is not being executed inside a virtual machine or a known malware analysis sandbox environment. If it detects that it is, it will exit.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The payload of [CozyCar](https://attack.mitre.org/software/S0046) is encrypted with simple XOR with a rotating key. The [CozyCar](https://attack.mitre.org/software/S0046) configuration file has been encrypted with RC4 keys.[^2]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | Password stealer and NTLM stealer modules in [CozyCar](https://attack.mitre.org/software/S0046) harvest stored credentials from the victim, including credentials used as part of Windows NTLM user authentication.[^2]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | The [CozyCar](https://attack.mitre.org/software/S0046) dropper has masqueraded a copy of the infected system's rundll32.exe executable that was moved to the malware's install directory and renamed according to a predefined configuration file.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | One persistence mechanism used by [CozyCar](https://attack.mitre.org/software/S0046) is to register itself as a scheduled task.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | One persistence mechanism used by [CozyCar](https://attack.mitre.org/software/S0046) is to register itself as a Windows service.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^3]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


