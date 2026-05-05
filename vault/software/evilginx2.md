---
aliases: 
    - S9003
    
mitre-attack: https://attack.mitre.org/software/S9003
---

## S9003

[evilginx2](https://attack.mitre.org/software/S9003) is an open-source adversary-in-the-middle (AiTM) attack framework based on the open-source nginx web server. [evilginx2](https://attack.mitre.org/software/S9003) can be used as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens, and session cookies.[^9] [^6] [^1] <br> 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[JavaScript\|T1059.007]] | JavaScript | [evilginx2](https://attack.mitre.org/software/S9003) can inject JavaScript code into HTML content to customize phishing attacks.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [evilginx2](https://attack.mitre.org/software/S9003) has the ability to hide phishing lures for a set time to avoid scanning by sandboxes.[^7]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [evilginx2](https://attack.mitre.org/software/S9003) can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.[^8]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [evilginx2](https://attack.mitre.org/software/S9003) can collect information on each session with a victim including the session cookie.[^9] [^1] <br> |
| [[Web Protocols\|T1071.001]] | Web Protocols | [evilginx2](https://attack.mitre.org/software/S9003) can proxy HTTPS connections between victims and destination websites.[^9] [^8] [^3]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [evilginx2](https://attack.mitre.org/software/S9003) has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.[^9] [^4] [^7] [^1]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [evilginx2](https://attack.mitre.org/software/S9003) can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.[^5]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [evilginx2](https://attack.mitre.org/software/S9003) can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.[^9]  |
| [[Data Encoding\|T1132]] | Data Encoding | [evilginx2](https://attack.mitre.org/software/S9003) can randomly generate and Base64 encode parameters in phishing links to defeat static detection.[^8]  |
| [[Install Root Certificate\|T1553.004]] | Install Root Certificate | [evilginx2](https://attack.mitre.org/software/S9003) has obtained a valid SSL/TLS certificate from LetsEncrypt to provide responses to Automatic Certificate Management Environment (ACME) challenges.[^9]  |
| [[External Proxy\|T1090.002]] | External Proxy | [evilginx2](https://attack.mitre.org/software/S9003) can route traffic via SOCKS5 and HTTP(S) proxies between an intended phishing victim's machine and legitimate websites.[^9] [^8] [^1] <br> |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [evilginx2](https://attack.mitre.org/software/S9003) can capture information from each session with a victim including the public IP used to access the server and the user agent.[^1]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [evilginx2](https://attack.mitre.org/software/S9003) can generate and display phishing URLs including hidden tracking pixels and can also embed URLs within iframes for browser-in-the-browser phishing.[^2] [^3] [^1] <br> |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [evilginx2](https://attack.mitre.org/software/S9003) can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.[^9]  |




## References

[^1]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)


[^2]: [Breakdev Evilginx 2.3 JAN 2019](https://breakdev.org/evilginx-2-3-phishermans-dream/)


[^3]: [Breakdev Evilginx 3.3 APR 2024](https://breakdev.org/evilginx-3-3-go-phish/)


[^4]: [Breakdev Evilginx 3.0 May 2023](https://breakdev.org/evilginx-3-0-evilginx-mastery/)


[^5]: [Breakdev Evilginx 2.2 NOV 2018](https://breakdev.org/evilginx-2-2-jolly-winter-update)


[^6]: [Breakdev Evilginx 2.1 SEP 2018](https://breakdev.org/evilginx-2-1-the-first-post-release-update/)


[^7]: [Breakdev Evilginx 3.2 AUG 2023](https://breakdev.org/evilginx-3-2/)


[^8]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)


[^9]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)


