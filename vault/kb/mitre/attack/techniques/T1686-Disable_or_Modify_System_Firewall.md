---
aliases: 
    - T1686
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1686-Disable_or_Modify_System_Firewall
tactic: 
     - Defense Impairment
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies, or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles, altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port.[^1] <br><br>Adversaries may disable or modify firewalls using different behaviors, depending on the platform. For example, in ESXi, firewall rules may be modified directly via the esxcli (e.g., via esxcli network firewall set) or via the vCenter user interface.[^5] [^4] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0108-netsh\|S0108]] | netsh | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to disable local firewall settings.[^3] [^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Ensure proper user permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1686.001-Cloud_Firewall\|T1686.001]] | Cloud Firewall |
| [[kb/mitre/attack/techniques/T1686.002-Network_Device_Firewall\|T1686.002]] | Network Device Firewall |
| [[kb/mitre/attack/techniques/T1686.003-Windows_Host_Firewall\|T1686.003]] | Windows Host Firewall |




> [!info]- References
> [^1]: [change_rdp_port_conti](https://x.com/TheDFIRReport/status/1498657772254240768)

> [^2]: [TechNet Netsh Firewall](https://technet.microsoft.com/en-us/library/cc771046(v=ws.10).aspx)

> [^3]: [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)

> [^4]: [Trellix Rnasomhouse 2024](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)

> [^5]: [Broadcom ESXi Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/add-allowed-ip-addresses-for-an-esxi-host-by-using-the-vmware-host-client.html)


