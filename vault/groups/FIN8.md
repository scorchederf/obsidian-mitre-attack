---
aliases: 
    - FIN8
    - Syssphinx
mitre-attack: https://attack.mitre.org/groups/G0061
---

## G0061

[FIN8](https://attack.mitre.org/groups/G0061) is a financially motivated threat group that has been active since at least January 2016, and known for targeting organizations in the hospitality, retail, entertainment, insurance, technology, chemical, and financial sectors. In June 2021, security researchers detected [FIN8](https://attack.mitre.org/groups/G0061) switching from targeting point-of-sale (POS) devices to distributing a number of ransomware variants.[^7] [^1] [^6] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Valid Accounts\|T1078]] | Valid Accounts | [FIN8](https://attack.mitre.org/groups/G0061) has used valid accounts for persistence and lateral movement.[^8]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [FIN8](https://attack.mitre.org/groups/G0061) has used FTP to exfiltrate collected data.[^8]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has executed the command `quser` to display the session details of a compromised machine.[^5]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has used Registry keys to detect and avoid executing in potential sandboxes.[^8]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [FIN8](https://attack.mitre.org/groups/G0061) has used RDP for lateral movement.[^8]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [FIN8](https://attack.mitre.org/groups/G0061) harvests credentials using Invoke-Mimikatz or Windows Credentials Editor (WCE).[^8]  |
| [[Tool\|T1588.002]] | Tool | [FIN8](https://attack.mitre.org/groups/G0061) has used open-source tools such as [Impacket](https://attack.mitre.org/software/S0357) for targeting efforts.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [FIN8](https://attack.mitre.org/groups/G0061) has used malicious e-mail attachments to lure victims into executing malware.[^7] [^1] [^8]  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [FIN8](https://attack.mitre.org/groups/G0061) has used an expired open-source X.509 certificate for testing in the OpenSSL repository, to connect to actor-controlled C2 servers.[^6]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [FIN8](https://attack.mitre.org/groups/G0061) has exploited the CVE-2016-0167 local vulnerability.[^1] [^8]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [FIN8](https://attack.mitre.org/groups/G0061) has used WMI event subscriptions for persistence.[^3]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [FIN8](https://attack.mitre.org/groups/G0061) has distributed targeted emails containing links to malicious documents with embedded macros.[^8]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [FIN8](https://attack.mitre.org/groups/G0061) has used scheduled tasks to maintain RDP backdoors.[^8]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [FIN8](https://attack.mitre.org/groups/G0061) has used emails with malicious links to lure victims into installing malware.[^7] [^1] [^8]  |
| [[Web Service\|T1102]] | Web Service | [FIN8](https://attack.mitre.org/groups/G0061) has used `sslip.io`, a free IP to domain mapping service that also makes SSL certificate generation easier for traffic encryption, as part of their command and control.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [FIN8](https://attack.mitre.org/groups/G0061) has used environment variables and standard input (stdin) to obfuscate command-line arguments. [FIN8](https://attack.mitre.org/groups/G0061) also obfuscates malicious macros delivered as payloads.[^7] [^8] [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FIN8](https://attack.mitre.org/groups/G0061) has deleted tmp and prefetch files during post compromise cleanup activities. [FIN8](https://attack.mitre.org/groups/G0061) has also deleted PowerShell scripts to evade detection on compromised machines.[^8] [^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [FIN8](https://attack.mitre.org/groups/G0061) has distributed targeted emails containing Word documents with embedded malicious macros.[^7] [^1] [^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FIN8](https://attack.mitre.org/groups/G0061) has used HTTPS for command and control.[^3]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [FIN8](https://attack.mitre.org/groups/G0061) has attempted to map to C$ on enumerated hosts to test the scope of their current credentials/context. [FIN8](https://attack.mitre.org/groups/G0061) has also used smbexec from the [Impacket](https://attack.mitre.org/software/S0357) suite for lateral movement.[^8] [^6]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [FIN8](https://attack.mitre.org/groups/G0061) has cleared logs during post compromise cleanup activities.[^8]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [FIN8](https://attack.mitre.org/groups/G0061) has used RAR to compress collected data before exfiltration.[^8]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [FIN8](https://attack.mitre.org/groups/G0061) aggregates staged data from a network into a single location.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FIN8](https://attack.mitre.org/groups/G0061) has used remote code execution to download subsequent payloads.[^1] [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has used PowerShell Scripts to check the architecture of a compromised machine before the selection of a 32-bit or 64-bit version of a malicious .NET loader.[^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [FIN8](https://attack.mitre.org/groups/G0061)'s malicious spearphishing payloads are executed as [PowerShell](https://attack.mitre.org/techniques/T1059/001). [FIN8](https://attack.mitre.org/groups/G0061) has also used [PowerShell](https://attack.mitre.org/techniques/T1059/001) for lateral movement and credential access.[^7] [^3] [^8] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FIN8](https://attack.mitre.org/groups/G0061) has used a Batch file to automate frequently executed post compromise cleanup activities.[^8]  [FIN8](https://attack.mitre.org/groups/G0061) has also executed commands remotely via `cmd.exe`.[^7] [^3] [^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [FIN8](https://attack.mitre.org/groups/G0061) has used the Plink utility to tunnel RDP back to C2 infrastructure.[^8]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [FIN8](https://attack.mitre.org/groups/G0061) has injected malicious code into a new svchost.exe process.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has used [dsquery](https://attack.mitre.org/software/S0105) and other Active Directory utilities to enumerate hosts; they have also used `nltest.exe /dclist` to retrieve a list of domain controllers.[^8] [^3]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [FIN8](https://attack.mitre.org/groups/G0061) has deployed ransomware such as [Ragnar Locker](https://attack.mitre.org/software/S0481), White Rabbit, and attempted to execute Noberus on compromised networks.[^5]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has retrieved a list of trusted domains by using `nltest.exe /domain_trusts`.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [FIN8](https://attack.mitre.org/groups/G0061) has deleted Registry keys during post compromise cleanup activities.[^8]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [FIN8](https://attack.mitre.org/groups/G0061) has used a malicious framework designed to impersonate the lsass.exe/vmtoolsd.exe token.[^3] [^5]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [FIN8](https://attack.mitre.org/groups/G0061) has used the [Ping](https://attack.mitre.org/software/S0097) command to check connectivity to actor-controlled C2 servers.[^6]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FIN8](https://attack.mitre.org/groups/G0061)'s malicious spearphishing payloads use WMI to launch malware and spawn `cmd.exe` execution. [FIN8](https://attack.mitre.org/groups/G0061) has also used WMIC and the [Impacket](https://attack.mitre.org/software/S0357) suite for lateral movement, as well as during and post compromise cleanup activities.[^7] [^3] [^8] [^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^8]  |
| [[Impacket\|S0357]] | Impacket | [^3] [^6]  |
| [[dsquery\|S0105]] | dsquery | [^8]  |
| [[Nltest\|S0359]] | Nltest | [^3]  |
| [[Ping\|S0097]] | Ping | [^6]  |
| [[PsExec\|S0029]] | PsExec | [^5]  |
| [[Sardonic\|S1085]] | Sardonic | [^6] [^5]  |
| [[BADHATCH\|S1081]] | BADHATCH | [^9]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | [^5]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [^1]  |
| [[PUNCHTRACK\|S0197]] | PUNCHTRACK | [^1]  |



## References

[^1]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^2]: FIN8


[^3]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^4]: Syssphinx


[^5]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^6]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^7]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)


[^8]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^9]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


