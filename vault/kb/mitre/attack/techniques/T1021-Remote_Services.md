---
aliases: 
    - T1021
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1021-Remote_Services
tactic: 
     - Lateral Movement
platforms:
     - Linux - macOS - Windows - IaaS - ESXi
permissions required:
     - none
---

## Description

Adversaries may use [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]] to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.<br><br>In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP).[^11] [^6]  They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter. <br><br>Legitimate applications (such as [[kb/mitre/attack/techniques/T1072-Software_Deployment_Tools\|Software Deployment Tools]] and other administrative programs) may utilize [[kb/mitre/attack/techniques/T1021-Remote_Services\|Remote Services]] to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including [[kb/mitre/attack/techniques/T1021.005-VNC\|VNC]] to send the screen and control buffers and [[kb/mitre/attack/techniques/T1021.004-SSH\|SSH]] for secure file transfer.[^8] [^9] [^4]  Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data.[^12] [^1] [^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has the ability to use RPC for lateral movement.[^7]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit the accounts that may use remote services. Limit the permissions for accounts that are at higher risk of compromise; for example, configure SSH so users can only run specific programs. |
| [[kb/mitre/attack/mitigations/M1027-Password_Policies\|M1027]] | Password Policies | Do not reuse local administrator account passwords across systems. Ensure password complexity and uniqueness such that the passwords cannot be cracked or guessed. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication on remote service logons where possible. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Prevent unnecessary remote access to file shares, hypervisors, sensitive systems, etc. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc.[^3]  |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | If remote services, such as the ability to make direct connections to cloud virtual machines, are not required, disable these connection types where feasible. On ESXi servers, consider enabling lockdown mode, which disables direct access to an ESXi host and requires that the host be managed remotely using vCenter.[^10] [^5]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1021.001-Remote_Desktop_Protocol\|T1021.001]] | Remote Desktop Protocol |
| [[kb/mitre/attack/techniques/T1021.002-SMB_Windows_Admin_Shares\|T1021.002]] | SMB／Windows Admin Shares |
| [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|T1021.003]] | Distributed Component Object Model |
| [[kb/mitre/attack/techniques/T1021.004-SSH\|T1021.004]] | SSH |
| [[kb/mitre/attack/techniques/T1021.005-VNC\|T1021.005]] | VNC |
| [[kb/mitre/attack/techniques/T1021.006-Windows_Remote_Management\|T1021.006]] | Windows Remote Management |
| [[kb/mitre/attack/techniques/T1021.007-Cloud_Services\|T1021.007]] | Cloud Services |
| [[kb/mitre/attack/techniques/T1021.008-Direct_Cloud_VM_Connections\|T1021.008]] | Direct Cloud VM Connections |




> [!info]- References
> [^1]: [Lockboxx ARD 2019](http://lockboxx.blogspot.com/2019/07/macos-red-teaming-206-ard-apple-remote.html)

> [^2]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)

> [^3]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)

> [^4]: [Apple Remote Desktop Admin Guide 3.3](https://images.apple.com/remotedesktop/pdf/ARD_Admin_Guide_v3.3.pdf)

> [^5]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)

> [^6]: [TechNet Remote Desktop Services](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)

> [^7]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^8]: [Remote Management MDM macOS](https://support.apple.com/en-us/HT209161)

> [^9]: [Kickstart Apple Remote Desktop commands](https://support.apple.com/en-us/HT201710)

> [^10]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)

> [^11]: [SSH Secure Shell](https://www.ssh.com/ssh)

> [^12]: [FireEye 2019 Apple Remote Desktop](https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html)


