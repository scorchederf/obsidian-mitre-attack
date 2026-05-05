---
aliases: 
    - S0334
    
mitre-attack: https://attack.mitre.org/software/S0334
---

## S0334

[DarkComet](https://attack.mitre.org/software/S0334) is a Windows remote administration tool and backdoor.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [DarkComet](https://attack.mitre.org/software/S0334) can disable Security Center functions like the Windows Firewall.[^1] [^2]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [DarkComet](https://attack.mitre.org/software/S0334) can execute various types of scripts on the victim’s machine.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [DarkComet](https://attack.mitre.org/software/S0334) can steal data from the clipboard.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [DarkComet](https://attack.mitre.org/software/S0334) can access the victim’s webcam to take pictures.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DarkComet](https://attack.mitre.org/software/S0334) can collect the computer name, RAM used, and operating system version from the victim’s machine.[^1] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DarkComet](https://attack.mitre.org/software/S0334) can load any files onto the infected machine to execute.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [DarkComet](https://attack.mitre.org/software/S0334) can list active processes running on the victim’s machine.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DarkComet](https://attack.mitre.org/software/S0334) can launch a remote shell to execute commands on the victim’s machine.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [DarkComet](https://attack.mitre.org/software/S0334) can open an active screen of the victim’s machine and take control of the mouse and keyboard.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [DarkComet](https://attack.mitre.org/software/S0334) adds several Registry entries to enable automatic execution at every system startup.[^1] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [DarkComet](https://attack.mitre.org/software/S0334) can disable Security Center functions like anti-virus.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [DarkComet](https://attack.mitre.org/software/S0334) can use HTTP for C2 communications.[^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [DarkComet](https://attack.mitre.org/software/S0334) can listen in to victims' conversations through the system’s microphone.[^1] [^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [DarkComet](https://attack.mitre.org/software/S0334) has the option to compress its payload using UPX or MPRESS.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [DarkComet](https://attack.mitre.org/software/S0334) adds a Registry value for its installation routine to the Registry Key `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System Enable LUA=”0”` and `HKEY_CURRENT_USER\Software\DC3_FEXEC`.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DarkComet](https://attack.mitre.org/software/S0334) has a keylogging capability.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [DarkComet](https://attack.mitre.org/software/S0334) gathers the username from the victim’s machine.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [DarkComet](https://attack.mitre.org/software/S0334) has dropped itself onto victim machines with file names such as WinDefender.Exe and winupdate.exe in an apparent attempt to masquerade as a legitimate file.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Transparent Tribe\|G0134]] | Transparent Tribe |
| [[SilverTerrier\|G0083]] | SilverTerrier |
| [[APT38\|G0082]] | APT38 |



## References

[^1]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^2]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^3]: DarkKomet


[^4]: [Unit42 SilverTerrier 2018](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)


[^5]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^6]: [Unit 42 ProjectM March 2016](https://unit42.paloaltonetworks.com/unit42-projectm-link-found-between-pakistani-actor-and-operation-transparent-tribe/)


[^7]: Fynloski


[^8]: Krademok


[^9]: FYNLOS


[^10]: DarkComet


