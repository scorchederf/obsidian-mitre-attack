---
aliases: 
    - T1083
mitre-attack: https://attack.mitre.org/techniques/T1083
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1083

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Many command shell utilities can be used to obtain this information. Examples include `dir`, `tree`, `ls`, `find`, and `locate`.[^354]  Custom tools may also be used to gather file and directory information and interact with the [Native API](https://attack.mitre.org/techniques/T1106). Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather file and directory information (e.g. `dir`, `show flash`, and/or `nvram`).[^185] <br><br>Some files and directories may require elevated or specific user permissions to access.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[RemoteUtilities\|S0592]] | RemoteUtilities | [RemoteUtilities](https://attack.mitre.org/software/S0592) can enumerate files and directories on a target machine.[^540]  |
| [[Diskpart\|S9002]] | Diskpart | If executed with elevated privileges, [Diskpart](https://attack.mitre.org/software/S9002) can list all volumes, including virtual disks.[^440]     |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can enumerate files on a target system.[^367]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^307]   |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) includes various modules for finding files of interest on hosts and network shares.[^244]  |
| [[PoshC2\|S0378]] | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^326]  |
| [[Rclone\|S1040]] | Rclone | [Rclone](https://attack.mitre.org/software/S1040) can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^684]  |
| [[TruffleHog\|S9009]] | TruffleHog | [TruffleHog](https://attack.mitre.org/software/S9009) has can browse and scan individual files and directories.[^685] [^448] [^19]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can search for files on the infected machine.[^629] [^594]  |
| [[Imminent Monitor\|S0434]] | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.[^378]  |
| [[Forfiles\|S0193]] | Forfiles | [Forfiles](https://attack.mitre.org/software/S0193) can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)[^464]  |
| [[cmd\|S0106]] | cmd | [cmd](https://attack.mitre.org/software/S0106) can be used to find files and directories with native functionality such as `dir` commands.[^343]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover specified filetypes and log files on a targeted system.[^72]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can obtain a list of directories.[^111]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can walk through directories and recursively search for strings in files.[^192]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) searches the system for all of the following file extensions: .avi, .mov, .mkv, .mpeg, .mpeg4, .mp4, .mp3, .wav, .ogg, .jpeg, .jpg, .png, .bmp, .gif, .tiff, .ico, .xlsx, and .zip. It can also obtain browsing history, cookies, and plug-in information.[^674] [^125]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get the current directory name as well as the size of a file. It also has commands to obtain information about logical drives, drive type, and free space.[^134]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) can search, read, write, move, and execute files.[^457] [^131]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) has the ability to enumerate directory content.[^299] [^418]  |
| [[QuietSieve\|S0686]] | QuietSieve | [QuietSieve](https://attack.mitre.org/software/S0686) can search files on the target host by extension, including doc, docx, xls, rtf, odt, txt, jpg, pdf, rar, zip, and 7z.[^60]   |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) checks its directory location in an attempt to avoid launching in a sandbox.[^697] [^342]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has identified specific files and directories within targeted hosts and systems for modification, execution, collection and exfiltration.[^587] [^308] [^149] [^368] [^79] [^741]  |
| [[AcidRain\|S1125]] | AcidRain | [AcidRain](https://attack.mitre.org/software/S1125) identifies specific files and directories in the Linux operating system associated with storage devices.[^529]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) has searched for folders associated with antivirus software.[^208]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) lists files in directories.[^257]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can gather victim drive information.[^680]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) gathers information on victim’s drives and has a plugin for document listing.[^235]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about available drives, default browser, desktop file list, My Documents, Internet history, program files, and root of available drives. It also searches for ICS-related software files.[^218]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) uses a driver to scan for specific filesystem driver objects.[^631]  |
| [[AvosLocker\|S1053]] | AvosLocker | [AvosLocker](https://attack.mitre.org/software/S1053) has searched for files and directories on a compromised network.[^625] [^227]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) may enumerate user directories on a victim.[^280]  |
| [[COATHANGER\|S1105]] | COATHANGER | [COATHANGER](https://attack.mitre.org/software/S1105) will survey the contents of system files during installation.[^39]  |
| [[Smoke Loader\|S0226]] | Smoke Loader | [Smoke Loader](https://attack.mitre.org/software/S0226) recursively searches through directories for files.[^431]  |
| [[WindTail\|S0466]] | WindTail | [WindTail](https://attack.mitre.org/software/S0466) has the ability to enumerate the users home directory and the path to its own application bundle.[^200] [^191]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) is capable of running commands to obtain a list of files and directories, as well as enumerating logical drives.[^672]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) has a command to search for files on the victim’s machine.[^317]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can obtain file and directory information.[^510]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) has the ability to only encrypt specific files.[^383]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) has the ability to enumerate files and drives.[^672]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) can enumerate and search for files and directories.[^427] [^290]  |
| [[LITTLELAMB.WOOLTEA\|S1121]] | LITTLELAMB.WOOLTEA | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can monitor for system upgrade events by checking for the presence of `/tmp/data/root/dev`.[^10]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) searches for specific directories on the victim’s machine.[^89]  |
| [[GeminiDuke\|S0049]] | GeminiDuke | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information from the victim, including installed drivers, programs previously executed by users, programs and services configured to automatically run at startup, files and folders present in any user's home folder, files and folders present in any user's My Documents, programs installed to the Program Files folder, and recently accessed files, folders, and programs.[^436]  |
| [[Havoc\|S1229]] | Havoc | The [Havoc](https://attack.mitre.org/software/S1229) interface can display a file explorer view of the compromised host.[^562]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) collects the volumes mapped on the system, and also steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^70]  |
| [[Prestige\|S1058]] | Prestige | [Prestige](https://attack.mitre.org/software/S1058) can traverse the file system to discover files to encrypt by identifying specific extensions defined in a hardcoded list.[^569]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has identified specific directories and files for exfiltration using the `ssh_upload` command which contains subcommands of `.sdira`, `sdir`, `sfile`, `sfinda`, `sfindr`, `sfind`.[^77] [^162]  [InvisibleFerret](https://attack.mitre.org/software/S1245) also has the capability to scan and upload files of interest from multiple OS systems through the use of scripts that check file names, file extensions, and avoids certain path names.[^251] [^323]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized the `findstr` on Windows or the macOS `find` commands to search for files of interest.[^347]   |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) searches for files on the victim's machine.[^119]  |
| [[SharpDisco\|S1089]] | SharpDisco | [SharpDisco](https://attack.mitre.org/software/S1089) can identify recently opened files by using an LNK format parser to extract the original file path from LNK files found in either `%USERPROFILE%\Recent` (Windows XP) or `%APPDATA%\Microsoft\Windows\Recent` (newer Windows versions) .[^737]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) can parse the hard drive on a compromised host to identify specific file extensions.[^381]  |
| [[WinMM\|S0059]] | WinMM | [WinMM](https://attack.mitre.org/software/S0059) sets a WH_CBT Windows hook to search for and capture files on the victim.[^512]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can list files and directories on a compromised host.[^474]  |
| [[AuditCred\|S0347]] | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) can search through folders and files on the system.[^740]  |
| [[Kasidet\|S0088]] | Kasidet | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to search for a given filename on a victim.[^38]  |
| [[OceanSalt\|S0346]] | OceanSalt | [OceanSalt](https://attack.mitre.org/software/S0346) can extract drive information from the endpoint and search files on the system.[^177]  |
| [[Playcrypt\|S1162]] | Playcrypt | [Playcrypt](https://attack.mitre.org/software/S1162) can avoid encrypting files with a .PLAY, .exe, .msi, .dll, .lnk, or .sys file extension.[^318]  |
| [[Brave Prince\|S0252]] | Brave Prince | [Brave Prince](https://attack.mitre.org/software/S0252) gathers file and directory information from the victim’s machine.[^434]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has searched for files within the victim environment for encryption and exfiltration.[^43] [^45] [^566]   [Medusa Ransomware](https://attack.mitre.org/software/S1244) has also identified files associated with remote management services.[^43] [^45]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to collect recently changed files with specific extensions.[^474]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to search for .txt, .ppt, .hwp, .pdf, and .doc files in specified directories.[^703]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) has the ability to search for files on the compromised host.[^152]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [CosmicDuke](https://attack.mitre.org/software/S0050) searches attached and mounted drives for file extensions and keywords that match a predefined list.[^413]  |
| [[Gomir\|S1198]] | Gomir | [Gomir](https://attack.mitre.org/software/S1198) collects information about directory and file structures, including total number of subdirectories, total number of files, and total size of files on infected systems.[^592]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to gather metadata from a file and to search for file and directory names.[^186]  |
| [[BOLDMOVE\|S1184]] | BOLDMOVE | [BOLDMOVE](https://attack.mitre.org/software/S1184) can list information of all files in the system recursively from the root directory or from a specified directory.[^445]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) contains commands to list files and directories, as well as search for files matching certain extensions from a defined list.[^156] [^222] [^78]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate files and directories.[^627]  |
| [[DynoWiper\|S9038]] | DynoWiper | [DynoWiper](https://attack.mitre.org/software/S9038) has used the Microsoft Windows native `FindFirstFile()` and `FindNextFile()` to recursively enumerate directories and files on the system.[^283]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can search for specific files and list directories.[^589]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) produces file listings in order to search for files to be exfiltrated.[^236] [^475] [^2]  |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect drive and file information on an infected machine.[^340]  |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) has the ability to browse files in directories such as Program Files and the Desktop.[^238]   |
| [[Prikormka\|S0113]] | Prikormka | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information about the paths, size, and creation time of files with specific file extensions, but not the actual content of the file.[^37]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can enumerate storage volumes and folder contents of a compromised host.[^406]  |
| [[Dacls\|S0497]] | Dacls | [Dacls](https://attack.mitre.org/software/S0497) can scan directories on a compromised host.[^231]  |
| [[DropBook\|S0547]] | DropBook | [DropBook](https://attack.mitre.org/software/S0547) can collect the names of all files and folders in the Program Files directories.[^351] [^516]   |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can list all files and their associated attributes, including filename, type, owner, creation time, last access time, last write time, size, and permissions.[^193]   |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can search for files and directories.[^41]  |
| [[ELMER\|S0064]] | ELMER | [ELMER](https://attack.mitre.org/software/S0064) is capable of performing directory listings.[^35]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) can execute `enum` to enumerate files in storage on a compromised system.[^726]  |
| [[ODAgent\|S1170]] | ODAgent | [ODAgent](https://attack.mitre.org/software/S1170) can identify the current working directory.[^356]  |
| [[FLASHFLOOD\|S0036]] | FLASHFLOOD | [FLASHFLOOD](https://attack.mitre.org/software/S0036) searches for interesting files (either a default or customized set of file extensions) on the local system and removable media.[^414]  |
| [[FYAnti\|S0628]] | FYAnti | [FYAnti](https://attack.mitre.org/software/S0628) can search the `C:\Windows\Microsoft.NET\` directory for files of a specified size.[^728]  |
| [[LoFiSe\|S1101]] | LoFiSe | [LoFiSe](https://attack.mitre.org/software/S1101) can monitor the file system to identify files less than 6.4 MB in size with file extensions including .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf, .rtf, .tif, .odt, .ods, .odp, .eml, and .msg.[^418]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed enumerating system drives and partitions.[^588] 	 |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can search for files associated with specific applications.[^334] [^750]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload to its C2 server information about files on the victim mobile device, including SD card size, installed app list, SMS content, contacts, and calling history.[^12]  |
| [[WastedLocker\|S0612]] | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) can enumerate files and directories just prior to encryption.[^709]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can list information about files in a directory and recently opened or used documents. [InvisiMole](https://attack.mitre.org/software/S0260) can also search for specific files by supplied file mask.[^276]  |
| [[P.A.S. Webshell\|S0598]] | P.A.S. Webshell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to list files and file characteristics including extension, size, ownership, and permissions.[^491]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can list directories on a victim.[^748]  |
| [[WINERACK\|S0219]] | WINERACK | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate files and directories.[^112]  |
| [[WhisperGate\|S0689]] | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) can locate files based on hardcoded file extensions.[^465] [^713] [^614] [^537]  |
| [[FruitFly\|S0277]] | FruitFly | [FruitFly](https://attack.mitre.org/software/S0277) looks for specific files and file types.[^539]  |
| [[AcidPour\|S1167]] | AcidPour | [AcidPour](https://attack.mitre.org/software/S1167) can identify specific files and directories within the Linux operating system corresponding with storage devices for follow-on wiping activity, similar to [AcidRain](https://attack.mitre.org/software/S1125).[^411]  |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has checked for the existence of specific files including `/usr/sbin/setenforce` and ` /etc/selinux/config`. It also has the ability to monitor the cryptocurrency miner file and process. [^661]   |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) has used DriveLetterView to enumerate drive information.[^548]  |
| [[Conti\|S0575]] | Conti | [Conti](https://attack.mitre.org/software/S0575) can discover files on a local system.[^668]  |
| [[SameCoin\|S9030]] | SameCoin | [SameCoin](https://attack.mitre.org/software/S9030) can list all system files and can avoid wiping specific directories such as Program Files, Windows, and Users.[^144]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) will check to see if the initial executing script is located on the user's Desktop as an anti-analysis check.[^30]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) searches for various filesystem paths to determine what banking applications are installed on the victim’s machine.[^555]  |
| [[Megazord\|S1191]] | Megazord | [Megazord](https://attack.mitre.org/software/S1191) can ignore specified directories for encryption.[^531] <br> |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) has a command to traverse the files and directories in a given path.[^735]   |
| [[Doki\|S0600]] | Doki | [Doki](https://attack.mitre.org/software/S0600) has resolved the path of a process PID to use as a script argument.[^57]  |
| [[Siloscape\|S0623]] | Siloscape |  [Siloscape](https://attack.mitre.org/software/S0623) searches for the Kubernetes config file and other related files using a regular expression.[^454]   |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) can enumerate files for encryption.[^64]  |
| [[Fysbis\|S0410]] | Fysbis | [Fysbis](https://attack.mitre.org/software/S0410) has the ability to search for files.[^580]   |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can look for files carrying specific extensions such as: .rtf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pps, .ppsx, .txt, .gpg, .pkr, .kdbx, .key, and .jpb.[^92]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) finds a specified directory, lists the files and metadata about those files.[^570]  |
| [[NETEAGLE\|S0034]] | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) allows adversaries to enumerate and modify the infected host's file system. It supports searching for directories, creating directories, listing directory contents, reading and writing to files, retrieving file attributes, and retrieving volume information.[^414]  |
| [[POORAIM\|S0216]] | POORAIM | [POORAIM](https://attack.mitre.org/software/S0216) can conduct file browsing.[^112]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has the ability to enumerate directories for files that match a set list.[^640]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can enumerate directories on target machines.[^428]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) gathers a list of installed apps from the uninstall program Registry. It also gathers registered mail, browser, and instant messaging clients from the Registry. [BlackEnergy](https://attack.mitre.org/software/S0089) has searched for given file types.[^417] [^642]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can browse the file system.[^422]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate information about files from the infected system, including file size, attributes, creation time, last access time, and write time. [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate the compilation timestamp of Windows executable files.[^223] 	 |
| [[NotPetya\|S0368]] | NotPetya | [NotPetya](https://attack.mitre.org/software/S0368) searches for files ending with dozens of different file extensions prior to encryption.[^425]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) can list directories.[^452]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has searched for files on the infected host.[^633]  |
| [[ObliqueRAT\|S0644]] | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) has the ability to recursively enumerate files on an infected endpoint.[^76]  |
| [[SHOTPUT\|S0063]] | SHOTPUT | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to obtain a directory listing.[^174]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) has searched for specific files prior to encryption.[^745]  |
| [[XAgentOSX\|S0161]] | XAgentOSX | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the readFiles function to return a detailed listing (sometimes recursive) of a specified directory.[^421]  [XAgentOSX](https://attack.mitre.org/software/S0161) contains the showBackupIosFolder function to check for IOS device backups by running `ls -la ~/Library/Application\ Support/MobileSync/Backup/`.[^421]  |
| [[China Chopper\|S0020]] | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can list directory contents.[^505] [^669]  |
| [[LightSpy\|S1185]] | LightSpy | [LightSpy](https://attack.mitre.org/software/S1185) uses the `NSFileManager` to move, create and delete files. [LightSpy](https://attack.mitre.org/software/S1185) can also use the assembly `bt` instruction to determine a file's executable permissions.[^83]  |
| [[Cheerscrypt\|S1096]] | Cheerscrypt | [Cheerscrypt](https://attack.mitre.org/software/S1096) can search for log and VMware-related files with .log, .vmdk, .vmem, .vswp, and .vmsn extensions.[^126]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) has a command to launch a file browser or explorer on the system.[^228]  |
| [[MiniDuke\|S0051]] | MiniDuke | [MiniDuke](https://attack.mitre.org/software/S0051) can enumerate local drives.[^428]  |
| [[Pteranodon\|S0147]] | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) identifies files matching certain file extension and copies them to subdirectories it created.[^515]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has searched for .ldb and .log files stored in browser extension directories for collection and exfiltration.[^73] [^643] [^77]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) has the ability to gather a list of files and directories on the infected system.[^298] [^404] [^639]  |
| [[Babuk\|S0638]] | Babuk | [Babuk](https://attack.mitre.org/software/S0638) has the ability to enumerate files on a targeted system.[^686] [^645]  |
| [[Exbyte\|S1179]] | Exbyte | [Exbyte](https://attack.mitre.org/software/S1179) enumerates all document files on an infected machine, then creates a summary of these items including filename and directory location prior to exfiltration to cloud hosting services.[^216]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) has the ability to enumerate file and folder names.[^273]  |
| [[BlackMould\|S0564]] | BlackMould | [BlackMould](https://attack.mitre.org/software/S0564) has the ability to find files on the targeted system.[^335]  |
| [[PACEMAKER\|S1109]] | PACEMAKER | [PACEMAKER](https://attack.mitre.org/software/S1109) can parse `/proc/"process_name"/cmdline` to look for the string `dswsd` within the command line.[^122]  |
| [[BBSRAT\|S0127]] | BBSRAT | [BBSRAT](https://attack.mitre.org/software/S0127) can list file and directory information.[^567]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has a module to enumerate drives and find files recursively.[^702] [^33] [^385] [^690]  [PlugX](https://attack.mitre.org/software/S0013) has also checked the path from which it is running for specific parameters prior to execution. [^702] [^133] [^139]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) can retrieve a file listing from the system.[^255] [^194]   |
| [[MultiLayer Wiper\|S1135]] | MultiLayer Wiper | [MultiLayer Wiper](https://attack.mitre.org/software/S1135) generates a list of all files and paths on the fixed drives of an infected system, enumerating all files on the system except specific folders defined in a hardcoded list.[^237]  |
| [[DustySky\|S0062]] | DustySky | [DustySky](https://attack.mitre.org/software/S0062) scans the victim for files that contain certain keywords and document types including PDF, DOC, DOCX, XLS, and XLSX, from a list that is obtained from the C2 as a text file. It can also identify logical drives for the infected machine.[^145] [^80]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) is capable of listing contents of folders on the victim. [Remsec](https://attack.mitre.org/software/S0125) also searches for custom network encryption software on victims.[^344] [^281] [^355]  |
| [[Rover\|S0090]] | Rover | [Rover](https://attack.mitre.org/software/S0090) automatically searches for files on local drives based on a predefined list of file extensions.[^363]  |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) recursively searches for all .doc files on the system and collects a directory listing of the Desktop, %TEMP%, and %WINDOWS%\Temp directories.[^581] [^708]  |
| [[Peppy\|S0643]] | Peppy | [Peppy](https://attack.mitre.org/software/S0643) can identify specific files for exfiltration.[^156]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can enumerate files by using a variety of functions.[^34]  |
| [[DEATHRANSOM\|S0616]] | DEATHRANSOM | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can use loop operations to enumerate directories on a compromised host.[^590]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can browse directories on a compromised host.[^558] [^158]  |
| [[Akira\|S1129]] | Akira | [Akira](https://attack.mitre.org/software/S1129) examines files prior to encryption to determine if they meet requirements for encryption and can be encrypted by the ransomware. These checks are performed through native Windows functions such as `GetFileAttributesW`.[^599] [^18]  |
| [[DarkGate\|S1111]] | DarkGate | Some versions of [DarkGate](https://attack.mitre.org/software/S1111) search for the hard-coded folder `C:\Program Files\e Carte Bleue`.[^707]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can exclude files associated with core system functions from encryption.[^695]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can check for the [FoggyWeb](https://attack.mitre.org/software/S0661) backdoor .pri file on a compromised AD FS server.[^306]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can check for the existence of files, including its own components, as well as retrieve a list of logical drives.[^14] [^274]  |
| [[CreepyDrive\|S1023]] | CreepyDrive | [CreepyDrive](https://attack.mitre.org/software/S1023) can specify the local file path to upload files from.[^495]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can search for files in directories.[^232]   |
| [[Elise\|S0081]] | Elise | A variant of [Elise](https://attack.mitre.org/software/S0081) executes `dir C:\progra~1` when initially run.[^597] [^282]  |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can detect the victim's file or folder list.[^660] 	 |
| [[WannaCry\|S0366]] | WannaCry | [WannaCry](https://attack.mitre.org/software/S0366) searches for variety of user files by file extension before encrypting them using RSA and AES, including Office, PDF, image, audio, video, source code, archive/compression format, and key and certificate files.[^107] [^179]  |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to discover drive information on the infected host.[^146]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can collect desktop filenames.[^387] [^424] [^155]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can search a compromised host for specific files.[^654]  |
| [[LODEINFO\|S9020]] | LODEINFO | <br>[LODEINFO](https://attack.mitre.org/software/S9020) has the ability to designate specific files and folders to encryption.[^207] [^338]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can enumerate drives and list the contents of the C: drive on a victim's computer.[^261]  |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) can search directories for files on the victim’s machine.[^563]  |
| [[3PARA RAT\|S0066]] | 3PARA RAT | [3PARA RAT](https://attack.mitre.org/software/S0066) has a command to retrieve metadata for files on disk as well as a command to list the current working directory.[^105]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can use `DirectoryList` to enumerate files in a specified directory.[^53]  |
| [[Royal\|S1073]] | Royal | [Royal](https://attack.mitre.org/software/S1073) can identify specific files and directories to exclude from the encryption process.[^66] [^279] [^375]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can search for specific files on a compromised system.[^215]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has searched the Program Files directories for specific folders and has searched for strings related to its mutexes.[^446] [^523] [^534]   |
| [[Spica\|S1140]] | Spica | [Spica](https://attack.mitre.org/software/S1140) can list filesystem contents on targeted systems.[^549]  |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has searched for folders, subfolders and other networked or mounted drives for follow on encryption actions.[^388]  [Embargo](https://attack.mitre.org/software/S1247) has also iterated device volumes using `FindFirstVolumeW()` and `FindNextVolumeW()` functions and then calls the `GetVolumePathNamesForVolumeNameW()` function to retrieve a list of drive letters and mounted folder paths for each specified volume.[^388]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can enumerate files and directories on a compromised host.[^657]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) has a command to list files on a system.[^292]  |
| [[TINYTYPHON\|S0131]] | TINYTYPHON | [TINYTYPHON](https://attack.mitre.org/software/S0131) searches through the drive containing the OS, then all drive letters C through to Z, for documents matching certain extensions.[^389]  |
| [[KONNI\|S0356]] | KONNI | A version of [KONNI](https://attack.mitre.org/software/S0356) searches for filenames created with a previous version of the malware, suggesting different versions targeted the same victims and the versions may work together.[^484]  |
| [[CORALDECK\|S0212]] | CORALDECK | [CORALDECK](https://attack.mitre.org/software/S0212) searches for specified files.[^112]  |
| [[SPACESHIP\|S0035]] | SPACESHIP | [SPACESHIP](https://attack.mitre.org/software/S0035) identifies files and directories for collection by searching for specific file extensions or file modification time.[^414]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) can enumerate files and collect associated metadata.[^691]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) can enumerate files and directories on a compromised host.[^198]  |
| [[down_new\|S0472]] | down_new | [down_new](https://attack.mitre.org/software/S0472) has the ability to list the directories on a compromised host.[^238]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) can list file and directory information.[^201]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) can perform a recursive directory listing for all volume drives available on the victim's machine and can also fetch specific files by their paths.[^266]  |
| [[RARSTONE\|S0055]] | RARSTONE | [RARSTONE](https://attack.mitre.org/software/S0055) obtains installer properties from Uninstall Registry Key entries to obtain information about installed applications and how to uninstall certain applications.[^415]  |
| [[Black Basta\|S1070]] | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) can enumerate specific files for encryption.[^135] [^157] [^653] [^353] [^501] [^289] [^409] [^739]  |
| [[4H RAT\|S0065]] | 4H RAT | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to obtain file and directory listings.[^105]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438) has a plugin that enumerates files with specific extensions on all hard disk drives and stores file information in encrypted log files.[^650]  |
| [[MegaCortex\|S0576]] | MegaCortex | [MegaCortex](https://attack.mitre.org/software/S0576) can parse the available drives and directories to determine which files to encrypt.[^69]   |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate drive types.[^420]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) has searched for files on the system, such as documents located in the desktop folder.[^370]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can use a file monitor to identify .lnk, .doc, .docx, .xls, .xslx, and .pdf files.[^737]  |
| [[Akira _v2\|S1194]] | Akira _v2 | [Akira _v2](https://attack.mitre.org/software/S1194) can target specific files and folders for encryption.[^160] [^18] [^531]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to get directory listings or drive information on a compromised host.[^453]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can check for specific files and directories associated with virtualization and malware analysis.[^58]  |
| [[Derusbi\|S0021]] | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is capable of obtaining directory, file, and drive listings.[^722] [^505]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can enumerate the victim's desktop.[^65] [^229]  |
| [[BadPatch\|S0337]] | BadPatch | [BadPatch](https://attack.mitre.org/software/S0337) searches for files with specific file extensions.[^407]  |
| [[MESSAGETAP\|S0443]] | MESSAGETAP | [MESSAGETAP](https://attack.mitre.org/software/S0443) checks for the existence of two configuration files (keyword_parm.txt and parm.txt) and attempts to read the files every 30 seconds.[^509]  |
| [[SUGARDUMP\|S1042]] | SUGARDUMP | [SUGARDUMP](https://attack.mitre.org/software/S1042) can search for and collect data from specific Chrome, Opera, Microsoft Edge, and Firefox files, including any folders that have the string `Profile` in its name.[^17]  |
| [[SOUNDBITE\|S0157]] | SOUNDBITE | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of enumerating and manipulating files and directories.[^102]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) has a command to return a directory listing for a specified directory.[^169]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has enumerated files and folders on all mounted drives.[^54] 	 |
| [[Cryptoistic\|S0498]] | Cryptoistic | [Cryptoistic](https://attack.mitre.org/software/S0498) can scan a directory to identify files for deletion.[^736]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) can enumerate common folders such as My Documents, Desktop, and AppData.[^309] [^575]  |
| [[ccf32\|S1043]] | ccf32 | [ccf32](https://attack.mitre.org/software/S1043) can parse collected files to identify specific file extensions.[^293]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can exclude files associated with core system functions from encryption.[^687]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) searches for files that are 60mb and less and contain the following extensions: .doc, .docx, .xls, .xlsx, .ppt, .pptx, .exe, .zip, and .rar. [Zebrocy](https://attack.mitre.org/software/S0251) also runs the `echo %APPDATA%` command to list the contents of the directory.[^651] [^670] [^314]  [Zebrocy](https://attack.mitre.org/software/S0251) can obtain the current execution path as well as perform drive enumeration.[^561] [^751]   |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) enumerates directories and scans for certain files.[^4] [^171]  |
| [[LunarMail\|S1142]] | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) can search its staging directory for output files it has produced.[^504]  |
| [[CrossRAT\|S0235]] | CrossRAT | [CrossRAT](https://attack.mitre.org/software/S0235) can list all files on a system.[^503]  |
| [[OwaAuth\|S0072]] | OwaAuth | [OwaAuth](https://attack.mitre.org/software/S0072) has a command to list its directory and logical drives.[^607]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can explore files on a compromised system.[^26]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) had commands to enumerate files and directories.[^103] [^48]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to retrieve a list of files in a given directory as well as drives and drive types.[^127]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) has the ability to identify specific files and directories that are not to be encrypted.[^380] [^477] [^357] [^212] [^412] [^81]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) can use a specific module for file enumeration.[^299]  |
| [[PinchDuke\|S0048]] | PinchDuke | [PinchDuke](https://attack.mitre.org/software/S0048) searches for files created within a certain timeframe and whose file extension matches a predefined list.[^436]  |
| [[USBStealer\|S0136]] | USBStealer | [USBStealer](https://attack.mitre.org/software/S0136) searches victim drives for files matching certain extensions (“.skr”,“.pkr” or “.key”) or names.[^693] [^608]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) can search for specific files.[^716]  |
| [[Kivars\|S0437]] | Kivars | [Kivars](https://attack.mitre.org/software/S0437) has the ability to list drives on the infected host.[^268]  |
| [[CaddyWiper\|S0693]] | CaddyWiper | [CaddyWiper](https://attack.mitre.org/software/S0693) can enumerate all files and directories on a compromised host.[^647]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use the Linux API `statvfs` to enumerate the current working directory.[^444] [^729]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) has the capability to identify the drive type on a victim.[^177]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to index files from drives, user profiles, and removable drives.[^333]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to list drives and files on the compromised host.[^268] [^325]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) identifies target files and directories for collection based on a configuration file.[^252] [^182]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) checks its current working directory upon execution and also contains watchdog functionality that ensures its executable is located in the correct path (else it will rewrite the payload).[^313]  |
| [[Pisloader\|S0124]] | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) has commands to list drives on the victim machine and to list file information for a given directory.[^679]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) has included a program "ExeProtector", which monitors for the existence of [GoldenSpy](https://attack.mitre.org/software/S0493) on the infected system and redownloads if necessary.[^706] 	 |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) lists the directories for Desktop, program files, and the user’s recently accessed files.[^434]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can collect directory and file lists.[^398] [^11] 	 |
| [[AshTag\|S9031]] | AshTag | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component can enumerate files on victim hosts.[^113]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can search for a specific file on the compromised computer and can enumerate files in Desktop, Downloads, and Documents folders.[^61]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can identify files with .doc, .docx, .ppt, .pptx, .xls, .xlsx, and .pdf extensions and specific timestamps for collection.[^293]  |
| [[ROADSWEEP\|S1150]] | ROADSWEEP | [ROADSWEEP](https://attack.mitre.org/software/S1150) can enumerate files on infected devices and avoid encrypting files with .exe, .dll, 	.sys, .lnk, or . lck extensions.[^640] [^527] [^117]  |
| [[SUNSPOT\|S0562]] | SUNSPOT | [SUNSPOT](https://attack.mitre.org/software/S0562) enumerated the Orion software Visual Studio solution directory path.[^394]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can search files on a compromised host.[^168] [^153]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) can search for specific file extensions, including zipped files.[^654]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to identify folders and files related to previous infections.[^488] 	 |
| [[ANELLDR\|S9027]] | ANELLDR | [ANELLDR](https://attack.mitre.org/software/S9027) can enumerate files in the current directory to search for encrypted payload files.[^9]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of files and directories in C:\ with the command `dir /s /a c:\ >> "C:\windows\TEMP\[RANDOM].tmp"`.[^683]  |
| [[BoomBox\|S0635]] | BoomBox | [BoomBox](https://attack.mitre.org/software/S0635) can search for specific files and directories on a machine.[^486]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can target directories on victim machines for file collection.[^154] [^715]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) can enumerate the contents of current working or other specified directories.[^49]  |
| [[InnaputRAT\|S0259]] | InnaputRAT | [InnaputRAT](https://attack.mitre.org/software/S0259) enumerates directories and obtains file attributes on a system.[^246]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to enumerate files and directories on a compromised host.[^612]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) can retrieve file listings from the victim machine.[^416]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) has searched folders and subfolders for files to encrypt.[^408]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) can search for specific files on an infected host.[^270]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to list files upon receiving the `ls` command from C2.[^402]  |
| [[CHOPSTICK\|S0023]] | CHOPSTICK | An older version of [CHOPSTICK](https://attack.mitre.org/software/S0023) has a module that monitors all mounted volumes for files with the extensions .doc, .docx, .pgp, .gpg, .m2f, or .m2o.[^392]  |
| [[StealBit\|S1200]] | StealBit | [StealBit](https://attack.mitre.org/software/S1200) can be configured to exfiltrate specific file types.[^687] [^468]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) has a command to open a file manager and explorer on the system.[^532]   |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) can obtain a list of all files and directories as well as logical drives.[^275]  |
| [[DDKONG\|S0255]] | DDKONG | [DDKONG](https://attack.mitre.org/software/S0255) lists files on the victim’s machine.[^753]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) can use the command code `do_vslist` to send file names, size, and status to C2.[^225]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has used `dir` to search for "programfiles" and "appdata".[^376] 	 |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) can obtain victim drive information as well as a list of folders in C:\Program Files.[^655]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can check for the presence of specific files prior to moving to the next phase of execution.[^634]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) can enumerate and collect items from local drives and folders.[^498]  |
| [[BLACKCOFFEE\|S0069]] | BLACKCOFFEE | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to enumerate files.[^211]  |
| [[Kinsing\|S0599]] | Kinsing | [Kinsing](https://attack.mitre.org/software/S0599) has used the find command to search for specific files.[^147]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can browse file systems using a file manager module.[^93]  |
| [[ZIPLINE\|S1114]] | ZIPLINE | [ZIPLINE](https://attack.mitre.org/software/S1114) can find and append specific files on Ivanti Connect Secure VPNs based upon received commands.[^609]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) collects the victim's %TEMP% directory path and version of Internet Explorer.[^290]  |
| [[Manjusaka\|S1156]] | Manjusaka | [Manjusaka](https://attack.mitre.org/software/S1156) can gather information about specific files on the victim system.[^405]  |
| [[IceApple\|S1022]] | IceApple | The [IceApple](https://attack.mitre.org/software/S1022) Directory Lister module can list information about files and directories including creation time, last write time, name, and size.[^616]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can enumerate drives and their types. It can also change file permissions using cacls.exe.[^727]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can recursively enumerate files in an operator-provided directory.[^41] [^471]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to search for specific files.[^233]  |
| [[Psylo\|S0078]] | Psylo | [Psylo](https://attack.mitre.org/software/S0078) has commands to enumerate all storage devices and to find all files that start with a particular string.[^12]  |
| [[Heyoka Backdoor\|S1027]] | Heyoka Backdoor | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) has the ability to search the compromised host for files.[^752]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of listing files, folders, and drives on a victim.[^607] [^565]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) has the ability to retrieve directory listings.[^504]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) has used `mdfind` to enumerate a list of apps known to grant screen sharing permissions and leverages a module to run the command `ls -la ~/Desktop`.[^717] [^51] <br> |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can collect information on the Windows directory and searches for compressed RAR files on the host.[^568] [^63] [^536]  |
| [[KillDisk\|S0607]] | KillDisk | [KillDisk](https://attack.mitre.org/software/S0607) has used the `FindNextFile` command as part of its file deletion process.[^303]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can exclude specific directories and files from encryption.[^390] [^550]  |
| [[SoreFang\|S0516]] | SoreFang | [SoreFang](https://attack.mitre.org/software/S0516) has the ability to list directories.[^316]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604)’s data wiper component enumerates specific files on all the Windows drives.[^545]  |
| [[LazyWiper\|S9039]] | LazyWiper | [LazyWiper](https://attack.mitre.org/software/S9039) can specifically target multiple files by extension including: .rar, .tar.gz, .zip, .7z, .json, .bcp, .bak, .gho, .erf, .edb, .onepkg, .pst, and .ldiff.[^283]  |
| [[Pcexter\|S1102]] | Pcexter | [Pcexter](https://attack.mitre.org/software/S1102) has the ability to search for files in specified directories.[^418]  |
| [[Pasam\|S0208]] | Pasam | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve lists of files.[^696]  |
| [[BADNEWS\|S0128]] | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) identifies files with certain extensions from USB devices, then copies them to a predefined directory.[^275]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can list contents of drives and search for files.[^359]  |
| [[Remexi\|S0375]] | Remexi | [Remexi](https://attack.mitre.org/software/S0375) searches for files on the system. [^221]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can identify whether it has been run previously on a host by checking for a specified folder.[^371]  |
| [[CookieMiner\|S0492]] | CookieMiner | [CookieMiner](https://attack.mitre.org/software/S0492) has looked for files in the user's home directory with "wallet" in their name using `find`.[^556]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can retrieve data from specific Windows directories, as well as open random files as part of [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497).[^712]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) can browse file systems.[^472] [^435]  |
| [[OSX／Shlayer\|S0402]] | OSX／Shlayer | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used the command `appDir="$(dirname $(dirname "$currentDir"))"` and `$(dirname "$(pwd -P)")` to construct installation paths.[^456] [^278]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) has several commands to search directories for files.[^743] [^682]  |
| [[INC Ransomware\|S1139]] | INC Ransomware | [INC Ransomware](https://attack.mitre.org/software/S1139) can receive command line arguments to encrypt specific files and directories.[^646] [^137]  |
| [[SplatCloak\|S1234]] | SplatCloak | [SplatCloak](https://attack.mitre.org/software/S1234) has used Windows API to identify files associated with Windows Defender and Kaspersky.[^129]  |
| [[FIVEHANDS\|S0618]] | FIVEHANDS | [FIVEHANDS](https://attack.mitre.org/software/S0618) has the ability to enumerate files on a compromised host in order to encrypt files with specific extensions.[^602] [^419]  |
| [[AutoIt backdoor\|S0129]] | AutoIt backdoor | [AutoIt backdoor](https://attack.mitre.org/software/S0129) is capable of identifying documents on the victim with the following extensions: .doc; .pdf, .csv, .ppt, .docx, .pst, .xls, .xlsx, .pptx, and .jpeg.[^389]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) can list files on available disk volumes.[^358] [^345]  |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can recursively search for files in folders and collects files from the desktop with certain extensions.[^189]  |
| [[BACKSPACE\|S0031]] | BACKSPACE | [BACKSPACE](https://attack.mitre.org/software/S0031) allows adversaries to search for files.[^414]  |
| [[Zox\|S0672]] | Zox | [Zox](https://attack.mitre.org/software/S0672) can enumerate files on a compromised host.[^622]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the victim's current directory.[^366]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) can list files and directories.[^392] [^21]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can enumerate files on a compromised host.[^148]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can enumerate directories on a compromise host.[^267]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can enumerate files and directories.[^150]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) can search files on a victim.[^473]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that scans for files in the Documents, Desktop, and Download folders and in other drives.[^719] [^524]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has searched for files within the victim environment for encryption and exfiltration.[^43] [^45] [^566]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also identified files associated with remote management services.[^43] [^45]  |
| [[UNC3886\|G1048]] | UNC3886 |  [UNC3886](https://attack.mitre.org/groups/G1048) has used `vmtoolsd.exe` to enumerate files on guest machines.[^362] [^720]  |
| [[Velvet Ant\|G1047]] | Velvet Ant | [Velvet Ant](https://attack.mitre.org/groups/G1047) has enumerated local files and folders on victim devices.[^311]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has used a batch script to gather folder and file names from victim hosts.[^121] [^393] [^197]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used WizTree to obtain network files and directory listings.[^277]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware can use a common function to identify target files by their extension, and some also enumerate files and directories, including a Destover-like variant that lists files and gathers information for all drives.[^578] [^257] [^662] [^517]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a script that checks `/proc/*/environ` for environment variables related to AWS.[^180]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) used a file listing plugin to collect information about file and directories both on local and remote drives.[^188]  |
| [[admin@338\|G0018]] | admin@338 | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following commands after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to obtain information about files and directories: `dir c:\ >> %temp%\download` `dir "c:\Documents and Settings" >> %temp%\download` `dir "c:\Program Files\" >> %temp%\download` `dir d:\ >> %temp%\download`[^403]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has the ability to enumerate all files and directories on an infected system.[^701] [^626] [^204]  [Kimsuky](https://attack.mitre.org/groups/G0094) has used a custom script with a function called CreateFileList() that can scan all filesystem drives, prioritizing C:\Users, to locate files and file extensions of interest that ultimately generates a file called `FileList.txt` saved within the victims %TEMP% Directory that contains the findings and the respective pathways.[^138]  |
| [[Play\|G1040]] | Play | [Play](https://attack.mitre.org/groups/G1040) has used the Grixba information stealer to list security files and processes.[^318]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has enumerated files on a compromised host.[^425] [^202]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover files in specific locations on the hard disk %TEMP% directory, the current user's desktop, the Program Files directory, and Recent.[^581] [^181]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also searched for files matching the `lPH*.dll` pattern.[^447]  |
| [[Patchwork\|G0040]] | Patchwork | A [Patchwork](https://attack.mitre.org/groups/G0040) payload has searched all fixed drives on the victim for files matching a specified list of extensions.[^442] [^275]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has used [Forfiles](https://attack.mitre.org/software/S0193) to locate PDF, Excel, and Word documents during collection. The group also searched a compromised DCCC computer for specific terms.[^464] [^118]  |
| [[Aoqin Dragon\|G1007]] | Aoqin Dragon | [Aoqin Dragon](https://attack.mitre.org/groups/G1007) has run scripts to identify file formats including Microsoft Word.[^752]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that searched for files with specific patterns.[^511]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) uses command-line interaction to search files and directories.[^132] [^195]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has enumerated directories containing vulnerability testing and cyber related content and facilities data such as construction drawings.[^423]  |
| [[Leafminer\|G0077]] | Leafminer | [Leafminer](https://attack.mitre.org/groups/G0077) used a tool called MailSniper to search for files on the desktop and another utility called Sobolsoft to extract attachments from EML files.[^130]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list a victim's logical drives and the type, as well the total/free space of the fixed devices. Other malware can list a directory's contents.[^689]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has searched file contents on a compromised host.[^669]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has used tools with the ability to search for files on a compromised host.[^226]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that checked if the ProgramData folder had folders or files with the keywords "Kasper," "Panda," or "ESET."[^678]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) have enumerated files and directories, or searched in specific locations within a compromised host.[^676]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor possesses the capability to list files and directories on a machine. [^271] 	<br> |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has collected a list of files from the victim and uploaded it to its C2 server, and then created a new list of specific files to steal.[^161]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has used the BLOODMINE utility to discover files with .css, .jpg, .png, .gif, .ico, .js, and .jsp extensions in Pulse Secure Connect logs.[^487]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has searched the entire target system for DOC, DOCX, PPT, PPTX, XLS, XLSX, and PDF files.[^320] [^301]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has utilized multiple commands to identify data of interest in file and directory listings.[^520]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to enumerate recently modified documents having either a .pdf, .doc, .docx, .xls or .xlsx extension.[^418]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has searched compromised systems for folders of interest including those related to HR, audit and expense, and meeting memos.[^483]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has monitored files' modified time.[^660] 	 |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has run commands to check the content of folders on compromised hosts and has specifically targeted files with .doc, .ppt, .xls, .jtd, .eml, .xps, and .pdf extensions.[^207] [^730] [^526]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) has executed `file /bin/pwd` on exploited victims, perhaps to return architecture related information.[^462]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has used the Windows `dir` command to enumerate files and directories in a victim's network.[^369]  |
| [[Winnti Group\|G0044]] | Winnti Group | [Winnti Group](https://attack.mitre.org/groups/G0044) has used a program named ff.exe to search for specific documents on compromised hosts.[^400]  |
| [[Scattered Spider\|G1015]] | Scattered Spider | [Scattered Spider](https://attack.mitre.org/groups/G1015) Spider enumerates a target organization for files and directories of interest, including source code, user provisioning, MFA device registration, network diagrams, and shared credentials in documents or spreadsheets.[^56] [^128] [^23] [^315] [^538]  |
| [[Windigo\|G0124]] | Windigo | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to check for the presence of files created by OpenSSH backdoors.[^364]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has searched for and collected files on local and network drives.[^593] [^469] [^577]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has conducted key word searches within files and directories on a compromised hosts to identify files for exfiltration.[^77] [^323]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used malware to collect information on files and directories.[^397]  |
| [[Confucius\|G0142]] | Confucius | [Confucius](https://attack.mitre.org/groups/G0142) has used a file stealer that checks the Document, Downloads, Desktop, and Picture folders for documents and images with specific extensions.[^648]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) macros can scan for Microsoft Word and Excel files to inject with additional malicious macros. [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also used its backdoors to automatically list interesting files (such as Office documents) found on a system.[^167] [^143] [^571]  Gamaredon Group has also identified directory trees, folders and files on the compromised host.[^16]   |
| [[Dark Caracal\|G0070]] | Dark Caracal | [Dark Caracal](https://attack.mitre.org/groups/G0070) collected file listings of all default Windows directories.[^503]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that looks for files and directories on the local file system.[^401] [^59]  |
| [[Sowbug\|G0054]] | Sowbug | [Sowbug](https://attack.mitre.org/groups/G0054) identified and extracted all Word documents on a server by using a command containing * .doc and *.docx. The actors also searched for documents based on a specific date range and attempted to identify all installed software on a victim.[^518]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered malicious JavaScript payloads capable of listing folders and emails in exploited email servers.[^543]  |
| [[Lotus Blossom\|G0030]] | Lotus Blossom | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `dir` to examine the local filesystem of victim machines.[^396]  |
| [[APT18\|G0026]] | APT18 | [APT18](https://attack.mitre.org/groups/G0026) can list files information for specific directories.[^391]  |







## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^5]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^6]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^7]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^8]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^9]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^10]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


[^11]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^12]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^13]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^14]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^15]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^16]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^17]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


[^18]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^19]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)


[^20]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^21]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^22]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^23]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^24]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^25]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^26]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^27]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^28]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^29]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^30]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)


[^31]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^32]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^33]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^34]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^35]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)


[^36]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^37]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^38]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^39]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)


[^40]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^41]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^42]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^43]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^44]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^45]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^46]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^47]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^48]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^49]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^50]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^51]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)


[^52]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^53]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^54]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^55]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^56]: [CISA Scattered Spider Advisory November 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)


[^57]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


[^58]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)


[^59]: [evolution of pirpi](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)


[^60]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^61]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^62]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^63]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)


[^64]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^65]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^66]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^67]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^68]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^69]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^70]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^71]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^72]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


[^73]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^74]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^75]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^76]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^77]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^78]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^79]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)


[^80]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^81]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^82]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^83]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^84]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^85]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^86]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^87]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^88]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^89]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^90]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^91]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^92]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^93]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^94]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^95]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^96]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^97]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^98]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^99]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^100]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^101]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^102]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^103]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^104]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^105]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^106]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^107]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)


[^108]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^109]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^110]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^111]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^112]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^113]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^114]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^115]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^116]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^117]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)


