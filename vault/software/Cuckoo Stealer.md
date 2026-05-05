---
aliases: 
    - S1153
    
mitre-attack: https://attack.mitre.org/software/S1153
---

## S1153

[Cuckoo Stealer](https://attack.mitre.org/software/S1153) is a macOS malware with characteristics of spyware and an infostealer that has been in use since at least 2024. [Cuckoo Stealer](https://attack.mitre.org/software/S1153) is a universal Mach-O binary that can run on Intel or ARM-based Macs and has been spread through trojanized versions of various potentially unwanted programs or PUP's such as converters, cleaners, and uninstallers.[^2] [^1] <br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) strings are XOR-encrypted.[^2] [^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) has copied its binary and the victim's scraped password into a hidden folder in the `/Users` directory.[^2] [^1]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can check the systems `LANG` environmental variable to prevent infecting devices from Armenia (`hy_AM`), Belarus (`be_BY`), Kazakhstan (`kk_KZ`), Russia (`ru_RU`), and Ukraine (`uk_UA`).[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can discover and send the username from a compromised host to C2.[^2]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can determine the geographical location of a victim host by checking the language.[^2] <br> |
| [[Launchctl\|T1569.001]] | Launchctl | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use `launchctl` to load a LaunchAgent for persistence.[^2]  |
| [[Software Discovery\|T1518]] | Software Discovery | <br>[Cuckoo Stealer](https://attack.mitre.org/software/S1153) has the ability to search systems for installed applications.[^2]  |
| [[Plist File Modification\|T1647]] | Plist File Modification | <br>[Cuckoo Stealer](https://attack.mitre.org/software/S1153) can create and populate property list (plist) files to enable execution.[^2] [^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can run `screencapture` to collect screenshots from compromised hosts. [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) has staged collected application data from Safari, Notes, and Keychain to `/var/folder`.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use `ps aux` to enumerate running processes.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can search for files associated with specific applications.[^2] [^1]  |
| [[Stripped Payloads\|T1027.008]] | Stripped Payloads | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) is a stripped binary payload.[^2] <br>[^1] <br> |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) strings are deobfuscated prior to execution.[^2] [^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can send information about the targeted system to C2 including captured passwords, OS build, hostname, and username.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | <br>[Cuckoo Stealer](https://attack.mitre.org/software/S1153) has copied and renamed itself to DumpMediaSpotifyMusicConverter.[^2] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use the curl API for C2 communications.[^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can spawn a bash shell to enable execution on compromised hosts.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use sockets for communications to its C2 server.[^2]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use `xattr -d com.apple.quarantine` to remove the quarantine flag attribute.[^2] [^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can achieve persistence by creating launch agents to repeatedly execute malicious payloads.[^2] [^1]  |
| [[AppleScript\|T1059.002]] | AppleScript | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use osascript to generate a password-stealing prompt, duplicate files and folders, and set environmental variables.[^2] [^1]  |
| [[Keychain\|T1555.001]] | Keychain | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can capture files from a targeted user's keychain directory.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can gather information about the OS version and hardware on compromised hosts.[^2] [^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | <br>[Cuckoo Stealer](https://attack.mitre.org/software/S1153) has captured passwords by prompting victims with a “macOS needs to access System Settings” GUI window.[^2]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can collect bookmarks, cookies, and history from Safari.[^2]  |




## References

[^1]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)


[^2]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


