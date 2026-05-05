---
aliases: 
    - S1246
    
mitre-attack: https://attack.mitre.org/software/S1246
---

## S1246

[BeaverTail](https://attack.mitre.org/software/S1246) is a malware that has both a JavaScript and C++ variant.  Active since 2022, [BeaverTail](https://attack.mitre.org/software/S1246) is capable of stealing logins from browsers and serves as a downloader for second stage payloads. [BeaverTail](https://attack.mitre.org/software/S1246) has previously been leveraged by North Korea-affiliated actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052). [BeaverTail](https://attack.mitre.org/software/S1246) has been delivered to victims through code repository sites and has been embedded within malicious attachments.[^8] [^5] [^6] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BeaverTail](https://attack.mitre.org/software/S1246) has used HTTP GET request to download malicious payloads to include [InvisibleFerret](https://attack.mitre.org/software/S1245) and HTTP POST to exfiltrate data to C2 infrastructure.[^2] [^8]  |
| [[JavaScript\|T1059.007]] | JavaScript | [BeaverTail](https://attack.mitre.org/software/S1246) has executed malicious JavaScript code.[^5] [^3] [^6] [^1] [^8]  [BeaverTail](https://attack.mitre.org/software/S1246) has also been compiled with the Qt framework to execute in both Windows and macOS.[^7]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [BeaverTail](https://attack.mitre.org/software/S1246) has stolen passwords saved in web browsers.[^5] [^2] [^4] [^7]  [BeaverTail](https://attack.mitre.org/software/S1246) has also been known to collect login data from Firefox within key3.db, key4.db and logins.json from `/.mozilla/firefox/` for exfiltration.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [BeaverTail](https://attack.mitre.org/software/S1246) has exfiltrated data collected from victim devices to C2 servers.[^2] [^8] [^7]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [BeaverTail](https://attack.mitre.org/software/S1246) has identified .ldb and .log files stored in browser extension directories for collection and exfiltration.[^6]  |
| [[Compromise Software Dependencies and Development Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | [BeaverTail](https://attack.mitre.org/software/S1246) has been hosted on code repositories and disseminated to victims through NPM packages.[^5] [^3] [^1] [^8] [^7]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [BeaverTail](https://attack.mitre.org/software/S1246) has searched the victim device for browser extensions including those commonly associated with cryptocurrency wallets.[^5] [^3] [^2] [^4] [^6] [^8] [^7]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [BeaverTail](https://attack.mitre.org/software/S1246) has been known to collect basic system information.[^5] [^8]  [BeaverTail](https://attack.mitre.org/software/S1246) has also collected data to include hostname and current timestamp prior to uploading data to the API endpoint `/uploads` on the C2 server.[^6]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [BeaverTail](https://attack.mitre.org/software/S1246) has staged collected data to the system’s temporary directory.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [BeaverTail](https://attack.mitre.org/software/S1246) has collected and archived sensitive data in a zip file.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [BeaverTail](https://attack.mitre.org/software/S1246) has exfiltrated data collected from local systems.[^2] [^6] [^8] [^7]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BeaverTail](https://attack.mitre.org/software/S1246) has obfuscated strings of code with Base64 encoding within the JavaScript version of the malware.[^6] [^8] [^7]  [BeaverTail](https://attack.mitre.org/software/S1246) has also utilized the open-source tool JavaScript-Obfuscator to obfuscate strings and functions.[^5] [^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BeaverTail](https://attack.mitre.org/software/S1246) has obtained and sent the current timestamp associated with the victim device to C2.[^6]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [BeaverTail](https://attack.mitre.org/software/S1246) has communicated with C2 IP addresses over ports 1224 or 1244.[^6] [^8] [^7]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [BeaverTail](https://attack.mitre.org/software/S1246) has collected keys stored for Solana stored in `.config/solana/id.json` and other login details associated with macOS within `/Library/Keychains/login.keychain` or for Linux within `/.local/share/keyrings`.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [BeaverTail](https://attack.mitre.org/software/S1246) has been executed through lures involving malicious JavaScript projects or trojanized remote conferencing software such as MicroTalk or FreeConference.[^6] [^7]  [BeaverTail](https://attack.mitre.org/software/S1246) has also been executed through macOS and Windows installers disguised as chat applications.[^5] [^1]  |
| [[Junk Data\|T1001.001]] | Junk Data | [BeaverTail](https://attack.mitre.org/software/S1246) has added junk data or a dummy character prepended to a string to hamper decoding attempts.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BeaverTail](https://attack.mitre.org/software/S1246) has been used to download a malicious payload to include Python based malware [InvisibleFerret](https://attack.mitre.org/software/S1245).[^5] [^2] [^4] [^6] [^8] [^7]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BeaverTail](https://attack.mitre.org/software/S1246) has searched for .ldb and .log files stored in browser extension directories for collection and exfiltration.[^2] [^4] [^6]  |
| [[Masquerading\|T1036]] | Masquerading | [BeaverTail](https://attack.mitre.org/software/S1246) has masqueraded as MiroTalk installation packages: “MiroTalk.dmg” for macOS and “MiroTalk.msi” for Windows, and has included login GUIs with MiroTalk themes.[^7]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BeaverTail](https://attack.mitre.org/software/S1246) has deleted files from a compromised host after they were exfiltrated.[^2]  |
| [[Financial Theft\|T1657]] | Financial Theft | [BeaverTail](https://attack.mitre.org/software/S1246) has searched the victim device for browser extensions commonly associated with cryptocurrency wallets.[^5] [^3] [^6] [^8] [^7]  |
| [[Keychain\|T1555.001]] | Keychain | [BeaverTail](https://attack.mitre.org/software/S1246) has collected keys associated with macOS within `/Library/Keychains/login.keychain`.[^2] [^4] [^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Contagious Interview\|G1052]] | Contagious Interview |



## References

[^1]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^2]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^3]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^4]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^5]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^6]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^7]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^8]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


