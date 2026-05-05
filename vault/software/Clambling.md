---
aliases: 
    - S0660
    
mitre-attack: https://attack.mitre.org/software/S0660
---

## S0660

[Clambling](https://attack.mitre.org/software/S0660) is a modular backdoor written in C++ that has been used by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2017.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Video Capture\|T1125]] | Video Capture | [Clambling](https://attack.mitre.org/software/S0660) can record screen content in AVI format.[^1] [^4]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Clambling](https://attack.mitre.org/software/S0660) has the ability to use TCP and UDP for communication.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Clambling](https://attack.mitre.org/software/S0660) has the ability to set its file attributes to hidden.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Clambling](https://attack.mitre.org/software/S0660) can use Dropbox to download malicious payloads, send commands, and receive information.[^1] [^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Clambling](https://attack.mitre.org/software/S0660) has the ability to capture screenshots.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Clambling](https://attack.mitre.org/software/S0660) can wait 30 minutes before initiating contact with C2.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Clambling](https://attack.mitre.org/software/S0660) has the ability to enumerate Registry keys, including `KEY_CURRENT_USER\Software\Bitcoin\Bitcoin-Qt\strDataDir` to search for a bitcoin wallet.[^1] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Clambling](https://attack.mitre.org/software/S0660) can browse directories on a compromised host.[^1] [^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Clambling](https://attack.mitre.org/software/S0660) can establish persistence by adding a Registry run key.[^1] [^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Clambling](https://attack.mitre.org/software/S0660) has gained execution through luring victims into opening malicious files.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Clambling](https://attack.mitre.org/software/S0660) can send files from a victim's machine to Dropbox.[^1] [^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | The [Clambling](https://attack.mitre.org/software/S0660) executable has been obfuscated when dropped on a compromised host.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Clambling](https://attack.mitre.org/software/S0660) can create and start services on a compromised host.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Clambling](https://attack.mitre.org/software/S0660) can inject into the `svchost.exe` process for execution.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Clambling](https://attack.mitre.org/software/S0660) has been delivered to victim's machines through malicious e-mail attachments.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Clambling](https://attack.mitre.org/software/S0660) has the ability to capture and store clipboard data.[^1] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Clambling](https://attack.mitre.org/software/S0660) can use cmd.exe for command execution.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Clambling](https://attack.mitre.org/software/S0660) can discover the hostname, computer name, and Windows version of a targeted machine.[^1] [^4]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Clambling](https://attack.mitre.org/software/S0660) has the ability to enumerate network shares.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Clambling](https://attack.mitre.org/software/S0660) has the ability to use Telnet for communication.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Clambling](https://attack.mitre.org/software/S0660) can capture keystrokes on a compromised host.[^1] [^4]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Clambling](https://attack.mitre.org/software/S0660) can execute binaries through process hollowing.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Clambling](https://attack.mitre.org/software/S0660) can deobfuscate its payload prior to execution.[^1] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Clambling](https://attack.mitre.org/software/S0660) can enumerate processes on a targeted system.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Clambling](https://attack.mitre.org/software/S0660) can determine the current time.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Clambling](https://attack.mitre.org/software/S0660) can set and delete Registry keys.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Clambling](https://attack.mitre.org/software/S0660) has the ability to communicate over HTTP.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Clambling](https://attack.mitre.org/software/S0660) has the ability to bypass UAC using a `passuac.dll` file.[^1] [^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Clambling](https://attack.mitre.org/software/S0660) can register itself as a system service to gain persistence.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Clambling](https://attack.mitre.org/software/S0660) can identify the username on a compromised host.[^1] [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | The [Clambling](https://attack.mitre.org/software/S0660) dropper can use PowerShell to download the malware.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Clambling](https://attack.mitre.org/software/S0660) can enumerate the IP address of a compromised machine.[^1] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Clambling](https://attack.mitre.org/software/S0660) can collect information from a compromised host.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Clambling](https://attack.mitre.org/software/S0660) can store a file named `mpsvc.dll`, which opens a malicious `mpsvc.mui` file, in the same folder as the legitimate Microsoft executable `MsMpEng.exe` to gain execution.[^1] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |



## References

[^1]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^2]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^3]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^4]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


