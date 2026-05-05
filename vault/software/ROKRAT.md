---
aliases: 
    - S0240
    
mitre-attack: https://attack.mitre.org/software/S0240
---

## S0240

[ROKRAT](https://attack.mitre.org/software/S0240) is a cloud-based remote access tool (RAT) used by [APT37](https://attack.mitre.org/groups/G0067) to target victims in South Korea. [APT37](https://attack.mitre.org/groups/G0067) has used ROKRAT during several campaigns from 2016 through 2021.[^4] [^1] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [ROKRAT](https://attack.mitre.org/software/S0240) can modify the `HKEY_CURRENT_USER\Software\Microsoft\Office\` registry key so it can bypass the VB object model (VBOM) on a compromised host.[^3]  |
| [[Audio Capture\|T1123]] | Audio Capture | [ROKRAT](https://attack.mitre.org/software/S0240) has an audio capture and eavesdropping module.[^6]  |
| [[Query Registry\|T1012]] | Query Registry | [ROKRAT](https://attack.mitre.org/software/S0240) can access the `HKLM\System\CurrentControlSet\Services\mssmbios\Data\SMBiosData` Registry key to obtain the System manufacturer value to identify the machine type.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [ROKRAT](https://attack.mitre.org/software/S0240) can steal credentials stored in Web browsers by querying the sqlite database.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [ROKRAT](https://attack.mitre.org/software/S0240) can use  `SetWindowsHookEx` and `GetKeyNameText` to capture keystrokes.[^4] [^7]  |
| [[Native API\|T1106]] | Native API | [ROKRAT](https://attack.mitre.org/software/S0240) can use a variety of API calls to execute shellcode.[^3]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [ROKRAT](https://attack.mitre.org/software/S0240) can check for debugging tools.[^1] [^5] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ROKRAT](https://attack.mitre.org/software/S0240) can list the current running processes on the system.[^4] [^5]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ROKRAT](https://attack.mitre.org/software/S0240) can request to delete files.[^5] 	 |
| [[Visual Basic\|T1059.005]] | Visual Basic | [ROKRAT](https://attack.mitre.org/software/S0240) has used Visual Basic for execution.[^3]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [ROKRAT](https://attack.mitre.org/software/S0240) can steal credentials by leveraging the Windows Vault mechanism.[^1]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [ROKRAT](https://attack.mitre.org/software/S0240) relies on a specific victim hostname to execute and decrypt important strings.[^7]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [ROKRAT](https://attack.mitre.org/software/S0240) can send collected files back over same C2 channel.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [ROKRAT](https://attack.mitre.org/software/S0240) has been delivered via spearphishing emails that contain a malicious Hangul Office or Microsoft Word document.[^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [ROKRAT](https://attack.mitre.org/software/S0240) can extract clipboard data from a compromised host.[^7]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [ROKRAT](https://attack.mitre.org/software/S0240) can encrypt data prior to exfiltration by using an RSA public key.[^7] [^3]  |
| [[System Checks\|T1497.001]] | System Checks | [ROKRAT](https://attack.mitre.org/software/S0240) can check for VMware-related files and DLLs related to sandboxes.[^1] [^5] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ROKRAT](https://attack.mitre.org/software/S0240) has the ability to gather a list of files and directories on the infected system.[^6] [^5] [^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ROKRAT](https://attack.mitre.org/software/S0240) can retrieve additional malicious payloads from its C2 server.[^4] [^5] [^7] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ROKRAT](https://attack.mitre.org/software/S0240) can decrypt strings using the victim's hostname as the key.[^7] [^3]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [ROKRAT](https://attack.mitre.org/software/S0240) has used legitimate social networking sites and cloud platforms (including but not limited to Twitter, Yandex, Dropbox, and Mediafire) for C2 communications.[^4] [^6] [^7]  |
| [[Screen Capture\|T1113]] | Screen Capture | [ROKRAT](https://attack.mitre.org/software/S0240) can capture screenshots of the infected system using the `gdi32` library.[^4] [^2] [^6] [^5] [^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ROKRAT](https://attack.mitre.org/software/S0240) can collect the username from a compromised host.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [ROKRAT](https://attack.mitre.org/software/S0240) can use `VirtualAlloc`, `WriteProcessMemory`, and then `CreateRemoteThread` to execute shellcode within the address space of `Notepad.exe`.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ROKRAT](https://attack.mitre.org/software/S0240) can gather the hostname and the OS version to ensure it doesn’t run on a Windows XP or Windows Server 2003 systems.[^4] [^2] [^6] [^5] [^7] [^3]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [ROKRAT](https://attack.mitre.org/software/S0240) can use  the `GetForegroundWindow` and `GetWindowText` APIs to discover where the user is typing.[^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [ROKRAT](https://attack.mitre.org/software/S0240) can collect host data and specific file types.[^5] [^7] [^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [ROKRAT](https://attack.mitre.org/software/S0240) has relied upon users clicking on a malicious attachment delivered through spearphishing.[^3]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [ROKRAT](https://attack.mitre.org/software/S0240) can send collected data to cloud storage services such as PCloud.[^3] [^7]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ROKRAT](https://attack.mitre.org/software/S0240) can use HTTP and HTTPS for command and control communication.[^4] [^5] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^2]: [Talos ROKRAT 2](https://blog.talosintelligence.com/2017/11/ROKRAT-Reloaded.html)


[^3]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^4]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)


[^5]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^6]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^7]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^8]: ROKRAT


