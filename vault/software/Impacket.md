---
aliases: 
    - S0357
    
mitre-attack: https://attack.mitre.org/software/S0357
---

## S0357

[Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.[^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Name Resolution Poisoning and SMB Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [Impacket](https://attack.mitre.org/software/S0357) modules like ntlmrelayx and smbrelayx can be used in conjunction with [Network Sniffing](https://attack.mitre.org/techniques/T1040) and [Name Resolution Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001) to gather NetNTLM credentials for [Brute Force](https://attack.mitre.org/techniques/T1110) or relay attacks that can gain code execution.[^5]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Impacket](https://attack.mitre.org/software/S0357) can be used to sniff network traffic via an interface or raw socket.[^5]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Impacket](https://attack.mitre.org/software/S0357) modules like GetUserSPNs can be used to get Service Principal Names (SPNs) for user accounts. The output is formatted to be compatible with cracking tools like John the Ripper and Hashcat.[^5]  |
| [[Ccache Files\|T1558.005]] | Ccache Files | [Impacket](https://attack.mitre.org/software/S0357) tools – such as `getST.py` or `ticketer.py` – can be used to steal or forge Kerberos tickets using ccache files given a password, hash, aesKey, or TGT.[^8] [^1]  |
| [[NTDS\|T1003.003]] | NTDS | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information from NTDS.dit.[^5]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Impacket](https://attack.mitre.org/software/S0357) contains various modules emulating other service execution tools such as [PsExec](https://attack.mitre.org/software/S0029).[^5]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.[^5]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Impacket](https://attack.mitre.org/software/S0357)'s `wmiexec` module can be used to execute commands through WMI.[^5] [^20]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.[^5]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Impacket](https://attack.mitre.org/software/S0357) has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.[^20]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | SecretsDump and [Mimikatz](https://attack.mitre.org/software/S0002) modules within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Storm-0501\|G1053]] | Storm-0501 |
| [[FIN13\|G1016]] | FIN13 |
| [[Magic Hound\|G0059]] | Magic Hound |
| [[APT41\|G0096]] | APT41 |
| [[HAFNIUM\|G0125]] | HAFNIUM |
| [[Lotus Blossom\|G0030]] | Lotus Blossom |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[Storm-1811\|G1046]] | Storm-1811 |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |
| [[APT29\|G0016]] | APT29 |
| [[menuPass\|G0045]] | menuPass |
| [[Sandworm Team\|G0034]] | Sandworm Team |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Velvet Ant\|G1047]] | Velvet Ant |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [on security kerberos linux](https://www.onsecurity.io/blog/abusing-kerberos-from-linux/)


[^2]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^3]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^4]: [apt41_dcsocytec_dec2022](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)


[^5]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)


[^6]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^7]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^8]: [Kerberos GNU/Linux](https://adepts.of0x.cc/kerberos-thievery-linux/)


[^9]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^10]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


[^11]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^12]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^13]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^14]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^15]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^16]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^17]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^18]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^19]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^20]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)


[^21]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^22]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^23]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^24]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^25]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^26]: [Core Security Impacket](https://www.coresecurity.com/core-labs/open-source-tools/impacket)


[^27]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


