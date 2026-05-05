---
aliases: 
    - S1201
    
mitre-attack: https://attack.mitre.org/software/S1201
---

## S1201

[TRANSLATEXT](https://attack.mitre.org/software/S1201) is malware that is believed to be used by [Kimsuky](https://attack.mitre.org/groups/G0094).[^1]  [TRANSLATEXT](https://attack.mitre.org/software/S1201) masqueraded as a Google Translate extension for Google Chrome, but is actually a collection of four malicious Javascript files that perform defense evasion, information collection and exfiltration.[^1]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has used HTTP to communicate with the C2 server.[^1]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has stolen credentials stored in Chrome.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has used PowerShell to collect system information and to upload the collected data to a Github repository.[^1]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has exfiltrated collected credentials to the C2 server.[^1]   |
| [[Modify Registry\|T1112]] | Modify Registry | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has modified the following registry key to install itself as the value, granting permission to install specified extensions: ` HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist`.[^1]   |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has the ability to use form-grabbing and event-listening to extract data from web data forms.[^1]   |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has used a dead drop resolver to retrieve configurations and commands from a public blog site.[^1]   |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has exfiltrated updated cookies from Google, Naver, Kakao or Daum to the C2 server.[^1]   |
| [[Screen Capture\|T1113]] | Screen Capture | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has the ability to capture screenshots of new browser tabs, based on the presence of the `Capture` flag.[^1]   |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has the ability to capture credentials, cookies, browser screenshots, etc. and to exfiltrate data.[^1]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has been named `GoogleTranslate.crx` to masquerade as a legitimate Chrome extension.[^1]   |
| [[Email Collection\|T1114]] | Email Collection | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has exfiltrated collected email addresses to the C2 server.[^1]   |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has used a Github repository for C2.[^1]   |
| [[Query Registry\|T1012]] | Query Registry | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has queried the following registry key to check for installed Chrome extensions: ` HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist `.[^1]   |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has redirected clients to legitimate Gmail, Naver or Kakao pages if the clients connect with no parameters.[^1]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Kimsuky\|G0094]] | Kimsuky |



## References

[^1]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)


