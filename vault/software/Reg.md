---
aliases: 
    - S0075
    
mitre-attack: https://attack.mitre.org/software/S0075
---

## S0075

[Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. [^7] <br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [Reg](https://attack.mitre.org/software/S0075) may be used to find credentials in the Windows Registry.[^6]  |
| [[Query Registry\|T1012]] | Query Registry | [Reg](https://attack.mitre.org/software/S0075) may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.[^7]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Reg](https://attack.mitre.org/software/S0075) may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.[^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Rancor\|G0075]] | Rancor |
| [[OilRig\|G0049]] | OilRig |
| [[Daggerfly\|G1034]] | Daggerfly |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[Turla\|G0010]] | Turla |
| [[Gamaredon Group\|G0047]] | Gamaredon Group |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |



## References

[^1]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^2]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^3]: [unit42_gamaredon_dec2022](https://unit42.paloaltonetworks.com/trident-ursa/)


[^4]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^5]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^6]: [Pentestlab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)


[^7]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)


[^8]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^9]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^10]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^11]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^12]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


