---
aliases: 
    - S1217
    
mitre-attack: https://attack.mitre.org/software/S1217
---

## S1217

[VIRTUALPITA](https://attack.mitre.org/software/S1217) is a passive backdoor with ESXi and Linux vCenter variants capable of command execution, file transfer, and starting and stopping processes. [VIRTUALPITA](https://attack.mitre.org/software/S1217) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who leveraged malicious vSphere Installation Bundles (VIBs) for install on ESXi hypervisors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can call a Python script to run commands on a targeted guest virtual machine.[^1]  |
| [[ESXi Administration Command\|T1675]] | ESXi Administration Command | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can execute commands on guest virtual machines from compromised ESXi hypervisors.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [VIRTUALPITA](https://attack.mitre.org/software/S1217) has the ability to upload and download files.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can start and stop the `vmsyslogd` service.[^1]  |
| [[Virtual Machine Discovery\|T1673]] | Virtual Machine Discovery | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can target specific guest virtual machines for script execution.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [VIRTUALPITA](https://attack.mitre.org/software/S1217) has the ability to spawn a bash shell for script execution.[^1]  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can persist as an init.d startup service on Linux vCenter systems.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [VIRTUALPITA](https://attack.mitre.org/software/S1217) has utilized VMware service names and ports to masquerade as legitimate services.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [VIRTUALPITA](https://attack.mitre.org/software/S1217) samples have been found in `/usr/libexec/setconf/ksmd` and `/usr/bin/ksmd`, named to spoof the legitimate Kernel Same-Page Merging Daemon binary. [^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [VIRTUALPITA](https://attack.mitre.org/software/S1217) is capable of file transfer and arbitrary command execution.[^1]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [VIRTUALPITA](https://attack.mitre.org/software/S1217) can impair logging by setting the `HISTFILE` environmental variable to `0` and stopping the `vmsyslogd` service.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [VIRTUALPITA](https://attack.mitre.org/software/S1217) has created listeners on hard coded TCP ports such as 2233, 7475, and 18098.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^2]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^3]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)


