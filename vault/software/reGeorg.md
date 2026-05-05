---
aliases: 
    - S1187
    
mitre-attack: https://attack.mitre.org/software/S1187
---

## S1187

[reGeorg](https://attack.mitre.org/software/S1187) is an open-source web shell written in Python that can be used as a proxy to bypass firewall rules and tunnel data in and out of targeted networks.[^5] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [reGeorg](https://attack.mitre.org/software/S1187) is a Python-based web shell.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [reGeorg](https://attack.mitre.org/software/S1187) can tunnel TCP sessions including RDP, SSH, and SMB through HTTP.[^5] [^4] [^3]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [reGeorg](https://attack.mitre.org/software/S1187) can be used to tunnel RDP connections.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [reGeorg](https://attack.mitre.org/software/S1187) has the ability to download files to targeted systems.[^6]  |
| [[SSH\|T1021.004]] | SSH | [reGeorg](https://attack.mitre.org/software/S1187) can communicate using SSH through an HTTP tunnel.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [reGeorg](https://attack.mitre.org/software/S1187) can use HTTP to tunnel connections in and out of targeted networks.[^5]  |
| [[Proxy\|T1090]] | Proxy | [reGeorg](https://attack.mitre.org/software/S1187) can establish an HTTP or SOCKS proxy to tunnel data in and out of a network.[^1] [^5] [^4]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [reGeorg](https://attack.mitre.org/software/S1187) has the ability to tunnel SMB sessions.[^5]  |
| [[Web Shell\|T1505.003]] | Web Shell | [reGeorg](https://attack.mitre.org/software/S1187) is a web shell that has been installed on exposed web servers for access to victim environments.[^4] [^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [reGeorg](https://attack.mitre.org/software/S1187) can tunnel TCP sessions into targeted networks.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [GitHub reGeorg 2016](https://github.com/xl7dev/WebShell/tree/master/reGeorg-master)


[^2]: [Security Affairs ANSSI APT28 OCT 2023](https://securityaffairs.com/153131/apt/france-anssi-apt28.html)


[^3]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^4]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^5]: [Fortinet reGeorg MAR 2019](https://www.fortiguard.com/encyclopedia/ips/47584/regeorg-http-tunnel)


[^6]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)


