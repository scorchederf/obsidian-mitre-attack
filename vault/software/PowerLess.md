---
aliases: 
    - S1012
    
mitre-attack: https://attack.mitre.org/software/S1012
---

## S1012

[PowerLess](https://attack.mitre.org/software/S1012) is a PowerShell-based modular backdoor that has been used by [Magic Hound](https://attack.mitre.org/groups/G0059) since at least 2022.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [PowerLess](https://attack.mitre.org/software/S1012) can use a module to log keystrokes.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [PowerLess](https://attack.mitre.org/software/S1012) has a browser info stealer module that can read Chrome and Edge browser database files.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PowerLess](https://attack.mitre.org/software/S1012) can download additional payloads to a compromised host.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PowerLess](https://attack.mitre.org/software/S1012) has the ability to exfiltrate data, including Chrome and Edge browser database files, from compromised machines.[^1] <br> |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [PowerLess](https://attack.mitre.org/software/S1012) can use an encrypted channel for C2 communications.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PowerLess](https://attack.mitre.org/software/S1012) can stage stolen browser data in `C:\\Windows\\Temp\\cup.tmp` and keylogger data in `C:\\Windows\\Temp\\Report.06E17A5A-7325-4325-8E5D-E172EBA7FC5BK`.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [PowerLess](https://attack.mitre.org/software/S1012) can encrypt browser database files prior to exfiltration.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [PowerLess](https://attack.mitre.org/software/S1012) is written in and executed via PowerShell without using powershell.exe.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PowerLess](https://attack.mitre.org/software/S1012) can use base64 and AES ECB decryption prior to execution of downloaded modules.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Magic Hound\|G0059]] | Magic Hound |



## References

[^1]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)