[^118]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)


[^119]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^120]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^121]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^122]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^123]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^124]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^125]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)


[^126]: [Trend Micro Cheerscrypt May 2022](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)


[^127]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^128]: [MSTIC Octo Tempest Operations October 2023](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)


[^129]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^130]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^131]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)


[^132]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^133]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^134]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^135]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)


[^136]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^137]: [SentinelOne INC Ransomware](https://www.sentinelone.com/anthology/inc-ransom/)


[^138]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^139]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)


[^140]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^141]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^142]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^143]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^144]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^145]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


[^146]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^147]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)


[^148]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^149]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)


[^150]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^151]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^152]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)


[^153]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^154]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^155]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^156]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^157]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)


[^158]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^159]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^160]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


[^161]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^162]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^163]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^164]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^165]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^166]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^167]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^168]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^169]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^170]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^171]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^172]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^173]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^174]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)


[^175]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^176]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^177]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^178]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^179]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)


[^180]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^181]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^182]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^183]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^184]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^185]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^186]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^187]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^188]: [Symantec Inception Framework March 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)


[^189]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^190]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^191]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)


[^192]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^193]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^194]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^195]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^196]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^197]: [CISA AA20-296A Berserk Bear December 2020](https://www.cisa.gov/uscert/ncas/alerts/aa20-296a#revisions)


[^198]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^199]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^200]: [objective-see windtail1 dec 2018](https://objective-see.com/blog/blog_0x3B.html)


[^201]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^202]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^203]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^204]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^205]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^206]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^207]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^208]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^209]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^210]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^211]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)


