---
aliases: 
    - S1050
    
mitre-attack: https://attack.mitre.org/software/S1050
---

## S1050

[PcShare](https://attack.mitre.org/software/S1050) is an open source remote access tool that has been modified and used by Chinese threat actors, most notably during the FunnyDream campaign since late 2018.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PcShare](https://attack.mitre.org/software/S1050) has been named `wuauclt.exe` to appear as the legitimate Windows Update AutoUpdate Client.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PcShare](https://attack.mitre.org/software/S1050) has used HTTP for C2 communication.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PcShare](https://attack.mitre.org/software/S1050) can obtain a list of running processes on a compromised host.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [PcShare](https://attack.mitre.org/software/S1050) can take screen shots of a compromised machine.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PcShare](https://attack.mitre.org/software/S1050) can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.[^2]  |
| [[Compression\|T1027.015]] | Compression | [PcShare](https://attack.mitre.org/software/S1050) has been compressed with LZW algorithm.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PcShare](https://attack.mitre.org/software/S1050) can execute `cmd` commands on a compromised host.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PcShare](https://attack.mitre.org/software/S1050) has been encrypted with XOR using different 32-long Base16 strings.[^2]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [PcShare](https://attack.mitre.org/software/S1050) has created the `HKCU\\Software\\Classes\\CLSID\\{42aedc87-2188-41fd-b9a3-0c966feabec1}\\InprocServer32` Registry key for persistence.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PcShare](https://attack.mitre.org/software/S1050) has the ability to capture keystrokes.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PcShare](https://attack.mitre.org/software/S1050) can collect files and information from a compromised host.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [PcShare](https://attack.mitre.org/software/S1050) has used `rundll32.exe` for execution.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PcShare](https://attack.mitre.org/software/S1050) has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [PcShare](https://attack.mitre.org/software/S1050) can search the registry files of a compromised host.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PcShare](https://attack.mitre.org/software/S1050) has deleted its files and components from a compromised host.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PcShare](https://attack.mitre.org/software/S1050) can upload files and information from a compromised host to its C2 servers.[^2]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [PcShare](https://attack.mitre.org/software/S1050) has used an invalid certificate in attempt to appear legitimate.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PcShare](https://attack.mitre.org/software/S1050) can delete its persistence mechanisms from the registry.[^2]  |
| [[Native API\|T1106]] | Native API | [PcShare](https://attack.mitre.org/software/S1050) has used a variety of Windows API functions.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | The [PcShare](https://attack.mitre.org/software/S1050) payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.[^2]  |
| [[Video Capture\|T1125]] | Video Capture | [PcShare](https://attack.mitre.org/software/S1050) can capture camera video as part of its collection process.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [GitHub PcShare 2014](https://github.com/LiveMirror/pcshare)


[^2]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^3]: [Secureworks BRONZE FLEETWOOD Profile](https://www.secureworks.com/research/threat-profiles/bronze-fleetwood)


