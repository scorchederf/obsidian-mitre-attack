---
aliases: 
    - CopyKittens
mitre-attack: https://attack.mitre.org/groups/G0052
---

## G0052

[CopyKittens](https://attack.mitre.org/groups/G0052) is an Iranian cyber espionage group that has been operating since at least 2013. It has targeted countries including Israel, Saudi Arabia, Turkey, the U.S., Jordan, and Germany. The group is responsible for the campaign known as Operation Wilted Tulip.[^1] [^5] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [CopyKittens](https://attack.mitre.org/groups/G0052) encrypts data with a substitute cipher prior to exfiltration.[^4]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [CopyKittens](https://attack.mitre.org/groups/G0052) uses ZPP, a .NET console program, to compress files with ZIP.[^5]  |
| [[PowerShell\|T1059.001]] | PowerShell | [CopyKittens](https://attack.mitre.org/groups/G0052) has used PowerShell Empire.[^5]  |
| [[Proxy\|T1090]] | Proxy | [CopyKittens](https://attack.mitre.org/groups/G0052) has used the AirVPN service for operational activity.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [CopyKittens](https://attack.mitre.org/groups/G0052) uses rundll32 to load various tools on victims, including a lateral movement tool named Vminst, Cobalt Strike, and shellcode.[^5]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [CopyKittens](https://attack.mitre.org/groups/G0052) has used `-w hidden` and `-windowstyle hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows. [^5]  |
| [[Tool\|T1588.002]] | Tool | [CopyKittens](https://attack.mitre.org/groups/G0052) has used Metasploit, [Empire](https://attack.mitre.org/software/S0363), and AirVPN for post-exploitation activities.[^2] [^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [CopyKittens](https://attack.mitre.org/groups/G0052) digitally signed an executable with a stolen certificate from legitimate company AI Squared.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [^5]  |
| [[TDTESS\|S0164]] | TDTESS | [^5]  |
| [[Matryoshka\|S0167]] | Matryoshka | [^5]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^5]  |



## References

[^1]: [ClearSky CopyKittens March 2017](http://www.clearskysec.com/copykitten-jpost/)


[^2]: [ClearSky and Trend Micro Operation Wilted Tulip July 2017](https://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^3]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^4]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)


[^5]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^6]: CopyKittens