[^212]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^213]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^214]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^215]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^216]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


[^217]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^218]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^219]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^220]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^221]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^222]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^223]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^224]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^225]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^226]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^227]: [Trend Micro AvosLocker Apr 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)


[^228]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^229]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^230]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^231]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


[^232]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^233]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^234]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^235]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^236]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^237]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^238]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^239]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^240]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^241]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^242]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^243]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^244]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^245]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^246]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^247]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^248]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^249]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^250]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^251]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^252]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^253]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^254]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^255]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^256]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^257]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^258]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^259]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^260]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^261]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^262]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^263]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^264]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^265]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^266]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^267]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^268]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^269]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^270]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^271]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^272]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^273]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^274]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^275]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^276]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^277]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^278]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


[^279]: [Kroll Royal Deep Dive February 2023](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)


[^280]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^281]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)


[^282]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^283]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)


[^284]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^285]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^286]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^287]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^288]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^289]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)


[^290]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^291]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^292]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^293]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^294]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^295]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^296]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^297]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^298]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^299]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^300]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^301]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^302]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^303]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)


[^304]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^305]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^306]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^307]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^308]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^309]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)


[^310]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^311]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)


[^312]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^313]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^314]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^315]: [CrowdStrike Scattered Spider JUL 2025](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)


[^316]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^317]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^318]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^319]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^320]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^321]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^322]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^323]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^324]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^325]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^326]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


