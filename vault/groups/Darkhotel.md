---
aliases: 
    - Darkhotel
    - DUBNIUM
    - Zigzag Hail
mitre-attack: https://attack.mitre.org/groups/G0012
---

## G0012

[Darkhotel](https://attack.mitre.org/groups/G0012) is a suspected South Korean threat group that has targeted victims primarily in East Asia since at least 2004. The group's name is based on cyber espionage operations conducted via hotel Internet networks against traveling executives and other select guests. [Darkhotel](https://attack.mitre.org/groups/G0012) has also conducted spearphishing campaigns and infected victims through peer-to-peer and file sharing networks.[^5] [^1] [^10] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has searched for anti-malware strings and anti-virus processes running on the system.[^1] [^3]   |
| [[User Activity Based Checks\|T1497.002]] | User Activity Based Checks | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that repeatedly checks the mouse cursor position to determine if a real user is on the system.[^11]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Darkhotel](https://attack.mitre.org/groups/G0012) has obfuscated code using RC4, XOR, and RSA.[^1] [^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Darkhotel](https://attack.mitre.org/groups/G0012) has used AES-256 and 3DES for C2 communications.[^7]  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | [Darkhotel](https://attack.mitre.org/groups/G0012) used a virus that propagates by infecting executables stored on shared drives.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the hostname, OS version, service pack version, and the processor architecture from the victim’s machine.[^1] [^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Darkhotel](https://attack.mitre.org/groups/G0012) has used a keylogger.[^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Darkhotel](https://attack.mitre.org/groups/G0012) has sent spearphishing emails with malicious RAR and .LNK attachments.[^1] [^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) malware can collect a list of running processes on a system.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Darkhotel](https://attack.mitre.org/groups/G0012) has decrypted strings and imports using RC4 during execution.[^1] [^7]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Darkhotel](https://attack.mitre.org/groups/G0012) used embedded iframes on hotel login portals to redirect selected victims to download malware.[^5]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Darkhotel](https://attack.mitre.org/groups/G0012)'s selective infector modifies executables stored on removable media as a method of spreading across computers.[^5]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Darkhotel](https://attack.mitre.org/groups/G0012) malware has employed just-in-time decryption of strings to evade sandbox detection.[^11]  |
| [[System Checks\|T1497.001]] | System Checks | [Darkhotel](https://attack.mitre.org/groups/G0012) malware has used a series of checks to determine if it's being analyzed; checks include the length of executable names, if a filename ends with `.Md5.exe`, and if the program is executed from the root of the C:\ drive, as well as checks for sandbox-related libraries.[^11] [^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) malware can obtain system time from a compromised host.[^11]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Darkhotel](https://attack.mitre.org/groups/G0012) has used code-signing certificates on its malware that are either forged due to weak keys or stolen. [Darkhotel](https://attack.mitre.org/groups/G0012) has also stolen certificates and signed backdoors and downloaders with them.[^5] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the IP address and network adapter information from the victim’s machine.[^1] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that searched for files with specific patterns.[^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Darkhotel](https://attack.mitre.org/groups/G0012) has dropped an mspaint.lnk shortcut to disk which launches a shell script that downloads and executes a file.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that is disguised as a Secure Shell (SSH) tool.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Darkhotel](https://attack.mitre.org/groups/G0012) has used first-stage payloads that download additional malware from C2 servers.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Darkhotel](https://attack.mitre.org/groups/G0012) has been known to establish persistence by adding programs to the Run Registry key.[^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Darkhotel](https://attack.mitre.org/groups/G0012) has exploited Adobe Flash vulnerability CVE-2015-8651 for execution.[^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Darkhotel](https://attack.mitre.org/groups/G0012) has sent spearphishing emails in an attempt to lure users into clicking on a malicious attachments.[^1] [^7]  |




## References

[^1]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^2]: Darkhotel


[^3]: [Microsoft DUBNIUM June 2016](https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/)


[^4]: Zigzag Hail


[^5]: [Kaspersky Darkhotel](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf)


[^6]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^7]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^8]: [Microsoft DUBNIUM Flash June 2016](https://www.microsoft.com/security/blog/2016/06/20/reverse-engineering-dubniums-flash-targeting-exploit/)


[^9]: DUBNIUM


[^10]: [Microsoft Digital Defense FY20 Sept 2020](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RWxPuf)


[^11]: [Lastline DarkHotel Just In Time Decryption Nov 2015](https://www.lastline.com/labsblog/defeating-darkhotel-just-in-time-decryption/)


