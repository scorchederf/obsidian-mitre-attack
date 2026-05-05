---
aliases: 
    - FIN13
    - Elephant Beetle
mitre-attack: https://attack.mitre.org/groups/G1016
---

## G1016

[FIN13](https://attack.mitre.org/groups/G1016) is a financially motivated cyber threat group that has targeted the financial, retail, and hospitality industries in Mexico and Latin America, as early as 2016. [FIN13](https://attack.mitre.org/groups/G1016) achieves its objectives by stealing intellectual property, financial data, mergers and acquisition information, or PII.[^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malware\|T1587.001]] | Malware | [FIN13](https://attack.mitre.org/groups/G1016) has utilized custom malware to maintain persistence in a compromised environment.[^1] [^2]  |
| [[Default Accounts\|T1078.001]] | Default Accounts | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged default credentials for authenticating myWebMethods (WMS) and QLogic web management interface to gain initial access.[^2]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [FIN13](https://attack.mitre.org/groups/G1016) has utilized web shells and Java tools for tunneling capabilities to and from compromised assets.[^2]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged `WMI` to move laterally within a compromised network via application servers and SQL servers.[^2]  |
| [[External Remote Services\|T1133]] | External Remote Services | [FIN13](https://attack.mitre.org/groups/G1016) has gained access to compromised environments via remote access services such as the corporate virtual private network (VPN).[^1]  |
| [[Domain Account\|T1087.002]] | Domain Account | [FIN13](https://attack.mitre.org/groups/G1016) can identify user accounts associated with a Service Principal Name and query Service Principal Names within the domain by utilizing the following scripts: `GetUserSPNs.vbs` and `querySpn.vbs`.[^1] [^2]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `nmap` for reconnaissance efforts. [FIN13](https://attack.mitre.org/groups/G1016) has also scanned for internal MS-SQL servers in a compromised network.[^1] [^2]  |
| [[Web Shell\|T1505.003]] | Web Shell | [FIN13](https://attack.mitre.org/groups/G1016) has utilized obfuscated and open-source web shells such as JspSpy, reGeorg, MiniWebCmdShell, and Vonloesch Jsp File Browser 1.2 to enable remote code execution and to execute commands on compromised web server.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has collected local host information by utilizing Windows commands `systeminfo`, `fsutil`, and `fsinfo`. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantex Altiris console and LanDesk account to retrieve host information.[^1] [^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `nslookup` and `ipconfig` for network reconnaissance efforts. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantec Altiris console and LanDesk account to retrieve network information.[^1] [^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [FIN13](https://attack.mitre.org/groups/G1016) has utilized a proxy tool to communicate between compromised assets.[^2]  |
| [[Data Manipulation\|T1565]] | Data Manipulation | [FIN13](https://attack.mitre.org/groups/G1016) has injected fraudulent transactions into compromised networks that mimic legitimate behavior to siphon off incremental amounts of money.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [FIN13](https://attack.mitre.org/groups/G1016) has used PowerShell commands to obtain DNS data from a compromised network.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [FIN13](https://attack.mitre.org/groups/G1016) has created scheduled tasks in the `C:\Windows` directory of the compromised network.[^1]   |
| [[Local Account\|T1136.001]] | Local Account | [FIN13](https://attack.mitre.org/groups/G1016) has created MS-SQL local accounts in a compromised network.[^2]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [FIN13](https://attack.mitre.org/groups/G1016) has extracted the SAM and SYSTEM registry hives using the `reg.exe` binary for obtaining password hashes from a compromised machine.[^2]  |
| [[NTDS\|T1003.003]] | NTDS | [FIN13](https://attack.mitre.org/groups/G1016) has harvested the NTDS.DIT file and leveraged the [Impacket](https://attack.mitre.org/software/S0357) tool on the compromised domain controller to locally decrypt it.[^2]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [FIN13](https://attack.mitre.org/groups/G1016) has exploited known vulnerabilities such as CVE-2017-1000486 (Primefaces Application Expression Language Injection), CVE-2015-7450 (WebSphere Application Server SOAP Deserialization Exploit), CVE-2010-5326 (SAP NewWeaver Invoker Servlet Exploit), and EDB-ID-24963 (SAP NetWeaver ConfigServlet Remote Code Execution) to gain initial access.[^1] [^2]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [FIN13](https://attack.mitre.org/groups/G1016) has researched employees to target for social engineering attacks.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [FIN13](https://attack.mitre.org/groups/G1016) has used scheduled tasks names such as `acrotyr` and `AppServicesr` to mimic the same names in a compromised network's `C:\Windows` directory.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged SMB to move laterally within a compromised network via application servers and SQL servers.[^2]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [FIN13](https://attack.mitre.org/groups/G1016) has obtained memory dumps with ProcDump to parse and extract credentials from a victim's LSASS process memory with [Mimikatz](https://attack.mitre.org/software/S0002).[^1] [^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [FIN13](https://attack.mitre.org/groups/G1016) has created hidden files and folders within a compromised Linux system `/tmp` directory. [FIN13](https://attack.mitre.org/groups/G1016) also has used `attrib.exe` to hide gathered local host information.[^1] [^2]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [FIN13](https://attack.mitre.org/groups/G1016) has obtained administrative credentials by browsing through local files on a compromised machine.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [FIN13](https://attack.mitre.org/groups/G1016) has observed the victim's software and infrastructure over several months to understand the technical process of legitimate financial transactions, prior to attempting to conduct fraudulent transactions.[^2]  |
| [[Tool\|T1588.002]] | Tool | [FIN13](https://attack.mitre.org/groups/G1016) has utilized publicly available tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Impacket](https://attack.mitre.org/software/S0357), PWdump7, ProcDump, Nmap, and Incognito V2 for targeting efforts.[^2]  |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | [FIN13](https://attack.mitre.org/groups/G1016) has utilized tools such as Incognito V2 for token manipulation and impersonation.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FIN13](https://attack.mitre.org/groups/G1016) has downloaded additional tools and malware to compromised systems.[^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FIN13](https://attack.mitre.org/groups/G1016) has used HTTP requests to chain multiple web shells and to contact actor-controlled C2 servers prior to exfiltrating stolen data.[^1] [^2]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [FIN13](https://attack.mitre.org/groups/G1016) has used the PowerShell utility `Invoke-SMBExec` to execute the pass the hash method for lateral movement within an compromised environment.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged `xp_cmdshell` and Windows Command Shell to execute commands on a compromised machine. [FIN13](https://attack.mitre.org/groups/G1016) has also attempted to leverage the ‘xp_cmdshell’ SQL procedure to execute remote commands on internal MS-SQL servers.[^1] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [FIN13](https://attack.mitre.org/groups/G1016) has used Windows Registry run keys such as, `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run\hosts` to maintain persistence.[^1]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `Ping` and `tracert` for network reconnaissance efforts.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [FIN13](https://attack.mitre.org/groups/G1016) has masqueraded staged data by using the Windows [certutil](https://attack.mitre.org/software/S0160) utility to generate fake Base64 encoded certificates with the input file.[^1] [^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [FIN13](https://attack.mitre.org/groups/G1016) has used VBS scripts for code execution on comrpomised machines.[^2]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [FIN13](https://attack.mitre.org/groups/G1016) has assigned newly created accounts the sysadmin role to maintain persistence.[^2]  |
| [[DLL\|T1574.001]] | DLL | [FIN13](https://attack.mitre.org/groups/G1016) has used IISCrack.dll as a side-loading technique to load a malicious version of httpodbc.dll on old IIS Servers (CVE-2001-0507).[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [FIN13](https://attack.mitre.org/groups/G1016) has remotely accessed compromised environments via Remote Desktop Services (RDS) for lateral movement.[^1]  |
| [[Network Topology\|T1590.004]] | Network Topology | [FIN13](https://attack.mitre.org/groups/G1016) has searched for infrastructure that can provide remote access to an environment for targeting efforts.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has executed net view commands for enumeration of open shares on compromised machines.[^1] [^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [FIN13](https://attack.mitre.org/groups/G1016) has compressed the dump output of compromised credentials with a 7zip binary.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `certutil` to decode base64 encoded versions of custom malware.[^1]  |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | [FIN13](https://attack.mitre.org/groups/G1016) has replaced legitimate KeePass binaries with trojanized versions to collect passwords from numerous applications.[^1]    |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [FIN13](https://attack.mitre.org/groups/G1016) has utilized `WMI` to execute commands and move laterally on compromised Windows machines.[^1] [^2]  |
| [[SSH\|T1021.004]] | SSH | [FIN13](https://attack.mitre.org/groups/G1016) has remotely accessed compromised environments via secure shell (SSH) for lateral movement.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [FIN13](https://attack.mitre.org/groups/G1016) has utilized the following temporary folders on compromised Windows and Linux systems for their operations prior to exfiltration: `C:\Windows\Temp` and `/tmp`.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [FIN13](https://attack.mitre.org/groups/G1016) has logged the keystrokes of victims to escalate privileges.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [FIN13](https://attack.mitre.org/groups/G1016) has masqueraded WAR files to look like legitimate packages such as, wsexample.war, wsexamples.com, examples.war, and exampl3s.war.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used `netstat` and other net  commands for network reconnaissance efforts.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has used the Windows `dir` command to enumerate files and directories in a victim's network.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FIN13](https://attack.mitre.org/groups/G1016) has gathered stolen credentials, sensitive data such as point-of-sale (POS), and ATM data from a compromised network before exfiltration.[^1] [^2]  |
| [[Permission Groups Discovery\|T1069]] | Permission Groups Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has enumerated all users and roles from a victim's main treasury system.[^1]  |
| [[Account Discovery\|T1087]] | Account Discovery | [FIN13](https://attack.mitre.org/groups/G1016) has enumerated all users and their roles from a victim's main treasury system.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [^2]  |
| [[Impacket\|S0357]] | Impacket | [^2]  |
| [[Empire\|S0363]] | Empire | [^2]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |



## References

[^1]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^2]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^3]: Elephant Beetle


