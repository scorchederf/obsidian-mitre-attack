---
aliases: 
    - T1195
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1195-Supply_Chain_Compromise
tactic: 
     - Initial Access
platforms:
     - Linux - Windows - macOS - SaaS
permissions required:
     - none
---

## Description

Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.<br><br>Supply chain compromise can take place at any stage of the supply chain including:<br><br>* Manipulation of development tools<br>* Manipulation of a development environment<br>* Manipulation of source code repositories (public or private)<br>* Manipulation of source code in open-source dependencies<br>* Manipulation of software update/distribution mechanisms<br>* Compromised/infected system images (removable media infected at the factory)[^6] [^3]  <br>* Replacement of legitimate software with modified versions<br>* Sales of modified/counterfeit products to legitimate distributors<br>* Shipment interdiction<br><br>While supply chain compromise can impact any component of hardware or software, adversaries looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels.[^4] [^8] [^9]  Adversaries may limit targeting to a desired victim set or distribute malicious software to a broad set of consumers but only follow up with specific victims.[^5] [^4] [^9]  Popular open-source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency.[^2] <br><br>In some cases, adversaries may conduct “second-order” supply chain compromises by leveraging the access gained from an initial supply chain compromise to further compromise a software component.[^10]  This may allow the threat actor to spread to even more victims.  




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | Application developers should be cautious when selecting third-party libraries to integrate into their application. Additionally, where possible, developers should lock software dependencies to specific versions rather than pulling the latest version on build.[^7]  |
| [[kb/mitre/attack/mitigations/M1016-Vulnerability_Scanning\|M1016]] | Vulnerability Scanning | Continuous monitoring of vulnerability sources and the use of automatic and manual code review tools should also be implemented as well.[^1]  |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Implement robust user account management practices to limit permissions associated with software execution. Ensure that software runs with the lowest necessary privileges, avoiding the use of root or administrator accounts when possible. By restricting permissions, you can minimize the risk of propagation and unauthorized actions in the event of a supply chain compromise, reducing the attack surface for adversaries to exploit within compromised systems. |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones.[^7]  |
| [[kb/mitre/attack/mitigations/M1046-Boot_Integrity\|M1046]] | Boot Integrity | Use secure methods to boot a system and verify the integrity of the operating system and loading mechanisms. |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1195.001-Compromise_Software_Dependencies_and_Development_Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools |
| [[kb/mitre/attack/techniques/T1195.002-Compromise_Software_Supply_Chain\|T1195.002]] | Compromise Software Supply Chain |
| [[kb/mitre/attack/techniques/T1195.003-Compromise_Hardware_Supply_Chain\|T1195.003]] | Compromise Hardware Supply Chain |




> [!info]- References
> [^1]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)

> [^2]: [Trendmicro NPM Compromise](https://www.trendmicro.com/vinfo/dk/security/news/cybercrime-and-digital-threats/hacker-infects-node-js-package-to-steal-from-bitcoin-wallets)

> [^3]: [Schneider Electric USB Malware](https://www.se.com/us/en/download/document/SESN-2018-236-01/)

> [^4]: [Avast CCleaner3 2018](https://blog.avast.com/new-investigations-in-ccleaner-incident-point-to-a-possible-third-stage-that-had-keylogger-capacities)

> [^5]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)

> [^6]: [IBM Storwize](https://www-01.ibm.com/support/docview.wss?uid=ssg1S1010146&myns=s028&mynp=OCSTHGUJ&mynp=OCSTLM5A&mynp=OCSTLM6B&mynp=OCHW206&mync=E&cm_sp=s028-_-OCSTHGUJ-OCSTLM5A-OCSTLM6B-OCHW206-_-E)

> [^7]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)

> [^8]: [Microsoft Dofoil 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/07/behavior-monitoring-combined-with-machine-learning-spoils-a-massive-dofoil-coin-mining-campaign/)

> [^9]: [Command Five SK 2011](https://web.archive.org/web/20160309235002/https://www.commandfive.com/papers/C5_APT_SKHack.pdf)

> [^10]: [Krebs 3cx overview 2023](https://krebsonsecurity.com/2023/04/3cx-breach-was-a-double-supply-chain-compromise/)