[^327]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^328]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^329]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^330]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^331]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^332]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^333]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^334]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^335]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^336]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^337]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^338]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^339]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^340]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^341]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^342]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)


[^343]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)


[^344]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)


[^345]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^346]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^347]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^348]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^349]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^350]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^351]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^352]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^353]: [Uptycs Black Basta ESXi June 2022](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)


[^354]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^355]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^356]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^357]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^358]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^359]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^360]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^361]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^362]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^363]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)


[^364]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^365]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^366]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^367]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)


[^368]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^369]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^370]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^371]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^372]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^373]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^374]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^375]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)


[^376]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^377]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^378]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^379]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^380]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)


[^381]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^382]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^383]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^384]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^385]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^386]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^387]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^388]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)


[^389]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^390]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)


[^391]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^392]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^393]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^394]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


[^395]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^396]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^397]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^398]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^399]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^400]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^401]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^402]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^403]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^404]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^405]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


[^406]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^407]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)


[^408]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)


[^409]: [Trend Micro Black Basta Spotlight September 2022](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)


[^410]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^411]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)


[^412]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^413]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)


[^414]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^415]: [Camba RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/bkdr_rarstone-new-rat-to-watch-out-for/)


[^416]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^417]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^418]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^419]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)


[^420]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^421]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^422]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^423]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^424]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^425]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^426]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^427]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^428]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^429]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^430]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^431]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)


