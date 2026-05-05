---
aliases: 
    - T1005
mitre-attack: https://attack.mitre.org/techniques/T1005
tactic: 
     - Collection
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1005

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.<br><br>Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as [cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008), which have functionality to interact with the file system to gather information.[^38]  Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.<br>


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[NPPSPY\|S1131]] | NPPSPY | [NPPSPY](https://attack.mitre.org/software/S1131) records data entered from the local system logon at Winlogon to capture credentials in cleartext.[^165]  |
| [[PowerSploit\|S0194]] | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^147] [^350]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can collect files and information from a compromised host.[^214]  |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to upload files from a compromised system.[^417]  |
| [[TruffleHog\|S9009]] | TruffleHog | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data from home directories of the victim environment.[^336]  |
| [[Out1\|S0594]] | Out1 | [Out1](https://attack.mitre.org/software/S0594) can copy files and Registry data from compromised hosts.[^415]  |
| [[Forfiles\|S0193]] | Forfiles | [Forfiles](https://attack.mitre.org/software/S0193) can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^356]  |
| [[MCMD\|S0500]] | MCMD | [MCMD](https://attack.mitre.org/software/S0500) has the ability to upload files from an infected device.[^401]  |
| [[esentutl\|S0404]] | esentutl | [esentutl](https://attack.mitre.org/software/S0404) can be used to collect data from local file systems.[^179]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can download files off the target system to send back to the server.[^497] [^80]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can retrieve files from compromised client machines.[^35]  |
| [[Wevtutil\|S0645]] | Wevtutil | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to export events from a specific log.[^102] [^320]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) collects local files and information from the victim’s local machine.[^519]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN |  [BLINDINGCAN](https://attack.mitre.org/software/S0520) has uploaded files from victim machines.[^346]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can collect data from a compromised host.[^260] [^431]  |
| [[QuietSieve\|S0686]] | QuietSieve | [QuietSieve](https://attack.mitre.org/software/S0686) can collect files from a compromised host.[^39]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can capture and compress stolen credentials from the Registry and volume shadow copies.[^453]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has commands that allow the actor download files from the compromised host to the C2 server, and to also download specific sections of a file.[^228]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) can collect information from a compromised host.[^482]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) searches the local system and gathers data.[^188]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) collects files with the following extensions: .ppt, .pptx, .pdf, .doc, .docx, .xls, .xlsx, .docm, .rtf, .inp, .xlsm, .csv, .odt, .pps, .vcf and sends them back to the C2 server.[^170]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) can gather information from compromised hosts.[^42]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to collect data from a compromised machine to deliver to the attacker.[^300]   |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) has collected files and data from a compromised host.[^517]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has collected files from victim machines, including certificates and cookies.[^209]  |
| [[CASTLETAP\|S1224]] | CASTLETAP | [CASTLETAP](https://attack.mitre.org/software/S1224) can execute a C2 command to transfer files from victim machines.[^109]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can collect data and files from a compromised host.[^398]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can download files from the victim's computer.[^435] [^36]  |
| [[FrameworkPOS\|S0503]] | FrameworkPOS | [FrameworkPOS](https://attack.mitre.org/software/S0503) can collect elements related to credit card data from process memory.[^279]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf.[^46]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected data utilizing a script that contained a list of excluded files and directory names and naming patterns of interest such as environment and configuration files, documents, spreadsheets, and other files that contained the words secret, wallet, private, and password.[^51]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) collects files from the local system.[^548]  |
| [[SharpDisco\|S1089]] | SharpDisco | [SharpDisco](https://attack.mitre.org/software/S1089) has dropped a recent-files stealer plugin to `C:\Users\Public\WinSrcNT\It11.exe`.[^562]  |
| [[xCaon\|S0653]] | xCaon | [xCaon](https://attack.mitre.org/software/S0653) has uploaded files from victims' machines.[^281]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) has the capability to upload collected files to C2.[^366]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to collect recently changed files on a compromised host.[^366]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can collect data on a compromised host.[^537] [^143]  |
| [[TinyTurla\|S0668]] | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) can upload files from a compromised host.[^551]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [CosmicDuke](https://attack.mitre.org/software/S0050) steals user files from local hard drives with file extensions that match a predefined list.[^307]  |
| [[EnvyScout\|S0634]] | EnvyScout | [EnvyScout](https://attack.mitre.org/software/S0634) can collect sensitive NTLM material from a compromised host.[^375]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can collect information from a compromised host.[^52]  |
| [[Tomiris\|S0671]] | Tomiris | [Tomiris](https://attack.mitre.org/software/S0671) has the ability to collect recent files matching a hardcoded list of extensions prior to exfiltration.[^387]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can gather data from infected systems.[^483]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) searches the File system for files of interest.[^171]   |
| [[PowerLess\|S1012]] | PowerLess | [PowerLess](https://attack.mitre.org/software/S1012) has the ability to exfiltrate data, including Chrome and Edge browser database files, from compromised machines.[^160] <br> |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) can collect local data from an infected machine.[^255]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can collect data from a compromised host.[^303]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can send files from the victim machine to C2.[^267] [^491]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can collect information from a compromised host.[^135]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can collect files and information from a compromised host.[^27]  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer | [AuTo Stealer](https://attack.mitre.org/software/S1029) can collect data such as PowerPoint files, Word documents, Excel files, PDF files, text files, database files, and image files from an infected machine.[^255]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) has collected data and files from a compromised host.[^554] [^458]  |
| [[FLASHFLOOD\|S0036]] | FLASHFLOOD | [FLASHFLOOD](https://attack.mitre.org/software/S0036) searches for interesting files (either a default or customized set of file extensions) on the local system. [FLASHFLOOD](https://attack.mitre.org/software/S0036) will scan the My Recent Documents, Desktop, Temporary Internet Files, and TEMP directories. [FLASHFLOOD](https://attack.mitre.org/software/S0036) also collects information stored in the Windows Address Book.[^308]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has collected information and files from a compromised machine.[^148]  |
| [[LoFiSe\|S1101]] | LoFiSe | [LoFiSe](https://attack.mitre.org/software/S1101) can collect files of interest from targeted systems.[^309]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) exfiltrates data collected from the victim mobile device.[^9]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can collect data from the system, and can monitor changes in specified directories.[^202]  |
| [[P.A.S. Webshell\|S0598]] | P.A.S. Webshell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) has the ability to copy files on a compromised host.[^380]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can upload files from a victim's machine.[^137]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can upload data from the victim's machine to the C2 server.[^61]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) uploads files from a specified directory to the C2 server.[^437]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can collect files from compromised hosts.[^495]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can copy files and directories from a compromised host.[^318]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) can collect information from a compromised host.[^363]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) has collected data and files from a compromised host.[^158]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) has the capability to upload collected files to a C2.[^342] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can collect data from a local system.[^543]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has uploaded files from victims' machines.[^488]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) can collect data from a compromised host, including Windows authentication information.[^98]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) has collected data and other information from a compromised host.[^503]  |
| [[Green Lambert\|S0690]] | Green Lambert | [Green Lambert](https://attack.mitre.org/software/S0690) can collect data from a compromised host.[^97]  |
| [[China Chopper\|S0020]] | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can upload local files.[^393] [^525] [^211] [^515]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has exfiltrated data collected from local systems.[^48] [^51] [^236] [^261]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can collect host data and specific file types.[^301] [^494] [^341]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) can collect files from a compromised host.[^200]  |
| [[BlackMould\|S0564]] | BlackMould | [BlackMould](https://attack.mitre.org/software/S0564) can copy files on a compromised host.[^247]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has collected information from a compromised host.[^136]   |
| [[Rover\|S0090]] | Rover | [Rover](https://attack.mitre.org/software/S0090) searches for files on local drives based on a predefined list of file extensions.[^272]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) can collect files from a local system.[^526]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can collect information from a compromised host.[^431]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) has stolen `sitemanager.xml` and `recentservers.xml` from `%APPDATA%\FileZilla\` if present.[^312]   |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) has the ability to upload files from victim's machines.[^571]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) can collect data from an infected host.[^423]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) can retrieve configuration data from a compromised AD FS server.[^227]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can read data from files.[^12] [^201]  |
| [[CreepyDrive\|S1023]] | CreepyDrive | [CreepyDrive](https://attack.mitre.org/software/S1023) can upload files to C2 from victim machines.[^384]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to collect information from the local database.[^166]   |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can collect information from an air-gapped host machine.[^508] 	 |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can collect data from a compromised host using a stealer module.[^313]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can collect files and information from a compromised host.[^226]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can upload files from infected hosts to the C2.[^11] [^146] [^252]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can collect data and files from a compromised host.[^192]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has collected local data from a compromised host to include desktop cryptocurrency wallet data, and documents from within Desktop, Documents, and Downloads.[^469]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can use its `Get` command to exfiltrate specified files from the compromised system.[^154]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) can collect local files from the system .[^212]   |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has stored collected information and discovered processes in a tmp file.[^99]  |
| [[RAPIDPULSE\|S1113]] | RAPIDPULSE | [RAPIDPULSE](https://attack.mitre.org/software/S1113) retrieves files from the victim system via encrypted commands sent to the web shell.[^376]  |
| [[DnsSystem\|S1021]] | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) can upload files from infected machines after receiving a command with `uploaddd` in the string.[^447]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) can send a file containing victim system information to C2.[^139]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) can collect data from a local system.[^141]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has collected data stored locally including chat logs and files associated with chat services such as Steam, Discord, and Telegram.[^334]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) can upload files from a compromised host.[^281]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can use a file monitor to steal specific files from targeted systems.[^562]  |
| [[Crutch\|S0538]] | Crutch | [Crutch](https://attack.mitre.org/software/S0538) can exfiltrate files from compromised systems.[^282]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to access the file system on a compromised host.[^343]  |
| [[Hikit\|S0009]] | Hikit | [Hikit](https://attack.mitre.org/software/S0009) can upload files from compromised machines.[^478]  |
| [[WellMail\|S0515]] | WellMail | [WellMail](https://attack.mitre.org/software/S0515) can exfiltrate files from the victim machine.[^293]  |
| [[RawPOS\|S0169]] | RawPOS | [RawPOS](https://attack.mitre.org/software/S0169) dumps memory from specific processes on a victim system, parses the dumped files, and scrapes them for credit card data.[^223] [^302] [^248]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) can collect data from a compromised host.[^238]  |
| [[Drovorub\|S0502]] | Drovorub | [Drovorub](https://attack.mitre.org/software/S0502) can transfer files from the victim machine.[^291]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) can upload files to its C2.[^89] [^397]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can retrieve information from the infected machine.[^43]  |
| [[BadPatch\|S0337]] | BadPatch | [BadPatch](https://attack.mitre.org/software/S0337) collects files from the local system that have the following extensions, then prepares them for exfiltration: .xls, .xlsx, .pdf, .mdb, .rar, .zip, .doc, .docx.[^304]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can upload files from the victim machine to C2 nodes.[^555] [^408]  |
| [[Cryptoistic\|S0498]] | Cryptoistic | [Cryptoistic](https://attack.mitre.org/software/S0498) can retrieve files from the local file system.[^561]  |
| [[MgBot\|S1146]] | MgBot | [MgBot](https://attack.mitre.org/software/S1146) includes modules for collecting files from local systems based on a given set of properties and filenames.[^22]  |
| [[ccf32\|S1043]] | ccf32 | [ccf32](https://attack.mitre.org/software/S1043) can collect files from a compromised host.[^214]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can collect data from a local system.[^133] [^18]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) collected information from a compromised host.[^32] [^73]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) can leverage an exfiltration module to download arbitrary files from compromised machines.[^220]  |
| [[PinchDuke\|S0048]] | PinchDuke | [PinchDuke](https://attack.mitre.org/software/S0048) collects user files from the compromised host based on predefined file extensions.[^324]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can upload files from a compromised host.[^89]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has the ability to upload files from a compromised host.[^344]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) can upload data and files from a victim's machine.[^509]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) can upload files from a compromised host.[^333]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can steal system information.[^162]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to steal documents from the local system including the print spooler queue.[^246]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) collects data from victim machines based on configuration information received from command and control nodes.[^184] [^128]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) can identify specific files and folders for follow-on exfiltration.[^257]  |
| [[DanBot\|S1014]] | DanBot | [DanBot](https://attack.mitre.org/software/S1014) can upload files from compromised hosts.[^163]  |
| [[Calisto\|S0274]] | Calisto | [Calisto](https://attack.mitre.org/software/S0274) can collect data from user directories.[^428]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can collect Microsoft Word documents from the target's file system, as well as `.txt`, `.doc`, and `.xls` files from the Internet Explorer cache.[^297] [^8] 	 |
| [[Pillowmint\|S0517]] | Pillowmint | [Pillowmint](https://attack.mitre.org/software/S0517) has collected credit card data using native API functions.[^251]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can collect then exfiltrate files from the compromised system.[^40]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can upload files from victims' machines.[^214] [^527]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can collect information and files from a compromised host.[^111]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) can collect information from a compromised host.[^502]  |
| [[PUNCHTRACK\|S0197]] | PUNCHTRACK | [PUNCHTRACK](https://attack.mitre.org/software/S0197) scrapes memory for properly formatted payment card data.[^402] [^149]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) has the ability to collect system information and files of interest from compromised systems.[^112] [^545]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can collect data and files from a compromised host.[^467]  |
| [[StealBit\|S1200]] | StealBit | [StealBit](https://attack.mitre.org/software/S1200) can upload data and files to the LockBit victim-shaming site.[^528] [^359]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can transfer files from a compromised host.[^411]  |
| [[SLIGHTPULSE\|S1110]] | SLIGHTPULSE | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can read files specified on the local system.[^94]  |
| [[SPAWNCHIMERA\|S9024]] | SPAWNCHIMERA | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has extracted the device’s Linux kernel image (vmlinux).[^123] [^241] [^540]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) gathers information from infected systems such as SSH information from the victim's `.ssh` directory.[^454]  [Troll Stealer](https://attack.mitre.org/software/S1196) collects information from local FileZilla installations and Microsoft Sticky Note.[^388]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can collect data from a local system.[^62]  |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022) can collect files, passwords, and other data from a compromised host.[^471]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can collect files and system information from a compromised host.[^27] [^362]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to upload files from a compromised host.[^167]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) has collected files and data from a compromised host.[^517]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) collects contacts and application data from files in Desktop, Documents, Downloads, Dropbox, and WeChat folders.[^230]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can exfiltrate files from the system using a documents collector tool.[^412]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) can collect data from an infected local host.[^100]  |
| [[Pcexter\|S1102]] | Pcexter | [Pcexter](https://attack.mitre.org/software/S1102) can upload files from targeted systems.[^309]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can upload logs and other data from a compromised host.[^84]  |
| [[Pasam\|S0208]] | Pasam | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve files.[^532]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) can upload files from compromised hosts.[^316]  |
| [[BADNEWS\|S0128]] | BADNEWS | When it first starts, [BADNEWS](https://attack.mitre.org/software/S0128) crawls the victim's local drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt.[^294] [^364]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can obtain data from local systems.[^268]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has the ability to exfiltrate documents from infected systems.[^524] 	 |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can use a variety of commands, including esentutl.exe to steal sensitive data from Internet Explorer and Microsoft Edge, to acquire information that is subsequently exfiltrated.[^79] [^419]  |
| [[CookieMiner\|S0492]] | CookieMiner | [CookieMiner](https://attack.mitre.org/software/S0492) has retrieved iPhone text messages from iTunes phone backup files.[^429]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can collect data from a compromised host.[^543]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) can collect a variety of information from victim machines.[^258]  |
| [[Zox\|S0672]] | Zox | [Zox](https://attack.mitre.org/software/S0672) has the ability to upload files from a targeted system.[^478]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) can upload files to the C2 from infected machines.[^328] [^2]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can collect data from a compromised host.[^107]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can collect data from a compromised host.[^197]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has uploaded files and information from victim machines.[^108]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has collected files and data from compromised machines.[^547] [^406]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has collected data from a compromised host prior to exfiltration.[^95]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has collected files and other sensitive information from a compromised network.[^365]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has collected data from local victim systems.[^90]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has used PowerShell to upload files from compromised systems.[^72]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has searched local system resources to access sensitive documents.[^203]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has collected data and files from compromised networks.[^444] [^213] [^277] [^398]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) captured local Windows security event log data from victim machines using the `wevtutil` utility to extract contents to an `evtx` output file.[^177]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) used a file hunting plugin to collect .txt, .pdf, .xls or .doc files from the infected host.[^558]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has collected Office, PDF, and HWP documents from its victims.[^536] [^481]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also harvested victim files through the use of the `RecentFiles()` function that collects paths of recently accessed files by parsing .lnk shortcuts from `%APPDATA%\Microsoft\Windows\Recent`.[^103]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has exfiltrated internal documents, files, and other data from compromised hosts.[^314]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can upload files from victim machines.[^335]  |
| [[Ember Bear\|G1003]] | Ember Bear | [Ember Bear](https://attack.mitre.org/groups/G1003) gathers victim system information such as enumerating the volume of a given device or extracting system and security event logs for analysis.[^305] [^377]  |
| [[FIN6\|G0037]] | FIN6 | [FIN6](https://attack.mitre.org/groups/G0037) has collected and exfiltrated payment card data from compromised systems.[^278] [^355] [^274]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) collected and exfiltrated files from the infected system.[^331]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has retrieved internal documents from machines inside victim environments, including by using [Forfiles](https://attack.mitre.org/software/S0193) to stage documents before exfiltration.[^356] [^87] [^434] [^505]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) gathered information and files from local directories for exfiltration.[^96] [^137]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has stolen files from a sensitive file server and the Active Directory database from targeted environments, and used [Wevtutil](https://attack.mitre.org/software/S0645) to extract event log information.[^299] [^354] [^311]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a web shell to exfiltrate a ZIP file containing a dump of LSASS memory on a compromised machine.[^296] [^351]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has stolen data from compromised hosts.[^569]  |
| [[Andariel\|G0138]] | Andariel | [Andariel](https://attack.mitre.org/groups/G0138) has collected large numbers of files from compromised network systems for later extraction.[^276]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected data and files from a compromised machine.[^515] [^86]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has used various tools to steal files from the compromised host.[^485] [^161]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has collected data from a compromised host.[^521]  |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has exfiltrated files stolen from local systems.[^114]  |
| [[LAPSUS$\|G1004]] | LAPSUS$ | [LAPSUS$](https://attack.mitre.org/groups/G1004) uploaded sensitive files, information, and credentials from a targeted organization for extortion or public release.[^253]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has run scripts to collect documents from targeted hosts.[^309]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has collected various files from the compromised computers.[^69] [^373] <br> |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers data from the local victim system.[^310]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) gathered data and files of interest from victim's systems.[^555]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) has collected data from victims' local systems.[^81]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has collected cached data and files from within the victim environment.[^315] [^570] [^477]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) has uploaded files and data from a compromised host.[^215]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has gathered stolen credentials, sensitive data such as point-of-sale (POS), and ATM data from a compromised network before exfiltration.[^280] [^339]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) collected data from the victim's local system, including password hashes from the SAM hive in the Registry.[^287]  |
| [[CURIUM\|G1012]] | CURIUM | [CURIUM](https://attack.mitre.org/groups/G1012) has exfiltrated data from a compromised machine.[^499]  |
| [[Windigo\|G0124]] | Windigo | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to gather credentials in files left on disk by OpenSSH backdoors.[^273]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has collected data from the local disk of compromised hosts.[^360] [^443]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) ran a command to compile an archive of file types of interest from the victim user's directories.[^124]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has collected files from infected systems and uploaded them to a C2 server.[^119] [^438]   |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) gathered data from database and other critical servers in victim environments, then used wiping mechanisms as an anti-analysis and anti-forensics mechanism.[^169]  |
| [[Axiom\|G0001]] | Axiom | [Axiom](https://attack.mitre.org/groups/G0001) has collected data from a compromised network.[^478]  |
| [[Dark Caracal\|G0070]] | Dark Caracal | [Dark Caracal](https://attack.mitre.org/groups/G0070) collected complete contents of the 'Pictures' folder from compromised Windows systems.[^392]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) will identify Microsoft Office documents on the victim's computer.[^329]  |
| [[APT1\|G0006]] | APT1 | [APT1](https://attack.mitre.org/groups/G0006) has collected files from a local victim.[^91]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Data Loss Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |





## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^9]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^10]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^11]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^12]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^13]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^14]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^15]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^16]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^17]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^18]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^19]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^20]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^21]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^22]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)


[^23]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^24]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^25]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^26]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^27]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^28]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^29]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^30]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^31]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^32]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^33]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^34]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^35]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^36]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)


[^37]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^38]: [show_run_config_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733)


[^39]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^40]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^41]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^42]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^43]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^44]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^45]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^46]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^47]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^48]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^49]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^50]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^51]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^52]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^53]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^54]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^55]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^56]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^57]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^58]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^59]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^60]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^61]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^62]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^63]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^64]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^65]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^66]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^67]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^68]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^69]: [DOJ APT10 Dec 2018](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)


