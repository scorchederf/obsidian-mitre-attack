---
aliases: 
    - MirrorFace
    - Earth Kasha
mitre-attack: https://attack.mitre.org/groups/G1054
---

## G1054

[MirrorFace](https://attack.mitre.org/groups/G1054) is a People's Republic of China (PRC)-aligned cyberespionage actor believed to be a subgroup under the [menuPass](https://attack.mitre.org/groups/G0045) umbrella based on targeting, tools, and infrastructure overlaps. [MirrorFace](https://attack.mitre.org/groups/G1054) has been active since at least 2019, at first exclusively targeting Japanese organizations across the media, defense, diplomatic, financial, manufacturing, and academic sectors. Subsequent [MirrorFace](https://attack.mitre.org/groups/G1054) operations included targets in Central Europe and featured use of [LODEINFO](https://attack.mitre.org/software/S9020), [HiddenFace](https://attack.mitre.org/software/S9023), and [UPPERCUT](https://attack.mitre.org/software/S0275) malware.[^8] [^7] [^6] [^3] [^9] [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [MirrorFace](https://attack.mitre.org/groups/G1054) has embedded OneDrive URLs in emails leading to malicious file installation.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Tasklist](https://attack.mitre.org/software/S0057) on compromised hosts for discovery.[^3]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [MirrorFace](https://attack.mitre.org/groups/G1054) can modify the system firewall to allow communication to certain ports.[^3]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [MirrorFace](https://attack.mitre.org/groups/G1054) has gathered data and files of interest on a single victim machine.[^9]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [MirrorFace](https://attack.mitre.org/groups/G1054) has disabled Windows Defender in compromised environments.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [MirrorFace](https://attack.mitre.org/groups/G1054) has used native Windows tools to obtain domain user information.[^9]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has deployed shellcode to check for Japanese Microsoft Office settings.[^4]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [MirrorFace](https://attack.mitre.org/groups/G1054) has placed specific content in phishing emails to target members of particular political parties.[^6] <br> |
| [[Proxy\|T1090]] | Proxy | [MirrorFace](https://attack.mitre.org/groups/G1054) has used the GO Simple Tunnel (GOST) proxy tool.[^3]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [MirrorFace](https://attack.mitre.org/groups/G1054) has deleted Windows event logs.[^3]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [MirrorFace](https://attack.mitre.org/groups/G1054) has used RDP to exfiltrate files of interest.[^9]  |
| [[Malware\|T1587.001]] | Malware | [MirrorFace](https://attack.mitre.org/groups/G1054) has created and continued to develop custom strains of malware including [LODEINFO](https://attack.mitre.org/software/S9020).[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [MirrorFace](https://attack.mitre.org/groups/G1054) has deleted directories containing malware and archives with files collected from the victim environment.[^6] [^9] [^1] [^3]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [MirrorFace](https://attack.mitre.org/groups/G1054) has used vssadmin to copy registry hives including SAM.[^9] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has run commands to check the content of folders on compromised hosts and has specifically targeted files with .doc, .ppt, .xls, .jtd, .eml, .xps, and .pdf extensions.[^6] [^9] [^3]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has run `nltest.exe  /domain_trusts` on compromised systems to discover domain relationships.[^9] <br> |
| [[Impersonation\|T1684.001]] | Impersonation | [MirrorFace](https://attack.mitre.org/groups/G1054) has sent targeted emails purporting to be from a Japanese political party’s PR department.[^6]  |
| [[Tool\|T1588.002]] | Tool | [MirrorFace](https://attack.mitre.org/groups/G1054) has used tools including the Secure Copy Protocol (SCP) client from PuTTY and [Cobalt Strike](https://attack.mitre.org/software/S0154).[^6] [^9] [^3]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [MirrorFace](https://attack.mitre.org/groups/G1054) has dumped LSASS memory for credential access.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [MirrorFace](https://attack.mitre.org/groups/G1054) has lured victims into opening crafted Word, Excel, and SFX files for execution.[^8] [^6] [^4] [^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Ping](https://attack.mitre.org/software/S0097) for system discovery.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [ipconfig](https://attack.mitre.org/software/S0100) for reconnaissance.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [MirrorFace](https://attack.mitre.org/groups/G1054) has abused a known Microsoft digital signature verification issues to append encrypted data to digital signatures that still appear to be validly signed.[^6]  |
| [[Data from Local System\|T1005]] | Data from Local System | [MirrorFace](https://attack.mitre.org/groups/G1054) gathered data and files of interest from victim's systems.[^9]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [MirrorFace](https://attack.mitre.org/groups/G1054) has used `cmd.exe` for malware execution, file discovery, and manual file manipulation.[^9] [^1] [^3] [^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [MirrorFace](https://attack.mitre.org/groups/G1054) has sent spearphishing emails with malicious attachments to deliver malware payloads.[^8] [^6] [^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [MirrorFace](https://attack.mitre.org/groups/G1054) has used remote templates with VBA code in malware infection chains.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Tasklist](https://attack.mitre.org/software/S0057) for discovery post compromise.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has employed malicious macros and native Windows tools such as csvde.exe, nltest.exe and quser.exe for discovery.[^4] [^9] [^3]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Secure File Transfer Protocol (SFTP) for file exfiltration.[^3]  |
| [[DLL\|T1574.001]] | DLL | [MirrorFace](https://attack.mitre.org/groups/G1054) has used legitimate EXE files to load malicious DLLs via sideloading.[^8] [^6] [^4] [^9]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [MirrorFace](https://attack.mitre.org/groups/G1054) has used SMB to copy malware between systems in compromised environments.[^9] [^3]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [MirrorFace](https://attack.mitre.org/groups/G1054) has used the the PuTTY suite Secure Copy Protocol (SCP) client for file transfer.[^6]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [MirrorFace](https://attack.mitre.org/groups/G1054) has exploited vulnerabilities in Fortigate and Array AG devices for initial access.[^3]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [MirrorFace](https://attack.mitre.org/groups/G1054) has crafted malware payloads to appear as Privacy-Enhanced Mail (PEM) files.[^4]  |
| [[NTDS\|T1003.003]] | NTDS | [MirrorFace](https://attack.mitre.org/groups/G1054) has dumped NTDS.dit through volume shadow copies.[^9] [^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [MirrorFace](https://attack.mitre.org/groups/G1054) has used rar.exe and the Makecab utility to archive files of interest prior to exfiltration.[^6] [^9] [^3]  |
| [[Template Injection\|T1221]] | Template Injection | [MirrorFace](https://attack.mitre.org/groups/G1054) has used remote template injection to retrieve malicious payloads from the C2.[^4]  |
| [[Password Filter DLL\|T1556.002]] | Password Filter DLL | [MirrorFace](https://attack.mitre.org/groups/G1054) has used a tool named MRSAStealer as a password filter to collect credentials on password changes.[^6]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [MirrorFace](https://attack.mitre.org/groups/G1054) has leveraged WMIC on targeted systems post compromise.[^3]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [MirrorFace](https://attack.mitre.org/groups/G1054) has exfiltrated stored emails from compromised hosts.[^6]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Base64 encoded shellcode in infection chains to evade detection.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Windows native tools to enumerate user information.[^9]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net |  [^3]  |
| [[ipconfig\|S0100]] | ipconfig | [^3]  |
| [[Tasklist\|S0057]] | Tasklist | [^3] <br> |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^3]  |
| [[Nltest\|S0359]] | Nltest | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Nltest](https://attack.mitre.org/software/S0359) for discovery.[^9]  |
| [[nbtstat\|S0102]] | nbtstat |  [^3]  |
| [[Ping\|S0097]] | Ping |  [^3]  |
| [[Wevtutil\|S0645]] | Wevtutil | [^3] <br> |
| [[ROAMINGHOUSE\|S9026]] | ROAMINGHOUSE | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) during operations.[^1]  |
| [[MirrorStealer\|S9022]] | MirrorStealer | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [MirrorStealer](https://attack.mitre.org/software/S9022) to harvest credentials.[^6]  |
| [[NOOPLDR\|S9025]] | NOOPLDR | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [NOOPLDR](https://attack.mitre.org/software/S9025) during operations.[^9]  |
| [[LODEINFO\|S9020]] | LODEINFO | [^8] [^4]  |
| [[HiddenFace\|S9023]] | HiddenFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [HiddenFace](https://attack.mitre.org/software/S9023) during operations.[^5] [^3] [^9]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) for persistence.[^9]  |
| [[DOWNIISSA\|S9021]] | DOWNIISSA | [DOWNIISSA](https://attack.mitre.org/software/S9021) has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) to download [LODEINFO](https://attack.mitre.org/software/S9020).[^8]  |
| [[UPPERCUT\|S0275]] | UPPERCUT |  [MirrorFace](https://attack.mitre.org/groups/G1054) has used [UPPERCUT](https://attack.mitre.org/software/S0275) during operations.[^1]  |



## References

[^1]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^2]: Earth Kasha


[^3]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^4]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^5]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^6]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^7]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^8]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


[^9]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


