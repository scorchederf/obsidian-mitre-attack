---
aliases: 
    - S0585
    
mitre-attack: https://attack.mitre.org/software/S0585
---

## S0585

[Kerrdown](https://attack.mitre.org/software/S0585) is a custom downloader that has been used by [APT32](https://attack.mitre.org/groups/G0050) since at least 2018 to install spyware from a server on the victim's network.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Kerrdown](https://attack.mitre.org/software/S0585) has been distributed via e-mails containing a malicious link.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Kerrdown](https://attack.mitre.org/software/S0585) can use a VBS base64 decoder function published by Motobit.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Kerrdown](https://attack.mitre.org/software/S0585) has been distributed through malicious e-mail attachments.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kerrdown](https://attack.mitre.org/software/S0585) can encrypt, encode, and compress multiple layers of shellcode.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kerrdown](https://attack.mitre.org/software/S0585) has the ability to determine if the compromised host is running a 32 or 64 bit OS architecture.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Kerrdown](https://attack.mitre.org/software/S0585) can use DLL side-loading to load malicious DLLs.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kerrdown](https://attack.mitre.org/software/S0585) can download specific payloads to a compromised host based on OS architecture.[^2]  |
| [[Compression\|T1027.015]] | Compression | [Kerrdown](https://attack.mitre.org/software/S0585) can encrypt, encode, and compress multiple layers of shellcode.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kerrdown](https://attack.mitre.org/software/S0585) can decode, decrypt, and decompress multiple layers of shellcode.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Kerrdown](https://attack.mitre.org/software/S0585) has gained execution through victims opening malicious files.[^1] [^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Kerrdown](https://attack.mitre.org/software/S0585) has gained execution through victims opening malicious links.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)


[^2]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


