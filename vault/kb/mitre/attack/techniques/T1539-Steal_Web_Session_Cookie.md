---
aliases: 
    - T1539
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie
tactic: 
     - Credential Access
platforms:
     - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.<br><br>Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.[^3] <br><br>There are several examples of malware targeting cookies from web browsers on the local system.[^9] [^6]  Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on [[kb/mitre/attack/techniques/T1204-User_Execution\|User Execution]] by tricking victims into running malicious JavaScript in their browser.[^8] [^1] <br><br>There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]]) that can be set up by an adversary and used in phishing campaigns.[^11] [^2] <br><br>After an adversary acquires a valid cookie, they can then perform a [[kb/mitre/attack/techniques/T1550.004-Web_Session_Cookie\|Web Session Cookie]] technique to login to the corresponding web application.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can collect information on each session with a victim including the session cookie.[^5] [^10] <br> |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train users to identify aspects of phishing attempts where they're asked to enter credentials into a site that has the incorrect domain for the application they are logging into. Additionally, train users not to run untrusted JavaScript in their browser, such as by copying and pasting code or dragging and dropping bookmarklets. |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Deploy hardware-based token (e.g., YubiKey or FIDO key), which incorporates the target login domain as part of the negotiation protocol, will prevent session cookie theft through proxy methods.<br><br>Implement Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. This mitigates the risk of session cookie replay attacks by ensuring that stolen tokens cannot be reused on unauthorized devices. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Implement auditing for authentication activities and user logins to detect the use of stolen session cookies. Monitor for impossible travel scenarios and anomalous behavior that could indicate the use of compromised session tokens or cookies. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Configure browsers or tasks to regularly delete persistent cookies.<br><br>Additionally, minimize the length of time a web cookie is viable to potentially reduce the impact of stolen cookies while also increasing the needed frequency of cookie theft attempts – providing defenders with additional chances at detection.[^7]  For example, use non-persistent cookies to limit the duration a session ID will remain on the web client cache where an attacker could obtain it.[^4]  |






> [!info]- References
> [^1]: [Krebs Discord Bookmarks 2023](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)

> [^2]: [GitHub Mauraena](https://github.com/muraenateam/muraena)

> [^3]: [Pass The Cookie](https://wunderwuzzi23.github.io/blog/passthecookie.html)

> [^4]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

> [^5]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)

> [^6]: [Unit 42 Mac Crypto Cookies January 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)

> [^7]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)

> [^8]: [Talos Roblox Scam 2023](https://blog.talosintelligence.com/roblox-scam-overview/)

> [^9]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)

> [^10]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)

> [^11]: [Github evilginx2](https://github.com/kgretzky/evilginx2)


