---
aliases: 
    - S0526
    
mitre-attack: https://attack.mitre.org/software/S0526
---

## S0526

[KGH_SPY](https://attack.mitre.org/software/S0526) is a modular suite of tools used by [Kimsuky](https://attack.mitre.org/groups/G0094) for reconnaissance, information stealing, and backdoor capabilities. [KGH_SPY](https://attack.mitre.org/software/S0526) derived its name from PDB paths and internal names found in samples containing "KGH".[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [KGH_SPY](https://attack.mitre.org/software/S0526) has masqueraded as a legitimate Windows tool.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to steal data from the Chrome, Edge, Firefox, Thunderbird, and Opera browsers.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to set a Registry key to run a cmd.exe command.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [KGH_SPY](https://attack.mitre.org/software/S0526) has been spread through Word documents containing malicious macros.[^1]  |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to set the `HKCU\Environment\UserInitMprLogonScript` Registry key to execute logon scripts.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to download and execute code from remote servers.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [KGH_SPY](https://attack.mitre.org/software/S0526) can send data to C2 with HTTP POST requests.[^1]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [KGH_SPY](https://attack.mitre.org/software/S0526) can harvest data from mail clients.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [KGH_SPY](https://attack.mitre.org/software/S0526) can enumerate files and directories on a compromised host.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [KGH_SPY](https://attack.mitre.org/software/S0526) can exfiltrate collected information from the host to the C2 server.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [KGH_SPY](https://attack.mitre.org/software/S0526) has used encrypted strings in its installer.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [KGH_SPY](https://attack.mitre.org/software/S0526) can execute PowerShell commands on the victim's machine.[^1]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [KGH_SPY](https://attack.mitre.org/software/S0526) can collect credentials from the Windows Credential Manager.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [KGH_SPY](https://attack.mitre.org/software/S0526) can save collected system information to a file named "info" before exfiltration.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [KGH_SPY](https://attack.mitre.org/software/S0526) can collect information on installed applications.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [KGH_SPY](https://attack.mitre.org/software/S0526) can collect drive information from a compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [KGH_SPY](https://attack.mitre.org/software/S0526) can send a file containing victim system information to C2.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [KGH_SPY](https://attack.mitre.org/software/S0526) can perform keylogging by polling the `GetAsyncKeyState()` function.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [KGH_SPY](https://attack.mitre.org/software/S0526) can decrypt encrypted strings and write them to a newly created folder.[^1]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [KGH_SPY](https://attack.mitre.org/software/S0526) can collect credentials from WINSCP.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


