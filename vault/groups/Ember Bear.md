---
aliases: 
    - Ember Bear
    - UNC2589
    - Bleeding Bear
    - DEV-0586
    - Cadet Blizzard
    - Frozenvista
    - UAC-0056
mitre-attack: https://attack.mitre.org/groups/G1003
---

## G1003

[Ember Bear](https://attack.mitre.org/groups/G1003) is a Russian state-sponsored cyber espionage group that has been active since at least 2020, linked to Russia's General Staff Main Intelligence Directorate (GRU) 161st Specialist Training Center (Unit 29155).[^9]  [Ember Bear](https://attack.mitre.org/groups/G1003) has primarily focused operations against Ukrainian government and telecommunication entities, but has also operated against critical infrastructure entities in Europe and the Americas.[^3]  [Ember Bear](https://attack.mitre.org/groups/G1003) conducted the [WhisperGate](https://attack.mitre.org/software/S0689) destructive wiper attacks against Ukraine in early 2022.[^8] [^11] [^9]  There is some confusion as to whether [Ember Bear](https://attack.mitre.org/groups/G1003) overlaps with another Russian-linked entity referred to as [Saint Bear](https://attack.mitre.org/groups/G1031). At present available evidence strongly suggests these are distinct activities with different behavioral profiles.[^3] [^10] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as Nmap and MASSCAN for remote service discovery.[^9]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Ember Bear](https://attack.mitre.org/groups/G1003) gathers credential material from target systems, such as SSH keys, to facilitate access to victim environments.[^3]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Ember Bear](https://attack.mitre.org/groups/G1003) has configured multi-hop proxies via ProxyChains within victim environments.[^9]  |
| [[Email Collection\|T1114]] | Email Collection | [Ember Bear](https://attack.mitre.org/groups/G1003) attempts to collect mail from accessed systems and servers.[^3] [^9]  |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Ember Bear](https://attack.mitre.org/groups/G1003) uses services such as IVPN, SurfShark, and Tor to add anonymization to operations.[^3]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Ember Bear](https://attack.mitre.org/groups/G1003) has compressed collected data prior to exfiltration.[^9]  |
| [[Masquerading\|T1036]] | Masquerading | [Ember Bear](https://attack.mitre.org/groups/G1003) has renamed the legitimate Sysinternals tool procdump to alternative names such as `dump64.exe` to evade detection.[^3]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Ember Bear](https://attack.mitre.org/groups/G1003) has used publicly available tools such as MASSCAN and Acunetix for vulnerability scanning of public-facing infrastructure.[^9]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Ember Bear](https://attack.mitre.org/groups/G1003) has used virtual private servers (VPSs) to host tools, perform reconnaissance, exploit victim infrastructure, and as a destination for data exfiltration.[^9]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Ember Bear](https://attack.mitre.org/groups/G1003) has enumerated SECURITY and SYSTEM log files during intrusions.[^9]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Ember Bear](https://attack.mitre.org/groups/G1003) gains initial access to victim environments by exploiting external-facing services. Examples include exploitation of CVE-2021-26084 in Confluence servers; CVE-2022-41040, ProxyShell, and other vulnerabilities in Microsoft Exchange; and multiple vulnerabilities in open-source platforms such as content management systems.[^3] [^9]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) have used VPNs both for initial access to victim environments and for persistence within them following compromise.[^9]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Ember Bear](https://attack.mitre.org/groups/G1003) engages in mass collection from compromised systems during intrusions.[^3]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Ember Bear](https://attack.mitre.org/groups/G1003) has used various non-standard ports for C2 communication.[^9]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Ember Bear](https://attack.mitre.org/groups/G1003) deletes files related to lateral movement to avoid detection.[^3]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Ember Bear](https://attack.mitre.org/groups/G1003) retrieves follow-on payloads direct from adversary-owned infrastructure for deployment on compromised hosts.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Ember Bear](https://attack.mitre.org/groups/G1003) uses socket-based tunneling utilities for command and control purposes such as NetCat and Go Simple Tunnel (GOST). These tunnels are used to push interactive command prompts over the created sockets.[^3]  [Ember Bear](https://attack.mitre.org/groups/G1003) has also used reverse TCP connections from Meterpreter installations to communicate back with C2 infrastructure.[^9]  |
| [[Video Capture\|T1125]] | Video Capture | [Ember Bear](https://attack.mitre.org/groups/G1003) has exfiltrated images from compromised IP cameras.[^9]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Ember Bear](https://attack.mitre.org/groups/G1003) has used ProxyChains to tunnel protocols to internal networks.[^9]  |
| [[Brute Force\|T1110]] | Brute Force | [Ember Bear](https://attack.mitre.org/groups/G1003) used the `su-bruteforce` tool to brute force specific users using the `su` command.[^9]  |
| [[Malware\|T1588.001]] | Malware | [Ember Bear](https://attack.mitre.org/groups/G1003) has acquired malware and related tools from dark web forums.[^9]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Ember Bear](https://attack.mitre.org/groups/G1003) has conducted password spraying against Outlook Web Access (OWA) infrastructure to identify valid user names and passwords.[^9]  |
| [[Scanning IP Blocks\|T1595.001]] | Scanning IP Blocks | [Ember Bear](https://attack.mitre.org/groups/G1003) has targeted IP ranges for vulnerability scanning related to government and critical infrastructure organizations.[^9]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Ember Bear](https://attack.mitre.org/groups/G1003) deploys web shells following initial access for either follow-on command execution or protocol tunneling. Example web shells used by [Ember Bear](https://attack.mitre.org/groups/G1003) include P0wnyshell, reGeorg, [P.A.S. Webshell](https://attack.mitre.org/software/S0598), and custom variants of publicly-available web shell examples.[^3] [^9]  |
| [[Establish Accounts\|T1585]] | Establish Accounts | [Ember Bear](https://attack.mitre.org/groups/G1003) has created accounts on dark web forums to obtain various tools and malware.[^9]  |
| [[External Defacement\|T1491.002]] | External Defacement | [Ember Bear](https://attack.mitre.org/groups/G1003) is linked to the defacement of several Ukrainian organization websites.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Ember Bear](https://attack.mitre.org/groups/G1003) uses remotely scheduled tasks to facilitate remote command execution on victim machines.[^3]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) has used exploits for vulnerabilities such as MS17-010, also known as `Eternal Blue`, during operations.[^9]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Ember Bear](https://attack.mitre.org/groups/G1003) has used PowerShell commands to gather information from compromised systems,  such as email servers.[^9]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Ember Bear](https://attack.mitre.org/groups/G1003) modifies registry values for anti-forensics and defense evasion purposes.[^3]  |
| [[DNS\|T1071.004]] | DNS | [Ember Bear](https://attack.mitre.org/groups/G1003) has used DNS tunnelling tools, such as dnscat/2 and Iodine, for C2 purposes.[^9]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Ember Bear](https://attack.mitre.org/groups/G1003) has used pass-the-hash techniques for lateral movement in victim environments.[^9]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate information from victim environments to cloud storage such as `mega.nz`.[^9]  |
| [[Exploits\|T1588.005]] | Exploits | [Ember Bear](https://attack.mitre.org/groups/G1003) has obtained exploitation scripts against publicly-disclosed vulnerabilities from public repositories.[^9]  |
| [[Supply Chain Compromise\|T1195]] | Supply Chain Compromise | [Ember Bear](https://attack.mitre.org/groups/G1003) has compromised information technology providers and software developers providing services to targets of interest, building initial access to ultimate victims at least in part through compromise of service providers that work with the victim organizations.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Ember Bear](https://attack.mitre.org/groups/G1003) gathers victim system information such as enumerating the volume of a given device or extracting system and security event logs for analysis.[^3] [^9]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [Ember Bear](https://attack.mitre.org/groups/G1003) conducted destructive operations against victims, including disk structure wiping, via the [WhisperGate](https://attack.mitre.org/software/S0689) malware in Ukraine.[^3]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Ember Bear](https://attack.mitre.org/groups/G1003) has used exploits to enable follow-on execution of frameworks such as Meterpreter.[^9]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Ember Bear](https://attack.mitre.org/groups/G1003) has renamed tools to match legitimate utilities, such as renaming GOST tunneling instances to `java` in victim environments.[^9]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Ember Bear](https://attack.mitre.org/groups/G1003) has dumped configuration settings in accessed IP cameras including plaintext credentials.[^9]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Ember Bear](https://attack.mitre.org/groups/G1003) uses legitimate Sysinternals tools such as procdump to dump LSASS memory.[^3] [^9]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Ember Bear](https://attack.mitre.org/groups/G1003) has used WMI execution with password hashes for command execution and lateral movement.[^9]  |
| [[Remote Services\|T1021]] | Remote Services | [Ember Bear](https://attack.mitre.org/groups/G1003) uses valid network credentials gathered through credential harvesting to move laterally within victim networks, often employing the [Impacket](https://attack.mitre.org/software/S0357) framework to do so.[^3]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [Ember Bear](https://attack.mitre.org/groups/G1003) has used frameworks such as [Impacket](https://attack.mitre.org/software/S0357) to dump LSA secrets for credential capture.[^9]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Ember Bear](https://attack.mitre.org/groups/G1003) acquires victim credentials by extracting registry hives such as the Security Account Manager through commands such as `reg save`.[^3] [^9]  |
| [[Default Accounts\|T1078.001]] | Default Accounts | [Ember Bear](https://attack.mitre.org/groups/G1003) has abused default user names and passwords in externally-accessible IP cameras for initial access.[^9]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Ember Bear](https://attack.mitre.org/groups/G1003) has used tools such as NMAP for remote system discovery and enumeration in victim environments.[^9]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[BloodHound\|S0521]] | BloodHound | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [BloodHound](https://attack.mitre.org/software/S0521) to profile Active Directory environments.[^9]  |
| [[Impacket\|S0357]] | Impacket | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [Impacket](https://attack.mitre.org/software/S0357) for lateral movement and process execution in victim environments.[^3] [^9]  |
| [[ngrok\|S0508]] | ngrok | [Ember Bear](https://attack.mitre.org/groups/G1003) used [ngrok](https://attack.mitre.org/software/S0508) during intrusions against Ukrainian victims.[^3]  |
| [[Rclone\|S1040]] | Rclone | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate information from victim environments.[^9]  |
| [[Responder\|S0174]] | Responder | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [Responder](https://attack.mitre.org/software/S0174) in intrusions.[^9]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [Ember Bear](https://attack.mitre.org/groups/G1003) used [CrackMapExec](https://attack.mitre.org/software/S0488) during intrusions.[^9]  |
| [[PsExec\|S0029]] | PsExec | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [PsExec](https://attack.mitre.org/software/S0029) through frameworks such as [Impacket](https://attack.mitre.org/software/S0357) for remote command execution.[^9]  |
| [[reGeorg\|S1187]] | reGeorg | [^3]  |
| [[P.A.S. Webshell\|S0598]] | P.A.S. Webshell | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [P.A.S. Webshell](https://attack.mitre.org/software/S0598) during intrusions.[^9]  |
| [[WhisperGate\|S0689]] | WhisperGate | [Ember Bear](https://attack.mitre.org/groups/G1003) is associated with [WhisperGate](https://attack.mitre.org/software/S0689) use against multiple victims in Ukraine.[^3] [^8] [^11]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Ember Bear](https://attack.mitre.org/groups/G1003) has used [Saint Bot](https://attack.mitre.org/software/S1018) during operations, but is distinct from the threat actor [Saint Bear](https://attack.mitre.org/groups/G1031).[^9]  |



## References

[^1]: Bleeding Bear


[^2]: Cadet Blizzard


[^3]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^4]: UNC2589


[^5]: Frozenvista


[^6]: UAC-0056


[^7]: DEV-0586


[^8]: [CrowdStrike Ember Bear Profile March 2022](https://www.crowdstrike.com/blog/who-is-ember-bear/)


[^9]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^10]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^11]: [Mandiant UNC2589 March 2022](https://www.mandiant.com/resources/russia-invasion-ukraine-retaliation)


