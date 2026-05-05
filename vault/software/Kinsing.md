---
aliases: 
    - S0599
    
mitre-attack: https://attack.mitre.org/software/S0599
---

## S0599

[Kinsing](https://attack.mitre.org/software/S0599) is Golang-based malware that runs a cryptocurrency miner and attempts to spread itself to other hosts in the victim environment. [^3] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kinsing](https://attack.mitre.org/software/S0599) has used the find command to search for specific files.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Kinsing](https://attack.mitre.org/software/S0599) has communicated with C2 over HTTP.[^3]  |
| [[Deploy Container\|T1610]] | Deploy Container | [Kinsing](https://attack.mitre.org/software/S0599) was run through a deployed Ubuntu container.[^3]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Kinsing](https://attack.mitre.org/software/S0599) has used valid SSH credentials to access remote hosts.[^3]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Kinsing](https://attack.mitre.org/software/S0599) has used Unix shell scripts to execute commands in the victim environment.[^3]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Kinsing](https://attack.mitre.org/software/S0599) has searched for private keys.[^3]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [Kinsing](https://attack.mitre.org/software/S0599) has used chmod to modify permissions on key files for use.[^3]  |
| [[Shell History\|T1552.003]] | Shell History | [Kinsing](https://attack.mitre.org/software/S0599) has searched `bash_history` for credentials.[^3]  |
| [[Brute Force\|T1110]] | Brute Force | [Kinsing](https://attack.mitre.org/software/S0599) has attempted to brute force hosts over SSH.[^3]  |
| [[SSH\|T1021.004]] | SSH | [Kinsing](https://attack.mitre.org/software/S0599) has used SSH for lateral movement.[^3]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Kinsing](https://attack.mitre.org/software/S0599) has used a script to parse files like `/etc/hosts` and SSH `known_hosts` to discover remote systems.[^3]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Kinsing](https://attack.mitre.org/software/S0599) was executed in an Ubuntu container deployed via an open Docker daemon API.[^3]  |
| [[Cron\|T1053.003]] | Cron | [Kinsing](https://attack.mitre.org/software/S0599) has used crontab to download and run shell scripts every minute to ensure persistence.[^3]  |
| [[Container Administration Command\|T1609]] | Container Administration Command | [Kinsing](https://attack.mitre.org/software/S0599) was executed with an Ubuntu container entry point that runs shell scripts.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kinsing](https://attack.mitre.org/software/S0599) has downloaded additional lateral movement scripts from C2.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Kinsing](https://attack.mitre.org/software/S0599) has used ps to list processes.[^3]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Kinsing](https://attack.mitre.org/software/S0599) has created and run a Bitcoin cryptocurrency miner.[^3] [^1]  |




## References

[^1]: [Sysdig Kinsing November 2020](https://sysdig.com/blog/zoom-into-kinsing-kdevtmpfsi/)


[^2]: [Aqua Security Cloud Native Threat Report June 2021](https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation)


[^3]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)


