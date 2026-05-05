---
aliases: 
    - Storm-1811
mitre-attack: https://attack.mitre.org/groups/G1046
---

## G1046

[Storm-1811](https://attack.mitre.org/groups/G1046) is a financially-motivated entity linked to [Black Basta](https://attack.mitre.org/software/S1070) ransomware deployment. [Storm-1811](https://attack.mitre.org/groups/G1046) is notable for unique phishing and social engineering mechanisms for initial access, such as overloading victim email inboxes with non-malicious spam to prompt a fake "help desk" interaction leading to the deployment of adversary tools and capabilities.[^3] [^4] [^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Cloud Accounts\|T1585.003]] | Cloud Accounts | [Storm-1811](https://attack.mitre.org/groups/G1046) has created malicious accounts to enable activity via Microsoft Teams, typically spoofing various IT support and helpdesk themes.[^3]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Storm-1811](https://attack.mitre.org/groups/G1046) has locally staged captured credentials for subsequent manual exfiltration.[^4]  |
| [[Email Bombing\|T1667]] | Email Bombing | [Storm-1811](https://attack.mitre.org/groups/G1046) has deployed large volumes of non-malicious email spam to victims in order to prompt follow-on interactions with the threat actor posing as IT support or helpdesk to resolve the problem.[^4] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Storm-1811](https://attack.mitre.org/groups/G1046) has created Windows Registry Run keys that execute various batch scripts to establish persistence on victim devices.[^4]  |
| [[Domains\|T1583.001]] | Domains | [Storm-1811](https://attack.mitre.org/groups/G1046) has created domains for use with RMM tools.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Storm-1811](https://attack.mitre.org/groups/G1046) has disguised [Cobalt Strike](https://attack.mitre.org/software/S0154) installers as a malicious DLL masquerading as part of a legitimate 7zip installation package.[^4]  |
| [[Tool\|T1588.002]] | Tool | [Storm-1811](https://attack.mitre.org/groups/G1046) acquired various legitimate and malicious tools, such as RMM software and commodity malware packages, for operations.[^3] [^4]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Storm-1811](https://attack.mitre.org/groups/G1046) has abused multiple types of legitimate remote access software and tools, such as ScreenConnect, NetSupport Manager, and AnyDesk.[^3] [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Storm-1811](https://attack.mitre.org/groups/G1046) has used PowerShell for multiple purposes, such as using PowerShell scripts executing in an infinite loop to create an SSH connection to a command and control server.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Storm-1811](https://attack.mitre.org/groups/G1046) has used multiple batch scripts during initial access and subsequent actions on victim machines.[^3] [^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Storm-1811](https://attack.mitre.org/groups/G1046) has distributed password-protected archives such as ZIP files during intrusions.[^4]  |
| [[Masquerade Account Name\|T1036.010]] | Masquerade Account Name | [Storm-1811](https://attack.mitre.org/groups/G1046) has created Microsoft Teams accounts that spoof IT support and helpdesk members for use in application and voice phishing.[^3]  |
| [[Input Capture\|T1056]] | Input Capture | [Storm-1811](https://attack.mitre.org/groups/G1046) has used a PowerShell script to capture user credentials after prompting a user to authenticate to run a malicious script masquerading as a legitimate update item.[^4]  |
| [[DLL\|T1574.001]] | DLL | [Storm-1811](https://attack.mitre.org/groups/G1046) has deployed a malicious DLL (7z.DLL) that is sideloaded by a modified, legitimate installer (7zG.exe) when that installer is executed with an additional command line parameter of `b` at runtime to load a [Cobalt Strike](https://attack.mitre.org/software/S0154) beacon payload.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Storm-1811](https://attack.mitre.org/groups/G1046) has prompted users to execute downloaded software and payloads as the result of social engineering activity.[^3] [^4] [^1]  |
| [[Spearphishing Voice\|T1566.004]] | Spearphishing Voice | [Storm-1811](https://attack.mitre.org/groups/G1046) has initiated voice calls with victims posing as IT support to prompt users to download and execute scripts and other tools for initial access.[^3] [^4] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Storm-1811](https://attack.mitre.org/groups/G1046) XOR encodes a [Cobalt Strike](https://attack.mitre.org/software/S0154) installation payload in a DLL file that is decoded with a hardcoded key when called by a legitimate 7zip installation process.[^4]  |
| [[Impersonation\|T1684.001]] | Impersonation | [Storm-1811](https://attack.mitre.org/groups/G1046) impersonates help desk and IT support personnel for phishing and social engineering purposes during initial access to victim environments.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Storm-1811](https://attack.mitre.org/groups/G1046) has used scripted `cURL` commands, [BITSAdmin](https://attack.mitre.org/software/S0190), and other mechanisms to retrieve follow-on batch scripts and tools for execution on victim devices.[^3] [^4] [^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Storm-1811](https://attack.mitre.org/groups/G1046) has used the [Impacket](https://attack.mitre.org/software/S0357) toolset to move and remotely execute payloads to other hosts in victim networks.[^4]  |
| [[SSH\|T1021.004]] | SSH | [Storm-1811](https://attack.mitre.org/groups/G1046) has used OpenSSH to establish an SSH tunnel to victims for persistent access.[^3]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Storm-1811](https://attack.mitre.org/groups/G1046) is a financially-motivated entity linked to the deployment of [Black Basta](https://attack.mitre.org/software/S1070) ransomware in victim environments.[^3]  |
| [[Masquerading\|T1036]] | Masquerading | [Storm-1811](https://attack.mitre.org/groups/G1046) has prompted users to download and execute batch scripts that masquerade as legitimate update files during initial access and social engineering operations.[^4]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Storm-1811](https://attack.mitre.org/groups/G1046) has enumerated domain accounts and access during intrusions.[^3]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Storm-1811](https://attack.mitre.org/groups/G1046) has used Microsoft Teams to send messages and initiate voice calls to victims posing as IT support personnel.[^3]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Storm-1811](https://attack.mitre.org/groups/G1046) has distributed malicious links to victims that redirect to EvilProxy-based phishing sites to harvest credentials.[^3]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Storm-1811](https://attack.mitre.org/groups/G1046) has performed domain account enumeration during intrusions.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Storm-1811](https://attack.mitre.org/groups/G1046) has used `whoami.exe` to determine if the active user on a compromised system is an administrator.[^4]  |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [Storm-1811](https://attack.mitre.org/groups/G1046) has exfiltrated captured user credentials via Secure Copy Protocol (SCP).[^4]  |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | [Storm-1811](https://attack.mitre.org/groups/G1046) has used `cacls.exe` via batch script to modify file and directory permissions in victim environments.[^4]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Storm-1811](https://attack.mitre.org/groups/G1046) has attempted to move laterally in victim environments via SMB using [Impacket](https://attack.mitre.org/software/S0357).[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Impacket\|S0357]] | Impacket | [Storm-1811](https://attack.mitre.org/groups/G1046) has used [Impacket](https://attack.mitre.org/software/S0357) for lateral movement activity.[^4]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [Storm-1811](https://attack.mitre.org/groups/G1046) has used [BITSAdmin](https://attack.mitre.org/software/S0190) to download payloads.[^3] [^2]  |
| [[Quick Assist\|S1209]] | Quick Assist | [Storm-1811](https://attack.mitre.org/groups/G1046) used [Quick Assist](https://attack.mitre.org/software/S1209) as part of social engineering activity to interact with victims to install follow-on malicious software.[^3]  |
| [[PsExec\|S0029]] | PsExec | [Storm-1811](https://attack.mitre.org/groups/G1046) has used [PsExec](https://attack.mitre.org/software/S0029) for remote process execution.[^3]  |
| [[Black Basta\|S1070]] | Black Basta | [Storm-1811](https://attack.mitre.org/groups/G1046) is associated with the deployment of [Black Basta](https://attack.mitre.org/software/S1070) ransomware.[^3] [^4]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Storm-1811](https://attack.mitre.org/groups/G1046) operations include the use of [Cobalt Strike](https://attack.mitre.org/software/S0154).[^3] [^4]  |
| [[QakBot\|S0650]] | QakBot | [Storm-1811](https://attack.mitre.org/groups/G1046) operations have included deployment of [QakBot](https://attack.mitre.org/software/S0650).[^3]  |



## References

[^1]: [RedCanary Storm-1811 2024](https://redcanary.com/blog/threat-intelligence/storm-1811-black-basta/)


[^2]: [RedCanary June Insights 2024](https://redcanary.com/blog/threat-intelligence/intelligence-insights-june-2024/)


[^3]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^4]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


