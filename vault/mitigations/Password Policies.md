---
aliases: 
    - M1027
    
mitre-attack: https://attack.mitre.org/mitigations/M1027
---

## M1027

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:<br><br>Windows Systems:<br><br>- Use Group Policy Management Console (GPMC) to configure:<br>    - Minimum password length (e.g., 12+ characters).<br>    - Password complexity requirements.<br>    - Password history (e.g., disallow last 24 passwords).<br>    - Account lockout duration and thresholds.<br><br>Linux Systems:<br><br>- Configure Pluggable Authentication Modules (PAM):<br>- Use `pam_pwquality` to enforce complexity and length requirements.<br>- Implement `pam_tally2` or `pam_faillock` for account lockouts.<br>- Use `pwunconv` to disable password reuse.<br><br>Password Managers:<br><br>- Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords.<br><br>Password Blacklisting:<br><br>- Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords.<br><br>Regular Auditing:<br><br>- Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners.<br><br>*Tools for Implementation*<br><br>Windows:<br><br>- Group Policy Management Console (GPMC): Enforce password policies.<br>- Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords.<br><br>Linux/macOS:<br><br>- PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules.<br>- Lynis: Audit password policies and system configurations.<br><br>Cross-Platform:<br><br>- Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords.<br>- Have I Been Pwned API: Prevent the use of breached passwords.<br>- NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Network Address Translation Traversal\|T1599.001]] | Network Address Translation Traversal | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | Ensure that cloud accounts, particularly privileged accounts, have complex, unique passwords across all systems on the network. Passwords and access keys should be rotated regularly. This limits the amount of time credentials can be used to access resources if a credential is compromised without your knowledge. Cloud service providers may track access key age to help audit and identify keys that may need to be rotated.[^1]  |
| [[Reversible Encryption\|T1556.005]] | Reversible Encryption | Ensure that `AllowReversiblePasswordEncryption` property is set to disabled unless there are application requirements.[^4]  |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | Do not store credentials within the Registry. |
| [[Pass the Ticket\|T1550.003]] | Pass the Ticket | Ensure that local administrator accounts have complex, unique passwords. |
| [[Private Keys\|T1552.004]] | Private Keys | Use strong passphrases for private keys to make cracking difficult. |
| [[Silver Ticket\|T1558.002]] | Silver Ticket | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire.[^2]  Also consider using Group Managed Service Accounts or another third party product such as password vaulting.[^2]  |
| [[Network Boundary Bridging\|T1599]] | Network Boundary Bridging | Refer to NIST guidelines when creating password policies. [^3]  |
| [[NTDS\|T1003.003]] | NTDS | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire.[^2]  Also consider using Group Managed Service Accounts or another third party product such as password vaulting.[^2]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment.[^6]  When possible, applications that use SSH keys should be updated periodically and properly secured.<br><br>Policies should minimize (if not eliminate) reuse of passwords between different user accounts, especially employees using the same credentials for personal accounts that may not be defended by enterprise security resources. |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Use strong passphrases for private keys to make cracking difficult. Do not store credentials within the Registry. Establish an organizational policy that prohibits password storage in files. |
| [[Credential Stuffing\|T1110.004]] | Credential Stuffing | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Password Cracking\|T1110.002]] | Password Cracking | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Use Alternate Authentication Material\|T1550]] | Use Alternate Authentication Material | Set and enforce secure password policies for accounts. |
| [[Forced Authentication\|T1187]] | Forced Authentication | Use strong passwords to increase the difficulty of credential hashes from being cracked if they are obtained. |
| [[DCSync\|T1003.006]] | DCSync | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Ensure that `AllowReversiblePasswordEncryption` property is set to disabled unless there are application requirements.[^4]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[AS-REP Roasting\|T1558.004]] | AS-REP Roasting | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. Also consider using Group Managed Service Accounts or another third party product such as password vaulting. [^2]  |
| [[LSA Secrets\|T1003.004]] | LSA Secrets | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Verify that account credentials that may be used to access deployment systems are unique and not used throughout the enterprise network. |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Cached Domain Credentials\|T1003.005]] | Cached Domain Credentials | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Local Accounts\|T1078.003]] | Local Accounts | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Proc Filesystem\|T1003.007]] | Proc Filesystem | Ensure that root accounts have complex, unique passwords across all systems on the network. |
| [[／etc／passwd and ／etc／shadow\|T1003.008]] | ／etc／passwd and ／etc／shadow | Ensure that root accounts have complex, unique passwords across all systems on the network. |
| [[Default Accounts\|T1078.001]] | Default Accounts | Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment. [^6]  |
| [[Modify System Image\|T1601]] | Modify System Image | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Password Guessing\|T1110.001]] | Password Guessing | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Keychain\|T1555.001]] | Keychain | The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password. |
| [[SSH Hijacking\|T1563.001]] | SSH Hijacking | Ensure SSH key pairs have strong passwords and refrain from using key-store technologies such as ssh-agent unless they are properly protected. |
| [[Remote Service Session Hijacking\|T1563]] | Remote Service Session Hijacking | Set and enforce secure password policies for accounts. |
| [[Domain Accounts\|T1078.002]] | Domain Accounts | Implement and enforce strong password policies for domain accounts to ensure passwords are complex, unique, and regularly rotated. This reduces the likelihood of password guessing, credential stuffing, and other attack methods that rely on weak or static credentials. |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | The password for the user's login keychain can be changed from the user's login password. This increases the complexity for an adversary because they need to know an additional password.<br><br>Organizations may consider weighing the risk of storing credentials in password stores and web browsers. If system, software, or web browser credential disclosure is a significant concern, technical controls, policy, and user training may be used to prevent storage of credentials in improper locations. |
| [[Password Spraying\|T1110.003]] | Password Spraying | Refer to NIST guidelines when creating password policies. [^3]  |
| [[Steal or Forge Kerberos Tickets\|T1558]] | Steal or Forge Kerberos Tickets | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire.[^2]  Also consider using Group Managed Service Accounts or another third party product such as password vaulting.[^2]  |
| [[Brute Force\|T1110]] | Brute Force | Refer to NIST guidelines when creating password policies.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | Organizations may consider weighing the risk of storing credentials in web browsers. If web browser credential disclosure is a significant concern, technical controls, policy, and user training may be used to prevent storage of credentials in web browsers. |
| [[Downgrade System Image\|T1601.002]] | Downgrade System Image | Refer to NIST guidelines when creating password policies.  [^3]  |
| [[Password Policy Discovery\|T1201]] | Password Policy Discovery | Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory (`C:\Windows\System32\` by default) of a domain controller and/or local computer with a corresponding entry in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages`. [^5]  |
| [[Remote Services\|T1021]] | Remote Services | Do not reuse local administrator account passwords across systems. Ensure password complexity and uniqueness such that the passwords cannot be cracked or guessed. |
| [[Password Managers\|T1555.005]] | Password Managers | Refer to NIST guidelines when creating password policies for master passwords.[^3]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | Do not reuse local administrator account passwords across systems. Ensure password complexity and uniqueness such that the passwords cannot be cracked or guessed. |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | Ensure that local administrator accounts have complex, unique passwords across all systems on the network. |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | Establish an organizational policy that prohibits password storage in files. |
| [[Patch System Image\|T1601.001]] | Patch System Image | Refer to NIST guidelines when creating password policies.  [^3]  |


## References

[^1]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^2]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^3]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^4]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^5]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^6]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


