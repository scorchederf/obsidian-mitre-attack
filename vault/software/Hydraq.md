---
aliases: 
    - S0203
    
mitre-attack: https://attack.mitre.org/software/S0203
---

## S0203

[Hydraq](https://attack.mitre.org/software/S0203) is a data-theft trojan first used by [Elderwood](https://attack.mitre.org/groups/G0066) in the 2009 Google intrusion known as Operation Aurora, though variations of this trojan have been used in more recent campaigns by other Chinese actors, possibly including [APT17](https://attack.mitre.org/groups/G0025).[^19] [^10] [^1] [^21] [^7] [^17] [^3] [^14] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Query Registry\|T1012]] | Query Registry | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can retrieve system information, such as CPU speed, from Registry keys.[^1] [^20]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can load and call DLL functions.[^1] [^20]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Hydraq](https://attack.mitre.org/software/S0203) uses svchost.exe to execute a malicious DLL included in a new service group.[^22]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can retrieve IP addresses of compromised machines.[^1] [^20]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can retrieve information such as computer name, OS version, processor speed, memory size, and CPU speed.[^20]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can read data from files.[^1] [^20]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Hydraq](https://attack.mitre.org/software/S0203) creates a Registry subkey to register its created service, and can also uninstall itself later by deleting this value. [Hydraq](https://attack.mitre.org/software/S0203)'s backdoor also enables remote attackers to modify and delete subkeys.[^1] [^20]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can download files and additional malware components.[^1] [^20]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Hydraq](https://attack.mitre.org/software/S0203) uses basic obfuscation in the form of spaghetti code.[^10] [^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Hydraq](https://attack.mitre.org/software/S0203) creates new services to establish persistence.[^1] [^20] [^22]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can clear all system event logs.[^1] [^20]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Hydraq](https://attack.mitre.org/software/S0203) C2 traffic is encrypted using bitwise NOT and XOR operations.[^20]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can monitor services.[^1] [^20]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can delete files.[^1] [^20]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can monitor processes.[^1] [^20]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Hydraq](https://attack.mitre.org/software/S0203) includes a component based on the code of VNC that can stream a live feed of the desktop of an infected host.[^20]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [Hydraq](https://attack.mitre.org/software/S0203) connects to a predefined domain on port 443 to exfil gathered information.[^20]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can check for the existence of files, including its own components, as well as retrieve a list of logical drives.[^1] [^20]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can adjust token privileges.[^20]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |
| [[Axiom\|G0001]] | Axiom |



## References

[^1]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^2]: Roarur


[^3]: [FireEye Sunshop Campaign May 2013](https://web.archive.org/web/20200302085651/https://www.fireeye.com/blog/threat-research/2013/05/ready-for-summer-the-sunshop-campaign.html)


[^4]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^5]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^6]: HydraQ


[^7]: [FireEye DeputyDog 9002 November 2013](https://web.archive.org/web/20190221032148/http://www.fireeye.com/blog/threat-research/2013/11/operation-ephemeral-hydra-ie-zero-day-linked-to-deputydog-uses-diskless-method.html)


[^8]: Homux


[^9]: HidraQ


[^10]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^11]: 9002 RAT


[^12]: Aurora


[^13]: MdmBot


[^14]: [PaloAlto 3102 Sept 2015](https://researchcenter.paloaltonetworks.com/2015/09/chinese-actors-use-3102-malware-in-attacks-on-us-government-and-eu-media/)


[^15]: Hydraq


[^16]: McRat


[^17]: [ProofPoint GoT 9002 Aug 2017](https://www.proofpoint.com/us/threat-insight/post/operation-rat-cook-chinese-apt-actors-use-fake-game-thrones-leaks-lures)


[^18]: HomeUnix


[^19]: [MicroFocus 9002 Aug 2016](https://community.softwaregrp.com/t5/Security-Research/9002-RAT-a-second-building-on-the-left/ba-p/228686#.WosBVKjwZPZ)


[^20]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^21]: [ASERT Seven Pointed Dagger Aug 2015](https://www.arbornetworks.com/blog/asert/wp-content/uploads/2016/01/ASERT-Threat-Intelligence-Brief-2015-08-Uncovering-the-Seven-Point-Dagger.pdf)


[^22]: [Symantec Hydraq Persistence Jan 2010](https://www.symantec.com/connect/blogs/how-trojanhydraq-stays-your-computer)


