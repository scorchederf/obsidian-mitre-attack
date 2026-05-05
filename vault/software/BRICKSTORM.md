---
aliases: 
    - S9015
    
mitre-attack: https://attack.mitre.org/software/S9015
---

## S9015

[BRICKSTORM](https://attack.mitre.org/software/S9015) is a cross-platform backdoor with variants written in Go and Rust that facilitates command and control, the ingress transfer of other malware, and the exfiltration of data.[^5] [^7] [^2] [^6]  [BRICKSTORM](https://attack.mitre.org/software/S9015) has also been created from a .NET application using ahead-of-time (AOT) compilation to blend in within victim environments.[^5]    [BRICKSTORM](https://attack.mitre.org/software/S9015) was first observed in April 2024.[^1]  [BRICKSTORM](https://attack.mitre.org/software/S9015) has previously been leveraged by People's Republic of China (PRC) state-nexus actors identified as UNC6201, UNC5221, WARP PANDA, PunyToad, and SYLVANITE.[^10] [^9] [^5] [^8] [^3] [^4] [^2] [^6] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BRICKSTORM](https://attack.mitre.org/software/S9015) has utilized Go libraries to include Garble to obfuscate code.[^7] [^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BRICKSTORM](https://attack.mitre.org/software/S9015) has uploaded files from the victim system to C2 servers.[^9] [^5] [^7] [^1] [^3] [^2] [^6]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [BRICKSTORM](https://attack.mitre.org/software/S9015) has appeared to resemble legitimate processes to include the vCenter process `vami-http`.[^9] [^1] [^6]  [BRICKSTORM](https://attack.mitre.org/software/S9015) has also leveraged legitimate names of VMware vSphere platform such as `vmsrc` or `vmware-sphere`.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BRICKSTORM](https://attack.mitre.org/software/S9015) has communicated to hardcoded C2 through WebSockets (WSS) to include domains associated with Cloudflare Workers.[^9] [^5] [^7] [^1] [^3] [^6]   [BRICKSTORM](https://attack.mitre.org/software/S9015) has also leveraged Gorilla mux library to serve its HTTP API calls.[^3]  |
| [[Relocate Malware\|T1070.010]] | Relocate Malware | [BRICKSTORM](https://attack.mitre.org/software/S9015) has copied itself to the `usr/sbin/` folder.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BRICKSTORM](https://attack.mitre.org/software/S9015) has the ability to check if it is running as an active child process through the detection of a specific environment variable.[^5]  |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | [BRICKSTORM](https://attack.mitre.org/software/S9015) has checked hard-coded paths of `/etc/sysconfig/` or `/etc/sysconfig/network` prior to execution and loading file contents from that path.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BRICKSTORM](https://attack.mitre.org/software/S9015) has utilized XOR cipher encryption to hide key strings within their code, to include IPv4 addresses of public DNS-over-HTTPS (DOH) servers.[^5]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [BRICKSTORM](https://attack.mitre.org/software/S9015) has impaired command logging through the use of `dev/null` which prevents generating output from the command and does not wait for input.[^5]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [BRICKSTORM](https://attack.mitre.org/software/S9015) has communicated with C2 infrastructure via TLS.[^9] [^5] [^7] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BRICKSTORM](https://attack.mitre.org/software/S9015) has decoded its encrypted C2 traffic prior to execution.[^9] [^5] [^7] [^2] [^6]  [BRICKSTORM](https://attack.mitre.org/software/S9015) also has the ability to decode its obfuscated payload before execution.[^7]  |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | [BRICKSTORM](https://attack.mitre.org/software/S9015) has created a new background session and has spawned a child process of a parent process when it determines it is not running in its intended state.[^5]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [BRICKSTORM](https://attack.mitre.org/software/S9015) has utilized a SOCKS proxy to tunnel access within the victim network and exfiltrate files from internal shares, code repositories, and other endpoints.[^9] [^5] [^7] [^1] [^3] [^2] [^6]   [BRICKSTORM](https://attack.mitre.org/software/S9015) has also leveraged Yamux for combining multiple concurrent logical streams over a single a socket.[^5] [^3] [^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BRICKSTORM](https://attack.mitre.org/software/S9015) has the ability to delete files and directories.[^5]  [BRICKSTORM](https://attack.mitre.org/software/S9015) also has deleted installer files after execution to reduce detection.[^7] [^1] [^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [BRICKSTORM](https://attack.mitre.org/software/S9015) has leveraged Base64 to encode C2 communications.[^3] [^2]  |
| [[Delay Execution\|T1678]] | Delay Execution | [BRICKSTORM](https://attack.mitre.org/software/S9015) has embedded delayed-start logic that attempts to circumvent detection for long-term persistence.[^7] [^3]  [BRICKSTORM](https://attack.mitre.org/software/S9015) has been observed configured with a “delay” timer built-in that waited for a hard-coded date months in the future before beginning to beacon to the configured C2 domain.[^6]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [BRICKSTORM](https://attack.mitre.org/software/S9015) has utilized DNS services sslip.io and nip.io to resolve C2 IP addresses.[^6]    |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BRICKSTORM](https://attack.mitre.org/software/S9015) has the ability to download files from the Adversaries C2 server to the compromised system.[^5] [^1] [^3] [^6]  |
| [[Web Service\|T1102]] | Web Service | [BRICKSTORM](https://attack.mitre.org/software/S9015) has leveraged DNS web services to resolve C2 IP addresses including sslip.io and nip.io.[^6]   [BRICKSTORM](https://attack.mitre.org/software/S9015) has also utilized Cloudflare Workers for C2 communications.[^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BRICKSTORM](https://attack.mitre.org/software/S9015) has identified specific files and directories within targeted hosts and systems for modification, execution, collection and exfiltration.[^9] [^5] [^7] [^1] [^3] [^6]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [BRICKSTORM](https://attack.mitre.org/software/S9015) has leveraged SOCKS Proxy to pivot into victim networks in attempts to resemble legitimate administrative traffic.[^9] [^5] [^7] [^1] [^3] [^6]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [BRICKSTORM](https://attack.mitre.org/software/S9015) has executed shell commands using `/bin/sh`.[^1]  |
| [[DNS\|T1071.004]] | DNS | [BRICKSTORM](https://attack.mitre.org/software/S9015) has used DNS over HTTPS to resolve C2 infrastructure and obscure DNS traffic from inspection.[^9] [^5] [^7] [^1] [^3]  |
| [[Service Stop\|T1489]] | Service Stop | [BRICKSTORM](https://attack.mitre.org/software/S9015) has terminated an existing process to ensure that its own new process can execute.[^5]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BRICKSTORM](https://attack.mitre.org/software/S9015) has commands that allow the actor download files from the compromised host to the C2 server, and to also download specific sections of a file.[^5]  |




## References

[^1]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^2]: [Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)


[^3]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)


[^4]: [Google BRICKSTORM GRIMBOLT UNC5221 UNC6201 February 2026](https://cloud.google.com/blog/topics/threat-intelligence/unc6201-exploiting-dell-recoverpoint-zero-day)


[^5]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^6]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)


[^7]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)


[^8]: [Dragos SYLVANITE MuddyWater Electrum March 2026](https://hub.dragos.com/hubfs/2026_YIR_ExecutiveBriefing%20O_G.pdf?hsLang=en)


[^9]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)


[^10]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


