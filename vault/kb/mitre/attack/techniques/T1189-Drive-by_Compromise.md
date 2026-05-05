---
aliases: 
    - T1189
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1189-Drive-by_Compromise
tactic: 
     - Initial Access
platforms:
     - Identity Provider - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. Multiple ways of delivering exploit code to a browser exist (i.e., [[kb/mitre/attack/techniques/T1608.004-Drive-by_Target\|Drive-by Target]]), including:<br><br>* A legitimate website is compromised, allowing adversaries to inject malicious code<br>* Script files served to a legitimate website from a publicly writeable cloud storage bucket are modified by an adversary<br>* Malicious ads are paid for and served through legitimate ad providers (i.e., [[kb/mitre/attack/techniques/T1583.008-Malvertising\|Malvertising]])<br>* Built-in web application interfaces that allow user-controllable content are leveraged for the insertion of malicious scripts or iFrames (e.g., cross-site scripting)<br><br>Browser push notifications may also be abused by adversaries and leveraged for malicious code injection via [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]]. By clicking "allow" on browser push notifications, users may be granting a website permission to run JavaScript code on their browser.[^8] [^3] [^7] <br><br>Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or a particular region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.[^9] <br><br>Typical drive-by compromise process:<br><br>1. A user visits a website that is used to host the adversary controlled content.<br>2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. The user may be required to assist in this process by enabling scripting, notifications, or active website components and ignoring warning dialog boxes.<br>3. Upon finding a vulnerable version, exploit code is delivered to the browser.<br>4. If exploitation is successful, the adversary will gain code execution on the user's system unless other protections are in place. In some cases, a second visit to the website after the initial scan is required before exploit code is delivered.<br><br>Unlike [[kb/mitre/attack/techniques/T1190-Exploit_Public-Facing_Application\|Exploit Public-Facing Application]], the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction. |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Adblockers can help prevent malicious code served through ads from executing in the first place. Script blocking extensions can also help to prevent the execution of JavaScript. <br><br>Consider disabling browser push notifications from certain applications and browsers.[^5] [^11] [^10]  |
| [[kb/mitre/attack/mitigations/M1048-Application_Isolation_and_Sandboxing\|M1048]] | Application Isolation and Sandboxing | Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist.[^2] [^12] <br><br>Other types of virtualization and application microsegmentation may also mitigate the impact of client-side exploitation. The risks of additional exploits and weaknesses in implementation may still exist for these types of systems.[^12]  |
| [[kb/mitre/attack/mitigations/M1050-Exploit_Protection\|M1050]] | Exploit Protection | Security applications that look for behavior used during exploitation such as Windows Defender Exploit Guard (WDEG) and the Enhanced Mitigation Experience Toolkit (EMET) can be used to mitigate some exploitation behavior.[^4]  Control flow integrity checking is another way to potentially identify and stop a software exploit from occurring.[^6]  Many of these protections depend on the architecture and target application binary for compatibility. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Ensuring that all browsers and plugins are kept updated can help prevent the exploit phase of this technique. Use modern browsers with security features turned on.[^1] <br> |






> [!info]- References
> [^1]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)

> [^2]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)

> [^3]: [push notification -mcafee](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/scammers-impersonating-windows-defender-to-push-malicious-windows-apps/)

> [^4]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)

> [^5]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)

> [^6]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)

> [^7]: [push notifications - malwarebytes](https://www.malwarebytes.com/blog/news/2019/01/browser-push-notifications-feature-asking-abused)

> [^8]: [Push notifications - viruspositive](https://viruspositive.com/resources/blogs/the-dark-side-of-web-push-notifications)

> [^9]: [Shadowserver Strategic Web Compromise](http://blog.shadowserver.org/2012/05/15/cyber-espionage-strategic-web-compromises-trusted-websites-serving-dangerous-results/)

> [^10]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)

> [^11]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)

> [^12]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


