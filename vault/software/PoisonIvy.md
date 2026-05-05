---
aliases: 
    - S0012
    
mitre-attack: https://attack.mitre.org/software/S0012
---

## S0012

[PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.[^24] [^26] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a Registry subkey that registers a new service. [PoisonIvy](https://attack.mitre.org/software/S0012) also creates a Registry entry modifying the Logical Disk Manager service to point to a malicious DLL dropped to disk.[^5]  |
| [[Modify Registry\|T1112]] | Modify Registry | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a Registry subkey that registers a new system device.[^5]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PoisonIvy](https://attack.mitre.org/software/S0012) creates run key Registry entries pointing to a malicious executable dropped to disk.[^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PoisonIvy](https://attack.mitre.org/software/S0012) hides any strings related to its own indicators of compromise.[^5]  |
| [[Keylogging\|T1056.001]] | Keylogging | [PoisonIvy](https://attack.mitre.org/software/S0012) contains a keylogger.[^24] [^5]  |
| [[Active Setup\|T1547.014]] | Active Setup | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a Registry key in the Active Setup pointing to a malicious executable.[^21] [^3] [^28]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a mutex using either a custom or default value.[^24]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [PoisonIvy](https://attack.mitre.org/software/S0012) can inject a malicious DLL into a process.[^24] [^5]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PoisonIvy](https://attack.mitre.org/software/S0012) stages collected data in a text file.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can open a command-line interface.[^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can upload files.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PoisonIvy](https://attack.mitre.org/software/S0012) uses the Camellia cipher to encrypt communications.[^24]  |
| [[Data from Local System\|T1005]] | Data from Local System | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can steal system information.[^5]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [PoisonIvy](https://attack.mitre.org/software/S0012) captures window titles.[^5]  |
| [[Rootkit\|T1014]] | Rootkit | [PoisonIvy](https://attack.mitre.org/software/S0012) starts a rootkit from a malicious file dropped to disk.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |
| [[APT5\|G1023]] | APT5 |
| [[GALLIUM\|G0093]] | GALLIUM |
| [[APT1\|G0006]] | APT1 |
| [[admin@338\|G0018]] | admin@338 |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |
| [[DragonOK\|G0017]] | DragonOK |
| [[PittyTiger\|G0011]] | PittyTiger |
| [[IndigoZebra\|G0136]] | IndigoZebra |
| [[Axiom\|G0001]] | Axiom |
| [[menuPass\|G0045]] | menuPass |
| [[Moafee\|G0002]] | Moafee |
| [[Mustang Panda\|G0129]] | Mustang Panda |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: [Haq 2014](https://www.fireeye.com/blog/threat-research/2014/09/the-path-to-mass-producing-cyber-attacks.html)


[^2]: [Symantec Darkmoon Sept 2014](https://www.symantec.com/connect/blogs/life-mars-how-attackers-took-advantage-hope-alien-existance-new-darkmoon-campaign)


[^3]: [paloalto Tropic Trooper 2016](https://unit42.paloaltonetworks.com/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)


[^4]: Poison Ivy


[^5]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^6]: [District Court of NY APT10 Indictment December 2018](https://www.justice.gov/opa/page/file/1122671/download)


[^7]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^8]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)


[^9]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^10]: Breut


[^11]: [Mandiant Advanced Persistent Threats](https://www.mandiant.com/resources/insights/apt-groups)


[^12]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^13]: Darkmoon


[^14]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^15]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^16]: PoisonIvy


[^17]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^18]: [Crowdstrike MUSTANG PANDA June 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)


[^19]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


[^20]: [Securelist APT Trends Q2 2017](https://securelist.com/apt-trends-report-q2-2017/79332/)


[^21]: [Microsoft PoisonIvy 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor%3aWin32%2fPoisonivy.E)


[^22]: [DustySky2](http://www.clearskysec.com/wp-content/uploads/2016/06/Operation-DustySky2_-6.2016_TLP_White.pdf)


[^23]: [Unit 42 Tropic Trooper Nov 2016](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)


[^24]: [FireEye Poison Ivy](https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf)


[^25]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^26]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^27]: [FireEye Operation Molerats](https://web.archive.org/web/20201031075438/https://www.fireeye.com/blog/threat-research/2013/08/operation-molerats-middle-east-cyber-attacks-using-poison-ivy.html)


[^28]: [FireEye Regsvr32 Targeting Mongolian Gov](https://www.fireeye.com/blog/threat-research/2017/02/spear_phishing_techn.html)


[^29]: [Villeneuve 2014](https://www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html)


[^30]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^31]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


