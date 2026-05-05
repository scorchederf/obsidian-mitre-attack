---
aliases: 
    - S0595
    
mitre-attack: https://attack.mitre.org/software/S0595
---

## S0595

[ThiefQuest](https://attack.mitre.org/software/S0595) is a virus, data stealer, and wiper that presents itself as ransomware targeting macOS systems. [ThiefQuest](https://attack.mitre.org/software/S0595) was first seen in 2020 distributed via trojanized pirated versions of popular macOS software on Russian forums sharing torrent links.[^4]  Even though [ThiefQuest](https://attack.mitre.org/software/S0595) presents itself as ransomware, since the dynamically generated encryption key is never sent to the attacker it may be more appropriately thought of as a form of wiper malware.[^8] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [ThiefQuest](https://attack.mitre.org/software/S0595) encrypts a set of file extensions on a host, deletes the original files, and provides a ransom note with no contact information.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ThiefQuest](https://attack.mitre.org/software/S0595) uploads files via unencrypted HTTP. [^8] [^5]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [ThiefQuest](https://attack.mitre.org/software/S0595) hides a copy of itself in the user's `~/Library` directory by using a `.` at the beginning of the file name followed by 9 random characters.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [ThiefQuest](https://attack.mitre.org/software/S0595) uses the `CGEventTap` functions to perform keylogging.[^6]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [ThiefQuest](https://attack.mitre.org/software/S0595) uses the function `kill_unwanted` to obtain a list of running processes and kills each process matching a list of security related processes.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [ThiefQuest](https://attack.mitre.org/software/S0595) searches through the `/Users/` folder looking for executable files. For each executable, [ThiefQuest](https://attack.mitre.org/software/S0595) prepends a copy of itself to the beginning of the file. When the file is executed, the [ThiefQuest](https://attack.mitre.org/software/S0595) code is executed first. [ThiefQuest](https://attack.mitre.org/software/S0595) creates a hidden file, copies the original target executable to the file, then executes the new hidden file to maintain the appearance of normal behavior. [^8] [^5]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | When running with root privileges after a [Launch Agent](https://attack.mitre.org/techniques/T1543/001) is installed, [ThiefQuest](https://attack.mitre.org/software/S0595) installs a plist file to the `/Library/LaunchDaemons/` folder with the `RunAtLoad` key set to `true` establishing persistence as a Launch Daemon. [^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [ThiefQuest](https://attack.mitre.org/software/S0595) prepends a copy of itself to the beginning of an executable file while maintaining the name of the executable.[^8] [^5]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ThiefQuest](https://attack.mitre.org/software/S0595) exfiltrates targeted file extensions in the `/Users/` folder to the command and control server via unencrypted HTTP. Network packets contain a string with two pieces of information: a file path and the contents of the file in a base64 encoded string.[^8] [^5]  |
| [[AppleScript\|T1059.002]] | AppleScript | [ThiefQuest](https://attack.mitre.org/software/S0595) uses [AppleScript](https://attack.mitre.org/techniques/T1059/002)'s `osascript -e` command to launch [ThiefQuest](https://attack.mitre.org/software/S0595)'s persistence via [Launch Agent](https://attack.mitre.org/techniques/T1543/001) and [Launch Daemon](https://attack.mitre.org/techniques/T1543/004). [^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [ThiefQuest](https://attack.mitre.org/software/S0595) installs a launch item using an embedded encrypted launch agent property list template. The plist file is installed in the `~/Library/LaunchAgents/` folder and configured with the path to the persistent binary located in the `~/Library/` folder.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ThiefQuest](https://attack.mitre.org/software/S0595) obtains a list of running processes using the function `kill_unwanted`.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [ThiefQuest](https://attack.mitre.org/software/S0595) uses various API functions such as `NSCreateObjectFileImageFromMemory` to load and link in-memory payloads.[^8]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [ThiefQuest](https://attack.mitre.org/software/S0595) uses the `kill_unwanted` function to get a list of running processes, compares each process with an encrypted list of “unwanted” security related programs, and kills the processes for security related programs.[^1]  |
| [[Native API\|T1106]] | Native API | [ThiefQuest](https://attack.mitre.org/software/S0595) uses various API to perform behaviors such as executing payloads and performing local enumeration.[^8]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [ThiefQuest](https://attack.mitre.org/software/S0595) invokes `time` call to check the system's time, executes a `sleep` command, invokes a second `time` call, and then compares the time difference between the two `time` calls and the amount of time the system slept to identify the sandbox.[^1]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [ThiefQuest](https://attack.mitre.org/software/S0595) uses a function named `is_debugging` to perform anti-debugging logic. The function invokes `sysctl` checking the returned value of `P_TRACED`. [ThiefQuest](https://attack.mitre.org/software/S0595) also calls `ptrace` with the `PTRACE_DENY_ATTACH` flag to prevent debugging.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ThiefQuest](https://attack.mitre.org/software/S0595) can download and execute payloads in-memory or from disk.[^8]  |




## References

[^1]: [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)


[^2]: MacRansom.K


[^3]: EvilQuest


[^4]: [Reed thiefquest fake ransom](https://blog.malwarebytes.com/detections/osx-thiefquest/)


[^5]: [reed thiefquest ransomware analysis](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)


[^6]: [Trendmicro Evolving ThiefQuest 2020](https://www.trendmicro.com/en_us/research/20/g/updates-on-quickly-evolving-thiefquest-macos-malware.html)


[^7]: ThiefQuest


[^8]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)


[^9]: [SentinelOne EvilQuest Ransomware Spyware 2020](https://www.sentinelone.com/blog/evilquest-a-new-macos-malware-rolls-ransomware-spyware-and-data-theft-into-one/)


