---
aliases: 
    - S0336
    
mitre-attack: https://attack.mitre.org/software/S0336
---

## S0336

[NanoCore](https://attack.mitre.org/software/S0336) is a modular remote access tool developed in .NET that can be used to spy on victims and steal information. It has been used by threat actors since 2013.[^1] [^7] [^6] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NanoCore](https://attack.mitre.org/software/S0336) has the capability to download and activate additional modules for execution.[^1] [^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [NanoCore](https://attack.mitre.org/software/S0336) can open a remote command-line interface and execute commands.[^6]  [NanoCore](https://attack.mitre.org/software/S0336) uses JavaScript files.[^7]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [NanoCore](https://attack.mitre.org/software/S0336) gathers the IP address from the victim’s machine.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [NanoCore](https://attack.mitre.org/software/S0336) can access the victim's webcam and capture data.[^1] [^6]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [NanoCore](https://attack.mitre.org/software/S0336)’s plugins were obfuscated with Eazfuscater.NET 3.3.[^6]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [NanoCore](https://attack.mitre.org/software/S0336) can modify the victim's anti-virus.[^1] [^6]  |
| [[Audio Capture\|T1123]] | Audio Capture | [NanoCore](https://attack.mitre.org/software/S0336) can capture audio feeds from the system.[^1] [^6]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [NanoCore](https://attack.mitre.org/software/S0336) can modify the victim's firewall.[^1] [^6]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [NanoCore](https://attack.mitre.org/software/S0336) uses VBS files.[^7]  |
| [[Keylogging\|T1056.001]] | Keylogging | [NanoCore](https://attack.mitre.org/software/S0336) can perform keylogging on the victim’s machine.[^6]  |
| [[Modify Registry\|T1112]] | Modify Registry | [NanoCore](https://attack.mitre.org/software/S0336) has the capability to edit the Registry.[^1] [^6]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [NanoCore](https://attack.mitre.org/software/S0336) uses DES to encrypt the C2 traffic.[^6]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [NanoCore](https://attack.mitre.org/software/S0336) creates a RunOnce key in the Registry to execute its VBS scripts each time the user logs on to the machine.[^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT33\|G0064]] | APT33 |
| [[SilverTerrier\|G0083]] | SilverTerrier |
| [[Gorgon Group\|G0078]] | Gorgon Group |
| [[Group5\|G0043]] | Group5 |



## References

[^1]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)


[^2]: [Unit42 SilverTerrier 2018](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)


[^3]: [Citizen Lab Group5](https://citizenlab.ca/2016/08/group5-syria/)


[^4]: [FireEye APT33 Webinar Sept 2017](https://www.brighttalk.com/webcast/10703/275683)


[^5]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^6]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^7]: [Cofense NanoCore Mar 2018](https://web.archive.org/web/20240522112705/https://cofense.com/blog/nanocore-rat-resurfaced-sewers/)


[^8]: NanoCore


