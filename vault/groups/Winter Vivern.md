---
aliases: 
    - Winter Vivern
    - TA473
    - UAC-0114
mitre-attack: https://attack.mitre.org/groups/G1035
---

## G1035

Winter Vivern is a group linked to Russian and Belorussian interests active since at least 2020 targeting various European government and NGO entities, along with sporadic targeting of Indian and US victims. The group leverages a combination of document-based phishing activity and server-side exploitation for initial access, leveraging adversary-controlled and -created infrastructure for follow-on command and control.[^7] [^6] [^2] [^1] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Winter Vivern](https://attack.mitre.org/groups/G1035) used XLM 4.0 macros for initial code execution for malicious document files.[^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Winter Vivern](https://attack.mitre.org/groups/G1035) uses HTTP and HTTPS protocols for exfiltration and command and control activity.[^6] [^2]  |
| [[Web Portal Capture\|T1056.003]] | Web Portal Capture | [Winter Vivern](https://attack.mitre.org/groups/G1035) registered and hosted domains to allow for creation of web pages mimicking legitimate government email logon sites to collect logon information.[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) PowerShell scripts execute `whoami` to identify the executing user.[^6]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Winter Vivern](https://attack.mitre.org/groups/G1035) used adversary-owned and -controlled servers to host web vulnerability scanning applications.[^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript to exploit targets when exploiting Roundcube Webmail servers.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Winter Vivern](https://attack.mitre.org/groups/G1035) leverages malicious attachments delivered via email for initial access activity.[^7] [^6] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Winter Vivern](https://attack.mitre.org/groups/G1035) has distributed malicious scripts and executables mimicking virus scanners.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered PowerShell scripts capable of taking screenshots of victim machines.[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Winter Vivern](https://attack.mitre.org/groups/G1035) created dedicated web pages mimicking legitimate government websites to deliver malicious fake anti-virus software.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered exploit payloads via base64-encoded payloads in malicious email messages.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Winter Vivern](https://attack.mitre.org/groups/G1035) executed PowerShell scripts to create scheduled tasks to retrieve remotely-hosted payloads.[^7]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Winter Vivern](https://attack.mitre.org/groups/G1035) has exploited known and zero-day vulnerabilities in software usch as Roundcube Webmail servers and the "Follina" vulnerability.[^1] [^4]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [Winter Vivern](https://attack.mitre.org/groups/G1035) has used remotely-hosted instances of the Acunetix vulnerability scanner.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Winter Vivern](https://attack.mitre.org/groups/G1035) executed PowerShell scripts that would subsequently attempt to establish persistence by creating scheduled tasks objects to periodically retrieve and execute remotely-hosted payloads.[^7]  |
| [[Web Services\|T1584.006]] | Web Services | [Winter Vivern](https://attack.mitre.org/groups/G1035) has used compromised WordPress sites to host malicious payloads for download.[^6]  |
| [[Masquerading\|T1036]] | Masquerading | [Winter Vivern](https://attack.mitre.org/groups/G1035) created specially-crafted documents mimicking legitimate government or similar documents during phishing campaigns.[^6]  |
| [[Domains\|T1583.001]] | Domains | [Winter Vivern](https://attack.mitre.org/groups/G1035) registered domains mimicking other entities throughout various campaigns.[^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) script execution includes basic victim information gathering steps which are then transmitted to command and control servers.[^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Winter Vivern](https://attack.mitre.org/groups/G1035) distributed Windows batch scripts disguised as virus scanners to prompt download of malicious payloads using built-in system tools.[^6] [^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Winter Vivern](https://attack.mitre.org/groups/G1035) has mimicked legitimate government-related domains to deliver malicious webpages containing links to documents or other content for user execution.[^6] [^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript payloads capable of listing folders and emails in exploited email servers.[^1]  |
| [[Local Email Collection\|T1114.001]] | Local Email Collection | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript payloads capable of exfiltrating email messages from exploited email servers.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Winter Vivern](https://attack.mitre.org/groups/G1035) passed execution from document macros to PowerShell scripts during initial access operations.[^7]  [Winter Vivern](https://attack.mitre.org/groups/G1035) used batch scripts that called PowerShell commands as part of initial access and installation operations.[^2]  |




## References

[^1]: [ESET WinterVivern 2023](https://www.welivesecurity.com/en/eset-research/winter-vivern-exploits-zero-day-vulnerability-roundcube-webmail-servers/)


[^2]: [CERT-UA WinterVivern 2023](https://cert.gov.ua/article/3761104)


[^3]: UAC-0114


[^4]: [Proofpoint WinterVivern 2023](https://www.proofpoint.com/us/blog/threat-insight/exploitation-dish-best-served-cold-winter-vivern-uses-known-zimbra-vulnerability)


[^5]: TA473


[^6]: [SentinelOne WinterVivern 2023](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)


[^7]: [DomainTools WinterVivern 2021](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/)


