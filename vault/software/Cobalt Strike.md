---
aliases: 
    - S0154
    
mitre-attack: https://attack.mitre.org/software/S0154
---

## S0154

[Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.[^52] <br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).[^52] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Fronting\|T1090.004]] | Domain Fronting | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to accept a value for HTTP Host Header to enable domain fronting.[^7]  |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use `sudo` to run a command.[^7]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use self signed Java applets to execute signed applet attacks.[^26] [^7]  |
| [[JavaScript\|T1059.007]] | JavaScript | The [Cobalt Strike](https://attack.mitre.org/software/S0154) System Profiler can use JavaScript to perform reconnaissance actions.[^26]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Cobalt Strike](https://attack.mitre.org/software/S0154) can start a VNC-based remote desktop server and tunnel the connection through the already established C2 channel.[^52] [^15]  |
| [[Native API\|T1106]] | Native API | [Cobalt Strike](https://attack.mitre.org/software/S0154)'s Beacon payload is capable of running shell commands without `cmd.exe` and PowerShell commands without `powershell.exe`[^52] [^26] [^7]  [Cobalt Strike](https://attack.mitre.org/software/S0154) can also use `CreateThreadpoolWait`, `SetThreadpoolWait`, and `MessageBoxA` for sandbox evasion and execution of embedded payloads in memory.[^79]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Cobalt Strike](https://attack.mitre.org/software/S0154) can perform pass the hash.[^6]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use known credentials to run commands and spawn processes as a domain user account.[^52] [^82] [^7]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [Cobalt Strike](https://attack.mitre.org/software/S0154) includes a capability to modify the Beacon payload to eliminate known signatures or unpacking methods.[^52] [^7]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use a number of known techniques to bypass Windows UAC.[^52] [^7]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can determine the NetBios name and  the IP addresses of targets machines including domain controllers.[^22] [^7]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use [PsExec](https://attack.mitre.org/software/S0029) to execute a payload on a remote host. It can also use Service Control Manager to start new services.[^52] [^6] [^7]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Cobalt Strike](https://attack.mitre.org/software/S0154) can collect data from a local system.[^6] [^7]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to load DLLs via reflective injection.[^26] [^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Cobalt Strike](https://attack.mitre.org/software/S0154) can track key presses with a keylogger module.[^52] [^80] [^7]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [Cobalt Strike](https://attack.mitre.org/software/S0154) can download a hosted "beacon" payload using [BITSAdmin](https://attack.mitre.org/software/S0190).[^69] [^26] [^7]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use process hollowing for execution.[^6] [^7]  |
| [[Software Discovery\|T1518]] | Software Discovery | The [Cobalt Strike](https://attack.mitre.org/software/S0154) System Profiler can discover applications through the browser and identify the version of Java the target has.[^7]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use known credentials to run commands and spawn processes as a local user account.[^52] [^82]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Cobalt Strike](https://attack.mitre.org/software/S0154) can be configured to have commands relayed over a peer-to-peer network of infected hosts. This can be used to limit the number of egress points, or provide access to a host without direct internet access.[^52] [^7]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Cobalt Strike](https://attack.mitre.org/software/S0154) can exploit vulnerabilities such as MS14-058.[^6] [^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Cobalt Strike](https://attack.mitre.org/software/S0154)'s Beacon payload is capable of capturing screenshots.[^52] [^80] [^7]  |
| [[Process Argument Spoofing\|T1564.010]] | Process Argument Spoofing | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use spoof arguments in spawned processes that execute beacon commands.[^7]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Cobalt Strike](https://attack.mitre.org/software/S0154) can modify Registry values within `HKEY_CURRENT_USER\Software\Microsoft\Office\<Excel Version>\Excel\Security\AccessVBOM\` to enable the execution of additional code.[^26]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Cobalt Strike](https://attack.mitre.org/software/S0154) can identify targets by querying account groups on a domain contoller.[^7]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can produce a sessions report from compromised hosts.[^26]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Cobalt Strike](https://attack.mitre.org/software/S0154) can leverage the HTTP protocol for C2 communication, while hiding the actual data in either an HTTP header, URI parameter, the transaction body, or appending it to the URI.[^7]  [Cobalt Strike](https://attack.mitre.org/software/S0154) has also added Host: ocsp.verisign.com to HTTP headers to mimic Online Certificate Status Protocol (OCSP) traffic.[^79]  |
| [[Parent PID Spoofing\|T1134.004]] | Parent PID Spoofing | [Cobalt Strike](https://attack.mitre.org/software/S0154) can spawn processes with alternate PPIDs.[^82] [^7]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Cobalt Strike](https://attack.mitre.org/software/S0154) can steal access tokens from exiting processes.[^52] [^7]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Cobalt Strike](https://attack.mitre.org/software/S0154) can install a new service.[^6]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use VBA to perform execution.[^6] [^82] [^26]  |
| [[Process Injection\|T1055]] | Process Injection | [Cobalt Strike](https://attack.mitre.org/software/S0154) can inject a variety of payloads into processes dynamically chosen by the adversary.[^52] [^7] [^84]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can enumerate services on compromised hosts.[^7]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Cobalt Strike](https://attack.mitre.org/software/S0154) can timestomp any files or payloads placed on a target machine to help them blend in.[^52] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can explore files on a compromised system.[^7]  |
| [[DNS\|T1071.004]] | DNS | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use a custom command and control protocol that can be encapsulated in DNS. All protocols use their standard assigned ports.[^52] [^26] [^7] 	 |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Cobalt Strike](https://attack.mitre.org/software/S0154) can set its Beacon payload to reach out to the C2 server on an arbitrary and random interval.[^52]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use `net localgroup` to list local groups on a system.[^7]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Cobalt Strike](https://attack.mitre.org/software/S0154) can execute a payload on a remote host with PowerShell. This technique does not write any data to disk.[^52] [^22]  [Cobalt Strike](https://attack.mitre.org/software/S0154) can also use [PowerSploit](https://attack.mitre.org/software/S0194) and other scripting frameworks to perform execution.[^6] [^82] [^26] [^7]  |
| [[SSH\|T1021.004]] | SSH | [Cobalt Strike](https://attack.mitre.org/software/S0154) can SSH to a remote service.[^6] [^7]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Cobalt Strike](https://attack.mitre.org/software/S0154)'s `execute-assembly` command can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^7]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) uses the native Windows Network Enumeration APIs to interrogate and discover targets in a Windows Active Directory network.[^52] [^26] [^7]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Cobalt Strike](https://attack.mitre.org/software/S0154) can spawn a job to inject into LSASS memory and dump password hashes.[^7]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to use Smart Applet attacks to disable the Java SecurityManager sandbox.[^26] [^7]  |
| [[Query Registry\|T1012]] | Query Registry | [Cobalt Strike](https://attack.mitre.org/software/S0154) can query `HKEY_CURRENT_USER\Software\Microsoft\Office\<Excel Version>\Excel\Security\AccessVBOM\`  to determine if the security setting for restricting default programmatic access is enabled.[^26] [^7]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Cobalt Strike](https://attack.mitre.org/software/S0154) can determine if the user on an infected machine is in the admin or domain admin group.[^22]  |
| [[User Activity Based Checks\|T1497.002]] | User Activity Based Checks | The [Cobalt Strike](https://attack.mitre.org/software/S0154) loader can use the `MessageBoxA` API to prompt for user interaction as an anti-sandbox measure.[^79]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Cobalt Strike](https://attack.mitre.org/software/S0154) will break large data sets into smaller chunks for exfiltration.[^52]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can perform port scans from an infected host.[^52] [^26] [^7]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154) can query shared drives on the local system.[^6]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use a custom command and control protocol that can be encapsulated in HTTP or HTTPS. All protocols use their standard assigned ports.[^52] [^26] [^7] [^74] [^17]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use RSA asymmetric encryption with PKCS1 padding to encrypt data sent to the C2 server.[^26]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Cobalt Strike](https://attack.mitre.org/software/S0154) can perform browser pivoting and inject into a user's browser to inherit cookies, authenticated HTTP sessions, and client SSL certificates.[^52] [^7]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Cobalt Strike](https://attack.mitre.org/software/S0154) can deobfuscate shellcode using a rolling XOR and decrypt metadata from Beacon sessions.[^26] [^7]  The [Cobalt Strike](https://attack.mitre.org/software/S0154) loader component can also decrypt the .bss section of the Beacon binary prior to execution.[^79]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Cobalt Strike](https://attack.mitre.org/software/S0154) uses a custom command and control protocol that is encapsulated in HTTP, HTTPS, or DNS. In addition, it conducts peer-to-peer communication over Windows named pipes encapsulated in the SMB protocol. All protocols use their standard assigned ports.[^52] [^7]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use `WinRM` to execute a payload on a remote host.[^52] [^7]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to use AES-256 symmetric encryption in CBC mode with HMAC-SHA-256 to encrypt task commands and XOR to encrypt shell code and configuration data.[^26]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Cobalt Strike](https://attack.mitre.org/software/S0154) can be configured to use TCP, ICMP, and UDP for C2 communications.[^26] [^7]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use Base64, URL-safe Base64, or NetBIOS encoding in its C2 traffic.[^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Cobalt Strike](https://attack.mitre.org/software/S0154) can deliver additional payloads to victim machines.[^26] [^7]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use Window admin shares (C$ and ADMIN$) for lateral movement.[^6] [^30]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use `rundll32.exe` to load DLL from the command line.[^7] [^84] [^30]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Cobalt Strike](https://attack.mitre.org/software/S0154) can conduct peer-to-peer communication over Windows named pipes encapsulated in the SMB protocol. All protocols use their standard assigned ports.[^52] [^26]  |
| [[Python\|T1059.006]] | Python | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use Python to perform execution.[^6] [^82] [^26] [^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use WMI to deliver a payload to a remote host.[^52] [^7] [^84]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Cobalt Strike](https://attack.mitre.org/software/S0154) can recover hashed passwords.[^52]  |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | [Cobalt Strike](https://attack.mitre.org/software/S0154) can make tokens from known credentials.[^52]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Cobalt Strike](https://attack.mitre.org/software/S0154) can exploit Oracle Java vulnerabilities for execution, including CVE-2011-3544, CVE-2013-2465, CVE-2012-4681, and CVE-2013-2460.[^26] [^7]  |
| [[Distributed Component Object Model\|T1021.003]] | Distributed Component Object Model | [Cobalt Strike](https://attack.mitre.org/software/S0154) can deliver Beacon payloads for lateral movement by leveraging remote COM execution.[^32]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Cobalt Strike](https://attack.mitre.org/software/S0154)'s Beacon payload can collect information on process details.[^52] [^26] [^7]  |
| [[Office Template Macros\|T1137.001]] | Office Template Macros | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to use an Excel Workbook to execute additional code by enabling Office to trust macros and execute code without user permission.[^26]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cobalt Strike](https://attack.mitre.org/software/S0154) uses a command-line interface to interact with systems.[^6] [^26] [^7] [^30]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Cobalt Strike](https://attack.mitre.org/software/S0154) can hash functions to obfuscate calls to the Windows API and use a public/private key pair to encrypt Beacon session metadata.[^26] [^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[Storm-1811\|G1046]] | Storm-1811 |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[APT32\|G0050]] | APT32 |
| [[ToddyCat\|G1022]] | ToddyCat |
| [[APT19\|G0073]] | APT19 |
| [[FIN6\|G0037]] | FIN6 |
| [[TA505\|G0092]] | TA505 |
| [[CopyKittens\|G0052]] | CopyKittens |
| [[DarkHydrus\|G0079]] | DarkHydrus |
| [[Play\|G1040]] | Play |
| [[Earth Lusca\|G1006]] | Earth Lusca |
| [[FIN7\|G0046]] | FIN7 |
| [[Mustard Tempest\|G1020]] | Mustard Tempest |
| [[APT41\|G0096]] | APT41 |
| [[menuPass\|G0045]] | menuPass |
| [[Aquatic Panda\|G0143]] | Aquatic Panda |
| [[Cobalt Group\|G0080]] | Cobalt Group |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[BlackByte\|G1043]] | BlackByte |
| [[Leviathan\|G0065]] | Leviathan |
| [[APT29\|G0016]] | APT29 |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[APT37\|G0067]] | APT37 |
| [[LuminousMoth\|G1014]] | LuminousMoth |
| [[Chimera\|G0114]] | Chimera |
| [[Indrik Spider\|G0119]] | Indrik Spider |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [DFIR Ryuk in 5 Hours October 2020](https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/)


[^2]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^3]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^4]: [Secureworks IRON RITUAL USAID Phish May 2021](https://www.secureworks.com/blog/usaid-themed-phishing-campaign-leverages-us-elections-lure)


[^5]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)


[^6]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)


[^7]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^8]: [Volexity OceanLotus Nov 2017](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)


[^9]: [TrendMicro Cobalt Group Nov 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/cobalt-spam-runs-use-macros-cve-2017-8759-exploit/)


[^10]: [Picus BlackByte 2022](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)


[^11]: [Dell SecureWorks BRONZE STARLIGHT Profile](https://www.secureworks.com/research/threat-profiles/bronze-starlight)


[^12]: [Crowdstrike Global Threat Report Feb 2018](https://crowdstrike.lookbookhq.com/global-threat-report-2018-web/cs-2018-global-threat-report)


[^13]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^14]: [FBI Flash FIN7 USB](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)


[^15]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^16]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^17]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^18]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^19]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^20]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^21]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^22]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^23]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^24]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^25]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^26]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^27]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^28]: [Crowdstrike EvilCorp March 2021](https://www.crowdstrike.com/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)


[^29]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^30]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^31]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^32]: [Cobalt Strike DCOM Jan 2017](https://blog.cobaltstrike.com/2017/01/24/scripting-matt-nelsons-mmc20-application-lateral-movement-technique/)


[^33]: [RiskIQ Cobalt Jan 2018](https://web.archive.org/web/20190508170147/https://www.riskiq.com/blog/labs/cobalt-group-spear-phishing-russian-banks/)


[^34]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^35]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^36]: [Proofpoint Cobalt June 2017](https://www.proofpoint.com/us/threat-insight/post/microsoft-word-intruder-integrates-cve-2017-0199-utilized-cobalt-group-target)


[^37]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^38]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^39]: [Crowdstrike MUSTANG PANDA June 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)


