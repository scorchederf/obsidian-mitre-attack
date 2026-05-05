---
aliases: 
    - Machete
    - APT-C-43
    - El Machete
mitre-attack: https://attack.mitre.org/groups/G0095
---

## G0095

[Machete](https://attack.mitre.org/groups/G0095) is a suspected Spanish-speaking cyber espionage group that has been active since at least 2010. It has primarily focused its operations within Latin America, with a particular emphasis on Venezuela, but also in the US, Europe, Russia, and parts of Asia. [Machete](https://attack.mitre.org/groups/G0095) generally targets high-profile organizations such as government institutions, intelligence services, and military units, as well as telecommunications and power companies.[^5] [^3] [^7] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [Machete](https://attack.mitre.org/groups/G0095) has relied on users opening malicious attachments delivered through spearphishing to execute malware.[^5] [^3] [^7] [^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Machete](https://attack.mitre.org/groups/G0095) has sent phishing emails that contain a link to an external server with ZIP and RAR archives.[^5] [^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Machete](https://attack.mitre.org/groups/G0095) has used batch files to initiate additional downloads of malicious files.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Machete](https://attack.mitre.org/groups/G0095) has embedded malicious macros within spearphishing attachments to download additional files.[^2]  |
| [[Python\|T1059.006]] | Python | [Machete](https://attack.mitre.org/groups/G0095) used multiple compiled Python scripts on the victim’s system. [Machete](https://attack.mitre.org/groups/G0095)'s main backdoor [Machete](https://attack.mitre.org/software/S0409) is also written in Python.[^5] [^7] [^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Machete](https://attack.mitre.org/groups/G0095) has created scheduled tasks to maintain [Machete](https://attack.mitre.org/software/S0409)'s persistence.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Machete](https://attack.mitre.org/groups/G0095)'s [Machete](https://attack.mitre.org/software/S0409) MSI installer has masqueraded as a legitimate Adobe Acrobat Reader installer.[^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Machete](https://attack.mitre.org/groups/G0095) has has relied on users opening malicious links delivered through spearphishing to execute malware.[^5] [^3] [^7]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Machete](https://attack.mitre.org/groups/G0095) has distributed [Machete](https://attack.mitre.org/software/S0409) through a fake blog website.[^3]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment |  [Machete](https://attack.mitre.org/groups/G0095) has delivered spearphishing emails that contain a zipped file with malicious contents.[^3] [^7] [^2]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Machete](https://attack.mitre.org/groups/G0095) has used msiexec to install the [Machete](https://attack.mitre.org/software/S0409) malware.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Machete\|S0409]] | Machete | [^3] [^7]  |



## References

[^1]: El Machete


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)


[^4]: Machete


[^5]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^6]: APT-C-43


[^7]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


