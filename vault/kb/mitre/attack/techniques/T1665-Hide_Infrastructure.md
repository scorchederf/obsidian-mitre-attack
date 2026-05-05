---
aliases: 
    - T1665
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1665-Hide_Infrastructure
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools,[^9]  masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers,[^6] [^1] [^3]  and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.<br><br>C2 networks may include the use of [[kb/mitre/attack/techniques/T1090-Proxy\|Proxy]] or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address.[^2] [^5] <br><br>Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents.[^8] [^10]  Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]]).[^9] [^8] <br><br>Hiding C2 infrastructure may also be supported by [[kb/mitre/attack/tactics/TA0042-Resource_Development\|Resource Development]] activities such as [[kb/mitre/attack/techniques/T1583-Acquire_Infrastructure\|Acquire Infrastructure]] and [[kb/mitre/attack/techniques/T1584-Compromise_Infrastructure\|Compromise Infrastructure]]. For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met.[^7] [^4] 








> [!info]- References
> [^1]: [Facad1ng](https://github.com/spyboy-productions/Facad1ng)

> [^2]: [sysdig](https://sysdig.com/content/c/pf-2023-global-cloud-threat-report?x=u_WFRi&xs=524303#page=1)

> [^3]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)

> [^4]: [QR-cofense](https://cofense.com/blog/major-energy-company-targeted-in-large-qr-code-campaign/)

> [^5]: [Orange Residential Proxies](https://www.orangecyberdefense.com/global/blog/research/residential-proxies)

> [^6]: [Schema-abuse](https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse)

> [^7]: [StarBlizzard](https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/)

> [^8]: [mod_rewrite](https://bluescreenofjeff.com/2016-04-12-combatting-incident-responders-with-apache-mod_rewrite/)

> [^9]: [TA571](https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta571-delivers-icedid-forked-loader)

> [^10]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


