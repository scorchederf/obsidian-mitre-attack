---
aliases: 
    - S1196
    
mitre-attack: https://attack.mitre.org/software/S1196
---

## S1196

[Troll Stealer](https://attack.mitre.org/software/S1196) is an information stealer written in Go associated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations. [Troll Stealer](https://attack.mitre.org/software/S1196) has typically been delivered through a dropper disguised as a legitimate security program installation file. [Troll Stealer](https://attack.mitre.org/software/S1196) features code similar to [AppleSeed](https://attack.mitre.org/software/S0622), also uniquely associated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Local System\|T1005]] | Data from Local System | [Troll Stealer](https://attack.mitre.org/software/S1196) gathers information from infected systems such as SSH information from the victim's `.ssh` directory.[^2]  [Troll Stealer](https://attack.mitre.org/software/S1196) collects information from local FileZilla installations and Microsoft Sticky Note.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Troll Stealer](https://attack.mitre.org/software/S1196) encrypts gathered information on victim devices prior to exfiltrating it through command and control infrastructure.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Troll Stealer](https://attack.mitre.org/software/S1196) can capture screenshots from victim machines.[^1] [^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Troll Stealer](https://attack.mitre.org/software/S1196) performs XOR encryption and Base64 encoding of data prior to sending to command and control infrastructure.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Troll Stealer](https://attack.mitre.org/software/S1196) has been delivered as a VMProtect-packed binary.[^1] [^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Troll Stealer](https://attack.mitre.org/software/S1196) collects the MAC address of victim devices.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Troll Stealer](https://attack.mitre.org/software/S1196) uses HTTP to communicate to command and control infrastructure.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Troll Stealer](https://attack.mitre.org/software/S1196) creates and executes a PowerShell script to delete itself.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Troll Stealer](https://attack.mitre.org/software/S1196), along with its associated dropper, utilizes legitimate, stolen code signing certificates.[^1] [^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Troll Stealer](https://attack.mitre.org/software/S1196) can create and execute Windows batch scripts.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Troll Stealer](https://attack.mitre.org/software/S1196) is typically installed via a dropper file that masquerades as a legitimate security program installation file.[^1] [^2]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Troll Stealer](https://attack.mitre.org/software/S1196) collects all data in victim `.ssh` folders by creating a compressed copy that is subsequently exfiltrated to command and control infrastructure. [Troll Stealer](https://attack.mitre.org/software/S1196) also collects key information associated with the Government Public Key Infrastructure (GPKI) service for South Korean government information systems.[^1] [^2]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Troll Stealer](https://attack.mitre.org/software/S1196) compresses stolen data prior to exfiltration.[^1]  |
| [[Data from Information Repositories\|T1213]] | Data from Information Repositories | [Troll Stealer](https://attack.mitre.org/software/S1196) gathers information from the Government Public Key Infrastructure (GPKI) folder, associated with South Korean government public key infrastructure, on infected systems.[^1] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Troll Stealer](https://attack.mitre.org/software/S1196) can enumerate and collect items from local drives and folders.[^1]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Troll Stealer](https://attack.mitre.org/software/S1196) creates a mutex during installation to prevent duplicate execution.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Troll Stealer](https://attack.mitre.org/software/S1196) can collect local system information.[^1] [^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Troll Stealer](https://attack.mitre.org/software/S1196) is dropped as a DLL file and executed via `rundll32.exe` by its installer.[^1] [^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Troll Stealer](https://attack.mitre.org/software/S1196) exfiltrates collected information to its command and control infrastructure.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Troll Stealer](https://attack.mitre.org/software/S1196) collects information from Chromium-based browsers and Firefox such as cookies, history, downloads, and extensions.[^1] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Troll Stealer](https://attack.mitre.org/software/S1196) encrypts data sent to command and control infrastructure using a combination of RC4 and RSA-4096 algorithms.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Troll Stealer](https://attack.mitre.org/software/S1196) creates and can execute a BAT script that will delete the malware.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^2]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^3]: [ASEC Troll Stealer 2024](https://asec.ahnlab.com/en/61934/)


