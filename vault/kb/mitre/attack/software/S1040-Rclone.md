---
aliases: 
    - S1040
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1040-Rclone
---

## Description

[[kb/mitre/attack/software/S1040-Rclone\|Rclone]] is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] has been used in a number of ransomware campaigns, including those associated with the Conti and DarkSide Ransomware-as-a-Service operations.[^5] [^2] [^3] [^1] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1030-Data_Transfer_Size_Limits\|T1030]] | Data Transfer Size Limits | The [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.[^5] [^4]  |
| [[kb/mitre/attack/techniques/T1048.002-Exfiltration_Over_Asymmetric_Encrypted_Non-C2_Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can exfiltrate data over SFTP or HTTPS via WebDAV.[^5]  |
| [[kb/mitre/attack/techniques/T1048.003-Exfiltration_Over_Unencrypted_Non-C2_Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can exfiltrate data over FTP or HTTP, including HTTP via WebDAV.[^5]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^5]  |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can compress files using `gzip` prior to exfiltration.[^5]  |
| [[kb/mitre/attack/techniques/T1567.002-Exfiltration_to_Cloud_Storage\|T1567.002]] | Exfiltration to Cloud Storage | [[kb/mitre/attack/software/S1040-Rclone\|Rclone]] can exfiltrate data to cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA.[^5] [^4]  |





> [!info]- References
> [^1]: [DarkSide Ransomware Gang](https://unit42.paloaltonetworks.com/darkside-ransomware/)

> [^2]: [Rclone Wars](https://redcanary.com/blog/rclone-mega-extortion/)

> [^3]: [Detecting Rclone](https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/)

> [^4]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)

> [^5]: [Rclone](https://rclone.org)


