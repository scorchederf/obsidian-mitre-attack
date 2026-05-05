---
aliases: 
    - T1185
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1185-Browser_Session_Hijacking
tactic: 
     - Collection
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.[^1] <br><br>A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions, and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet.[^5] [^3]  Executing browser-based behaviors such as pivoting may require specific process permissions, such as `SeDebugPrivilege` and/or high-integrity/administrator rights.<br><br>Another example involves pivoting browser traffic from the adversary's browser through the user's browser by setting up a proxy which will redirect web traffic. This does not alter the user's traffic in any way, and the proxy connection can be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet, such as [[kb/mitre/attack/techniques/T1213.002-Sharepoint\|Sharepoint]] or webmail, that is accessible through the browser and which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication.[^2] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Close all browser sessions regularly and when they are no longer needed. |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Since browser pivoting requires a high integrity process to launch from, restricting user permissions and addressing Privilege Escalation and [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|Bypass User Account Control]] opportunities can limit the exposure to this technique. |






> [!info]- References
> [^1]: [Wikipedia Man in the Browser](https://en.wikipedia.org/wiki/Man-in-the-browser)

> [^2]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)

> [^3]: [ICEBRG Chrome Extensions](https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses)

> [^4]: [Breakdev Evilginx 2.2 NOV 2018](https://breakdev.org/evilginx-2-2-jolly-winter-update)

> [^5]: [Cobalt Strike Browser Pivot](https://www.cobaltstrike.com/help-browser-pivoting)


