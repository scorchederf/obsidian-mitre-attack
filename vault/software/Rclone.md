---
aliases: 
    - S1040
    
mitre-attack: https://attack.mitre.org/software/S1040
---

## S1040

[Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.[^5] [^6] [^10] [^12] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data to cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA.[^5] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Rclone](https://attack.mitre.org/software/S1040) can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^5]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | The [Rclone](https://attack.mitre.org/software/S1040) "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.[^5] [^7]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Rclone](https://attack.mitre.org/software/S1040) can compress files using `gzip` prior to exfiltration.[^5]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over SFTP or HTTPS via WebDAV.[^5]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over FTP or HTTP, including HTTP via WebDAV.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[WIRTE\|G0090]] | WIRTE |
| [[Medusa Group\|G1051]] | Medusa Group |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[INC Ransom\|G1032]] | INC Ransom |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Akira\|G1024]] | Akira |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |



## References

[^1]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^2]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^3]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^4]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^5]: [Rclone](https://rclone.org)


[^6]: [Rclone Wars](https://redcanary.com/blog/rclone-mega-extortion/)


[^7]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^8]: [Huntress INC Ransomware May 2024](https://www.huntress.com/blog/lolbin-to-inc-ransomware)


[^9]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^10]: [Detecting Rclone](https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/)


[^11]: [SOCRadar_MuddyWaterDindoor_Mar2026](https://socradar.io/blog/iran-muddywater-dindoor-malware-us-networks/)


[^12]: [DarkSide Ransomware Gang](https://unit42.paloaltonetworks.com/darkside-ransomware/)


[^13]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^14]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^15]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


