---
aliases: 
    - T1546
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1546-Event_Triggered_Execution
tactic: 
     - Privilege Escalation - Persistence
platforms:
     - Linux - macOS - Windows - SaaS - IaaS - Office Suite
permissions required:
     - none
---

## Description

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.[^3] [^5] [^2] <br><br>Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.[^1] [^6] [^7] <br><br>Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges. 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-Pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-Pacu\|Pacu]] can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.[^4]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Perform regular software updates to mitigate exploitation risk. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1546.001-Change_Default_File_Association\|T1546.001]] | Change Default File Association |
| [[kb/mitre/attack/techniques/T1546.002-Screensaver\|T1546.002]] | Screensaver |
| [[kb/mitre/attack/techniques/T1546.003-Windows_Management_Instrumentation_Event_Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription |
| [[kb/mitre/attack/techniques/T1546.004-Unix_Shell_Configuration_Modification\|T1546.004]] | Unix Shell Configuration Modification |
| [[kb/mitre/attack/techniques/T1546.005-Trap\|T1546.005]] | Trap |
| [[kb/mitre/attack/techniques/T1546.006-LC_LOAD_DYLIB_Addition\|T1546.006]] | LC_LOAD_DYLIB Addition |
| [[kb/mitre/attack/techniques/T1546.007-Netsh_Helper_DLL\|T1546.007]] | Netsh Helper DLL |
| [[kb/mitre/attack/techniques/T1546.008-Accessibility_Features\|T1546.008]] | Accessibility Features |
| [[kb/mitre/attack/techniques/T1546.009-AppCert_DLLs\|T1546.009]] | AppCert DLLs |
| [[kb/mitre/attack/techniques/T1546.010-AppInit_DLLs\|T1546.010]] | AppInit DLLs |
| [[kb/mitre/attack/techniques/T1546.011-Application_Shimming\|T1546.011]] | Application Shimming |
| [[kb/mitre/attack/techniques/T1546.012-Image_File_Execution_Options_Injection\|T1546.012]] | Image File Execution Options Injection |
| [[kb/mitre/attack/techniques/T1546.013-PowerShell_Profile\|T1546.013]] | PowerShell Profile |
| [[kb/mitre/attack/techniques/T1546.014-Emond\|T1546.014]] | Emond |
| [[kb/mitre/attack/techniques/T1546.015-Component_Object_Model_Hijacking\|T1546.015]] | Component Object Model Hijacking |
| [[kb/mitre/attack/techniques/T1546.016-Installer_Packages\|T1546.016]] | Installer Packages |
| [[kb/mitre/attack/techniques/T1546.017-Udev_Rules\|T1546.017]] | Udev Rules |
| [[kb/mitre/attack/techniques/T1546.018-Python_Startup_Hooks\|T1546.018]] | Python Startup Hooks |




> [!info]- References
> [^1]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)

> [^2]: [Microsoft DART Case Report 001](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)

> [^3]: [Backdooring an AWS account](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)

> [^4]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)

> [^5]: [Varonis Power Automate Data Exfiltration](https://www.varonis.com/blog/power-automate-data-exfiltration)

> [^6]: [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)

> [^7]: [amnesia malware](https://researchcenter.paloaltonetworks.com/2017/04/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/)


