---
aliases: 
    - T1592
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1592-Gather_Victim_Host_Information
tactic: 
     - Reconnaissance
platforms:
     - PRE
permissions required:
     - none
---

## Description

Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.).<br><br>Adversaries may gather this information in various ways, such as direct collection actions via [[kb/mitre/attack/techniques/T1595-Active_Scanning\|Active Scanning]] or [[kb/mitre/attack/techniques/T1598-Phishing_for_Information\|Phishing for Information]]. Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.[^3]  Information about hosts may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1593.001-Social_Media\|Social Media]] or [[kb/mitre/attack/techniques/T1594-Search_Victim-Owned_Websites\|Search Victim-Owned Websites]]). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1593-Search_Open_Websites_Domains\|Search Open Websites/Domains]] or [[kb/mitre/attack/techniques/T1596-Search_Open_Technical_Databases\|Search Open Technical Databases]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1587-Develop_Capabilities\|Develop Capabilities]] or [[kb/mitre/attack/techniques/T1588-Obtain_Capabilities\|Obtain Capabilities]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1195-Supply_Chain_Compromise\|Supply Chain Compromise]] or [[kb/mitre/attack/techniques/T1133-External_Remote_Services\|External Remote Services]]).<br><br>Adversaries may also gather victim host information via User-Agent HTTP headers, which are sent to a server to identify the application, operating system, vendor, and/or version of the requesting user agent. This can be used to inform the adversary’s follow-on action. For example, adversaries may check user agents for the requesting operating system, then only serve malware for target operating systems while ignoring others.[^2] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-Pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1592.001-Hardware\|T1592.001]] | Hardware |
| [[kb/mitre/attack/techniques/T1592.002-Software\|T1592.002]] | Software |
| [[kb/mitre/attack/techniques/T1592.003-Firmware\|T1592.003]] | Firmware |
| [[kb/mitre/attack/techniques/T1592.004-Client_Configurations\|T1592.004]] | Client Configurations |




> [!info]- References
> [^1]: [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)

> [^2]: [TrellixQakbot](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)

> [^3]: [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)