[^432]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^433]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^434]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^435]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)


[^436]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^437]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^438]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^439]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^440]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)


[^441]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^442]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^443]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^444]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^445]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)


[^446]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^447]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^448]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)


[^449]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^450]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^451]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^452]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^453]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^454]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)


[^455]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^456]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)


[^457]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^458]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^459]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^460]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^461]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^462]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^463]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^464]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


[^465]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)


[^466]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^467]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^468]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


[^469]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^470]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^471]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^472]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^473]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^474]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^475]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^476]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^477]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)


[^478]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^479]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^480]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^481]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^482]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^483]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^484]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^485]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^486]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^487]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^488]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^489]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^490]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^491]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^492]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^493]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^494]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^495]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^496]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^497]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^498]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^499]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^500]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^501]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)


[^502]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^503]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^504]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^505]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^506]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^507]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^508]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^509]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)


[^510]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^511]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^512]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^513]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^514]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^515]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^516]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^517]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^518]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^519]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^520]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^521]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^522]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^523]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)


[^524]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^525]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^526]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^527]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)


[^528]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^529]: [AcidRain JAGS 2022](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)


[^530]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^531]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^532]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^533]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^534]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)


[^535]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^536]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^537]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)


[^538]: [Mandiant VMware vSphere JUL 2025](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)


