---
aliases: 
    - S9024
    
mitre-attack: https://attack.mitre.org/software/S9024
---

## S9024

[SPAWNCHIMERA](https://attack.mitre.org/software/S9024) is a backdoor that supports command and control and can inject malicious components into native processes.[^5] [^3] [^2]   [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) It incorporates capabilities from multiple tools within the SPAWN malware family, including SPAWNANT, SPAWNMOLE, and SPAWNSNAIL.[^6] [^3] [^2]   [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) was first reported in April 2024.[^3]  [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has been observed in activity attributed to People's Republic of China (PRC) state-sponsored threat actors, including UNC5221..[^6] [^4] [^3] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has decoded a XOR encoded private key.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has searched for running processes to include web or dsmdm.[^5] [^3]  |
| [[Delay Execution\|T1678]] | Delay Execution | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has used delayed execution to pause for a defined interval before performing environment discovery, repeatedly checking for specific processes, such as the `dslogserver` process, prior to continuing execution. [^5]  |
| [[Web Shell\|T1505.003]] | Web Shell | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has created web shells that facilitate actions on the victim host.[^5]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) can persist across system upgrades by hijacking the execution flow of dspkginstall, a binary used during the system upgrade process.[^6] [^3]  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has modified the boot process files within `/tmp/coreboot_fs/bin/init` to establish persistence.[^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has checked where SELinux is enabled on the targeted host.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has extracted the device’s Linux kernel image (vmlinux).[^5] [^4] [^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has created SSH tunnels to facilitate C2 communications.[^5] [^6] [^3]  |
| [[Python\|T1059.006]] | Python | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has searched the contents of two Python files scanner.py and scanner_legacy.py by searching for specific lines and replacing them with values that reduce their ability to track mismatches or new files.[^5]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has been compiled as a Position Independent Executable (PIE) to use a third-party library for injection.[^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has encoded a private key with XOR.[^2]  [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has also encrypted data to be extracted using AES encryption.[^4] [^1]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has executed only in memory and hooked itself into existing processes on the victim device to include the web process.[^5] [^3] [^2]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has leveraged IPC using a UNIX domain socket between the dsmdm process and the web process.[^3] [^2]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has monitored and filtered network traffic on compromised edge devices, allowing legitimate traffic to pass while redirecting attacker-controlled traffic to infrastructure under adversary control. [^6] [^3]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has disabled logging and log forwarding on Ivanti devices targeting the `dslogserver` process.[^5] [^4] [^3] [^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has the ability to bind on a localhost and listen on port 8300.[^3] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has deleted generated files and folders from victim devices.[^5]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has modified the Ivanti Integrity Checker Tool to evade detection.[^5] [^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has generated RSA keys against modified files to sign the manifest file, so they appear legitimate.[^5] [^6]   |
| [[Timestomp\|T1070.006]] | Timestomp | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has updated the timestamp using the `touch` command.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has obtained system information such as release, uptime, and current time.[^3]    |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has fixed a buffer overflow vulnerability (CVE-2025-0282) by hooking the strncpy function and limiting the size to 256 to prevent other actors from leveraging the exploit.[^2]   [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has converted its process name to hexadecimal and verifies an added value which is triggered when the first byte of the source copied to the fixed strncpy function matches `0x04050203`.[^2]  |




## References

[^1]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^2]: [JPCERT SPAWNCHIMERA Ivanti February 2025](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)


[^3]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^4]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^5]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)


[^6]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


