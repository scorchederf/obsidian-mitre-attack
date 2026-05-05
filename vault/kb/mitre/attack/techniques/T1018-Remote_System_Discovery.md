---
aliases: 
    - T1018
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1018-Remote_System_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [[kb/mitre/attack/software/S0097-Ping\|Ping]], `net view` using [[kb/mitre/attack/software/S0039-Net\|Net]], or, on ESXi servers, `esxcli network diag ping`.<br><br>Adversaries may also analyze data from local host files (ex: `C:\Windows\System32\Drivers\etc\hosts` or `/etc/hosts`) or other passive means (such as local [[kb/mitre/attack/software/S0099-Arp\|Arp]] cache entries) in order to discover the presence of remote systems in an environment.<br><br>Adversaries may also target discovery of network infrastructure as well as leverage [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] commands on network devices to gather detailed information about systems within a network (e.g. `show cdp neighbors`, `show arp`).[^9] [^17]   <br>


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-Net\|S0039]] | Net | Commands such as `net view` can be used in [[kb/mitre/attack/software/S0039-Net\|Net]] to gather information about available remote systems.[^4]  |
| [[kb/mitre/attack/software/S0097-Ping\|S0097]] | Ping | [[kb/mitre/attack/software/S0097-Ping\|Ping]] can be used to identify remote systems within a network.[^7]  |
| [[kb/mitre/attack/software/S0099-Arp\|S0099]] | Arp | [[kb/mitre/attack/software/S0099-Arp\|Arp]] can be used to display a host's ARP cache, which may include address resolutions for remote systems.[^14] [^6]  |
| [[kb/mitre/attack/software/S0359-Nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate remote domain controllers using options such as `/dclist` and `/dsgetdc`.[^13]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover active IP addresses, along with the machine name, within a targeted network.[^18]  |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] can enumerate and collect the properties of domain computers, including domain controllers.[^15]  |
| [[kb/mitre/attack/software/S0552-AdFind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] has the ability to query Active Directory for computers.[^3] [^1] [^2] [^5]  |
| [[kb/mitre/attack/software/S0590-NBTscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can list NetBIOS computer names.[^16] [^8] 	 |
| [[kb/mitre/attack/software/S0684-ROADTools\|S0684]] | ROADTools | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] can enumerate Azure AD systems and devices.[^11]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate and collect the properties of domain computers.[^12]  |








> [!info]- References
> [^1]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)

> [^2]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)

> [^3]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)

> [^4]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)

> [^5]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)

> [^6]: [Palo Alto ARP](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-reference/cortex-xdr-analytics-alert-reference/uncommon-arp-cache-listing-via-arp-exe.html)

> [^7]: [TechNet Ping](https://technet.microsoft.com/en-us/library/bb490968.aspx)

> [^8]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^9]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^10]: [Elastic - Koadiac Detection with EQL](https://www.elastic.co/security-labs/embracing-offensive-tooling-building-detections-against-koadic-using-eql)

> [^11]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)

> [^12]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^13]: [Nltest Manual](https://ss64.com/nt/nltest.html)

> [^14]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)

> [^15]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)

> [^16]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^17]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)

> [^18]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


