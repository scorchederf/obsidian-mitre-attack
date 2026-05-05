---
aliases: 
    - S1070
    
mitre-attack: https://attack.mitre.org/software/S1070
---

## S1070

[Black Basta](https://attack.mitre.org/software/S1070) is ransomware written in C++ that has been offered within the ransomware-as-a-service (RaaS) model since at least April 2022; there are variants that target Windows and VMWare ESXi servers. [Black Basta](https://attack.mitre.org/software/S1070) operations have included the double extortion technique where in addition to demanding ransom for decrypting the files of targeted organizations the cyber actors also threaten to post sensitive information to a leak site if the ransom is not paid. [Black Basta](https://attack.mitre.org/software/S1070) affiliates have targeted multiple high-value organizations, with the largest number of victims based in the U.S. Based on similarities in TTPs, leak sites, payment sites, and negotiation tactics, security researchers assess the [Black Basta](https://attack.mitre.org/software/S1070) RaaS operators could include current or former members of the [Conti](https://attack.mitre.org/software/S0575) group.[^13] [^1] [^2] [^6] [^9] [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Black Basta](https://attack.mitre.org/software/S1070) can delete shadow copies using vssadmin.exe.[^2] [^8] [^4] [^6] [^9] [^1] [^13] [^3] [^3] [^10]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Black Basta](https://attack.mitre.org/software/S1070) can collect system boot configuration and CPU information.[^2] [^8]  |
| [[Code Signing\|T1553.002]] | Code Signing | The [Black Basta](https://attack.mitre.org/software/S1070) dropper has been digitally signed with a certificate issued by Akeo Consulting for legitimate executables used for creating bootable USB drives.[^10]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Black Basta](https://attack.mitre.org/software/S1070) can make a random number of calls to the `kernel32.beep` function to hinder log analysis.[^10]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [Black Basta](https://attack.mitre.org/software/S1070) has set the desktop wallpaper on victims' machines to display a ransom note.[^2] [^5] [^8] [^4] [^6] [^9] [^1] [^13] [^10]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Black Basta](https://attack.mitre.org/software/S1070) can use LDAP queries to connect to AD and iterate over connected workstations.[^10]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Black Basta](https://attack.mitre.org/software/S1070) has modified the Registry to enable itself to run in safe mode, to change the icons and file extensions for encrypted files, and to add the malware path for persistence.[^2] [^8] [^4] [^9] [^1] [^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Black Basta](https://attack.mitre.org/software/S1070) can enumerate specific files for encryption.[^8] [^6] [^9] [^12] [^1] [^13] [^3] [^10]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Black Basta](https://attack.mitre.org/software/S1070) can encrypt files with the ChaCha20 cypher and using a multithreaded process to increase speed.[^2] [^5] [^8] [^9] [^12] [^1] [^13] [^3] [^10]  [Black Basta](https://attack.mitre.org/software/S1070) has also encrypted files while the victim system is in safe mode, appending `.basta` upon completion.[^4]   |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | The [Black Basta](https://attack.mitre.org/software/S1070) dropper can check system flags, CPU registers, CPU instructions, process timing, system libraries, and APIs to determine if a debugger is present.[^10]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Black Basta](https://attack.mitre.org/software/S1070) has been downloaded and executed from malicious Excel files.[^4] [^3]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | The [Black Basta](https://attack.mitre.org/software/S1070) binary can use `chmod` to gain full permissions to targeted files.[^12]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Black Basta](https://attack.mitre.org/software/S1070) can use `cmd.exe` to enable shadow copy deletion.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Black Basta](https://attack.mitre.org/software/S1070) can check whether the service name `FAX` is present.[^8]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Black Basta](https://attack.mitre.org/software/S1070) can enumerate volumes.[^2] [^8]  |
| [[System Checks\|T1497.001]] | System Checks | [Black Basta](https://attack.mitre.org/software/S1070) can check system flags and libraries, process timing, and API's to detect code emulation or sandboxing.[^13] [^10]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Black Basta](https://attack.mitre.org/software/S1070) has used PowerShell scripts for discovery and to execute files over the network.[^4] [^3] [^9]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Black Basta](https://attack.mitre.org/software/S1070) can create a new service to establish persistence.[^2] [^6]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Black Basta](https://attack.mitre.org/software/S1070) has used WMI to execute files over the network.[^9]  |
| [[Safe Mode Boot\|T1688]] | Safe Mode Boot | [Black Basta](https://attack.mitre.org/software/S1070) can reboot victim machines in safe mode with networking via `bcdedit /set safeboot network`.[^2] [^8] [^4] [^6] [^13]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Black Basta](https://attack.mitre.org/software/S1070) had added data prior to the Portable Executable (PE) header to prevent automatic scanners from identifying the payload.[^10]  |
| [[Native API\|T1106]] | Native API | [Black Basta](https://attack.mitre.org/software/S1070) has the ability to use native APIs for numerous functions including discovery and defense evasion.[^2] [^8] [^6] [^10] [^4]   |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Black Basta](https://attack.mitre.org/software/S1070) has used `ShellExecuteA` to shut down and restart the victim system.[^4]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | The [Black Basta](https://attack.mitre.org/software/S1070) dropper has mimicked an application for creating USB bootable drivers.[^10]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Black Basta](https://attack.mitre.org/software/S1070) will check for the presence of a hard-coded mutex `dsajdhas.0` before executing.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Black Basta](https://attack.mitre.org/software/S1070) has established persistence by creating a new service named `FAX` after deleting the legitimate service by the same name.[^2] [^8] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Storm-1811\|G1046]] | Storm-1811 |



## References

[^1]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)


[^2]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)


[^3]: [Trend Micro Black Basta Spotlight September 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)


[^4]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)


[^5]: [BlackBerry Black Basta May 2022](https://blogs.blackberry.com/en/2022/05/black-basta-rebrand-of-conti-or-something-new)


[^6]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)


[^7]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^8]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)


[^9]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)


[^10]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)


[^11]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^12]: [Uptycs Black Basta ESXi June 2022](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)


[^13]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)


