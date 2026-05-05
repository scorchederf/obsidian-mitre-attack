---
aliases: 
    - S0409
    
mitre-attack: https://attack.mitre.org/software/S0409
---

## S0409

[Machete](https://attack.mitre.org/software/S0409) is a cyber espionage toolset used by [Machete](https://attack.mitre.org/groups/G0095). It is a Python-based backdoor targeting Windows machines that was first observed in 2010.[^6] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Machete](https://attack.mitre.org/software/S0409)’s downloaded data is decrypted using AES.[^6]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Machete](https://attack.mitre.org/software/S0409) has used AES to exfiltrate documents.[^6]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Machete](https://attack.mitre.org/software/S0409) has scanned and looked for cryptographic keys and certificate file extensions.[^6]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Machete](https://attack.mitre.org/software/S0409)'s collected data is exfiltrated over the same channel used for C2.[^6]  |
| [[File Deletion\|T1070.004]] | File Deletion | Once a file is uploaded, [Machete](https://attack.mitre.org/software/S0409) will delete it from the machine.[^6]   |
| [[Process Discovery\|T1057]] | Process Discovery | [Machete](https://attack.mitre.org/software/S0409) has a component to check for running processes to look for web browsers.[^6]   |
| [[Video Capture\|T1125]] | Video Capture | [Machete](https://attack.mitre.org/software/S0409) takes photos from the computer’s web camera.[^2] [^5] [^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Machete](https://attack.mitre.org/software/S0409) has been packed with NSIS.[^6]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | The different components of [Machete](https://attack.mitre.org/software/S0409) are executed by Windows Task Scheduler.[^6] [^2]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Machete](https://attack.mitre.org/software/S0409) retrieves the user profile data (e.g., browsers) from Chrome and Firefox browsers.[^6]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Machete](https://attack.mitre.org/software/S0409) collects stored credentials from several web browsers.[^6]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Machete](https://attack.mitre.org/software/S0409) has used base64 encoding.[^2]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Machete](https://attack.mitre.org/software/S0409) uses FTP for Command & Control.[^6] [^5] [^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Machete](https://attack.mitre.org/software/S0409) collects the MAC address of the target computer and other network configuration information.[^6] [^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Machete](https://attack.mitre.org/software/S0409) renamed task names to masquerade as legitimate Google Chrome, Java, Dropbox, Adobe Reader and Python tasks.[^6]   |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Machete](https://attack.mitre.org/software/S0409)’s collected files are exfiltrated automatically to remote servers.[^6]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Machete](https://attack.mitre.org/software/S0409) renamed payloads to masquerade as legitimate Google Chrome, Java, Dropbox, Adobe Reader and Python executables.[^6] [^2]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [Machete](https://attack.mitre.org/software/S0409) sends stolen data to the C2 server every 10 minutes.[^6]   |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Machete](https://attack.mitre.org/software/S0409) stores files and logs in a folder on the local drive.[^6] [^5]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Machete](https://attack.mitre.org/software/S0409) hijacks the clipboard data by creating an overlapped window that listens to keyboard events.[^6] [^2]   |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Machete](https://attack.mitre.org/software/S0409) used the startup folder for persistence.[^2] [^5]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Machete](https://attack.mitre.org/software/S0409) captures audio from the computer’s microphone.[^2] [^5] [^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Machete](https://attack.mitre.org/software/S0409) uses HTTP for Command & Control.[^6] [^5] [^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Machete](https://attack.mitre.org/software/S0409) saves the window names.[^6]   |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Machete](https://attack.mitre.org/software/S0409)'s collected data is encrypted with AES before exfiltration.[^6]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer |  [Machete](https://attack.mitre.org/software/S0409) can download additional files for execution on the victim’s machine.[^6]   |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | [Machete](https://attack.mitre.org/software/S0409) can find, encrypt, and upload files from fixed and removable drives.[^5] [^6]   |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | [Machete](https://attack.mitre.org/software/S0409) has a feature to copy files from every drive onto a removable drive in a hidden folder.[^6] [^2]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Machete](https://attack.mitre.org/software/S0409) has used TLS-encrypted FTP to exfiltrate data.[^5]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Machete](https://attack.mitre.org/software/S0409) logs keystrokes from the victim’s machine.[^6] [^2] [^5] [^1]  |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery | [Machete](https://attack.mitre.org/software/S0409) uses the `netsh wlan show networks mode=bssid` and `netsh wlan show interfaces` commands to list all nearby WiFi networks and connected interfaces.[^6]   |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Machete](https://attack.mitre.org/software/S0409) detects the insertion of new devices by listening for the WM_DEVICECHANGE window message.[^6]    |
| [[Data from Local System\|T1005]] | Data from Local System | [Machete](https://attack.mitre.org/software/S0409) searches the File system for files of interest.[^6]   |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Machete](https://attack.mitre.org/software/S0409) has sent data over HTTP if FTP failed, and has also used a fallback server.[^6]   |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Machete](https://attack.mitre.org/software/S0409) stores zipped files with profile data from installed web browsers.[^6]   |
| [[Python\|T1059.006]] | Python | [Machete](https://attack.mitre.org/software/S0409) is written in Python and is used in conjunction with additional Python scripts.[^6] [^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Machete](https://attack.mitre.org/software/S0409) produces file listings in order to search for files to be exfiltrated.[^6] [^5] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Machete](https://attack.mitre.org/software/S0409) collects the hostname of the target computer.[^6]   |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [Machete](https://attack.mitre.org/software/S0409) has the capability to exfiltrate stolen data to a hidden folder on a removable drive.[^6]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Machete](https://attack.mitre.org/software/S0409) captures screenshots.[^6] [^2] [^5] [^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Machete](https://attack.mitre.org/software/S0409) has used pyobfuscate, zlib compression, and base64 encoding for obfuscation. [Machete](https://attack.mitre.org/groups/G0095) has also used some visual obfuscation techniques by naming variables as combinations of letters to hinder analysis.[^5] [^6]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Machete\|G0095]] | Machete |



## References

[^1]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^2]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)


[^3]: Pyark


[^4]: Machete


[^5]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^6]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


