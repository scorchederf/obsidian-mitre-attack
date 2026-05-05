---
aliases: 
    - S0606
    
mitre-attack: https://attack.mitre.org/software/S0606
---

## S0606

[Bad Rabbit](https://attack.mitre.org/software/S0606) is a self-propagating ransomware that affected the Ukrainian transportation sector in 2017. [Bad Rabbit](https://attack.mitre.org/software/S0606) has also targeted organizations and consumers in Russia. [^3] [^2] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Bad Rabbit](https://attack.mitre.org/software/S0606) has encrypted files and disks using AES-128-CBC and RSA-2048.[^3]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Bad Rabbit](https://attack.mitre.org/software/S0606)’s `infpub.dat` file uses NTLM login credentials to brute force Windows machines.[^3]  |
| [[Firmware Corruption\|T1495]] | Firmware Corruption | [Bad Rabbit](https://attack.mitre.org/software/S0606) has used an executable that installs a modified bootloader to prevent normal boot-up.[^3]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Bad Rabbit](https://attack.mitre.org/software/S0606) drops a file named `infpub.dat`into the Windows directory and is executed through SCManager and `rundll.exe`. |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Bad Rabbit](https://attack.mitre.org/software/S0606)’s `infpub.dat` file creates a scheduled task to launch a malicious executable.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Bad Rabbit](https://attack.mitre.org/software/S0606) has masqueraded as a Flash Player installer through the executable file `install_flash_player.exe`.[^2] [^3]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Bad Rabbit](https://attack.mitre.org/software/S0606) spread through watering holes on popular sites by injecting JavaScript into the HTML body or a `.js` file.[^2] [^3]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Bad Rabbit](https://attack.mitre.org/software/S0606) has used [Mimikatz](https://attack.mitre.org/software/S0002) to harvest credentials from the victim's machine.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Bad Rabbit](https://attack.mitre.org/software/S0606) has attempted to bypass UAC and gain elevated administrative privileges.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Bad Rabbit](https://attack.mitre.org/software/S0606) can enumerate all running processes to compare hashes.[^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Bad Rabbit](https://attack.mitre.org/software/S0606) enumerates open SMB shares on internal victim networks.[^2]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Bad Rabbit](https://attack.mitre.org/software/S0606) used the EternalRomance SMB exploit to spread through victim networks.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Bad Rabbit](https://attack.mitre.org/software/S0606) has used rundll32 to launch a malicious DLL as `C:Windowsinfpub.dat`.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Bad Rabbit](https://attack.mitre.org/software/S0606) has been executed through user installation of an executable disguised as a flash installer.[^2] [^3]  |
| [[Native API\|T1106]] | Native API | [Bad Rabbit](https://attack.mitre.org/software/S0606) has used various Windows API calls.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Secureworks IRON VIKING ](https://www.secureworks.com/research/threat-profiles/iron-viking)


[^2]: [ESET Bad Rabbit](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)


[^3]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)


[^4]: [Dragos Apr 2019](https://dragos.com/blog/industry-news/implications-of-it-ransomware-for-ics-environments/)


