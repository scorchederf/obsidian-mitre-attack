---
aliases: 
    - S9003
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S9003-evilginx2
---

## Description

[[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] is an open-source adversary-in-the-middle (AiTM) attack framework based on the open-source nginx web server. [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can be used as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens, and session cookies.[^2] [^4] [^9] <br> 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1001-Data_Obfuscation\|T1001]] | Data Obfuscation | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.[^2]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can capture information from each session with a victim including the public IP used to access the server and the user agent.[^9]  |
| [[kb/mitre/attack/techniques/T1059.007-JavaScript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject JavaScript code into HTML content to customize phishing attacks.[^5]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can proxy HTTPS connections between victims and destination websites.[^2] [^8] [^7]  |
| [[kb/mitre/attack/techniques/T1090.002-External_Proxy\|T1090.002]] | External Proxy | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can route traffic via SOCKS5 and HTTP(S) proxies between an intended phishing victim's machine and legitimate websites.[^2] [^8] [^9] <br> |
| [[kb/mitre/attack/techniques/T1111-Multi-Factor_Authentication_Interception\|T1111]] | Multi-Factor Authentication Interception | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.[^2]  |
| [[kb/mitre/attack/techniques/T1132-Data_Encoding\|T1132]] | Data Encoding | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can randomly generate and Base64 encode parameters in phishing links to defeat static detection.[^8]  |
| [[kb/mitre/attack/techniques/T1185-Browser_Session_Hijacking\|T1185]] | Browser Session Hijacking | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.[^3]  |
| [[kb/mitre/attack/techniques/T1480-Execution_Guardrails\|T1480]] | Execution Guardrails | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.[^8]  |
| [[kb/mitre/attack/techniques/T1497.003-Time_Based_Checks\|T1497.003]] | Time Based Checks | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to hide phishing lures for a set time to avoid scanning by sandboxes.[^6]  |
| [[kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie\|T1539]] | Steal Web Session Cookie | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can collect information on each session with a victim including the session cookie.[^2] [^9] <br> |
| [[kb/mitre/attack/techniques/T1553.004-Install_Root_Certificate\|T1553.004]] | Install Root Certificate | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has obtained a valid SSL/TLS certificate from LetsEncrypt to provide responses to Automatic Certificate Management Environment (ACME) challenges.[^2]  |
| [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.[^2] [^1] [^6] [^9]  |
| [[kb/mitre/attack/techniques/T1598.003-Spearphishing_Link\|T1598.003]] | Spearphishing Link | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can generate and display phishing URLs including hidden tracking pixels and can also embed URLs within iframes for browser-in-the-browser phishing.[^5] [^7] [^9] <br> |





> [!info]- References
> [^1]: [Breakdev Evilginx 3.0 May 2023](https://breakdev.org/evilginx-3-0-evilginx-mastery/)

> [^2]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)

> [^3]: [Breakdev Evilginx 2.2 NOV 2018](https://breakdev.org/evilginx-2-2-jolly-winter-update)

> [^4]: [Breakdev Evilginx 2.1 SEP 2018](https://breakdev.org/evilginx-2-1-the-first-post-release-update/)

> [^5]: [Breakdev Evilginx 2.3 JAN 2019](https://breakdev.org/evilginx-2-3-phishermans-dream/)

> [^6]: [Breakdev Evilginx 3.2 AUG 2023](https://breakdev.org/evilginx-3-2/)

> [^7]: [Breakdev Evilginx 3.3 APR 2024](https://breakdev.org/evilginx-3-3-go-phish/)

> [^8]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)

> [^9]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)


