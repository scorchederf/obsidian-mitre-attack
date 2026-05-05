---
aliases: 
    - S1218
    
mitre-attack: https://attack.mitre.org/software/S1218
---

## S1218

[VIRTUALPIE](https://attack.mitre.org/software/S1218) is a lightweight backdoor written in Python that spawns an IPv6 listener on a VMware ESXi server and features command line execution, file transfer,  and reverse shell capabilities. [VIRTUALPIE](https://attack.mitre.org/software/S1218) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who installed it via malicious vSphere Installation Bundles (VIBs).[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [VIRTUALPIE](https://attack.mitre.org/software/S1218) is a Python-based backdoor malware.[^4] [^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [VIRTUALPIE](https://attack.mitre.org/software/S1218) can use a custom RC4 encrypted protocol for C2 communications.[^4] [^3]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [VIRTUALPIE](https://attack.mitre.org/software/S1218) has created listeners on hard coded TCP port 546.[^4]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [VIRTUALPIE](https://attack.mitre.org/software/S1218) has file transfer capabilities.[^4]  |
| [[vSphere Installation Bundles\|T1505.006]] | vSphere Installation Bundles | [VIRTUALPIE](https://attack.mitre.org/software/S1218) has been installed on VMware ESXi servers through malicious vSphere Installation Bundles (VIBs).[^4]  |
| [[Hypervisor CLI\|T1059.012]] | Hypervisor CLI | [VIRTUALPIE](https://attack.mitre.org/software/S1218) is capable of command line execution on compromised ESXi servers.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^2]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)


[^3]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^4]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


