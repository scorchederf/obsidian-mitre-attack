---
aliases: 
    - Salt Typhoon
mitre-attack: https://attack.mitre.org/groups/G1045
---

## G1045

[Salt Typhoon](https://attack.mitre.org/groups/G1045) is a People's Republic of China (PRC) state-backed actor that has been active since at least 2019 and responsible for numerous compromises of network infrastructure at major U.S. telecommunication and internet service providers (ISP).[^1] [^2] <br>

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has cleared logs including .bash_history, auth.log, lastlog, wtmp, and btmp.[^2]  |
| [[Network Topology\|T1590.004]] | Network Topology | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used configuration files from exploited network devices to help discover upstream and downstream network segments.[^2]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has modified device configurations to create and use Generic Routing Encapsulation (GRE) tunnels.[^2] <br> |
| [[Malware\|T1587.001]] | Malware | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used custom tooling including [JumbledPath](https://attack.mitre.org/software/S1206).[^2]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has exfiltrated configuration files from exploited network devices over FTP and TFTP.[^2]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has added SSH authorized_keys under root or other users at the Linux level on compromised network devices.[^2]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used a variety of tools and techniques to capture packet data between network interfaces.[^2]  |
| [[Network Device Configuration Dump\|T1602.002]] | Network Device Configuration Dump | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has attempted to acquire credentials by dumping network device configurations.[^2]  |
| [[Password Cracking\|T1110.002]] | Password Cracking | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has cracked passwords for accounts with weak encryption obtained from the configuration files of compromised network devices.[^2]  |
| [[SSH\|T1021.004]] | SSH | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has modified the loopback address on compromised switches and used them as the source of SSH connections to additional devices within the target environment, allowing them to bypass access control lists (ACLs).[^2]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has made changes to the Access Control List (ACL) and loopback interface address on compromised devices.[^2]  |
| [[Tool\|T1588.002]] | Tool | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used publicly available tooling to exploit vulnerabilities.[^2]  |
| [[Create Account\|T1136]] | Create Account | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has created Linux-level users on compromised network devices through modification of `/etc/shadow` and `/etc/passwd`.[^2]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has exploited CVE-2018-0171 in the Smart Install feature of Cisco IOS and Cisco IOS XE software for initial access.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[JumbledPath\|S1206]] | JumbledPath | [^2]  |



## References

[^1]: [US Dept. of Treasury Salt Typhoon JAN 2025](https://home.treasury.gov/news/press-releases/jy2792)


[^2]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)


