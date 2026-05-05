---
aliases: 
    - S0531
    
mitre-attack: https://attack.mitre.org/software/S0531
---

## S0531

[Grandoreiro](https://attack.mitre.org/software/S0531) is a banking trojan written in Delphi that was first observed in 2016 and uses a Malware-as-a-Service (MaaS) business model. [Grandoreiro](https://attack.mitre.org/software/S0531) has confirmed victims in Brazil, Mexico, Portugal, and Spain.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Grandoreiro](https://attack.mitre.org/software/S0531) can use VBScript to execute malicious code.[^3] [^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Grandoreiro](https://attack.mitre.org/software/S0531) has used malicious links to gain execution on victim machines.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can identify installed security tools based on process names.[^2]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Grandoreiro](https://attack.mitre.org/software/S0531) can write or modify browser shortcuts to enable launching of malicious browser extensions.[^1]   |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Grandoreiro](https://attack.mitre.org/software/S0531) can steal the victim's cookies to use for duplicating the active session from another device.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Grandoreiro](https://attack.mitre.org/software/S0531) can download its second stage from a hardcoded URL within the loader's code.[^1] [^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Grandoreiro](https://attack.mitre.org/software/S0531) can use SSL in C2 communication.[^1]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Grandoreiro](https://attack.mitre.org/software/S0531) can obtain C2 information from Google Docs.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Grandoreiro](https://attack.mitre.org/software/S0531) has named malicious browser extensions and update files to appear legitimate.[^1] [^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Grandoreiro](https://attack.mitre.org/software/S0531) can modify the Registry to store its configuration at `HKCU\Software\` under frequently changing names including `%USERNAME%` and `ToolTech-RM`.[^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Grandoreiro](https://attack.mitre.org/software/S0531) can utilize web services including Google sites to send and receive C2 data.[^1] [^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Grandoreiro](https://attack.mitre.org/software/S0531) can send data it retrieves to the C2 server.[^2]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [Grandoreiro](https://attack.mitre.org/software/S0531) can modify the binary ACL to prevent security tools from running.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [Grandoreiro](https://attack.mitre.org/software/S0531) payload has been delivered encrypted with a custom XOR-based algorithm and also as a base64-encoded ZIP file.[^3] [^2] [^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can determine the time on the victim machine via IPinfo.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Grandoreiro](https://attack.mitre.org/software/S0531) can use run keys and create link files in the startup folder for persistence.[^1] [^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Grandoreiro](https://attack.mitre.org/software/S0531) has infected victims via malicious attachments.[^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can collect the username from the victim's machine.[^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can identify installed security tools based on window names.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [Grandoreiro](https://attack.mitre.org/software/S0531) can store its configuration in the Registry at `HKCU\Software\` under frequently changing names including `%USERNAME%` and `ToolTech-RM`.[^2]  |
| [[Email Account\|T1087.003]] | Email Account | [Grandoreiro](https://attack.mitre.org/software/S0531) can parse Outlook .pst files to extract e-mail addresses.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can collect the computer name and OS version from a compromised host.[^2]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Grandoreiro](https://attack.mitre.org/software/S0531) has added BMP images to the resources section of its Portable Executable (PE) file increasing each binary to at least 300MB in size.[^2]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Grandoreiro](https://attack.mitre.org/software/S0531) can use MSI files to execute DLLs.[^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can list installed security products including the Trusteer and Diebold Warsaw GAS Tecnologia online banking protections.[^2] [^2]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Grandoreiro](https://attack.mitre.org/software/S0531) can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields.[^3] [^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Grandoreiro](https://attack.mitre.org/software/S0531) can log keystrokes on the victim's machine.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Grandoreiro](https://attack.mitre.org/software/S0531) can delete .LNK files created in the Startup folder.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [Grandoreiro](https://attack.mitre.org/software/S0531) can detect VMWare via its I/O port and Virtual PC via the `vpcext` instruction.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Grandoreiro](https://attack.mitre.org/software/S0531) can hook APIs, kill processes, break file system paths, and change ACLs to prevent security tools from running.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Grandoreiro](https://attack.mitre.org/software/S0531) can capture clipboard data from a compromised host.[^1]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [Grandoreiro](https://attack.mitre.org/software/S0531) can use malicious browser extensions to steal cookies and other user information.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Grandoreiro](https://attack.mitre.org/software/S0531) can decrypt its encrypted internal strings.[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Grandoreiro](https://attack.mitre.org/software/S0531) has used compromised websites and Google Ads to bait victims into downloading its installer.[^3] [^1]  |
| [[Network Device Firewall\|T1686.002]] | Network Device Firewall | [Grandoreiro](https://attack.mitre.org/software/S0531) can block the Deibold Warsaw GAS Tecnologia security tool at the firewall level. [^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Grandoreiro](https://attack.mitre.org/software/S0531) can bypass UAC by registering as the default handler for .MSC files.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Grandoreiro](https://attack.mitre.org/software/S0531) can determine the IP and physical location of the compromised host via IPinfo.[^2]  |
| [[Native API\|T1106]] | Native API | [Grandoreiro](https://attack.mitre.org/software/S0531) can execute through the `WinExec` API.[^2]  |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Grandoreiro](https://attack.mitre.org/software/S0531) can use a DGA for hiding C2 addresses, including use of an algorithm with a user-specific key that changes daily.[^3] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Grandoreiro](https://attack.mitre.org/software/S0531) has the ability to use HTTP in C2 communications.[^1] [^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Grandoreiro](https://attack.mitre.org/software/S0531) has been spread via malicious links embedded in e-mails.[^1] [^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Grandoreiro](https://attack.mitre.org/software/S0531) can steal cookie data and credentials from Google Chrome.[^1] [^2]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Grandoreiro](https://attack.mitre.org/software/S0531) can block the Deibold Warsaw GAS Tecnologia security tool at the firewall level.[^2]  |




## References

[^1]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)


[^2]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^3]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


