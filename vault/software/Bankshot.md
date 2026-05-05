---
aliases: 
    - S0239
    
mitre-attack: https://attack.mitre.org/software/S0239
---

## S0239

[Bankshot](https://attack.mitre.org/software/S0239) is a remote access tool (RAT) that was first reported by the Department of Homeland Security in December of 2017. In 2018, [Lazarus Group](https://attack.mitre.org/groups/G0032) used the [Bankshot](https://attack.mitre.org/software/S0239) implant in attacks against the Turkish financial sector. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Bankshot](https://attack.mitre.org/software/S0239) uses HTTP for command and control communication.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Bankshot](https://attack.mitre.org/software/S0239) collects files from the local system.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Bankshot](https://attack.mitre.org/software/S0239) marks files to be deleted upon the next system reboot and uninstalls and removes itself from the system.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Bankshot](https://attack.mitre.org/software/S0239) searches for files on the victim's machine.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Bankshot](https://attack.mitre.org/software/S0239) modifies the time of a file as specified by the control server.[^3]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Bankshot](https://attack.mitre.org/software/S0239) leverages a known zero-day vulnerability in Adobe Flash to execute the implant into the victims’ machines.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Bankshot](https://attack.mitre.org/software/S0239) identifies processes and collects the process ids.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bankshot](https://attack.mitre.org/software/S0239) decodes embedded XOR strings.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bankshot](https://attack.mitre.org/software/S0239) gathers system information, network addresses, and the operation system version.[^3] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Bankshot](https://attack.mitre.org/software/S0239) can terminate a specific process by its process id.[^3] [^1]  |
| [[Native API\|T1106]] | Native API | [Bankshot](https://attack.mitre.org/software/S0239) creates processes using the Windows API calls: CreateProcessA() and CreateProcessAsUserA().[^3]  |
| [[Query Registry\|T1012]] | Query Registry | [Bankshot](https://attack.mitre.org/software/S0239) searches for certain Registry keys to be configured before executing the payload.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Bankshot](https://attack.mitre.org/software/S0239) encodes commands from the control server using a range of characters and gzip.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Bankshot](https://attack.mitre.org/software/S0239) recursively generates a list of files within a directory and sends them back to the control server.[^3]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Bankshot](https://attack.mitre.org/software/S0239) generates a false TLS handshake using a public certificate to disguise C2 network communications.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bankshot](https://attack.mitre.org/software/S0239) uploads files and secondary payloads to the victim's machine.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [Bankshot](https://attack.mitre.org/software/S0239) gathers domain and account names/information through process monitoring.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Bankshot](https://attack.mitre.org/software/S0239) gathers domain and account names/information through process monitoring.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Bankshot](https://attack.mitre.org/software/S0239) writes data into the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Pniumj`.[^1]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Bankshot](https://attack.mitre.org/software/S0239) grabs a user token using WTSQueryUserToken and then creates a process by impersonating a logged-on user.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Bankshot](https://attack.mitre.org/software/S0239) uses the command-line interface to execute arbitrary commands.[^3] [^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Bankshot](https://attack.mitre.org/software/S0239) exfiltrates data over its C2 channel.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Bankshot](https://attack.mitre.org/software/S0239) gathers disk type and disk free space.[^3] [^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [Bankshot](https://attack.mitre.org/software/S0239) deletes all artifacts associated with the malware from the infected machine.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Bankshot](https://attack.mitre.org/software/S0239) binds and listens on port 1058 for HTTP traffic while also utilizing a FakeTLS method.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^2]: Bankshot


[^3]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^4]: [MAR10135536-B](https://web.archive.org/web/20220529212912/https://www.cisa.gov/uscert/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^5]: Trojan Manuscript


