---
aliases: 
    - S0584
    
mitre-attack: https://attack.mitre.org/software/S0584
---

## S0584

[AppleJeus](https://attack.mitre.org/software/S0584) is a family of downloaders initially discovered in 2018 embedded within trojanized cryptocurrency applications. [AppleJeus](https://attack.mitre.org/software/S0584) has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032), targeting companies in the energy, finance, government, industry, technology, and telecommunications sectors, and several countries including the United States, United Kingdom, South Korea, Australia, Brazil, New Zealand, and Russia. [AppleJeus](https://attack.mitre.org/software/S0584) has been used to distribute the [FALLCHILL](https://attack.mitre.org/software/S0181) RAT.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [AppleJeus](https://attack.mitre.org/software/S0584) has decoded files received from a C2.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [AppleJeus](https://attack.mitre.org/software/S0584) has deleted the MSI file after installation.[^3]  |
| [[Installer Packages\|T1546.016]] | Installer Packages | During [AppleJeus](https://attack.mitre.org/software/S0584)'s installation process, it uses `postinstall` scripts to extract a hidden plist from the application's `/Resources` folder and execute the `plist` file as a [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) with elevated permissions.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [AppleJeus](https://attack.mitre.org/software/S0584) has exfiltrated collected host information to a C2 server.[^3]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [AppleJeus](https://attack.mitre.org/software/S0584) has been distributed via spearphishing link.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [AppleJeus](https://attack.mitre.org/software/S0584) can install itself as a service.[^3]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [AppleJeus](https://attack.mitre.org/software/S0584) has added a leading `.` to plist filenames, unlisting them from the Finder app and default Terminal directory listings.[^3]  |
| [[Launchctl\|T1569.001]] | Launchctl | [AppleJeus](https://attack.mitre.org/software/S0584) has loaded a plist file using the `launchctl` command.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [AppleJeus](https://attack.mitre.org/software/S0584) has sent data to its C2 server via `POST` requests.[^3] [^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [AppleJeus](https://attack.mitre.org/software/S0584) has used a valid digital signature from Sectigo to appear legitimate.[^3]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [AppleJeus](https://attack.mitre.org/software/S0584) has used shell scripts to execute commands after installation and set persistence mechanisms.[^3] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [AppleJeus](https://attack.mitre.org/software/S0584) has collected the victim host information after infection.[^3]  |
| [[Msiexec\|T1218.007]] | Msiexec | [AppleJeus](https://attack.mitre.org/software/S0584) has been installed via MSI installer.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [AppleJeus](https://attack.mitre.org/software/S0584) has created a scheduled SYSTEM task that runs when a user logs in.[^3]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [AppleJeus](https://attack.mitre.org/software/S0584) has presented the user with a UAC prompt to elevate privileges while installing.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [AppleJeus](https://attack.mitre.org/software/S0584) has required user execution of a malicious MSI installer.[^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [AppleJeus](https://attack.mitre.org/software/S0584) has XOR-encrypted collected system information prior to sending to a C2. [AppleJeus](https://attack.mitre.org/software/S0584) has also used the open source ADVObfuscation library for its components.[^3]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [AppleJeus](https://attack.mitre.org/software/S0584) has waited a specified time before downloading a second stage payload.[^3]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [AppleJeus](https://attack.mitre.org/software/S0584) has placed a plist file within the `LaunchDaemons` folder and launched it manually.[^3] [^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [AppleJeus](https://attack.mitre.org/software/S0584)'s spearphishing links required user interaction to navigate to the malicious website.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [ObjectiveSee AppleJeus 2019](https://objective-see.org/blog/blog_0x49.html)


[^2]: AppleJeus


[^3]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


