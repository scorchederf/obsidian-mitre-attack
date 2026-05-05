---
aliases: 
    - S9001
    
mitre-attack: https://attack.mitre.org/software/S9001
---

## S9001

[SystemBC](https://attack.mitre.org/software/S9001) is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.[SystemBC](https://attack.mitre.org/software/S9001) executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. [SystemBC](https://attack.mitre.org/software/S9001) was first detected in 2018, and has been used by [Wizard Spider](https://attack.mitre.org/groups/G0102) since at least 2020, and by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2022.[^5] [^10] [^8] [^1] [^11] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [SystemBC](https://attack.mitre.org/software/S9001) has executed a copy of itself as a scheduled task with the `start` command. The copy of [SystemBC](https://attack.mitre.org/software/S9001) has random file and directory names within the ProgramData directory.[^10] [^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SystemBC](https://attack.mitre.org/software/S9001) has used hidden scheduled tasks to execute PowerShell commands by adding the following: `-WindowStyle Hidden -ep bypass -file `.[^10]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SystemBC](https://attack.mitre.org/software/S9001) has used `cmd.exe` to execute VBS scripts, BAT scripts and CMD scripts.[^10]  |
| [[Local Account\|T1087.001]] | Local Account | [SystemBC](https://attack.mitre.org/software/S9001) has collected the Windows account username on the victim machine.[^10]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SystemBC](https://attack.mitre.org/software/S9001) has leveraged the time of the device to create a text file with a filename that uses the function of `uniqid(time()).‘.txt`, consisting of the 10 character UNIX timestamp and 13 hexadecimal characters.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SystemBC](https://attack.mitre.org/software/S9001) has downloaded additional files for execution on the victim’s machine.[^10] [^5]  The server component of [SystemBC](https://attack.mitre.org/software/S9001) has the ability to send additional files to victim machines.[^5]  |
| [[Native API\|T1106]] | Native API | [SystemBC](https://attack.mitre.org/software/S9001) has utilized native Windows API functions such as `EnumWindows`and `GetVolumeInformationA` during discovery activities.[^10]    |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SystemBC](https://attack.mitre.org/software/S9001) has the ability to decrypt RC4 encrypted packets and to decode obfuscated data before C2 communication.[^1]  Additionally, [SystemBC](https://attack.mitre.org/software/S9001) has decrypted its config file that was encoded with XOR and a hardcoded 40-byte key.[^11]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [SystemBC](https://attack.mitre.org/software/S9001) has encoded with XOR and encrypted with RC4 its beacon.[^11]  |
| [[DNS\|T1071.004]] | DNS | [SystemBC](https://attack.mitre.org/software/S9001) has used DNS servers to resolve .bit domains to C2 infrastructure.[^9]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | The server component of [SystemBC](https://attack.mitre.org/software/S9001) has used various TCP ports for C2 communication.[^5]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [SystemBC](https://attack.mitre.org/software/S9001) has utilized the `-WindowStyle Hidden -ep bypass -file `to conceal PowerShell windows.[^10]    |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SystemBC](https://attack.mitre.org/software/S9001) has collected username  , build number and serial number, then sent the information to the C2 server.[^10] [^1]  [SystemBC](https://attack.mitre.org/software/S9001) has also gathered device name, operating system, and processor type.[^9]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [SystemBC](https://attack.mitre.org/software/S9001) has used multiple proxy layers, such as SOCKS5 and [Tor](https://attack.mitre.org/software/S0183), for C2 communication.[^9] [^10] [^5] [^8]  [SystemBC](https://attack.mitre.org/software/S9001) has also leveraged [Tor](https://attack.mitre.org/software/S0183) for encrypting and concealing C2 traffic.[^10]  The server component of [SystemBC](https://attack.mitre.org/software/S9001) has used SOCKS5 for C2 communication.[^5]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [SystemBC](https://attack.mitre.org/software/S9001) has checked if the last characters of DNS server names end in .bit before initializing C2 communication.[^9]  [SystemBC](https://attack.mitre.org/software/S9001) has identified running processes associated with anti-virus solutions to include `a2guard.exe` to determine whether it executes or not.[^10]    |
| [[Process Discovery\|T1057]] | Process Discovery | [SystemBC](https://attack.mitre.org/software/S9001) has the ability to enumerate running processes.[^10]    |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [SystemBC](https://attack.mitre.org/software/S9001) has downloaded a text file into memory and set the area of memory via the VirtualProtect call. Then, [SystemBC](https://attack.mitre.org/software/S9001) has executed the file via the CreateThread call.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SystemBC](https://attack.mitre.org/software/S9001) has encrypted its C2 traffic with RC4.[^9] [^10]  |
| [[Delay Execution\|T1678]] | Delay Execution | [SystemBC](https://attack.mitre.org/software/S9001) has leveraged the Sleep functions before and after commands to ensure execution using the hexadecimal values within commands to include `Sleep(0x2710u)` that waits 10 seconds, and `Sleep(0xEA60u)` for 60 seconds.[^10]    |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [SystemBC](https://attack.mitre.org/software/S9001) has used raw TCP on non-standard ports, such as 4044, for C2 communications and for HTTP communications, which include downloading binaries.[^10] [^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [SystemBC](https://attack.mitre.org/software/S9001) has leveraged VBScript to execute malicious code.[^10]    |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[Fox Kitten\|G0117]] | Fox Kitten |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [AhnLab_SystemBC_Apr2022](https://asec.ahnlab.com/en/33600/)


[^2]: Coroxy


[^3]: [FortinetEtAl_IranianIntrusion_Mar2025](https://www.fortinet.com/content/dam/fortinet/assets/reports/report-incident-response-middle-east.pdf)


[^4]: [Broadcom_SystemBCCoroxy_Nov2023](https://www.broadcom.com/support/security-center/protection-bulletin/systembc-coroxy-continuous-activities)


[^5]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)


[^6]: [Microsoft_Coroxy_Oct2020](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win32/Coroxy.A&ThreatID=2147766831)


[^7]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^8]: [BlackBasta](https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/)


[^9]: [HarmonProofpoint_SystemBC_Aug2019](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)


[^10]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^11]: [Lumen_SystemBC_Sept2025](https://blog.lumen.com/systembc-bringing-the-noise/)


[^12]: [Microsoft_PistachioTempest_Jan2024](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/pistachio-tempest)


