---
aliases: 
    - S0483
    
mitre-attack: https://attack.mitre.org/software/S0483
---

## S0483

[IcedID](https://attack.mitre.org/software/S0483) is a modular banking malware designed to steal financial information that has been observed in the wild since at least 2017.  [IcedID](https://attack.mitre.org/software/S0483)  has been downloaded by [Emotet](https://attack.mitre.org/software/S0367) in multiple campaigns.[^9] [^10] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [IcedID](https://attack.mitre.org/software/S0483) has manipulated Keitaro Traffic Direction System to filter researcher and sandbox traffic.[^8]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [IcedID](https://attack.mitre.org/software/S0483) can inject a [Cobalt Strike](https://attack.mitre.org/software/S0154) beacon into cmd.exe via process hallowing.[^5]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [IcedID](https://attack.mitre.org/software/S0483) used the following command to check the country/language of the active console: <br>` cmd.exe /c chcp >&2`.[^5] <br> |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [IcedID](https://attack.mitre.org/software/S0483) used [Nltest](https://attack.mitre.org/software/S0359) during initial discovery.[^2] [^5]  |
| [[Msiexec\|T1218.007]] | Msiexec | [IcedID](https://attack.mitre.org/software/S0483) can inject itself into a suspended msiexec.exe process to send beacons to C2 while appearing as a normal msi application. [^10]  [IcedID](https://attack.mitre.org/software/S0483) has also used msiexec.exe to deploy the [IcedID](https://attack.mitre.org/software/S0483) loader.[^8]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [IcedID](https://attack.mitre.org/software/S0483) has cloned legitimate websites/applications to distribute the malware.[^8]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [IcedID](https://attack.mitre.org/software/S0483) has exfiltrated collected data via HTTPS.[^2]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [IcedID](https://attack.mitre.org/software/S0483) has the ability to identify Workgroup membership.[^9]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [IcedID](https://attack.mitre.org/software/S0483) has created a scheduled task to establish persistence.[^10] [^5] [^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [IcedID](https://attack.mitre.org/software/S0483) has used rundll32.exe to execute the [IcedID](https://attack.mitre.org/software/S0483) loader.[^8] [^5]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [IcedID](https://attack.mitre.org/software/S0483) has modified legitimate .dll files to include malicious code.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [IcedID](https://attack.mitre.org/software/S0483) has been executed through Word and Excel files with malicious embedded macros and through ISO and LNK files that execute the malicious DLL.[^10] [^5] [^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [IcedID](https://attack.mitre.org/software/S0483) can identify AV products on an infected host using the following command:<br>` WMIC.exe WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get * /Format:List`.[^2] [^5]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [IcedID](https://attack.mitre.org/software/S0483) has embedded malicious functionality in a legitimate DLL file.[^8] <br><br> |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [IcedID](https://attack.mitre.org/software/S0483) has utilzed encrypted binaries and base64 encoded strings.[^10]  |
| [[Native API\|T1106]] | Native API | [IcedID](https://attack.mitre.org/software/S0483) has called `ZwWriteVirtualMemory`, `ZwProtectVirtualMemory`, `ZwQueueApcThread`, and `NtResumeThread` to inject itself into a remote process.[^10]  |
| [[Steganography\|T1027.003]] | Steganography | [IcedID](https://attack.mitre.org/software/S0483) has embedded binaries within RC4 encrypted .png files.[^10]  |
| [[Domain Account\|T1087.002]] | Domain Account | [IcedID](https://attack.mitre.org/software/S0483) can query LDAP and can use built-in `net` commands to identify additional users on the network to infect.[^9] [^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [IcedID](https://attack.mitre.org/software/S0483) has used WMI to execute binaries.[^10] [^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [IcedID](https://attack.mitre.org/software/S0483) has used obfuscated VBA string expressions.[^10]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [IcedID](https://attack.mitre.org/software/S0483) has used `ZwQueueApcThread` to inject itself into remote processes.[^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [IcedID](https://attack.mitre.org/software/S0483) has the ability to download additional modules and a configuration file from C2.[^9] [^10] [^5] [^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [IcedID](https://attack.mitre.org/software/S0483) used the `ipconfig /all` command and a batch script to gather network information.[^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [IcedID](https://attack.mitre.org/software/S0483) has been delivered via phishing e-mails with malicious attachments.[^10] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [IcedID](https://attack.mitre.org/software/S0483) has used HTTPS in communications with C2.[^10] [^5] [^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [IcedID](https://attack.mitre.org/software/S0483) has used the `net view /all` command to show available shares.[^5]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [IcedID](https://attack.mitre.org/software/S0483) has used web injection attacks to redirect victims to spoofed sites designed to harvest banking and other credentials.  [IcedID](https://attack.mitre.org/software/S0483) can use a self signed TLS certificate in connection with the spoofed site and simultaneously maintains a live connection with the legitimate site to display the correct URL and certificates in the browser.[^9] [^10]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [IcedID](https://attack.mitre.org/software/S0483) has established persistence by creating a Registry run key.[^9]  |
| [[Software Packing\|T1027.002]] | Software Packing | [IcedID](https://attack.mitre.org/software/S0483) has packed and encrypted its loader module.[^10]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [IcedID](https://attack.mitre.org/software/S0483) has the ability to identify the computer name and OS version on a compromised host.[^9] [^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [IcedID](https://attack.mitre.org/software/S0483) has used SSL and TLS in communications with C2.[^9] [^10]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA551\|G0127]] | TA551 |
| [[TA578\|G1038]] | TA578 |



## References

[^1]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^2]: [DFIR_Sodinokibi_Ransomware](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)


[^3]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^4]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^5]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^6]: [Secureworks GOLD CABIN](https://www.secureworks.com/research/threat-profiles/gold-cabin)


[^7]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^8]: [Trendmicro_IcedID](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)


[^9]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)


[^10]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)


