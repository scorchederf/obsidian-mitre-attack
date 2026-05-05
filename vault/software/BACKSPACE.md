---
aliases: 
    - S0031
    
mitre-attack: https://attack.mitre.org/software/S0031
---

## S0031

[BACKSPACE](https://attack.mitre.org/software/S0031) is a backdoor used by [APT30](https://attack.mitre.org/groups/G0013) that dates back to at least 2005. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | During its initial execution, [BACKSPACE](https://attack.mitre.org/software/S0031) extracts operating system information from the infected host.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BACKSPACE](https://attack.mitre.org/software/S0031) is capable of deleting Registry keys, sub-keys, and values on a victim system.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | Adversaries can direct [BACKSPACE](https://attack.mitre.org/software/S0031) to execute from the command line on infected hosts, or have [BACKSPACE](https://attack.mitre.org/software/S0031) create a reverse shell.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [BACKSPACE](https://attack.mitre.org/software/S0031) is capable of enumerating and making modifications to an infected system's Registry.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BACKSPACE](https://attack.mitre.org/software/S0031) uses HTTP as a transport to communicate with its command server.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BACKSPACE](https://attack.mitre.org/software/S0031) may collect information about running processes.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | Newer variants of [BACKSPACE](https://attack.mitre.org/software/S0031) will encode C2 communications with a custom system.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | The "ZJ" variant of [BACKSPACE](https://attack.mitre.org/software/S0031) allows "ZJ link" infections with Internet access to relay traffic from "ZJ listen" to a command server.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BACKSPACE](https://attack.mitre.org/software/S0031) achieves persistence by creating a shortcut to itself in the CSIDL_STARTUP directory.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | Adversaries can direct [BACKSPACE](https://attack.mitre.org/software/S0031) to upload files to the C2 Server.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BACKSPACE](https://attack.mitre.org/software/S0031) allows adversaries to search for files.[^1]  |
| [[Multi-Stage Channels\|T1104]] | Multi-Stage Channels | [BACKSPACE](https://attack.mitre.org/software/S0031) attempts to avoid detection by checking a first stage command and control server to determine if it should connect to the second stage server, which performs "louder" interactions with the malware.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [BACKSPACE](https://attack.mitre.org/software/S0031) achieves persistence by creating a shortcut to itself in the CSIDL_STARTUP directory.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | The "ZR" variant of [BACKSPACE](https://attack.mitre.org/software/S0031) will check to see if known host-based firewalls are installed on the infected systems. [BACKSPACE](https://attack.mitre.org/software/S0031) will attempt to establish a C2 channel, then will examine open windows to identify a pop-up from the firewall software and will simulate a mouse-click to allow the connection to proceed.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT30\|G0013]] | APT30 |



## References

[^1]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


