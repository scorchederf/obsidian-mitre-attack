---
aliases: 
    - Deep Panda
    - Shell Crew
    - WebMasters
    - KungFu Kittens
    - PinkPanther
    - Black Vine
mitre-attack: https://attack.mitre.org/groups/G0009
---

## G0009

[Deep Panda](https://attack.mitre.org/groups/G0009) is a suspected Chinese threat group known to target many industries, including government, defense, financial, and telecommunications. [^6]  The intrusion into healthcare company Anthem has been attributed to [Deep Panda](https://attack.mitre.org/groups/G0009). [^9]  This group is also known as Shell Crew, WebMasters, KungFu Kittens, and PinkPanther. [^7]  [Deep Panda](https://attack.mitre.org/groups/G0009) also appears to be known as Black Vine based on the attribution of both group names to the Anthem intrusion. [^4]  Some analysts track [Deep Panda](https://attack.mitre.org/groups/G0009) and [APT19](https://attack.mitre.org/groups/G0073) as the same group, but it is unclear from open source information if the groups are the same. [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Deep Panda](https://attack.mitre.org/groups/G0009) uses the Microsoft [Tasklist](https://attack.mitre.org/software/S0057) utility to list processes running on systems.[^6]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Deep Panda](https://attack.mitre.org/groups/G0009) has used ping to identify other machines of interest.[^6]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Deep Panda](https://attack.mitre.org/groups/G0009) uses Web shells on publicly accessible Web servers to access victim networks.[^10]  |
| [[Indicator Removal from Tools\|T1027.005]] | Indicator Removal from Tools | [Deep Panda](https://attack.mitre.org/groups/G0009) has updated and modified its malware, resulting in different hash values that evade detection.[^4]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Deep Panda](https://attack.mitre.org/groups/G0009) has used regsvr32.exe to execute a server variant of [Derusbi](https://attack.mitre.org/software/S0021) in victim networks.[^7]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Deep Panda](https://attack.mitre.org/groups/G0009) has used `-w hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows by setting the WindowStyle parameter to hidden. [^6]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Deep Panda](https://attack.mitre.org/groups/G0009) has used PowerShell scripts to download and execute programs in memory, without writing to disk.[^6]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | [Deep Panda](https://attack.mitre.org/groups/G0009) has used the sticky-keys technique to bypass the RDP login screen on remote systems during intrusions.[^7]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | The [Deep Panda](https://attack.mitre.org/groups/G0009) group is known to utilize WMI for lateral movement.[^6]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Deep Panda](https://attack.mitre.org/groups/G0009) uses net.exe to connect to network shares using `net use` commands with compromised credentials.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [^6]  |
| [[Tasklist\|S0057]] | Tasklist | [^6]  |
| [[Ping\|S0097]] | Ping | [^6]  |
| [[StreamEx\|S0142]] | StreamEx | [^5]  |
| [[Derusbi\|S0021]] | Derusbi | [^9]  |
| [[Sakula\|S0074]] | Sakula | [^9]  |
| [[Mivast\|S0080]] | Mivast | [^4]  |



## References

[^1]: Black Vine


[^2]: Deep Panda


[^3]: [ICIT China's Espionage Jul 2016](https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/)


[^4]: [Symantec Black Vine](https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf)


[^5]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^6]: [Alperovitch 2014](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)


[^7]: [RSA Shell Crew](https://www.rsa.com/content/dam/en/white-paper/rsa-incident-response-emerging-threat-profile-shell-crew.pdf)


[^8]: PinkPanther


[^9]: [ThreatConnect Anthem](https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/)


[^10]: [CrowdStrike Deep Panda Web Shells](http://www.crowdstrike.com/blog/mo-shells-mo-problems-deep-panda-web-shells/)


[^11]: KungFu Kittens


[^12]: WebMasters


[^13]: Shell Crew


