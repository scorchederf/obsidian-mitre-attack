---
aliases: 
    - S0079
    
mitre-attack: https://attack.mitre.org/software/S0079
---

## S0079

[MobileOrder](https://attack.mitre.org/software/S0079) is a Trojan intended to compromise Android mobile devices. It has been used by [Scarlet Mimic](https://attack.mitre.org/groups/G0029). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [MobileOrder](https://attack.mitre.org/software/S0079) exfiltrates data to its C2 server over the same protocol as C2 communications.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to download a file from the C2 server to the victim mobile device's SD card.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MobileOrder](https://attack.mitre.org/software/S0079) exfiltrates data collected from the victim mobile device.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload information about all running processes to its C2 server.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload to its C2 server victim mobile device information, including IMEI, IMSI, SIM card serial number, phone number, Android version, and other information.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload to its C2 server information about files on the victim mobile device, including SD card size, installed app list, SMS content, contacts, and calling history.[^1]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload to its C2 server victim browser bookmarks.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Scarlet Mimic\|G0029]] | Scarlet Mimic |



## References

[^1]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


