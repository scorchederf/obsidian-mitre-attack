---
aliases: 
    - T1133
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/persistence
    - attack/type/technique
    - platform/containers
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1133-External_Remote_Services
tactic: 
     - Persistence - Initial Access
platforms:
     - Containers - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [[kb/mitre/attack/techniques/T1021.006-Windows_Remote_Management\|Windows Remote Management]] and [[kb/mitre/attack/techniques/T1021.005-VNC\|VNC]] can also be used externally.[^5] <br><br>Access to [[kb/mitre/attack/techniques/T1078-Valid_Accounts\|Valid Accounts]] to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.[^4]  Access to remote services may be used as a redundant or persistent access mechanism during an operation.<br><br>Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.[^1] [^3] <br><br>Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access.[^2]  Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.[^7] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Restrict all traffic to and from public Tor nodes. [^6]  |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use strong two-factor or multi-factor authentication for remote service accounts to mitigate an adversary's ability to leverage stolen credentials, but be aware of [[kb/mitre/attack/techniques/T1111-Multi-Factor_Authentication_Interception\|Multi-Factor Authentication Interception]] techniques for some two-factor authentication implementations. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit access to remote services through centrally managed concentrators such as VPNs and other managed remote access systems. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable or block remotely available services that may be unnecessary. |






> [!info]- References
> [^1]: [Trend Micro Exposed Docker Server](https://www.trendmicro.com/en_us/research/20/f/xorddos-kaiji-botnet-malware-variants-target-exposed-docker-servers.html)

> [^2]: [The BadPilot campaign](https://www.microsoft.com/en-us/security/blog/2025/02/12/the-badpilot-campaign-seashell-blizzard-subgroup-conducts-multiyear-global-access-operation/?ref=thestack.technology)

> [^3]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)

> [^4]: [Volexity Virtual Private Keylogging](https://www.volexity.com/blog/2015/10/07/virtual-private-keylogging-cisco-web-vpns-leveraged-for-access-and-persistence/)

> [^5]: [MacOS VNC software for Remote Desktop](https://support.apple.com/guide/remote-desktop/set-up-a-computer-running-vnc-software-apdbed09830/mac)

> [^6]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)

> [^7]: [Russian threat actors dig in, prepare to seize on war fatigue](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/russian-threat-actors-dig-in-prepare-to-seize-on-war-fatigue)


