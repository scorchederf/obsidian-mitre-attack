---
aliases: 
    - S0331
    
mitre-attack: https://attack.mitre.org/software/S0331
---

## S0331

[Agent Tesla](https://attack.mitre.org/software/S0331) is a spyware Trojan written for the .NET framework that has been observed since at least 2014.[^1] [^7] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Injection\|T1055]] | Process Injection | [Agent Tesla](https://attack.mitre.org/software/S0331) can inject into known, vulnerable binaries on targeted hosts.[^2]   |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion |  [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to perform anti-sandboxing and anti-virtualization checks.[^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Agent Tesla](https://attack.mitre.org/software/S0331) can steal data from the victim’s clipboard.[^6] [^1] [^8] [^7]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | The primary delivered mechanism for [Agent Tesla](https://attack.mitre.org/software/S0331) is through email phishing messages.[^7]   |
| [[Screen Capture\|T1113]] | Screen Capture | [Agent Tesla](https://attack.mitre.org/software/S0331) can capture screenshots of the victim’s desktop.[^6] [^10] [^1] [^8] [^7]  |
| [[Local Account\|T1087.001]] | Local Account | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect account information from the victim’s machine.[^10]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Agent Tesla](https://attack.mitre.org/software/S0331) can add itself to the Registry as a startup program to establish persistence.[^1] [^2]   |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to extract credentials from configuration or support files.[^2]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Agent Tesla](https://attack.mitre.org/software/S0331) has used wmi queries to gather information from the system.[^7]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Agent Tesla](https://attack.mitre.org/software/S0331) has been executed through malicious e-mail attachments [^7]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Agent Tesla](https://attack.mitre.org/software/S0331) has exploited Office vulnerabilities such as CVE-2017-11882 and CVE-2017-8570 for execution during delivery.[^2]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the IP address of the victim machine and spawn instances of netsh.exe to enumerate wireless settings.[^10] [^2]   |
| [[Regsvcs／Regasm\|T1218.009]] | Regsvcs／Regasm | [Agent Tesla](https://attack.mitre.org/software/S0331) has dropped RegAsm.exe onto systems for performing malicious activity.[^2]   |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the timestamp from the victim’s machine.[^10]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the username from the victim’s machine.[^10] [^1] [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Agent Tesla](https://attack.mitre.org/software/S0331) can download additional files for execution on the victim’s machine.[^6] [^10]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can list the current running processes on the system.[^8]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Agent Tesla](https://attack.mitre.org/software/S0331) can gather credentials from a number of browsers.[^7]   |
| [[Video Capture\|T1125]] | Video Capture | [Agent Tesla](https://attack.mitre.org/software/S0331) can access the victim’s webcam and record video.[^10] [^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Agent Tesla](https://attack.mitre.org/software/S0331) has had its code obfuscated in an apparent attempt to make analysis difficult.[^1]  [Agent Tesla](https://attack.mitre.org/software/S0331) has used the Rijndael symmetric encryption algorithm to encrypt strings.[^3]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to use form-grabbing to extract data from web data forms.[^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Agent Tesla](https://attack.mitre.org/software/S0331) has used HTTP for C2 communications.[^10] [^8]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Agent Tesla](https://attack.mitre.org/software/S0331) has routines for exfiltration over SMTP, FTP, and HTTP.[^6] [^7] [^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Agent Tesla](https://attack.mitre.org/software/S0331) has used `ProcessWindowStyle.Hidden` to hide windows.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Agent Tesla](https://attack.mitre.org/software/S0331) can log keystrokes on the victim’s machine.[^6] [^10] [^8] [^7] [^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Agent Tesla](https://attack.mitre.org/software/S0331)  has achieved persistence via scheduled tasks.[^2]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Agent Tesla](https://attack.mitre.org/software/S0331) has created hidden folders.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to decrypt strings encrypted with the Rijndael symmetric encryption algorithm.[^3]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to steal credentials from FTP clients and wireless profiles.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Agent Tesla](https://attack.mitre.org/software/S0331) has the capability to kill any running analysis processes and AV software.[^8]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the system's computer name and also has the capability to collect information on the processor, memory, OS, and video card from the system.[^1] [^8] [^3]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Agent Tesla](https://attack.mitre.org/software/S0331) can encrypt data with 3DES before sending it over to a C2 server.[^6]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Agent Tesla](https://attack.mitre.org/software/S0331) has used SMTP for C2 communications.[^9] [^8] [^7]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Agent Tesla](https://attack.mitre.org/software/S0331) can achieve persistence by modifying Registry key entries.[^2]   |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Agent Tesla](https://attack.mitre.org/software/S0331) has used process hollowing to create and manipulate processes through sections of unmapped memory by reallocating that space with its malicious code.[^2]   |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [Agent Tesla](https://attack.mitre.org/software/S0331) has the ability to extract credentials from the Registry.[^2]   |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect names and passwords of all Wi-Fi networks to which a device has previously connected.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[SilverTerrier\|G0083]] | SilverTerrier |
| [[TA2541\|G1018]] | TA2541 |



## References

[^1]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)


[^2]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)


[^3]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)


[^4]: Agent Tesla


[^5]: [Unit42 SilverTerrier 2018](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)


[^6]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)


[^7]: [Bitdefender Agent Tesla April 2020](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)


[^8]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)


[^9]: [Cofense Agent Tesla](https://cofense.com/blog/the-rise-of-agent-tesla-understanding-the-notorious-keylogger/)


[^10]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)


[^11]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


