---
aliases: 
    - T1557
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle
tactic: 
     - Credential Access - Collection
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|Network Sniffing]], [[kb/mitre/attack/techniques/T1565.002-Transmitted_Data_Manipulation\|Transmitted Data Manipulation]], or replay attacks ([[kb/mitre/attack/techniques/T1212-Exploitation_for_Credential_Access\|Exploitation for Credential Access]]). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions.[^11] <br><br>For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware.[^10] [^12] [^2]  Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens ([[kb/mitre/attack/techniques/T1528-Steal_Application_Access_Token\|Steal Application Access Token]]) and session cookies ([[kb/mitre/attack/techniques/T1539-Steal_Web_Session_Cookie\|Steal Web Session Cookie]]).[^9] [^7]  [[kb/mitre/attack/techniques/T1689-Downgrade_Attack\|Downgrade Attack]]s can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm.[^5] [^8] [^14] <br><br>Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in [[kb/mitre/attack/techniques/T1565.002-Transmitted_Data_Manipulation\|Transmitted Data Manipulation]]. Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a [[kb/mitre/attack/techniques/T1498-Network_Denial_of_Service\|Network Denial of Service]].


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] opens a new network listener for the `mpnotify.exe` process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.[^4]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.[^3] [^1] [^6] [^13]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train users to be suspicious about certificate errors. Adversaries may use their own certificates in an attempt to intercept HTTPS traffic. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. This may mitigate, or at least alleviate, the scope of AiTM activity. |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that can identify traffic patterns indicative of AiTM activity can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit access to network infrastructure and resources that can be used to reshape traffic or otherwise produce AiTM conditions. |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Use network appliances and host-based security software to block network traffic that is not necessary within the environment, such as legacy protocols that may be leveraged for AiTM conditions. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable legacy network protocols that may be used   to intercept network traffic if applicable, especially those that are not needed within an environment. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1557.001-Name_Resolution_Poisoning_and_SMB_Relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay |
| [[kb/mitre/attack/techniques/T1557.002-ARP_Cache_Poisoning\|T1557.002]] | ARP Cache Poisoning |
| [[kb/mitre/attack/techniques/T1557.003-DHCP_Spoofing\|T1557.003]] | DHCP Spoofing |
| [[kb/mitre/attack/techniques/T1557.004-Evil_Twin\|T1557.004]] | Evil Twin |




> [!info]- References
> [^1]: [Breakdev Evilginx 3.0 May 2023](https://breakdev.org/evilginx-3-0-evilginx-mastery/)

> [^2]: [ad_blocker_with_miner](https://securelist.com/ad-blocker-with-miner-included/101105/)

> [^3]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)

> [^4]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)

> [^5]: [mitm_tls_downgrade_att](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)

> [^6]: [Breakdev Evilginx 3.2 AUG 2023](https://breakdev.org/evilginx-3-2/)

> [^7]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)

> [^8]: [taxonomy_downgrade_att_tls](https://arxiv.org/abs/1809.05681)

> [^9]: [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)

> [^10]: [ttint_rat](https://blog.netlab.360.com/ttint-an-iot-remote-control-trojan-spread-through-2-0-day-vulnerabilities/)

> [^11]: [Rapid7 MiTM Basics](https://www.rapid7.com/fundamentals/man-in-the-middle-attacks/)

> [^12]: [dns_changer_trojans](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/web-attack/125/how-dns-changer-trojans-direct-users-to-threats)

> [^13]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)

> [^14]: [tlseminar_downgrade_att](https://tlseminar.github.io/downgrade-attacks/)


