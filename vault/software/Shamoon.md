---
aliases: 
    - S0140
    
mitre-attack: https://attack.mitre.org/software/S0140
---

## S0140

[Shamoon](https://attack.mitre.org/software/S0140) is wiper malware that was first used by an Iranian group known as the "Cutting Sword of Justice" in 2012. Other versions known as Shamoon 2 and Shamoon 3 were observed in 2016 and 2018. [Shamoon](https://attack.mitre.org/software/S0140) has also been seen leveraging [RawDisk](https://attack.mitre.org/software/S0364) and Filerase to carry out data wiping tasks. Analysis has linked [Shamoon](https://attack.mitre.org/software/S0140) with [Kwampirs](https://attack.mitre.org/software/S0236) based on multiple shared artifacts and coding patterns.[^8]  The term Shamoon is sometimes used to refer to the group using the malware as well as the malware itself.[^3] [^6] [^5] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Shamoon](https://attack.mitre.org/software/S0140) obtains the system time and will only activate if it is greater than a preset date.[^3] [^6]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [Shamoon](https://attack.mitre.org/software/S0140) has been seen overwriting features of disk structure such as the MBR.[^5] [^4] [^3] [^6]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Shamoon](https://attack.mitre.org/software/S0140) obtains the victim's operating system version and keyboard layout and sends the information to the C2 server.[^3] [^6]  |
| [[Query Registry\|T1012]] | Query Registry | [Shamoon](https://attack.mitre.org/software/S0140) queries several Registry keys to identify hard disk partitions to overwrite.[^3]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Shamoon](https://attack.mitre.org/software/S0140) accesses network share(s), enables share access to the target device, copies an executable payload to the target system, and uses a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053) to execute the malware.[^4]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Shamoon](https://attack.mitre.org/software/S0140) creates a new service named “ntssrv” that attempts to appear legitimate; the service's display name is “Microsoft Network Realtime Inspection Service” and its description is “Helps guard against time change attempts targeting known and newly discovered vulnerabilities in network time protocols.” Newer versions create the "MaintenaceSrv" service, which misspells the word "maintenance."[^3] [^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Shamoon](https://attack.mitre.org/software/S0140) can download an executable to run on the victim.[^3]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Shamoon](https://attack.mitre.org/software/S0140) attempts to overwrite operating system files and disk structures with image files.[^5] [^4] [^3]  In a later variant, randomly generated data was used for data overwrites.[^6] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Shamoon](https://attack.mitre.org/software/S0140) creates a new service named “ntssrv” to execute the payload. Newer versions create the "MaintenaceSrv" and "hdv_725x" services.[^3] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Shamoon](https://attack.mitre.org/software/S0140) obtains the target's IP address and local network segment.[^3] [^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Shamoon](https://attack.mitre.org/software/S0140) contains base64-encoded strings.[^3]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | If [Shamoon](https://attack.mitre.org/software/S0140) cannot access shares using current privileges, it attempts access using hard coded, domain-specific credentials gathered earlier in the intrusion.[^4] [^6]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Shamoon](https://attack.mitre.org/software/S0140) creates a new service named “ntssrv” to execute the payload. [Shamoon](https://attack.mitre.org/software/S0140) can also spread via [PsExec](https://attack.mitre.org/software/S0029).[^3] [^7]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Shamoon](https://attack.mitre.org/software/S0140) can impersonate tokens using `LogonUser`, `ImpersonateLoggedOnUser`, and `ImpersonateNamedPipeClient`.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Shamoon](https://attack.mitre.org/software/S0140) attempts to copy itself to remote machines on the network.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Shamoon](https://attack.mitre.org/software/S0140) copies an executable payload to the target system by using [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) and then scheduling an unnamed task to execute the malware.[^4] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Shamoon](https://attack.mitre.org/software/S0140) decrypts ciphertext using an XOR cipher and a base64-encoded string.[^6] 	 |
| [[Modify Registry\|T1112]] | Modify Registry | Once [Shamoon](https://attack.mitre.org/software/S0140) has access to a network share, it enables the RemoteRegistry service on the target system. It will then connect to the system with RegConnectRegistryW and modify the Registry to disable UAC remote restrictions by setting `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy` to 1.[^4] [^3] [^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Shamoon](https://attack.mitre.org/software/S0140) attempts to disable UAC remote restrictions by modifying the Registry.[^3]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [Shamoon](https://attack.mitre.org/software/S0140) will reboot the infected system once the wiping functionality has been completed.[^6] [^2] 	 |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Shamoon](https://attack.mitre.org/software/S0140) has an operational mode for encrypting data instead of overwriting it.[^3] [^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Shamoon](https://attack.mitre.org/software/S0140) scans the C-class subnet of the IPs on the victim's interfaces.[^4]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Shamoon](https://attack.mitre.org/software/S0140) can change the modified time for files to evade forensic detection.[^2] 	 |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Shamoon](https://attack.mitre.org/software/S0140) has used HTTP for C2.[^3]  |




## References

[^1]: Disttrack


[^2]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)


[^3]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^4]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)


[^5]: [Symantec Shamoon 2012](https://www.symantec.com/connect/blogs/shamoon-attacks)


[^6]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)


[^7]: [McAfee Shamoon December19 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-attackers-employ-new-tool-kit-to-wipe-infected-systems/)


[^8]: [Cylera Kwampirs 2022](https://resources.cylera.com/hubfs/Cylera%20Labs/Cylera%20Labs%20Kwampirs%20Shamoon%20Technical%20Report.pdf)


