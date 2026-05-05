---
aliases: 
    - S0280
    
mitre-attack: https://attack.mitre.org/software/S0280
---

## S0280

[MirageFox](https://attack.mitre.org/software/S0280) is a remote access tool used against Windows systems. It appears to be an upgraded version of a tool known as Mirage, which is a RAT believed to originate in 2012. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MirageFox](https://attack.mitre.org/software/S0280) can collect CPU and architecture information from the victim’s machine.[^2]  |
| [[DLL\|T1574.001]] | DLL | [MirageFox](https://attack.mitre.org/software/S0280) is likely loaded via DLL hijacking into a legitimate McAfee binary.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MirageFox](https://attack.mitre.org/software/S0280) has the capability to execute commands using cmd.exe.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MirageFox](https://attack.mitre.org/software/S0280) can gather the username from the victim’s machine.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [MirageFox](https://attack.mitre.org/software/S0280) has a function for decrypting data containing C2 configuration information.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ke3chang\|G0004]] | Ke3chang |



## References

[^1]: MirageFox


[^2]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)


