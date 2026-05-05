---
aliases: 
    - S0600
    
mitre-attack: https://attack.mitre.org/software/S0600
---

## S0600

[Doki](https://attack.mitre.org/software/S0600) is a backdoor that uses a unique Dogecoin-based Domain Generation Algorithm and was first observed in July 2020. [Doki](https://attack.mitre.org/software/S0600) was used in conjunction with the [ngrok](https://attack.mitre.org/software/S0508) Mining Botnet in a campaign that targeted Docker servers in cloud platforms. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Doki](https://attack.mitre.org/software/S0600) has used the DynDNS service and a DGA based on the Dogecoin blockchain to generate C2 domains.[^1]  |
| [[Escape to Host\|T1611]] | Escape to Host | [Doki](https://attack.mitre.org/software/S0600)’s container was configured to bind the host root directory.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Doki](https://attack.mitre.org/software/S0600) has used a script that gathers information from a hardcoded list of IP addresses and uploads to an Ngrok URL.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Doki](https://attack.mitre.org/software/S0600) has used the embedTLS library for network communications.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Doki](https://attack.mitre.org/software/S0600) has used Ngrok to establish C2 and exfiltrate data.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Doki](https://attack.mitre.org/software/S0600) has downloaded scripts from C2.[^1]  |
| [[Deploy Container\|T1610]] | Deploy Container | [Doki](https://attack.mitre.org/software/S0600) was run through a deployed container.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Doki](https://attack.mitre.org/software/S0600) has executed shell scripts with /bin/sh.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Doki](https://attack.mitre.org/software/S0600) has resolved the path of a process PID to use as a script argument.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Doki](https://attack.mitre.org/software/S0600) has communicated with C2 over HTTPS.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Doki](https://attack.mitre.org/software/S0600) has used the dogechain.info API to generate a C2 address.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Doki](https://attack.mitre.org/software/S0600) has disguised a file as a Linux kernel module.[^1]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Doki](https://attack.mitre.org/software/S0600) was executed through an open Docker daemon API port.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Doki](https://attack.mitre.org/software/S0600) has searched for the current process’s PID.[^1]  |




## References

[^1]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


