---
aliases: 
    - S0686
    
mitre-attack: https://attack.mitre.org/software/S0686
---

## S0686

[QuietSieve](https://attack.mitre.org/software/S0686) is an information stealer that has been used by [Gamaredon Group](https://attack.mitre.org/groups/G0047) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hidden Window\|T1564.003]] | Hidden Window | [QuietSieve](https://attack.mitre.org/software/S0686) has the ability to execute payloads in a hidden window.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [QuietSieve](https://attack.mitre.org/software/S0686) can use HTTPS in C2 communications.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [QuietSieve](https://attack.mitre.org/software/S0686) can download and execute payloads on a target host.[^1]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [QuietSieve](https://attack.mitre.org/software/S0686) can check C2 connectivity with a `ping` to 8.8.8.8 (Google public DNS).[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [QuietSieve](https://attack.mitre.org/software/S0686) can search files on the target host by extension, including doc, docx, xls, rtf, odt, txt, jpg, pdf, rar, zip, and 7z.[^1]   |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [QuietSieve](https://attack.mitre.org/software/S0686) can identify and search removable drives for specific file name extensions.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [QuietSieve](https://attack.mitre.org/software/S0686) can collect files from a compromised host.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [QuietSieve](https://attack.mitre.org/software/S0686) can identify and search networked drives for specific file name extensions.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [QuietSieve](https://attack.mitre.org/software/S0686) has taken screenshots every five minutes and saved them to the user's local Application Data folder under `Temp\SymbolSourceSymbols\icons` or `Temp\ModeAuto\icons`.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Gamaredon Group\|G0047]] | Gamaredon Group |



## References

[^1]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


