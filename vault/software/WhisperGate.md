---
aliases: 
    - S0689
    
mitre-attack: https://attack.mitre.org/software/S0689
---

## S0689

[WhisperGate](https://attack.mitre.org/software/S0689) is a multi-stage wiper designed to look like ransomware that has been used against multiple government, non-profit, and information technology organizations in Ukraine since at least January 2022.[^2] [^8] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bootkit\|T1542.003]] | Bootkit | [WhisperGate](https://attack.mitre.org/software/S0689) overwrites the MBR with a bootloader component that performs destructive wiping operations on hard drives and displays a fake ransom note when the host boots.[^3] [^2] [^7] [^9] [^4]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [WhisperGate](https://attack.mitre.org/software/S0689)'s downloader can reverse its third stage file bytes and reflectively load the file as a .NET assembly.[^5]  |
| [[Data Destruction\|T1485]] | Data Destruction | [WhisperGate](https://attack.mitre.org/software/S0689) can corrupt files by overwriting the first 1 MB with `0xcc` and appending random extensions.[^7] [^3] [^2] [^8] [^9] [^4]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [WhisperGate](https://attack.mitre.org/software/S0689) can download and execute AdvancedRun.exe to disable the Windows Defender Theat Protection service and set an exclusion path for the C:\ drive.[^8] [^9] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [WhisperGate](https://attack.mitre.org/software/S0689) can locate files based on hardcoded file extensions.[^7] [^8] [^9] [^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [WhisperGate](https://attack.mitre.org/software/S0689) can use PowerShell to support multiple actions including execution and defense evasion.[^8] [^9] [^4]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | [WhisperGate](https://attack.mitre.org/software/S0689) has used `InstallUtil.exe` as part of its process to disable Windows Defender.[^8]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [WhisperGate](https://attack.mitre.org/software/S0689) can Base64 encode strings, store downloaded files in reverse byte order,  and use the Eazfuscator tool to obfuscate its third stage.[^9] [^4] [^5]  |
| [[Native API\|T1106]] | Native API | [WhisperGate](https://attack.mitre.org/software/S0689) has used the `ExitWindowsEx` to flush file buffers to disk and stop running processes and other API calls.[^9] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [WhisperGate](https://attack.mitre.org/software/S0689) can make an HTTPS connection to download additional files.[^8] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [WhisperGate](https://attack.mitre.org/software/S0689) can delete tools from a compromised host after execution.[^9]  |
| [[Disk Structure Wipe\|T1561.002]] | Disk Structure Wipe | [WhisperGate](https://attack.mitre.org/software/S0689) can overwrite the Master Book Record (MBR) on victim systems with a malicious 16-bit bootloader.[^7] [^3] [^2] [^8] [^9] [^4]  |
| [[Disk Content Wipe\|T1561.001]] | Disk Content Wipe | [WhisperGate](https://attack.mitre.org/software/S0689) can overwrite sectors of a victim host's hard drive at periodic offsets.[^3] [^9] [^4]  |
| [[System Checks\|T1497.001]] | System Checks | [WhisperGate](https://attack.mitre.org/software/S0689) can stop its execution when it recognizes the presence of certain monitoring tools.[^8]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [WhisperGate](https://attack.mitre.org/software/S0689) can recognize the presence of monitoring tools on a target system.[^8]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [WhisperGate](https://attack.mitre.org/software/S0689) can enumerate connected remote logical drives.[^9]  |
| [[Service Execution\|T1569.002]] | Service Execution | [WhisperGate](https://attack.mitre.org/software/S0689) can download and execute AdvancedRun.exe via `sc.exe`.[^4] [^8]  |
| [[System Shutdown／Reboot\|T1529]] | System Shutdown／Reboot | [WhisperGate](https://attack.mitre.org/software/S0689) can shutdown a compromised host through execution of `ExitWindowsEx` with the `EXW_SHUTDOWN` flag.[^9]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [WhisperGate](https://attack.mitre.org/software/S0689) has the ability to inject its fourth stage into a suspended process created by the legitimate Windows utility `InstallUtil.exe`.[^9] [^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [WhisperGate](https://attack.mitre.org/software/S0689) can use `cmd.exe` to execute commands.[^8]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [WhisperGate](https://attack.mitre.org/software/S0689) can use a Visual Basic script to exclude the `C:\` drive from Windows Defender.[^8] [^9]  |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | The [WhisperGate](https://attack.mitre.org/software/S0689) third stage can use the AdvancedRun.exe tool to execute commands in the context of the Windows TrustedInstaller group via `%TEMP%\AdvancedRun.exe" /EXEFilename "C:\Windows\System32\sc.exe" /WindowState 0 /CommandLine "stop WinDefend" /StartDirectory "" /RunAs 8 /Run`.[^9]  |
| [[Web Service\|T1102]] | Web Service | [WhisperGate](https://attack.mitre.org/software/S0689) can download additional payloads hosted on a Discord channel.[^3] [^8] [^7] [^9] [^4]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [WhisperGate](https://attack.mitre.org/software/S0689) has the ability to enumerate fixed logical drives on a targeted system.[^9]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [WhisperGate](https://attack.mitre.org/software/S0689) can pause for 20 seconds to bypass antivirus solutions.[^4] [^5]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [WhisperGate](https://attack.mitre.org/software/S0689) can deobfuscate downloaded files stored in reverse byte order and decrypt embedded resources using multiple XOR operations.[^9] [^4]  |
| [[Masquerading\|T1036]] | Masquerading | [WhisperGate](https://attack.mitre.org/software/S0689) has been disguised as a JPG extension to avoid detection as a malicious PE file.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [WhisperGate](https://attack.mitre.org/software/S0689) can download additional stages of malware from a Discord CDN channel.[^7] [^8] [^9] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Ember Bear\|G1003]] | Ember Bear |



## References

[^1]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^2]: [Cybereason WhisperGate February 2022](https://www.cybereason.com/blog/cybereason-vs.-whispergate-wiper)


[^3]: [Crowdstrike WhisperGate January 2022](https://www.crowdstrike.com/blog/technical-analysis-of-whispergate-malware)


[^4]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)


[^5]: [RecordedFuture WhisperGate Jan 2022](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)


[^6]: [CrowdStrike Ember Bear Profile March 2022](https://www.crowdstrike.com/blog/who-is-ember-bear/)


[^7]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)


[^8]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)


[^9]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)


[^10]: [Mandiant UNC2589 March 2022](https://www.mandiant.com/resources/russia-invasion-ukraine-retaliation)


