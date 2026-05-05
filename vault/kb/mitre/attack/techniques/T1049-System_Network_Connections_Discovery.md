---
aliases: 
    - T1049
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1049-System_Network_Connections_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. <br><br>An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.[^3] [^1] [^4]  Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.<br><br>Utilities and commands that acquire this information include [[kb/mitre/attack/software/S0104-netstat\|netstat]], "net use," and "net session" with [[kb/mitre/attack/software/S0039-Net\|Net]]. In Mac and Linux, [[kb/mitre/attack/software/S0104-netstat\|netstat]] and `lsof` can be used to list current connections. `who -a` and `w` can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] may be used (e.g. `show ip sockets`, `show tcp brief`).[^13]  On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.[^6] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0039-Net\|S0039]] | Net | Commands such as `net use` and `net session` can be used in [[kb/mitre/attack/software/S0039-Net\|Net]] to gather information about network connections from a particular host.[^14]  |
| [[kb/mitre/attack/software/S0102-nbtstat\|S0102]] | nbtstat | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover current NetBIOS sessions. |
| [[kb/mitre/attack/software/S0104-netstat\|S0104]] | netstat | [[kb/mitre/attack/software/S0104-netstat\|netstat]] can be used to enumerate local network connections, including active TCP connections and other network statistics.[^5]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] has a built-in utility command for `netstat`, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.[^12]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can enumerate the current network connections of a host.[^8]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0104-netstat\|netstat]] to enumerate TCP and UDP connections.[^11]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] used the Windows function `GetExtendedUdpTable` to detect connected UDP endpoints.[^9]  |
| [[kb/mitre/attack/software/S0488-CrackMapExec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-CrackMapExec\|CrackMapExec]] can discover active sessions for a targeted system.[^7]  |
| [[kb/mitre/attack/software/S0633-Sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-Sliver\|Sliver]] can collect network connection information.[^15]  |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | Once inside a Virtual Private Cloud, [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can attempt to identify DirectConnect, VPN, or VPC Peering.[^10]  |
| [[kb/mitre/attack/software/S1144-FRP\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-FRP\|FRP]] can use a dashboard and U/I to display the status of connections from the FRP client and server.[^2]  |








> [!info]- References
> [^1]: [Microsoft Azure Virtual Network Overview](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)

> [^2]: [FRP GitHub](https://github.com/fatedier/frp)

> [^3]: [Amazon AWS VPC Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

> [^4]: [Google VPC Overview](https://cloud.google.com/vpc/docs/vpc)

> [^5]: [TechNet Netstat](https://technet.microsoft.com/en-us/library/bb490947.aspx)

> [^6]: [Sygnia ESXi Ransomware 2025](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)

> [^7]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)

> [^8]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^9]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^10]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)

> [^11]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^12]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^13]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^14]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)

> [^15]: [GitHub Sliver Netstat](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)