[^70]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^71]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^72]: [Trend Micro Earth Simnavaz October 2024](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)


[^73]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^74]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^75]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^76]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^77]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^78]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^79]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)


[^80]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^81]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^82]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^83]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^84]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^85]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^86]: [Microsoft Silk Typhoon MAR 2025](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)


[^87]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)


[^88]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^89]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^90]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^91]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^92]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^93]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^94]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^95]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^96]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^97]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)


[^98]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^99]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^100]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^101]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^102]: [Wevtutil Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)


[^103]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^104]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^105]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^106]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^107]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^108]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^109]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^110]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^111]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^112]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^113]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^114]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^115]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^116]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^117]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^118]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^119]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^120]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^121]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^122]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^123]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)


[^124]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


[^125]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^126]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^127]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^128]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^129]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^130]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^131]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^132]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^133]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)


[^134]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^135]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^136]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^137]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^138]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^139]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^140]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^141]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^142]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^143]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^144]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^145]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^146]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^147]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^148]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^149]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^150]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^151]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^152]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^153]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^154]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^155]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^156]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^157]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^158]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^159]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^160]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)


[^161]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^162]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^163]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^164]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^165]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)


[^166]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^167]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^168]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^169]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^170]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^171]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^172]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^173]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^174]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^175]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^176]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^177]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^178]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^179]: [Red Canary 2021 Threat Detection Report March 2021](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)


