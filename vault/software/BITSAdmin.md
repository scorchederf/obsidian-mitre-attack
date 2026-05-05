---
aliases: 
    - S0190
    
mitre-attack: https://attack.mitre.org/software/S0190
---

## S0190

[BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). [^10] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files from SMB file servers.[^8]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload files from a compromised host.[^10]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files.[^10]  |
| [[BITS Jobs\|T1197]] | BITS Jobs | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to launch a malicious process.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Wizard Spider\|G0102]] | Wizard Spider |
| [[APT41\|G0096]] | APT41 |
| [[Daggerfly\|G1034]] | Daggerfly |
| [[HEXANE\|G1001]] | HEXANE |
| [[MirrorFace\|G1054]] | MirrorFace |
| [[Leviathan\|G0065]] | Leviathan |
| [[Storm-1811\|G1046]] | Storm-1811 |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |
| [[Ferocious Kitten\|G0137]] | Ferocious Kitten |



## References

[^1]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^2]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)


[^3]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^4]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^5]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^6]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^7]: [RedCanary June Insights 2024](https://redcanary.com/blog/threat-intelligence/intelligence-insights-june-2024/)


[^8]: [Microsoft About BITS](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)


[^9]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^10]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)


[^11]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^12]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


