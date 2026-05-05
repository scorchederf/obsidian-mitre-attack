---
aliases: 
    - T1602
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/network_devices
mitre-attack: kb/mitre/attack/techniques/T1602-Data_from_Configuration_Repository
tactic: 
     - Collection
platforms:
     - Network Devices
permissions required:
     - none
---

## Description

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.<br><br>Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.[^4] [^3] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Segregate SNMP traffic on a separate management network.[^3]  |
| [[kb/mitre/attack/mitigations/M1031-Network_Intrusion_Prevention\|M1031]] | Network Intrusion Prevention | Configure intrusion prevention devices to detect SNMP queries and commands from unauthorized sources.[^4]  |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Apply extended ACLs to block unauthorized protocols outside the trusted network.[^3]  |
| [[kb/mitre/attack/mitigations/M1041-Encrypt_Sensitive_Information\|M1041]] | Encrypt Sensitive Information | Configure SNMPv3 to use the highest level of security (authPriv) available.[^3]  |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Keep system images and software updated and migrate to SNMPv3.[^1]  |
| [[kb/mitre/attack/mitigations/M1054-Software_Configuration\|M1054]] | Software Configuration | Allowlist MIB objects and implement SNMP views.[^5]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1602.001-SNMP_MIB_Dump\|T1602.001]] | SNMP (MIB Dump) |
| [[kb/mitre/attack/techniques/T1602.002-Network_Device_Configuration_Dump\|T1602.002]] | Network Device Configuration Dump |




> [!info]- References
> [^1]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)

> [^2]: [Cisco Advisory SNMP v3 Authentication Vulnerabilities](https://tools.cisco.com/security/center/content/CiscoAppliedMitigationBulletin/cisco-amb-20080610-SNMPv3)

> [^3]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)

> [^4]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^5]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


