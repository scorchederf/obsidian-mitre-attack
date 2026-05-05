---
aliases: 
    - Akira
    - GOLD SAHARA
    - PUNK SPIDER
    - Howling Scorpius
mitre-attack: https://attack.mitre.org/groups/G1024
---

## G1024

[Akira](https://attack.mitre.org/groups/G1024) is a ransomware variant and ransomware deployment entity active since at least March 2023.[^5]  [Akira](https://attack.mitre.org/groups/G1024) uses compromised credentials to access single-factor external access mechanisms such as VPNs for initial access, then various publicly-available tools and techniques for lateral movement.[^5] [^2]  [Akira](https://attack.mitre.org/groups/G1024) operations are associated with "double extortion" ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Technical analysis of [Akira](https://attack.mitre.org/software/S1129) ransomware indicates variants capable of targeting Windows or VMWare ESXi hypervisors and multiple overlaps with [Conti](https://attack.mitre.org/software/S0575) ransomware.[^8] [^11] [^10] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Akira](https://attack.mitre.org/groups/G1024) will exfiltrate victim data using applications such as [Rclone](https://attack.mitre.org/software/S1040).[^2]  |
| [[Sharepoint\|T1213.002]] | Sharepoint | [Akira](https://attack.mitre.org/groups/G1024) has accessed and downloaded information stored in SharePoint instances as part of data gathering and exfiltration activity.[^2]  |
| [[Account Access Removal\|T1531]] | Account Access Removal | [Akira](https://attack.mitre.org/groups/G1024) deletes administrator accounts in victim networks prior to encryption.[^2]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Akira](https://attack.mitre.org/groups/G1024) uses the built-in [Nltest](https://attack.mitre.org/software/S0359) utility or tools such as [AdFind](https://attack.mitre.org/software/S0552) to enumerate Active Directory trusts in victim environments.[^5]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Akira](https://attack.mitre.org/groups/G1024) has used legitimate names and locations for files to evade defenses.[^10]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Akira](https://attack.mitre.org/groups/G1024) uses valid account information to remotely access victim networks, such as VPN credentials.[^2] [^5] [^10] <br> |
| [[Steal or Forge Kerberos Tickets\|T1558]] | Steal or Forge Kerberos Tickets | [Akira](https://attack.mitre.org/groups/G1024) have used scripts to dump Kerberos authentication credentials.[^10]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Akira](https://attack.mitre.org/groups/G1024) uses software such as Advanced IP Scanner and MASSCAN to identify remote hosts within victim networks.[^5]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Akira](https://attack.mitre.org/groups/G1024) has used RDP for lateral movement.[^10]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Akira](https://attack.mitre.org/groups/G1024) has used PowerShell scripts for credential harvesting and privilege escalation.[^10] <br> |
| [[Financial Theft\|T1657]] | Financial Theft | [Akira](https://attack.mitre.org/groups/G1024) engages in double-extortion ransomware, exfiltrating files then encrypting them, in order to prompt victims to pay a ransom.[^8] [^11]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Akira](https://attack.mitre.org/groups/G1024) encrypts files in victim environments as part of ransomware operations.[^8] [^11]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Akira](https://attack.mitre.org/groups/G1024) uses compromised VPN accounts for initial access to victim networks.[^2]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Akira](https://attack.mitre.org/groups/G1024) has used binary padding to obfuscate payloads.[^10]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Akira](https://attack.mitre.org/groups/G1024) has disabled or modified security tools for defense evasion.[^10]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Akira](https://attack.mitre.org/groups/G1024) uses legitimate utilities such as AnyDesk and PuTTy for maintaining remote access to victim environments.[^2] [^5]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Akira](https://attack.mitre.org/groups/G1024) uses utilities such as WinRAR to archive data prior to exfiltration.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Rclone\|S1040]] | Rclone | [^5]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^5]  |
| [[LaZagne\|S0349]] | LaZagne | [^5]  |
| [[AdFind\|S0552]] | AdFind | [^5]  |
| [[PsExec\|S0029]] | PsExec | [^5]   |
| [[Megazord\|S1191]] | Megazord | [^11] [^10] [^4]  |
| [[Akira\|S1129]] | Akira | [^9] [^10]  |
| [[Akira _v2\|S1194]] | Akira _v2 | [^11] [^10] <br>[^4]  |



## References

[^1]: Howling Scorpius


[^2]: [Secureworks GOLD SAHARA](https://www.secureworks.com/research/threat-profiles/gold-sahara)


[^3]: GOLD SAHARA


[^4]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^5]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^6]: [CrowdStrike PUNK SPIDER](https://www.crowdstrike.com/adversaries/punk-spider/)


[^7]: PUNK SPIDER


[^8]: [BushidoToken Akira 2023](https://blog.bushidotoken.net/2023/09/tracking-adversaries-akira-another.html)


[^9]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^10]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^11]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


