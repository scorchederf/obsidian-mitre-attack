---
aliases: 
    - S0653
    
mitre-attack: https://attack.mitre.org/software/S0653
---

## S0653

[xCaon](https://attack.mitre.org/software/S0653) is an HTTP variant of the [BoxCaon](https://attack.mitre.org/software/S0651) malware family that has used by [IndigoZebra](https://attack.mitre.org/groups/G0136) since at least 2014. [xCaon](https://attack.mitre.org/software/S0653) has been used to target political entities in Central Asia, including Kyrgyzstan and Uzbekistan.[^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [xCaon](https://attack.mitre.org/software/S0653) has uploaded files from victims' machines.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [xCaon](https://attack.mitre.org/software/S0653) has communicated with the C2 server by sending POST requests over HTTP.[^2]   |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [xCaon](https://attack.mitre.org/software/S0653) has added persistence via the Registry key `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load` which causes the malware to run each time any user logs in.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [xCaon](https://attack.mitre.org/software/S0653) has used the GetAdaptersInfo() API call to get the victim's MAC address.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [xCaon](https://attack.mitre.org/software/S0653) has checked for the existence of Kaspersky antivirus software on the system.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [xCaon](https://attack.mitre.org/software/S0653) has encrypted data sent to the C2 server using a XOR key.[^2]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [xCaon](https://attack.mitre.org/software/S0653) has a command to download files to the victim's machine.[^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [xCaon](https://attack.mitre.org/software/S0653) has used Base64 to encode its C2 traffic.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [xCaon](https://attack.mitre.org/software/S0653) has a command to start an interactive shell.[^2]  |
| [[Native API\|T1106]] | Native API | [xCaon](https://attack.mitre.org/software/S0653) has leveraged native OS function calls to retrieve  victim's network adapter's  information using GetAdapterInfo() API.[^2]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [xCaon](https://attack.mitre.org/software/S0653) has decoded strings from the C2 server before executing commands.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[IndigoZebra\|G0136]] | IndigoZebra |



## References

[^1]: xCaon


[^2]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^3]: [Securelist APT Trends Q2 2017](https://securelist.com/apt-trends-report-q2-2017/79332/)


