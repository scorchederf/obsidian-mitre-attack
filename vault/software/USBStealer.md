---
aliases: 
    - S0136
    
mitre-attack: https://attack.mitre.org/software/S0136
---

## S0136

[USBStealer](https://attack.mitre.org/software/S0136) is malware that has been used by [APT28](https://attack.mitre.org/groups/G0007) since at least 2005 to extract information from air-gapped networks. It does not have the capability to communicate over the Internet and has been used in conjunction with [ADVSTORESHELL](https://attack.mitre.org/software/S0045). [^3]  [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | Once a removable media device is inserted back into the first victim, [USBStealer](https://attack.mitre.org/software/S0136) collects data from it that was exfiltrated from a second victim.[^3] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Most strings in [USBStealer](https://attack.mitre.org/software/S0136) are encrypted using 3DES and XOR and reversed.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [USBStealer](https://attack.mitre.org/software/S0136) searches victim drives for files matching certain extensions (“.skr”,“.pkr” or “.key”) or names.[^3] [^1]  |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [USBStealer](https://attack.mitre.org/software/S0136) exfiltrates collected files via removable media from air-gapped victims.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | [USBStealer](https://attack.mitre.org/software/S0136) sets the timestamps of its dropper files to the last-access and last-write timestamps of a standard Windows library chosen on the system.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [USBStealer](https://attack.mitre.org/software/S0136) registers itself under a Registry Run key with the name "USB Disk Security."[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | For all non-removable drives on a victim, [USBStealer](https://attack.mitre.org/software/S0136) executes automated collection of certain files for later exfiltration.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [USBStealer](https://attack.mitre.org/software/S0136) mimics a legitimate Russian program called USB Disk Security.[^3]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [USBStealer](https://attack.mitre.org/software/S0136) automatically exfiltrates collected files via removable media when an infected device connects to an air-gapped victim machine after initially being connected to an internet-enabled victim machine. [^3]  |
| [[Communication Through Removable Media\|T1092]] | Communication Through Removable Media | [USBStealer](https://attack.mitre.org/software/S0136) drops commands for a second victim onto a removable media drive inserted into the first victim, and commands are executed when the drive is inserted into the second victim.[^3]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [USBStealer](https://attack.mitre.org/software/S0136) drops itself onto removable media and relies on Autorun to execute the malicious file when a user opens the removable media on another system.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [USBStealer](https://attack.mitre.org/software/S0136) has several commands to delete files associated with the malware from the victim.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [USBStealer](https://attack.mitre.org/software/S0136) monitors victims for insertion of removable drives. When dropped onto a second victim, it also enumerates drives connected to the system.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [USBStealer](https://attack.mitre.org/software/S0136) collects files matching certain criteria from the victim and stores them in a local directory for later exfiltration.[^3] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)


[^2]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^3]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)


