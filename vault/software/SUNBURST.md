---
aliases: 
    - S0559
    
mitre-attack: https://attack.mitre.org/software/S0559
---

## S0559

[SUNBURST](https://attack.mitre.org/software/S0559) is a trojanized DLL designed to fit within the SolarWinds Orion software update framework. It was used by [APT29](https://attack.mitre.org/groups/G0016) since at least February 2020.[^10] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [SUNBURST](https://attack.mitre.org/software/S0559) remained dormant after initial access for a period of up to two weeks.[^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SUNBURST](https://attack.mitre.org/software/S0559) used the WMI query `Select * From Win32_SystemDriver` to retrieve a driver listing.[^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected hostname and OS version.[^7] [^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SUNBURST](https://attack.mitre.org/software/S0559) had commands that allow an attacker to write or delete registry keys, and was observed stopping services by setting their `HKLM\SYSTEM\CurrentControlSet\services\\[service_name]\\Start` registry entries to value 4.[^7] [^8]  It also deleted previously-created Image File Execution Options (IFEO) Debugger registry values and registry keys related to HTTP proxy to clean up traces of its activity.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SUNBURST](https://attack.mitre.org/software/S0559) encrypted C2 traffic using a single-byte-XOR cipher.[^7]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SUNBURST](https://attack.mitre.org/software/S0559) used Base64 encoding in its C2 traffic.[^7]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [SUNBURST](https://attack.mitre.org/software/S0559) removed IFEO registry values to clean up traces of persistence.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SUNBURST](https://attack.mitre.org/software/S0559) collected information from a compromised host.[^8] [^7]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected device `UPTIME`.[^7] [^8]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) had commands to enumerate files and directories.[^7] [^8]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [SUNBURST](https://attack.mitre.org/software/S0559) attempted to disable software security services following checks against a FNV-1a + XOR hashed hardcoded blocklist.[^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected all network interface MAC addresses that are up and not loopback devices, as well as IP address, DHCP configuration, and domain information.[^7]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [SUNBURST](https://attack.mitre.org/software/S0559) obfuscated collected system information using a FNV-1a + XOR algorithm.[^7]  |
| [[Image File Execution Options Injection\|T1546.012]] | Image File Execution Options Injection | [SUNBURST](https://attack.mitre.org/software/S0559) created an Image File Execution Options (IFEO) Debugger registry value for the process `dllhost.exe` to trigger the installation of [Cobalt Strike](https://attack.mitre.org/software/S0154).[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [SUNBURST](https://attack.mitre.org/software/S0559) used Rundll32 to execute payloads.[^1]   |
| [[Compression\|T1027.015]] | Compression | [SUNBURST](https://attack.mitre.org/software/S0559) strings were compressed and encoded in Base64.[^8]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected a list of service names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists.[^7]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SUNBURST](https://attack.mitre.org/software/S0559) created VBScripts that were named after existing services or folders to blend into legitimate activities.[^1]   |
| [[Code Signing\|T1553.002]] | Code Signing | [SUNBURST](https://attack.mitre.org/software/S0559) was digitally signed by SolarWinds from March - May 2020.[^7]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected a list of process names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists.[^7]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [SUNBURST](https://attack.mitre.org/software/S0559) masqueraded its network traffic as the Orion Improvement Program (OIP) protocol.[^7]  |
| [[Junk Data\|T1001.001]] | Junk Data | [SUNBURST](https://attack.mitre.org/software/S0559) added junk bytes to its C2 over HTTP.[^7]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [SUNBURST](https://attack.mitre.org/software/S0559) used VBScripts to initiate the execution of payloads.[^1]  |
| [[DNS\|T1071.004]] | DNS | [SUNBURST](https://attack.mitre.org/software/S0559) used DNS for C2 traffic designed to mimic normal SolarWinds API communications.[^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SUNBURST](https://attack.mitre.org/software/S0559) had a command to delete files.[^7] [^8]  |
| [[Clear Network Connection History and Configurations\|T1070.007]] | Clear Network Connection History and Configurations | [SUNBURST](https://attack.mitre.org/software/S0559) also removed the firewall rules it created during execution.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [SUNBURST](https://attack.mitre.org/software/S0559) checked the domain name of the compromised host to verify it was running in a real environment.[^8]  |
| [[Query Registry\|T1012]] | Query Registry | [SUNBURST](https://attack.mitre.org/software/S0559) collected the registry value `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MachineGuid` from compromised hosts.[^7]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) checked for a variety of antivirus/endpoint detection agents prior to execution.[^8] [^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SUNBURST](https://attack.mitre.org/software/S0559) collected the username from a compromised host.[^7] [^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SUNBURST](https://attack.mitre.org/software/S0559) delivered different payloads, including [TEARDROP](https://attack.mitre.org/software/S0560) in at least one instance.[^7]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [SUNBURST](https://attack.mitre.org/software/S0559) source code used generic variable names and pre-obfuscated strings, and was likely sanitized of developer comments before being added to [SUNSPOT](https://attack.mitre.org/software/S0562).[^11]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SUNBURST](https://attack.mitre.org/software/S0559) communicated via HTTP GET or HTTP POST requests to third party servers for C2.[^7]  |
| [[Steganography\|T1001.002]] | Steganography | [SUNBURST](https://attack.mitre.org/software/S0559) C2 data attempted to appear as benign XML related to .NET assemblies or as a faux JSON blob.[^7] [^5] [^2]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [SUNBURST](https://attack.mitre.org/software/S0559) dynamically resolved C2 infrastructure for randomly-generated subdomains within a parent domain.[^7]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [SUNBURST](https://attack.mitre.org/software/S0559) removed HTTP proxy registry values to clean up traces of execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^2]: [Symantec Sunburst Sending Data January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-sunburst-sending-data)


[^3]: Solorigate


[^4]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^5]: [FireEye SUNBURST Additional Details Dec 2020](https://www.fireeye.com/blog/threat-research/2020/12/sunburst-additional-technical-details.html)


[^6]: SUNBURST


[^7]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^8]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^9]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


[^10]: [SolarWinds Sunburst Sunspot Update January 2021](https://orangematter.solarwinds.com/2021/01/11/new-findings-from-our-investigation-of-sunburst/)


[^11]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


