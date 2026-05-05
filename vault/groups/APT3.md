---
aliases: 
    - APT3
    - Gothic Panda
    - Pirpi
    - UPS Team
    - Buckeye
    - Threat Group-0110
    - TG-0110
mitre-attack: https://attack.mitre.org/groups/G0022
---

## G0022

[APT3](https://attack.mitre.org/groups/G0022) is a China-based threat group that researchers have attributed to China's Ministry of State Security.[^3] [^16]  This group is responsible for the campaigns known as Operation Clandestine Fox, Operation Clandestine Wolf, and Operation Double Tap.[^3] [^17]  As of June 2015, the group appears to have shifted from targeting primarily US victims to primarily political organizations in Hong Kong.[^18] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | An [APT3](https://attack.mitre.org/groups/G0022) downloader creates persistence by creating the following scheduled task: `schtasks /create /tn "mysc" /tr C:\Users\Public\test.exe /sc ONLOGON /ru "System"`.[^17]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | An [APT3](https://attack.mitre.org/groups/G0022) downloader first establishes a SOCKS5 connection to 192.157.198[.]103 using TCP port 1913; once the server response is verified, it then requests a connection to 192.184.60[.]229 on TCP port 81.[^17]  |
| [[Password Cracking\|T1110.002]] | Password Cracking | [APT3](https://attack.mitre.org/groups/G0022) has been known to brute force password hashes to be able to leverage plain text credentials.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [APT3](https://attack.mitre.org/groups/G0022) has been known to use `-WindowStyle Hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows.[^17]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [APT3](https://attack.mitre.org/groups/G0022) has used tools to dump passwords from browsers.[^18]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command `"cmd.exe" /C whoami`. The group also uses a tool to execute commands on remote computers.[^17] [^18]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | A keylogging tool used by [APT3](https://attack.mitre.org/groups/G0022) gathers network information from the victim, including the MAC address, IP address, WINS, DHCP server, and gateway.[^18] [^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can enumerate current network connections.[^18] [^10] [^2]  |
| [[External Proxy\|T1090.002]] | External Proxy | An [APT3](https://attack.mitre.org/groups/G0022) downloader establishes SOCKS5 connections for its initial C2.[^17]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can run DLLs.[^10]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [APT3](https://attack.mitre.org/groups/G0022) obfuscates files or information to help evade defensive measures.[^18]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT3](https://attack.mitre.org/groups/G0022) has sent spearphishing emails containing malicious links.[^3]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [APT3](https://attack.mitre.org/groups/G0022) has been known to add created accounts to local admin groups to maintain elevated access.[^9]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT3](https://attack.mitre.org/groups/G0022) has lured victims into clicking malicious links delivered through spearphishing.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [APT3](https://attack.mitre.org/groups/G0022) has a tool that exfiltrates data over the C2 channel.[^10]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can locate credentials in files on the file system such as those from Firefox or Chrome.[^18]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [APT3](https://attack.mitre.org/groups/G0022) has been known to stage files for exfiltration in a single location.[^9]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [APT3](https://attack.mitre.org/groups/G0022) leverages valid accounts after gaining credentials for use within the victim domain.[^18]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT3](https://attack.mitre.org/groups/G0022) will identify Microsoft Office documents on the victim's computer.[^9]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT3](https://attack.mitre.org/groups/G0022) has exploited the Adobe Flash Player vulnerability CVE-2015-3113 and Internet Explorer vulnerability CVE-2014-1776.[^3] [^10]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [APT3](https://attack.mitre.org/groups/G0022) will copy files over to Windows Admin Shares (like ADMIN$) as part of lateral movement.[^18]  |
| [[DLL\|T1574.001]] | DLL | [APT3](https://attack.mitre.org/groups/G0022) has been known to side load DLLs with a valid version of Chrome with one of their tools.[^10] [^6]  |
| [[Local Account\|T1087.001]] | Local Account | [APT3](https://attack.mitre.org/groups/G0022) has used a tool that can obtain info about local and global group users, power users, and administrators.[^18]  |
| [[File Deletion\|T1070.004]] | File Deletion | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can delete files.[^10]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that looks for files and directories on the local file system.[^10] [^2]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [APT3](https://attack.mitre.org/groups/G0022) replaces the Sticky Keys binary `C:\Windows\System32\sethc.exe` for persistence.[^9]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [APT3](https://attack.mitre.org/groups/G0022) has used tools to compress data before exfilling it.[^9]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can obtain information about the local system.[^18] [^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT3](https://attack.mitre.org/groups/G0022) has used PowerShell on victim systems to download and run payloads after exploitation.[^17]  |
| [[Windows Service\|T1543.003]] | Windows Service | [APT3](https://attack.mitre.org/groups/G0022) has a tool that creates a new service for persistence.[^17]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [APT3](https://attack.mitre.org/groups/G0022) has used a tool to dump credentials by injecting itself into lsass.exe and triggering with the argument "dig."[^18]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT3](https://attack.mitre.org/groups/G0022) places scripts in the startup folder for persistence.[^17]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [APT3](https://attack.mitre.org/groups/G0022) enables the Remote Desktop Protocol for persistence.[^9]  [APT3](https://attack.mitre.org/groups/G0022) has also interacted with compromised systems to browse and copy files through RDP sessions.[^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can list out currently running processes.[^10] [^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | An [APT3](https://attack.mitre.org/groups/G0022) downloader establishes SOCKS5 connections for its initial C2.[^17]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can enumerate the permissions associated with Windows groups.[^18]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can detect the existence of remote systems.[^18] [^10]  |
| [[Keylogging\|T1056.001]] | Keylogging | [APT3](https://attack.mitre.org/groups/G0022) has used a keylogging tool that records keystrokes in encrypted files.[^18]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [APT3](https://attack.mitre.org/groups/G0022) has been known to create or enable accounts, such as `support_388945a0`.[^9]  |
| [[Software Packing\|T1027.002]] | Software Packing | [APT3](https://attack.mitre.org/groups/G0022) has been known to pack their tools.[^1] [^3]   |
| [[Local Account\|T1136.001]] | Local Account | [APT3](https://attack.mitre.org/groups/G0022) has been known to create or enable accounts, such as `support_388945a0`.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can copy files to remote machines.[^10]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command `"cmd.exe" /C whoami` to verify that it is running with the elevated privileges of “System.”[^17]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [APT3](https://attack.mitre.org/groups/G0022) has been known to remove indicators of compromise from tools.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[LaZagne\|S0349]] | LaZagne | [^18]  |
| [[schtasks\|S0111]] | schtasks | [^17]  |
| [[RemoteCMD\|S0166]] | RemoteCMD | [^18]  |
| [[SHOTPUT\|S0063]] | SHOTPUT | [^3]  |
| [[PlugX\|S0013]] | PlugX | [^6]  |
| [[OSInfo\|S0165]] | OSInfo | [^18]  |



## References

[^1]: [APT3 Adversary Emulation Plan](https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf)


[^2]: [evolution of pirpi](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)


[^3]: [FireEye Clandestine Wolf](https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html)


[^4]: Threat Group-0110


[^5]: Pirpi


[^6]: [FireEye Clandestine Fox Part 2](https://www.fireeye.com/blog/threat-research/2014/06/clandestine-fox-part-deux.html)


[^7]: [Twitter Cglyer Status Update APT3 eml](https://x.com/cglyer/status/985311489782374400)


[^8]: Gothic Panda


[^9]: [aptsim](http://carnal0wnage.attackresearch.com/2012/09/more-on-aptsim.html)


[^10]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^11]: TG-0110


[^12]: Buckeye


[^13]: APT3


[^14]: [PWC Pirpi Scanbox](http://pwc.blogs.com/cyber_security_updates/2015/07/pirpi-scanbox.html)


[^15]: UPS Team


[^16]: [Recorded Future APT3 May 2017](https://www.recordedfuture.com/research/chinese-mss-behind-apt3)


[^17]: [FireEye Operation Double Tap](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)


[^18]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


