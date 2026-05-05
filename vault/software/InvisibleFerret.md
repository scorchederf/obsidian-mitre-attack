---
aliases: 
    - S1245
    
mitre-attack: https://attack.mitre.org/software/S1245
---

## S1245

[InvisibleFerret](https://attack.mitre.org/software/S1245) is a modular python malware that is leveraged for data exfiltration and remote access capabilities.[^4] [^1] [^6]    [InvisibleFerret](https://attack.mitre.org/software/S1245) consists of four modules: main, payload, browser, and AnyDesk.[^4]   [InvisibleFerret](https://attack.mitre.org/software/S1245) malware has been leveraged by North Korea-affiliated threat actors identified as DeceptiveDevelopment or [Contagious Interview](https://attack.mitre.org/groups/G1052) since 2023.[^2] [^1] [^6] [^5]   [InvisibleFerret](https://attack.mitre.org/software/S1245) has historically been introduced to the victim environment through the use of the [BeaverTail](https://attack.mitre.org/software/S1246) malware.[^3] [^4] [^1] [^6] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Information Discovery\|T1082]] | System Information Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected OS type, hostname and system version through the "pay" module.[^3] [^4]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also queried the victim device using Python scripts to obtain the User and Hostname.[^2] [^6]  |
| [[Financial Theft\|T1657]] | Financial Theft | [InvisibleFerret](https://attack.mitre.org/software/S1245) has searched the victim device credentials and files commonly associated with cryptocurrency wallets.[^3] [^4] [^1] [^6]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has identified specific directories and files for exfiltration using the `ssh_upload` command which contains subcommands of `.sdira`, `sdir`, `sfile`, `sfinda`, `sfindr`, `sfind`.[^4] [^1]  [InvisibleFerret](https://attack.mitre.org/software/S1245) also has the capability to scan and upload files of interest from multiple OS systems through the use of scripts that check file names, file extensions, and avoids certain path names.[^3] [^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized the `findstr` on Windows or the macOS `find` commands to search for files of interest.[^5]   |
| [[Input Capture\|T1056]] | Input Capture | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected mouse and keyboard events using “pyWinhook”.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [InvisibleFerret](https://attack.mitre.org/software/S1245) has decoded XOR-encrypted and Base-64-encoded payloads prior to execution.[^4]  |
| [[Selective Exclusion\|T1679]] | Selective Exclusion | [InvisibleFerret](https://attack.mitre.org/software/S1245) has the capability to scan for file names, file extensions, and avoids pre-designated path names and file types.[^3] [^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [InvisibleFerret](https://attack.mitre.org/software/S1245) has downloaded “AnyDesk.exe” into the user’s home directory from the C2 server when checks for the service fail to identify its presence in the victim environment.[^4]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also been configured to download additional payloads using a command which calls to the /bow URI.[^1] [^6]  |
| [[Software Discovery\|T1518]] | Software Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has gathered installed programs and running processes.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has the capability to query installed programs and running processes.[^1]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also identified running processes using the Python project “psutil”.[^6]  |
| [[Keylogging\|T1056.001]] | Keylogging | [InvisibleFerret](https://attack.mitre.org/software/S1245) has conducted keylogging using the Python project “pyWinHook” and "Pyhook".[^3] [^4] [^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also captured keylogging thread checks for changes in an active window and key presses.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [InvisibleFerret](https://attack.mitre.org/software/S1245) has queried the victim device using Python scripts to obtain the User and Hostname.[^2] [^6]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [InvisibleFerret](https://attack.mitre.org/software/S1245) has stolen login data, autofill data, cryptocurrency wallets, and payment information saved in web browsers such as Chrome, Brave, Opera, Yandex and Edge, to include versions affiliated with major operating systems on Windows, Linux, and macOS.[^3] [^4]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also leveraged the command `ssh_zcp` to copy browser data to include extensions and cryptocurrency wallet data.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected the local IP address, and external IP.[^4] [^6]  |
| [[Service Stop\|T1489]] | Service Stop | [InvisibleFerret](https://attack.mitre.org/software/S1245) has terminated Chrome and Brave browsers using the `taskkill` command on Windows and the `killall` command on other systems such as Linux and macOS.[^4]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also utilized it’s `ssh_kill` command to terminate Chrome and Brave browser processes.[^6]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has identified the user’s UUID and username through the "pay" module.[^3] [^4] [^6]   |
| [[Launch Agent\|T1543.001]] | Launch Agent | [InvisibleFerret](https://attack.mitre.org/software/S1245) has established persistence using LaunchAgents on macOS that run on Startup using a file named “com.avatar.update.wake.plist”.[^1]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | [InvisibleFerret](https://attack.mitre.org/software/S1245) has established persistence within GNOME-based Linux environments by placing entries within `.desktop` that run on Startup.[^1]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized remote access software including AnyDesk client through the “adc” module.[^3] [^4] [^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also downloaded the AnyDesk client should it not already exist on the compromised host by searching for `C:/Program Files(x86)/AnyDesk/AnyDesk.exe`.[^1]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected the internal IP address, IP geolocation information of the infected host and sends the data to a C2 server.[^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also leveraged the “pay” module to obtain region name, country, city, zip code, ISP, latitude and longitude using “http://ip-api.com/json”.[^4]  |
| [[Python\|T1059.006]] | Python | [InvisibleFerret](https://attack.mitre.org/software/S1245) is written in Python and has used Python scripts for execution.[^3] [^2] [^4] [^1] [^6]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [InvisibleFerret](https://attack.mitre.org/software/S1245) has executed Python instances of the browser module “.n2/bow” utilizing the `CREATE_NO_WINDOW` process creation flag.[^4]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [InvisibleFerret](https://attack.mitre.org/software/S1245) has been observed utilizing HTTP communications to the C2 server over ports 1224, 2245 and 8637.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used HTTP communications to the “/Uploads” URI for file exfiltration.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [InvisibleFerret](https://attack.mitre.org/software/S1245) has staged data in consolidated folders prior to exfiltration.[^4]  |
| [[Password Managers\|T1555.005]] | Password Managers | [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized the command `ssh_zcp` to exfiltrate data from browser extensions and password managers via Telegram and FTP.[^4] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used HTTP for C2 communications.[^3] [^4] [^6]   |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used 7zip, RAR and zip files to archive collected data for exfiltration.[^4] [^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [InvisibleFerret](https://attack.mitre.org/software/S1245) has established persistence within Windows devices by creating a .bat file “queue.bat” within the Startup folder to run a Python script.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected data utilizing a script that contained a list of excluded files and directory names and naming patterns of interest such as environment and configuration files, documents, spreadsheets, and other files that contained the words secret, wallet, private, and password.[^4]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [InvisibleFerret](https://attack.mitre.org/software/S1245) has stolen data from the clipboard using the Python project “pyperclip”.[^3] [^4] [^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also captured clipboard contents during copy and paste operations.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized the XOR and Base64 encoding for each of its modules.[^4]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also obfuscated files with a combination of zlib, Base64 and reverse string order.[^3]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also utilized the XOR and Base64 encoding some of its Python scripts.[^6]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used FTP to exfiltrate files and directories using the command `ssh_upload` which contains with six subcommands of `.sdira`, `sdir`, `sfile`, `sfinda`, `sfindr` and `sfind` that had varying functions.[^4] [^1]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has exfiltrated stolen files and data to the C2 servers over ports 1224, 2245 and 8637.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [InvisibleFerret](https://attack.mitre.org/software/S1245) has established a connection with the C2 server over TCP traffic.[^6]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also created a TCP reverse shell communicating via a socket connection over ports 1245, 80, 2245, 3001, and 5000.[^4]  |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | [InvisibleFerret](https://attack.mitre.org/software/S1245) has leveraged Telegram chat to upload stolen data using the Telegram API with a bot token.[^4] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized a PowerShell script created in the victim’s home directory named “conf.ps1” that is used to modify configuration files for AnyDesk remote services.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Contagious Interview\|G1052]] | Contagious Interview |



## References

[^1]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^2]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^3]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^4]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^5]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^6]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