[^180]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^181]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^182]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^183]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^184]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^185]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^186]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^187]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^188]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^189]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^190]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^191]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^192]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^193]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^194]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^195]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^196]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^197]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^198]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^199]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^200]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^201]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^202]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^203]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^204]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^205]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^206]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^207]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^208]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^209]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)


[^210]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^211]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^212]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^213]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^214]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^215]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^216]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^217]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^218]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^219]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^220]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^221]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^222]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^223]: [Kroll RawPOS Jan 2017](https://www.kroll.com/en/insights/publications/malware-analysis-report-rawpos-malware)


[^224]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^225]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^226]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^227]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^228]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^229]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^230]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^231]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^232]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)


[^233]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^234]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^235]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^236]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^237]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^238]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^239]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^240]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^241]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^242]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^243]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^244]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^245]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^246]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^247]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^248]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)


[^249]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^250]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^251]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)


[^252]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^253]: [MSTIC DEV-0537 Mar 2022](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)


[^254]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^255]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^256]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^257]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^258]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^259]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^260]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^261]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^262]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^263]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^264]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^265]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^266]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^267]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^268]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^269]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^270]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^271]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^272]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)


[^273]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^274]: [RiskIQ Newegg September 2018](https://web.archive.org/web/20181209083100/https://www.riskiq.com/blog/labs/magecart-newegg/)


[^275]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^276]: [FSI Andariel Campaign Rifle July 2017](https://fsiceat.tistory.com/2)


[^277]: [Novetta Blockbuster RATs](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)


[^278]: [Trend Micro FIN6 October 2019](https://www.trendmicro.com/en_us/research/19/j/fin6-compromised-e-commerce-platform-via-magecart-to-inject-credit-card-skimmers-into-thousands-of-online-shops.html)


[^279]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)


[^280]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^281]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^282]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^283]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^284]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^285]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^286]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^287]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^288]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^289]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^290]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^291]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)


