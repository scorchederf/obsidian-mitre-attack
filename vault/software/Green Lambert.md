---
aliases: 
    - S0690
    
mitre-attack: https://attack.mitre.org/software/S0690
---

## S0690

[Green Lambert](https://attack.mitre.org/software/S0690) is a modular backdoor that security researchers assess has been used by an advanced threat group referred to as Longhorn and The Lamberts. First reported in 2017, the Windows variant of [Green Lambert](https://attack.mitre.org/software/S0690) may have been used as early as 2008; a macOS version was uploaded to a multiscanner service in September 2014.[^3] [^2]   

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [Green Lambert](https://attack.mitre.org/software/S0690) can add a plist file in the `Library/LaunchDaemons` to establish persistence.[^2] [^4]   |
| [[Keychain\|T1555.001]] | Keychain | [Green Lambert](https://attack.mitre.org/software/S0690) can use Keychain Services API functions to find and collect passwords, such as `SecKeychainFindInternetPassword` and `SecKeychainItemCopyAttributesAndData`.[^2] [^4]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Green Lambert](https://attack.mitre.org/software/S0690) can use `uname` to identify the operating system name, version, and processor type.[^2] [^4]    |
| [[DNS\|T1071.004]] | DNS | [Green Lambert](https://attack.mitre.org/software/S0690) can use DNS for C2 communications.[^2] [^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Green Lambert](https://attack.mitre.org/software/S0690) can use multiple custom routines to decrypt strings prior to execution.[^2] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Green Lambert](https://attack.mitre.org/software/S0690) can obtain proxy information from a victim's machine using system environment variables.[^2] [^4]   |
| [[Proxy\|T1090]] | Proxy | [Green Lambert](https://attack.mitre.org/software/S0690) can use proxies for C2 traffic.[^2] [^4]  |
| [[Login Items\|T1547.015]] | Login Items | [Green Lambert](https://attack.mitre.org/software/S0690) can add [Login Items](https://attack.mitre.org/techniques/T1547/015) to establish persistence.[^2] [^4]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Green Lambert](https://attack.mitre.org/software/S0690) can delete the original executable after initial installation in addition to unused functions.[^2] [^4]   |
| [[Data from Local System\|T1005]] | Data from Local System | [Green Lambert](https://attack.mitre.org/software/S0690) can collect data from a compromised host.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Green Lambert](https://attack.mitre.org/software/S0690) has encrypted strings.[^2] [^4]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Green Lambert](https://attack.mitre.org/software/S0690) can use shell scripts for execution, such as `/bin/sh -c`.[^2] [^4]   |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | [Green Lambert](https://attack.mitre.org/software/S0690) can establish persistence on a compromised host through modifying the `profile`, `login`, and run command (rc) files associated with the `bash`, `csh`, and `tcsh` shells. [^2] [^4]   |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Green Lambert](https://attack.mitre.org/software/S0690) can create a [Launch Agent](https://attack.mitre.org/techniques/T1543/001) with the `RunAtLoad` key-value pair set to `true`, ensuring the `com.apple.GrowlHelper.plist` file runs every time a user logs in.[^2] [^4]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [Green Lambert](https://attack.mitre.org/software/S0690) can add `init.d` and `rc.d` files in the `/etc` folder to establish persistence.[^2] [^4]   |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Green Lambert](https://attack.mitre.org/software/S0690) has created a new executable named `Software Update Check` to appear legitimate.[^2] [^4]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Green Lambert](https://attack.mitre.org/software/S0690) has been disguised as a Growl help file.[^2] [^4]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Green Lambert](https://attack.mitre.org/software/S0690) can collect the date and time from a compromised host.[^2] [^4]  |




## References

[^1]: Green Lambert


[^2]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)


[^3]: [Kaspersky Lamberts Toolkit April 2017](https://securelist.com/unraveling-the-lamberts-toolkit/77990/)


[^4]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)


