---
aliases: 
    - S0281
    
mitre-attack: https://attack.mitre.org/software/S0281
---

## S0281

[Dok](https://attack.mitre.org/software/S0281) is a Trojan application disguised as a .zip file that is able to collect user credentials and install a malicious proxy server to redirect a user's network traffic (i.e. [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)).[^4] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [Dok](https://attack.mitre.org/software/S0281) proxies web traffic to potentially monitor and alter victim HTTP(S) traffic.[^4] [^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Dok](https://attack.mitre.org/software/S0281) is packed with an UPX executable packer.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Dok](https://attack.mitre.org/software/S0281) installs two LaunchAgents to redirect all network traffic with a randomly generated name for each plist file maintaining the format `com.random.name.plist`.[^4] [^2]  |
| [[AppleScript\|T1059.002]] | AppleScript | [Dok](https://attack.mitre.org/software/S0281) uses AppleScript to create a login item for persistence.[^4]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [Dok](https://attack.mitre.org/software/S0281) gives all users execute permissions for the application using the command `chmod +x /Users/Shared/AppStore.app`.[^2]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Dok](https://attack.mitre.org/software/S0281) exfiltrates logs of its execution stored in the `/tmp` folder over FTP using the `curl` command.[^1]   |
| [[Install Root Certificate\|T1553.004]] | Install Root Certificate | [Dok](https://attack.mitre.org/software/S0281) installs a root certificate to aid in [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) actions using the command `add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/filename`.[^4] [^1]  |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | [Dok](https://attack.mitre.org/software/S0281) adds `admin  ALL=(ALL) NOPASSWD: ALL` to the `/etc/sudoers` file.[^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Dok](https://attack.mitre.org/software/S0281) prompts the user for credentials.[^4]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Dok](https://attack.mitre.org/software/S0281) downloads and installs [Tor](https://attack.mitre.org/software/S0183) via homebrew.[^4]  |
| [[Login Items\|T1547.015]] | Login Items | [Dok](https://attack.mitre.org/software/S0281) uses AppleScript to install a login Item by sending Apple events to the `System Events` process.[^1]  |




## References

[^1]: [hexed osx.dok analysis 2019](https://web.archive.org/web/20221007144948/http://www.hexed.in/2019/07/osxdok-analysis.html)


[^2]: [CheckPoint Dok](https://blog.checkpoint.com/2017/04/27/osx-malware-catching-wants-read-https-traffic/)


[^3]: Retefe


[^4]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^5]: Dok


