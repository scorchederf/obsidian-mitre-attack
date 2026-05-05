---
aliases: 
    - T1657
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/impact
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1657-Financial_Theft
tactic: 
     - Impact
platforms:
     - Linux - macOS - Office Suite - SaaS - Windows
permissions required:
     - none
---

## Description

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,[^3]  business email compromise (BEC) and fraud,[^8]  "pig butchering,"[^6]  bank hacking,[^9]  and exploiting cryptocurrency networks.[^12]  <br><br>Adversaries may [[kb/mitre/attack/techniques/T1586-Compromise_Accounts\|Compromise Accounts]] to conduct unauthorized transfers of funds.[^11]  In the case of business email compromise or email fraud, an adversary may utilize [[kb/mitre/attack/techniques/T1684.001-Impersonation\|Impersonation]] of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary.[^8]  This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.[^2] <br><br>Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]] [^1]  and [[kb/mitre/attack/tactics/TA0010-Exfiltration\|Exfiltration]] of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary.[^10]  Adversaries may use dedicated leak sites to distribute victim data.[^7] <br><br>Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as [[kb/mitre/attack/techniques/T1485-Data_Destruction\|Data Destruction]] and business disruption.[^5] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train and encourage users to identify social engineering techniques used to enable financial theft. Also consider training users on procedures to prevent and respond to swatting and doxing, acts increasingly deployed by financially motivated groups to further coerce victims into satisfying ransom/extortion demands.[^13] [^4]  |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit access/authority to execute sensitive transactions, and switch to systems and procedures designed to authenticate/approve payments and purchase requests outside of insecure communication lines such as email. |






> [!info]- References
> [^1]: [NYT-Colonial](https://www.nytimes.com/2021/05/13/technology/colonial-pipeline-ransom.html)

> [^2]: [VEC](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.)

> [^3]: [FBI-ransomware](https://www.cisa.gov/sites/default/files/Ransomware_Trifold_e-version.pdf)

> [^4]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)

> [^5]: [AP-NotPetya](https://apnews.com/article/russia-ukraine-technology-business-europe-hacking-ce7a8aca506742ab8e8873e7f9f229c2)

> [^6]: [wired-pig butchering](https://www.wired.com/story/pig-butchering-fbi-ic3-2022-report/)

> [^7]: [Crowdstrike-leaks](https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/)

> [^8]: [FBI-BEC](https://www.fbi.gov/file-repository/fy-2022-fbi-congressional-report-business-email-compromise-and-real-estate-wire-fraud-111422.pdf/view)

> [^9]: [DOJ-DPRK Heist](https://www.justice.gov/usao-cdca/pr/3-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyber-attacks-and)

> [^10]: [Mandiant-leaks](https://www.mandiant.com/resources/blog/ransomware-extortion-ot-docs)

> [^11]: [Internet crime report 2022](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf)

> [^12]: [BBC-Ronin](https://www.bbc.com/news/technology-60933174)

> [^13]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


