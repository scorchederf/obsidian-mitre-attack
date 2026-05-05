---
aliases: 
    - APT12
    - IXESHE
    - DynCalc
    - Numbered Panda
    - DNSCALC
mitre-attack: https://attack.mitre.org/groups/G0005
---

## G0005

[APT12](https://attack.mitre.org/groups/G0005) is a threat group that has been attributed to China. The group has targeted a variety of victims including but not limited to media outlets, high-tech companies, and multiple governments.[^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [APT12](https://attack.mitre.org/groups/G0005) has attempted to get victims to open malicious Microsoft Word and PDF attachment sent via spearphishing.[^9] [^2]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [APT12](https://attack.mitre.org/groups/G0005) has used blogs and WordPress for C2 infrastructure.[^3]  |
| [[DNS Calculation\|T1568.003]] | DNS Calculation | [APT12](https://attack.mitre.org/groups/G0005) has used multiple variants of [DNS Calculation](https://attack.mitre.org/techniques/T1568/003) including multiplying the first two octets of an IP address and adding the third octet to that value in order to get a resulting command and control port.[^3]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT12](https://attack.mitre.org/groups/G0005) has exploited multiple vulnerabilities for execution, including Microsoft Office vulnerabilities (CVE-2009-3129, CVE-2012-0158) and vulnerabilities in Adobe Reader and Flash (CVE-2009-4324, CVE-2009-0927, CVE-2011-0609, CVE-2011-0611).[^9] [^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT12](https://attack.mitre.org/groups/G0005) has sent emails with malicious Microsoft Office documents and PDFs attached.[^9] [^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[HTRAN\|S0040]] | HTRAN | [^2]  |
| [[Ixeshe\|S0015]] | Ixeshe | [^8] [^9]  |
| [[RIPTIDE\|S0003]] | RIPTIDE | [^9]  |



## References

[^1]: Numbered Panda


[^2]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^3]: [Meyers Numbered Panda](http://www.crowdstrike.com/blog/whois-numbered-panda/)


[^4]: APT12


[^5]: DNSCALC


[^6]: IXESHE


[^7]: DynCalc


[^8]: [Moran 2013](https://web.archive.org/web/20191224162418/https://www.fireeye.com/blog/threat-research/2013/08/survival-of-the-fittest-new-york-times-attackers-evolve-quickly.html)


[^9]: [Moran 2014](https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html)