[^292]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^293]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^294]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^295]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^296]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^297]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^298]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^299]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^300]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^301]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^302]: [TrendMicro RawPOS April 2015](http://sjc1-te-ftp.trendmicro.com/images/tex/pdf/RawPOS%20Technical%20Brief.pdf)


[^303]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^304]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)


[^305]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^306]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^307]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)


[^308]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^309]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^310]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^311]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^312]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)


[^313]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^314]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^315]: [SPECOPS Outpost24 Handala Hack Stryker March 2026](https://specopssoft.com/blog/stryker-cyber-attack-what-we-know-remote-wipe/)


[^316]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^317]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^318]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^319]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^320]: [F-Secure Lazarus Cryptocurrency Aug 2020](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)


[^321]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^322]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^323]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^324]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^325]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^326]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^327]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^328]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^329]: [aptsim](http://carnal0wnage.attackresearch.com/2012/09/more-on-aptsim.html)


[^330]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^331]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^332]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^333]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^334]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)


[^335]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^336]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)


[^337]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^338]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^339]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^340]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^341]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^342]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^343]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^344]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^345]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^346]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^347]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^348]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^349]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^350]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^351]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^352]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^353]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^354]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^355]: [RiskIQ British Airways September 2018](https://web.archive.org/web/20181231220607/https://riskiq.com/blog/labs/magecart-british-airways-breach/)


[^356]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


[^357]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^358]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^359]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


