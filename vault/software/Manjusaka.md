---
aliases: 
    - S1156
    
mitre-attack: https://attack.mitre.org/software/S1156
---

## S1156

[Manjusaka](https://attack.mitre.org/software/S1156) is a Chinese-language intrusion framework, similar to [Sliver](https://attack.mitre.org/software/S0633) and [Cobalt Strike](https://attack.mitre.org/software/S0154), with an ELF binary written in GoLang as the controller for Windows and Linux implants written in Rust. First identified in 2022, [Manjusaka](https://attack.mitre.org/software/S1156) consists of multiple components, only one of which (a command and control module) is freely available.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Manjusaka](https://attack.mitre.org/software/S1156) performs basic system profiling actions to fingerprint and register the victim system with the C2 controller.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Manjusaka](https://attack.mitre.org/software/S1156) extracts credentials from the Windows Registry associated with Premiumsoft Navicat, a utility used to facilitate access to various database types.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Manjusaka](https://attack.mitre.org/software/S1156) gathers information about current network connections, local and remote addresses associated with them, and associated processes.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Manjusaka](https://attack.mitre.org/software/S1156) gathers credentials from Chromium-based browsers.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Manjusaka](https://attack.mitre.org/software/S1156) data exfiltration takes place over HTTP channels.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Manjusaka](https://attack.mitre.org/software/S1156) can execute arbitrary commands passed to it from the C2 controller via `cmd.exe /c`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Manjusaka](https://attack.mitre.org/software/S1156) can gather information about specific files on the victim system.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Manjusaka](https://attack.mitre.org/software/S1156) can take screenshots of the victim desktop.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Manjusaka](https://attack.mitre.org/software/S1156) communication includes a client-created session cookie with base64-encoded information representing information from the victim system.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Manjusaka](https://attack.mitre.org/software/S1156) has used HTTP for command and control communication.[^1]  |




## References

[^1]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


