---
aliases: 
    - M1017
    
mitre-attack: https://attack.mitre.org/mitigations/M1017
---

## M1017

User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:<br><br>Create Comprehensive Training Programs:<br><br>- Design training modules tailored to the organization's risk profile, covering topics such as phishing, password management, and incident reporting.<br>- Provide role-specific training for high-risk employees, such as helpdesk staff or executives.<br><br>Use Simulated Exercises:<br><br>- Conduct phishing simulations to measure user susceptibility and provide targeted follow-up training.<br>- Run social engineering drills to evaluate employee responses and reinforce protocols.<br><br>Leverage Gamification and Engagement:<br><br>- Introduce interactive learning methods such as quizzes, gamified challenges, and rewards for successful detection and reporting of threats.<br><br>Incorporate Security Policies into Onboarding:<br><br>- Include cybersecurity training as part of the onboarding process for new employees.<br>- Provide easy-to-understand materials outlining acceptable use policies and reporting procedures.<br><br>Regular Refresher Courses:<br><br>- Update training materials to include emerging threats and techniques used by adversaries.<br>- Ensure all employees complete periodic refresher courses to stay informed.<br><br>Emphasize Real-World Scenarios:<br><br>- Use case studies of recent attacks to demonstrate the consequences of successful phishing or social engineering.<br>- Discuss how specific employee actions can prevent or mitigate such attacks.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | Users can be trained to identify social engineering techniques and spearphishing messages with malicious links. |
| [[Spearphishing Voice\|T1566.004]] | Spearphishing Voice | Users can be trained to identify and report social engineering techniques and spearphishing attempts, while also being suspicious of and verifying the identify of callers.[^3]  |
| [[User Execution\|T1204]] | User Execution | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[Code Repositories\|T1213.003]] | Code Repositories | Develop and publish policies that define acceptable information to be stored in code repositories. |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint systems or servers. |
| [[Databases\|T1213.006]] | Databases | Develop and publish policies that define acceptable information to be stored in databases and acceptable handling of customer data. Only store information required for business operations.  |
| [[Masquerading\|T1036]] | Masquerading | Train users not to open email attachments or click unknown links (URLs). Such training fosters more secure habits within your organization and will limit many of the risks.   |
| [[Data from Information Repositories\|T1213]] | Data from Information Repositories | Develop and publish policies that define acceptable information to be stored in repositories. |
| [[Phishing for Information\|T1598]] | Phishing for Information | Users can be trained to identify social engineering techniques and spearphishing attempts. |
| [[Confluence\|T1213.001]] | Confluence | Develop and publish policies that define acceptable information to be stored in Confluence repositories. |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |
| [[ARP Cache Poisoning\|T1557.002]] | ARP Cache Poisoning | Train users to be suspicious about certificate errors. Adversaries may use their own certificates in an attempt to intercept HTTPS traffic. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | Users can be trained to identify social engineering techniques and spearphishing attempts. Additionally, users may perform visual checks of the domains they visit; however, homographs in ASCII and in IDN domains and URL schema obfuscation may render manual checks difficult. Phishing training and other cybersecurity training may raise awareness to check URLs before visiting the sites. |
| [[Messaging Applications\|T1213.005]] | Messaging Applications | Develop and publish policies that define acceptable information to be posted in chat applications.  |
| [[Spearphishing Voice\|T1598.004]] | Spearphishing Voice | Users can be trained to identify and report social engineering techniques and spearphishing attempts, while also being suspicious of and verifying the identify of callers.[^3]  |
| [[Customer Relationship Management Software\|T1213.004]] | Customer Relationship Management Software | Develop and publish policies that define acceptable information to be stored in CRM databases and acceptable handling of customer data. Only store customer information required for business operations.  |
| [[Impersonation\|T1684.001]] | Impersonation | Train users to be aware of impersonation tricks and how to counter them, for example confirming incoming requests through an independent platform like a phone call or in-person, to reduce risk. |
| [[Spearphishing Service\|T1598.001]] | Spearphishing Service | Users can be trained to identify social engineering techniques and spearphishing attempts. |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | Train users to be suspicious about certificate errors. Adversaries may use their own certificates in an attempt to intercept HTTPS traffic. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[NTDS\|T1003.003]] | NTDS | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | Close all browser sessions regularly and when they are no longer needed. |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Have a strict approval policy for use of deployment systems. |
| [[Malicious Image\|T1204.003]] | Malicious Image | Train users to be aware of the existence of malicious images and how to avoid deploying instances and containers from them. |
| [[Financial Theft\|T1657]] | Financial Theft | Train and encourage users to identify social engineering techniques used to enable financial theft. Also consider training users on procedures to prevent and respond to swatting and doxing, acts increasingly deployed by financially motivated groups to further coerce victims into satisfying ransom/extortion demands.[^5] [^6]  |
| [[Password Managers\|T1555.005]] | Password Managers | Provide user training on secure practices for managing credentials, including avoiding storing sensitive passwords in browsers and using password managers securely. Users should also be educated on identifying phishing attempts that could steal session cookies or credentials. |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint systems or servers. |
| [[Double File Extension\|T1036.007]] | Double File Extension | Train users to look for double extensions in filenames, and in general use training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | Remove smart cards when not in use. |
| [[Malicious Library\|T1204.005]] | Malicious Library | Train developers to be aware of the existence of malicious libraries and how to avoid installing them.  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | Users need to be trained to not authorize third-party applications they don’t recognize. The user should pay particular attention to the redirect URL: if the URL is a misspelled or convoluted sequence of words related to an expected service or SaaS application, the website is likely trying to spoof a legitimate service. Users should also be cautious about the permissions they are granting to apps. For example, offline access and access to read emails should excite higher suspicions because adversaries can utilize SaaS APIs to discover credentials and other sensitive communications. |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | Provide user training on secure practices for managing credentials, including avoiding storing sensitive passwords in browsers and using password managers securely. Users should also be educated on identifying phishing attempts that could steal session cookies or credentials. |
| [[Spearphishing Attachment\|T1598.002]] | Spearphishing Attachment | Users can be trained to identify social engineering techniques and spearphishing attempts. |
| [[IDE Extensions\|T1176.002]] | IDE Extensions | Train users to minimize IDE extension use, and to only install trusted extensions.  |
| [[Software Extensions\|T1176]] | Software Extensions | Train users to minimize extension use, and to only install trusted extensions.  |
| [[Template Injection\|T1221]] | Template Injection | Train users to identify social engineering techniques and spearphishing emails that could be used to deliver malicious documents. |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | Use user training as a way to bring awareness and raise suspicion for potentially malicious events and dialog boxes (ex: Office documents prompting for credentials). |
| [[Domain Controller Authentication\|T1556.001]] | Domain Controller Authentication | Train users to recognize and handle suspicious email attachments. Emphasize the importance of caution when opening attachments from unknown or unexpected sources, even if they appear legitimate. Implement email warning banners to alert users about emails originating from outside the organization or containing attachments, reinforcing awareness and helping users identify potential spearphishing attempts. |
| [[Evil Twin\|T1557.004]] | Evil Twin | Train users to be suspicious about access points marked as “Open” or “Unsecure” as well as certificate errors. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | Close out all browser sessions when finished using them to prevent any potentially malicious extensions from continuing to run. |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | Users can be trained to identify social engineering techniques and spearphishing emails. |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction. |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |
| [[Sharepoint\|T1213.002]] | Sharepoint | Develop and publish policies that define acceptable information to be stored in SharePoint repositories. |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | Users can be trained to identify social engineering techniques and spearphishing emails with malicious links which includes phishing for consent with OAuth 2.0. Additionally, users may perform visual checks of the domains they visit; however, homographs in ASCII and in IDN domains and URL schema obfuscation may render manual checks difficult. Use email warning banners to alert users when emails contain links from external senders, prompting them to exercise caution and reducing the likelihood of falling victim to spearphishing attacks. Phishing training and other cybersecurity training may raise awareness to check URLs before visiting the sites. |
| [[Social Engineering\|T1684]] | Social Engineering | Reduces success of phishing/vishing/impersonation and modern “human interface” lures.[^4] [^2] [^7]  |
| [[Chat Messages\|T1552.008]] | Chat Messages | Ensure that developers and system administrators are aware of the risk associated with sharing unsecured passwords across communication services. |
| [[Malicious Link\|T1204.001]] | Malicious Link | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[Malicious File\|T1204.002]] | Malicious File | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | Limit credential overlap across accounts and systems by training users and administrators not to use the same password for multiple accounts. |
| [[Valid Accounts\|T1078]] | Valid Accounts | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |
| [[Phishing\|T1566]] | Phishing | Users can be trained to identify social engineering techniques and phishing emails. |
| [[Email Bombing\|T1667]] | Email Bombing | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful social engineering via e-mail bombing. |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | Ensure that a finite amount of ingress points to a software deployment system exist with restricted access for those required to allow and enable newly deployed software. |
| [[Re-opened Applications\|T1547.007]] | Re-opened Applications | Holding the Shift key while logging in prevents apps from opening automatically.[^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | Train users to identify aspects of phishing attempts where they're asked to enter credentials into a site that has the incorrect domain for the application they are logging into. Additionally, train users not to run untrusted JavaScript in their browser, such as by copying and pasting code or dragging and dropping bookmarklets. |
| [[Multi-Factor Authentication Request Generation\|T1621]] | Multi-Factor Authentication Request Generation | Train users to only accept 2FA/MFA requests from login attempts they initiated, to review source location of the login attempt prompting the 2FA/MFA requests, and to report suspicious/unsolicited prompts. |


## References

[^1]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^2]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^3]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^4]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^5]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^6]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^7]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


