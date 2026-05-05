---
aliases: 
    - M1041
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information
---

## Description

Protect sensitive information at rest, in transit, and during processing by using strong encryption algorithms. Encryption ensures the confidentiality and integrity of data, preventing unauthorized access or tampering. This mitigation can be implemented through the following measures:<br><br>Encrypt Data at Rest:<br><br>- Use Case: Use full-disk encryption or file-level encryption to secure sensitive data stored on devices.<br>- Implementation: Implement BitLocker for Windows systems or FileVault for macOS devices to encrypt hard drives.<br><br>Encrypt Data in Transit:<br><br>- Use Case: Use secure communication protocols (e.g., TLS, HTTPS) to encrypt sensitive data as it travels over networks.<br>- Implementation: Enable HTTPS for all web applications and configure mail servers to enforce STARTTLS for email encryption.<br><br>Encrypt Backups:<br><br>- Use Case: Ensure that backup data is encrypted both during storage and transfer to prevent unauthorized access.<br>- Implementation: Encrypt cloud backups using AES-256 before uploading them to Amazon S3 or Google Cloud.<br><br>Encrypt Application Secrets:<br><br>- Use Case: Store sensitive credentials, API keys, and configuration files in encrypted vaults.<br>- Implementation: Use HashiCorp Vault or AWS Secrets Manager to manage and encrypt secrets.<br><br>Database Encryption:<br><br>- Use Case: Enable Transparent Data Encryption (TDE) or column-level encryption in database management systems.<br>- Implementation: Use MySQL’s built-in encryption features to encrypt sensitive database fields such as social security numbers.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003-OS_Credential_Dumping\|T1003]] | OS Credential Dumping | Ensure Domain Controller backups are properly secured. |
| [[kb/mitre/attack/techniques/T1003.003-NTDS\|T1003.003]] | NTDS | Ensure Domain Controller backups are properly secured.[^2]  |
| [[kb/mitre/attack/techniques/T1020.001-Traffic_Duplication\|T1020.001]] | Traffic Duplication | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/techniques/T1040-Network_Sniffing\|T1040]] | Network Sniffing | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|T1070]] | Indicator Removal | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |
| [[kb/mitre/attack/techniques/T1114-Email_Collection\|T1114]] | Email Collection | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/techniques/T1114.001-Local_Email_Collection\|T1114.001]] | Local Email Collection | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/techniques/T1114.002-Remote_Email_Collection\|T1114.002]] | Remote Email Collection | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/techniques/T1114.003-Email_Forwarding_Rule\|T1114.003]] | Email Forwarding Rule | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. Strong passwords should be used on certain encrypted documents that use them to prevent offline cracking through [[kb/mitre/attack/techniques/T1110-Brute_Force\|Brute Force]] techniques. |
| [[kb/mitre/attack/techniques/T1213-Data_from_Information_Repositories\|T1213]] | Data from Information Repositories | Encrypt data stored at rest in databases.  |
| [[kb/mitre/attack/techniques/T1213.006-Databases\|T1213.006]] | Databases | Encrypt data stored at rest in databases. |
| [[kb/mitre/attack/techniques/T1530-Data_from_Cloud_Storage\|T1530]] | Data from Cloud Storage | Encrypt data stored at rest in cloud storage.[^4] [^3]  Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications.[^8]  |
| [[kb/mitre/attack/techniques/T1550.001-Application_Access_Token\|T1550.001]] | Application Access Token | File encryption should be enforced across email communications containing sensitive information that may be obtained through access to email services. |
| [[kb/mitre/attack/techniques/T1552-Unsecured_Credentials\|T1552]] | Unsecured Credentials | When possible, store keys on separate cryptographic hardware instead of on the local system.  |
| [[kb/mitre/attack/techniques/T1552.004-Private_Keys\|T1552.004]] | Private Keys | When possible, store keys on separate cryptographic hardware instead of on the local system. For example, on Windows systems use a TPM to secure keys and other sensitive credential material.[^5]  |
| [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/techniques/T1557.002-ARP_Cache_Poisoning\|T1557.002]] | ARP Cache Poisoning | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/techniques/T1558-Steal_or_Forge_Kerberos_Tickets\|T1558]] | Steal or Forge Kerberos Tickets | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.[^6]  |
| [[kb/mitre/attack/techniques/T1558.002-Silver_Ticket\|T1558.002]] | Silver Ticket | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.[^6]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.[^6]  |
| [[kb/mitre/attack/techniques/T1558.004-AS-REP_Roasting\|T1558.004]] | AS-REP Roasting | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.[^6]  |
| [[kb/mitre/attack/techniques/T1565-Data_Manipulation\|T1565]] | Data Manipulation | Consider encrypting important information to reduce an adversary’s ability to perform tailored data modifications. |
| [[kb/mitre/attack/techniques/T1565.001-Stored_Data_Manipulation\|T1565.001]] | Stored Data Manipulation | Consider encrypting important information to reduce an adversary’s ability to perform tailored data modifications. |
| [[kb/mitre/attack/techniques/T1565.002-Transmitted_Data_Manipulation\|T1565.002]] | Transmitted Data Manipulation | Encrypt all important data flows to reduce the impact of tailored modifications on data in transit. |
| [[kb/mitre/attack/techniques/T1602-Data_from_Configuration_Repository\|T1602]] | Data from Configuration Repository | Configure SNMPv3 to use the highest level of security (authPriv) available.[^7]  |
| [[kb/mitre/attack/techniques/T1602.001-SNMP_MIB_Dump\|T1602.001]] | SNMP (MIB Dump) | Configure SNMPv3 to use the highest level of security (authPriv) available.[^7]  |
| [[kb/mitre/attack/techniques/T1602.002-Network_Device_Configuration_Dump\|T1602.002]] | Network Device Configuration Dump | Configure SNMPv3 to use the highest level of security (authPriv) available.[^7]   |
| [[kb/mitre/attack/techniques/T1649-Steal_or_Forge_Authentication_Certificates\|T1649]] | Steal or Forge Authentication Certificates | Ensure certificates as well as associated private keys are appropriately secured. Consider utilizing additional hardware credential protections such as trusted platform modules (TPM) or hardware security modules (HSM). Enforce HTTPS and enable Extended Protection for<br>Authentication.[^1]  |
| [[kb/mitre/attack/techniques/T1659-Content_Injection\|T1659]] | Content Injection | Where possible, ensure that online traffic is appropriately encrypted through services such as trusted VPNs. |
| [[kb/mitre/attack/techniques/T1669-Wi-Fi_Networks\|T1669]] | Wi-Fi Networks | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure that web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/techniques/T1685.005-Clear_Windows_Event_Logs\|T1685.005]] | Clear Windows Event Logs | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |
| [[kb/mitre/attack/techniques/T1685.006-Clear_Linux_or_Mac_System_Logs\|T1685.006]] | Clear Linux or Mac System Logs | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |



> [!info]- References
> [^1]: [SpecterOps Certified Pre Owned](https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)

> [^2]: [Metcalf 2015](http://adsecurity.org/?p=1275)

> [^3]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)

> [^4]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)

> [^5]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)

> [^6]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)

> [^7]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)

> [^8]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


