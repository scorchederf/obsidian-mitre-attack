---
aliases: 
    - BlackTech
    - Palmerworm
mitre-attack: https://attack.mitre.org/groups/G0098
---

## G0098

[BlackTech](https://attack.mitre.org/groups/G0098) is a suspected Chinese cyber espionage group that has primarily targeted organizations in East Asia--particularly Taiwan, Japan, and Hong Kong--and the US since at least 2013. [BlackTech](https://attack.mitre.org/groups/G0098) has used a combination of custom malware, dual-use tools, and living off the land tactics to compromise media, construction, engineering, electronics, and financial company networks.[^5] [^3] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [BlackTech](https://attack.mitre.org/groups/G0098) has used spearphishing e-mails with links to cloud services to deliver malware.[^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [BlackTech](https://attack.mitre.org/groups/G0098) has used e-mails with malicious links to lure victims into installing malware.[^5] 	  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [BlackTech](https://attack.mitre.org/groups/G0098) has used stolen code-signing certificates for its malicious payloads.[^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [BlackTech](https://attack.mitre.org/groups/G0098) has used the SNScan tool to find other potential targets on victim networks.[^3]  |
| [[Tool\|T1588.002]] | Tool | [BlackTech](https://attack.mitre.org/groups/G0098) has obtained and used tools such as Putty, SNScan, and [PsExec](https://attack.mitre.org/software/S0029) for its operations.[^3]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [BlackTech](https://attack.mitre.org/groups/G0098) has exploited a buffer overflow vulnerability in Microsoft Internet Information Services (IIS) 6.0, CVE-2017-7269, in order to establish a new HTTP or command and control (C2) server.[^5]  |
| [[SSH\|T1021.004]] | SSH | [BlackTech](https://attack.mitre.org/groups/G0098) has used Putty for remote access.[^3]  |
| [[Native API\|T1106]] | Native API | [BlackTech](https://attack.mitre.org/groups/G0098) has used built-in API functions.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [BlackTech](https://attack.mitre.org/groups/G0098) has exploited multiple vulnerabilities for execution, including Microsoft Office vulnerabilities CVE-2012-0158, CVE-2014-6352, CVE-2017-0199, and Adobe Flash CVE-2015-5119.[^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [BlackTech](https://attack.mitre.org/groups/G0098) has used spearphishing e-mails with malicious password-protected archived files (ZIP or RAR) to deliver malware.[^5] [^6]  |
| [[Right-to-Left Override\|T1036.002]] | Right-to-Left Override | [BlackTech](https://attack.mitre.org/groups/G0098) has used right-to-left-override to obfuscate the filenames of malicious e-mail attachments.[^5]  |
| [[DLL\|T1574.001]] | DLL | [BlackTech](https://attack.mitre.org/groups/G0098) has used DLL side loading by giving DLLs hardcoded names and placing them in searched directories.[^10]   |
| [[Malicious File\|T1204.002]] | Malicious File | [BlackTech](https://attack.mitre.org/groups/G0098) has used e-mails with malicious documents to lure victims into installing malware.[^5] [^6] 	  |
| [[Digital Certificates\|T1588.004]] | Digital Certificates | [BlackTech](https://attack.mitre.org/groups/G0098) has used valid, stolen digital certificates for some of their malware and tools.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[PsExec\|S0029]] | PsExec | [^3]  |
| [[Flagpro\|S0696]] | Flagpro | [^6]  |
| [[TSCookie\|S0436]] | TSCookie | [^7]  |
| [[Kivars\|S0437]] | Kivars | [^5] [^3]  |
| [[PLEAD\|S0435]] | PLEAD | [^5] [^8] [^10] [^3]  |
| [[Waterbear\|S0579]] | Waterbear | [^10]  |



## References

[^1]: [IronNet BlackTech Oct 2021](https://www.ironnet.com/blog/china-cyber-attacks-the-current-threat-landscape)


[^2]: [Reuters Taiwan BlackTech August 2020](https://www.reuters.com/article/us-taiwan-cyber-china/taiwan-says-china-behind-cyberattacks-on-government-agencies-emails-idUSKCN25F0JK)


[^3]: [Symantec Palmerworm Sep 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt)


[^4]: [ESET PLEAD Malware July 2018](https://www.welivesecurity.com/2018/07/09/certificates-stolen-taiwanese-tech-companies-plead-malware-campaign/)


[^5]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^6]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^7]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^8]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^9]: Palmerworm


[^10]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


