---
aliases: 
    - S0274
    
mitre-attack: https://attack.mitre.org/software/S0274
---

## S0274

[Calisto](https://attack.mitre.org/software/S0274) is a macOS Trojan that opens a backdoor on the compromised machine. [Calisto](https://attack.mitre.org/software/S0274) is believed to have first been developed in 2016. [^3]  [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Calisto](https://attack.mitre.org/software/S0274) adds a .plist file to the /Library/LaunchAgents folder to maintain persistence.[^3]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Calisto](https://attack.mitre.org/software/S0274) collects information on bookmarks from Google Chrome.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Calisto](https://attack.mitre.org/software/S0274) runs the `ifconfig` command to obtain the IP address from the victim’s machine.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Calisto](https://attack.mitre.org/software/S0274) has the capability to upload and download files to the victim's machine.[^2]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Calisto](https://attack.mitre.org/software/S0274) presents an input prompt asking for the user's login and password.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Calisto](https://attack.mitre.org/software/S0274) can collect data from user directories.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Calisto](https://attack.mitre.org/software/S0274) has the capability to use `rm -rf` to remove folders and files from the victim's machine.[^3]  |
| [[Launchctl\|T1569.001]] | Launchctl | [Calisto](https://attack.mitre.org/software/S0274) uses launchctl to enable screen sharing on the victim’s machine.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Calisto](https://attack.mitre.org/software/S0274) uses the `zip -r` command to compress the data collected on the local system.[^3] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Calisto](https://attack.mitre.org/software/S0274)'s installation file is an unsigned DMG image under the guise of Intego’s security solution for mac.[^3]  |
| [[Keychain\|T1555.001]] | Keychain | [Calisto](https://attack.mitre.org/software/S0274) collects Keychain storage data and copies those passwords/tokens to a file.[^3] [^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Calisto](https://attack.mitre.org/software/S0274) uses a hidden directory named .calisto to store data from the victim’s machine before exfiltration.[^3] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Calisto](https://attack.mitre.org/software/S0274) uses a hidden directory named .calisto to store data from the victim’s machine before exfiltration.[^3] [^2]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | [Calisto](https://attack.mitre.org/software/S0274) adds permissions and remote logins to all users.[^2]  |
| [[Local Account\|T1136.001]] | Local Account | [Calisto](https://attack.mitre.org/software/S0274) has the capability to add its own account to the victim's machine.[^2]  |




## References

[^1]: Calisto


[^2]: [Symantec Calisto July 2018](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)


[^3]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)