[^40]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^41]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^42]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^43]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^44]: [Anomali MUSTANG PANDA October 2019](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)


[^45]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^46]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^47]: [RiskIQ Cobalt Nov 2017](https://web.archive.org/web/20190508170630/https://www.riskiq.com/blog/labs/cobalt-strike/)


[^48]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^49]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^50]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^51]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^52]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)


[^53]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^54]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


[^55]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^56]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^57]: [Secureworks BRONZE PRESIDENT December 2019](https://www.secureworks.com/research/bronze-president-targets-ngos)


[^58]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^59]: [McAfee Dianxun March 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-dianxun.pdf)


[^60]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^61]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^62]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^63]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^64]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^65]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^66]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^67]: [NCC Group TA505](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)


[^68]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^69]: [CobaltStrike Scripted Web Delivery](https://www.cobaltstrike.com/help-scripted-web-delivery)


[^70]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)


[^71]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^72]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^73]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^74]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^75]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^76]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^77]: [ESET T3 Threat Report 2021](https://www.welivesecurity.com/wp-content/uploads/2022/02/eset_threat_report_t32021.pdf)


[^78]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^79]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^80]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)


[^81]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^82]: [CobaltStrike Daddy May 2017](https://web.archive.org/web/20171009220105/https://blog.cobaltstrike.com/2017/05/23/cobalt-strike-3-8-whos-your-daddy/)


[^83]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^84]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^85]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


[^86]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


