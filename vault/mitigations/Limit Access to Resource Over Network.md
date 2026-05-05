---
aliases: 
    - M1035
    
mitre-attack: https://attack.mitre.org/mitigations/M1035
---

## M1035

Restrict access to network resources, such as file shares, remote systems, and services, to only those users, accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators, RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can be implemented through the following measures:<br><br>Audit and Restrict Access:<br><br>- Regularly audit permissions for file shares, network services, and remote access tools.<br>- Remove unnecessary access and enforce least privilege principles for users and services.<br>- Use Active Directory and IAM tools to restrict access based on roles and attributes.<br><br>Deploy Secure Remote Access Solutions:<br><br>- Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections.<br>- Configure access controls to restrict connections based on time, device, and user identity.<br>- Enforce MFA for all remote access mechanisms.<br><br>Disable Unnecessary Services:<br><br>- Identify running services using tools like netstat (Windows/Linux) or Nmap.<br>- Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface.<br>- Use firewall rules to block traffic on unused ports and protocols.<br><br>Network Segmentation and Isolation:<br><br>- Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access.<br>- Restrict communication between subnets to prevent lateral movement.<br><br>Monitor and Log Access:<br><br>- Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools.<br>- Enable auditing and logging for successful and failed attempts to access restricted resources.<br><br>*Tools for Implementation*<br><br>File Share Management:<br><br>- Microsoft Active Directory Group Policies<br>- Samba (Linux/Unix file share management)<br>- AccessEnum (Windows access auditing tool)<br><br>Secure Remote Access:<br><br>- Microsoft Remote Desktop Gateway<br>- Apache Guacamole (open-source RDP/VNC gateway)<br>- Zero Trust solutions: Tailscale, Cloudflare Zero Trust<br><br>Service and Protocol Hardening:<br><br>- Nmap or Nessus for network service discovery<br>- Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols<br>- iptables or firewalld (Linux) for blocking unnecessary traffic<br><br>Network Segmentation:<br><br>- pfSense for open-source network isolation

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Pre-OS Boot\|T1542]] | Pre-OS Boot | Prevent access to file shares, remote access to systems, unnecessary services. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc. |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | Limit access to network infrastructure and resources that can be used to reshape traffic or otherwise produce AiTM conditions. |
| [[RDP Hijacking\|T1563.002]] | RDP Hijacking | Use remote desktop gateways. |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | Limit access to the Instance Metadata API using a host-based firewall such as iptables. |
| [[Build Image on Host\|T1612]] | Build Image on Host | Limit communications with the container service to local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API on port 2375. Instead, communicate with the Docker API over TLS on port 2376.[^2]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | Use remote desktop gateways. |
| [[Remote Services\|T1021]] | Remote Services | Prevent unnecessary remote access to file shares, hypervisors, sensitive systems, etc. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc.[^6]  |
| [[Hardware Additions\|T1200]] | Hardware Additions | Establish network access control policies, such as using device certificates and the 802.1x standard. [^4]  Restrict use of DHCP to registered devices to prevent unregistered devices from communicating with trusted systems. |
| [[TFTP Boot\|T1542.005]] | TFTP Boot | Restrict use of protocols without encryption or authentication mechanisms. Limit access to administrative and management interfaces from untrusted network sources.  |
| [[Container API\|T1552.007]] | Container API | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^2] [^5]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^7]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |
| [[Deploy Container\|T1610]] | Deploy Container | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API, Kubernetes API Server, and container orchestration web applications.[^2] [^5]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^7]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |
| [[External Remote Services\|T1133]] | External Remote Services | Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems. |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Limit network access to sensitive services, such as the Instance Metadata API. |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | Consider disabling Windows administrative shares. |
| [[Container and Resource Discovery\|T1613]] | Container and Resource Discovery | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^2] [^5]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^7]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | Ensure that all publicly exposed services are actually intended to be so, and restrict access to any that should only be available internally.  |
| [[ARP Cache Poisoning\|T1557.002]] | ARP Cache Poisoning | Create static ARP entries for networked devices. Implementing static ARP entries may be infeasible for large networks. |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | If possible, use a Remote Desktop Gateway to manage connections and security configuration of RDP within a network.[^1]  |
| [[Container Administration Command\|T1609]] | Container Administration Command | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^2] [^5]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^7]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |


## References

[^1]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^2]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^3]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^4]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^5]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^6]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^7]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


