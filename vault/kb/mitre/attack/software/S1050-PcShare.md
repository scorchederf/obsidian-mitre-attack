---
aliases: 
    - S1050
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S1050-PcShare
---

## Description

[[kb/mitre/attack/software/S1050-PcShare\|PcShare]] is an open source remote access tool that has been modified and used by Chinese threat actors, most notably during the FunnyDream campaign since late 2018.[^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-Data_from_Local_System\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can collect files and information from a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1012-Query_Registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can search the registry files of a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1016-System_Network_Configuration_Discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.[^1]  |
| [[kb/mitre/attack/techniques/T1027.013-Encrypted_Encoded_File\|T1027.013]] | Encrypted／Encoded File | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has been encrypted with XOR using different 32-long Base16 strings.[^1]  |
| [[kb/mitre/attack/techniques/T1027.015-Compression\|T1027.015]] | Compression | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has been compressed with LZW algorithm.[^1]  |
| [[kb/mitre/attack/techniques/T1036.001-Invalid_Code_Signature\|T1036.001]] | Invalid Code Signature | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has used an invalid certificate in attempt to appear legitimate.[^1]  |
| [[kb/mitre/attack/techniques/T1036.005-Match_Legitimate_Resource_Name_or_Location\|T1036.005]] | Match Legitimate Resource Name or Location | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has been named `wuauclt.exe` to appear as the legitimate Windows Update AutoUpdate Client.[^1]  |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can upload files and information from a compromised host to its C2 servers.[^1]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | The [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has the ability to capture keystrokes.[^1]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can obtain a list of running processes on a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can execute `cmd` commands on a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1070.004-File_Deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has deleted its files and components from a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-Web_Protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has used HTTP for C2 communication.[^1]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has used a variety of Windows API functions.[^1]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can delete its persistence mechanisms from the registry.[^1]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can take screen shots of a compromised machine.[^1]  |
| [[kb/mitre/attack/techniques/T1125-Video_Capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can capture camera video as part of its collection process.[^1]  |
| [[kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information\|T1140]] | Deobfuscate／Decode Files or Information | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm.[^1]  |
| [[kb/mitre/attack/techniques/T1218.011-Rundll32\|T1218.011]] | Rundll32 | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has used `rundll32.exe` for execution.[^1]  |
| [[kb/mitre/attack/techniques/T1546.015-Component_Object_Model_Hijacking\|T1546.015]] | Component Object Model Hijacking | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] has created the `HKCU\\Software\\Classes\\CLSID\\{42aedc87-2188-41fd-b9a3-0c966feabec1}\\InprocServer32` Registry key for persistence.[^1]  |





> [!info]- References
> [^1]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^2]: [GitHub PcShare 2014](https://github.com/LiveMirror/pcshare)


