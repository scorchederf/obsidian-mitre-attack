---
aliases: 
    - S1071
    
mitre-attack: https://attack.mitre.org/software/S1071
---

## S1071

[Rubeus](https://attack.mitre.org/software/S1071) is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.[^3] [^5] [^4] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [Rubeus](https://attack.mitre.org/software/S1071) can use the `KerberosRequestorSecurityToken.GetRequest` method to request kerberoastable service tickets.[^3]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Rubeus](https://attack.mitre.org/software/S1071) can gather information about domain trusts.[^4] [^2]  |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | [Rubeus](https://attack.mitre.org/software/S1071) can create silver tickets.[^3]  |
| [[AS-REP Roasting\|T1558.004]] | AS-REP Roasting | [Rubeus](https://attack.mitre.org/software/S1071) can reveal the credentials of accounts that have Kerberos pre-authentication disabled through AS-REP roasting.[^3] [^4] [^2]   |
| [[Golden Ticket\|T1558.001]] | Golden Ticket | [Rubeus](https://attack.mitre.org/software/S1071) can forge a ticket-granting ticket.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |



## References

[^1]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^2]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)


[^3]: [GitHub Rubeus March 2023](https://github.com/GhostPack/Rubeus)


[^4]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^5]: [FireEye KEGTAP SINGLEMALT October 2020](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)


