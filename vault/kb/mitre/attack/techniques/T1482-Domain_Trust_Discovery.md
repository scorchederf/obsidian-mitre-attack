---
aliases: 
    - T1482
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1482-Domain_Trust_Discovery
tactic: 
     - Discovery
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.[^19]  Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [[kb/mitre/attack/techniques/T1134.005-SID-History_Injection\|SID-History Injection]], [[kb/mitre/attack/techniques/T1550.003-Pass_the_Ticket\|Pass the Ticket]], and [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|Kerberoasting]].[^9] [^11]  Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.[^11]  The Windows utility [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] is known to be used by adversaries to enumerate domain trusts.[^18] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0105-dsquery\|S0105]] | dsquery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] can be used to gather information on domain trusts with `dsquery * -filter "(objectClass=trustedDomain)" -attr *`.[^11]  |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] has modules such as `Get-NetDomainTrust` and `Get-NetForestTrust` to enumerate domain and forest trusts.[^7] [^15]  |
| [[kb/mitre/attack/software/S0359-Nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-Nltest\|Nltest]] may be used to enumerate trusted domains by using commands such as `nltest /domain_trusts`.[^13] [^10]  |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] has modules for enumerating domain trusts.[^17]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] has modules for enumerating domain trusts.[^12]  |
| [[kb/mitre/attack/software/S0521-BloodHound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-BloodHound\|BloodHound]] has the ability to map domain trusts and identify misconfigurations for potential abuse.[^16]  |
| [[kb/mitre/attack/software/S0552-AdFind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-AdFind\|AdFind]] can gather information about organizational units (OUs) and domain trusts from Active Directory.[^5] [^2] [^3] [^20]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.[^8] [^1]  |
| [[kb/mitre/attack/software/S1071-Rubeus\|S1071]] | Rubeus | [[kb/mitre/attack/software/S1071-Rubeus\|Rubeus]] can gather information about domain trusts.[^14] [^6]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Employ network segmentation for sensitive domains.[^11] . |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Map the trusts within existing domains/forests and keep trust relationships to a minimum. |






> [!info]- References
> [^1]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)

> [^2]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)

> [^3]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)

> [^4]: [Microsoft GetAllTrustRelationships](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.domain.getalltrustrelationships?redirectedfrom=MSDN&view=netframework-4.7.2#System_DirectoryServices_ActiveDirectory_Domain_GetAllTrustRelationships)

> [^5]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)

> [^6]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)

> [^7]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)

> [^8]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^9]: [AdSecurity Forging Trust Tickets](https://adsecurity.org/?p=1588)

> [^10]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)

> [^11]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)

> [^12]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)

> [^13]: [Nltest Manual](https://ss64.com/nt/nltest.html)

> [^14]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)

> [^15]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^16]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)

> [^17]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^18]: [Microsoft Operation Wilysupply](https://www.microsoft.com/security/blog/2017/05/04/windows-defender-atp-thwarts-operation-wilysupply-software-supply-chain-cyberattack/)

> [^19]: [Microsoft Trusts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10))

> [^20]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


