---
aliases: 
    - T1675
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/esxi
mitre-attack: kb/mitre/attack/techniques/T1675-ESXi_Administration_Command
tactic: 
     - Execution
platforms:
     - ESXi
permissions required:
     - none
---

## Description

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux.[^4]  <br><br>Adversaries may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`,  `ListFileInGuest`, and `InitiateFileTransferFromGuest`.[^1] [^3]  This may enable follow-on behaviors on the guest VMs, such as [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|File and Directory Discovery]], [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|Data from Local System]], or [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|OS Credential Dumping]]. 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | If not required, restrict the permissions of users to perform Guest Operations on ESXi-hosted VMs.[^2]  |






> [!info]- References
> [^1]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)

> [^2]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)

> [^3]: [Broadcom Running Guest OS Operations](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/web-services-sdk-programming-guide/virtual-machine-guest-operations/running-guest-os-operations.html)

> [^4]: [Broadcom VMware Tools Services](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-4-0/vmware-tools-administration-12-4-0/introduction-to-vmware-tools/vmware-tools-service.html)


