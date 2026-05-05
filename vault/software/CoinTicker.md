---
aliases: 
    - S0369
    
mitre-attack: https://attack.mitre.org/software/S0369
---

## S0369

[CoinTicker](https://attack.mitre.org/software/S0369) is a malicious application that poses as a cryptocurrency price ticker and installs components of the open source backdoors EvilOSX and EggShell.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [CoinTicker](https://attack.mitre.org/software/S0369) downloads the following hidden files to evade detection and maintain persistence: /private/tmp/.info.enc, /private/tmp/.info.py, /private/tmp/.server.sh, ~/Library/LaunchAgents/.espl.plist, ~/Library/Containers/.[random string]/[random string].[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [CoinTicker](https://attack.mitre.org/software/S0369) initially downloads a hidden encoded file.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [CoinTicker](https://attack.mitre.org/software/S0369) executes a bash script to establish a reverse shell.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [CoinTicker](https://attack.mitre.org/software/S0369) executes a Python script to download its second stage.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CoinTicker](https://attack.mitre.org/software/S0369) decodes the initially-downloaded hidden encoded file using OpenSSL.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [CoinTicker](https://attack.mitre.org/software/S0369) creates user launch agents named .espl.plist and com.apple.[random string].plist to establish persistence.[^1] 	 |
| [[Python\|T1059.006]] | Python | [CoinTicker](https://attack.mitre.org/software/S0369) executes a Python script to download its second stage.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [CoinTicker](https://attack.mitre.org/software/S0369) executes a bash script to establish a reverse shell.[^1]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | [CoinTicker](https://attack.mitre.org/software/S0369) downloads the EggShell mach-o binary using curl, which does not set the quarantine flag.[^1]  |




## References

[^1]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)


