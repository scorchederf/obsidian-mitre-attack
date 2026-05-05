---
aliases: 
    - S0144
    
mitre-attack: https://attack.mitre.org/software/S0144
---

## S0144

[ChChes](https://attack.mitre.org/software/S0144) is a Trojan that appears to be used exclusively by [menuPass](https://attack.mitre.org/groups/G0045). It was used to target Japanese organizations in 2016. Its lack of persistence methods suggests it may be intended as a first-stage tool. [^3]  [^8]  [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ChChes](https://attack.mitre.org/software/S0144) communicates to its C2 server over HTTP and embeds data within the Cookie HTTP header.[^3] [^8]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ChChes](https://attack.mitre.org/software/S0144) establishes persistence by adding a Registry Run key.[^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [ChChes](https://attack.mitre.org/software/S0144) can encode C2 data with a custom technique that utilizes Base64.[^3] [^8] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ChChes](https://attack.mitre.org/software/S0144) is capable of downloading files, including additional modules.[^3] [^8] [^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [ChChes](https://attack.mitre.org/software/S0144) can alter the victim's proxy configuration.[^5]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [ChChes](https://attack.mitre.org/software/S0144) steals credentials stored inside Internet Explorer.[^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ChChes](https://attack.mitre.org/software/S0144) collects the victim hostname, window resolution, and Microsoft Windows version.[^3] [^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ChChes](https://attack.mitre.org/software/S0144) collects the victim's %TEMP% directory path and version of Internet Explorer.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [ChChes](https://attack.mitre.org/software/S0144) can encrypt C2 traffic with AES or RC4.[^3] [^8]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [ChChes](https://attack.mitre.org/software/S0144) copies itself to an .exe file with a filename that is likely intended to imitate Norton Antivirus but has several letters reversed (e.g. notron.exe).[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ChChes](https://attack.mitre.org/software/S0144) collects its process identifier (PID) on the victim.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [ChChes](https://attack.mitre.org/software/S0144) samples were digitally signed with a certificate originally used by Hacking Team that was later leaked and subsequently revoked.[^3] [^8] [^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[menuPass\|G0045]] | menuPass |



## References

[^1]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^2]: Scorpion


[^3]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^4]: ChChes


[^5]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^6]: [Twitter Nick Carr APT10](https://x.com/ItsReallyNick/status/850105140589633536)


[^7]: HAYMAKER


[^8]: [JPCERT ChChes Feb 2017](https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html)


