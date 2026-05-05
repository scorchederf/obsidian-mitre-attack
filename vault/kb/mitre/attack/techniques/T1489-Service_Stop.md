---
aliases: 
    - T1489
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1489-Service_Stop
tactic: 
     - Impact
platforms:
     - ESXi - IaaS - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.[^3] [^7]  <br><br>Adversaries may accomplish this by disabling individual services of high importance to an organization, such as `MSExchangeIS`, which will make Exchange content inaccessible.[^7]  In some cases, adversaries may stop or disable many or all services to render systems unusable.[^3]  Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [[kb/mitre/attack/techniques/T1485-Data_Destruction\|Data Destruction]] or [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]] on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.[^2] [^6] <br><br>Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.[^5] [^1] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions. |
| [[kb/mitre/attack/mitigations/M1060-Out-of-Band_Communications_Channel\|M1060]] | Out-of-Band Communications Channel | Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident.[^4]  |






> [!info]- References
> [^1]: [AWS DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

> [^2]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)

> [^3]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)

> [^4]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)

> [^5]: [Datadog Security Labs Cloud Persistence 2025](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/)

> [^6]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

> [^7]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


