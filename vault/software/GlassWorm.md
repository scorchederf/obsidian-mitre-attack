---
aliases: 
    - S9010
    
mitre-attack: https://attack.mitre.org/software/S9010
---

## S9010

[GlassWorm](https://attack.mitre.org/software/S9010) is a worm that propagated through supply chain attacks by compromising repository credentials from victim environments and having malicious payloads added to those compromised accounts for distribution to victims across the various development ecosystems.[^5] [^4] [^2]    [GlassWorm](https://attack.mitre.org/software/S9010) has numerous variants, including Rust binaries, encrypted JavaScript and a variant leveraging invisible Unicode characters that made reverse engineering difficult.[^6] [^5] [^1]   [GlassWorm](https://attack.mitre.org/software/S9010) has employed a unique command and control (C2) methodology using Solana blockchain.[^3] [^5]    [GlassWorm](https://attack.mitre.org/software/S9010) was first reported in October 2025.[^3] [^5] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Databases\|T1213.006]] | Databases | [GlassWorm](https://attack.mitre.org/software/S9010) has collected data from macOS devices through the gathering of Apple Notes related files by targeting `/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite`,  `/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite-wal`, and `/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite-shm`.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [GlassWorm](https://attack.mitre.org/software/S9010) has distributed C2 using BitTorrent’s Distributed Hash Table (DHT) network to harness a decentralized command capability.[^5]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [GlassWorm](https://attack.mitre.org/software/S9010) has utilized logic to avoid executing on Russian based devices.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has the ability to check the system’s time zone on the victim device.[^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [GlassWorm](https://attack.mitre.org/software/S9010) has archived collected files within a zip file prior to exfiltration to include `/tmp/out.zip`.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GlassWorm](https://attack.mitre.org/software/S9010) has used HTTP for C2 and extracts data from the HTTP response headers.[^5]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [GlassWorm](https://attack.mitre.org/software/S9010) has established persistence on macOS via a LaunchAgent by writing a plist under `/library/LaunchAgents`.[^6] [^2]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged peer-to-peer software to facilitate communications within the victim network to include the software WebRTC.[^5]   [GlassWorm](https://attack.mitre.org/software/S9010) has also established a SOCKS proxy to interact with victim devices that also acted as a proxy node for follow-on behaviors.[^5]  |
| [[Network Device Configuration Dump\|T1602.002]] | Network Device Configuration Dump | [GlassWorm](https://attack.mitre.org/software/S9010) has gathered data pertaining to VPN configurations.[^6] [^2]   [GlassWorm](https://attack.mitre.org/software/S9010) has also targeted locally stored data on macOS located in `/Library/Application Support/Fortinet/FortiClient/conf/vpn.plist`.[^2]  |
| [[Keychain\|T1555.001]] | Keychain | [GlassWorm](https://attack.mitre.org/software/S9010) has collected keys stored within `/Library/Keychains/login.keychain-db`.[^6] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [GlassWorm](https://attack.mitre.org/software/S9010) has decoded its Base64 instructions.[^5]   [GlassWorm](https://attack.mitre.org/software/S9010) has also decrypted its AES protected payloads.[^6] [^5] [^2]  |
| [[Delay Execution\|T1678]] | Delay Execution | [GlassWorm](https://attack.mitre.org/software/S9010) has used a timeout function set to `9e5` which delays execution 900,000 milliseconds or 15 minutes to avoid detection.[^6]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [GlassWorm](https://attack.mitre.org/software/S9010) has harvested Safari cookies stored within `/Library/Containers/com.apple.Safari/Data/Library/Cookies/ Cookies.binarycookies`.[^2]   [GlassWorm](https://attack.mitre.org/software/S9010) has also stolen cookies within Chromium and Firefox browsers.[^6] [^2]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged blockchain-based C2 infrastructure to include Solana blockchain that contains additional C2 details within the memo field.[^6] [^3] [^5] [^4] [^2] [^1]   [GlassWorm](https://attack.mitre.org/software/S9010) has also leveraged Google Calendar to host encoded data.[^5] [^2] [^1]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [GlassWorm](https://attack.mitre.org/software/S9010) has gathered code repository authentication materials for NPM and GitHub.[^6] [^5] [^2]   [GlassWorm](https://attack.mitre.org/software/S9010) has collected details pertaining to the npm configuration data for `_authToken`.[^5] [^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [GlassWorm](https://attack.mitre.org/software/S9010) has gathered credentials stored in Mozilla FireFox and Chromium-based Browsers.[^6] [^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [GlassWorm](https://attack.mitre.org/software/S9010) has collected local data from a compromised host to include desktop cryptocurrency wallet data, and documents from within Desktop, Documents, and Downloads.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged Hidden Virtual Network Computing (HVNC) to remain undetected and conduct execution of collection and communication actions.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged AES-256-CBC encryption to obfuscate its malicious JavaScript payload.[^6] [^5] [^2] [^1]   [GlassWorm](https://attack.mitre.org/software/S9010) has also utilized Base64 encoding to obfuscate the C2 details stored in the Solana memo field.[^6] [^5] [^1]  |
| [[Financial Theft\|T1657]] | Financial Theft | [GlassWorm](https://attack.mitre.org/software/S9010) has the ability to steal credentials for cryptocurrency wallets.[^6] [^5] [^2]  |
| [[Masquerading\|T1036]] | Masquerading | [GlassWorm](https://attack.mitre.org/software/S9010) has masqueraded as legitimate VSCode extensions.[^4] [^1]   [GlassWorm](https://attack.mitre.org/software/S9010) has also impersonated Github projects.[^4]  |
| [[Compromise Software Dependencies and Development Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | [GlassWorm](https://attack.mitre.org/software/S9010) has spread through Visual Studio extensions.[^5] [^4] [^2]   [GlassWorm](https://attack.mitre.org/software/S9010) has also spread through JavaScript projects hosted on Github.[^4]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [GlassWorm](https://attack.mitre.org/software/S9010) has staged collected data in a working directory within a temp folder to include `/tmp/ijewf`.[^6] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [GlassWorm](https://attack.mitre.org/software/S9010) has set registry run keys for persistence in both `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\`.[^5]  |
| [[Invisible Unicode\|T1027.018]] | Invisible Unicode | [GlassWorm](https://attack.mitre.org/software/S9010) has utilized invisible Unicode Private Use Area (PUA) characters to obfuscate its malicious code so that it does not render in code editors.[^6] [^5] [^4]  |
| [[Transmitted Data Manipulation\|T1565.002]] | Transmitted Data Manipulation | [GlassWorm](https://attack.mitre.org/software/S9010) can intercept and modify transaction details associated with hardware wallet applications before signing.[^6]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged geofencing logic to detect whether it is operating in a Russian associated time zone to determine whether it continues to execute.[^2]  |
| [[AppleScript\|T1059.002]] | AppleScript | [GlassWorm](https://attack.mitre.org/software/S9010) has utilized AppleScript to include `set keychainPassword to do shell script` to execute shell command that retrieves passwords from the macOS keychain.[^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged JavaScript to execute its malicious code to include its hidden Unicode characters using the `eval` call.[^3] [^5] [^4] [^2]   [GlassWorm](https://attack.mitre.org/software/S9010) has also utilized encrypted payloads compiled in JavaScript.[^6]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has identified the system language settings by checking for `ru_RU`, `ru-RU`, `ru`, and `Russian` to prevent execution in a Russian associated device.[^2]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has searched browser data for cookies, history, login databases, and cryptocurrency wallets.[^2]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [GlassWorm](https://attack.mitre.org/software/S9010) has utilized Google Calendar as backup C2.[^5] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has the ability to check the OS of the victim host.[^2] [^1]   [GlassWorm](https://attack.mitre.org/software/S9010) has checked whether the OS platform value includes `darwin` prior to execution of macOS specific scripts.[^2] [^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [GlassWorm](https://attack.mitre.org/software/S9010) can modify hardware wallet applications.[^6]  |
| [[Software Discovery\|T1518]] | Software Discovery | [GlassWorm](https://attack.mitre.org/software/S9010) has searched for existing wallet applications to include Ledger Live and Trezor Suite.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GlassWorm](https://attack.mitre.org/software/S9010) has downloaded additional payloads from C2.[^6] [^3] [^2] [^1]  |




## References

[^1]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)


[^2]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^3]: [Koi Glassworm Extensions November 2025](https://www.koi.ai/blog/glassworm-returns-new-wave-openvsx-malware-expose-attacker-infrastructure)


[^4]: [Aikido GlassWorm October 2025](https://www.aikido.dev/blog/the-return-of-the-invisible-threat-hidden-pua-unicode-hits-github-repositorties)


[^5]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)


[^6]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)


