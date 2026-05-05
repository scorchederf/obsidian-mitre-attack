---
aliases: 
    - S0488
    
mitre-attack: https://attack.mitre.org/software/S0488
---

## S0488

[CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump usernames and hashed passwords from the SAM.[^2]  |
| [[NTDS\|T1003.003]] | NTDS | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords associated with Active Directory using Windows' Directory Replication Services API (DRSUAPI), or Volume Shadow Copy.[^2]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force credential authentication by using a supplied list of usernames and a single password.[^2]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover the password policies applied to the target system.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the domain user accounts on a targeted system.[^2]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active sessions for a targeted system.[^2]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force passwords for a specified user on a single target system or across an entire network.[^2]  |
| [[At\|T1053.002]] | At | [CrackMapExec](https://attack.mitre.org/software/S0488) can set a scheduled task on the target system to execute commands remotely using [at](https://attack.mitre.org/software/S0110).[^2]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the shared folders and associated permissions for a targeted network.[^2]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover active IP addresses, along with the machine name, within a targeted network.[^2]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [CrackMapExec](https://attack.mitre.org/software/S0488) can dump hashed passwords from LSA secrets for the targeted system.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [CrackMapExec](https://attack.mitre.org/software/S0488) can execute remote commands using Windows Management Instrumentation.[^2] 	 |
| [[Modify Registry\|T1112]] | Modify Registry | [CrackMapExec](https://attack.mitre.org/software/S0488) can create a registry key using wdigest.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover specified filetypes and log files on a targeted system.[^2]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [CrackMapExec](https://attack.mitre.org/software/S0488) can pass the hash to authenticate via SMB.[^2]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the system drives and associated system name.[^2]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [CrackMapExec](https://attack.mitre.org/software/S0488) can gather the user accounts within domain groups.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CrackMapExec](https://attack.mitre.org/software/S0488) can execute PowerShell commands via WMI.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [CrackMapExec](https://attack.mitre.org/software/S0488) can collect DNS information from the targeted system.[^2]  |
| [[Brute Force\|T1110]] | Brute Force | [CrackMapExec](https://attack.mitre.org/software/S0488) can brute force supplied user credentials across a network range.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT39\|G0087]] | APT39 |
| [[FIN7\|G0046]] | FIN7 |
| [[Ember Bear\|G1003]] | Ember Bear |
| [[Dragonfly\|G0035]] | Dragonfly |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [Secureworks IRON LIBERTY July 2019](https://www.secureworks.com/research/resurgent-iron-liberty-targeting-energy-sector)


[^2]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


[^3]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^4]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^5]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^6]: [BitDefender Chafer May 2020](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)


[^7]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^8]: [FireEye APT39 Jan 2019](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)


[^9]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


