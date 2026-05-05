---
aliases: 
    - S0223
    
mitre-attack: https://attack.mitre.org/software/S0223
---

## S0223

[POWERSTATS](https://attack.mitre.org/software/S0223) is a PowerShell-based first stage backdoor used by [MuddyWater](https://attack.mitre.org/groups/G0069). [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Component Object Model\|T1559.001]] | Component Object Model | [POWERSTATS](https://attack.mitre.org/software/S0223) can use DCOM (targeting the 127.0.0.1 loopback address) to execute additional payloads on compromised hosts.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [POWERSTATS](https://attack.mitre.org/software/S0223) can deobfuscate the main backdoor code.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [POWERSTATS](https://attack.mitre.org/software/S0223) has the ability to identify the username on the compromised host.[^3]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [POWERSTATS](https://attack.mitre.org/software/S0223) has created a scheduled task named "MicrosoftEdge" to establish persistence.[^7]  |
| [[Local Account\|T1087.001]] | Local Account | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve usernames from compromised hosts.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [POWERSTATS](https://attack.mitre.org/software/S0223) has detected security tools.[^2]  |
| [[Mshta\|T1218.005]] | Mshta | [POWERSTATS](https://attack.mitre.org/software/S0223) can use Mshta.exe to execute additional payloads on compromised hosts.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [POWERSTATS](https://attack.mitre.org/software/S0223) can use WMI queries to retrieve data from compromised hosts.[^2] [^7]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [POWERSTATS](https://attack.mitre.org/software/S0223) can sleep for a given number of seconds.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve OS name/architecture and computer/domain name information from compromised hosts.[^2] [^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [POWERSTATS](https://attack.mitre.org/software/S0223) encoded C2 traffic with base64.[^5]  |
| [[External Proxy\|T1090.002]] | External Proxy | [POWERSTATS](https://attack.mitre.org/software/S0223) has connected to C2 servers through proxies.[^2]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [POWERSTATS](https://attack.mitre.org/software/S0223) can use DDE to execute additional payloads on compromised hosts.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [POWERSTATS](https://attack.mitre.org/software/S0223) uses PowerShell for obfuscation and execution.[^5] [^7] [^3] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve IP, network adapter configuration information, and domain from compromised hosts.[^2] [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [POWERSTATS](https://attack.mitre.org/software/S0223) can upload files from compromised hosts.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [POWERSTATS](https://attack.mitre.org/software/S0223) can disable Microsoft Office Protected View by changing Registry keys.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [POWERSTATS](https://attack.mitre.org/software/S0223) has established persistence through a scheduled task using the command `”C:\Windows\system32\schtasks.exe” /Create /F /SC DAILY /ST 12:00 /TN MicrosoftEdge /TR “c:\Windows\system32\wscript.exe C:\Windows\temp\Windows.vbe”`.[^7]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [POWERSTATS](https://attack.mitre.org/software/S0223) has encrypted C2 traffic with RSA.[^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [POWERSTATS](https://attack.mitre.org/software/S0223) uses character replacement, [PowerShell](https://attack.mitre.org/techniques/T1059/001) environment variables, and XOR encoding to obfuscate code. [POWERSTATS](https://attack.mitre.org/software/S0223)'s backdoor code is a multi-layer obfuscated, encoded, and compressed blob. [^2] [^7]  [POWERSTATS](https://attack.mitre.org/software/S0223) has used PowerShell code with custom string obfuscation [^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [POWERSTATS](https://attack.mitre.org/software/S0223) can delete all files on the C:\, D:\, E:\ and, F:\ drives using [PowerShell](https://attack.mitre.org/techniques/T1059/001) Remove-Item commands.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [POWERSTATS](https://attack.mitre.org/software/S0223) can use VBScript (VBE) code for execution.[^7] [^3]  |
| [[JavaScript\|T1059.007]] | JavaScript | [POWERSTATS](https://attack.mitre.org/software/S0223) can use JavaScript code for execution.[^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve and execute additional [PowerShell](https://attack.mitre.org/techniques/T1059/001) payloads from the C2 server.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve screenshots from compromised hosts.[^2] [^3]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [POWERSTATS](https://attack.mitre.org/software/S0223) has used useless code blocks to counter analysis.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [POWERSTATS](https://attack.mitre.org/software/S0223) has used `get_tasklist` to discover processes on the compromised host.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [ClearSky MuddyWater June 2019](https://www.clearskysec.com/wp-content/uploads/2019/06/Clearsky-Iranian-APT-group-%E2%80%98MuddyWater%E2%80%99-Adds-Exploits-to-Their-Arsenal.pdf)


[^2]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^3]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^4]: POWERSTATS


[^5]: [Unit 42 MuddyWater Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/)


[^6]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^7]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)


[^8]: Powermud


[^9]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


