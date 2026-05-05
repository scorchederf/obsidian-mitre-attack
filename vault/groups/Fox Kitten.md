---
aliases: 
    - Fox Kitten
    - UNC757
    - Parisite
    - Pioneer Kitten
    - RUBIDIUM
    - Lemon Sandstorm
mitre-attack: https://attack.mitre.org/groups/G0117
---

## G0117

[Fox Kitten](https://attack.mitre.org/groups/G0117) is threat actor with a suspected nexus to the Iranian government that has been active since at least 2017 against entities in the Middle East, North Africa, Europe, Australia, and North America. [Fox Kitten](https://attack.mitre.org/groups/G0117) has targeted multiple industrial verticals including oil and gas, technology, government, defense, healthcare, manufacturing, and engineering.[^6] [^1] [^13] [^10] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Fox Kitten](https://attack.mitre.org/groups/G0117) has downloaded additional tools including [PsExec](https://attack.mitre.org/software/S0029) directly to endpoints.[^3]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used a Perl reverse shell to communicate with C2.[^10]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [Fox Kitten](https://attack.mitre.org/groups/G0117) has obtained files from the victim's cloud storage instances.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Angry IP Scanner to detect remote systems.[^3]  |
| [[Brute Force\|T1110]] | Brute Force | [Fox Kitten](https://attack.mitre.org/groups/G0117) has brute forced RDP credentials.[^10]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Fox Kitten](https://attack.mitre.org/groups/G0117) has exploited known vulnerabilities in remote services including RDP.[^6] [^1] [^10]  |
| [[Local Account\|T1136.001]] | Local Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has created a local user account with administrator privileges.[^10]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used 7-Zip to archive data.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded scripts to avoid detection.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Fox Kitten](https://attack.mitre.org/groups/G0117) has searched local system resources to access sensitive documents.[^3]  |
| [[Establish Accounts\|T1585]] | Establish Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has created KeyBase accounts to communicate with ransomware victims.[^10] [^7]  |
| [[VNC\|T1021.005]] | VNC | [Fox Kitten](https://attack.mitre.org/groups/G0117) has installed TightVNC server and client on compromised servers and endpoints for lateral movement.[^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed files to gain valid credentials.[^3]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Google Chrome bookmarks to identify internal resources and assets.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used cmd.exe likely as a password changing mechanism.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded payloads to avoid detection.[^3]  |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed victim security and IT environments and Microsoft Teams to mine valuable information.[^3]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used valid accounts to access SMB shares.[^3]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Fox Kitten](https://attack.mitre.org/groups/G0117) has exploited known vulnerabilities in Fortinet, PulseSecure, and Palo Alto VPN appliances.[^6] [^13] [^1] [^3] [^10]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used scripts to access credential information from the KeePass database.[^3]  |
| [[NTDS\|T1003.003]] | NTDS | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Volume Shadow Copy to access credential information from NTDS.[^3]  |
| [[Local Account\|T1087.001]] | Local Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed ntuser.dat and UserClass.dat on compromised hosts.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the Softerra LDAP browser to browse documentation on service accounts.[^3]  |
| [[SSH\|T1021.004]] | SSH | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the PuTTY and Plink tools for lateral movement.[^3]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has installed web shells on compromised hosts to maintain access.[^3] [^10]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Scheduled Tasks for persistence and to load and execute a reverse proxy binary.[^3] [^10]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Fox Kitten](https://attack.mitre.org/groups/G0117) has named the task for a reverse proxy lpupdate to appear legitimate.[^3]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used prodump to dump credentials from LSASS.[^3]  |
| [[Proxy\|T1090]] | Proxy | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the open source reverse proxy tools including FRPC and Go Proxy to establish connections from C2 to local servers.[^3] [^10] [^7]  |
| [[Query Registry\|T1012]] | Query Registry | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed Registry hives ntuser.dat and UserClass.dat.[^3]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used protocol tunneling for communication and RDP activity on compromised hosts through the use of open source tools such as [ngrok](https://attack.mitre.org/software/S0508) and custom tool SSHMinion.[^1] [^3] [^10]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used RDP to log in and move laterally in the target environment.[^3] [^10]  |
| [[Web Service\|T1102]] | Web Service | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Amazon Web Services to host C2.[^10]  |
| [[Data from Network Shared Drive\|T1039]] | Data from Network Shared Drive | [Fox Kitten](https://attack.mitre.org/groups/G0117) has searched network shares to access sensitive documents.[^3]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used valid credentials with various services during lateral movement.[^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used tools including NMAP to conduct broad scanning to identify open ports.[^3] [^10]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used sticky keys to launch a command prompt.[^3]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used a Twitter account to communicate with ransomware victims.[^10]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Fox Kitten](https://attack.mitre.org/groups/G0117) has named binaries and configuration files svhost and dllhost respectively to appear legitimate.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used PowerShell scripts to access credential data.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used WizTree to obtain network files and directory listings.[^3]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ngrok\|S0508]] | ngrok | [^1]  |
| [[PsExec\|S0029]] | PsExec | [^3] [^7]  |
| [[SystemBC\|S9001]] | SystemBC | [^8]  |
| [[China Chopper\|S0020]] | China Chopper | [^3]  |
| [[Pay2Key\|S0556]] | Pay2Key | [^6] [^7]  |



## References

[^1]: [CrowdStrike PIONEER KITTEN August 2020](https://www.crowdstrike.com/blog/who-is-pioneer-kitten/)


[^2]: Parisite


[^3]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^4]: Lemon Sandstorm


[^5]: RUBIDIUM


[^6]: [ClearkSky Fox Kitten February 2020](https://www.clearskysec.com/fox-kitten/)


[^7]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


[^8]: [FortinetEtAl_IranianIntrusion_Mar2025](https://www.fortinet.com/content/dam/fortinet/assets/reports/report-incident-response-middle-east.pdf)


[^9]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^10]: [ClearSky Pay2Kitten December 2020](https://www.clearskysec.com/wp-content/uploads/2020/12/Pay2Kitten.pdf)


[^11]: UNC757


[^12]: Pioneer Kitten


[^13]: [Dragos PARISITE ](https://www.dragos.com/threat/parisite/)


