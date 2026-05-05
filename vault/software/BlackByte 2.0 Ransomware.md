---
aliases: 
    - S1181
    
mitre-attack: https://attack.mitre.org/software/S1181
---

## S1181

[BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) is a replacement for [BlackByte Ransomware](https://attack.mitre.org/software/S1180). Unlike [BlackByte Ransomware](https://attack.mitre.org/software/S1180), [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) does not have a common key for victim decryption. [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) remains uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Timestomp\|T1070.006]] | Timestomp | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) can timestomp files for defense evasion and anti-forensics purposes.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) modifies the victim Registry to allow for elevated execution.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) is a ransomware variant associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) modifies volume shadow copies during execution in a way that destroys them on the victim machine.[^1]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) exploits a vulnerability in the RTCore64.sys driver (CVE-2019-16098) to enable privilege escalation and defense evasion when run as a service.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) can identify network shares connected to the victim machine.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) can terminate running services.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) deletes itself following device encryption.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) executes as a service when deployed.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) injects into a newly-created `svchost.exe` process prior to device encryption.[^1]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) modifies the Windows firewall during execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackByte\|G1043]] | BlackByte |



## References

[^1]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


