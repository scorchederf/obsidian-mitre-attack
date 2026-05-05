---
aliases: 
    - Higaisa
mitre-attack: https://attack.mitre.org/groups/G0126
---

## G0126

[Higaisa](https://attack.mitre.org/groups/G0126) is a threat group suspected to have South Korean origins. [Higaisa](https://attack.mitre.org/groups/G0126) has targeted government, public, and trade organizations in North Korea; however, they have also carried out attacks in China, Japan, Russia, Poland, and other nations. [Higaisa](https://attack.mitre.org/groups/G0126) was first disclosed in early 2019 but is assessed to have operated as early as 2009.[^2] [^1] [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Higaisa](https://attack.mitre.org/groups/G0126) has used VBScript code on the victim's machine.[^3]  |
| [[Native API\|T1106]] | Native API | [Higaisa](https://attack.mitre.org/groups/G0126) has called various native OS APIs.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Higaisa](https://attack.mitre.org/groups/G0126) exfiltrated data over its C2 channel.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Higaisa](https://attack.mitre.org/groups/G0126)’s JavaScript file used a legitimate Microsoft Office 2007 package to side-load the `OINFO12.OCX` dynamic link library.[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Higaisa](https://attack.mitre.org/groups/G0126) used a function to gather the current time.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Higaisa](https://attack.mitre.org/groups/G0126) discovered system proxy settings and used them if available.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Higaisa](https://attack.mitre.org/groups/G0126) used malicious e-mail attachments to lure victims into executing LNK files.[^2] [^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Higaisa](https://attack.mitre.org/groups/G0126) used Base64 encoded compressed payloads.[^2] [^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Higaisa](https://attack.mitre.org/groups/G0126) dropped and added `officeupdate.exe` to scheduled tasks.[^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Higaisa](https://attack.mitre.org/groups/G0126) collected the system GUID and computer name.[^3] [^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Higaisa](https://attack.mitre.org/groups/G0126) has sent spearphishing emails containing malicious attachments.[^2] [^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Higaisa](https://attack.mitre.org/groups/G0126) used HTTP and HTTPS to send data back to its C2 server.[^2] [^1]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [Higaisa](https://attack.mitre.org/groups/G0126) used a FakeTLS session for C2 communications.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Higaisa](https://attack.mitre.org/groups/G0126) has exploited CVE-2018-0798 for execution.[^3]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Higaisa](https://attack.mitre.org/groups/G0126) sent the victim computer identifier in a User-Agent string back to the C2 server every 10 minutes.[^3]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Higaisa](https://attack.mitre.org/groups/G0126) used JavaScript to execute additional files.[^2] [^1] [^3]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Higaisa](https://attack.mitre.org/groups/G0126) performed padding with null bytes before calculating its hash.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Higaisa](https://attack.mitre.org/groups/G0126) used Base64 encoded compressed payloads.[^2] [^1]  |
| [[XSL Script Processing\|T1220]] | XSL Script Processing | [Higaisa](https://attack.mitre.org/groups/G0126) used an XSL file to run VBScript code.[^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Higaisa](https://attack.mitre.org/groups/G0126) used a payload that creates a hidden window.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Higaisa](https://attack.mitre.org/groups/G0126) used AES-128 to encrypt C2 traffic.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Higaisa](https://attack.mitre.org/groups/G0126) collected the system volume serial number.[^3] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Higaisa](https://attack.mitre.org/groups/G0126) added a spoofed binary to the start-up folder for persistence.[^2] [^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Higaisa](https://attack.mitre.org/groups/G0126)’s shellcode attempted to find the process ID of the current process.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Higaisa](https://attack.mitre.org/groups/G0126) named a shellcode loader binary `svchast.exe` to spoof the legitimate `svchost.exe`.[^2] [^1]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Higaisa](https://attack.mitre.org/groups/G0126) used `ipconfig` to gather network configuration information.[^2] [^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Higaisa](https://attack.mitre.org/groups/G0126) used `cmd.exe` for execution.[^2] [^1] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Higaisa](https://attack.mitre.org/groups/G0126) used certutil to decode Base64 binaries at runtime and a 16-byte XOR key to decrypt data.[^2] [^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [^2] [^3]  |
| [[PlugX\|S0013]] | PlugX | [^2]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^2]  |



## References

[^1]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^2]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^3]: [PTSecurity Higaisa 2020](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)


