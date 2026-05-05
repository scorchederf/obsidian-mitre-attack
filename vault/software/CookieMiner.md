---
aliases: 
    - S0492
    
mitre-attack: https://attack.mitre.org/software/S0492
---

## S0492

[CookieMiner](https://attack.mitre.org/software/S0492) is mac-based malware that targets information associated with cryptocurrency exchanges as well as enabling cryptocurrency mining on the victim system itself. It was first discovered in the wild in 2019.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [CookieMiner](https://attack.mitre.org/software/S0492) can steal saved usernames and passwords in Chrome as well as credit card credentials.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [CookieMiner](https://attack.mitre.org/software/S0492) has used the `curl --upload-file` command to exfiltrate data over HTTP.[^1]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [CookieMiner](https://attack.mitre.org/software/S0492) has loaded coinmining software onto systems to mine for Koto cryptocurrency. [^1]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [CookieMiner](https://attack.mitre.org/software/S0492) can steal Google Chrome and Apple Safari browser cookies from the victim’s machine. [^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [CookieMiner](https://attack.mitre.org/software/S0492) has checked for the presence of "Little Snitch", macOS network monitoring and application firewall software, stopping and exiting if it is found.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CookieMiner](https://attack.mitre.org/software/S0492) has looked for files in the user's home directory with "wallet" in their name using `find`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CookieMiner](https://attack.mitre.org/software/S0492) can download additional scripts from a web server.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CookieMiner](https://attack.mitre.org/software/S0492) has used Google Chrome's decryption and extraction operations.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [CookieMiner](https://attack.mitre.org/software/S0492) has retrieved iPhone text messages from iTunes phone backup files.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [CookieMiner](https://attack.mitre.org/software/S0492) has checked for the presence of "Little Snitch", macOS network monitoring and application firewall software, stopping and exiting if it is found.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [CookieMiner](https://attack.mitre.org/software/S0492) has used base64 encoding to obfuscate scripts on the system.[^1]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [CookieMiner](https://attack.mitre.org/software/S0492) has used a Unix shell script to run a series of commands targeting macOS.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [CookieMiner](https://attack.mitre.org/software/S0492) has installed multiple new Launch Agents in order to maintain persistence for cryptocurrency mining software.[^1]  |
| [[Python\|T1059.006]] | Python | [CookieMiner](https://attack.mitre.org/software/S0492) has used python scripts on the user’s system, as well as the Python variant of the [Empire](https://attack.mitre.org/software/S0363) agent, EmPyre.[^1]  |




## References

[^1]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)


