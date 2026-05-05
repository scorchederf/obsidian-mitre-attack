---
aliases: 
    - S0387
    
mitre-attack: https://attack.mitre.org/software/S0387
---

## S0387

[KeyBoy](https://attack.mitre.org/software/S0387) is malware that has been used in targeted campaigns against members of the Tibetan Parliament in 2016.[^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [KeyBoy](https://attack.mitre.org/software/S0387) can determine the public or WAN IP address for the system.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [KeyBoy](https://attack.mitre.org/software/S0387) can gather extended system information, such as information about the operating system and memory.[^2] [^5]  |
| [[Windows Service\|T1543.003]] | Windows Service | [KeyBoy](https://attack.mitre.org/software/S0387) installs a service pointing to a malicious DLL dropped to disk.[^5]  |
| [[Python\|T1059.006]] | Python | [KeyBoy](https://attack.mitre.org/software/S0387) uses Python scripts for installing files and performing execution.[^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [KeyBoy](https://attack.mitre.org/software/S0387) uses `-w Hidden` to conceal a [PowerShell](https://attack.mitre.org/techniques/T1059/001) window that downloads a payload. [^2]  |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [KeyBoy](https://attack.mitre.org/software/S0387) uses custom SSL libraries to impersonate SSL in C2 traffic.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [KeyBoy](https://attack.mitre.org/software/S0387) installs a keylogger for intercepting credentials and keystrokes.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | In one version of [KeyBoy](https://attack.mitre.org/software/S0387), string obfuscation routines were used to hide many of the critical values referenced in the malware.[^3]  |
| [[Timestomp\|T1070.006]] | Timestomp | [KeyBoy](https://attack.mitre.org/software/S0387) time-stomped its DLL in order to evade detection.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [KeyBoy](https://attack.mitre.org/software/S0387) has a download and upload functionality.[^2] [^5]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [KeyBoy](https://attack.mitre.org/software/S0387) has a command to launch a file browser or explorer on the system.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [KeyBoy](https://attack.mitre.org/software/S0387) uses VBS scripts for installing files and performing execution.[^3]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [KeyBoy](https://attack.mitre.org/software/S0387) uses the Dynamic Data Exchange (DDE) protocol to download remote payloads.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [KeyBoy](https://attack.mitre.org/software/S0387) uses PowerShell commands to download and execute payloads.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [KeyBoy](https://attack.mitre.org/software/S0387) has a command to perform screen grabbing.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [KeyBoy](https://attack.mitre.org/software/S0387) can launch interactive shells for communicating with the victim machine.[^2] [^5]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [KeyBoy](https://attack.mitre.org/software/S0387) attempts to collect passwords from browsers.[^5]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | [KeyBoy](https://attack.mitre.org/software/S0387) issues the command `reg add “HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon”` to achieve persistence.[^2]  [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Tropic Trooper\|G0081]] | Tropic Trooper |



## References

[^1]: [CitizenLab Tropic Trooper Aug 2018](https://citizenlab.ca/2018/08/familiar-feeling-a-malware-campaign-targeting-the-tibetan-diaspora-resurfaces/)


[^2]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^3]: [CitizenLab KeyBoy Nov 2016](https://citizenlab.ca/2016/11/parliament-keyboy/)


[^4]: KeyBoy


[^5]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)


[^6]: [Unit 42 Tropic Trooper Nov 2016](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)


