---
aliases: 
    - S0363
    
mitre-attack: https://attack.mitre.org/software/S0363
---

## S0363

[Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.[^9] [^14] [^18] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Video Capture\|T1125]] | Video Capture | [Empire](https://attack.mitre.org/software/S0363) can capture webcam data on Windows and macOS systems.[^14]  |
| [[Distributed Component Object Model\|T1021.003]] | Distributed Component Object Model | [Empire](https://attack.mitre.org/software/S0363) can utilize `Invoke-DCOM` to leverage remote COM execution for lateral movement.[^14]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Empire](https://attack.mitre.org/software/S0363) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^14] [^19]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Empire](https://attack.mitre.org/software/S0363) can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^14] [^11]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Empire](https://attack.mitre.org/software/S0363) leverages PowerShell for the majority of its client-side agent tasks. [Empire](https://attack.mitre.org/software/S0363) also contains the ability to conduct PowerShell remoting with the `Invoke-PSRemoting` module.[^14] [^9]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Empire](https://attack.mitre.org/software/S0363) has modules for enumerating domain trusts.[^14]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Empire](https://attack.mitre.org/software/S0363) includes keylogging capabilities for Windows, Linux, and macOS systems.[^14]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Empire](https://attack.mitre.org/software/S0363) has the ability to obfuscate commands using `Invoke-Obfuscation`.[^14]  |
| [[Local Account\|T1136.001]] | Local Account | [Empire](https://attack.mitre.org/software/S0363) has a module for creating a local user if permissions allow.[^14]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Empire](https://attack.mitre.org/software/S0363) is capable of capturing screenshots on Windows and macOS systems.[^14]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Empire](https://attack.mitre.org/software/S0363) can perform port scans from an infected host.[^14]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Empire](https://attack.mitre.org/software/S0363) can use various modules to search for files containing passwords.[^14]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Empire](https://attack.mitre.org/software/S0363) can ZIP directories on the target system.[^14]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Empire](https://attack.mitre.org/software/S0363) can use `New-GPOImmediateTask` to modify a GPO that will install and execute a malicious [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).[^14]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Empire](https://attack.mitre.org/software/S0363) can send data gathered from a target through the command and control channel.[^14] [^11]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Empire](https://attack.mitre.org/software/S0363) can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^14] [^11]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Empire](https://attack.mitre.org/software/S0363) can harvest clipboard data on both Windows and macOS systems.[^14]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Empire](https://attack.mitre.org/software/S0363) can exploit vulnerabilities such as MS16-032 and MS16-135.[^14]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Empire](https://attack.mitre.org/software/S0363) has the ability to automatically send collected data back to the threat actors' C2.[^11]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [Empire](https://attack.mitre.org/software/S0363) can leverage WMI debugging to remotely replace binaries like sethc.exe, Utilman.exe, and Magnify.exe with cmd.exe.[^14]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Empire](https://attack.mitre.org/software/S0363) can automatically gather the username, domain name, machine name, and other information from a compromised system.[^11]  |
| [[Keychain\|T1555.001]] | Keychain | [Empire](https://attack.mitre.org/software/S0363) uses the command `/usr/bin/security dump-keychain -d` to read the keychain credential.[^7]  |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [Empire](https://attack.mitre.org/software/S0363) includes various modules for enumerating Group Policy.[^14]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.[^14] [^4]  |
| [[Security Support Provider\|T1547.005]] | Security Support Provider | [Empire](https://attack.mitre.org/software/S0363) can enumerate Security Support Providers (SSPs) as well as utilize [PowerSploit](https://attack.mitre.org/software/S0194)'s `Install-SSP` and `Invoke-Mimikatz` to install malicious SSPs and log authentication events.[^14]  |
| [[SSH\|T1021.004]] | SSH | [Empire](https://attack.mitre.org/software/S0363) contains modules for executing commands over SSH as well as in-memory VNC agent injection.[^14]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Empire](https://attack.mitre.org/software/S0363) uses [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-Kerberoast` to request service tickets and return crackable ticket hashes.[^14]  |
| [[SID-History Injection\|T1134.005]] | SID-History Injection | [Empire](https://attack.mitre.org/software/S0363) can add a SID-History to a user if on a domain controller.[^14]  |
| [[Path Interception by Unquoted Path\|T1574.009]] | Path Interception by Unquoted Path | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit unquoted path vulnerabilities.[^14]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Empire](https://attack.mitre.org/software/S0363) can modify the registry run keys `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` and `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^14]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Empire](https://attack.mitre.org/software/S0363) can find shared drives on the local system.[^14]  |
| [[Path Interception by Search Order Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit search order hijacking vulnerabilities.[^14]  |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use golden tickets.[^14]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Empire](https://attack.mitre.org/software/S0363) has a limited number of built-in modules for exploiting remote SMB, JBoss, and Jenkins servers.[^14]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Empire](https://attack.mitre.org/software/S0363) can use [PsExec](https://attack.mitre.org/software/S0029) to execute a payload on a remote host.[^14]  |
| [[Exfiltration to Code Repository\|T1567.001]] | Exfiltration to Code Repository | [Empire](https://attack.mitre.org/software/S0363) can use GitHub for data exfiltration.[^14]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Empire](https://attack.mitre.org/software/S0363) includes various modules for finding files of interest on hosts and network shares.[^14]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [Empire](https://attack.mitre.org/software/S0363) contains some modules that leverage API hooking to carry out tasks, such as netripper.[^14]  |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit path interception opportunities in the PATH environment variable.[^14]  |
| [[Native API\|T1106]] | Native API | [Empire](https://attack.mitre.org/software/S0363) contains a variety of enumeration modules that have an option to use API calls to carry out tasks.[^14]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Empire](https://attack.mitre.org/software/S0363) can use WMI to deliver a payload to a remote host.[^14]   |
| [[Process Injection\|T1055]] | Process Injection | [Empire](https://attack.mitre.org/software/S0363) contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^14]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Empire](https://attack.mitre.org/software/S0363) can perform pass the hash attacks.[^14]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Empire](https://attack.mitre.org/software/S0363) has the ability to gather browser data such as bookmarks and visited sites.[^14]  |
| [[MSBuild\|T1127.001]] | MSBuild | [Empire](https://attack.mitre.org/software/S0363) can use built-in modules to abuse trusted utilities like MSBuild.exe.[^14] <br> |
| [[Private Keys\|T1552.004]] | Private Keys | [Empire](https://attack.mitre.org/software/S0363) can use modules like `Invoke-SessionGopher` to extract private key and session information.[^14]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Empire](https://attack.mitre.org/software/S0363) can use Dropbox for data exfiltration.[^14]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Empire](https://attack.mitre.org/software/S0363) can conduct command and control over protocols like HTTP and HTTPS.[^14]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Empire](https://attack.mitre.org/software/S0363) can use [PowerSploit](https://attack.mitre.org/software/S0194)'s `Invoke-TokenManipulation` to manipulate access tokens.[^14]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Empire](https://attack.mitre.org/software/S0363) can be used to conduct packet captures on target hosts.[^14]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Empire](https://attack.mitre.org/software/S0363) has the ability to collect emails on a target system.[^14]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Empire](https://attack.mitre.org/software/S0363) has modules for executing scripts.[^14]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Empire](https://attack.mitre.org/software/S0363) can use Dropbox and GitHub for C2.[^14]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Empire](https://attack.mitre.org/software/S0363) can use modules that extract passwords from common web browsers such as Firefox and Chrome.[^14]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Empire](https://attack.mitre.org/software/S0363) can enumerate antivirus software on the target.[^14]  |
| [[Local Account\|T1087.001]] | Local Account | [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.[^14]  |
| [[Dylib Hijacking\|T1574.004]] | Dylib Hijacking | [Empire](https://attack.mitre.org/software/S0363) has a dylib hijacker module that generates a malicious dylib given the path to a legitimate dylib of a vulnerable application.[^14]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Empire](https://attack.mitre.org/software/S0363) can enumerate the current network connections of a host.[^14]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Empire](https://attack.mitre.org/software/S0363) has modules to interact with the Windows task scheduler.[^14]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Empire](https://attack.mitre.org/software/S0363) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.[^14]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Empire](https://attack.mitre.org/software/S0363) can use TLS to encrypt its C2 channel.[^14]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [Empire](https://attack.mitre.org/software/S0363) can use `Invoke-RunAs` to make tokens.[^14]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Empire](https://attack.mitre.org/software/S0363) can utilize built-in modules to modify service binaries and restore them to their original state.[^14]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Empire](https://attack.mitre.org/software/S0363) uses a command-line interface to interact with systems.[^14]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Empire](https://attack.mitre.org/software/S0363) can find information about processes running on local and remote systems.[^14] [^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Empire](https://attack.mitre.org/software/S0363) can upload and download to and from a victim machine.[^14]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Empire](https://attack.mitre.org/software/S0363) can timestomp any files or payloads placed on a target machine to help them blend in.[^14]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Empire](https://attack.mitre.org/software/S0363) can persist by modifying a .LNK file to include a backdoor.[^14]  |
| [[DLL\|T1574.001]] | DLL | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit various DLL hijacking opportunities.[^14]  |
| [[Domain Account\|T1136.002]] | Domain Account | [Empire](https://attack.mitre.org/software/S0363) has a module for creating a new domain user if permissions allow.[^14]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Empire](https://attack.mitre.org/software/S0363) can enumerate the username on targeted hosts.[^11]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Empire](https://attack.mitre.org/software/S0363) includes various modules to attempt to bypass UAC for escalation of privileges.[^14]  |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use silver tickets.[^14]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Silence\|G0091]] | Silence |
| [[FIN10\|G0051]] | FIN10 |
| [[Turla\|G0010]] | Turla |
| [[WIRTE\|G0090]] | WIRTE |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[Play\|G1040]] | Play |
| [[Leviathan\|G0065]] | Leviathan |
| [[FIN13\|G1016]] | FIN13 |
| [[APT19\|G0073]] | APT19 |
| [[Indrik Spider\|G0119]] | Indrik Spider |
| [[CopyKittens\|G0052]] | CopyKittens |
| [[HEXANE\|G1001]] | HEXANE |
| [[APT41\|G0096]] | APT41 |
| [[LazyScripter\|G0140]] | LazyScripter |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[APT33\|G0064]] | APT33 |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^2]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^3]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^4]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^5]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^6]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^7]: [Empire Keychain Decrypt](https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/collection/osx/keychaindump_decrypt.py)


[^8]: [Group IB Silence Aug 2019](https://www.group-ib.com/resources/threat-research/silence_2.0.going_global.pdf)


[^9]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^10]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^11]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^12]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^13]: [FireEye FIN10 June 2017](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)


[^14]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^15]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^16]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^17]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^18]: [GitHub ATTACK Empire](https://github.com/dstepanic/attck_empire)


[^19]: [GitHub Inveigh](https://github.com/Kevin-Robertson/Inveigh)


[^20]: [Lab52 WIRTE Apr 2019](https://lab52.io/blog/wirte-group-attacking-the-middle-east/)


[^21]: EmPyre


[^22]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^23]: [ESET Turla August 2018](https://www.welivesecurity.com/wp-content/uploads/2018/08/Eset-Turla-Outlook-Backdoor.pdf)


[^24]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^25]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^26]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^27]: [DHS/CISA Ransomware Targeting Healthcare October 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)


[^28]: PowerShell Empire


[^29]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


