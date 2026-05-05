---
aliases: 
    - Sea Turtle
    - Teal Kurma
    - Marbled Dust
    - Cosmic Wolf
    - SILICON
mitre-attack: https://attack.mitre.org/groups/G1041
---

## G1041

[Sea Turtle](https://attack.mitre.org/groups/G1041) is a Türkiye-linked threat actor active since at least 2017 performing espionage and service provider compromise operations against victims in Asia, Europe, and North America. [Sea Turtle](https://attack.mitre.org/groups/G1041) is notable for targeting registrars managing ccTLDs and complex DNS-based intrusions where the threat actor compromised DNS providers to hijack DNS resolution for ultimate victims, enabling [Sea Turtle](https://attack.mitre.org/groups/G1041) to spoof log in portals and other applications for credential collection.[^2] [^6] [^4] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Sea Turtle](https://attack.mitre.org/groups/G1041) accessed victim networks from VPN service provider networks.[^5]  |
| [[Remote Data Staging\|T1074.002]] | Remote Data Staging | [Sea Turtle](https://attack.mitre.org/groups/G1041) staged collected email archives in the public web directory of a website that was accessible from the internet.[^5]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Sea Turtle](https://attack.mitre.org/groups/G1041) collected email archives from victim environments.[^5]  |
| [[DNS Server\|T1583.002]] | DNS Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) built adversary-in-the-middle DNS servers to impersonate legitimate services that were later used to capture credentials.[^6] [^2]  |
| [[Install Digital Certificate\|T1608.003]] | Install Digital Certificate | [Sea Turtle](https://attack.mitre.org/groups/G1041) captured legitimate SSL certificates from victim organizations and installed these on [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled infrastructure to enable subsequent adversary-in-the-middle operations.[^2]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [Sea Turtle](https://attack.mitre.org/groups/G1041) unset the Bash and MySQL history files on victim systems.[^5]  |
| [[DNS Server\|T1584.002]] | DNS Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) modified Name Server (NS) items to refer to [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled DNS servers to provide responses for all DNS lookups.[^2] [^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Sea Turtle](https://attack.mitre.org/groups/G1041) created adversary-in-the-middle servers to impersonate legitimate services and enable credential capture.[^2]  |
| [[Digital Certificates\|T1588.004]] | Digital Certificates | [Sea Turtle](https://attack.mitre.org/groups/G1041) created new certificates using a technique called the actors performed "certificate impersonation," a technique in which [Sea Turtle](https://attack.mitre.org/groups/G1041) obtained a certificate authority-signed X.509 certificate from another provider for the same domain imitating the one already used by the targeted organization.[^2] [^6]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Sea Turtle](https://attack.mitre.org/groups/G1041) used the tar utility to create a local archive of email data on a victim system.[^5]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [Sea Turtle](https://attack.mitre.org/groups/G1041) executed [SnappyTCP](https://attack.mitre.org/software/S1163) using the tool NoHup, which keeps the malware running on a system after exiting the shell or terminal.[^5]  |
| [[Tool\|T1588.002]] | Tool | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used tools such as Adminer during intrusions.[^5]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Sea Turtle](https://attack.mitre.org/groups/G1041) gained access to victim environments by exploiting multiple known vulnerabilities over several campaigns.[^2] [^4]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Sea Turtle](https://attack.mitre.org/groups/G1041) compromised cPanel accounts in victim environments.[^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used exploits for vulnerabilities such as CVE-2021-44228, CVE-2021-21974, and CVE-2022-0847 to achieve client code execution.[^4]  |
| [[Phishing\|T1566]] | Phishing | [Sea Turtle](https://attack.mitre.org/groups/G1041) used spear phishing to gain initial access to victims.[^2]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Sea Turtle](https://attack.mitre.org/groups/G1041) has used external-facing SSH to achieve initial access to the IT environments of victim organizations.[^5]  |
| [[Databases\|T1213.006]] | Databases | [Sea Turtle](https://attack.mitre.org/groups/G1041) used the tool Adminer to remotely logon to the MySQL service of victim machines.[^5]  |
| [[Domains\|T1583.001]] | Domains | [Sea Turtle](https://attack.mitre.org/groups/G1041) registered domains for authoritative name servers used in DNS hijacking activity and for command and control servers.[^6] [^5]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [Sea Turtle](https://attack.mitre.org/groups/G1041) downloaded source code files from remote addresses then compiled them locally via GCC in victim environments.[^5]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [Sea Turtle](https://attack.mitre.org/groups/G1041) has overwritten Linux system logs and unsets the Bash history file (effectively removing logging) during intrusions.[^5]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Sea Turtle](https://attack.mitre.org/groups/G1041) used shell scripts for post-exploitation execution in victim environments.[^4] [^5]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Sea Turtle](https://attack.mitre.org/groups/G1041) deployed the [SnappyTCP](https://attack.mitre.org/software/S1163) web shell during intrusion operations.[^4] [^5]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Sea Turtle](https://attack.mitre.org/groups/G1041) used compromised credentials to maintain long-term access to victim environments.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Sea Turtle](https://attack.mitre.org/groups/G1041) connected over TCP using HTTP to establish command and control channels.[^5]  |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | [Sea Turtle](https://attack.mitre.org/groups/G1041) targeted third-party entities in trusted relationships with primary targets to ultimately achieve access at primary targets. Entities targeted included DNS registrars, telecommunication companies, and internet service providers.[^2]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [Sea Turtle](https://attack.mitre.org/groups/G1041) modified DNS records at service providers to redirect traffic from legitimate resources to [Sea Turtle](https://attack.mitre.org/groups/G1041)-controlled servers to enable adversary-in-the-middle attacks for credential capture.[^2] [^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[SnappyTCP\|S1163]] | SnappyTCP | [Sea Turtle](https://attack.mitre.org/groups/G1041) used [SnappyTCP](https://attack.mitre.org/software/S1163) following initial access in intrusions from 2021 to 2023.[^4]  |



## References

[^1]: Cosmic Wolf


[^2]: [Talos Sea Turtle 2019](https://blog.talosintelligence.com/seaturtle/)


[^3]: Teal Kurma


[^4]: [PWC Sea Turtle 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/tortoise-and-malwahare.html)


[^5]: [Hunt Sea Turtle 2024](https://www.huntandhackett.com/blog/turkish-espionage-campaigns)


[^6]: [Talos Sea Turtle 2019_2](https://blog.talosintelligence.com/sea-turtle-keeps-on-swimming/)


[^7]: Marbled Dust


[^8]: SILICON


[^9]: [Microsoft Digital Defense 2021](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RWMFIi?id=101738)


