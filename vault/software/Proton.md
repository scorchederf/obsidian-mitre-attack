---
aliases: 
    - S0279
    
mitre-attack: https://attack.mitre.org/software/S0279
---

## S0279

[Proton](https://attack.mitre.org/software/S0279) is a macOS backdoor focusing on data theft and credential access  [^2] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Proton](https://attack.mitre.org/software/S0279) prompts users for their credentials.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Proton](https://attack.mitre.org/software/S0279) persists via Launch Agent.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Proton](https://attack.mitre.org/software/S0279) removes all files in the /tmp directory.[^2]  |
| [[VNC\|T1021.005]] | VNC | [Proton](https://attack.mitre.org/software/S0279) uses VNC to connect into systems.[^2]  |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | [Proton](https://attack.mitre.org/software/S0279) modifies the tty_tickets line in the sudoers file.[^2]  |
| [[Keychain\|T1555.001]] | Keychain | [Proton](https://attack.mitre.org/software/S0279) gathers credentials in files for keychains.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Proton](https://attack.mitre.org/software/S0279) kills security tools like Wireshark that are running.[^2]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [Proton](https://attack.mitre.org/software/S0279) removes logs from `/var/logs` and `/Library/logs`.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Proton](https://attack.mitre.org/software/S0279) uses an encrypted file to store commands and configuration values.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Proton](https://attack.mitre.org/software/S0279) gathers credentials for Google Chrome.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Proton](https://attack.mitre.org/software/S0279) uses a keylogger to capture keystrokes.[^2]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Proton](https://attack.mitre.org/software/S0279) gathers credentials in files for 1password.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Proton](https://attack.mitre.org/software/S0279) captures the content of the desktop with the screencapture binary.[^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Proton](https://attack.mitre.org/software/S0279) zips up files before exfiltrating them.[^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Proton](https://attack.mitre.org/software/S0279) uses macOS' .command file type to script actions.[^2]  |




## References

[^1]: Proton


[^2]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


