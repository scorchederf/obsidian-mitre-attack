---
aliases: 
    - M1021
    
mitre-attack: https://attack.mitre.org/mitigations/M1021
---

## M1021

Restricting web-based content involves enforcing policies and technologies that limit access to potentially malicious websites, unsafe downloads, and unauthorized browser behaviors. This can include URL filtering, download restrictions, script blocking, and extension control to protect against exploitation, phishing, and malware delivery. This mitigation can be implemented through the following measures:<br><br>Deploy Web Proxy Filtering:<br><br>- Use solutions to filter web traffic based on categories, reputation, and content types.<br>- Enforce policies that block unsafe websites or file types at the gateway level.<br><br>Enable DNS-Based Filtering:<br><br>- Implement tools to restrict access to domains associated with malware or phishing campaigns.<br>- Use public DNS filtering services to enhance protection.<br><br>Enforce Content Security Policies (CSP):<br><br>- Configure CSP headers on internal and external web applications to restrict script execution, iframe embedding, and cross-origin requests.<br><br>Control Browser Features:<br><br>- Disable unapproved browser features like automatic downloads, developer tools, or unsafe scripting.<br>- Enforce policies through tools like Group Policy Management to control browser settings.<br><br>Monitor and Alert on Web-Based Threats:<br><br>- Use SIEM tools to collect and analyze web proxy logs for signs of anomalous or malicious activity.<br>- Configure alerts for access attempts to blocked domains or repeated file download failures.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Content Injection\|T1659]] | Content Injection | Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns. |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | Determine if certain websites that can be used for spearphishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | Administrators can block end-user consent to OAuth applications, disabling users from authorizing third-party apps through OAuth 2.0 and forcing administrative consent for all requests. They can also block end-user registration of applications by their users, to reduce risk. A Cloud Access Security Broker can also be used to ban applications.<br><br>Azure offers a couple of enterprise policy settings in the Azure Management Portal that may help:<br><br>"Users -> User settings -> App registrations: Users can register applications" can be set to "no" to prevent users from registering new applications. <br>"Enterprise applications -> User settings -> Enterprise applications: Users can consent to apps accessing company data on their behalf" can be set to "no" to prevent users from consenting to allow third-party multi-tenant applications |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface. |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns, such as CHM files |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | In some cases a local DNS sinkhole may be used to help prevent behaviors associated with dynamic resolution. |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |
| [[User Execution\|T1204]] | User Execution | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| [[External Remote Services\|T1133]] | External Remote Services | Restrict all traffic to and from public Tor nodes. [^3]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | Adblockers can help prevent malicious code served through ads from executing in the first place. Script blocking extensions can also help to prevent the execution of JavaScript. <br><br>Consider disabling browser push notifications from certain applications and browsers.[^5] [^2] [^4]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | Determine if certain social media sites, personal webmail services, or other service that can be used for spearphishing is necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | In some cases a local DNS sinkhole may be used to help prevent DGA-based command and control at a reduced cost. |
| [[Application Access Token\|T1550.001]] | Application Access Token | Update corporate policies to restrict what types of third-party applications may be added to any online service or tool that is linked to the company's information, accounts or network (e.g., Google, Microsoft, Dropbox, Basecamp, GitHub). However, rather than providing high-level guidance on this, be extremely specific—include a list of per-approved applications and deny all others not on the list. Administrators may also block end-user consent through administrative portals, such as the Azure Portal, disabling users from authorizing third-party apps through OAuth and forcing administrative consent.[^1]  |
| [[Web Service\|T1102]] | Web Service | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |
| [[Phishing\|T1566]] | Phishing | Determine if certain websites or attachment types (ex: .scr, .exe, .pif, .cpl, etc.) that can be used for phishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | If a link is being requested by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as `.scr`, `.exe`, `.pif`, `.cpl`, etc.   |
| [[Visual Basic\|T1059.005]] | Visual Basic | Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |
| [[Trusted Developer Utilities Proxy Execution\|T1127]] | Trusted Developer Utilities Proxy Execution | Consider disabling software installation or execution from the internet via developer utilities. |
| [[JavaScript\|T1059.007]] | JavaScript | Script blocking extensions can help prevent the execution of JavaScript and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface. |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | Script blocking extensions can help prevent the execution of scripts and HTA files that may commonly be used during the exploitation process. For malicious code served up through ads, adblockers can help prevent that code from executing in the first place. |
| [[System Binary Proxy Execution\|T1218]] | System Binary Proxy Execution | Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc. |
| [[Exfiltration to Code Repository\|T1567.001]] | Exfiltration to Code Repository | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[ClickOnce\|T1127.002]] | ClickOnce | Disable ClickOnce installations from the internet using the following registry key: <br>`\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\Security\TrustManager\PromptingLevel — Internet:Disabled`[^6]  |
| [[Exfiltration to Text Storage Sites\|T1567.003]] | Exfiltration to Text Storage Sites | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[Malicious Link\|T1204.001]] | Malicious Link | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | Block unknown or unused attachments by default that should not be transmitted over email as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some email scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious attachments. |


## References

[^1]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^2]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^3]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^4]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^5]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^6]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


