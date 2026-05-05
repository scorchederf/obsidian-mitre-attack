---
aliases: 
    - S1063
    
mitre-attack: https://attack.mitre.org/software/S1063
---

## S1063

[Brute Ratel C4](https://attack.mitre.org/software/S1063) is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. [Brute Ratel C4](https://attack.mitre.org/software/S1063) was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of [Brute Ratel C4](https://attack.mitre.org/software/S1063) was leaked in the cybercriminal underground, leading to its use by threat actors.[^4] [^6] [^7] [^2] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has injected [Latrodectus](https://attack.mitre.org/software/S1160) into the Explorer.exe process on comrpomised hosts.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can create Windows system services for execution.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use cmd.exe for execution.[^6]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WinRM for pivoting.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can take screenshots on compromised hosts.[^6]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can enumerate all processes and locate specific process IDs (PIDs).[^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used encrypted payload files and maintains an encrypted configuration structure in memory.[^6] [^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WMI to move laterally.[^6]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used a payload file named OneDrive.update to appear benign.[^6]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use SMB to pivot in compromised networks.[^6] [^7] [^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to upload files from a compromised system.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to deobfuscate its payload prior to execution.[^6]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use `net group` for discovery on targeted domains.[^5]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.[^6] [^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can detect EDR userland hooks.[^6]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).[^6] [^7]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used Microsoft Word icons to hide malicious LNK files.[^6]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries, `net group "Domain Admins" /domain` and `net user /domain` for discovery.[^6] [^5]  |
| [[Remote Services\|T1021]] | Remote Services | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use RPC for lateral movement.[^6]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used reflective loading to execute malicious DLLs.[^7]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can conduct port scanning against targeted systems.[^6]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.[^6] [^5]  |
| [[Native API\|T1106]] | Native API | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call multiple Windows APIs for execution, to share memory, and defense evasion.[^6] [^7]  |
| [[Web Service\|T1102]] | Web Service | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.[^6]  |
| [[DNS\|T1071.004]] | DNS | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.[^6] [^5]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use TCP for external C2.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can download files to compromised hosts.[^6] [^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call and dynamically resolve hashed APIs.[^6]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call `NtDelayExecution` to pause execution.[^6] [^7]  |
| [[DLL\|T1574.001]] | DLL | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used search order hijacking to load a malicious payload DLL as a dependency to a benign application packaged in the same ISO.[^6]  [Brute Ratel C4](https://attack.mitre.org/software/S1063) has loaded a malicious DLL by spoofing the name of the legitimate Version.DLL and placing it in the same folder as the digitally-signed Microsoft binary OneDriveUpdater.exe.[^6]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can decode Kerberos 5 tickets and convert it to hashcat format for subsequent cracking.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has gained execution through users opening malicious documents.[^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use HTTPS and HTTPS for C2 communication.[^6] [^5]  |




## References

[^1]: [Rapid7 Fake W2 July 2024](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)


[^2]: [SANS Brute Ratel October 2022](https://www.sans.org/blog/cracked-brute-ratel-c4-framework-proliferates-across-the-cybercriminal-underground/)


[^3]: BRc4


[^4]: [Dark Vortex Brute Ratel C4](https://bruteratel.com/)


[^5]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^6]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^7]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)


