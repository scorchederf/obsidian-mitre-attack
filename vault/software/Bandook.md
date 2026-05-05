---
aliases: 
    - S0234
    
mitre-attack: https://attack.mitre.org/software/S0234
---

## S0234

[Bandook](https://attack.mitre.org/software/S0234) is a commercially available RAT, written in Delphi and C++, that has been available since at least 2007. It has been used against government, financial, energy, healthcare, education, IT, and legal organizations in the US, South America, Europe, and Southeast Asia. [Bandook](https://attack.mitre.org/software/S0234) has been used by [Dark Caracal](https://attack.mitre.org/groups/G0070), as well as in a separate campaign referred to as "Operation Manul".[^1] [^2] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Audio Capture\|T1123]] | Audio Capture | [Bandook](https://attack.mitre.org/software/S0234) has modules that are capable of capturing audio.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Bandook](https://attack.mitre.org/software/S0234) can upload files from a victim's machine over the C2 channel.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Bandook](https://attack.mitre.org/software/S0234) is capable of spawning a Windows command shell.[^1] [^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Bandook](https://attack.mitre.org/software/S0234) contains keylogging capabilities.[^4]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Bandook](https://attack.mitre.org/software/S0234) has been launched by starting iexplore.exe and replacing it with [Bandook](https://attack.mitre.org/software/S0234)'s payload.[^2] [^1] [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bandook](https://attack.mitre.org/software/S0234) can download files to the system.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Bandook](https://attack.mitre.org/software/S0234) can detect USB devices.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [Bandook](https://attack.mitre.org/software/S0234) has used .PNG images within a zip file to build the executable. [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Bandook](https://attack.mitre.org/software/S0234) has a command to list files on a system.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Bandook](https://attack.mitre.org/software/S0234) has a command built in to use a raw TCP socket.[^3]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Bandook](https://attack.mitre.org/software/S0234) is delivered via a malicious Word document inside a zip file.[^3]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Bandook](https://attack.mitre.org/software/S0234) can support commands to execute Java-based payloads.[^3]   |
| [[Screen Capture\|T1113]] | Screen Capture | [Bandook](https://attack.mitre.org/software/S0234) is capable of taking an image of and uploading the current desktop.[^2] [^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Bandook](https://attack.mitre.org/software/S0234) has a command to get the public IP address from a system.[^3]   |
| [[PowerShell\|T1059.001]] | PowerShell | [Bandook](https://attack.mitre.org/software/S0234) has used PowerShell loaders as part of execution.[^3]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Bandook](https://attack.mitre.org/software/S0234) can collect information about the drives available on the system.[^3]   |
| [[Malicious File\|T1204.002]] | Malicious File | [Bandook](https://attack.mitre.org/software/S0234) has used lure documents to convince the user to enable macros.[^3]   |
| [[Native API\|T1106]] | Native API | [Bandook](https://attack.mitre.org/software/S0234) has used the ShellExecuteW() function call.[^3]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Bandook](https://attack.mitre.org/software/S0234) has used malicious VBA code against the target system.[^3]  |
| [[Video Capture\|T1125]] | Video Capture | [Bandook](https://attack.mitre.org/software/S0234) has modules that are capable of capturing video from a victim's webcam.[^1]  |
| [[Python\|T1059.006]] | Python | [Bandook](https://attack.mitre.org/software/S0234) can support commands to execute Python-based payloads.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Bandook](https://attack.mitre.org/software/S0234) has a command to delete a file.[^3]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Bandook](https://attack.mitre.org/software/S0234) has used AES encryption for C2 communication.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bandook](https://attack.mitre.org/software/S0234) has decoded its PowerShell script.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Bandook](https://attack.mitre.org/software/S0234) can collect local files from the system .[^3]   |
| [[Code Signing\|T1553.002]] | Code Signing | [Bandook](https://attack.mitre.org/software/S0234) was signed with valid Certum certificates.[^3]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dark Caracal\|G0070]] | Dark Caracal |



## References

[^1]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)


[^2]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^3]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^4]: [BH Manul Aug 2016](https://www.blackhat.com/docs/us-16/materials/us-16-Quintin-When-Governments-Attack-State-Sponsored-Malware-Attacks-Against-Activists-Lawyers-And-Journalists.pdf)