[^360]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^361]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^362]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^363]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^364]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)


[^365]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^366]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^367]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^368]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^369]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^370]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^371]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^372]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^373]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^374]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^375]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^376]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^377]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^378]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^379]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^380]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^381]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^382]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^383]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^384]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^385]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^386]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^387]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)


[^388]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^389]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^390]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^391]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^392]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^393]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^394]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^395]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^396]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^397]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^398]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^399]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^400]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^401]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


[^402]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^403]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^404]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^405]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^406]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^407]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^408]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^409]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^410]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^411]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^412]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^413]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^414]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^415]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^416]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^417]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^418]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^419]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^420]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^421]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^422]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^423]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^424]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^425]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^426]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^427]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^428]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)


[^429]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)


[^430]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^431]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^432]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^433]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^434]: [TrendMicro Pawn Storm 2019](https://documents.trendmicro.com/assets/white_papers/wp-pawn-storm-in-2019.pdf)


[^435]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^436]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^437]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^438]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^439]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^440]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^441]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^442]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^443]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^444]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^445]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^446]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^447]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


[^448]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^449]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^450]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^451]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^452]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^453]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)


[^454]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^455]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^456]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^457]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^458]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^459]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^460]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^461]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^462]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^463]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^464]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^465]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^466]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^467]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^468]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^469]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^470]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^471]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^472]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^473]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^474]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^475]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^476]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^477]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^478]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^479]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^480]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^481]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^482]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^483]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^484]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^485]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


[^486]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^487]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^488]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^489]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^490]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^491]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^492]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^493]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^494]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^495]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^496]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^497]: [Github Koadic](https://github.com/offsecginger/koadic)


[^498]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^499]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^500]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^501]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^502]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^503]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^504]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^505]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^506]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^507]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^508]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^509]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)


[^510]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^511]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^512]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^513]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^514]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^515]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^516]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^517]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^518]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^519]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^520]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^521]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^522]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^523]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^524]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^525]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)


[^526]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^527]: [Kaspersky APT Trends Q1 2020](https://securelist.com/apt-trends-report-q1-2020/96826/)


[^528]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^529]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^530]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^531]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^532]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


[^533]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^534]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^535]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^536]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^537]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^538]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^539]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^540]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^541]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^542]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^543]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^544]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^545]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^546]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^547]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^548]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^549]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^550]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^551]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^552]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^553]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^554]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^555]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^556]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^557]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^558]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^559]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^560]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^561]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^562]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^563]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^564]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^565]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^566]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^567]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^568]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^569]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^570]: [DOJ FBI Handala Hack March 2026](https://www.justice.gov/opa/media/1431956/dl?inline)


[^571]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^572]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^573]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^574]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


