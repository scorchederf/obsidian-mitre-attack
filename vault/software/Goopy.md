---
aliases: 
    - S0477
    
mitre-attack: https://attack.mitre.org/software/S0477
---

## S0477

[Goopy](https://attack.mitre.org/software/S0477) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050) and shares several similarities to another backdoor used by the group ([Denis](https://attack.mitre.org/software/S0354)). [Goopy](https://attack.mitre.org/software/S0477) is named for its impersonation of the legitimate Google Updater executable.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | [Goopy](https://attack.mitre.org/software/S0477) has the ability to communicate with its C2 over DNS.[^1] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Goopy](https://attack.mitre.org/software/S0477) has the ability to use a Microsoft Outlook backdoor macro to communicate with its C2.[^1] 	 |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Goopy](https://attack.mitre.org/software/S0477)'s decrypter have been inflated with junk code in between legitimate API functions, and also included infinite loops to avoid analysis.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Goopy](https://attack.mitre.org/software/S0477) has the ability to disable Microsoft Outlook's security policies to disable macro warnings.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Goopy](https://attack.mitre.org/software/S0477) has the ability to use cmd.exe to execute commands passed from an Outlook C2 channel.[^1] 	 |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Goopy](https://attack.mitre.org/software/S0477) has the ability to enumerate the infected system's user name.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Goopy](https://attack.mitre.org/software/S0477) has the ability to communicate with its C2 over HTTP.[^1] 	 |
| [[Process Discovery\|T1057]] | Process Discovery | [Goopy](https://attack.mitre.org/software/S0477) has checked for the Google Updater process to ensure [Goopy](https://attack.mitre.org/software/S0477) was loaded properly.[^1]  |
| [[Clear Mailbox Data\|T1070.008]] | Clear Mailbox Data | [Goopy](https://attack.mitre.org/software/S0477) has the ability to delete emails used for C2 once the content has been copied.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Goopy](https://attack.mitre.org/software/S0477) has the ability to exfiltrate documents from infected systems.[^1] 	 |
| [[Native API\|T1106]] | Native API | [Goopy](https://attack.mitre.org/software/S0477) has the ability to  enumerate the infected system's user name via `GetUserNameW`.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Goopy](https://attack.mitre.org/software/S0477) has the ability to use a Microsoft Outlook backdoor macro to communicate with its C2.[^1] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Goopy](https://attack.mitre.org/software/S0477) has used a polymorphic decryptor to decrypt itself at runtime.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Goopy](https://attack.mitre.org/software/S0477) has the ability to side-load malicious DLLs with legitimate applications from Kaspersky, Microsoft, and Google.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Goopy](https://attack.mitre.org/software/S0477) has the ability to exfiltrate data over the Microsoft Outlook C2 channel.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Goopy](https://attack.mitre.org/software/S0477) has impersonated the legitimate goopdate.dll, which was dropped on the target system with a legitimate GoogleUpdate.exe.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Goopy](https://attack.mitre.org/software/S0477) has the ability to maintain persistence by creating scheduled tasks set to run every hour.[^1] 	 |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Goopy](https://attack.mitre.org/software/S0477) has had null characters padded in its malicious DLL payload.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


