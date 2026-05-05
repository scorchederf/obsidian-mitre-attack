---
aliases: 
    - APT37
    - InkySquid
    - ScarCruft
    - Reaper
    - Group123
    - TEMP.Reaper
    - Ricochet Chollima
mitre-attack: https://attack.mitre.org/groups/G0067
---

## G0067

[APT37](https://attack.mitre.org/groups/G0067) is a North Korean state-sponsored cyber espionage group that has been active since at least 2012. The group has targeted victims primarily in South Korea, but also in Japan, Vietnam, Russia, Nepal, China, India, Romania, Kuwait, and other parts of the Middle East. [APT37](https://attack.mitre.org/groups/G0067) has also been linked to the following campaigns between 2016-2018: Operation Daybreak, Operation Erebus, Golden Time, Evil New Year, Are you Happy?, FreeMilk, North Korean Human Rights, and Evil New Year 2018.[^7] [^9] [^5] <br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups.

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [APT37](https://attack.mitre.org/groups/G0067)'s has added persistence via the Registry key `HKCU\Software\Microsoft\CurrentVersion\Run\`.[^7] [^5]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [APT37](https://attack.mitre.org/groups/G0067) has a Bluetooth device harvester, which uses Windows Bluetooth APIs to find information on connected Bluetooth devices. [^11]  |
| [[Python\|T1059.006]] | Python | [APT37](https://attack.mitre.org/groups/G0067) has used Python scripts to execute payloads.[^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [APT37](https://attack.mitre.org/groups/G0067) has downloaded second stage malware from compromised websites.[^7] [^11] [^12] [^8]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT37](https://attack.mitre.org/groups/G0067) uses HTTPS to conceal C2 communications.[^5]  |
| [[Steganography\|T1027.003]] | Steganography | [APT37](https://attack.mitre.org/groups/G0067) uses steganography to send images to users that are embedded with shellcode.[^5] [^11]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [APT37](https://attack.mitre.org/groups/G0067) leverages social networking sites and cloud platforms (AOL, Twitter, Yandex, Mediafire, pCloud, Dropbox, and Box) for C2.[^7] [^5]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT37](https://attack.mitre.org/groups/G0067) collects the computer name, the BIOS model, and execution path.[^5]  |
| [[Malicious File\|T1204.002]] | Malicious File | [APT37](https://attack.mitre.org/groups/G0067) has sent spearphishing attachments attempting to get a user to open them.[^7]  |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | [APT37](https://attack.mitre.org/groups/G0067) has signed its malware with an invalid digital certificates listed as “Tencent Technology (Shenzhen) Company Limited.”[^9]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [APT37](https://attack.mitre.org/groups/G0067) has a function in the initial dropper to bypass Windows UAC in order to execute the next payload with higher privileges.[^11]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [APT37](https://attack.mitre.org/groups/G0067) identifies the victim username.[^5]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [APT37](https://attack.mitre.org/groups/G0067) has used a credential stealer known as ZUMKONG that can harvest usernames and passwords stored in browsers.[^7]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [APT37](https://attack.mitre.org/groups/G0067) has used malware that will issue the command `shutdown /r /t 1` to reboot a system after wiping its MBR.[^5]  |
| [[Data from Local System\|T1005]] | Data from Local System | [APT37](https://attack.mitre.org/groups/G0067) has collected data from victims' local systems.[^7]  |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [APT37](https://attack.mitre.org/groups/G0067) has used Windows DDE for execution of commands and a malicious VBS.[^9]  |
| [[Native API\|T1106]] | Native API | [APT37](https://attack.mitre.org/groups/G0067) leverages the Windows API calls: VirtualAlloc(), WriteProcessMemory(), and CreateRemoteThread() for process injection.[^5]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [APT37](https://attack.mitre.org/groups/G0067) has used exploits for Flash Player (CVE-2016-4117, CVE-2018-4878), Word (CVE-2017-0199), Internet Explorer (CVE-2020-1380 and CVE-2020-26411), and Microsoft Edge (CVE-2021-26411) for execution.[^9] [^7] [^5] [^12]  |
| [[Process Injection\|T1055]] | Process Injection | [APT37](https://attack.mitre.org/groups/G0067) injects its malware variant, [ROKRAT](https://attack.mitre.org/software/S0240), into the cmd.exe process.[^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [APT37](https://attack.mitre.org/groups/G0067) obfuscates strings and payloads.[^5] [^11] [^8]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [APT37](https://attack.mitre.org/groups/G0067) has used strategic web compromises, particularly of South Korean websites, to distribute malware. The group has also used torrent file-sharing sites to more indiscriminately disseminate malware to victims. As part of their compromises, the group has used a Javascript based profiler called RICECURRY to profile a victim's web browser and deliver malicious code accordingly.[^9] [^7] [^12]  |
| [[Process Discovery\|T1057]] | Process Discovery | [APT37](https://attack.mitre.org/groups/G0067)'s Freenki malware lists running processes using the Microsoft Windows API.[^5]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [APT37](https://attack.mitre.org/groups/G0067) has used Ruby scripts to execute payloads.[^8]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [APT37](https://attack.mitre.org/groups/G0067) has used the command-line interface.[^7] [^5]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [APT37](https://attack.mitre.org/groups/G0067) delivers malware using spearphishing emails with malicious HWP attachments.[^7] [^5] [^11]  |
| [[Audio Capture\|T1123]] | Audio Capture | [APT37](https://attack.mitre.org/groups/G0067) has used an audio capturing utility known as SOUNDWAVE that captures microphone input.[^7]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT37](https://attack.mitre.org/groups/G0067) executes shellcode and a VBA script to decode Base64 strings.[^5]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT37](https://attack.mitre.org/groups/G0067) has created scheduled tasks to run malicious scripts on a compromised host.[^8]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [APT37](https://attack.mitre.org/groups/G0067) has access to destructive malware that is capable of overwriting a machine's Master Boot Record (MBR).[^7] [^5]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[DOGCALL\|S0213]] | DOGCALL | [^7] [^10]  |
| [[HAPPYWORK\|S0214]] | HAPPYWORK | [^7]  |
| [[KARAE\|S0215]] | KARAE | [^7]  |
| [[SLOWDRIFT\|S0218]] | SLOWDRIFT | [^7]  |
| [[SHUTTERSPEED\|S0217]] | SHUTTERSPEED | [^7]  |
| [[WINERACK\|S0219]] | WINERACK | [^7]  |
| [[NavRAT\|S0247]] | NavRAT | [^13]  |
| [[POORAIM\|S0216]] | POORAIM | [^7]  |
| [[ROKRAT\|S0240]] | ROKRAT | [^5] [^11]  |
| [[CORALDECK\|S0212]] | CORALDECK | [^7]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [^12]  |
| [[Final1stspy\|S0355]] | Final1stspy | [^10]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [^12]  |



## References

[^1]: TEMP.Reaper


[^2]: Group123


[^3]: Reaper


[^4]: [CrowdStrike Richochet Chollima September 2021](https://www.crowdstrike.com/adversaries/ricochet-chollima/)


[^5]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^6]: APT37


[^7]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^8]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^9]: [Securelist ScarCruft Jun 2016](https://securelist.com/operation-daybreak/75100/)


[^10]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^11]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^12]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^13]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


[^14]: Ricochet Chollima


[^15]: InkySquid


[^16]: ScarCruft


