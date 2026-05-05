---
aliases: 
    - S0414
    
mitre-attack: https://attack.mitre.org/software/S0414
---

## S0414

[BabyShark](https://attack.mitre.org/software/S0414) is a Microsoft Visual Basic (VB) script-based malware family that is believed to be associated with several North Korean campaigns. [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BabyShark](https://attack.mitre.org/software/S0414) has used scheduled tasks to maintain persistence.[^8]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `whoami` command.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BabyShark](https://attack.mitre.org/software/S0414) has downloaded additional files from the C2.[^6] [^2]  |
| [[Query Registry\|T1012]] | Query Registry | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `reg query` command for `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default`.[^4] 	 |
| [[Mshta\|T1218.005]] | Mshta | [BabyShark](https://attack.mitre.org/software/S0414) has used mshta.exe to download and execute applications from a remote server.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [BabyShark](https://attack.mitre.org/software/S0414) has a [PowerShell](https://attack.mitre.org/techniques/T1059/001)-based remote administration ability that can implement a PowerShell or C# based keylogger.[^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `tasklist` command.[^4] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [BabyShark](https://attack.mitre.org/software/S0414) can execute additional  VisualBasic content.[^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BabyShark](https://attack.mitre.org/software/S0414) has used `dir` to search for "programfiles" and "appdata".[^4] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BabyShark](https://attack.mitre.org/software/S0414) has the ability to decode downloaded files prior to execution.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `ver` command.[^4] 	 |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [BabyShark](https://attack.mitre.org/software/S0414) has encoded data using [certutil](https://attack.mitre.org/software/S0160) before exfiltration.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BabyShark](https://attack.mitre.org/software/S0414) has cleaned up all files associated with the secondary payload execution.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BabyShark](https://attack.mitre.org/software/S0414) has added a Registry key to ensure all future macros are enabled for Microsoft Word and Excel as well as for additional persistence.[^4] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `ipconfig /all` command.[^4] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BabyShark](https://attack.mitre.org/software/S0414) has used cmd.exe to execute commands.[^4] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^2]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)


[^3]: BabyShark


[^4]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^5]: LATEOP


[^6]: [Unit42 BabyShark Apr 2019](https://unit42.paloaltonetworks.com/babyshark-malware-part-two-attacks-continue-using-kimjongrat-and-pcrat/)


[^7]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^8]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


