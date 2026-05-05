---
aliases: 
    - S1046
    
mitre-attack: https://attack.mitre.org/software/S1046
---

## S1046

[PowGoop](https://attack.mitre.org/software/S1046) is a loader that consists of a DLL loader and a PowerShell-based downloader; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) as their main loader.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [PowGoop](https://attack.mitre.org/software/S1046) can receive encrypted commands from C2.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [PowGoop](https://attack.mitre.org/software/S1046) has disguised a PowerShell script as a .dat file (goopdate.dat).[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PowGoop](https://attack.mitre.org/software/S1046) can send HTTP GET requests to malicious servers.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowGoop](https://attack.mitre.org/software/S1046) has the ability to use PowerShell scripts to execute commands.[^1]  |
| [[DLL\|T1574.001]] | DLL | [PowGoop](https://attack.mitre.org/software/S1046) can side-load `Goopdate.dll` into `GoogleUpdate.exe`.[^1] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PowGoop](https://attack.mitre.org/software/S1046) can decrypt PowerShell scripts for execution.[^1] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PowGoop](https://attack.mitre.org/software/S1046) has used a DLL named Goopdate.dll to impersonate a legitimate Google update file.[^1]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [PowGoop](https://attack.mitre.org/software/S1046) can use a modified Base64 encoding mechanism to send data to and from the C2 server.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^2]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)


