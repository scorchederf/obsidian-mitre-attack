---
aliases: 
    - Silent Librarian
    - TA407
    - COBALT DICKENS
mitre-attack: https://attack.mitre.org/groups/G0122
---

## G0122

[Silent Librarian](https://attack.mitre.org/groups/G0122) is a group that has targeted research and proprietary data at universities, government agencies, and private sector companies worldwide since at least 2013. Members of  [Silent Librarian](https://attack.mitre.org/groups/G0122) are known to have been affiliated with the Iran-based Mabna Institute which has conducted cyber intrusions at the behest of the government of Iran, specifically the Islamic Revolutionary Guard Corps (IRGC).[^6] [^5] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Digital Certificates\|T1588.004]] | Digital Certificates | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free Let's Encrypt SSL certificates for use on their phishing pages.[^5] [^3]  |
| [[Search Victim-Owned Websites\|T1594]] | Search Victim-Owned Websites | [Silent Librarian](https://attack.mitre.org/groups/G0122) has searched victim's websites to identify the interests and academic areas of targeted individuals and to scrape source code, branding, and organizational contact information for phishing pages.[^6] [^5] [^1]  |
| [[Email Collection\|T1114]] | Email Collection | [Silent Librarian](https://attack.mitre.org/groups/G0122) has exfiltrated entire mailboxes from compromised accounts.[^6]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used links in e-mails to direct victims to credential harvesting websites designed to appear like the targeted organization's login page.[^6] [^5] [^2] [^1] [^3] [^4]  |
| [[Employee Names\|T1589.003]] | Employee Names | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected lists of names for individuals from targeted organizations.[^6]  |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | [Silent Librarian](https://attack.mitre.org/groups/G0122) has set up auto forwarding rules on compromised e-mail accounts.[^6]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has established e-mail accounts to receive e-mails forwarded from compromised accounts.[^6]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected e-mail addresses from targeted organizations from open Internet searches.[^6]  |
| [[Link Target\|T1608.005]] | Link Target | [Silent Librarian](https://attack.mitre.org/groups/G0122) has cloned victim organization login pages and staged them for later use in credential harvesting campaigns. [Silent Librarian](https://attack.mitre.org/groups/G0122) has also made use of a variety of URL shorteners for these staged websites.[^3] [^4] [^1]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used collected lists of names and e-mail accounts to use in password spraying attacks against private sector targets.[^6]  |
| [[Domains\|T1583.001]] | Domains | [Silent Librarian](https://attack.mitre.org/groups/G0122) has acquired domains to establish credential harvesting pages, often spoofing the target organization and using free top level domains .TK, .ML, .GA, .CF, and .GQ.[^6] [^5] [^2] [^1] [^3] [^4]  |
| [[Tool\|T1588.002]] | Tool | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free and publicly available tools including SingleFile and HTTrack to copy login pages of targeted organizations.[^1] [^3]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used compromised credentials to obtain unauthorized access to online accounts.[^6]  |




## References

[^1]: [Proofpoint TA407 September 2019](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian)


[^2]: [Secureworks COBALT DICKENS August 2018](https://www.secureworks.com/blog/back-to-school-cobalt-dickens-targets-universities)


[^3]: [Secureworks COBALT DICKENS September 2019](https://www.secureworks.com/blog/cobalt-dickens-goes-back-to-school-again)


[^4]: [Malwarebytes Silent Librarian October 2020](https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/)


[^5]: [Phish Labs Silent Librarian](https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment)


[^6]: [DOJ Iran Indictments March 2018](https://www.justice.gov/usao-sdny/press-release/file/1045781/download)


[^7]: COBALT DICKENS


[^8]: TA407