[^539]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^540]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^541]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^542]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^543]: [ESET WinterVivern 2023](https://www.welivesecurity.com/en/eset-research/winter-vivern-exploits-zero-day-vulnerability-roundcube-webmail-servers/)


[^544]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^545]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^546]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^547]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^548]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^549]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)


[^550]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)


[^551]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^552]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^553]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^554]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^555]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^556]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)


[^557]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^558]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^559]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^560]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^561]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^562]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^563]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^564]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^565]: [ZScaler Hacking Team](http://research.zscaler.com/2015/08/chinese-cyber-espionage-apt-group.html)


[^566]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^567]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


[^568]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^569]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^570]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^571]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^572]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^573]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^574]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^575]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)


[^576]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^577]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^578]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^579]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^580]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)


[^581]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^582]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^583]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^584]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^585]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^586]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^587]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)


[^588]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^589]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^590]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^591]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^592]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^593]: [therecord_redcurl](https://therecord.media/redcurl-hackers-russian-bank-australian-company)


[^594]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^595]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^596]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^597]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^598]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^599]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^600]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^601]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^602]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^603]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^604]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^605]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^606]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^607]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^608]: [Kaspersky Sofacy](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)


[^609]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^610]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^611]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^612]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^613]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^614]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)


[^615]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^616]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^617]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^618]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^619]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^620]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^621]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^622]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^623]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^624]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^625]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)


