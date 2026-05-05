---
aliases: 
    - S0611
    
mitre-attack: https://attack.mitre.org/software/S0611
---

## S0611

[Clop](https://attack.mitre.org/software/S0611) is a ransomware family that was first observed in February 2019 and has been used against retail, transportation and logistics, education, manufacturing, engineering, automotive, energy, financial, aerospace, telecommunications, professional and legal services, healthcare, and high tech industries. [Clop](https://attack.mitre.org/software/S0611) is a variant of the CryptoMix ransomware.[^1] [^3] [^4]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Clop](https://attack.mitre.org/software/S0611) can search for processes with antivirus and antimalware product names.[^1] [^3]  |
| [[Service Stop\|T1489]] | Service Stop | [Clop](https://attack.mitre.org/software/S0611) can kill several processes and services related to backups and security solutions.[^4] [^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Clop](https://attack.mitre.org/software/S0611) has used a simple XOR operation to decrypt strings.[^1]  |
| [[Native API\|T1106]] | Native API | [Clop](https://attack.mitre.org/software/S0611) has used built-in API functions such as WNetOpenEnumW(), WNetEnumResourceW(), WNetCloseEnum(), GetProcAddress(), and VirtualAlloc().[^1] [^3]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Clop](https://attack.mitre.org/software/S0611) has used the `sleep` command to avoid sandbox detection.[^4]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Clop](https://attack.mitre.org/software/S0611) has been packed to help avoid detection.[^1] [^3]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Clop](https://attack.mitre.org/software/S0611) has checked the keyboard language using the GetKeyboardLayout() function to avoid installation on Russian-language or other Commonwealth of Independent States-language machines; it will also check the `GetTextCharset` function.[^1]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Clop](https://attack.mitre.org/software/S0611) has searched folders and subfolders for files to encrypt.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Clop](https://attack.mitre.org/software/S0611) can enumerate all processes on the victim's machine.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Clop](https://attack.mitre.org/software/S0611) can use cmd.exe to help execute commands on the system.[^3]   |
| [[Code Signing\|T1553.002]] | Code Signing | [Clop](https://attack.mitre.org/software/S0611) can use code signing to evade detection.[^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Clop](https://attack.mitre.org/software/S0611) can make modifications to Registry keys.[^3]   |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Clop](https://attack.mitre.org/software/S0611) can enumerate network shares.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Clop](https://attack.mitre.org/software/S0611) can delete the shadow volumes with `vssadmin Delete Shadows /all /quiet` and can use bcdedit to disable recovery options.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Clop](https://attack.mitre.org/software/S0611) can encrypt files using AES, RSA, and RC4 and will add the ".clop" extension to encrypted files.[^1] [^4] [^3]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Clop](https://attack.mitre.org/software/S0611) can uninstall or disable security products.[^3]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Clop](https://attack.mitre.org/software/S0611) can use msiexec.exe to disable security tools on the system.[^3]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA505\|G0092]] | TA505 |



## References

[^1]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)


[^2]: Clop


[^3]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)


[^4]: [Unit42 Clop April 2021](https://unit42.paloaltonetworks.com/clop-ransomware/)


