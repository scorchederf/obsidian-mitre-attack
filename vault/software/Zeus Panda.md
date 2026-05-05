---
aliases: 
    - S0330
    
mitre-attack: https://attack.mitre.org/software/S0330
---

## S0330

[Zeus Panda](https://attack.mitre.org/software/S0330) is a Trojan designed to steal banking information and other sensitive credentials for exfiltration. [Zeus Panda](https://attack.mitre.org/software/S0330)’s original source code was leaked in 2011, allowing threat actors to use its source code as a basis for new malware variants. It is mainly used to target Windows operating systems ranging from Windows XP through Windows 10.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [Zeus Panda](https://attack.mitre.org/software/S0330) hooks processes by leveraging its own IAT hooked functions.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Zeus Panda](https://attack.mitre.org/software/S0330) uses PowerShell to download and execute the payload.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) checks to see if anti-virus, anti-spyware, or firewall products are installed in the victim’s environment.[^1] [^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) checks for running processes on the victim’s machine.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Zeus Panda](https://attack.mitre.org/software/S0330) can take screenshots of the victim’s machine.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Zeus Panda](https://attack.mitre.org/software/S0330) can download additional malware plug-in modules and execute them on the victim’s machine.[^2]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Zeus Panda](https://attack.mitre.org/software/S0330) can launch remote scripts on the victim’s machine.[^2] 	 |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) collects the current system time (UTC) and sends it back to the C2 server.[^2]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) queries the system's keyboard mapping to determine the language used on the system. It will terminate execution if it detects LANG_RUSSIAN, LANG_BELARUSIAN, LANG_KAZAK, or LANG_UKRAINIAN.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Zeus Panda](https://attack.mitre.org/software/S0330) modifies several Registry keys under `HKCU\Software\Microsoft\Internet Explorer\ PhishingFilter\` to disable phishing filters.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Zeus Panda](https://attack.mitre.org/software/S0330) uses HTTP for C2 communications.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Zeus Panda](https://attack.mitre.org/software/S0330) has a command to delete a file. It also can uninstall scripts and delete files to cover its track.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Zeus Panda](https://attack.mitre.org/software/S0330) encrypts strings with XOR. [Zeus Panda](https://attack.mitre.org/software/S0330) also encrypts all configuration and settings in AES and RC4.[^1] [^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Zeus Panda](https://attack.mitre.org/software/S0330) obfuscates the macro commands in its initial payload.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Zeus Panda](https://attack.mitre.org/software/S0330) can launch an interface where it can execute several commands on the victim’s PC.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Zeus Panda](https://attack.mitre.org/software/S0330) can hook GetClipboardData function to watch for clipboard pastes to collect.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Zeus Panda](https://attack.mitre.org/software/S0330) checks for the existence of a Registry key and if it contains certain values.[^2]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Zeus Panda](https://attack.mitre.org/software/S0330) checks processes on the system and if they meet the necessary requirements, it injects into that process.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) collects the OS version, system architecture, computer name, product ID, install date, and information on the keyboard mapping to determine the language used on the system.[^1] [^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Zeus Panda](https://attack.mitre.org/software/S0330) adds persistence by creating Registry Run keys.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Zeus Panda](https://attack.mitre.org/software/S0330) can perform keylogging on the victim’s machine by hooking the functions TranslateMessage and WM_KEYDOWN.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Zeus Panda](https://attack.mitre.org/software/S0330) decrypts strings in the code during the execution process.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Zeus Panda](https://attack.mitre.org/software/S0330) searches for specific directories on the victim’s machine.[^2]  |




## References

[^1]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)


[^2]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^3]: Zeus Panda


