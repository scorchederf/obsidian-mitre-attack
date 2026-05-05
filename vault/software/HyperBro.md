---
aliases: 
    - S0398
    
mitre-attack: https://attack.mitre.org/software/S0398
---

## S0398

[HyperBro](https://attack.mitre.org/software/S0398) is a custom in-memory backdoor used by [Threat Group-3390](https://attack.mitre.org/groups/G0027).[^4] [^1] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Injection\|T1055]] | Process Injection | [HyperBro](https://attack.mitre.org/software/S0398) can run shellcode it injects into a newly created process.[^4]  |
| [[DLL\|T1574.001]] | DLL | [HyperBro](https://attack.mitre.org/software/S0398) has used a legitimate application to sideload a DLL to decrypt, decompress, and run a payload.[^4] [^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HyperBro](https://attack.mitre.org/software/S0398) has used HTTPS for C2 communications.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [HyperBro](https://attack.mitre.org/software/S0398) can unpack and decrypt its payload prior to execution.[^2] [^3]  |
| [[Service Execution\|T1569.002]] | Service Execution | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to start and stop a specified service.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [HyperBro](https://attack.mitre.org/software/S0398) can list all services and their configurations.[^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to take screenshots.[^4]  |
| [[Software Packing\|T1027.002]] | Software Packing | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to pack its payload.[^3]  |
| [[Native API\|T1106]] | Native API | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to run an application (`CreateProcessW`) or script/file (`ShellExecuteW`) via API.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HyperBro](https://attack.mitre.org/software/S0398) can be delivered encrypted to a compromised host.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to download additional files.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to delete a specified file.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |



## References

[^1]: [Securelist LuckyMouse June 2018](https://securelist.com/luckymouse-hits-national-data-center/86083/)


[^2]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^3]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^4]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^5]: [Hacker News LuckyMouse June 2018](https://thehackernews.com/2018/06/chinese-watering-hole-attack.html)


[^6]: HyperBro


