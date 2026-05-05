---
aliases: 
    - Earth Lusca
    - TAG-22
    - Charcoal Typhoon
    - CHROMIUM
    - ControlX
mitre-attack: https://attack.mitre.org/groups/G1006
---

## G1006

[Earth Lusca](https://attack.mitre.org/groups/G1006) is a suspected China-based cyber espionage group that has been active since at least April 2019. [Earth Lusca](https://attack.mitre.org/groups/G1006) has targeted organizations in Australia, China, Hong Kong, Mongolia, Nepal, the Philippines, Taiwan, Thailand, Vietnam, the United Arab Emirates, Nigeria, Germany, France, and the United States. Targets included government institutions, news media outlets, gambling companies, educational institutions, COVID-19 research organizations, telecommunications companies, religious movements banned in China, and cryptocurrency trading platforms; security researchers assess some [Earth Lusca](https://attack.mitre.org/groups/G1006) operations may be financially motivated.[^1] <br><br>[Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Web Services\|T1583.006]] | Web Services | [Earth Lusca](https://attack.mitre.org/groups/G1006) has established GitHub accounts to host their malware.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used steganography to hide shellcode in a BMP image file.[^1]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Earth Lusca](https://attack.mitre.org/groups/G1006) has staged malware and malicious files on compromised web servers, GitHub, and Google Drive.[^1]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [Earth Lusca](https://attack.mitre.org/groups/G1006) has dropped an SSH-authorized key in the `/root/.ssh` folder in order to access a compromised server with SSH.[^1]  |
| [[DCSync\|T1003.006]] | DCSync | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used a `DCSync` command with [Mimikatz](https://attack.mitre.org/software/S0002) to retrieve credentials from an exploited controller.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Earth Lusca](https://attack.mitre.org/groups/G1006) used VBA scripts.[^1]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Earth Lusca](https://attack.mitre.org/groups/G1006) has performed watering hole attacks.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `powershell “Get-EventLog -LogName security -Newest 500 | where {$_.EventID -eq 4624} | format-list -<br>property * | findstr “Address””` to find the network information of successfully logged-in accounts to discovery addresses of other machines. [Earth Lusca](https://attack.mitre.org/groups/G1006) has also used multiple scanning tools to discover other machines within the same compromised network.[^1]  |
| [[Web Services\|T1584.006]] | Web Services | [Earth Lusca](https://attack.mitre.org/groups/G1006) has compromised Google Drive repositories.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Earth Lusca](https://attack.mitre.org/groups/G1006) has manipulated legitimate websites to inject malicious JavaScript code as part of their watering hole operations.[^1]  |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [Mimikatz](https://attack.mitre.org/software/S0002) to exploit a domain controller via the ZeroLogon exploit (CVE-2020-1472).[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `move [file path] c:\windows\system32\spool\prtprocs\x64\spool.dll` to move and register a malicious DLL name as a Windows print processor, which eventually was loaded by the Print Spooler service.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [certutil](https://attack.mitre.org/software/S0160) to decode a string into a cabinet file.[^1]  |
| [[Domains\|T1583.001]] | Domains | [Earth Lusca](https://attack.mitre.org/groups/G1006) has registered domains, intended to look like legitimate target domains, that have been used in watering hole attacks.[^1]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) collected information on user accounts via the `whoami` command.[^1]  |
| [[Print Processors\|T1547.012]] | Print Processors | [Earth Lusca](https://attack.mitre.org/groups/G1006) has added the Registry key `HKLM\SYSTEM\ControlSet001\Control\Print\Environments\Windows x64\Print Processors\UDPrint” /v Driver /d “spool.dll /f` to load malware as a Print Processor.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used PowerShell to execute commands.[^1]  |
| [[Python\|T1059.006]] | Python | [Earth Lusca](https://attack.mitre.org/groups/G1006) used Python scripts for port scanning or building reverse shells.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [Tasklist](https://attack.mitre.org/software/S0057) to obtain information from a compromised host.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `schtasks /Create /SC ONLOgon /TN WindowsUpdateCheck /TR “[file path]” /ru system` for persistence.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Earth Lusca](https://attack.mitre.org/groups/G1006) has placed a malicious payload in `%WINDIR%\SYSTEM32\oci.dll` so it would be sideloaded by the MSDTC service.[^1]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Earth Lusca](https://attack.mitre.org/groups/G1006) modified the registry using the command `reg add “HKEY_CURRENT_USER\Environment” /v UserInitMprLogonScript /t REG_SZ /d “[file path]”` for persistence.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Earth Lusca](https://attack.mitre.org/groups/G1006) used a VBA script to execute WMI.[^1]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used ProcDump to obtain the hashes of credentials by dumping the memory of the LSASS process.[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used `mshta.exe` to load an HTA script within a malicious .LNK file.[^1]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [Nltest](https://attack.mitre.org/software/S0359) to obtain information about domain controllers.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used the megacmd tool to upload stolen files from a victim network to MEGA.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used the Fodhelper UAC bypass technique to gain elevated privileges.[^1]  |
| [[Tool\|T1588.002]] | Tool | [Earth Lusca](https://attack.mitre.org/groups/G1006) has acquired and used a variety of open source tools.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [Tasklist](https://attack.mitre.org/software/S0057) to obtain information from a compromised host.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Earth Lusca](https://attack.mitre.org/groups/G1006) required users to click on a malicious file for the loader to activate.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Earth Lusca](https://attack.mitre.org/groups/G1006) has compromised victims by directly exploiting vulnerabilities of public-facing servers, including those associated with Microsoft Exchange and Oracle GlassFish.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Earth Lusca](https://attack.mitre.org/groups/G1006) adopted Cloudflare as a proxy for compromised servers.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Earth Lusca](https://attack.mitre.org/groups/G1006) used Base64 to encode strings.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Earth Lusca](https://attack.mitre.org/groups/G1006) created a service using the command `sc create “SysUpdate” binpath= “cmd /c start “[file path]””&&sc config “SysUpdate” start= auto&&net<br>start SysUpdate` for persistence.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Earth Lusca](https://attack.mitre.org/groups/G1006) has sent spearphishing emails to potential targets that contained a malicious link.[^1]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used WinRAR to compress stolen files into an archive prior to exfiltration.[^1]  |
| [[Server\|T1583.004]] | Server | [Earth Lusca](https://attack.mitre.org/groups/G1006) has acquired multiple servers for some of their operations, using each server for a different role.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) employed a PowerShell script called RDPConnectionParser to read and filter the Windows event log “Microsoft-Windows-TerminalServices-RDPClient/Operational”<br>(Event ID 1024) to obtain network information from RDP connections. [Earth Lusca](https://attack.mitre.org/groups/G1006) has also used [netstat](https://attack.mitre.org/software/S0104) from a compromised system to obtain network connection information.[^1]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Earth Lusca](https://attack.mitre.org/groups/G1006) has scanned for vulnerabilities in the public-facing servers of their targets.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `ipconfig` to obtain information about network configurations.[^1]  |
| [[Malware\|T1588.001]] | Malware | [Earth Lusca](https://attack.mitre.org/groups/G1006) has acquired and used a variety of malware, including [Cobalt Strike](https://attack.mitre.org/software/S0154).[^1]  |
| [[Server\|T1584.004]] | Server | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used compromised web servers as part of their operational infrastructure.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Earth Lusca](https://attack.mitre.org/groups/G1006)  has sent spearphishing emails that required the user to click on a malicious link and subsequently open a decoy document with a malicious loader.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [^1]  |
| [[PowerSploit\|S0194]] | PowerSploit | [^1]  |
| [[Tasklist\|S0057]] | Tasklist | [^1]  |
| [[Nltest\|S0359]] | Nltest | [^1]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^1]  |
| [[NBTscan\|S0590]] | NBTscan | [^1]  |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [^1]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^1]  |
| [[ShadowPad\|S0596]] | ShadowPad | [^1]  |



## References

[^1]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^2]: [Recorded Future RedHotel August 2023](https://go.recordedfuture.com/hubfs/reports/cta-2023-0808.pdf)


[^3]: CHROMIUM


[^4]: Charcoal Typhoon


[^5]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^6]: TAG-22


[^7]: [Recorded Future TAG-22 July 2021](https://www.recordedfuture.com/research/chinese-group-tag-22-targets-nepal-philippines-taiwan)


[^8]: ControlX


