---
aliases: 
    - APT-C-36
    - Blind Eagle
    - TAG-144
    - AguilaCiega
    - APT-Q-98
mitre-attack: https://attack.mitre.org/groups/G0099
---

## G0099

[APT-C-36](https://attack.mitre.org/groups/G0099) is a suspected South American threat group that has engaged in espionage and financially motivated operations since at least 2018. [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.[^4] [^10] [^6] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Domains\|T1583.001]] | Domains | [APT-C-36](https://attack.mitre.org/groups/G0099) has acquired domains to host malicious payloads.[^10] [^6] [^7] [^3] [^3] [^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT-C-36](https://attack.mitre.org/groups/G0099) has prompted victims to open attachments and to accept macros in order to execute the subsequent payload.[^4] [^3]  [APT-C-36](https://attack.mitre.org/groups/G0099) has also lured victims into opening malicious files hosted on Google Drive that triggered WebDAV requests to download malware.[^6] [^5]  |
| [[Written Content\|T1683.001]] | Written Content | [APT-C-36](https://attack.mitre.org/groups/G0099) has generated email content impersonating official notifications and documents that direct victims to execute malicious payloads.[^10]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [APT-C-36](https://attack.mitre.org/groups/G0099) has used junk characters to obfuscate malicious scripts.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [APT-C-36](https://attack.mitre.org/groups/G0099) has used WMI to execute PowerShell.[^5]  |
| [[JavaScript\|T1059.007]] | JavaScript |  [APT-C-36](https://attack.mitre.org/groups/G0099) has used a fileless attack chain composed of three JavaScript code snippets to execute subsequent payloads.[^5]  |
| [[Impersonation\|T1684.001]] | Impersonation | [APT-C-36](https://attack.mitre.org/groups/G0099) has impersonated banks including Banco Davivienda, Bancolombia, and BBVA as well as government institutions such as Colombia’s National Directorate of Taxes and Customs, Ministry of Foreign Affairs, and Office of the Attorney General.[^10] [^7] [^3] [^5]  |
| [[Malware\|T1588.001]] | Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has utilized well known malware including the Packer-as-a-Service HeartCrypt, PureCrypter, and open-source RATs such as [Remcos](https://attack.mitre.org/software/S0332).[^6] [^7] [^3]  |
| [[Botnet\|T1584.005]] | Botnet | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a botnet management interface to control large numbers of compromised hosts.[^7]  |
| [[Web Services\|T1583.006]] | Web Services | [APT-C-36](https://attack.mitre.org/groups/G0099) campaign architecture has included image hosting sites, Pastebin, Discord, GitHub, Google Drive, BitBucket, and Dropbox.[^10] [^6] [^3] [^5] <br> |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [APT-C-36](https://attack.mitre.org/groups/G0099) has disguised its scheduled tasks as those used by Google.[^4]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT-C-36](https://attack.mitre.org/groups/G0099) has used encoded and obfuscated files, images, and executables.[^10] <br> |
| [[Tool\|T1588.002]] | Tool | [APT-C-36](https://attack.mitre.org/groups/G0099) utilizes tools well known in crime communities and has obtained and used a modified variant of [Imminent Monitor](https://attack.mitre.org/software/S0434).[^4] [^6]  |
| [[Malware\|T1587.001]] | Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has customized existing malware with new capabilities including [njRAT](https://attack.mitre.org/software/S0385), [AsyncRAT](https://attack.mitre.org/software/S1087), LimeRAT, and BitRAT.[^10] <br> |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [APT-C-36](https://attack.mitre.org/groups/G0099) has used ConfuserEx to obfuscate its variant of [Imminent Monitor](https://attack.mitre.org/software/S0434), compressed payloads and RAT packages, and password protected encrypted email attachments to avoid detection.[^4]  [APT-C-36](https://attack.mitre.org/groups/G0099) has also compressed initial droppers into ZIP, LHA and UUE formats.[^10]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT-C-36](https://attack.mitre.org/groups/G0099) has disguised malicious executables to appear as legitimate files.[^10]  |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a compromised account to send a phishing email to an address likely used and monitored by the IT team within the same targeted organization.[^5]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [APT-C-36](https://attack.mitre.org/groups/G0099) has used malicious links in emails, often impersonating official notifications and documents, to direct users to execute malicious payloads.[^10]  |
| [[Audio-Visual Content\|T1683.002]] | Audio-Visual Content | [APT-C-36](https://attack.mitre.org/groups/G0099) has used phishing pages appearing like legitimate banking login portals to compromise credentials.[^7]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [APT-C-36](https://attack.mitre.org/groups/G0099) has regularly used compromised email accounts in spearphishing campaigns.[^3] [^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a macro function to set scheduled tasks, disguised as those used by Google.[^4]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [APT-C-36](https://attack.mitre.org/groups/G0099) has used geolocation filtering in malware delivery to redirect traffic not coming from a targeted region or country, such as Ecuador or Colombia, to legitimate sites.[^10] [^3] <br> |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT-C-36](https://attack.mitre.org/groups/G0099) has sent emails containing a link that appear to lead to an urgent notification from a government institution, at times using URL shorteners like cort[.]as, acortaurl[.]com, and gtly[.]to.[^10] [^6] [^6] [^3]  |
| [[External Remote Services\|T1133]] | External Remote Services | [APT-C-36](https://attack.mitre.org/groups/G0099) has used VPNs in their operational infrastructure.[^3]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [APT-C-36](https://attack.mitre.org/groups/G0099) has incorporated virtual private servers (VPS) into its operational infrastructure.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT-C-36](https://attack.mitre.org/groups/G0099) has downloaded binary data from a specified domain after the malicious document is opened.[^4]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [APT-C-36](https://attack.mitre.org/groups/G0099) has staged malware implants on group-owned repositories and sites.[^10] [^7] <br> |
| [[Steganography\|T1027.003]] | Steganography | [APT-C-36](https://attack.mitre.org/groups/G0099) has used steganography to hide malicious code, typically in the resource section of executable files.[^10] [^3] [^3] [^5]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT-C-36](https://attack.mitre.org/groups/G0099) has used VBScript for initial malware deployment including within a malicious Word document which is executed upon the document opening.[^4] [^10] [^7] <br> |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [APT-C-36](https://attack.mitre.org/groups/G0099) has used DDNS services such as DuckDNS, noip[.]com, and con-ip[.]com to redirect victims to sites or repositories hosting malware implants.[^10] [^6] [^7] [^3] [^5]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [APT-C-36](https://attack.mitre.org/groups/G0099) has set the ShowWindow property of the Win32_ProcessStartup object to zero to hide PowerShell execution.[^5]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [APT-C-36](https://attack.mitre.org/groups/G0099) has used port 4050 for C2 communications.[^4]  |
| [[Cloud Accounts\|T1586.003]] | Cloud Accounts | [APT-C-36](https://attack.mitre.org/groups/G0099) has used compromised Google Drive accounts including one associated with a  Colombian government organization.[^3]  |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | [APT-C-36](https://attack.mitre.org/groups/G0099) has gathered information on Colombian financial institutions, including Bancolombia, BBVA, Banco Caja Social, and Davivienda to craft phishing pages.[^7]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT-C-36](https://attack.mitre.org/groups/G0099) has used spearphishing emails with malicious .pdf and .docx files and password protected RAR attachments to avoid being detected by the email gateway.[^4] [^10] [^3] [^3]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [APT-C-36](https://attack.mitre.org/groups/G0099) has used process hollowing to execute malware in the memory of legitimate processes.[^10]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT-C-36](https://attack.mitre.org/groups/G0099) has used PowerShell in malware execution including as part of fileless attack chains to download additional payloads.[^10] [^5] <br> |
| [[DLL\|T1574.001]] | DLL | [APT-C-36](https://attack.mitre.org/groups/G0099) has used side-loading to execute the HijackLoader payload.[^10]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[DCRAT\|S9017]] | DCRAT | [APT-C-36](https://attack.mitre.org/groups/G0099) has used [DCRAT](https://attack.mitre.org/software/S9017) during operations.[^5]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a customized version of [AsyncRAT](https://attack.mitre.org/software/S1087).[^10] [^6] [^7] [^3]  |
| [[Remcos\|S0332]] | Remcos | [APT-C-36](https://attack.mitre.org/groups/G0099) used [Remcos](https://attack.mitre.org/software/S0332) during operations.[^6] [^7] [^3] [^5]  |
| [[Imminent Monitor\|S0434]] | Imminent Monitor | [^4]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a customized version of [QuasarRAT](https://attack.mitre.org/software/S0262) known as BlotchyQuasar.[^3] [^10]  |
| [[HeartCrypt\|S9018]] | HeartCrypt | [APT-C-36](https://attack.mitre.org/groups/G0099) has used [HeartCrypt](https://attack.mitre.org/software/S9018) in [Remcos](https://attack.mitre.org/software/S0332) infection chains.[^6]  |
| [[PureCrypter\|S9019]] | PureCrypter | [APT-C-36](https://attack.mitre.org/groups/G0099) has used [PureCrypter](https://attack.mitre.org/software/S9019) during operations.[^6]  |
| [[Caminho\|S9016]] | Caminho | [APT-C-36](https://attack.mitre.org/groups/G0099) has used [Caminho](https://attack.mitre.org/software/S9016) during operations.[^5]  |
| [[njRAT\|S0385]] | njRAT | [APT-C-36](https://attack.mitre.org/groups/G0099) has used a customized version of [njRAT](https://attack.mitre.org/software/S0385).[^10] [^6] [^3]  |



## References

[^1]: AguilaCiega


[^2]: APT-Q-98


[^3]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)


[^4]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^5]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


[^6]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^7]: [LevelBlue Blind Eagle Proton66 JUN 2025](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/)


[^8]: Blind Eagle


[^9]: TAG-144


[^10]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


