---
aliases: 
    - S0089
    
mitre-attack: https://attack.mitre.org/software/S0089
---

## S0089

[BlackEnergy](https://attack.mitre.org/software/S0089) is a malware toolkit that has been used by both criminal and APT actors. It dates back to at least 2007 and was originally designed to create botnets for use in conducting Distributed Denial of Service (DDoS) attacks, but its use has evolved to support various plug-ins. It is well known for being used during the confrontation between Georgia and Russia in 2008, as well as in targeting Ukrainian institutions. Variants include BlackEnergy 2 and BlackEnergy 3. [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [BlackEnergy](https://attack.mitre.org/software/S0089) attempts to bypass default User Access Control (UAC) settings by exploiting a backward-compatibility setting found in Windows 7 and later.[^8]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | A [BlackEnergy](https://attack.mitre.org/software/S0089) 2 plug-in uses WMI to gather victim host details.[^5]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [BlackEnergy](https://attack.mitre.org/software/S0089) has used a plug-in to gather credentials from web browsers including FireFox, Google Chrome, and Internet Explorer.[^8] [^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [BlackEnergy](https://attack.mitre.org/software/S0089) has removed the watermark associated with enabling the `TESTSIGNING` boot configuration option by removing the relevant strings in the `user32.dll.mui` of the system.[^8]  |
| [[Screen Capture\|T1113]] | Screen Capture | [BlackEnergy](https://attack.mitre.org/software/S0089) is capable of taking screenshots.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [BlackEnergy](https://attack.mitre.org/software/S0089) injects its DLL component into svchost.exe.[^8]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | The [BlackEnergy](https://attack.mitre.org/software/S0089) component KillDisk is capable of deleting Windows Event Logs.[^4]  |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | [BlackEnergy](https://attack.mitre.org/software/S0089) has enabled the `TESTSIGNING` boot configuration option to facilitate loading of a driver component.[^8]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) has gathered a process list by using [Tasklist](https://attack.mitre.org/software/S0057).exe.[^8] [^1] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) gathers a list of installed apps from the uninstall program Registry. It also gathers registered mail, browser, and instant messaging clients from the Registry. [BlackEnergy](https://attack.mitre.org/software/S0089) has searched for given file types.[^8] [^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) has conducted port scans on a host.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [BlackEnergy](https://attack.mitre.org/software/S0089) has run a plug-in on a victim to spread through the local network by using [PsExec](https://attack.mitre.org/software/S0029) and accessing admin shares.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) has gathered information about local network connections using [netstat](https://attack.mitre.org/software/S0104).[^8] [^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) can gather very specific information about attached USB devices, to include device instance ID and drive geometry.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | The [BlackEnergy](https://attack.mitre.org/software/S0089) 3 variant drops its main DLL component and then creates a .lnk shortcut to that file in the startup folder.[^8]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [BlackEnergy](https://attack.mitre.org/software/S0089) has used a plug-in to gather credentials stored in files on the host by various software programs, including The Bat! email client, Outlook, and Windows Credential Store.[^8] [^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [BlackEnergy](https://attack.mitre.org/software/S0089) has run a keylogger plug-in on a victim.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | One variant of [BlackEnergy](https://attack.mitre.org/software/S0089) creates a new service using either a hard-coded or randomly generated name.[^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | The [BlackEnergy](https://attack.mitre.org/software/S0089) 3 variant drops its main DLL component and then creates a .lnk shortcut to that file in the startup folder.[^8]  |
| [[Data Destruction\|T1485]] | Data Destruction | [BlackEnergy](https://attack.mitre.org/software/S0089) 2 contains a "Destroy" plug-in that destroys data stored on victim hard drives by overwriting file contents.[^5] [^3]  |
| [[Services File Permissions Weakness\|T1574.010]] | Services File Permissions Weakness | One variant of [BlackEnergy](https://attack.mitre.org/software/S0089) locates existing driver services that have been disabled and drops its driver component into one of those service's paths, replacing the legitimate executable. The malware then sets the hijacked service to start automatically to establish persistence.[^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) has gathered information about network IP configurations using [ipconfig](https://attack.mitre.org/software/S0100).exe and about routing tables using [route](https://attack.mitre.org/software/S0103).exe.[^8] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BlackEnergy](https://attack.mitre.org/software/S0089) has used [Systeminfo](https://attack.mitre.org/software/S0096) to gather the OS version, as well as information on the system configuration, BIOS, the motherboard, and the processor.[^8] [^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [BlackEnergy](https://attack.mitre.org/software/S0089) has the capability to communicate over a backup channel via plus.google.com.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BlackEnergy](https://attack.mitre.org/software/S0089) communicates with its C2 server over HTTP.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)


[^2]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^3]: [ESET BlackEnergy Jan 2016](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)


[^4]: [ESEST Black Energy Jan 2016](http://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)


[^5]: [Securelist BlackEnergy Feb 2015](https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/)


[^6]: [iSIGHT Sandworm 2014](https://www.fireeye.com/blog/threat-research/2016/01/ukraine-and-sandworm-team.html)


[^7]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^8]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^9]: [UK NCSC Olympic Attacks October 2020](https://www.gov.uk/government/news/uk-exposes-series-of-russian-cyber-attacks-against-olympic-and-paralympic-games)