[^626]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^627]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^628]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^629]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)


[^630]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^631]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^632]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^633]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^634]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^635]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^636]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^637]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^638]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^639]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^640]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^641]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^642]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)


[^643]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^644]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^645]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^646]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^647]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)


[^648]: [TrendMicro Confucius APT Aug 2021](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)


[^649]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^650]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^651]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)


[^652]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^653]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)


[^654]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^655]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^656]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^657]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^658]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^659]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^660]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^661]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^662]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^663]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^664]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^665]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^666]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^667]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^668]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^669]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^670]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)


[^671]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^672]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^673]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^674]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^675]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^676]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^677]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^678]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^679]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^680]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^681]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^682]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^683]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^684]: [Rclone](https://rclone.org)


[^685]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)


[^686]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)


[^687]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^688]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^689]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^690]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^691]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^692]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^693]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)


[^694]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^695]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^696]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


[^697]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^698]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^699]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^700]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^701]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^702]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^703]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^704]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^705]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^706]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^707]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^708]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)


[^709]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^710]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^711]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^712]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^713]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)


[^714]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^715]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^716]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^717]: [Application Bundle Manipulation Brandon Dalton](https://redcanary.com/blog/mac-application-bundles/)


[^718]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^719]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^720]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)


[^721]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^722]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^723]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^724]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^725]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^726]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^727]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^728]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^729]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^730]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^731]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^732]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^733]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^734]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^735]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^736]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^737]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^738]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^739]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)


[^740]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^741]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)


[^742]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^743]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^744]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^745]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^746]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^747]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^748]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^749]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^750]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)


[^751]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^752]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^753]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^754]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^755]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^756]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


