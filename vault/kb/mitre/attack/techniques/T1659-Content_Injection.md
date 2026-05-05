---
aliases: 
    - T1659
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1659-Content_Injection
tactic: 
     - Initial Access - Command and Control
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., [[kb/mitre/attack/techniques/T1608.004-Drive-by_Target\|Drive-by Target]] followed by [[kb/mitre/attack/techniques/T1189-Drive-by_Compromise\|Drive-by Compromise]]), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|Ingress Tool Transfer]]) and other data to already compromised systems.[^4] <br><br>Adversaries may inject content to victim systems in various ways, including:<br><br>* From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]], which describes AiTM activity solely within an enterprise environment) [^1] <br>* From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server [^3] <br><br>Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception."[^3] [^4] [^2] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Where possible, ensure that online traffic is appropriately encrypted through services such as trusted VPNs. |






> [!info]- References
> [^1]: [Kaspersky Encyclopedia MiTM](https://encyclopedia.kaspersky.com/glossary/man-in-the-middle-attack/)

> [^2]: [EFF China GitHub Attack](https://www.eff.org/deeplinks/2015/04/china-uses-unencrypted-websites-to-hijack-browsers-in-github-attack)

> [^3]: [Kaspersky ManOnTheSide](https://usa.kaspersky.com/blog/man-on-the-side/27854/)

> [^4]: [ESET MoustachedBouncer](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


