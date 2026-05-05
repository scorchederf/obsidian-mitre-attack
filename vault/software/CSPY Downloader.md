---
aliases: 
    - S0527
    
mitre-attack: https://attack.mitre.org/software/S0527
---

## S0527

[CSPY Downloader](https://attack.mitre.org/software/S0527) is a tool designed to evade analysis and download additional payloads used by [Kimsuky](https://attack.mitre.org/groups/G0094).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to self delete.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [CSPY Downloader](https://attack.mitre.org/software/S0527) can write to the Registry under the `%windir%` variable to execute tasks.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [CSPY Downloader](https://attack.mitre.org/software/S0527) can use the schtasks utility to bypass UAC.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [CSPY Downloader](https://attack.mitre.org/software/S0527) has come signed with revoked certificates.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CSPY Downloader](https://attack.mitre.org/software/S0527) can download additional tools to a compromised host.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [CSPY Downloader](https://attack.mitre.org/software/S0527) has attempted to appear as a legitimate Windows service with a fake description claiming it is used to support packed applications.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [CSPY Downloader](https://attack.mitre.org/software/S0527) can use GET requests to download additional payloads from C2.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [CSPY Downloader](https://attack.mitre.org/software/S0527) has been delivered via malicious documents with embedded macros.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [CSPY Downloader](https://attack.mitre.org/software/S0527) can bypass UAC using the SilentCleanup task to execute the binary with elevated privileges.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [CSPY Downloader](https://attack.mitre.org/software/S0527) can search loaded modules, PEB structure, file paths, Registry keys, and memory to determine if it is being debugged or running in a virtual environment.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [CSPY Downloader](https://attack.mitre.org/software/S0527) has been packed with UPX.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to remove values it writes to the Registry.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


