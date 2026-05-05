---
aliases: 
    - Kimsuky
    - Black Banshee
    - Velvet Chollima
    - Emerald Sleet
    - THALLIUM
    - APT43
    - TA427
    - Springtail
    - Earth Kumiho
    - PatheticSlug
mitre-attack: https://attack.mitre.org/groups/G0094
---

## G0094

[Kimsuky](https://attack.mitre.org/groups/G0094) is a Democratic People's Republic of Korea (DPRK)-based cyber espionage group that has been active since at least 2012. The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. Its operations expanded to include the United Nations and organizations in the government, education, business services, and manufacturing sectors across the United States, Japan, Russia, and Europe. [Kimsuky](https://attack.mitre.org/groups/G0094) has focused collection on foreign policy and national security issues tied to the Korean Peninsula, nuclear policy, and sanctions. [Kimsuky](https://attack.mitre.org/groups/G0094) operations have overlapped with those of other North Korean state-sponsored cyber espionage actors as a result of ad hoc collaborations or other limited resource sharing.[^35] [^20] [^41] [^10] [^42] [^32]  <br><br>[Kimsuky](https://attack.mitre.org/groups/G0094) was assessed to be responsible for the 2014 Korea Hydro & Nuclear Power Co. compromise; other notable campaigns include Operation STOLEN PENCIL (2018), Operation Kabar Cobra (2019), and Operation Smoke Screen (2019).[^28] [^34] [^31]  In 2023, [Kimsuky](https://attack.mitre.org/groups/G0094) was observed using commercial large language models (LLMs) to assist with vulnerability research, scripting, social engineering and reconnaissance.[^43] <br><br>DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under [Lazarus Group](https://attack.mitre.org/groups/G0032), rather than tracking operationally distinct subgroups.

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Delay Execution\|T1678]] | Delay Execution | [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized the Sleep function to ensure execution of scripts.[^12] [^14]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected Office, PDF, and HWP documents from its victims.[^40] [^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also harvested victim files through the use of the `RecentFiles()` function that collects paths of recently accessed files by parsing .lnk shortcuts from `%APPDATA%\Microsoft\Windows\Recent`.[^14]  |
| [[Malware\|T1587.001]] | Malware | [Kimsuky](https://attack.mitre.org/groups/G0094) has developed its own unique malware such as MailFetch.py for use in operations.[^24] [^19] [^42]  |
| [[Acquire Infrastructure\|T1583]] | Acquire Infrastructure | [Kimsuky](https://attack.mitre.org/groups/G0094) has used funds from stolen and laundered cryptocurrency to acquire operational infrastructure.[^42]  |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [Kimsuky](https://attack.mitre.org/groups/G0094) has used RDP for direct remote point-and-click access.[^28]  |
| [[Email Accounts\|T1585.002]] | Email Accounts | [Kimsuky](https://attack.mitre.org/groups/G0094) has created email accounts for phishing operations.[^24] [^42] [^32]  |
| [[Phishing\|T1566]] | Phishing | [Kimsuky](https://attack.mitre.org/groups/G0094) has used spearphishing to gain initial access and intelligence.[^43] [^42]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Kimsuky](https://attack.mitre.org/groups/G0094) has been observed turning off Windows Security Center and can hide the AV software window from the view of the infected user.[^40] [^19]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Kimsuky](https://attack.mitre.org/groups/G0094) has used spearphishing attachments to entice victims into opening malicious files, including LNK files disguised with tailored filenames and fake extensions.[^8] [^16] [^10] [^20] [^41] [^19] [^36]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also delivered malicious payloads within archive files (e.g., ZIP), which display decoy documents upon execution while running malicious code in the background.[^12]   |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Kimsuky](https://attack.mitre.org/groups/G0094) has used the Nirsoft SniffPass network sniffer to obtain passwords sent over non-secure protocols.[^10] [^28]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Kimsuky](https://attack.mitre.org/groups/G0094) has sent spearphishing emails containing a link to a document that contained malicious macros or took the victim to an actor-controlled domain.[^35] [^28] [^24]  |
| [[Web Portal Capture\|T1056.003]] | Web Portal Capture | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected credentials from a fake Google account login page.[^11]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Kimsuky](https://attack.mitre.org/groups/G0094) has used malware, such as [TRANSLATEXT](https://attack.mitre.org/software/S1201), to steal and exfiltrate browser cookies.[^22] [^39]   |
| [[Tool\|T1588.002]] | Tool | [Kimsuky](https://attack.mitre.org/groups/G0094) has obtained and used tools such as Nirsoft WebBrowserPassVIew, [Mimikatz](https://attack.mitre.org/software/S0002), and [PsExec](https://attack.mitre.org/software/S0029).[^28] [^19] [^42]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a tool called GREASE to add a Windows admin account in order to allow them continued access via RDP.[^28]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [Kimsuky](https://attack.mitre.org/groups/G0094) has exfiltrated data to C2 servers using an automated script that executes every 10 minutes and after successful checks for the presence of pre-designated staged filenames.[^14]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kimsuky](https://attack.mitre.org/groups/G0094) has decoded malicious VBScripts using Base64.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also decoded malicious PowerShell scripts using Base64.[^18] [^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has decoded RC4 obfuscated files prior to downloading files from their infrastructure.[^14]  |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged ClickFix type tactics enticing victims to copy and paste malicious code.[^36]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Kimsuky](https://attack.mitre.org/groups/G0094) has encoded malicious PowerShell scripts using Base64.[^18]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Kimsuky](https://attack.mitre.org/groups/G0094) has used compromised and acquired infrastructure to host and deliver malware including Blogspot to host beacons, file exfiltrators, and implants.[^19] [^42]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also hosted malicious payloads on Dropbox.[^18]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kimsuky](https://attack.mitre.org/groups/G0094) has downloaded additional scripts, tools, and malware onto victim systems.[^19] [^33] [^18] [^14]  |
| [[Develop Capabilities\|T1587]] | Develop Capabilities | [Kimsuky](https://attack.mitre.org/groups/G0094) created and used a mailing toolkit to use in spearphishing attacks.[^16]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [Kimsuky](https://attack.mitre.org/groups/G0094) has exfiltrated stolen files and data to actor-controlled Blogspot accounts.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also leveraged Dropbox for uploading victim system information.[^18]  |
| [[Phishing for Information\|T1598]] | Phishing for Information | [Kimsuky](https://attack.mitre.org/groups/G0094) has used tailored spearphishing emails to gather victim information including contat lists to identify additional targets.[^42]  |
| [[Impersonation\|T1684.001]] | Impersonation | [Kimsuky](https://attack.mitre.org/groups/G0094) has also impersonated legitimate people, such as a foreign advisor, an embassy employee, and a think tank employee.[^11]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also purported to be a Japanese diplomat to communicate with the victims.[^36]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Kimsuky](https://attack.mitre.org/groups/G0094) has signed files with the name EGIS CO,. Ltd. and has stolen a valid certificate that is used to sign the malware and the dropper.[^8] [^39]    |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Kimsuky](https://attack.mitre.org/groups/G0094) has disguised services to appear as benign software or related to operating system functions.[^10] [^18]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Kimsuky](https://attack.mitre.org/groups/G0094) has the ability to steal data from the clipboard.[^14]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged Component Object Model (COM) to create scheduled tasks to include using naming conventions that mimic legitimate applications.[^12]  [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged obfuscation VBScript to form a string in `WScript.Shell` which has downloaded a malicious payload to the victim environment.[^14]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Blogspot pages and a Github repository for C2.[^19] [^22]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also leveraged Dropbox for downloading payloads and uploading victim system information.[^18]  |
| [[Service Stop\|T1489]] | Service Stop | [Kimsuky](https://attack.mitre.org/groups/G0094) has disabled actively running virtual environments using the `KillMe` function to include VMware, Microsoft Hypervisors, and VirtualBox.[^14]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected sensitive browser data using the function `GetBrowserData()` to include login credentials, bookmarks, cookies, and encryption keys.[^14]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Kimsuky](https://attack.mitre.org/groups/G0094) has lured victims into clicking malicious links.[^24]  |
| [[Internal Spearphishing\|T1534]] | Internal Spearphishing | [Kimsuky](https://attack.mitre.org/groups/G0094) has sent internal spearphishing emails for lateral movement after stealing victim information.[^24]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [Kimsuky](https://attack.mitre.org/groups/G0094) has exploited various vulnerabilities for initial access, including Microsoft Exchange vulnerability CVE-2020-0688.[^24]  |
| [[Social Media\|T1593.001]] | Social Media | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Twitter to monitor potential victims and to prepare targeted phishing e-mails.[^41]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged dynamic API resolution using custom hashing techniques.[^12]   |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated code within files by converting hexadecimal strings to decimal numbers using the `CLng function` in combination with processing arithmetic operations and leveraging the `Chr function` to generate readable characters.[^14]   [Kimsuky](https://attack.mitre.org/groups/G0094) has also encoded files with Base64 and RC4.[^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized XOR and RC4 to encode malicious payloads.[^12]   |
| [[Establish Accounts\|T1585]] | Establish Accounts | [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged stolen PII to create accounts.[^42]  |
| [[Employee Names\|T1589.003]] | Employee Names | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected victim employee name information.[^24]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Kimsuky](https://attack.mitre.org/groups/G0094) has used `rundll32.exe` to execute malicious scripts and malware on a victim's network.[^19] [^14]  |
| [[Hidden Users\|T1564.002]] | Hidden Users | [Kimsuky](https://attack.mitre.org/groups/G0094) has run `reg add ‘HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList’ /v` to hide a newly created user.[^24]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Google Chrome browser extensions to infect victims and to steal passwords and cookies.[^13] [^28]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Kimsuky](https://attack.mitre.org/groups/G0094) has deleted the exfiltrated data on disk after transmission. [Kimsuky](https://attack.mitre.org/groups/G0094) has also used an instrumentor script to terminate browser processes running on an infected system and then delete the cookie files on disk.[^40] [^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has deleted files using the `Remove-Item` PowerShell commandlet to remove traces of executed payloads.[^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also removed remnants of files used for delivery to include .log and .zip files.[^14]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a modified TeamViewer client as a command and control channel.[^40] [^33]  |
| [[Server\|T1583.004]] | Server | [Kimsuky](https://attack.mitre.org/groups/G0094) has purchased hosting servers with virtual currency and prepaid cards.[^24]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Kimsuky](https://attack.mitre.org/groups/G0094) has accessed a Local State files associated with Chromium-based browsers that contain the AES key used to encrypt passwords stored in the browser to include `app_bound_encrypted_key`.[^14]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Kimsuky](https://attack.mitre.org/groups/G0094) has used the Invoke-Mimikatz PowerShell script to reflectively load a Mimikatz credential stealing DLL into memory.[^42]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used reflective loading through .NET assembly using `[System.Reflection.Assembly]::Load`.[^18]  |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a proprietary tool to intercept one time passwords required for two-factor authentication.[^24]  |
| [[Search Victim-Owned Websites\|T1594]] | Search Victim-Owned Websites | [Kimsuky](https://attack.mitre.org/groups/G0094) has searched for information on the target company's website.[^24]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Kimsuky](https://attack.mitre.org/groups/G0094) has executed Windows commands by using `cmd` and running batch scripts.[^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used `cmd.exe` to automatically open downloaded decoy pdf documents with the system’s default PDF viewer.[^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized malicious payloads to create reverse shells within the victim environment.[^12]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used batch scripts to eventually run [QuasarRAT](https://attack.mitre.org/software/S0262).[^36]  |
| [[Domains\|T1583.001]] | Domains | [Kimsuky](https://attack.mitre.org/groups/G0094) has registered domains to spoof targeted organizations and trusted third parties including search engines, web platforms, and cryptocurrency exchanges.[^8] [^1] [^10] [^20] [^41] [^24] [^42]  |
| [[Query Registry\|T1012]] | Query Registry | [Kimsuky](https://attack.mitre.org/groups/G0094) has obtained specific Registry keys and values on a compromised host.[^19]  |
| [[Gather Victim Org Information\|T1591]] | Gather Victim Org Information | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected victim organization information including but not limited to organization hierarchy, functions, press releases, and others.[^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used large language models (LLMs) to gather information about potential targets of interest.[^43]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Kimsuky](https://attack.mitre.org/groups/G0094)  has used HTTP GET and POST requests for C2.[^19] [^14]  |
| [[Social Media Accounts\|T1585.001]] | Social Media Accounts | [Kimsuky](https://attack.mitre.org/groups/G0094) has created social media accounts to monitor news and security trends as well as potential targets.[^24]  |
| [[Financial Theft\|T1657]] | Financial Theft | [Kimsuky](https://attack.mitre.org/groups/G0094) has stolen and laundered cryptocurrency to self-fund operations including the acquisition of infrastructure.[^42]  |
| [[Local Account\|T1136.001]] | Local Account | [Kimsuky](https://attack.mitre.org/groups/G0094) has created accounts with `net user`.[^24]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has used an instrumentor script to gather the names of all services running on a victim's system.[^19]  |
| [[Dynamic Resolution\|T1568]] | Dynamic Resolution | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Dynamic DNS (DDNS) services, such as FreeDNS or No-IP DDNS, to include servers located in South Korea.[^36]  |
| [[Binary Padding\|T1027.001]] | Binary Padding | [Kimsuky](https://attack.mitre.org/groups/G0094) has performed padding of PowerShell command line code with over 100 spaces.[^18]  |
| [[Email Accounts\|T1586.002]] | Email Accounts | [Kimsuky](https://attack.mitre.org/groups/G0094) has compromised email accounts to send spearphishing e-mails.[^16] [^41]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [Kimsuky](https://attack.mitre.org/groups/G0094) has used RC4 encryption before exfil.[^40]  |
| [[Timestomp\|T1070.006]] | Timestomp | [Kimsuky](https://attack.mitre.org/groups/G0094) has manipulated timestamps for creation or compilation dates to defeat anti-forensics.[^20]  |
| [[Spearphishing Link\|T1598.003]] | Spearphishing Link | [Kimsuky](https://attack.mitre.org/groups/G0094) has used links in e-mail to steal account information including web beacons for target profiling.[^16] [^41] [^24] [^32]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also utilized QR codes (also known as Quishing) to direct victims to malicious links through the reliance of a mobile device to scan a code with an embedded malicious URL.[^15] [^11]  |
| [[LNK Icon Smuggling\|T1027.012]] | LNK Icon Smuggling | [Kimsuky](https://attack.mitre.org/groups/G0094) has used the LNK icon location to execute malicious scripts.[^14]    [Kimsuky](https://attack.mitre.org/groups/G0094) has also padded the LNK target field properties with extra spaces to obscure the script.[^18]  |
| [[Search Open Technical Databases\|T1596]] | Search Open Technical Databases | [Kimsuky](https://attack.mitre.org/groups/G0094) has used LLMs to better understand publicly reported vulnerabilities.[^43] [^9]   |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated code by filling scripts with junk code and concatenating strings to hamper analysis and detection.[^18]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [Kimsuky](https://attack.mitre.org/groups/G0094) has used pass the hash for authentication to remote access software used in C2.[^10]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [Kimsuky](https://attack.mitre.org/groups/G0094) has used modified versions of PHProxy to examine web traffic between the victim and the accessed website.[^10]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has checked for the presence of antivirus software with `powershell Get-CimInstance -Namespace root/securityCenter2 – classname antivirusproduct`.[^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained details on antivirus software through WMI queries using `Win32_OperatingSystem` and `SecurityCenter2.AntiVirusProduct`.[^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also checked the status of Windows Defender through the use `cmd /s sc query WinDefend`.[^14]  |
| [[Mshta\|T1218.005]] | Mshta | [Kimsuky](https://attack.mitre.org/groups/G0094) has used mshta.exe to run malicious scripts on the system.[^35] [^10] [^33] [^24] [^14]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Kimsuky](https://attack.mitre.org/groups/G0094) has exfiltrated data over its C2 channel.[^40] [^19]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Kimsuky](https://attack.mitre.org/groups/G0094) has the ability to use form-grabbing to extract emails and passwords from web data forms.[^22]   |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged the PowerShell `-ErrorAction SilentlyContinue` command to continue execution through system events.[^14]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Kimsuky](https://attack.mitre.org/groups/G0094) has been observed disabling the system firewall.[^40]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Kimsuky](https://attack.mitre.org/groups/G0094) has used RDP to establish persistence.[^10]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has enumerated OS type, OS version, and other information using a script or the "systeminfo" command.[^40] [^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained system information such as OS type, OS version, and system type through querying various Windows Management Instrumentation (WMI) classes including `Win32_OperatingSystem`.[^18] [^14]  |
| [[Native API\|T1106]] | Native API | [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized Native APIs to collect data from victim hosts and facilitate execution of malicious scripts.[^12] [^14]  |
| [[Domains\|T1584.001]] | Domains | [Kimsuky](https://attack.mitre.org/groups/G0094) has compromised legitimate sites and used them to distribute malware.[^24] [^42]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected valid email addresses including personal accounts that were subsequently used for spearphishing and other forms of social engineering.[^41] [^32] [^42]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Kimsuky](https://attack.mitre.org/groups/G0094) has used JScript for logging and downloading additional tools.[^16] [^10]  [Kimsuky](https://attack.mitre.org/groups/G0094) has used [TRANSLATEXT](https://attack.mitre.org/software/S1201), which contained four Javascript files for bypassing defenses, collecting sensitive information and screenshots, and exfiltrating data.[^22]   |
| [[System Checks\|T1497.001]] | System Checks | [Kimsuky](https://attack.mitre.org/groups/G0094) has detected and killed virtual environments by using the PowerShell cmdlet `Get-CimInstance` that searches the classname of the computer system manufacturer through an if statement of `if($computerSystem.Manufacturer -match "VMware" -or $computerSystem.Manufacturer -match "Microsoft" -or $computerSystem.Manufacturer -match "VirtualBox")`.[^14]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated binary strings including the use of XOR encryption and Base64 encoding.[^8] [^16]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also modified the first byte of DLL implants targeting victims to prevent recognition of the executable file format.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated strings using Single Instruction Multiple Data (SIMD) instructions that complicate static analysis.[^12]   |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Kimsuky](https://attack.mitre.org/groups/G0094) has staged collected data files under `C:\Program Files\Common Files\System\Ole DB\`.[^10] [^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also gathered data in structured directories prior to exfiltration under the %TEMP% environment variable.[^14]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [Kimsuky](https://attack.mitre.org/groups/G0094) has used e-mail to send exfiltrated data to C2 servers.[^10]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a PowerShell-based keylogger as well as a tool called MECHANICAL to log keystrokes.[^35] [^40] [^10] [^28] [^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also leveraged Native Windows API functions such as `GetAsyncKeyState()` along with others to capture keystrokes every 50 milliseconds and stores data in a file stored in the temp directory.[^14]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Kimsuky](https://attack.mitre.org/groups/G0094) has packed malware with UPX.[^41]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Kimsuky](https://attack.mitre.org/groups/G0094) has used tools that are capable of obtaining credentials from saved mail.[^28]  |
| [[Dead Drop Resolver\|T1102.001]] | Dead Drop Resolver | [Kimsuky](https://attack.mitre.org/groups/G0094) has used [TRANSLATEXT](https://attack.mitre.org/software/S1201) and a dead drop resolver to retrieve configurations and commands from a public blog site.[^22]   |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [Kimsuky](https://attack.mitre.org/groups/G0094) has used QuickZip to archive stolen files before exfiltration.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has used the Send() function to compress all collected data into a zip file named init,.zip, then renames it to init.dat, before exfiltration.[^14]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has used `ipconfig/all` and web beacons sent via email to gather network configuration information.[^19] [^32]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also identified Host IP addresses leveraging the WMI class `Win32_NetworkAdapterConfiguration`.[^18]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Kimsuky](https://attack.mitre.org/groups/G0094) has used browser extensions including Google Chrome to steal passwords and cookies from browsers. [Kimsuky](https://attack.mitre.org/groups/G0094) has also used Nirsoft's WebBrowserPassView tool to dump the passwords obtained from victims.[^13] [^10] [^28] [^19]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Kimsuky](https://attack.mitre.org/groups/G0094) has the ability to load DLLs via reflective injection by allocating memory using `VirtualAllocEx()`, then decrypting a DLL with `WriteProcessMemory()` and invoking execution through `CreateRemoteThread()`.[^14]  |
| [[Change Default File Association\|T1546.001]] | Change Default File Association | [Kimsuky](https://attack.mitre.org/groups/G0094) has a HWP document stealer module which changes the default program association in the registry to open HWP documents.[^40]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Kimsuky](https://attack.mitre.org/groups/G0094) has used emails containing Word, Excel and/or HWP (Hangul Word Processor) documents in their spearphishing campaigns.[^13] [^40] [^8] [^16] [^20] [^41] [^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also distributed emails with attached compressed zip files that contained malicious .LNK files masquerading as legitimate files.[^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has delivered tailored PDF documents that contain malicious links.[^36]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) can gather a list of all processes running on a victim's machine.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained running processes on the victim device utilizing PowerShell cmdlet `Get-Process`.[^18]  |
| [[Process Injection\|T1055]] | Process Injection | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Win7Elevate to inject malicious code into explorer.exe.[^40]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Kimsuky](https://attack.mitre.org/groups/G0094) has captured browser screenshots using [TRANSLATEXT](https://attack.mitre.org/software/S1201).[^22]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained screen captures with custom malware.[^12]   |
| [[Modify Registry\|T1112]] | Modify Registry | [Kimsuky](https://attack.mitre.org/groups/G0094) has modified Registry settings for default file associations to enable all macros and for persistence.[^10] [^33] [^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also modified the registry entry for `HKCU:\Software\Microsoft\Windows\CurrentVersion\Run` registry key for persistence with the name WindowsSecurityCheck.[^14]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Kimsuky](https://attack.mitre.org/groups/G0094) has executed a variety of PowerShell scripts including Invoke-Mimikatz.[^35] [^10] [^19] [^24] [^42] [^14]   [Kimsuky](https://attack.mitre.org/groups/G0094) has also utilized PowerShell scripts for execution, persistence, and defense evasion.[^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged PowerShell’s cmdlet `Expand-Archive` to extract contents of zip files into the same directory.[^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has employed ClickFix type tactics enticing victims to copy and paste malicious PowerShell commands and scripts, where the scripts ultimately led to [QuasarRAT](https://attack.mitre.org/software/S0262).[^36]  |
| [[Exploits\|T1588.005]] | Exploits | [Kimsuky](https://attack.mitre.org/groups/G0094) has obtained exploit code for various CVEs.[^24]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Kimsuky](https://attack.mitre.org/groups/G0094) has executed malware with `regsvr32s`.[^12] [^24]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Kimsuky](https://attack.mitre.org/groups/G0094) has placed scripts in the startup folder for persistence and modified the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce` Registry key.[^40] [^10] [^33] [^19] [^24]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Kimsuky](https://attack.mitre.org/groups/G0094) has created new services for persistence.[^40] [^10]  |
| [[Web Services\|T1583.006]] | Web Services | [Kimsuky](https://attack.mitre.org/groups/G0094) has hosted content used for targeting efforts via web services such as Blogspot.[^19]   [Kimsuky](https://attack.mitre.org/groups/G0094) has also leveraged Dropbox for hosting payloads and uploading victim system information. [^18]  |
| [[Query Public AI Services\|T1682]] | Query Public AI Services | [Kimsuky](https://attack.mitre.org/groups/G0094) has used LLMs to identify think tanks, government organizations, and experts to inform targeting for spearphishing campaigns.[^43]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has the ability to enumerate all files and directories on an infected system.[^40] [^19] [^24]  [Kimsuky](https://attack.mitre.org/groups/G0094) has used a custom script with a function called CreateFileList() that can scan all filesystem drives, prioritizing C:\Users, to locate files and file extensions of interest that ultimately generates a file called `FileList.txt` saved within the victims %TEMP% Directory that contains the findings and the respective pathways.[^14]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Kimsuky](https://attack.mitre.org/groups/G0094) has used an information gathering module that will hide an AV software window from the victim.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also been known to use `-WindowStyle Hidden` to conceal PowerShell windows.[^18] [^14]  |
| [[Compression\|T1027.015]] | Compression | [Kimsuky](https://attack.mitre.org/groups/G0094) has delivered malicious payloads within Zip archives.[^12]   |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Kimsuky](https://attack.mitre.org/groups/G0094) has downloaded additional malware with scheduled tasks.[^24] [^36]  [Kimsuky](https://attack.mitre.org/groups/G0094) has established persistence by creating a scheduled task named “ChromeUpdateTaskMachine” through the PowerShell cmdlet `Register-ScheduleTask` which was set to execute another PowerShell script once, then five minutes after its creation and periodically repeat every 30 minutes.[^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also set scheduled tasks that run periodically using the PT1M repetition pattern leveraging naming conventions of Anti-Virus software to include "AhnlabUpdate".[^12]    |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has gathered the identity of the user by querying `System.Security.Principal` namespace using the `GetCurrent()` method.[^14]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized a mutex to detect whether its malware is actively running on the victim host.[^12] [^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has leveraged PowerShell to store the Process ID (PID) of the currently running malicious PowerShell script into a file named pid.txt which is saved locally on the victim host in the %TEMP% Directory and is queried prior to execution of subsequent PowerShell script to prevent duplication.[^14]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Kimsuky](https://attack.mitre.org/groups/G0094) has renamed malware to legitimate names such as `ESTCommon.dll` or `patch.dll`.[^25]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also disguised payloads using legitimate file names including a PowerShell payload named chrome.ps1. [^18]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used a malicious QR code that masqueraded as a legitimate package delivery service.[^15]      |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated HTTP Post request communications utilizing XOR with a designated key, followed by Base64 encoding.[^12]   |
| [[Search Engines\|T1593.002]] | Search Engines | [Kimsuky](https://attack.mitre.org/groups/G0094) has searched for vulnerabilities, tools, and geopolitical trends on Google to target victims.[^24]  |
| [[Double File Extension\|T1036.007]] | Double File Extension | [Kimsuky](https://attack.mitre.org/groups/G0094) has used an additional filename extension to hide the true file type. [Kimsuky](https://attack.mitre.org/groups/G0094) has also masqueraded malicious LNK files as PDF objects using the double extension .pdf.lnk.[^18]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a file injector DLL to spawn a benign process on the victim's system and inject the malicious payload into it via process hollowing.[^19]  |
| [[Code Signing Certificates\|T1588.003]] | Code Signing Certificates | [Kimsuky](https://attack.mitre.org/groups/G0094) has stolen a valid certificate that is used to sign the malware and the dropper.[^39]   |
| [[Email Forwarding Rule\|T1114.003]] | Email Forwarding Rule | [Kimsuky](https://attack.mitre.org/groups/G0094) has set auto-forward rules on victim's e-mail accounts.[^10]  |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [Kimsuky](https://attack.mitre.org/groups/G0094) has used FTP to download additional malware to the target machine.[^16]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Kimsuky](https://attack.mitre.org/groups/G0094) has gathered credentials using [Mimikatz](https://attack.mitre.org/software/S0002) and ProcDump.[^10] [^28] [^24]  |
| [[Traffic Signaling\|T1205]] | Traffic Signaling | [Kimsuky](https://attack.mitre.org/groups/G0094) has used [TRANSLATEXT](https://attack.mitre.org/software/S1201) to redirect clients to legitimate Gmail, Naver or Kakao pages if the clients connect with no parameters.[^22]   |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Kimsuky](https://attack.mitre.org/groups/G0094) has used Visual Basic to download malicious payloads.[^8] [^16] [^33] [^19] [^14]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used malicious VBA macros within maldocs disguised as forms that trigger when a victim types any content into the lure.[^19]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also leveraged VBScript (VBS) scripts to execute temp.vbs every 19 minutes using a scheduled task to run [QuasarRAT](https://attack.mitre.org/software/S0262).[^36]  |
| [[Additional Local or Domain Groups\|T1098.007]] | Additional Local or Domain Groups | [Kimsuky](https://attack.mitre.org/groups/G0094) has added accounts to specific groups with `net localgroup`.[^24]  |
| [[Python\|T1059.006]] | Python | [Kimsuky](https://attack.mitre.org/groups/G0094) has used a macOS Python implant to gather data as well as MailFetcher.py code to automatically collect email data.[^10] [^24]  |
| [[Web Shell\|T1505.003]] | Web Shell | [Kimsuky](https://attack.mitre.org/groups/G0094) has used modified versions of open source PHP web shells to maintain access, often adding "Dinosaur" references within the code.[^10]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has enumerated drives.[^19] [^40] [^14]  |
| [[Remote Email Collection\|T1114.002]] | Remote Email Collection | [Kimsuky](https://attack.mitre.org/groups/G0094) has used tools such as the MailFetch mail crawler to collect victim emails (excluding spam) from online services via IMAP.[^24]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [Kimsuky](https://attack.mitre.org/groups/G0094) has gathered the system time of the device using the PowerShell cmdlet `Get-Date`.[^14]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[certutil\|S0160]] | certutil | [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized certutil to decode a malicious payload.[^14]  |
| [[CSPY Downloader\|S0527]] | CSPY Downloader | [^20]  |
| [[Mimikatz\|S0002]] | Mimikatz | [^28] [^24] [^42]  |
| [[schtasks\|S0111]] | schtasks | [^20] [^24]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^42]  |
| [[PsExec\|S0029]] | PsExec | [^28]  |
| [[Amadey\|S1025]] | Amadey | [^42]  |
| [[NOKKI\|S0353]] | NOKKI | [^33]  |
| [[Brave Prince\|S0252]] | Brave Prince | [^19] [^42]  |
| [[AppleSeed\|S0622]] | AppleSeed | [^41] [^24]  |
| [[Gomir\|S1198]] | Gomir | [Gomir](https://attack.mitre.org/software/S1198) is uniquely associated with [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^37]  |
| [[TRANSLATEXT\|S1201]] | TRANSLATEXT | [^22]  |
| [[HTTPTroy\|S9007]] | HTTPTroy | [^12]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [^42]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [^20]  |
| [[GoBear\|S1197]] | GoBear | [GoBear](https://attack.mitre.org/software/S1197) is exclusively linked to [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^39] [^37]  |
| [[Gold Dragon\|S0249]] | Gold Dragon | [^19] [^42]  |
| [[BabyShark\|S0414]] | BabyShark | [^10] [^20] [^33] [^42]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) is exclusively linked to [Kimsuky](https://attack.mitre.org/groups/G0094) operations.[^39] [^37] [^5]  |



## References

[^1]: [Zdnet Kimsuky Group September 2020](https://www.zdnet.com/article/north-korea-has-tried-to-hack-11-officials-of-the-un-security-council/)


[^2]: PatheticSlug


[^3]: Earth Kumiho


[^4]: [Microsoft Threat Actor Naming July 2023](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)


[^5]: [ASEC Troll Stealer 2024](https://asec.ahnlab.com/en/61934/)


[^6]: Black Banshee


[^7]: [Cloudflare 2026 Threat Report New Threat Actors March 2026](https://blog.cloudflare.com/2026-threat-report/)


[^8]: [ThreatConnect Kimsuky September 2020](https://threatconnect.com/blog/kimsuky-phishing-operations-putting-in-work/)


[^9]: [OpenAI-CTI](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)


[^10]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)


[^11]: [FBI_KimsukyQR_Jan2026](https://www.ic3.gov/CSA/2026/260108.pdf)


[^12]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^13]: [Zdnet Kimsuky Dec 2018](https://www.zdnet.com/article/cyber-espionage-group-uses-chrome-extension-to-infect-victims/)


[^14]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^15]: [EnkiWhiteHat_KimsukyDOCSWAP_Dec2025](https://www.enki.co.kr/en/media-center/blog/kimsuky-distributing-malicious-mobile-app-via-qr-code)


[^16]: [VirusBulletin Kimsuky October 2019](https://www.virusbulletin.com/virusbulletin/2020/03/vb2019-paper-kimsuky-group-tracking-king-spearphishing/)


[^17]: Kimsuky


[^18]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^19]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^20]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^21]: TA427


[^22]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)


[^23]: [Rapid7 Threat Landscape Actors March 2026](https://www.rapid7.com/cdn/assets/bltc1ddd6561ab54a26/69ba67de50ca691edcd3f5b7/rapid7-threat-landscape-report-2026.pdf)


[^24]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^25]: [Kimsuky Malwarebytes](https://www.malwarebytes.com/blog/threat-intelligence/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor)


[^26]: THALLIUM


[^27]: Springtail


[^28]: [Netscout Stolen Pencil Dec 2018](https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/)


[^29]: Emerald Sleet


[^30]: APT43


[^31]: [AhnLab Kimsuky Kabar Cobra Feb 2019](https://global.ahnlab.com/global/upload/download/techreport/%5BAnalysis_Report%5DOperation%20Kabar%20Cobra.pdf)


[^32]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^33]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^34]: [EST Kimsuky SmokeScreen April 2019](https://blog.alyac.co.kr/attachment/cfile5.uf@99A0CD415CB67E210DCEB3.pdf)


[^35]: [EST Kimsuky April 2019](https://blog.alyac.co.kr/2234)


[^36]: [NaumaanProofpoint_GlobalClickFix_April2025](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)


[^37]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^38]: Velvet Chollima


[^39]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^40]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^41]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^42]: [Mandiant APT43 March 2024](https://services.google.com/fh/files/misc/apt43-report-en.pdf)


[^43]: [MSFT-AI](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)


