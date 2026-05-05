---
aliases: 
    - M1030
    
mitre-attack: https://attack.mitre.org/mitigations/M1030
---

## M1030

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.<br><br>Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures:<br><br>Segment Critical Systems:<br><br>- Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers.<br>- Use VLANs, firewalls, or routers to enforce logical separation.<br><br>Implement DMZ for Public-Facing Services:<br><br>- Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems.<br>- Apply strict firewall rules to filter traffic between the DMZ and internal networks.<br><br>Use Cloud-Based Segmentation:<br><br>- In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules.<br>- Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments.<br><br>Apply Microsegmentation for Workloads:<br><br>- Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement.<br><br>Restrict Traffic with ACLs and Firewalls:<br><br>- Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies.<br>- Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic.<br><br>Monitor and Audit Segmented Networks:<br><br>- Regularly review firewall rules, ACLs, and segmentation policies.<br>- Monitor network flows for anomalies to ensure segmentation is effective.<br><br>Test Segmentation Effectiveness:<br><br>- Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Runtime Data Manipulation\|T1565.003]] | Runtime Data Manipulation | Identify critical business and system processes that may be targeted by adversaries and work to isolate and secure those systems against unauthorized access and tampering. |
| [[Container and Resource Discovery\|T1613]] | Container and Resource Discovery | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[Account Manipulation\|T1098]] | Account Manipulation | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| [[Create Account\|T1136]] | Create Account | Configure access controls and firewalls to limit access to domain controllers and systems used to create and manage accounts. |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | Do not leave RDP accessible from the internet. Enable firewall rules to block RDP traffic between network security zones within a network. |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | Segment externally facing servers and services from the rest of the network with a DMZ or on separate hosting infrastructure. |
| [[Network Device Configuration Dump\|T1602.002]] | Network Device Configuration Dump | Segregate SNMP traffic on a separate management network.[^1]   |
| [[Cloud Account\|T1136.003]] | Cloud Account | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | Enable firewall rules to block RDP traffic between network security zones within a network. |
| [[Service Stop\|T1489]] | Service Stop | Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions. |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | Segment networks and systems appropriately to reduce access to critical systems and services to controlled methods. |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.[^2]  |
| [[Build Image on Host\|T1612]] | Build Image on Host | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | Employ network segmentation for sensitive domains.[^3] . |
| [[Additional Cloud Credentials\|T1098.001]] | Additional Cloud Credentials | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| [[Deploy Container\|T1610]] | Deploy Container | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | Ensure proper network segmentation is followed to protect critical servers and devices. |
| [[Remote Service Session Hijacking\|T1563]] | Remote Service Session Hijacking | Enable firewall rules to block unnecessary traffic between network security zones within a network. |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports for that particular network segment. |
| [[External Remote Services\|T1133]] | External Remote Services | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Ensure proper system isolation for critical network systems through use of firewalls. |
| [[Wi-Fi Networks\|T1669]] | Wi-Fi Networks | Network segmentation can be used to isolate infrastructure components that do not require broad network access. Separate networking environments for Wi-Fi and Ethernet-wired networks, particularly where Ethernet-based networks allow for access to sensitive resources. |
| [[Distributed Component Object Model\|T1021.003]] | Distributed Component Object Model | Enable Windows firewall, which prevents DCOM instantiation by default. |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.[^2]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | Network segmentation can be used to isolate infrastructure components that do not require broad network access. This may mitigate, or at least alleviate, the scope of AiTM activity. |
| [[Container API\|T1552.007]] | Container API | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[Data from Configuration Repository\|T1602]] | Data from Configuration Repository | Segregate SNMP traffic on a separate management network.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports and through proper network gateway systems. Also ensure hosts are only provisioned to communicate over authorized interfaces. |
| [[Data Manipulation\|T1565]] | Data Manipulation | Identify critical business and system processes that may be targeted by adversaries and work to isolate and secure those systems against unauthorized access and tampering. |
| [[SNMP (MIB Dump)\|T1602.001]] | SNMP (MIB Dump) | Segregate SNMP traffic on a separate management network.[^1]  |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | Network segmentation can be used to isolate infrastructure components that do not require broad network access. This may mitigate, or at least alleviate, the scope of AiTM activity. |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | If the service is necessary, lock down critical enclaves with separate WinRM infrastructure and follow WinRM best practices on use of host firewalls to restrict WinRM access to allow communication only to/from specific devices.[^4]  |
| [[Exfiltration Over Symmetric Encrypted Non-C2 Protocol\|T1048.001]] | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.[^2]  |
| [[Domain Account\|T1136.002]] | Domain Account | Configure access controls and firewalls to limit access to domain controllers and systems used to create and manage accounts. |
| [[Network Sniffing\|T1040]] | Network Sniffing | Deny direct access of broadcasts and multicast sniffing, and prevent attacks such as [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001) |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | Network segmentation can be used to isolate infrastructure components that do not require broad network access. |


## References

[^1]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^2]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^3]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^4]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


