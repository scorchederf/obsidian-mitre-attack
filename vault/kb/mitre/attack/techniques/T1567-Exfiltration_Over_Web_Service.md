---
aliases: 
    - T1567
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1567-Exfiltration_Over_Web_Service
tactic: 
     - Exfiltration
platforms:
     - ESXi - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.<br><br>Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] has been used by threat actors to configure servers for data exfiltration.[^1]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1021-Restrict_Web-Based_Content\|M1021]] | Restrict Web-Based Content | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1567.001-Exfiltration_to_Code_Repository\|T1567.001]] | Exfiltration to Code Repository |
| [[kb/mitre/attack/techniques/T1567.002-Exfiltration_to_Cloud_Storage\|T1567.002]] | Exfiltration to Cloud Storage |
| [[kb/mitre/attack/techniques/T1567.003-Exfiltration_to_Text_Storage_Sites\|T1567.003]] | Exfiltration to Text Storage Sites |
| [[kb/mitre/attack/techniques/T1567.004-Exfiltration_Over_Webhook\|T1567.004]] | Exfiltration Over Webhook |




> [!info]- References
> [^1]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)


