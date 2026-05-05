---
aliases: 
    - T1119
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1119-Automated_Collection
tactic: 
     - Collection
platforms:
     - IaaS - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]] to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. <br><br>In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.[^1]  <br><br>This functionality could also be built into remote access tools. <br><br>This technique may incorporate use of other techniques such as [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|File and Directory Discovery]] and [[kb/mitre/attack/techniques/T1570-Lateral_Tool_Transfer\|Lateral Tool Transfer]] to identify and move files, as well as [[kb/mitre/attack/techniques/T1538-Cloud_Service_Dashboard\|Cloud Service Dashboard]] and [[kb/mitre/attack/techniques/T1619-Cloud_Storage_Object_Discovery\|Cloud Storage Object Discovery]] to identify resources in cloud environments.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can automatically gather the username, domain name, machine name, and other information from a compromised system.[^2]  |
| [[kb/mitre/attack/software/S0378-PoshC2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-PoshC2\|PoshC2]] contains a module for recursively parsing through files and directories to gather valid credit card numbers.[^8]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.[^7]  |
| [[kb/mitre/attack/software/S0684-ROADTools\|S0684]] | ROADTools | [[kb/mitre/attack/software/S0684-ROADTools\|ROADTools]] automatically gathers data from Azure AD environments using the Azure Graph API.[^4]  |
| [[kb/mitre/attack/software/S0699-Mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-Mythic\|Mythic]] supports scripting of file downloads from agents.[^5] 	 |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.[^6]  |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] collection is automatically recorded to a specified file on the victim machine.[^3]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1029-Remote_Data_Storage\|M1029]] | Remote Data Storage | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. Strong passwords should be used on certain encrypted documents that use them to prevent offline cracking through [[kb/mitre/attack/techniques/T1110-Brute_Force\|Brute Force]] techniques. |






> [!info]- References
> [^1]: [Mandiant UNC3944 SMS Phishing 2023](https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware)

> [^2]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^3]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)

> [^4]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)

> [^5]: [Mythc Documentation](https://docs.mythic-c2.net/)

> [^6]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)

> [^7]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^8]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


