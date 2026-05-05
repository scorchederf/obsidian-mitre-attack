---
aliases: 
    - T1016
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [[kb/mitre/attack/software/S0099-Arp\|Arp]], [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]]/[[kb/mitre/attack/software/S0101-ifconfig\|ifconfig]], [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]], and [[kb/mitre/attack/software/S0103-route\|route]].<br><br>Adversaries may also leverage a [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. `show ip route`, `show ip interface`).[^11] [^13]  On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.[^23] <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|System Network Configuration Discovery]] during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0099-Arp\|S0099]] | Arp | [[kb/mitre/attack/software/S0099-Arp\|Arp]] can be used to display ARP configuration information on the host.[^18]  |
| [[kb/mitre/attack/software/S0100-ipconfig\|S0100]] | ipconfig | [[kb/mitre/attack/software/S0100-ipconfig\|ipconfig]] can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |
| [[kb/mitre/attack/software/S0101-ifconfig\|S0101]] | ifconfig | [[kb/mitre/attack/software/S0101-ifconfig\|ifconfig]] can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |
| [[kb/mitre/attack/software/S0102-nbtstat\|S0102]] | nbtstat | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover local NetBIOS domain names. |
| [[kb/mitre/attack/software/S0103-route\|S0103]] | route | [[kb/mitre/attack/software/S0103-route\|route]] can be used to discover routing configuration information. |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^17]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can retrieve the contents of the IP routing table as well as information about the Windows domain.[^10] [^1]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^9]  |
| [[kb/mitre/attack/software/S0359-Nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^16]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^22] [^4]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] can enumerate network adapter information.[^15]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.[^6]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can collect DNS information from the targeted system.[^21]  |
| [[kb/mitre/attack/software/S0552-AdFind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can extract subnet information from Active Directory.[^5] [^2] [^3]  |
| [[kb/mitre/attack/software/S0590-NBTscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can be used to collect MAC addresses.[^19] [^8] 	 |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] has the ability to gather network configuration information.[^20]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.[^12]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can enumerate the NetBIOS name on targeted machines.[^7]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can capture information from each session with a victim including the public IP used to access the server and the user agent.[^14]  |






## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1016.001-Internet_Connection_Discovery\|T1016.001]] | Internet Connection Discovery |
| [[kb/mitre/attack/techniques/T1016.002-Wi-Fi_Discovery\|T1016.002]] | Wi-Fi Discovery |




> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)

> [^3]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)

> [^4]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^5]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)

> [^6]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^7]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)

> [^8]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^9]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^10]: [Github Koadic](https://github.com/offsecginger/koadic)

> [^11]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^12]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^13]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)

> [^14]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)

> [^15]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^16]: [Nltest Manual](https://ss64.com/nt/nltest.html)

> [^17]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^18]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)

> [^19]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^20]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)

> [^21]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^22]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^23]: [Trellix Rnasomhouse 2024](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)


