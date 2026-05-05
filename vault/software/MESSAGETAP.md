---
aliases: 
    - S0443
    
mitre-attack: https://attack.mitre.org/software/S0443
---

## S0443

[MESSAGETAP](https://attack.mitre.org/software/S0443) is a data mining malware family deployed by [APT41](https://attack.mitre.org/groups/G0096) into telecommunications networks to monitor and save SMS traffic from specific phone numbers, IMSI numbers, or that contain specific keywords. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | Once loaded into memory, [MESSAGETAP](https://attack.mitre.org/software/S0443) deletes the keyword_parm.txt and parm.txt configuration files from disk. [^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [MESSAGETAP](https://attack.mitre.org/software/S0443) uses the libpcap library to listen to all traffic and parses network protocols starting with Ethernet and IP layers. It continues parsing protocol layers including SCTP, SCCP, and TCAP and finally extracts SMS message data and routing metadata.  [^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | After checking for the existence of two files, keyword_parm.txt and parm.txt, [MESSAGETAP](https://attack.mitre.org/software/S0443) XOR decodes and read the contents of the files. [^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [MESSAGETAP](https://attack.mitre.org/software/S0443) stored targeted SMS messages that matched its target list in CSV files on the compromised system.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | After loading the keyword and phone data files, [MESSAGETAP](https://attack.mitre.org/software/S0443) begins monitoring all network connections to and from the victim server. [^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [MESSAGETAP](https://attack.mitre.org/software/S0443) has XOR-encrypted and stored contents of SMS messages that matched its target list. [^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [MESSAGETAP](https://attack.mitre.org/software/S0443) checks two files, keyword_parm.txt and parm.txt, for instructions on how to target and save data parsed and extracted from SMS message data from the network traffic. If an SMS message contained either a phone number, IMSI number, or keyword that matched the predefined list, it is saved to a CSV file for later theft by the threat actor.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MESSAGETAP](https://attack.mitre.org/software/S0443) checks for the existence of two configuration files (keyword_parm.txt and parm.txt) and attempts to read the files every 30 seconds.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)


[^2]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


