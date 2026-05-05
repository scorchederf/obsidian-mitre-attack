---
aliases: 
    - M1060
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1060-Out-of-Band_Communications_Channel
---

## Description

Establish secure out-of-band communication channels to ensure the continuity of critical communications during security incidents, data integrity attacks, or in-network communication failures. Out-of-band communication refers to using an alternative, separate communication path that is not dependent on the potentially compromised primary network infrastructure. This method can include secure messaging apps, encrypted phone lines, satellite communications, or dedicated emergency communication systems. Leveraging these alternative channels reduces the risk of adversaries intercepting, disrupting, or tampering with sensitive communications and helps coordinate an effective incident response.[^2] [^1] 

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1114-Email_Collection\|T1114]] | Email Collection | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email to prevent adversaries from collecting data through compromised email accounts.[^2]  |
| [[kb/mitre/attack/techniques/T1114.001-Local_Email_Collection\|T1114.001]] | Local Email Collection | Implement secure out-of-band alerts to notify security teams of unusual local email activities, such as mass forwarding or large attachments being sent, indicating potential data exfiltration attempts.[^2]  |
| [[kb/mitre/attack/techniques/T1114.002-Remote_Email_Collection\|T1114.002]] | Remote Email Collection | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. <br><br>For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email. This reduces the risk of sensitive data being collected through compromised email accounts.<br><br>Set up out-of-band alerts to notify security teams of unusual email activities, such as mass forwarding or large attachments being sent, which could indicate email collection attempts.<br><br>Create plans for leveraging a secure out-of-band communications channel, rather than an existing in-network email server, in case of a security incident.[^2]  |
| [[kb/mitre/attack/techniques/T1114.003-Email_Forwarding_Rule\|T1114.003]] | Email Forwarding Rule | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. <br><br>For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email. This reduces the risk of sensitive data being collected through compromised email accounts.<br><br>Set up out-of-band alerts to notify security teams of unusual email activities, such as mass forwarding or large attachments being sent, which could indicate email collection attempts.<br><br>Create plans for leveraging a secure out-of-band communications channel, rather than an existing in-network email server, in case of a security incident.[^2]  |
| [[kb/mitre/attack/techniques/T1213-Data_from_Information_Repositories\|T1213]] | Data from Information Repositories | Create plans for leveraging a secure out-of-band communications channel, rather than existing in-network chat applications, in case of a security incident.[^2]  |
| [[kb/mitre/attack/techniques/T1213.005-Messaging_Applications\|T1213.005]] | Messaging Applications | Implement secure out-of-band communication channels to use as an alternative to in-network chat applications during a security incident. This ensures that critical communications remain secure even if primary messaging channels are compromised by adversaries.[^2]  |
| [[kb/mitre/attack/techniques/T1489-Service_Stop\|T1489]] | Service Stop | Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident.[^2]  |



> [!info]- References
> [^1]: [NIST Special Publication 800-53 Revision 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)

> [^2]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


