---
aliases: 
    - Tropic Trooper
    - Pirate Panda
    - KeyBoy
mitre-attack: https://attack.mitre.org/groups/G0081
---

## G0081

[Tropic Trooper](https://attack.mitre.org/groups/G0081) is an unaffiliated threat group that has led targeted campaigns against targets in Taiwan, the Philippines, and Hong Kong. [Tropic Trooper](https://attack.mitre.org/groups/G0081) focuses on targeting government, healthcare, transportation, and high-tech industries and has been active since 2011.[^3] [^13] [^5] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has installed a service pointing to a malicious DLL dropped to disk.[^8]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has deleted dropper files on an infected system using command scripts.[^5] 	 |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Tropic Trooper](https://attack.mitre.org/groups/G0081) sent spearphishing emails that contained malicious Microsoft Office and fake installer file attachments.[^13] [^4] [^2] [^6] [^5]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used a delivered trojan to download additional files.[^5]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) is capable of enumerating the running processes on the system using `pslist`.[^13] [^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has lured victims into executing malware via malicious e-mail attachments.[^6]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has encrypted traffic with the C2 to prevent network detection.[^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used HTTP in communication with the C2.[^6] [^5]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created a hidden directory under `C:\ProgramData\Apple\Updates\` and `C:\Users\Public\Documents\Flash\`.[^3] [^5]  |
| [[Template Injection\|T1221]] | Template Injection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) delivered malicious documents with the XLSX extension, typically used by OpenXML documents, but the file itself was actually an OLE (XLS) document.[^13]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used `letmein` to scan for saved usernames on the target system.[^4]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used `pr` and an openly available tool to scan for open ports on target systems.[^4] [^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used scripts to collect the host's network topology.[^5] 	 |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has exfiltrated data using USB storage devices.[^5] 	 |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created shortcuts in the Startup folder to establish persistence.[^6] [^5]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has started a web service in the target host and wait for the adversary to connect, acting as a web shell.[^5] 	 |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used SSL to connect to C2 servers.[^3] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used Windows command scripts.[^5] 	 |
| [[Native API\|T1106]] | Native API | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used multiple Windows APIs including HttpInitialize, HttpCreateHttpHandle, and HttpAddUrl.[^5]  |
| [[DLL\|T1574.001]] | DLL | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has been known to side-load DLLs using a valid version of a Windows Address Book and Windows Defender executable with one of their tools.[^9] [^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has monitored files' modified time.[^5] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has encrypted configuration files.[^3] [^5]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has hidden payloads in Flash directories and fake installer files.[^5]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used base64 encoding to hide command strings delivered from the C2.[^5]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used known administrator account credentials to execute the backdoor directly.[^5] 	 |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has detected a target system’s system volume information.[^4] [^5]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has created the Registry key `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell` and sets the value to establish persistence.[^13] [^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has executed commands through Microsoft security vulnerabilities, including CVE-2017-11882, CVE-2018-0802, and CVE-2012-0158.[^3] [^13]  |
| [[DNS\|T1071.004]] | DNS | [Tropic Trooper](https://attack.mitre.org/groups/G0081)'s backdoor has communicated to the C2 over the DNS protocol.[^5] 	 |
| [[Automated Collection\|T1119]] | Automated Collection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has collected information automatically using the adversary's [USBferry](https://attack.mitre.org/software/S0452) attack.[^5] 	 |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has injected a DLL backdoor into dllhost.exe and svchost.exe.[^3] [^5]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used a copy function to automatically exfiltrate sensitive data from air-gapped systems using USB storage.[^5] 	 |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used `netview` to scan target systems for shared resources.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has detected a target system’s OS version.[^4] [^5]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) can search for anti-virus software running on the system.[^13]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used shellcode with an XOR algorithm to decrypt a payload. [Tropic Trooper](https://attack.mitre.org/groups/G0081) also decrypted image files which contained a payload.[^13] [^5]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has tested if the localhost network is available and other connection capability on an infected system using command scripts.[^5] 	 |
| [[Steganography\|T1027.003]] | Steganography | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used JPG files with encrypted payloads to mask their backdoor routines and evade detection.[^5]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Tropic Trooper](https://attack.mitre.org/groups/G0081)'s backdoor could list the infected system's installed software.[^5]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has attempted to transfer [USBferry](https://attack.mitre.org/software/S0452) from an infected USB device by copying an Autorun function to the target machine.[^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[BITSAdmin\|S0190]] | BITSAdmin | [^3]  |
| [[KeyBoy\|S0387]] | KeyBoy | [^13] [^2]  |
| [[USBferry\|S0452]] | USBferry | [^5]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [^13]  |
| [[YAHOYAH\|S0388]] | YAHOYAH | [^4]  |
| [[ShadowPad\|S0596]] | ShadowPad | [^12]  |



## References

[^1]: Pirate Panda


[^2]: [CitizenLab Tropic Trooper Aug 2018](https://citizenlab.ca/2018/08/familiar-feeling-a-malware-campaign-targeting-the-tibetan-diaspora-resurfaces/)


[^3]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)


[^4]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


[^5]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^6]: [Anomali Pirate Panda April 2020](https://www.anomali.com/blog/anomali-suspects-that-china-backed-apt-pirate-panda-may-be-seeking-access-to-vietnam-government-data-center#When:15:00:00Z)


[^7]: Tropic Trooper


[^8]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^9]: [CitizenLab KeyBoy Nov 2016](https://citizenlab.ca/2016/11/parliament-keyboy/)


[^10]: [Crowdstrike Pirate Panda April 2020](https://www.crowdstrike.com/blog/on-demand-webcast-crowdstrike-experts-on-covid-19-cybersecurity-challenges-and-recommendations/)


[^11]: KeyBoy


[^12]: [Recorded Future RedEcho Feb 2021](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)


[^13]: [Unit 42 Tropic Trooper Nov 2016](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)


