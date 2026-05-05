---
aliases: 
    - T1114
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1114-Email_Collection
tactic: 
     - Collection
platforms:
     - Windows - macOS - Linux - Office Suite
permissions required:
     - none
---

## Description

Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses.[^2] [^1]  Adversaries can collect or forward email from mail servers or clients. 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1032-Multi-factor_Authentication\|M1032]] | Multi-factor Authentication | Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis.<br><br>In an Exchange environment, Administrators can use Get-InboxRule to discover and remove potentially malicious auto-forwarding rules.[^3]   |
| [[kb/mitre/attack/mitigations/M1060-Out-of-Band_Communications_Channel\|M1060]] | Out-of-Band Communications Channel | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email to prevent adversaries from collecting data through compromised email accounts.[^2]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1114.001-Local_Email_Collection\|T1114.001]] | Local Email Collection |
| [[kb/mitre/attack/techniques/T1114.002-Remote_Email_Collection\|T1114.002]] | Remote Email Collection |
| [[kb/mitre/attack/techniques/T1114.003-Email_Forwarding_Rule\|T1114.003]] | Email Forwarding Rule |




> [!info]- References
> [^1]: [CISA AA20-352A 2021](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)

> [^2]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)

> [^3]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


