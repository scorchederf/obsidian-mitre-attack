---
aliases: 
    - Storm-0501
mitre-attack: https://attack.mitre.org/groups/G1053
---

## G1053

[Storm-0501](https://attack.mitre.org/groups/G1053) is a financially motivated cyber criminal group that uses commodity and open-source tools to conduct ransomware operations. [Storm-0501](https://attack.mitre.org/groups/G1053) has been active since 2021 and has previously been affiliated with Sabbath Ransomware and other Ransomware-as-a-Service (RaaS) variants such as Hive, [BlackCat](https://attack.mitre.org/software/S1068), Hunters International, [LockBit 3.0](https://attack.mitre.org/software/S1202), and [Embargo](https://attack.mitre.org/software/S1247) ransomware.[^4] [^1] [^2] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Storm-0501](https://attack.mitre.org/groups/G1053) has used legitimate remote monitoring and management (RMM) tools including AnyDesk, NinjaOne, and Level.io.[^1]  |
| [[Transfer Data to Cloud Account\|T1537]] | Transfer Data to Cloud Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has copied data from the victims environment to their own infrastructure leveraging AzCopy CLI.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has deleted snapshots, restore points, storage accounts, and backup services to prevent remediation and restoration.[^2]  [Storm-0501](https://attack.mitre.org/groups/G1053) has also impacted Azure resources through the targeting of `Microsoft.Compute/snapshots/delete`,<br>`Microsoft.Compute/restorePointCollections/delete`,<br>`Microsoft.Storage/storageAccounts/delete`, and <br>`Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/delete`.[^2]  |
| [[Group Policy Modification\|T1484.001]] | Group Policy Modification | [Storm-0501](https://attack.mitre.org/groups/G1053) distributed Group Policy Objects to tamper with security products.[^1]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [Storm-0501](https://attack.mitre.org/groups/G1053) had modified Azure Storage account resources through the `Microsoft.Storage/storageAccounts/write` operation to expose non-remotely accessible accounts for data exfiltration.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged PowerShell to execute commands and scripts.[^1] [^2]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Storm-0501](https://attack.mitre.org/groups/G1053) has destroyed data and backup files.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Storm-0501](https://attack.mitre.org/groups/G1053) had used a scheduled task named “SysUpdate” that was registered via GPO on devices in the network to distribute the [Embargo](https://attack.mitre.org/software/S1247) ransomware.[^1]  |
| [[Cloud Account\|T1087.004]] | Cloud Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has conducted enumeration of users, roles, and resources within victim Azure tenants using the tool Azurehound.[^2]  |
| [[DCSync\|T1003.006]] | DCSync | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized DCSync to extract credentials from victims.[^2]  |
| [[Cloud Service Discovery\|T1526]] | Cloud Service Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has discovered the victim environment’s protections to include Azure policies, resource locks, and Azure Storage immutability policies.[^2]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Storm-0501](https://attack.mitre.org/groups/G1053) has exfiltrated stolen data to the MEGA file sharing site.[^3]  [Storm-0501](https://attack.mitre.org/groups/G1053) has also utilized [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate data from victim environments to cloud storage such as MegaSync.[^1]  [Storm-0501](https://attack.mitre.org/groups/G1053) has exfiltrated data to their own infrastructure utilizing AzCopy Command-Line tool (CLI).[^2]  |
| [[Cloud API\|T1059.009]] | Cloud API | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged Cloud CLI to execute commands and exfiltrate data from compromised environments.[^2]  |
| [[Cloud Services\|T1021.007]] | Cloud Services | [Storm-0501](https://attack.mitre.org/groups/G1053) has used compromised Entra Connect Sync Server to move laterally within the victim environment.[^2]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized the post-exploitation tool known as Evil-WinRM that uses PowerShell over Windows Remote Management (WinRM) for remote code execution.[^2]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Storm-0501](https://attack.mitre.org/groups/G1053) has exploited N-day vulnerabilities associated with public facing services to gain initial access to victim environments to include Zoho ManageEngine (CVE-2022-47966), Citrix NetScaler “Citrix Bleed” (CVE-2023-4966), and Adobe ColdFusion 2016 (CVE-2023-29300 or CVE-2023-38203).[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has discovered running processes through `tasklist.exe`.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has detected endpoint security solutions using `sc query sense` and `sc query windefend`.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Storm-0501](https://attack.mitre.org/groups/G1053) has encrypted files in victim environments using ransomware as a service (RaaS) including Sabbath, Hive, [BlackCat](https://attack.mitre.org/software/S1068), Hunters International, [LockBit 3.0](https://attack.mitre.org/software/S1202) and [Embargo](https://attack.mitre.org/software/S1247) ransomware.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Storm-0501](https://attack.mitre.org/groups/G1053) has engaged in double-extortion ransomware, exfiltrating data and directly contacting victims when the primary organization refuses to pay along with posting data on their data leak sites.[^4] [^2] [^3]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged compromised accounts to access Microsoft Entra Connect, which was used to synchronize on-premises identities and Microsoft Entra identities, allowing users to sign into both environments with the same password.[^1]  [Storm-0501](https://attack.mitre.org/groups/G1053) has also used the victim Global Administrator account that lacked any registered MFA method to access victim cloud environments.[^2]  [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged Storage Account Access Keys within the victim environment.[^2]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Storm-0501](https://attack.mitre.org/groups/G1053) has launched [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacon files using regsvr32.exe.[^1]  |
| [[Cloud Secrets Management Stores\|T1555.006]] | Cloud Secrets Management Stores | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized Azure Key Vault to store the encryption key using the operation `Microsoft.KeyVault/Vaults/write`.[^2]  |
| [[Password Managers\|T1555.005]] | Password Managers | [Storm-0501](https://attack.mitre.org/groups/G1053) has stolen credentials contained in the password manager Keepass by utilizing Find-KeePassConfig.ps1.[^1]  |
| [[Trust Modification\|T1484.002]] | Trust Modification | [Storm-0501](https://attack.mitre.org/groups/G1053) created a new federated domain within the victim Microsoft Entra tenant using Global Administrator level access to establish a persistent backdoor for later use.[^1] [^2]  |
| [[Cloud Infrastructure Discovery\|T1580]] | Cloud Infrastructure Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has enumerated compromised cloud environments to identify critical assets, data stores, and back resources.[^2]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has used Windows native utility [Nltest](https://attack.mitre.org/software/S0359) `nltest.exe` for discovery.[^1]  |
| [[Delete Cloud Instance\|T1578.003]] | Delete Cloud Instance | [Storm-0501](https://attack.mitre.org/groups/G1053) has conducted mass deletion of cloud data stores and resources from Azure subscriptions.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged native Windows tools and commands such as `systeminfo` and open-source tools including OSQuery and ossec-win32 to query details about the endpoint.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Storm-0501](https://attack.mitre.org/groups/G1053) has used Themida to pack [Cobalt Strike](https://attack.mitre.org/software/S0154) payloads.[^3]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Storm-0501](https://attack.mitre.org/groups/G1053) has identified system language codes on a compromised host to determine if the victim falls under a non-supported language code that is prohibited for targeting, including victims associated with Russia and other Commonwealth of Independent States (CIS) that may draw attention of law enforcement in countries where the ransomware operator or affiliates may reside/operate from.[^4] [^3]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged the Azure Owner role to access and steal the Storage Account Access keys using the `Microsoft.Storage/storageAccounts/listkeys/action` operation.[^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized [Rclone](https://attack.mitre.org/software/S1040) masqueraded as svhost.exe and scvhost.exe.[^1]  |
| [[Additional Cloud Roles\|T1098.003]] | Additional Cloud Roles | [Storm-0501](https://attack.mitre.org/groups/G1053) has elevated their access to Azure resources using `Microsoft.Authorization/elevateAccess/action` and `Microsoft.Authorization/roleAssignments/write` operations to gain User Access Administrator and Owner Azure roles over the victims’ Azure subscriptions.[^2]  |
| [[Domain Account\|T1087.002]] | Domain Account | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized an obfuscated version of the Active Directory reconnaissance tool ADRecon.ps1 (obfs.ps1 or recon.ps1) to discover domain accounts.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Storm-0501](https://attack.mitre.org/groups/G1053) has launched [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacon files with rundll32.exe.[^1]  |
| [[Digital Certificates\|T1587.003]] | Digital Certificates | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized their own self-signed TLS certificate “Microsoft IT TLS CA 5” with their infrastructure.[^3]  |
| [[Vulnerabilities\|T1588.006]] | Vulnerabilities | [Storm-0501](https://attack.mitre.org/groups/G1053) has obtained capabilities to exploit N-day vulnerabilities associated with public facing services to gain initial access to victim environments to include Zoho ManageEngine (CVE-2022-47966), Citrix NetScaler “Citrix Bleed” (CVE-2023-4966), and Adobe ColdFusion 2016 (CVE-2023-29300 or CVE-2023-38203).[^1]  |
| [[Conditional Access Policies\|T1556.009]] | Conditional Access Policies | [Storm-0501](https://attack.mitre.org/groups/G1053) has registered their own MFA method, and leveraged a victim hybrid joined server to circumvent Conditional Access Policies.[^2]  |
| [[OS Credential Dumping\|T1003]] | OS Credential Dumping | [Storm-0501](https://attack.mitre.org/groups/G1053) has used the SecretsDump module within [Impacket](https://attack.mitre.org/software/S0357) can perform credential dumping to obtain account and password information.[^1]  |
| [[Brute Force\|T1110]] | Brute Force | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged brute force attacks to obtain credentials.[^1]  |
| [[Additional Cloud Credentials\|T1098.001]] | Additional Cloud Credentials | [Storm-0501](https://attack.mitre.org/groups/G1053) has reset the password of identified administrator accounts that lack MFA and registered their own MFA method.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Net\|S0039]] | Net | [Storm-0501](https://attack.mitre.org/groups/G1053) has used the [Net](https://attack.mitre.org/software/S0039) utility on the Windows operating system.[^1] [^2]  |
| [[Impacket\|S0357]] | Impacket | [Storm-0501](https://attack.mitre.org/groups/G1053) has used [Impacket](https://attack.mitre.org/software/S0357) to extract credentials over the network and from victim devices.[^1]  |
| [[AADInternals\|S0677]] | AADInternals | [Storm-0501](https://attack.mitre.org/groups/G1053) used the PowerShell module [AADInternals](https://attack.mitre.org/software/S0677) to create a back door within the victim tenant, thus allowing for the impersonation of any user in the organization and bypassing MFA to sign in to any application to include Office 365.[^1]  |
| [[Tasklist\|S0057]] | Tasklist | [Storm-0501](https://attack.mitre.org/groups/G1053) discovered running processes through `tasklist.exe`.[^1]  |
| [[Rclone\|S1040]] | Rclone | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized [Rclone](https://attack.mitre.org/software/S1040) for data exfiltration.[^1]  |
| [[Nltest\|S0359]] | Nltest | [Storm-0501](https://attack.mitre.org/groups/G1053) has used Windows native utility [Nltest](https://attack.mitre.org/software/S0359), e.g. `nltest.exe`, for discovery.[^1]  |
| [[Embargo\|S1247]] | Embargo | [Storm-0501](https://attack.mitre.org/groups/G1053) has used [Embargo](https://attack.mitre.org/software/S1247) for ransomware activities.[^1] [^2]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Storm-0501](https://attack.mitre.org/groups/G1053) has utilized [Cobalt Strike](https://attack.mitre.org/software/S0154) for C2 communications and used a unique “license_id” of “666.”[^1]  |



## References

[^1]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^2]: [Microsoft Storm-0501 Embargo Ransomware August 2025](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)


[^3]: [Google Mandiant Storm-0501 Sabbath Ransomware November 2021](https://cloud.google.com/blog/topics/threat-intelligence/sabbath-ransomware-affiliate/)


[^4]: [Avertium Storm-0501 Sabbath Ransomware Arcane January 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-sabbath-ransomware-gang)


