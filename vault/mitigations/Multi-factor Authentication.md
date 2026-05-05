---
aliases: 
    - M1032
    
mitre-attack: https://attack.mitre.org/mitigations/M1032
---

## M1032

Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include:<br><br>- *Something you know*: Passwords, PINs.<br>- *Something you have*: Physical tokens, smartphone authenticator apps.<br>- *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans.<br><br>Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures:<br><br>Identity and Access Management (IAM):<br><br>- Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles.<br>- Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations).<br>- Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra.<br><br>Authentication Tools and Methods:<br><br>- Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP).<br>- Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security.<br>- Enforce biometric authentication for compatible devices and applications.<br><br>Secure Legacy Systems:<br><br>- Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet.<br>- Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins.<br><br>Monitoring and Alerting:<br><br>- Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems.<br>- Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations.<br><br>Training and Policy Enforcement:<br><br>- Educate employees on the importance of MFA and secure authenticator usage.<br>- Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Additional Cloud Credentials\|T1098.001]] | Additional Cloud Credentials | Use multi-factor authentication for user and privileged accounts. Consider enforcing multi-factor authentication for the `CreateKeyPair` and `ImportKeyPair` API calls through IAM policies.[^8]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | Use multi-factor authentication wherever possible. |
| [[Local Account\|T1136.001]] | Local Account | Use multi-factor authentication for user and privileged accounts. |
| [[Wi-Fi Networks\|T1669]] | Wi-Fi Networks | Harden access requirements for Wi-Fi networks through using two or more pieces of evidence to authenticate, such as a username and password in addition to a token from a physical smart card or token generator. |
| [[Pluggable Authentication Modules\|T1556.003]] | Pluggable Authentication Modules | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs.  |
| [[Data from Information Repositories\|T1213]] | Data from Information Repositories | Use two or more pieces of evidence to authenticate to a system; such as username and password in addition to a token from a physical smart card or token generator. |
| [[Network Boundary Bridging\|T1599]] | Network Boundary Bridging | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control.[^6]  |
| [[Email Collection\|T1114]] | Email Collection | Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries. |
| [[Multi-Factor Authentication Request Generation\|T1621]] | Multi-Factor Authentication Request Generation | Implement more secure 2FA/MFA mechanisms in replacement of simple push or one-click 2FA/MFA options. For example, having users enter a one-time code provided by the login screen into the 2FA/MFA application or utilizing other out-of-band 2FA/MFA mechanisms (such as rotating code-based hardware tokens providing rotating codes that need an accompanying user pin) may be more secure. Furthermore, change default configurations and implement limits upon the maximum number of 2FA/MFA request prompts that can be sent to users in period of time.[^3]  |
| [[Default Accounts\|T1078.001]] | Default Accounts | Implement multi-factor authentication (MFA) for default accounts whenever possible to prevent unauthorized access, even if credentials for these accounts are compromised. MFA adds an additional layer of security that requires more than just a username and password, making it significantly harder for adversaries to exploit these accounts for initial access or lateral movement. |
| [[Modify System Image\|T1601]] | Modify System Image | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control.[^6]  |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs. |
| [[Domain Account\|T1136.002]] | Domain Account | Use multi-factor authentication for user and privileged accounts. |
| [[Cloud Account\|T1136.003]] | Cloud Account | Use multi-factor authentication for user and privileged accounts. |
| [[Local Accounts\|T1078.003]] | Local Accounts | Enable multi-factor authentication (MFA) for local accounts to add an extra layer of protection against credential theft and misuse. MFA can be implemented using methods like mobile-based authenticators or hardware tokens, even in environments that do not rely on domain controllers or cloud services. This additional security measure can help reduce the risk of adversaries gaining unauthorized access to local systems and resources. |
| [[Device Registration\|T1098.005]] | Device Registration | Require multi-factor authentication to register devices in Entra ID.[^2]  Configure multi-factor authentication systems to disallow enrolling new devices for inactive accounts.[^1]  When first enrolling MFA, use conditional access policies to restrict device enrollment to trusted locations or devices, and consider using temporary access passes as an initial MFA solution to enroll a device.[^4]  |
| [[Password Spraying\|T1110.003]] | Password Spraying | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | Use multi-factor authentication for cloud accounts, especially privileged accounts. This can be implemented in a variety of forms (e.g. hardware, virtual, SMS), and can also be audited using administrative reporting features.[^5]  |
| [[Downgrade System Image\|T1601.002]] | Downgrade System Image | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control.[^6]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | Use multi-factor authentication for user and privileged accounts. |
| [[Hybrid Identity\|T1556.007]] | Hybrid Identity | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs.  |
| [[SSH\|T1021.004]] | SSH | Require multi-factor authentication for SSH connections wherever possible, such as password protected SSH keys. |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | Deploy hardware-based token (e.g., YubiKey or FIDO key), which incorporates the target login domain as part of the negotiation protocol, will prevent session cookie theft through proxy methods.<br><br>Implement Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. This mitigates the risk of session cookie replay attacks by ensuring that stolen tokens cannot be reused on unauthorized devices. |
| [[Network Address Translation Traversal\|T1599.001]] | Network Address Translation Traversal | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control. [^6]  |
| [[Additional Cloud Roles\|T1098.003]] | Additional Cloud Roles | Use multi-factor authentication for user and privileged accounts. |
| [[Password Guessing\|T1110.001]] | Password Guessing | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries. |
| [[Trusted Relationship\|T1199]] | Trusted Relationship | Require MFA for all delegated administrator accounts.[^7]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | Use multi-factor authentication for remote logins.[^10]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | Implement multi-factor authentication (MFA) across all account types, including default, local, domain, and cloud accounts, to prevent unauthorized access, even if credentials are compromised. MFA provides a critical layer of security by requiring multiple forms of verification beyond just a password. This measure significantly reduces the risk of adversaries abusing valid accounts to gain initial access, escalate privileges, maintain persistence, or evade defenses within your network. |
| [[Create Account\|T1136]] | Create Account | Use multi-factor authentication for user and privileged accounts. |
| [[Domain Controller Authentication\|T1556.001]] | Domain Controller Authentication | Integrating multi-factor authentication (MFA) as part of organizational policy can greatly reduce the risk of an adversary gaining control of valid credentials that may be used for additional tactics such as initial access, lateral movement, and collecting information. MFA can also be used to restrict access to cloud resources and APIs.  |
| [[Data Destruction\|T1485]] | Data Destruction | Implement multi-factor authentication (MFA) delete for cloud storage resources, such as AWS S3 buckets, to prevent unauthorized deletion of critical data and infrastructure. MFA delete requires additional authentication steps, making it significantly more difficult for adversaries to destroy data without proper credentials. This additional security layer helps protect against the impact of data destruction in cloud environments by ensuring that only authenticated actions can irreversibly delete storage or machine images. |
| [[Additional Container Cluster Roles\|T1098.006]] | Additional Container Cluster Roles | Require multi-factor authentication for user accounts integrated into container clusters through cloud deployments or via authentication protocols such as LDAP or SAML.  |
| [[Cloud Services\|T1021.007]] | Cloud Services | Use multi-factor authentication on cloud services whenever possible. |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Ensure proper system and access isolation for critical network systems through use of multi-factor authentication. |
| [[Brute Force\|T1110]] | Brute Force | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[Credential Stuffing\|T1110.004]] | Credential Stuffing | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[Password Cracking\|T1110.002]] | Password Cracking | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| [[Remote Services\|T1021]] | Remote Services | Use multi-factor authentication on remote service logons where possible. |
| [[External Remote Services\|T1133]] | External Remote Services | Use strong two-factor or multi-factor authentication for remote service accounts to mitigate an adversary's ability to leverage stolen credentials, but be aware of [Multi-Factor Authentication Interception](https://attack.mitre.org/techniques/T1111) techniques for some two-factor authentication implementations. |
| [[Additional Email Delegate Permissions\|T1098.002]] | Additional Email Delegate Permissions | Use multi-factor authentication for user and privileged accounts. |
| [[Multi-Factor Authentication\|T1556.006]] | Multi-Factor Authentication | Ensure that MFA and MFA policies and requirements are properly implemented for existing and deactivated or dormant accounts and devices. If possible, consider configuring MFA solutions to "fail closed" rather than grant access in case of serious errors. |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | Consider using multi-factor authentication to restrict access to resources and cloud storage APIs.[^9]  |
| [[Patch System Image\|T1601.001]] | Patch System Image | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control.[^6]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | Use multi-factor authentication for logons to code repositories. |
| [[Network Device Authentication\|T1556.004]] | Network Device Authentication | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS.  Follow vendor prescribed best practices for hardening access control. [^6]  |


## References

[^1]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^2]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^3]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^4]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^5]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^6]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^7]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^8]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^9]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^10]: [Berkley Secure](https://security.berkeley.edu/node/94)


