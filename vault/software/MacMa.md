---
aliases: 
    - S1016
    
mitre-attack: https://attack.mitre.org/software/S1016
---

## S1016

[MacMa](https://attack.mitre.org/software/S1016) is a macOS-based backdoor with a large set of functionalities to control and exfiltrate files from a compromised computer. [MacMa](https://attack.mitre.org/software/S1016) has been observed in the wild since November 2021.[^5]  [MacMa](https://attack.mitre.org/software/S1016) shares command and control and unique libraries with [MgBot](https://attack.mitre.org/software/S1146) and [Nightdoor](https://attack.mitre.org/software/S1147), indicating a relationship with the [Daggerfly](https://attack.mitre.org/groups/G1034) threat actor.[^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MacMa](https://attack.mitre.org/software/S1016) can collect the username from the compromised machine.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MacMa](https://attack.mitre.org/software/S1016) can collect information about a compromised computer, including: Hardware UUID, Mac serial number, and macOS version.[^5]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [MacMa](https://attack.mitre.org/software/S1016) has used a custom JSON-based protocol for its C&C communications.[^5]  |
| [[Code Signing\|T1553.002]] | Code Signing | [MacMa](https://attack.mitre.org/software/S1016) has been delivered using ad hoc Apple Developer code signing certificates.[^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [MacMa](https://attack.mitre.org/software/S1016) has used Apple’s Core Graphic APIs, such as `CGWindowListCreateImageFromArray`, to capture the user's screen and open windows.[^5] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [MacMa](https://attack.mitre.org/software/S1016) can collect IP addresses from a compromised host.[^5]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MacMa](https://attack.mitre.org/software/S1016) has stored collected files locally before exfiltration.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [MacMa](https://attack.mitre.org/software/S1016) installs a `com.apple.softwareupdate.plist` file in the `/LaunchAgents` folder with the `RunAtLoad` value set to `true`. Upon user login, [MacMa](https://attack.mitre.org/software/S1016) is executed from `/var/root/.local/softwareupdate` with root privileges. Some variations also include the `LimitLoadToSessionType` key with the value `Aqua`, ensuring the [MacMa](https://attack.mitre.org/software/S1016) only runs when there is a logged in GUI user.[^5] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MacMa](https://attack.mitre.org/software/S1016) can collect then exfiltrate files from the compromised system.[^5]  |
| [[Remote Services\|T1021]] | Remote Services | [MacMa](https://attack.mitre.org/software/S1016) can manage remote screen sessions.[^5]  |
| [[Native API\|T1106]] | Native API | [MacMa](https://attack.mitre.org/software/S1016) has used macOS API functions to perform tasks.[^5] [^2]  |
| [[Audio Capture\|T1123]] | Audio Capture | [MacMa](https://attack.mitre.org/software/S1016) has the ability to record audio.[^2]  |
| [[Keychain\|T1555.001]] | Keychain | [MacMa](https://attack.mitre.org/software/S1016) can dump credentials from the macOS keychain.[^5]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MacMa](https://attack.mitre.org/software/S1016) exfiltrates data from a supplied path over its C2 channel.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MacMa](https://attack.mitre.org/software/S1016) can enumerate running processes.[^5]  |
| [[Timestomp\|T1070.006]] | Timestomp | [MacMa](https://attack.mitre.org/software/S1016) has the capability to create and modify file timestamps.[^5]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [MacMa](https://attack.mitre.org/software/S1016) has used TCP port 5633 for C2 Communication.[^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MacMa](https://attack.mitre.org/software/S1016) decrypts a downloaded file using AES-128-EBC with a custom delta.[^5]  |
| [[Keylogging\|T1056.001]] | Keylogging | [MacMa](https://attack.mitre.org/software/S1016) can use Core Graphics Event Taps to intercept user keystrokes from any text input field and saves them to text files. Text input fields include Spotlight, Finder, Safari, Mail, Messages, and other apps that have text fields for passwords.[^2] [^6]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [MacMa](https://attack.mitre.org/software/S1016) can clear possible malware traces such as application logs.[^5]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [MacMa](https://attack.mitre.org/software/S1016) can execute supplied shell commands and uses bash scripts to perform additional actions.[^5] [^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [MacMa](https://attack.mitre.org/software/S1016) can collect information about a compromised computer's disk sizes.[^5]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | [MacMa](https://attack.mitre.org/software/S1016) has removed the `com.apple.quarantineattribute` from the dropped file, `$TMPDIR/airportpaird`.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MacMa](https://attack.mitre.org/software/S1016) has downloaded additional files, including an exploit for used privilege escalation.[^5] [^2]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [MacMa](https://attack.mitre.org/software/S1016) has used TLS encryption to initialize a custom protocol for C2 communications.[^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MacMa](https://attack.mitre.org/software/S1016) can search for a specific file on the compromised computer and can enumerate files in Desktop, Downloads, and Documents folders.[^5]  |
| [[File Deletion\|T1070.004]] | File Deletion | [MacMa](https://attack.mitre.org/software/S1016) can delete itself from the compromised computer.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Daggerfly\|G1034]] | Daggerfly |



## References

[^1]: DazzleSpy


[^2]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)


[^3]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)


[^4]: OSX.CDDS


[^5]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^6]: [SentinelOne MacMa Nov 2021](https://www.sentinelone.com/labs/infect-if-needed-a-deeper-dive-into-targeted-backdoor-macos-macma/)


[^7]: [SentinelOne Macma 2021](https://www.sentinelone.com/labs/infect-if-needed-a-deeper-dive-into-targeted-backdoor-macos-macma/)


