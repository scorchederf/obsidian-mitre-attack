---
aliases: 
    - BlackByte
    - Hecamede
mitre-attack: https://attack.mitre.org/groups/G1043
---

## G1043

[BlackByte](https://attack.mitre.org/groups/G1043) is a ransomware threat actor operating since at least 2021. [BlackByte](https://attack.mitre.org/groups/G1043) is associated with several versions of ransomware also labeled [BlackByte Ransomware](https://attack.mitre.org/software/S1180). [BlackByte](https://attack.mitre.org/groups/G1043) ransomware operations initially used a common encryption key allowing for the development of a universal decryptor, but subsequent versions such as [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) use more robust encryption mechanisms. [BlackByte](https://attack.mitre.org/groups/G1043) is notable for operations targeting critical infrastructure entities among other targets across North America.[^4] [^6] [^7] [^5] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used various system commands and tools to pull system information during operations.[^4] [^7] [^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Arp](https://attack.mitre.org/software/S0099) to pull system network information and identify connected devices.[^4] [^5]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as NetScan to enumerate network services in victim environments.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BlackByte](https://attack.mitre.org/groups/G1043) has transferred tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) to victim environments from file sharing and hosting websites.[^5]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated Active Directory information and trust relationships during operations.[^4] [^5]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [BlackByte](https://attack.mitre.org/groups/G1043) modified firewall rules on victim machines to enable remote system discovery.[^6] [^7]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [BlackByte](https://attack.mitre.org/groups/G1043) masqueraded configuration files containing encryption keys as PNG files.[^4]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [BlackByte](https://attack.mitre.org/groups/G1043) created scheduled tasks for payload execution.[^4] [^6]  |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | [BlackByte](https://attack.mitre.org/groups/G1043) constructed a valid authentication token following Microsoft Exchange exploitation to allow for follow-on privileged command execution.[^5]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BlackByte](https://attack.mitre.org/groups/G1043) deleted ransomware executables post-encryption.[^6] [^7] [^5] [^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [BlackByte](https://attack.mitre.org/groups/G1043) modified multiple services on victim machines to enable encryption operations.[^7]  [BlackByte](https://attack.mitre.org/groups/G1043) has installed tools such as AnyDesk as a service on victim machines.[^5]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [BlackByte](https://attack.mitre.org/groups/G1043) has used RDP to access other hosts within victim networks.[^5] [^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [BlackByte](https://attack.mitre.org/groups/G1043) disabled security tools such as Windows Defender and the Raccine anti-ransomware tool during operations.[^4] [^6] [^3]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) identified system language settings to determine follow-on execution.[^6]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [BlackByte](https://attack.mitre.org/groups/G1043) compressed data collected from victim environments prior to exfiltration.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [BlackByte](https://attack.mitre.org/groups/G1043) executed ransomware using the Windows command shell.[^4]  |
| [[Domain Account\|T1136.002]] | Domain Account | [BlackByte](https://attack.mitre.org/groups/G1043) created privileged domain accounts during intrusions.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BlackByte](https://attack.mitre.org/groups/G1043) performed Registry modifications to escalate privileges and disable security tools.[^6] [^3]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [BlackByte](https://attack.mitre.org/groups/G1043) used process hollowing for defense evasion purposes.[^5]  |
| [[Internal Defacement\|T1491.001]] | Internal Defacement | [BlackByte](https://attack.mitre.org/groups/G1043) left ransom notes in all directories where encryption takes place.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BlackByte](https://attack.mitre.org/groups/G1043) collected victim device information then transmitted this via HTTP POST to command and control infrastructure.[^5]  |
| [[Domain Account\|T1087.002]] | Domain Account | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as [AdFind](https://attack.mitre.org/software/S0552) to identify and enumerate domain accounts.[^5]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [BlackByte](https://attack.mitre.org/groups/G1043) transfered tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and the AnyDesk remote access tool during operations using SMB shares.[^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [BlackByte](https://attack.mitre.org/groups/G1043) staged encryption keys on virtual private servers operated by the adversary.[^4]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [BlackByte](https://attack.mitre.org/groups/G1043) exploited vulnerabilities such as ProxyLogon and ProxyShell for initial access to victim environments.[^4] [^6] [^7] [^5]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [BlackByte](https://attack.mitre.org/groups/G1043) has staged tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) at public file sharing and hosting sites.[^5]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BlackByte](https://attack.mitre.org/groups/G1043) resized and deleted volume shadow copy files to prevent system recovery after encryption.[^6] [^7]  |
| [[Query Registry\|T1012]] | Query Registry | [BlackByte](https://attack.mitre.org/groups/G1043) queried registry values to determine system language settings.[^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [BlackByte](https://attack.mitre.org/groups/G1043) used encoded PowerShell commands during operations.[^4]  [BlackByte](https://attack.mitre.org/groups/G1043) has used remote PowerShell commands in victim networks.[^5]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BlackByte](https://attack.mitre.org/groups/G1043) transmitted collected victim host information via HTTP POST to command and control infrastructure.[^5]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials from victim systems.[^6] [^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [BlackByte](https://attack.mitre.org/groups/G1043) created malicious services for ransomware execution.[^7] [^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated network shares on victim devices.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BlackByte](https://attack.mitre.org/groups/G1043) has encoded commands in base64-encoded sections concatenated together in PowerShell.[^4]  [BlackByte](https://attack.mitre.org/groups/G1043) uses PowerShell commands to disable Windows Defender.[^6]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [BlackByte](https://attack.mitre.org/groups/G1043) has exploited CVE-2024-37085 in VMWare ESXi software for authentication bypass and subsequent privilege escalation.[^3]  |
| [[Web Shell\|T1505.003]] | Web Shell | [BlackByte](https://attack.mitre.org/groups/G1043) has used ASPX web shells following exploitation of vulnerabilities in services such as Microsoft Exchange.[^6] [^5]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [BlackByte](https://attack.mitre.org/groups/G1043) has gained access to victim environments through legitimate VPN credentials.[^3]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [BlackByte](https://attack.mitre.org/groups/G1043) has used services such as `anonymfiles.com` and `file.io` to exfiltrate victim data.[^6]  |
| [[Process Injection\|T1055]] | Process Injection | [BlackByte](https://attack.mitre.org/groups/G1043) has injected [Cobalt Strike](https://attack.mitre.org/software/S0154) into `wuauclt.exe` during intrusions.[^6]  [BlackByte](https://attack.mitre.org/groups/G1043) has injected ransomware into `svchost.exe` before encryption.[^7]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [BlackByte](https://attack.mitre.org/groups/G1043) used SMB file shares to distribute payloads throughout victim networks, including BlackByte ransomware variants during wormable operations.[^6] [^5] [^3]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | [BlackByte](https://attack.mitre.org/groups/G1043) captured credentials for or impersonated domain administration users.[^5] [^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BlackByte](https://attack.mitre.org/groups/G1043) has used Registry Run keys for persistence.[^5]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BlackByte](https://attack.mitre.org/groups/G1043) stopped execution if identified language settings on victim machines was Russian or one of several language associated with former Soviet republics.[^6]  [BlackByte](https://attack.mitre.org/groups/G1043) has used ransomware variants requiring a key passed on the command line for the malware to execute.[^3]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [BlackByte](https://attack.mitre.org/groups/G1043) has encrypted victim files for ransom. Early versions of BlackByte ransomware used a common key for encryption, but later versions use unique keys per victim.[^4] [^6] [^7] [^5] [^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated installed security products during operations.[^5]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as AnyDesk in victim environments.[^6] [^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [BlackByte](https://attack.mitre.org/groups/G1043) used WMI to delete Volume Shadow Copies on victim machines.[^4]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Arp](https://attack.mitre.org/software/S0099) to identify remotely-connected devices.[^4] [^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Arp\|S0099]] | Arp | [BlackByte](https://attack.mitre.org/groups/G1043) used [Arp](https://attack.mitre.org/software/S0099) to identify connected hosts in victim networks.[^4]  |
| [[Mimikatz\|S0002]] | Mimikatz | [BlackByte](https://attack.mitre.org/groups/G1043) has used [Mimikatz](https://attack.mitre.org/software/S0002) for credential dumping during operations.[^5]  |
| [[AdFind\|S0552]] | AdFind | [BlackByte](https://attack.mitre.org/groups/G1043) used [AdFind](https://attack.mitre.org/software/S0552) during operations.[^7] [^5]  |
| [[PsExec\|S0029]] | PsExec | [BlackByte](https://attack.mitre.org/groups/G1043) has used [PsExec](https://attack.mitre.org/software/S0029) to remotely execute payloads during wormable ransomware execution.[^5]  |
| [[BlackByte 2.0 Ransomware\|S1181]] | BlackByte 2.0 Ransomware | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) is ransomware uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations and is a replacement for [BlackByte Ransomware](https://attack.mitre.org/software/S1180).[^5]  |
| [[Exbyte\|S1179]] | Exbyte | [BlackByte](https://attack.mitre.org/groups/G1043) used [Exbyte](https://attack.mitre.org/software/S1179) for automated file collection and exfiltration.[^7] [^5]  |
| [[BlackByte Ransomware\|S1180]] | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is ransomware uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations prior to 2023.[^5] [^2]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [BlackByte](https://attack.mitre.org/groups/G1043) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) as a post-exploitation tool.[^6] [^5]  |



## References

[^1]: Hecamede


[^2]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^3]: [Cisco BlackByte 2024](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)


[^4]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^5]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^6]: [Picus BlackByte 2022](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)


[^7]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


