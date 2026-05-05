---
aliases: 
    - S0191
    
mitre-attack: https://attack.mitre.org/software/S0191
---

## S0191

[Winexe](https://attack.mitre.org/software/S0191) is a lightweight, open source tool similar to [PsExec](https://attack.mitre.org/software/S0029) designed to allow system administrators to execute commands on remote servers. [^2]  [Winexe](https://attack.mitre.org/software/S0191) is unique in that it is a GNU/Linux based client. [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Service Execution\|T1569.002]] | Service Execution | [Winexe](https://attack.mitre.org/software/S0191) installs a service on the remote system, executes the command, then uninstalls the service.[^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[DarkVishnya\|G0105]] | DarkVishnya |
| [[Silence\|G0091]] | Silence |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Securelist DarkVishnya Dec 2018](https://securelist.com/darkvishnya/89169/)


[^2]: [Winexe Github Sept 2013](https://github.com/skalkoto/winexe/)


[^3]: [SecureList Silence Nov 2017](https://securelist.com/the-silence/83009/)


[^4]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)


[^5]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


[^6]: [Secpod Winexe June 2017](https://web.archive.org/web/20211019012628/https://www.secpod.com/blog/winexe/)


