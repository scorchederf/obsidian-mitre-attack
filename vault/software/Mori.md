---
aliases: 
    - S1047
    
mitre-attack: https://attack.mitre.org/software/S1047
---

## S1047

[Mori](https://attack.mitre.org/software/S1047) is a backdoor that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least January 2022.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Mori](https://attack.mitre.org/software/S1047) can communicate using HTTP over IPv4 or IPv6 depending on a flag set.[^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [Mori](https://attack.mitre.org/software/S1047) has obfuscated the FML.dll with 200MB of junk data.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Mori](https://attack.mitre.org/software/S1047) can use `regsvr32.exe` for DLL execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Mori](https://attack.mitre.org/software/S1047) can resolve networking APIs from strings that are ADD-encrypted.[^1]  |
| [[DNS\|T1071.004]] | DNS | [Mori](https://attack.mitre.org/software/S1047) can use DNS tunneling to communicate with C2.[^1] [^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Mori](https://attack.mitre.org/software/S1047) can read data from the Registry including from `HKLM\Software\NFC\IPA` and<br>`HKLM\Software\NFC\`.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Mori](https://attack.mitre.org/software/S1047) can write data to `HKLM\Software\NFC\IPA` and `HKLM\Software\NFC\` and delete Registry values.[^1] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Mori](https://attack.mitre.org/software/S1047) can delete its DLL file and related files by Registry value.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Mori](https://attack.mitre.org/software/S1047) can use Base64 encoded JSON libraries used in C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^2]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)


