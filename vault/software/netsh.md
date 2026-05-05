---
aliases: 
    - S0108
    
mitre-attack: https://attack.mitre.org/software/S0108
---

## S0108

[netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [netsh](https://attack.mitre.org/software/S0108) can be used to disable local firewall settings.[^9] [^12]  |
| [[Netsh Helper DLL\|T1546.007]] | Netsh Helper DLL | [netsh](https://attack.mitre.org/software/S0108) can be used as a persistence proxy technique to execute a helper DLL when netsh.exe is executed.[^3]  |
| [[Proxy\|T1090]] | Proxy | [netsh](https://attack.mitre.org/software/S0108) can be used to set up a proxy tunnel to allow remote host access to an infected host.[^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [netsh](https://attack.mitre.org/software/S0108) can be used to discover system firewall settings.[^9] [^12]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[Naikon\|G0019]] | Naikon |
| [[APT32\|G0050]] | APT32 |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[Lazarus Group\|G0032]] | Lazarus Group |
| [[Carbanak\|G0008]] | Carbanak |
| [[Dragonfly\|G0035]] | Dragonfly |



## References

[^1]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^2]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^3]: [Demaske Netsh Persistence](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)


[^4]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^5]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^6]: [Securelist fileless attacks Feb 2017](https://securelist.com/fileless-attacks-against-enterprise-networks/77403/)


[^7]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^8]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^9]: [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)


[^10]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^11]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^12]: [TechNet Netsh Firewall](https://technet.microsoft.com/en-us/library/cc771046(v=ws.10).aspx)


[^13]: [Group-IB Anunak](http://www.group-ib.com/files/Anunak_APT_against_financial_institutions.pdf)


