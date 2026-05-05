---
aliases: 
    - S0468
    
mitre-attack: https://attack.mitre.org/software/S0468
---

## S0468

[Skidmap](https://attack.mitre.org/software/S0468) is a kernel-mode rootkit used for cryptocurrency mining.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Skidmap](https://attack.mitre.org/software/S0468) is a kernel-mode rootkit used for cryptocurrency mining.[^1]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to add the public key of its handlers to the `authorized_keys` file to maintain persistence on an infected host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to download files on an infected host.[^1]   |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Skidmap](https://attack.mitre.org/software/S0468) has encrypted it's main payload using 3DES.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Skidmap](https://attack.mitre.org/software/S0468) has created a fake `rm` binary to replace the legitimate Linux binary.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to set SELinux to permissive mode.[^1]  |
| [[Cron\|T1053.003]] | Cron | [Skidmap](https://attack.mitre.org/software/S0468) has installed itself via crontab.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Skidmap](https://attack.mitre.org/software/S0468) has checked for the existence of specific files including `/usr/sbin/setenforce` and ` /etc/selinux/config`. It also has the ability to monitor the cryptocurrency miner file and process. [^1]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to check if `/usr/sbin/setenforce` exists. This file controls what mode SELinux is in.[^1]   |
| [[Kernel Modules and Extensions\|T1547.006]] | Kernel Modules and Extensions | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to install several loadable kernel modules (LKMs) on infected machines.[^1]  |
| [[Pluggable Authentication Modules\|T1556.003]] | Pluggable Authentication Modules | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to replace the pam_unix.so file on an infected machine with its own malicious version that accepts a specific backdoor password for all users.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to check whether the infected system’s OS is Debian or RHEL/CentOS to determine which cryptocurrency miner it should use.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Skidmap](https://attack.mitre.org/software/S0468) is a kernel-mode rootkit that has the ability to hook system calls to hide specific files and fake network and CPU-related statistics to make the CPU load of the infected machine always appear low.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Skidmap](https://attack.mitre.org/software/S0468) has monitored critical processes to ensure resiliency.[^1]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to download, unpack, and decrypt tar.gz files .[^1]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Skidmap](https://attack.mitre.org/software/S0468) has used `pm.sh` to download and install its main payload.[^1]  |




## References

[^1]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


