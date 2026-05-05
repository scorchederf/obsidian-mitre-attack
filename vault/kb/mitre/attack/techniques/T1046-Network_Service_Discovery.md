---
aliases: 
    - T1046
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1046-Network_Service_Discovery
tactic: 
     - Discovery
platforms:
     - Containers - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.[^3]    <br><br>Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.<br><br>Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as `dns-sd -B _ssh._tcp .`) to find other systems broadcasting the ssh service.[^10] [^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a built-in module for port scanning.[^12]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can scan for open TCP ports on the target network.[^4]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can perform port scans from an infected host.[^8]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can perform port scans from an infected host.[^13]  |
| [[kb/mitre/attack/software/S0590-NBTscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can be used to scan IP networks.[^2] [^7]  |
| [[kb/mitre/attack/software/S0683-Peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can initiate a port scan against a given IP address.[^11]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can scan for open ports on a compromised machine.[^6]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can conduct port scanning against targeted systems.[^5]  |
| [[kb/mitre/attack/software/S1144-FRP\|S1144]] | FRP | As part of load balancing [[kb/mitre/attack/software/S1144-FRP\|FRP]] can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.[^1]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Ensure proper network segmentation is followed to protect critical servers and devices. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Use network intrusion detection/prevention systems to detect and prevent remote service scans. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation. |






> [!info]- References
> [^1]: [FRP GitHub](https://github.com/fatedier/frp)

> [^2]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^3]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)

> [^4]: [Github Koadic](https://github.com/offsecginger/koadic)

> [^5]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^6]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^7]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^8]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^9]: [macOS APT Activity Bradley](https://themittenmac.com/what-does-apt-activity-look-like-on-macos/)

> [^10]: [apple doco bonjour description](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html)

> [^11]: [Peirates GitHub](https://github.com/inguardians/peirates)

> [^12]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^13]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


