---
aliases: 
    - APT19
    - Codoso
    - C0d0so0
    - Codoso Team
    - Sunshop Group
mitre-attack: https://attack.mitre.org/groups/G0073
---

## G0073

[APT19](https://attack.mitre.org/groups/G0073) is a Chinese-based threat group that has targeted a variety of industries, including defense, finance, energy, pharmaceutical, telecommunications, high tech, education, manufacturing, and legal services. In 2017, a phishing campaign was used to target seven law and investment firms. [^8]  Some analysts track [APT19](https://attack.mitre.org/groups/G0073) and [Deep Panda](https://attack.mitre.org/groups/G0009) as the same group, but it is unclear from open source information if the groups are the same. [^5]  [^4]  [^7] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | An [APT19](https://attack.mitre.org/groups/G0073) HTTP malware variant establishes persistence by setting the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\Windows Debug Tools-%LOCALAPPDATA%\`.[^7]  |
| [[PowerShell\|T1059.001]] | PowerShell | [APT19](https://attack.mitre.org/groups/G0073) used PowerShell commands to execute payloads.[^8]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [APT19](https://attack.mitre.org/groups/G0073) used `-W Hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows by setting the WindowStyle parameter to hidden. [^8]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to collect the MAC address and IP address from the victim’s machine.[^7]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to collect the victim’s username.[^7]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [APT19](https://attack.mitre.org/groups/G0073) configured its payload to inject into the rundll32.exe.[^8]  |
| [[Modify Registry\|T1112]] | Modify Registry | [APT19](https://attack.mitre.org/groups/G0073) uses a Port 22 malware variant to modify several Registry keys.[^7]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [APT19](https://attack.mitre.org/groups/G0073) performed a watering hole attack on forbes.com in 2014 to compromise targets.[^7]  |
| [[Windows Service\|T1543.003]] | Windows Service | An [APT19](https://attack.mitre.org/groups/G0073) Port 22 malware variant registers itself as a service.[^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT19](https://attack.mitre.org/groups/G0073) used HTTP for C2 communications. [APT19](https://attack.mitre.org/groups/G0073) also used an HTTP malware variant to communicate over HTTP for C2.[^8] [^7]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [APT19](https://attack.mitre.org/groups/G0073) downloaded and launched code within a SCT file.[^8]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [APT19](https://attack.mitre.org/groups/G0073) used Base64 to obfuscate payloads.[^8]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT19](https://attack.mitre.org/groups/G0073) sent spearphishing emails with malicious attachments in RTF and XLSM formats to deliver initial exploits.[^8]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT19](https://attack.mitre.org/groups/G0073) attempted to get users to launch malicious attachments delivered via spearphishing emails.[^8]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT19](https://attack.mitre.org/groups/G0073) collected system architecture information. [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to gather the hostname and CPU information from the victim’s machine.[^8] [^7]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | An [APT19](https://attack.mitre.org/groups/G0073) HTTP malware variant used Base64 to encode communications to the C2 server.[^7]  |
| [[Tool\|T1588.002]] | Tool | [APT19](https://attack.mitre.org/groups/G0073) has obtained and used publicly-available tools like [Empire](https://attack.mitre.org/software/S0363).[^6] [^8]  |
| [[DLL\|T1574.001]] | DLL | [APT19](https://attack.mitre.org/groups/G0073) launched an HTTP malware variant and a Port 22 malware variant using a legitimate executable that loaded the malicious DLL.[^7]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [APT19](https://attack.mitre.org/groups/G0073) used Regsvr32 to bypass application control techniques.[^8]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | An [APT19](https://attack.mitre.org/groups/G0073) HTTP malware variant decrypts strings using single-byte XOR keys.[^7]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [APT19](https://attack.mitre.org/groups/G0073) used Base64 to obfuscate executed commands.[^8]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Empire\|S0363]] | Empire | [^6]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^8]  |



## References

[^1]: Codoso Team


[^2]: Codoso


[^3]: Sunshop Group


[^4]: [FireEye APT Groups](https://www.fireeye.com/current-threats/apt-groups.html#apt19)


[^5]: [ICIT China's Espionage Jul 2016](https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/)


[^6]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^7]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^8]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^9]: [Dark Reading Codoso Feb 2015](https://www.darkreading.com/attacks-breaches/chinese-hacking-group-codoso-team-uses-forbescom-as-watering-hole-/d/d-id/1319059)


[^10]: C0d0so0


[^11]: APT19


