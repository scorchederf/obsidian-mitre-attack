---
aliases: 
    - S0374
    
mitre-attack: https://attack.mitre.org/software/S0374
---

## S0374

[SpeakUp](https://attack.mitre.org/software/S0374) is a Trojan backdoor that targets both Linux and OSX devices. It was first observed in January 2019. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `cat /proc/cpuinfo | grep -c “cpu family” 2>&1` command to gather system information. [^1]  |
| [[Cron\|T1053.003]] | Cron | [SpeakUp](https://attack.mitre.org/software/S0374) uses cron tasks to ensure persistence. [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SpeakUp](https://attack.mitre.org/software/S0374) downloads and executes additional files from a remote server. [^1]  |
| [[Python\|T1059.006]] | Python | [SpeakUp](https://attack.mitre.org/software/S0374) uses Python scripts.[^1]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [SpeakUp](https://attack.mitre.org/software/S0374) can perform brute forcing using a pre-defined list of usernames and passwords in an attempt to log in to administrative panels. [^1]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `whoami` command. [^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [SpeakUp](https://attack.mitre.org/software/S0374) checks for availability of specific ports on servers.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [SpeakUp](https://attack.mitre.org/software/S0374) uses POST and GET requests over HTTP to communicate with its main C&C server. [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `ifconfig -a` command. [^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [SpeakUp](https://attack.mitre.org/software/S0374) attempts to exploit the following vulnerabilities in order to execute its malicious script: CVE-2012-0874, CVE-2010-1871, CVE-2017-10271, CVE-2018-2894, CVE-2016-3088, JBoss AS 3/4/5/6, and the Hadoop YARN ResourceManager. [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SpeakUp](https://attack.mitre.org/software/S0374) deletes files to remove evidence on the machine. [^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [SpeakUp](https://attack.mitre.org/software/S0374) uses Perl scripts.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SpeakUp](https://attack.mitre.org/software/S0374) encodes C&C communication using Base64. [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SpeakUp](https://attack.mitre.org/software/S0374) encodes its second-stage payload with Base64. [^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `arp -a` command. [^1]  |




## References

[^1]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


