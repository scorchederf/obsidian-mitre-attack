---
aliases: 
    - S0518
    
mitre-attack: https://attack.mitre.org/software/S0518
---

## S0518

[PolyglotDuke](https://attack.mitre.org/software/S0518) is a downloader that has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least 2013. [PolyglotDuke](https://attack.mitre.org/software/S0518) has been used to drop [MiniDuke](https://attack.mitre.org/software/S0051).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [PolyglotDuke](https://attack.mitre.org/software/S0518) can write encrypted JSON configuration files to the Registry.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PolyglotDuke](https://attack.mitre.org/software/S0518) can custom encrypt strings.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [PolyglotDuke](https://attack.mitre.org/software/S0518) can store encrypted JSON configuration files in the Registry.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PolyglotDuke](https://attack.mitre.org/software/S0518) can retrieve payloads from the C2 server.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [PolyglotDuke](https://attack.mitre.org/software/S0518) can be executed using rundll32.exe.[^2]  |
| [[Native API\|T1106]] | Native API | [PolyglotDuke](https://attack.mitre.org/software/S0518) can use `LoadLibraryW` and `CreateProcess` to load and execute code.[^2]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [PolyglotDuke](https://attack.mitre.org/software/S0518) can use Twitter, Reddit, Imgur and other websites to get a C2 URL.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PolyglotDuke](https://attack.mitre.org/software/S0518) has has used HTTP GET requests in C2 communications.[^2]  |
| [[Steganography\|T1027.003]] | Steganography | [PolyglotDuke](https://attack.mitre.org/software/S0518) can use steganography to hide C2 information in images.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PolyglotDuke](https://attack.mitre.org/software/S0518) can use a custom algorithm to decrypt strings used by the malware.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


