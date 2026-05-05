---
aliases: 
    - S0349
    
mitre-attack: https://attack.mitre.org/software/S0349
---

## S0349

[LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.[^14] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from chats, databases, mail, and WiFi.[^14]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from Vault files.[^14] 	 |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from LSA secrets to obtain account and password information.[^14]  |
| [[／etc／passwd and ／etc／shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credential information from /etc/shadow using the shadow.py module.[^14]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from web browsers such as Google Chrome, Internet Explorer, and Firefox.[^14]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from memory to obtain account and password information.[^14]  |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from MSCache to obtain account and password information.[^14]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from databases, mail, and WiFi across multiple platforms.[^14]  |
| [[Keychain\|T1555.001]] | Keychain | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from macOS Keychains.[^14] 	 |
| [[Proc Filesystem\|T1003.007]] | Proc Filesystem | [LaZagne](https://attack.mitre.org/software/S0349) can use the `<PID>/maps` and `<PID>/mem` files to identify regex patterns to dump cleartext passwords from the browser's process memory.[^14] [^13]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Leafminer\|G0077]] | Leafminer |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[APT3\|G0022]] | APT3 |
| [[Scattered Spider\|G1015]] | Scattered Spider |
| [[OilRig\|G0049]] | OilRig |
| [[MuddyWater\|G0069]] | MuddyWater |
| [[Inception\|G0100]] | Inception |
| [[APT33\|G0064]] | APT33 |
| [[TeamTNT\|G0139]] | TeamTNT |
| [[Tonto Team\|G0131]] | Tonto Team |
| [[Evilnum\|G0120]] | Evilnum |
| [[Akira\|G1024]] | Akira |



## References

[^1]: [ATT TeamTNT Chimaera September 2020](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)


[^2]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^3]: [MSTIC Octo Tempest Operations October 2023](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)


[^4]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^5]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^6]: [GitHub LaZange Dec 2018](https://github.com/AlessandroZ/LaZagne)


[^7]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^8]: LaZagne


[^9]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^10]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^11]: [Arctic Wolf Akira 2023](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)


[^12]: [FireEye APT35 2018](https://static.carahsoft.com/concrete/files/1015/2779/3571/M-Trends-2018-Report.pdf)


[^13]: [Picus Labs Proc cump 2022](https://www.picussecurity.com/resource/the-mitre-attck-t1003-os-credential-dumping-technique-and-its-adversary-use)


[^14]: [GitHub LaZagne Dec 2018](https://github.com/AlessandroZ/LaZagne)


[^15]: [TrendMicro Tonto Team October 2020](https://vb2020.vblocalhost.com/uploads/VB2020-06.pdf)


[^16]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


[^17]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


