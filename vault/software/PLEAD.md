---
aliases: 
    - S0435
    
mitre-attack: https://attack.mitre.org/software/S0435
---

## S0435

[PLEAD](https://attack.mitre.org/software/S0435) is a remote access tool (RAT) and downloader used by [BlackTech](https://attack.mitre.org/groups/G0098) in targeted attacks in East Asia including Taiwan, Japan, and Hong Kong.[^4] [^7]  [PLEAD](https://attack.mitre.org/software/S0435) has also been referred to as [TSCookie](https://attack.mitre.org/software/S0436), though more recent reporting indicates likely separation between the two. [PLEAD](https://attack.mitre.org/software/S0435) was observed in use as early as March 2017.[^6] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PLEAD](https://attack.mitre.org/software/S0435) has used HTTP for communications with command and control (C2) servers.[^7] [^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to execute shell commands on the compromised host.[^7]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to steal saved passwords from Microsoft Outlook.[^3]  |
| [[Proxy\|T1090]] | Proxy | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to proxy network communications.[^7]  |
| [[Malicious File\|T1204.002]] | Malicious File | [PLEAD](https://attack.mitre.org/software/S0435) has been executed via malicious e-mail attachments.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to list drives and files on the compromised host.[^4] [^7]  |
| [[Junk Data\|T1001.001]] | Junk Data | [PLEAD](https://attack.mitre.org/software/S0435) samples were found to be highly obfuscated with junk code.[^3] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to upload and download files to and from an infected host.[^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to delete files on the compromised host.[^4]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [PLEAD](https://attack.mitre.org/software/S0435) has been executed via malicious links in e-mails.[^4]  |
| [[Native API\|T1106]] | Native API | [PLEAD](https://attack.mitre.org/software/S0435) can use `ShellExecute` to execute applications.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to list processes on the compromised host.[^4]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to list open windows on the compromised host.[^4] [^4]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [PLEAD](https://attack.mitre.org/software/S0435) has used RC4 encryption to download modules.[^7]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [PLEAD](https://attack.mitre.org/software/S0435) can harvest saved credentials from browsers such as Google Chrome, Microsoft Internet Explorer, and Mozilla Firefox.[^4] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackTech\|G0098]] | BlackTech |



## References

[^1]: [Trend Micro PLEAD RTLO](https://blog.trendmicro.com/trendlabs-security-intelligence/plead-targeted-attacks-against-taiwanese-government-agencies-2/)


[^2]: [Symantec Palmerworm Sep 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt)


[^3]: [ESET PLEAD Malware July 2018](https://www.welivesecurity.com/2018/07/09/certificates-stolen-taiwanese-tech-companies-plead-malware-campaign/)


[^4]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^5]: PLEAD


[^6]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^7]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^8]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


