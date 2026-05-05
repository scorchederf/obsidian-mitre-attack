---
aliases: 
    - S1240
    
mitre-attack: https://attack.mitre.org/software/S1240
---

## S1240

[RedLine Stealer](https://attack.mitre.org/software/S1240) is an information-stealer malware variant first identified in 2020.[^5] [^1] [^6]   [RedLine Stealer](https://attack.mitre.org/software/S1240) is a Malware as a Service (MaaS) and was reportedly sold as either a one-time purchase or a monthly subscription service.[^5] [^4]    Information obtained from [RedLine Stealer](https://attack.mitre.org/software/S1240) has been known to be sold on the deep and dark web to Initial Access Brokers (IABs), who use or resell the stolen credentials for further intrusions.[^2] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Code Signing\|T1553.002]] | Code Signing | [RedLine Stealer](https://attack.mitre.org/software/S1240) has used both valid certificates and self-signed digital certificates to appear legitimate.[^5]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [RedLine Stealer](https://attack.mitre.org/software/S1240) can disable security software and update services.[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) has obtained the username from the victim’s machine.[^1] [^6] [^4]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) has identified installed antivirus software on the system.[^2] [^4]  |
| [[Query Registry\|T1012]] | Query Registry | [RedLine Stealer](https://attack.mitre.org/software/S1240) can query the Windows Registry.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RedLine Stealer](https://attack.mitre.org/software/S1240) can capture screenshots on a compromised host.[^3] [^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [RedLine Stealer](https://attack.mitre.org/software/S1240) malware has been executed through the download of malicious files.[^5] [^2] [^4]  [RedLine Stealer](https://attack.mitre.org/software/S1240) has also lured users to install malware with an Install Wizard interface.[^3]  |
| [[Financial Theft\|T1657]] | Financial Theft | [RedLine Stealer](https://attack.mitre.org/software/S1240) has collected data from cryptocurrency wallets and harvested credit cards details from browsers.[^5] [^2] [^1] [^6] [^4]  |
| [[Local Account\|T1087.001]] | Local Account | [RedLine Stealer](https://attack.mitre.org/software/S1240) has collected account information from the victim’s machine.[^1] [^6]  |
| [[Masquerading\|T1036]] | Masquerading | [RedLine Stealer](https://attack.mitre.org/software/S1240) malware has masqueraded as legitimate software such as "PDF Converter Software" which has been distributed through poisoned search engine results often resembling legitimate software lures with the combination of typo squatted domains.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [RedLine Stealer](https://attack.mitre.org/software/S1240) has used obfuscation tools such as DNGuard and Boxed App to pack their code.[^5]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) has gathered detailed information about victims’ systems, such as IP addresses, and geolocation.[^5] [^2] [^1]  [RedLine Stealer](https://attack.mitre.org/software/S1240) has also checked the IP from where it was being executed and leveraged an opensource geolocation IP-lookup service. [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [RedLine Stealer](https://attack.mitre.org/software/S1240) has encrypted and encoded configuration data with Base64 and XOR functions.[^6]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) can retrieve system default language and time zone.[^6]  |
| [[Web Service\|T1102]] | Web Service | [RedLine Stealer](https://attack.mitre.org/software/S1240) has leveraged legitimate file sharing web services to host malicious payloads.[^1] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) can enumeate information about victims’ systems including IP addresses.[^2]  |
| [[Lua\|T1059.011]] | Lua | [RedLine Stealer](https://attack.mitre.org/software/S1240) malware has leveraged Lua bytecode to perform malicious behavior.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [RedLine Stealer](https://attack.mitre.org/software/S1240) has collected data stored locally including chat logs and files associated with chat services such as Steam, Discord, and Telegram.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has the ability download additional payloads.[^2] [^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [RedLine Stealer](https://attack.mitre.org/software/S1240) has used Base64 to encode command and control traffic.[^3]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [RedLine Stealer](https://attack.mitre.org/software/S1240) has stolen browser cookies and settings.[^5] [^2] [^1] [^6]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) can collect information from browsers and browser extensions.[^6]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [RedLine Stealer](https://attack.mitre.org/software/S1240) has obtained credentials from VPN services, FTP clients and Instant Messenger (IM)/Chat clients.[^2] [^1] [^6]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [RedLine Stealer](https://attack.mitre.org/software/S1240) was designed to steal sensitive information from web browsers, including credit card details, saved credentials, and autocomplete data.[^5]  [RedLine Stealer](https://attack.mitre.org/software/S1240) can also gather credentials from several browsers.[^2] [^1] [^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RedLine Stealer](https://attack.mitre.org/software/S1240) has decoded its payload prior to execution.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [RedLine Stealer](https://attack.mitre.org/software/S1240) has sent victim data to its C2 server or RedLine panel server.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [RedLine Stealer](https://attack.mitre.org/software/S1240) has been installed via MSI Installer.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) can collect information about the local system.[^2] [^1] [^6] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RedLine Stealer](https://attack.mitre.org/software/S1240) has utilized HTTP for C2 communications.[^3]  [RedLine Stealer](https://attack.mitre.org/software/S1240) has also conducted C2 communications to hardcoded C2 servers over HTTPS.[^5] [^6]  [RedLine Stealer](https://attack.mitre.org/software/S1240) has  leveraged SOAP protocol for C2 communications.[^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [RedLine Stealer](https://attack.mitre.org/software/S1240) has built in settings to not operate based on geolocation or country of the victim host.[^5] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [RedLine Stealer](https://attack.mitre.org/software/S1240) has achieved persistence via scheduled tasks.[^3]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [RedLine Stealer](https://attack.mitre.org/software/S1240) has an anti-sandbox technique that requires the malware to consistently check with the C2 server, if the communication fails [RedLine Stealer](https://attack.mitre.org/software/S1240) will not continue execution.[^6]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [RedLine Stealer](https://attack.mitre.org/software/S1240) has obfuscated scripts within text files used in execution.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RedLine Stealer](https://attack.mitre.org/software/S1240) has executed windows [cmd](https://attack.mitre.org/software/S0106) using `ErrorHandler.cmd` to create scheduled tasks.[^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [RedLine Stealer](https://attack.mitre.org/software/S1240) can get a list of programs on the victim device.[^6]  |




## References

[^1]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)


[^2]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)


[^3]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)


[^4]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)


[^5]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)


[^6]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)


