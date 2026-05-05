---
aliases: 
    - Elderwood
    - Elderwood Gang
    - Beijing Group
    - Sneaky Panda
mitre-attack: https://attack.mitre.org/groups/G0066
---

## G0066

[Elderwood](https://attack.mitre.org/groups/G0066) is a suspected Chinese cyber espionage group that was reportedly responsible for the 2009 Google intrusion known as Operation Aurora. [^2]  The group has targeted defense organizations, supply chain manufacturers, human rights and nongovernmental organizations (NGOs), and IT service providers. [^4]  [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Elderwood](https://attack.mitre.org/groups/G0066) has encrypted documents and malicious executables.[^4]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Elderwood](https://attack.mitre.org/groups/G0066) has leveraged multiple types of spearphishing in order to attempt to get a user to open attachments.[^4] [^7]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Elderwood](https://attack.mitre.org/groups/G0066) has delivered zero-day exploits and malware to victims via targeted emails containing a link to malicious content hosted on an uncommon Web server.[^4] [^7]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Elderwood](https://attack.mitre.org/groups/G0066) has delivered zero-day exploits and malware to victims via targeted emails containing malicious attachments.[^4] [^7]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Elderwood](https://attack.mitre.org/groups/G0066) has leveraged multiple types of spearphishing in order to attempt to get a user to open links.[^4] [^7]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Elderwood](https://attack.mitre.org/groups/G0066) has delivered zero-day exploits and malware to victims by injecting malicious code into specific public Web pages visited by targets within a particular sector.[^4] [^7] [^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Elderwood](https://attack.mitre.org/groups/G0066) has used exploitation of endpoint software, including Microsoft Internet Explorer Adobe Flash vulnerabilities, to gain execution. They have also used zero-day exploits.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | The Ritsol backdoor trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) can download files onto a compromised host from a remote location.[^5]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Elderwood](https://attack.mitre.org/groups/G0066) has packed malware payloads before delivery to victims.[^4]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Wiarp\|S0206]] | Wiarp | [^4]  |
| [[Naid\|S0205]] | Naid | [^4]  |
| [[Hydraq\|S0203]] | Hydraq | [^4]  |
| [[Briba\|S0204]] | Briba | [^4]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^4]  |
| [[Nerex\|S0210]] | Nerex | [^4]  |
| [[Pasam\|S0208]] | Pasam | [^4]  |
| [[Linfo\|S0211]] | Linfo | [^4]  |
| [[Vasport\|S0207]] | Vasport | [^4]  |



## References

[^1]: Sneaky Panda


[^2]: [Security Affairs Elderwood Sept 2012](http://securityaffairs.co/wordpress/8528/hacking/elderwood-project-who-is-behind-op-aurora-and-ongoing-attacks.html)


[^3]: Elderwood


[^4]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^5]: [Symantec Ristol May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3909-99)


[^6]: Elderwood Gang


[^7]: [CSM Elderwood Sept 2012](https://www.csmonitor.com/USA/2012/0914/Stealing-US-business-secrets-Experts-ID-two-huge-cyber-gangs-in-China)


[^8]: Beijing Group


