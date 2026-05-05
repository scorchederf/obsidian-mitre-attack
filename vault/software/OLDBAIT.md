---
aliases: 
    - S0138
    
mitre-attack: https://attack.mitre.org/software/S0138
---

## S0138

[OLDBAIT](https://attack.mitre.org/software/S0138) is a credential harvester used by [APT28](https://attack.mitre.org/groups/G0007). [^2]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [OLDBAIT](https://attack.mitre.org/software/S0138) installs itself in `%ALLUSERPROFILE%\\Application Data\Microsoft\MediaPlayer\updatewindws.exe`; the directory name is missing a space and the file name is missing the letter "o."[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [OLDBAIT](https://attack.mitre.org/software/S0138) collects credentials from Internet Explorer, Mozilla Firefox, and Eudora.[^2]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [OLDBAIT](https://attack.mitre.org/software/S0138) can use SMTP for C2.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [OLDBAIT](https://attack.mitre.org/software/S0138) obfuscates internal strings and unpacks them at startup.[^2]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [OLDBAIT](https://attack.mitre.org/software/S0138) collects credentials from several email clients.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OLDBAIT](https://attack.mitre.org/software/S0138) can use HTTP for C2.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [FireEye APT28 January 2017](https://www.mandiant.com/sites/default/files/2021-09/APT28-Center-of-Storm-2017.pdf)


[^2]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


