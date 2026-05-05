---
aliases: 
    - S0582
    
mitre-attack: https://attack.mitre.org/software/S0582
---

## S0582

[LookBack](https://attack.mitre.org/software/S0582) is a remote access trojan written in C++ that was used against at least three US utility companies in July 2019. The TALONITE activity group has been observed using [LookBack](https://attack.mitre.org/software/S0582).[^4] [^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Stop\|T1489]] | Service Stop | [LookBack](https://attack.mitre.org/software/S0582) can kill processes and delete services.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LookBack](https://attack.mitre.org/software/S0582) executes the `cmd.exe` command.[^4]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [LookBack](https://attack.mitre.org/software/S0582) has used VBA macros in Microsoft Word attachments to drop additional files to the host.[^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [LookBack](https://attack.mitre.org/software/S0582) can enumerate services on the victim machine.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LookBack](https://attack.mitre.org/software/S0582) can list running processes.[^4]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [LookBack](https://attack.mitre.org/software/S0582) can shutdown and reboot the victim machine.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [LookBack](https://attack.mitre.org/software/S0582) has a C2 proxy tool that masquerades as `GUP.exe`, which is software used by Notepad++.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LookBack](https://attack.mitre.org/software/S0582)’s C2 proxy tool sends data to a C2 server over HTTP.[^4]  |
| [[Screen Capture\|T1113]] | Screen Capture | [LookBack](https://attack.mitre.org/software/S0582) can take desktop screenshots.[^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [LookBack](https://attack.mitre.org/software/S0582) uses a modified version of RC4 for data transfer.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [LookBack](https://attack.mitre.org/software/S0582) sets up a Registry Run key to establish a persistence mechanism.[^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [LookBack](https://attack.mitre.org/software/S0582) removes itself after execution and can delete files on the system.[^4]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [LookBack](https://attack.mitre.org/software/S0582) uses a custom binary protocol over sockets for C2 communications.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LookBack](https://attack.mitre.org/software/S0582) can retrieve file listings from the victim machine.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LookBack](https://attack.mitre.org/software/S0582) has a function that decrypts malicious data.[^4]  |
| [[DLL\|T1574.001]] | DLL | [LookBack](https://attack.mitre.org/software/S0582) side loads its communications module as a DLL into the `libcurl.dll` loader.[^4]  |




## References

[^1]: LookBack


[^2]: [Dragos Threat Report 2020](https://hub.dragos.com/hubfs/Year-in-Review/Dragos_2020_ICS_Cybersecurity_Year_In_Review.pdf?hsCtaTracking=159c0fc3-92d8-425d-aeb8-12824f2297e8%7Cf163726d-579b-4996-9a04-44e5a124d770)


[^3]: [Dragos TALONITE](https://www.dragos.com/threat/talonite/)


[^4]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


