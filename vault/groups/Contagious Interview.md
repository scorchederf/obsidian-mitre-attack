---
aliases: 
    - Contagious Interview
    - DeceptiveDevelopment
    - Gwisin Gang
    - Tenacious Pungsan
    - DEV#POPPER
    - PurpleBravo
    - TAG-121
mitre-attack: https://attack.mitre.org/groups/G1052
---

## G1052

[Contagious Interview](https://attack.mitre.org/groups/G1052) is a North Korea–aligned threat group active since 2023. The group conducts both cyberespionage and financially motivated operations, including the theft of cryptocurrency and user credentials. [Contagious Interview](https://attack.mitre.org/groups/G1052) targets Windows, Linux, and macOS systems, with a particular focus on individuals engaged in software development and cryptocurrency-related activities. [^5] [^11] [^20] [^10] [^13] [^17] [^21] [^15] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Keychain\|T1555.001]] | Keychain | [Contagious Interview](https://attack.mitre.org/groups/G1052) has leveraged malware variants configured to dump credentials from the macOS keychain.[^2] [^9] [^18]  |
| [[Establish Accounts\|T1585]] | Establish Accounts | [Contagious Interview](https://attack.mitre.org/groups/G1052) has created and maintained personas on code repositories to distribute malicious payloads.[^3] [^5] [^8] [^9] [^18] [^13]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Contagious Interview](https://attack.mitre.org/groups/G1052) has conducted key word searches within files and directories on a compromised hosts to identify files for exfiltration.[^13] [^21]  |
| [[Web Services\|T1583.006]] | Web Services | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used web services such as Dropbox to receive stolen data and Google Drive, Firebase, GitHub, and Telegram to disseminate files.[^2] [^10]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also used a cloud platform such as Vercel for C2 operations leveraging malicious web applications and static pages.[^8] [^9] [^18]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also used Slack to coordinate their activities.[^3]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used TCP port 1224 for C2.[^8]  |
| [[Malicious Library\|T1204.005]] | Malicious Library | [Contagious Interview](https://attack.mitre.org/groups/G1052) has relied on users to install a malicious library from a code repository to infect the victim's device and has led to additional payload distribution and theft of sensitive data.[^3] [^5] [^11] [^8] [^9] [^18] [^13] [^1] [^17] [^21]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Contagious Interview](https://attack.mitre.org/groups/G1052) has downloaded remote management and monitoring software such as “AnyDesk” for post compromise activities.[^11] [^13] [^19] [^21] [^15]  |
| [[Masquerading\|T1036]] | Masquerading | [Contagious Interview](https://attack.mitre.org/groups/G1052) has delivered [BeaverTail](https://attack.mitre.org/software/S1246) malware masquerading as legitimate software or applications.[^11] [^13] [^17] [^21] [^15]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also delivered malicious payloads masquerading as legitimate software drivers.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Contagious Interview](https://attack.mitre.org/groups/G1052) has distributed malicious files requiring direct victim interaction to execute through the guise of a code test.[^19] [^7]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Contagious Interview](https://attack.mitre.org/groups/G1052) has requested victims to disable Docker and other container environments in attempts to thwart container isolation and ensure device infection.[^18]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [Contagious Interview](https://attack.mitre.org/groups/G1052) has leveraged Telegram API to exfiltrate stolen data.[^13]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Contagious Interview](https://attack.mitre.org/groups/G1052) has targeted macOS victim hosts using a bash downloader coremedia.sh and a bash script cloud.sh.[^2]  |
| [[Malware\|T1587.001]] | Malware | [Contagious Interview](https://attack.mitre.org/groups/G1052) has developed malware that utilizes Qt cross-platform framework to include [BeaverTail](https://attack.mitre.org/software/S1246).[^13] [^15]  |
| [[Code Repositories\|T1593.003]] | Code Repositories | [Contagious Interview](https://attack.mitre.org/groups/G1052) had identified and solicited victims through code repositories such as GitHub.[^21]  |
| [[Domains\|T1583.001]] | Domains | [Contagious Interview](https://attack.mitre.org/groups/G1052) has registered domains to leverage in their social engineering campaigns.[^10] [^13] [^15]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also registered domains to utilize for C2.[^3] [^2] [^5] [^8] [^9] [^18]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used fake job advertisements and messages sent via social media to spearphish targets.[^2] [^5] [^10] [^13] [^19] [^7]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also leveraged hiring websites to solicit victims.[^10]  |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | [Contagious Interview](https://attack.mitre.org/groups/G1052) has targeted macOS victim hosts using a bash downloader `coremedia.sh` and a bash script `cloud.sh`.[^2]  |
| [[Written Content\|T1683.001]] | Written Content | [Contagious Interview](https://attack.mitre.org/groups/G1052) has created fake social media accounts such as LinkedIn and Telegram accounts for their targeting efforts.[^13]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Contagious Interview](https://attack.mitre.org/groups/G1052) has convinced victims to disable Docker and other container environments and run code on their machine natively in attempts to bypass container isolation and ensure device infection.[^18]  |
| [[Search Threat Vendor Data\|T1681]] | Search Threat Vendor Data | [Contagious Interview](https://attack.mitre.org/groups/G1052) has registered accounts with Threat Intelligence vendor services to check for reporting associated with their infrastructure and to evaluate new potential infrastructure.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Contagious Interview](https://attack.mitre.org/groups/G1052) has utilized VBS scripts to open cmd.exe and run commands to include the go_batch.bat batch file.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Contagious Interview](https://attack.mitre.org/groups/G1052) has stolen cryptocurrency wallet credentials and credit card information utilizing [BeaverTail](https://attack.mitre.org/software/S1246) and [InvisibleFerret](https://attack.mitre.org/software/S1245) malware.[^11] [^9] [^18] [^13] [^17] [^21] [^15]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Contagious Interview](https://attack.mitre.org/groups/G1052) has exfiltrated victim information using FTP.[^13] [^21] [^15]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Contagious Interview](https://attack.mitre.org/groups/G1052) has leveraged JavaScript in the execution of their downloader malware targeting Windows devices using a NodeJS script titled nvidia.js.[^2]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | [Contagious Interview](https://attack.mitre.org/groups/G1052) has established persistence using [InvisibleFerret](https://attack.mitre.org/software/S1245) malware to create a .desktop entry to run on startup on GNOME-based Linux devices.[^17]  |
| [[Develop Capabilities\|T1587]] | Develop Capabilities | [Contagious Interview](https://attack.mitre.org/groups/G1052) developed malicious NPM packages for delivery to or retrieval by victims.[^3] [^5] [^11] [^8] [^9] [^18] [^21]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Contagious Interview](https://attack.mitre.org/groups/G1052) has configured malware to remove archives used in collection activities following successful exfiltration.[^9]  |
| [[Tool\|T1588.002]] | Tool | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used remote management and monitoring software such as “AnyDesk”.[^11] [^13] [^19] [^21] [^15]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Contagious Interview](https://attack.mitre.org/groups/G1052) has established persistence using [InvisibleFerret](https://attack.mitre.org/software/S1245) malware to create file to run the script on Startup via LaunchAgents.[^17]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also utilized a plist file located in `/Library/LaunchAgents` to enable a malicious bash script the ability to persist.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Contagious Interview](https://attack.mitre.org/groups/G1052) has exfiltrated data from a compromised host to actor-controlled C2 servers.[^3] [^11] [^10] [^8] [^9] [^18] [^13] [^19] [^21] [^15]  |
| [[Social Media\|T1593.001]] | Social Media | [Contagious Interview](https://attack.mitre.org/groups/G1052) had identified and solicited victims through social media such as LinkedIn, X, and Telegram.[^2] [^5] [^19] [^7] [^21] [^15]  |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used services such as Astrill VPN.[^3] [^10]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used hexadecimal string encoding to hide critical JavaScript module names, function names, and C2 URLs, which are decoded dynamically at runtime.[^8]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Contagious Interview](https://attack.mitre.org/groups/G1052) has exfiltrated stolen passwords to Dropbox.[^2]  |
| [[Impersonation\|T1684.001]] | Impersonation | [Contagious Interview](https://attack.mitre.org/groups/G1052) had impersonated HR hiring personnel through social media, job board notifications, and conducted interviews with victims in order to entice them to download malware disguised as legitimate applications or malicious scripts from code repositories.[^3] [^5] [^18] [^19] [^1] [^7] [^21] [^15]  |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | [Contagious Interview](https://attack.mitre.org/groups/G1052) has leveraged ClickFix type tactics enticing victims to copy and paste malicious code.[^3] [^2] [^5]  |
| [[Python\|T1059.006]] | Python | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used the Python-based malware such as [InvisibleFerret](https://attack.mitre.org/software/S1245) to install and execute Python Packages and Python modules.[^11] [^13] [^21]  |
| [[Gather Victim Identity Information\|T1589]] | Gather Victim Identity Information | [Contagious Interview](https://attack.mitre.org/groups/G1052) has researched specific professional groups such as software developers for targeting.[^18] [^19] [^1] [^7] [^21] [^15]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also researched individuals who work in roles related to cryptocurrency and blockchain technologies.[^3] [^2]  |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [Contagious Interview](https://attack.mitre.org/groups/G1052) has acquired virtual private servers from services such as Stark Industries Solutions and RouterHosting.[^11] [^21]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also utilized hosting providers to include Tier[.]Net, Majestic Hosting, Leaseweb Singapore, and Kaopu Cloud.[^10]  |
| [[Artificial Intelligence\|T1588.007]] | Artificial Intelligence | [Contagious Interview](https://attack.mitre.org/groups/G1052) has appeared to have used AI to generate images and content to facilitate their campaigns.[^10]  |
| [[Proxy\|T1090]] | Proxy | [Contagious Interview](https://attack.mitre.org/groups/G1052) has leveraged Astrill VPN for C2.[^10]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Contagious Interview](https://attack.mitre.org/groups/G1052) has encrypted C2 traffic using RC4.[^2] <br> |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Contagious Interview](https://attack.mitre.org/groups/G1052) has lured victims to click on a malicious link that led to download of a malicious payload.[^10]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also leveraged links to malicious payloads on social media and code repositories.[^10]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Contagious Interview](https://attack.mitre.org/groups/G1052) has utilized email notifications from malware distribution servers to track victim engagement.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Contagious Interview](https://attack.mitre.org/groups/G1052) has configured malicious webpages to identify the victim’s operating system by reviewing the details of the victims User-Agent of their browser.[^2]  |
| [[Search Open Websites／Domains\|T1593]] | Search Open Websites／Domains | [Contagious Interview](https://attack.mitre.org/groups/G1052) has utilized open-source indicator of compromise repositories to determine their exposure to include VirusTotal, and MalTrail.[^3]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Contagious Interview](https://attack.mitre.org/groups/G1052) has obfuscated JavaScript code using Base64 and variable substitutions.[^13] [^19] [^1] [^17]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Contagious Interview](https://attack.mitre.org/groups/G1052) has hosted malicious payloads on code repositories used as lures for victims to download.[^3] [^5] [^11] [^10] [^8] [^9] [^18] [^13] [^19] [^1] [^17] [^21]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Contagious Interview](https://attack.mitre.org/groups/G1052) has utilized Visual Basic scripts in the execution of their downloader malware targeting Windows devices including as script called update.vbs.[^2]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Contagious Interview](https://attack.mitre.org/groups/G1052) has configured C2 endpoints to review IP geolocation, request headers, victim environment details and runtime conditions prior to delivering payloads.[^18]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Contagious Interview](https://attack.mitre.org/groups/G1052) has created fake social media accounts such as LinkedIn and Telegram accounts for their targeting efforts.[^10] [^13] [^19] [^7] [^15] [^17]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Contagious Interview](https://attack.mitre.org/groups/G1052) has established persistence using [InvisibleFerret](https://attack.mitre.org/software/S1245) malware to place a .bat file in the Startup Folder.[^17]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Contagious Interview](https://attack.mitre.org/groups/G1052) has created fake email accounts to correspond with social media accounts, fake LinkedIn personas, code repository accounts, and job announcements on development job board services.[^3] [^10] [^18] [^13] [^17] [^15]  [Contagious Interview](https://attack.mitre.org/groups/G1052) has also utilized fake email accounts with Threat Intelligence vendor services.[^3]  |
| [[Audio-Visual Content\|T1683.002]] | Audio-Visual Content | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used AI to clone video-conferencing applications to distribute their [BeaverTail](https://attack.mitre.org/software/S1246) malware. They have also used AI to create deepfake videos. [^15]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [^11] [^13] [^17] [^21] [^15] [^10]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [^8] [^9] [^18]  |
| [[BeaverTail\|S1246]] | BeaverTail | [^13] [^17] [^21] [^15] [^11] [^10]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [^9]  |



## References

[^1]: [Securonix Contagious Interview DEVPOPPER April 2024](https://www.securonix.com/blog/analysis-of-devpopper-new-attack-campaign-targeting-software-developers-likely-associated-with-north-korean-threat-actors/)


[^2]: [Sekoia ClickFake 2025](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)


[^3]: [Sentinel One Contagious Interview ClickFix September 2025](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)


[^4]: Gwisin Gang


[^5]: [Validin Contagious Interview North Korea ClickFix January 2025](https://www.validin.com/blog/inoculating_contagious_interview_with_validin/)


[^6]: PurpleBravo


[^7]: [SecurityScorecard Contagious Interview FamousChollima October 2024](https://securityscorecard.com/blog/the-job-offer-that-wasnt-how-we-stopped-an-espionage-plot/)


[^8]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


[^9]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^10]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^11]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^12]: DEV#POPPER


[^13]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^14]: [dtex DPRK 2025 structure ITworkers](https://reports.dtexsystems.com/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf)


[^15]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^16]: DeceptiveDevelopment


[^17]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^18]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^19]: [SecurityScorecard Contagious Interview October 2024](https://securityscorecard.com/blog/inside-a-north-korean-phishing-operation-targeting-devops-employees/)


[^20]: [Datadog Contagious Interview Tenacious Pungsan October 2024](https://securitylabs.datadoghq.com/articles/tenacious-pungsan-dprk-threat-actor-contagious-interview/)


[^21]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^22]: Tenacious Pungsan


[^23]: TAG-121


