---
aliases: 
    - S0561
    
mitre-attack: https://attack.mitre.org/software/S0561
---

## S0561

[GuLoader](https://attack.mitre.org/software/S0561) is a file downloader that has been used since at least December 2019 to distribute a variety of remote administration tool (RAT) malware, including [NETWIRE](https://attack.mitre.org/software/S0198), [Agent Tesla](https://attack.mitre.org/software/S0331), [NanoCore](https://attack.mitre.org/software/S0336), FormBook, and Parallax RAT.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [GuLoader](https://attack.mitre.org/software/S0561) has been spread in phishing campaigns using malicious web links.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [GuLoader](https://attack.mitre.org/software/S0561) has the ability to inject shellcode into a donor processes that is started in a suspended state. [GuLoader](https://attack.mitre.org/software/S0561) has previously used RegAsm as a donor process.[^2]  |
| [[System Checks\|T1497.001]] | System Checks | [GuLoader](https://attack.mitre.org/software/S0561) has the ability to perform anti-VM and anti-sandbox checks using string hashing, the API call `EnumWindows`, and checking for Qemu guest agent.[^2]  |
| [[Native API\|T1106]] | Native API | [GuLoader](https://attack.mitre.org/software/S0561) can use a number of different APIs for discovery and execution.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [GuLoader](https://attack.mitre.org/software/S0561) can delete its executable from the `AppData\Local\Temp` directory on the compromised host.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GuLoader](https://attack.mitre.org/software/S0561) can download further malware for execution on the victim's machine.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GuLoader](https://attack.mitre.org/software/S0561) can use HTTP to retrieve additional binaries.[^1] [^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [GuLoader](https://attack.mitre.org/software/S0561) has relied upon users clicking on links to malicious documents.[^1]  |
| [[Web Service\|T1102]] | Web Service | [GuLoader](https://attack.mitre.org/software/S0561) has the ability to download malware from Google Drive.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [GuLoader](https://attack.mitre.org/software/S0561) can establish persistence via the Registry under `HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce`.[^1]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [GuLoader](https://attack.mitre.org/software/S0561) has the ability to perform anti-debugging based on time checks, API calls, and CPUID.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | The [GuLoader](https://attack.mitre.org/software/S0561) executable has been retrieved via embedded macros in malicious Word documents.[^1]  |




## References

[^1]: [Unit 42 NETWIRE April 2020](https://unit42.paloaltonetworks.com/guloader-installing-netwire-rat/)


[^2]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)


