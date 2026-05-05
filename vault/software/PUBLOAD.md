---
aliases: 
    - S1228
    
mitre-attack: https://attack.mitre.org/software/S1228
---

## S1228

[PUBLOAD](https://attack.mitre.org/software/S1228) is a stager malware that has been observed installing itself in existing directories such as `C:\Users\Public` or creating new directories to stage the malware and its components.[^2]   [PUBLOAD](https://attack.mitre.org/software/S1228) malware collects details of the victim host, establishes persistence, encrypts victim details using RC4 and communicates victim details back to C2.  [PUBLOAD](https://attack.mitre.org/software/S1228) malware has previously been leveraged by China-affiliated actors identified as [Mustang Panda](https://attack.mitre.org/groups/G0129).   [PUBLOAD](https://attack.mitre.org/software/S1228) is also known as “NoFive” and some public reporting identifies the loader component as [CLAIMLOADER](https://attack.mitre.org/software/S1236).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PUBLOAD](https://attack.mitre.org/software/S1228) has acted as a stager that can download the next-stage payload from its C2 server.[^9] [^6] [^1] [^2] [^4]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also delivered FDMTP as a secondary control tool and PTSOCKET for exfiltration to some infected systems.[^8]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has identified AV products on an infected host using the following command: `WMIC  /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List`.[^8]  |
| [[Code Signing\|T1553.002]] | Code Signing | [PUBLOAD](https://attack.mitre.org/software/S1228) has used valid legitimate digital signatures and certificates to evade detection.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has obtained the username from an infected host.[^3] [^5] [^1] [^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has checked supported languages on the compromised system.[^5]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [PUBLOAD](https://attack.mitre.org/software/S1228) has modified HTTP POST requests to resemble legitimate communications.[^9] [^4]   PUBLOAD used FakeTLS headers in network packets to impersonate various versions of TLS protocols to blend in with legitimate network traffic.  [PUBLOAD](https://attack.mitre.org/software/S1228) has utilized FakeTLS headers with the bytes 17 03 03.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [PUBLOAD](https://attack.mitre.org/software/S1228) has created scheduled tasks to maintain persistence with the command `schtasks.exe /F /Create /TN Microsoft_Licensing /sc minute /MO 1 /TR C:\\Users\\Public\\Libraries\...`[^3] [^9] [^2]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [PUBLOAD](https://attack.mitre.org/software/S1228) has embedded debug strings with messages to distract analysts.[^3] [^2]   [PUBLOAD](https://attack.mitre.org/software/S1228) has leveraged `OutputDebugStringW` and `OutputDebugStringA` functions.[^2]  |
| [[Compression\|T1027.015]] | Compression | [PUBLOAD](https://attack.mitre.org/software/S1228) has been delivered as compressed files within ZIP files to victims.[^9] [^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has used `tasklist` to gather running processes on victim host.[^8]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also leveraged the `OpenEventA` Windows API function to check whether the same process was already running.[^2]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PUBLOAD](https://attack.mitre.org/software/S1228) has decoded its payload prior to execution.[^3] [^9] [^1] [^2] [^4]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [PUBLOAD](https://attack.mitre.org/software/S1228) has used `curl` for data exfiltration over FTP.[^8]  |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has collected information on Wi-Fi networks from victim hosts leveraging `netsh wlan show profiles`, `netsh wlan show interface`, and `netsh wlan show`. [^8]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PUBLOAD](https://attack.mitre.org/software/S1228) has used RC4 encryption in C2 communications.[^3] [^5] [^2]  |
| [[DLL\|T1574.001]] | DLL | [PUBLOAD](https://attack.mitre.org/software/S1228) has abused legitimate executables to side-load malicious DLLs.[^3] [^5] [^9] [^1] [^2] [^4] [^7]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has obtained information about local networks through the `ipconfig /all` command.[^8]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [PUBLOAD](https://attack.mitre.org/software/S1228) has utilized environmental keying in the payload to include the victim volume serial number, computer name, username, and machine’s tick count.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PUBLOAD](https://attack.mitre.org/software/S1228) has used several commands executed in sequence via `cmd`. [^8]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PUBLOAD](https://attack.mitre.org/software/S1228) has obfuscated DLL names using the ror13AddHash32 algorithm.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PUBLOAD](https://attack.mitre.org/software/S1228) has added Registry Run keys to achieve persistence using `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. [^3] [^5] [^9] [^8] [^2]  |
| [[Native API\|T1106]] | Native API | [PUBLOAD](https://attack.mitre.org/software/S1228) has used various Windows API calls during execution, when establishing persistence and defense evasion.[^9] [^1]  [PUBLOAD](https://attack.mitre.org/software/S1228) stager leveraged Windows API functions with callback including `GrayStringW`, `EnumDateFormatsA`, and `LineDDA` to bypass anti-virus monitoring. [^2]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also utilized other native windows API functions with callback functions such as `EnumChildWindows` and `EnumSystemLanguageGroupsA`. [^4]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [PUBLOAD](https://attack.mitre.org/software/S1228) has used utilities such as `WinRAR` to archive data prior to exfiltration.[^8]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | PUBLOAD has leveraged `wmic logicaldisk get` to map local network drives.[^8]  |
| [[Software Discovery\|T1518]] | Software Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has used several commands executed in sequence via `cmd` in a short interval to gather software versions including querying Registry keys.[^8]  |
| [[Query Registry\|T1012]] | Query Registry | [PUBLOAD](https://attack.mitre.org/software/S1228) has queried Registry values to identify software using `reg query`.[^8]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [PUBLOAD](https://attack.mitre.org/software/S1228) has utilized a magic value in C2 communications and only executes in memory when response packets match specific values of 17 03 03.[^5] [^6] [^1] [^2] [^7]   [PUBLOAD](https://attack.mitre.org/software/S1228) has also used magic bytes consisting of 46 77 4d.[^5]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has identified internet connectivity details through commands such as `tracert -h 5 -4 google.com` and `curl http://myip.ipip.net`.[^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PUBLOAD](https://attack.mitre.org/software/S1228) has communicated via `curl` over HTTP to identify device IP data.[^8]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also utilized HTTP for a command-and-control protocol through HTTP POST.[^5] [^9] [^4]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also leveraged HTTPS for C2.[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has leveraged `tasklist` to gather running services on victim host.[^8]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has collected the machine’s tick count through the use of `GetTickCount`.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has used several commands executed in sequence via `cmd` in a short interval to gather information on network connections.[^8]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [PUBLOAD](https://attack.mitre.org/software/S1228) has used `wmic` to gather information from the victim device.[^8]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [PUBLOAD](https://attack.mitre.org/software/S1228) has leveraged `curl` for data exfiltration over FTP by uploading RAR archives containing targeted files (.doc, .docx, .xls, .xlsx, .pdf, .ppt, .pptx) to an adversary-owned FTP site.[^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PUBLOAD](https://attack.mitre.org/software/S1228) has renamed malicious files to mimic legitimate file names such as adobe_wf.exe.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PUBLOAD](https://attack.mitre.org/software/S1228) has collected and sent system information including volume serial number, computer name, and system uptime to designated C2.[^3] [^1]   [PUBLOAD](https://attack.mitre.org/software/S1228) has also used several commands executed in sequence via `cmd` in a short interval to gather system information about the infected host including `systeminfo`.[^8]  [PUBLOAD](https://attack.mitre.org/software/S1228) has decrypted shellcode that collects the computer name.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^2]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^3]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^4]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^5]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)


[^6]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)


[^7]: [PaloAlto MUSTANG PANDA PUBLOAD MARCH 2024](https://unit42.paloaltonetworks.com/chinese-apts-target-asean-entities/)


[^8]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^9]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)


