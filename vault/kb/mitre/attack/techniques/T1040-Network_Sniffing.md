---
aliases: 
    - T1040
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1040-Network_Sniffing
tactic: 
     - Credential Access - Discovery
platforms:
     - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.<br><br>Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|Name Resolution Poisoning and SMB Relay]], can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.<br><br>Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent [[kb/mitre/attack/tactics/TA0008-Lateral_Movement\|Lateral Movement]] and/or [[kb/mitre/attack/tactics/TA0005-Stealth\|Stealth]] activities. Adversaries may likely also utilize network sniffing during [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] (AiTM) to passively gain additional knowledge about the environment.<br><br>In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.[^10] [^1] [^4]  Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic.[^11] [^3]  The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.[^11] <br><br>On network devices, adversaries may perform network captures using [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] commands such as `monitor capture`.[^13] [^6] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0174-Responder\|S0174]] | Responder | [[kb/mitre/attack/software/S0174-Responder\|Responder]] captures hashes and credentials that are sent to the system after the name services have been poisoned.[^9]  |
| [[kb/mitre/attack/software/S0357-Impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-Impacket\|Impacket]] can be used to sniff network traffic via an interface or raw socket.[^12]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can be used to conduct packet captures on target hosts.[^8]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for taking packet captures on compromised hosts.[^2]  |
| [[kb/mitre/attack/software/S0590-NBTscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-NBTscan\|NBTscan]] can dump and print whole packet content.[^5] [^7] 	 |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | In cloud environments, ensure that users are not granted permissions to create or modify traffic mirrors unless this is explicitly required. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Deny direct access of broadcasts and multicast sniffing, and prevent attacks such as [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|Name Resolution Poisoning and SMB Relay]] |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication wherever possible. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |






> [!info]- References
> [^1]: [GCP Packet Mirroring](https://cloud.google.com/vpc/docs/packet-mirroring)

> [^2]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^3]: [SpecterOps AWS Traffic Mirroring](https://posts.specterops.io/through-the-looking-glass-part-1-f539ae308512)

> [^4]: [Azure Virtual Network TAP](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview)

> [^5]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)

> [^6]: [capture_embedded_packet_on_software](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html)

> [^7]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)

> [^8]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^9]: [GitHub Responder](https://github.com/SpiderLabs/Responder)

> [^10]: [AWS Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html)

> [^11]: [Rhino Security Labs AWS VPC Traffic Mirroring](https://rhinosecuritylabs.com/aws/abusing-vpc-traffic-mirroring-in-aws/)

> [^12]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)

> [^13]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


