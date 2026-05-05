---
aliases: 
    - S1039
    
mitre-attack: https://attack.mitre.org/software/S1039
---

## S1039

[Bumblebee](https://attack.mitre.org/software/S1039) is a custom loader written in C++ that has been used by multiple threat actors, including possible initial access brokers, to download and execute additional payloads since at least March 2022. [Bumblebee](https://attack.mitre.org/software/S1039) has been linked to ransomware operations including [Conti](https://attack.mitre.org/software/S0575), Quantum, and Mountlocker and derived its name from the appearance of "bumblebee" in the user-agent.[^4] [^5] [^1] <br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bumblebee](https://attack.mitre.org/software/S1039) can enumerate the OS version and domain on a targeted system.[^4] [^5] [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to identify the user name.[^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Bumblebee](https://attack.mitre.org/software/S1039) can use WMI to gather system information and to spawn processes for code injection.[^4] [^5] [^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Bumblebee](https://attack.mitre.org/software/S1039) can send collected data in JSON format to C2.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Bumblebee](https://attack.mitre.org/software/S1039) can use `cmd.exe` to drop and run files.[^4] [^5]  |
| [[System Checks\|T1497.001]] | System Checks | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to search for designated file paths and Registry keys that indicate a virtualized environment from multiple products.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bumblebee](https://attack.mitre.org/software/S1039) can deobfuscate C2 server responses and unpack its code on targeted hosts.[^5] [^6]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | The [Bumblebee](https://attack.mitre.org/software/S1039) loader can support the `Dij` command which gives it the ability to inject DLLs into the memory of other processes.[^5] [^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Bumblebee](https://attack.mitre.org/software/S1039) can compress data stolen from the Registry and volume shadow copies prior to exfiltration.[^3]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to set a hardcoded and randomized sleep interval.[^5]  |
| [[Odbcconf\|T1218.008]] | Odbcconf | [Bumblebee](https://attack.mitre.org/software/S1039) can use `odbcconf.exe` to run DLLs on targeted hosts.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Bumblebee](https://attack.mitre.org/software/S1039) can capture and compress stolen credentials from the Registry and volume shadow copies.[^3]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Bumblebee](https://attack.mitre.org/software/S1039) can identify specific analytical tools based on running processes.[^5] [^1] [^6]  |
| [[Asynchronous Procedure Call\|T1055.004]] | Asynchronous Procedure Call | [Bumblebee](https://attack.mitre.org/software/S1039) can use asynchronous procedure call (APC) injection to execute commands received from C2.[^5]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Bumblebee](https://attack.mitre.org/software/S1039) can create a Visual Basic script to enable persistence.[^5] [^1]  |
| [[Web Service\|T1102]] | Web Service | [Bumblebee](https://attack.mitre.org/software/S1039) has been downloaded to victim's machines from OneDrive.[^5]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to perform anti-virtualization checks.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bumblebee](https://attack.mitre.org/software/S1039) can download and execute additional payloads including through the use of a `Dex` command.[^4] [^5] [^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Bumblebee](https://attack.mitre.org/software/S1039) can use backup C2 servers if the primary server fails.[^5]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Bumblebee](https://attack.mitre.org/software/S1039) has been spread through e-mail campaigns with malicious links.[^5] [^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to base64 encode C2 server responses.[^5]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Bumblebee](https://attack.mitre.org/software/S1039) has used `rundll32` for execution of the loader component.[^5] [^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Bumblebee](https://attack.mitre.org/software/S1039) has named component DLLs "RapportGP.dll" to match those used by the security company Trusteer.[^6]  |
| [[Process Injection\|T1055]] | Process Injection | [Bumblebee](https://attack.mitre.org/software/S1039) can inject code into multiple processes on infected endpoints.[^3]  |
| [[Native API\|T1106]] | Native API | [Bumblebee](https://attack.mitre.org/software/S1039) can use multiple Native APIs.[^5] [^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Bumblebee](https://attack.mitre.org/software/S1039) has been delivered as password-protected zipped ISO files and used control-flow-flattening to obfuscate the flow of functions.[^5] [^3] [^6]  |
| [[Shared Modules\|T1129]] | Shared Modules |  [Bumblebee](https://attack.mitre.org/software/S1039) can use `LoadLibrary` to attempt to execute GdiPlus.dll.[^6]  |
| [[Query Registry\|T1012]] | Query Registry | [Bumblebee](https://attack.mitre.org/software/S1039) can check the Registry for specific keys.[^6]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Bumblebee](https://attack.mitre.org/software/S1039) can encrypt C2 requests and responses with RC4[^5]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to bypass UAC to deploy post exploitation tools with elevated privileges.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Bumblebee](https://attack.mitre.org/software/S1039) can identify processes associated with analytical tools.[^5] [^1] [^6]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Bumblebee](https://attack.mitre.org/software/S1039) has relied upon a user downloading a file from a OneDrive link for execution.[^5] [^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Bumblebee](https://attack.mitre.org/software/S1039) has gained execution through luring users into opening malicious attachments.[^5] [^1] [^3] [^6] <br> |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Bumblebee](https://attack.mitre.org/software/S1039) can achieve persistence by copying its DLL to a subdirectory of %APPDATA% and creating a Visual Basic Script that will load the DLL via a scheduled task.[^5] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Bumblebee](https://attack.mitre.org/software/S1039) has relied upon a user opening an ISO file to enable execution of malicious shortcut files and DLLs.[^5] [^1] [^3] [^6] <br> |
| [[PowerShell\|T1059.001]] | PowerShell | [Bumblebee](https://attack.mitre.org/software/S1039) can use PowerShell for execution.[^6]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Bumblebee](https://attack.mitre.org/software/S1039) can use a COM object to execute queries to gather system information.[^5]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Bumblebee](https://attack.mitre.org/software/S1039) can search for tools used in static analysis.[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Bumblebee](https://attack.mitre.org/software/S1039) can uninstall its loader through the use of a `Sdl` command.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TA578\|G1038]] | TA578 |
| [[EXOTIC LILY\|G1011]] | EXOTIC LILY |



## References

[^1]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^2]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^3]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^4]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^5]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^6]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)


