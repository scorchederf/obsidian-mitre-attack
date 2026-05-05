---
aliases: 
    - T1057
mitre-attack: https://attack.mitre.org/techniques/T1057
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1057

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from [Process Discovery](https://attack.mitre.org/techniques/T1057) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>In Windows environments, adversaries could obtain details on running processes using the [Tasklist](https://attack.mitre.org/software/S0057) utility via [cmd](https://attack.mitre.org/software/S0106) or `Get-Process` via [PowerShell](https://attack.mitre.org/techniques/T1059/001). Information about processes can also be extracted from the output of [Native API](https://attack.mitre.org/techniques/T1106) calls such as `CreateToolhelp32Snapshot`. In Mac and Linux, this is accomplished with the `ps` command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.[^675] [^324] <br><br>On network devices, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `show processes` can be used to display current running processes.[^172] [^125] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all running processes on the machine.[^414]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^276]  |
| [[PowerSploit\|S0194]] | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194)'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^191] [^420]  |
| [[Tasklist\|S0057]] | Tasklist | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover processes running on a system.[^345]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can find information about processes running on local and remote systems.[^220] [^311]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can obtain a list of running processes on a compromised host.[^264]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) can examine running processes to determine if a debugger is present.[^463]  |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can enumerate all processes and locate specific process IDs (PIDs).[^489]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can discover running processes on compromised machines.[^535] <br> |
| [[Imminent Monitor\|S0434]] | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.[^68]  |
| [[Donut\|S0695]] | Donut | [Donut](https://attack.mitre.org/software/S0695) includes subprojects that enumerate and identify information about [Process Injection](https://attack.mitre.org/techniques/T1055) candidates.[^250] 	 |
| [[IronNetInjector\|S0581]] | IronNetInjector | [IronNetInjector](https://attack.mitre.org/software/S0581) can identify processes via C# methods such as `GetProcessesByName` and running [Tasklist](https://attack.mitre.org/software/S0057) with the Python `os.popen` function.[^318]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can list the running processes and get the process ID and parent process’s ID.[^181]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) uses module networkDll for process list discovery.[^320] [^45]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to list the victim's processes.[^127]  |
| [[EKANS\|S0605]] | EKANS | [EKANS](https://attack.mitre.org/software/S0605) looks for processes from a hard-coded list.[^503] [^306] [^319]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can enumerate processes on a targeted host.[^269] [^381]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can identify processes based on PID.[^325]  |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) enumerates all running processes.[^625] [^321]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can identify processes associated with analytical tools.[^12] [^479] [^295]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has the ability to check if it is running as an active child process through the detection of a specific environment variable.[^277]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) lists processes running on the system.[^231]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can gather a process list from the victim.[^610]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) gets an output of running processes using the `tasklist` command.[^212]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about running processes.[^201]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) can monitor the `/proc/[PID]` directory of known [RotaJakiro](https://attack.mitre.org/software/S1078) processes as a part of its persistence when executing with non-root permissions. If the process is found dead, it resurrects the process. [RotaJakiro](https://attack.mitre.org/software/S1078) processes can be matched to an associated Advisory Lock, in the `/proc/locks` folder, to ensure it doesn't spawn more than one process.[^436]  |
| [[AvosLocker\|S1053]] | AvosLocker | [AvosLocker](https://attack.mitre.org/software/S1053) has discovered system processes by calling `RmGetList`.[^564]  |
| [[Get2\|S0460]] | Get2 | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify running processes on an infected host.[^415]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) may collect process information by running `tasklist` on a victim.[^251]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) can enumerate current running processes on the targeted machine.[^59]  |
| [[PAKLOG\|S1233]] | PAKLOG | [PAKLOG](https://attack.mitre.org/software/S1233) has detected and logged the full path of processes active in the foreground using Windows API calls.[^122]  |
| [[COATHANGER\|S1105]] | COATHANGER | [COATHANGER](https://attack.mitre.org/software/S1105) will query running process information to determine subsequent program execution flow.[^33]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `tasklist` command.[^57]  |
| [[HALFBAKED\|S0151]] | HALFBAKED | [HALFBAKED](https://attack.mitre.org/software/S0151) can obtain information about running processes on the victim.[^260]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) can obtain a list of running processes on the system.[^283]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has gathered information about running processes.[^595] [^259]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) can stop processes associated with files currently in use to maximize the impact of encryption.[^230]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) checks for running processes on the victim’s machine.[^83]  |
| [[GeminiDuke\|S0049]] | GeminiDuke | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on running processes and environment variables from the victim.[^397]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can enumerate processes on targeted hosts.[^512] [^119] [^388]  |
| [[FrameworkPOS\|S0503]] | FrameworkPOS | [FrameworkPOS](https://attack.mitre.org/software/S0503) can enumerate and exclude selected processes on a compromised host to speed execution of memory scraping.[^346]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) lists the running processes on the system.[^65]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has the capability to query installed programs and running processes.[^150]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also identified running processes using the Python project “psutil”.[^293]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) identifies processes and collects the process ids.[^646]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) can determine if a user is logged in by checking to see if explorer.exe is running.[^355]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) performs the `tasklist` command to list running processes.[^678]  |
| [[WinMM\|S0059]] | WinMM | [WinMM](https://attack.mitre.org/software/S0059) sets a WH_CBT Windows hook to collect information on process creation.[^464]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can enumerate processes on a target system.[^433]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has checked the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler.[^193]  [TONESHELL](https://attack.mitre.org/software/S1239) has also searched for running antivirus processes to include ESET’s antivirus associated executables ekrn.exe and egui.exe.[^352]  |
| [[UPSTYLE\|S1164]] | UPSTYLE | [UPSTYLE](https://attack.mitre.org/software/S1164) has the ability to read `/proc/self/cmdline` to see if it is running as a monitored process.[^123]  |
| [[Kasidet\|S0088]] | Kasidet | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to search for a given process name in processes currently running in the system.[^32]  |
| [[OceanSalt\|S0346]] | OceanSalt | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the name and ID for every process running on the system.[^166]  |
| [[Brave Prince\|S0252]] | Brave Prince | [Brave Prince](https://attack.mitre.org/software/S0252) lists the running processes.[^395]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has utilized an encoded list of the processes that it detects and terminates.[^37] [^173] [^515]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can enumerate processes on a target system.[^433]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can enumerate the current process on a compromised host.[^630]  |
| [[macOS.OSAMiner\|S1048]] | macOS.OSAMiner | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `ps ax | grep <name> | grep -v grep | ...` and `ps ax | grep -E...` to conduct process discovery.[^41]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can discover processes on compromised hosts.[^335]  |
| [[iKitten\|S0278]] | iKitten | [iKitten](https://attack.mitre.org/software/S0278) lists the current processes running.[^487]  |
| [[Bad Rabbit\|S0606]] | Bad Rabbit | [Bad Rabbit](https://attack.mitre.org/software/S0606) can enumerate all running processes to compare hashes.[^8]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to enumerate loaded modules for a process.[^174] . |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has been observed enumerating local processes.[^523]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) contains a command to list processes.[^147] [^204] [^72] 	  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate running processes.[^567]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can retrieve a list of running processes from a compromised machine.[^399]   |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) has a component to check for running processes to look for web browsers.[^213]   |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) has the ability to use [Tasklist](https://attack.mitre.org/software/S0057) to identify running processes.[^214]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has used `tasklist` to gather running processes on victim host.[^510]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also leveraged the `OpenEventA` Windows API function to check whether the same process was already running.[^193]   |
| [[SystemBC\|S9001]] | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) has the ability to enumerate running processes.[^17]    |
| [[Dacls\|S0497]] | Dacls | [Dacls](https://attack.mitre.org/software/S0497) can collect data on running and parent processes.[^209]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can call `NtQuerySystemProcessInformation` with `SystemProcessInformation` to enumerate all running processes, including associated information such as PID, parent PID, image name, and owner.[^180]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can enumerate running processes on a machine.[^35]  |
| [[ELMER\|S0064]] | ELMER | [ELMER](https://attack.mitre.org/software/S0064) is capable of performing process listings.[^30]  |
| [[ShrinkLocker\|S1178]] | ShrinkLocker | [ShrinkLocker](https://attack.mitre.org/software/S1178) checks whether the Bitlocker Drive Encryption Tools service is running.[^446]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) can use the `getprocesslist` command to enumerate processes on a compromised host.[^654] [^533] [^539]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can use `ps aux` to enumerate running processes.[^307]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload information about all running processes to its C2 server.[^10]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can obtain a list of running processes.[^248] [^80]  |
| [[Apostle\|S1133]] | Apostle | [Apostle](https://attack.mitre.org/software/S1133) retrieves a list of all running processes on a victim host, and stops all services containing the string "sql," likely to propagate ransomware activity to database files.[^322]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can gather a list of processes.[^470]  |
| [[WINERACK\|S0219]] | WINERACK | [WINERACK](https://attack.mitre.org/software/S0219) can enumerate processes.[^105]  |
| [[FruitFly\|S0277]] | FruitFly | [FruitFly](https://attack.mitre.org/software/S0277) has the ability to list processes on the system.[^487]  |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has monitored critical processes to ensure resiliency.[^593]   |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) can use the `ps` command to discover other cryptocurrency miners active on the system.[^341]  |
| [[Conti\|S0575]] | Conti | [Conti](https://attack.mitre.org/software/S0575) can enumerate through all open processes to search for any that have the string “sql” in their process name.[^601]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) can identify processes running on the victim machine, such as security software, during execution.[^560] [^26]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) can enumerate the running processes on a compromised host.[^502]  |
| [[Megazord\|S1191]] | Megazord | [Megazord](https://attack.mitre.org/software/S1191) can terminate a list of specified services and processes.[^483]  |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) has used `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next` API calls to enumerate the running processes in the system.[^663]  |
| [[Doki\|S0600]] | Doki | [Doki](https://attack.mitre.org/software/S0600) has searched for the current process’s PID.[^51]  |
| [[Fysbis\|S0410]] | Fysbis | [Fysbis](https://attack.mitre.org/software/S0410) can collect information about running processes.[^526]   |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) can get a list of the processes and running tasks on the system.[^616]  |
| [[UBoatRAT\|S0333]] | UBoatRAT | [UBoatRAT](https://attack.mitre.org/software/S0333) can list running processes on the system.[^651]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) can collect information on installed applications via Windows registry keys, as well as collecting information on running processes.[^103]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can search for different processes on a system.[^86]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to deploy a reconnaissance module to retrieve a list of the active processes.[^659]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) obtains a list of running processes through WMI querying and the `ps` command.[^517]  |
| [[NavRAT\|S0247]] | NavRAT | [NavRAT](https://attack.mitre.org/software/S0247) uses `tasklist /v` to check running processes.[^504]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) can list active processes running on the victim’s machine.[^402]  |
| [[NETEAGLE\|S0034]] | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) can send process listings over the C2 channel.[^378]  |
| [[POORAIM\|S0216]] | POORAIM | [POORAIM](https://attack.mitre.org/software/S0216) can enumerate processes.[^105]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can check if a process name contains “creensaver.”[^576]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can list running processes on the localhost.[^390]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can identify the process that owns remote connections.[^310]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) has gathered a process list by using [Tasklist](https://attack.mitre.org/software/S0057).exe.[^380] [^578] [^112]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) can enumerate and examine running processes to determine if a debugger is present.[^430]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can enumerate all running processes and process information on an infected machine.[^205] 	 |
| [[ObliqueRAT\|S0644]] | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) can check for blocklisted process names on a compromised host.[^71]  |
| [[SHOTPUT\|S0063]] | SHOTPUT | [SHOTPUT](https://attack.mitre.org/software/S0063) has a command to obtain a process listing.[^162]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) has collected information about running processes.[^670]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) can list processes on targeted hosts.[^524]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) has been used to run the `tasklist` command on a compromised system.[^128]  |
| [[XAgentOSX\|S0161]] | XAgentOSX | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getProcessList function to run `ps aux` to get running processes.[^384]  |
| [[LightSpy\|S1185]] | LightSpy | If sent the command `16002`, [LightSpy](https://attack.mitre.org/software/S1185) uses the `NSWorkspace runningApplications()` method to collect the process ID, path to the executable, bundle information, and the filename of the executable for all running applications.[^75]  |
| [[HELLOKITTY\|S0617]] | HELLOKITTY | [HELLOKITTY](https://attack.mitre.org/software/S0617) can search for specific processes to terminate.[^533]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) can enumerate a list of running processes on a compromised system.[^48]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can list the current running processes on the system.[^132] [^372]  |
| [[Babuk\|S0638]] | Babuk | [Babuk](https://attack.mitre.org/software/S0638) has the ability to check running processes on a targeted system.[^471] [^614] [^580]  |
| [[Javali\|S0528]] | Javali | [Javali](https://attack.mitre.org/software/S0528) can monitor processes for open browsers and custom banking applications.[^120]  |
| [[BBSRAT\|S0127]] | BBSRAT | [BBSRAT](https://attack.mitre.org/software/S0127) can list running processes.[^516]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has a module to list the processes running on a machine.[^357]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) can obtain a list of running processes on the victim’s machine.[^434] [^228] [^182]  |
| [[DustySky\|S0062]] | DustySky | [DustySky](https://attack.mitre.org/software/S0062) collects information about running processes from victims.[^136] [^73]  |
| [[Duqu\|S0038]] | Duqu | The discovery modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on process details.[^47]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) can obtain a process list from the victim.[^332]  |
| [[Industroyer2\|S1072]] | Industroyer2 | [Industroyer2](https://attack.mitre.org/software/S1072) has the ability to cyclically enumerate running processes such as PServiceControl.exe, PService_PDD.exe, and other targets supplied through a hardcoded configuration.[^676]  |
| [[Sykipot\|S0018]] | Sykipot | [Sykipot](https://attack.mitre.org/software/S0018) may gather a list of running processes by running `tasklist /v`.[^444]  |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) uses the `tasklist /v` command to obtain a list of processes.[^527] [^635]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can enumerate processes running on a victim's machine.[^29]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can enumerate processes on a targeted system.[^507]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can enumerate processes on compromised hosts.[^240]  |
| [[Akira\|S1129]] | Akira | [Akira](https://attack.mitre.org/software/S1129) verifies the deletion of volume shadow copies by checking for the existence of the process ID related to the process created to delete these items.[^542]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) performs various checks for running processes, including security software by looking for hard-coded process name values.[^633] [^386]   |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can identify and terminate specific services.[^556] [^553]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) can collect a list of running processes from an infected host.[^495]  |
| [[ThiefQuest\|S0595]] | ThiefQuest | [ThiefQuest](https://attack.mitre.org/software/S0595) obtains a list of running processes using the function `kill_unwanted`.[^622]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can enumerate all Common Language Runtimes (CLRs) and running Application Domains in the compromised AD FS server's `Microsoft.IdentityServer.ServiceHost.exe` process.[^275]  |
| [[Carbanak\|S0030]] | Carbanak | [Carbanak](https://attack.mitre.org/software/S0030) lists running processes.[^110]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can monitor processes.[^14] [^247]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can gather a list of processes running on the machine.[^210]   |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) enumerates processes via the `tasklist` command.[^252]  |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can use `tasklist` to gather information about the process running on the infected system.[^592] 	 |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to list processes on the infected host.[^138]  |
| [[Latrodectus\|S1160]] | Latrodectus | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can enumerate running processes including process grandchildren on targeted hosts.[^359] [^145] [^387]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has enumerated running processes on a compromised host to determine if it is running under the process name `dfrgui.exe`.[^585]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can kill a process using specific process ID.[^13] [^315]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to list running processes through the use of `tasklist`.[^235]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to collect running processes.[^156]      |
| [[Bundlore\|S0482]] | Bundlore | [Bundlore](https://attack.mitre.org/software/S0482) has used the `ps` command to list processes.[^131]  |
| [[P8RAT\|S0626]] | P8RAT | [P8RAT](https://attack.mitre.org/software/S0626) can check for specific processes associated with virtual environments.[^656]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) identifies the `explorer.exe` process on the executing system.[^62]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can execute `ProcessList` for process discovery.[^46]  |
| [[LP-Notes\|S9036]] | LP-Notes | [LP-Notes](https://attack.mitre.org/software/S9036) has searched for the process taskhostw.exe.[^156]  |
| [[Royal\|S1073]] | Royal | [Royal](https://attack.mitre.org/software/S1073) can use `GetCurrentProcess` to enumerate processes.[^61]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can use its `Process List` command to enumerate processes on compromised hosts.[^199]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has performed process name checks and has monitored applications.[^407]   |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has utilized MS4Killer to detect running processes on the victim device.[^179]  [Embargo](https://attack.mitre.org/software/S1247) has also captured a snapshot of active running processes using the Windows API `CreateToolHelp32Snapshot()`.[^362]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can use [Tasklist](https://attack.mitre.org/software/S0057) to collect a list of running tasks.[^201] [^588]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) can iterate over the running processes to find a suitable injection target.[^148]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has used the command `cmd /c tasklist` to get a snapshot of the current processes on the target machine.[^343] [^129]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) has the capability to list processes.[^626]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [JHUHUGIT](https://attack.mitre.org/software/S0044) obtains a list of running processes on the victim.[^113] [^52]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect process filenames and SID authority level.[^619]  |
| [[down_new\|S0472]] | down_new | [down_new](https://attack.mitre.org/software/S0472) has the ability to list running processes on a compromised host.[^214]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) can list running processes.[^186]  |
| [[4H RAT\|S0065]] | 4H RAT | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to obtain a listing of running processes (including loaded modules).[^98]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) checks the running processes for evidence it may be running in a sandbox environment. It specifically enumerates processes for Wireshark and Sysinternals.[^467]  |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate processes.[^383]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) has the ability to use `GetWindowThreadProcessId` to identify the process behind a specified window.[^665]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) can enumerate a list of running processes on a compromised machine.[^192]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) runs `tasklist` to obtain running processes.[^429]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can obtain information about process integrity levels.[^94]  |
| [[Derusbi\|S0021]] | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) collects current and parent process IDs.[^648] [^459]  |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) can search a list of running processes.[^656]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can identify installed security tools based on process names.[^121]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) has created a snapshot of running processes using `CreateToolhelp32Snapshot`.[^296]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can identity the current process on a compromised host.[^60]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) lists the system’s processes.[^190] [^56]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) has a command to return a list of running processes.[^157]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can check running processes against a list of blocklisted applications.[^374] <br> |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has called `CreateToolhelp32Snapshot` to enumerate all running processes.[^49]  |
| [[Final1stspy\|S0355]] | Final1stspy | [Final1stspy](https://attack.mitre.org/software/S0355) obtains a list of running processes.[^620]  |
| [[MgBot\|S1146]] | MgBot | [MgBot](https://attack.mitre.org/software/S1146) includes a module for establishing a process watchdog for itself, identifying if the [MgBot](https://attack.mitre.org/software/S1146) process is still running.[^468]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can determine if a running process has administrative privileges and terminate processes that interfere with encryption or exfiltration.[^615] [^411]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) uses the `tasklist` and `wmic process get Capture, ExecutablePath` commands to gather the processes running on the system.[^586] [^603] [^288] [^282] [^511]  |
| [[Pandora\|S0664]] | Pandora | [Pandora](https://attack.mitre.org/software/S0664) can monitor processes on a compromised host.[^155]  |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) checks its parent process for indications that it is running in a sandbox setup.[^2] [^159]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154)'s Beacon payload can collect information on process details.[^289] [^405] [^22]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) collected a list of process names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists.[^96]  |
| [[EvilBunny\|S0396]] | EvilBunny | [EvilBunny](https://attack.mitre.org/software/S0396) has used EnumProcesses() to identify how many process are running in the environment.[^371]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to list running processes on the infected host.[^118]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) has the ability to enumerate running processes on a compromised host.[^422]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) can use `GetCurrentProcessId` for process discovery.[^643]  |
| [[CaddyWiper\|S0693]] | CaddyWiper | [CaddyWiper](https://attack.mitre.org/software/S0693) can obtain a list of current processes.[^582]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) can enumerate the process it is currently running under.[^406]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) has a command to perform a process listing.[^650]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify running processes and associated plugins on an infected host.[^305]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to list processes on the compromised host.[^242]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) can identify the process it is currently running under and its number, and pass this back to a command and control node.[^322]  |
| [[Carbon\|S0335]] | Carbon | [Carbon](https://attack.mitre.org/software/S0335) can list the processes on the victim’s machine.[^261]  |
| [[TRAILBLAZE\|S9012]] | TRAILBLAZE | [TRAILBLAZE](https://attack.mitre.org/software/S9012) has conducted process discovery by searching for specific named processes such as `/home/bin/web`.[^299] [^634]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) contains watchdog functionality that ensures its process is always running, else spawns a new instance.[^279]  |
| [[BISCUIT\|S0017]] | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to enumerate running processes and identify their owners.[^650]  |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) checks the running processes on the victim’s machine.[^395]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can gather a list of running processes by using [Tasklist](https://attack.mitre.org/software/S0057).[^9]  |
| [[AshTag\|S9031]] | AshTag | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component has process management functionality.[^106]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) has collected a list of running processes.[^284]  |
| [[NKAbuse\|S1107]] | NKAbuse | [NKAbuse](https://attack.mitre.org/software/S1107) will check victim systems to ensure only one copy of the malware is running.[^565]  |
| [[Pillowmint\|S0517]] | Pillowmint | [Pillowmint](https://attack.mitre.org/software/S0517) can iterate through running processes every six seconds collecting a list of processes to capture from later.[^314] 	 |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can enumerate running processes.[^55]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to discover processes, including `Bka.exe` and `BkavUtil.exe`.[^264]  |
| [[SUNSPOT\|S0562]] | SUNSPOT | [SUNSPOT](https://attack.mitre.org/software/S0562) monitored running processes for instances of `MsBuild.exe` by hashing the name of each running process and comparing it to the corresponding value `0x53D525`. It also extracted command-line arguments and individual arguments from the running `MsBuild.exe` process to identify the directory path of the Orion software Visual Studio solution.[^364]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can collect information about running processes.[^143]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) can identify running processes on a compromised host.[^585]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) collects a list of running services with the command `tasklist /v`.[^613]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can gather process information on targeted systems.[^641] [^104]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) can list running processes.[^379]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) can enumerate all processes on the victim's machine.[^375]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to list all running processes.[^373]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) collects a list of running processes.[^253]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) has a command, ps, to obtain a listing of processes on the system.[^484]   |
| [[SPAWNCHIMERA\|S9024]] | SPAWNCHIMERA | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has searched for running processes to include web or dsmdm.[^163] [^344]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `tasklist` command.[^351] 	 |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) can obtain a list of processes running on the system.[^586] [^288]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can check if the explorer.exe process is responsible for calling its install function.[^571]  |
| [[BLACKCOFFEE\|S0069]] | BLACKCOFFEE | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to discover processes.[^196]  |
| [[Kinsing\|S0599]] | Kinsing | [Kinsing](https://attack.mitre.org/software/S0599) has used ps to list processes.[^139]  |
| [[Meteor\|S0688]] | Meteor | [Meteor](https://attack.mitre.org/software/S0688) can check if a specific process is running, such as Kaspersky's `avp.exe`.[^590]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can search a list of running processes for Tr.exe.[^168]  |
| [[ZIPLINE\|S1114]] | ZIPLINE | [ZIPLINE](https://attack.mitre.org/software/S1114) can identify running processes and their names.[^548]  |
| [[Maze\|S0449]] | Maze | [Maze](https://attack.mitre.org/software/S0449) has gathered all of the running system processes.[^472] 	 |
| [[HIUPAN\|S1230]] | HIUPAN | [HIUPAN](https://attack.mitre.org/software/S1230) has conducted process discovery to identify the [PUBLOAD](https://attack.mitre.org/software/S1228) malware under the process WCBrowserWatcher.exe and will launch it from an install directory if it is not found.[^510]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) collects its process identifier (PID) on the victim.[^124]  |
| [[PowerStallion\|S0393]] | PowerStallion | [PowerStallion](https://attack.mitre.org/software/S0393) has been used to monitor process lists.[^408]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can list running processes.[^655]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can enumerate the processes that run on the platform.[^35] [^431]  |
| [[Heyoka Backdoor\|S1027]] | Heyoka Backdoor | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can gather process information.[^677]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) has used shell commands to list running processes.[^458]  |
| [[KillDisk\|S0607]] | KillDisk | [KillDisk](https://attack.mitre.org/software/S0607) has called `GetCurrentProcess`.[^272]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can define specific processes to be terminated or left alone at execution.[^361] [^42] [^413] [^76] [^497] [^664]  |
| [[SoreFang\|S0516]] | SoreFang | [SoreFang](https://attack.mitre.org/software/S0516) can enumerate processes on a victim machine through use of [Tasklist](https://attack.mitre.org/software/S0057).[^281]  |
| [[Socksbot\|S0273]] | Socksbot | [Socksbot](https://attack.mitre.org/software/S0273) can list all running processes.[^249]  |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can list the current running processes on the system.[^609]  |
| [[Pasam\|S0208]] | Pasam | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve lists of running processes.[^624]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) has used `get_tasklist` to discover processes on the compromised host.[^432]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can retrieve a list of running processes.[^337]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has checked for the Google Updater process to ensure [Goopy](https://attack.mitre.org/software/S0477) was loaded properly.[^612]  |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the PID of a malicious process.[^366]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) searches for different processes on the system.[^207]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) has the ability to check running processes.[^347]  |
| [[SYSCON\|S0464]] | SYSCON | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to use [Tasklist](https://attack.mitre.org/software/S0057) to list running processes.[^637]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can enumerate running processes.[^639]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) can query and kill system processes.[^396]  |
| [[Helminth\|S0170]] | Helminth | [Helminth](https://attack.mitre.org/software/S0170) has used [Tasklist](https://attack.mitre.org/software/S0057) to get information on processes.[^246]  |
| [[Komplex\|S0162]] | Komplex | The OsInfo function in [Komplex](https://attack.mitre.org/software/S0162) collects a running process list.[^513]  |
| [[INC Ransomware\|S1139]] | INC Ransomware | [INC Ransomware](https://attack.mitre.org/software/S1139) can use the Microsoft Win32 Restart Manager to kill processes with a specific handle or that are accessing resources it wants to encrypt.[^581]  |
| [[Waterbear\|S0579]] | Waterbear | [Waterbear](https://attack.mitre.org/software/S0579) can identify the process for a specific security product.[^308]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) uses the `tasklist` to view running processes on the victim’s machine.[^660]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) has a plugin designed to obtain a list of processes.[^338] [^440]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567)’s dropper can list all running processes.[^333] [^323]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) used the `ps` command to monitor the running processes on the system.[^54] 	 |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can collect a list of running processes by calling CreateToolhelp32Snapshot.[^177] [^309]  |
| [[BACKSPACE\|S0031]] | BACKSPACE | [BACKSPACE](https://attack.mitre.org/software/S0031) may collect information about running processes.[^378]  |
| [[Zox\|S0672]] | Zox | [Zox](https://attack.mitre.org/software/S0672) has the ability to list processes.[^561]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) can list running processes.[^363]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can obtain a list of processes on a compromised host.[^241]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has enumerated processes by ID, name, or privileges.[^140]   |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a hard-coded security tool process list that identifies and terminates using an undocumented IOCTL code 0x222094.[^37]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 to perform process discovery by executing `tasklist /v`. Additionally, WsTaskLoad.exe executes `tasklist /v` to perform process discovery.[^290]    |
| [[UNC3886\|G1048]] | UNC3886 | [UNC3886](https://attack.mitre.org/groups/G1048) has run scripts to list all running processes on a guest VM from an ESXi host.[^645]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has run `tasklist` on a victim's machine and used infostealers to capture processes.[^144] [^245]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families gather a list of running processes on a victim system and send it to their C2 server. A Destover-like variant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) also gathers process times.[^522] [^263] [^334] [^231] [^209] [^594]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for rival malware and removes it if found.[^642]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also searched for running processes containing the strings aliyun or liyun to identify machines running Alibaba Cloud Security tools.[^169]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to identify active processes and other associated loaded modules.[^176]  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used [Tasklist](https://attack.mitre.org/software/S0057) to obtain information from a compromised host.[^544]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) can gather a list of all processes running on a victim's machine.[^566]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained running processes on the victim device utilizing PowerShell cmdlet `Get-Process`.[^183]  |
| [[Play\|G1040]] | Play | <br>[Play](https://attack.mitre.org/groups/G1040) has used the information stealer Grixba to check for a list of security processes.[^285]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover running processes using the `tasklist /v` command.[^527]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also enumerated processes associated with specific open ports or named pipes.[^408]  |
| [[APT28\|G0007]] | APT28 | An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan will enumerate the victim's processes searching for explorer.exe if its current process does not have necessary permissions.[^246]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has enumerated processes on targeted systems.[^109]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) malware can collect a list of running processes on a system.[^142]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) performs process discovery using `tasklist` commands.[^126] [^301]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has enumerated running processes on targeted systems including through the use of [Tasklist](https://attack.mitre.org/software/S0057).[^671] [^425] [^385]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list running processes.[^618]  |
| [[Andariel\|G0138]] | Andariel | [Andariel](https://attack.mitre.org/groups/G0138) has used `tasklist` to enumerate processes and find a specific string.[^469]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `tasklist` to enumerate processes.[^602]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to obtain a list of running processes on the system.[^608] [^331]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) leveraged Sysmon to understand the processes, services in the organization.[^146]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has used Windows-based utilities to carry out tasks including tasklist.exe. [^447]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `tasklist /v` to determine active process information.[^287]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also used [TONESHELL](https://attack.mitre.org/software/S1239) malware to check the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler.[^193]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used `tasklist` to enumerate processes.[^474]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has run `cmd /c start /b tasklist` to enumerate processes.[^381]  |
| [[Storm-0501\|G1053]] | Storm-0501 | [Storm-0501](https://attack.mitre.org/groups/G1053) has discovered running processes through `tasklist.exe`.[^481]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) is capable of enumerating the running processes on the system using `pslist`.[^437] [^592]  |
| [[Molerats\|G0021]] | Molerats | [Molerats](https://attack.mitre.org/groups/G0021) actors obtained a list of active processes on the victim and sent them to C2 servers.[^136]  |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers a list of running processes.[^382]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [Tasklist](https://attack.mitre.org/software/S0057) on compromised hosts for discovery.[^477]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067)'s Freenki malware lists running processes using the Microsoft Windows API.[^376]  |
| [[Winnti Group\|G0044]] | Winnti Group | [Winnti Group](https://attack.mitre.org/groups/G0044) looked for a specific process running on infected servers.[^369]  |
| [[Rocke\|G0106]] | Rocke | [Rocke](https://attack.mitre.org/groups/G0106) can detect a running process's PID on the infected machine.[^667] 	 |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to identify running processes on the victim's machine.[^367]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126)’s shellcode attempted to find the process ID of the current process.[^496]  |
| [[Windshift\|G0112]] | Windshift | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to enumerate active processes.[^67]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used tools to enumerate processes on target hosts including Process Explorer.[^424] [^137] [^16]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can list out currently running processes.[^370] [^53]  |
| [[APT1\|G0006]] | APT1 | [APT1](https://attack.mitre.org/groups/G0006) gathered a list of running processes on the system using `tasklist /v`.[^115]  |
| [[Deep Panda\|G0009]] | Deep Panda | [Deep Panda](https://attack.mitre.org/groups/G0009) uses the Microsoft [Tasklist](https://attack.mitre.org/software/S0057) utility to list processes running on systems.[^506]  |
| [[Poseidon Group\|G0033]] | Poseidon Group | After compromising a victim, [Poseidon Group](https://attack.mitre.org/groups/G0033) lists all running processes.[^491]  |







## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)


[^9]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^10]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^11]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^12]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^13]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^14]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^15]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^16]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^17]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^18]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^19]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^20]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^21]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^22]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^23]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^24]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^25]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^26]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)


[^27]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^28]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^29]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^30]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)


[^31]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^32]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^33]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)


[^34]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^35]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^36]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^37]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^38]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^39]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^40]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^41]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)


[^42]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)


[^43]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^44]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^45]: [Bitdefender Trickbot March 2020](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)


[^46]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^47]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)


[^48]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^49]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^50]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^51]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


[^52]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^53]: [evolution of pirpi](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)


[^54]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^55]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^56]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^57]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^58]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^59]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^60]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^61]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^62]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^63]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^64]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^65]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^66]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^67]: [BlackBerry Bahamut](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)


[^68]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)


[^69]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^70]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^71]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^72]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^73]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^74]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^75]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^76]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)


[^77]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^78]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^79]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^80]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^81]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^82]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^83]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^84]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^85]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^86]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^87]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^88]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^89]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^90]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^91]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^92]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^93]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^94]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^95]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^96]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^97]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^98]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^99]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^100]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^101]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^102]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^103]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^104]: [Cato LAMEHUG JUL 2025](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)


[^105]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^106]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^107]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^108]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^109]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^110]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)


[^111]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^112]: [ESET BlackEnergy Jan 2016](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)


[^113]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^114]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^115]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^116]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^117]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^118]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^119]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)


[^120]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


[^121]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^122]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^123]: [Palo Alto MidnightEclipse APR 2024](https://unit42.paloaltonetworks.com/cve-2024-3400/)


[^124]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^125]: [show_processes_cisco_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_monitor_permit_list_through_show_process_memory.html#wp3599497760)


[^126]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^127]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^128]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^129]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^130]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^131]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)


[^132]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)


[^133]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^134]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^135]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^136]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


[^137]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^138]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^139]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)


[^140]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^141]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^142]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^143]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^144]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^145]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^146]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^147]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^148]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^149]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^150]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^151]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^152]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^153]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^154]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^155]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^156]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^157]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^158]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^159]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^160]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^161]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^162]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)


[^163]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)


[^164]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^165]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^166]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^167]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^168]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^169]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^170]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^171]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^172]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^173]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^174]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^175]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^176]: [Symantec Inception Framework March 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)


[^177]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^178]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^179]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^180]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^181]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^182]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^183]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^184]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^185]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^186]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^187]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^188]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^189]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^190]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^191]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^192]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^193]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^194]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^195]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^196]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)


[^197]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^198]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^199]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^200]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^201]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^202]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^203]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^204]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^205]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^206]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^207]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^208]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^209]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


[^210]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^211]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^212]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^213]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^214]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^215]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^216]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^217]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^218]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^219]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^220]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^221]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^222]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^223]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^224]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^225]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^226]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^227]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^228]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^229]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^230]: [CISA RansomHub AUG 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)


[^231]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^232]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^233]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^234]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^235]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^236]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^237]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^238]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^239]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^240]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^241]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^242]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^243]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^244]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^245]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^246]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^247]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^248]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^249]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^250]: [Donut Github](https://github.com/TheWover/donut)


[^251]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^252]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^253]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^254]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^255]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^256]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^257]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^258]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^259]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)


[^260]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


[^261]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)


[^262]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^263]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^264]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^265]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^266]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^267]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^268]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^269]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^270]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^271]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^272]: [Trend Micro KillDisk 2](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)


[^273]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^274]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^275]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^276]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^277]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^278]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^279]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^280]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^281]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^282]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^283]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^284]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)


[^285]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^286]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^287]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^288]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)


[^289]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)


[^290]: [BlackBerry_FIN7_April2024](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)


[^291]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^292]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^293]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^294]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^295]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)


[^296]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^297]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^298]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^299]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^300]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^301]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^302]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^303]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^304]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^305]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^306]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)


[^307]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^308]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


[^309]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)


[^310]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^311]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^312]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^313]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^314]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)


[^315]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^316]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^317]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^318]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


[^319]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


[^320]: [ESET Trickbot Oct 2020](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)


[^321]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)


[^322]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^323]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^324]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^325]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^326]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^327]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^328]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^329]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^330]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^331]: [ClearSky MuddyWater June 2019](https://www.clearskysec.com/wp-content/uploads/2019/06/Clearsky-Iranian-APT-group-%E2%80%98MuddyWater%E2%80%99-Adds-Exploits-to-Their-Arsenal.pdf)


[^332]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^333]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^334]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^335]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)


[^336]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^337]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^338]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)


[^339]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^340]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^341]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^342]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^343]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^344]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^345]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)


[^346]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)


[^347]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^348]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^349]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^350]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^351]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^352]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)


[^353]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^354]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^355]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^356]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^357]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^358]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^359]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^360]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^361]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)


[^362]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)


[^363]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^364]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


[^365]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^366]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^367]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^368]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^369]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^370]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^371]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)


[^372]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^373]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^374]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^375]: [Mcafee Clop Aug 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)


[^376]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^377]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^378]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^379]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^380]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^381]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^382]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^383]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^384]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^385]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^386]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)


[^387]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^388]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)


[^389]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^390]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^391]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^392]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^393]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^394]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^395]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^396]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)


[^397]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^398]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^399]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^400]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^401]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^402]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^403]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^404]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^405]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^406]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^407]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^408]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^409]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^410]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^411]: [SentinelOne LockBit 2.0](https://www.sentinelone.com/anthology/lockbit-2-0/)


[^412]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^413]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)


[^414]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^415]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^416]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^417]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^418]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^419]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^420]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^421]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^422]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^423]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^424]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)


[^425]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^426]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^427]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^428]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^429]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^430]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^431]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^432]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^433]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^434]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^435]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^436]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)


[^437]: [Unit 42 Tropic Trooper Nov 2016](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)


[^438]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^439]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^440]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^441]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^442]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^443]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^444]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)


[^445]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^446]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)


[^447]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^448]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^449]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^450]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^451]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^452]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^453]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^454]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^455]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^456]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^457]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^458]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^459]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^460]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^461]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^462]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^463]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^464]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^465]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^466]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^467]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^468]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^469]: [Kaspersky Andariel Ransomware June 2021](https://securelist.com/andariel-evolves-to-target-south-korea-with-ransomware/102811/)


[^470]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^471]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)


[^472]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)


[^473]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^474]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^475]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^476]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^477]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^478]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^479]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^480]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^481]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^482]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^483]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^484]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^485]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^486]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^487]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^488]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^489]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^490]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^491]: [Kaspersky Poseidon Group](https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/)


[^492]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^493]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^494]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^495]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^496]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^497]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)


[^498]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^499]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^500]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^501]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^502]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^503]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)


[^504]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


[^505]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^506]: [Alperovitch 2014](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)


[^507]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^508]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^509]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^510]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^511]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^512]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^513]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)


[^514]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^515]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^516]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


[^517]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^518]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^519]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^520]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^521]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^522]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^523]: [ASEC Emotet 2017](https://global.ahnlab.com/global/upload/download/asecreport/ASEC%20REPORT_vol.88_ENG.pdf)


[^524]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^525]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^526]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)


[^527]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^528]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^529]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^530]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^531]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^532]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^533]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^534]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^535]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^536]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^537]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^538]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^539]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^540]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^541]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^542]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^543]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^544]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^545]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^546]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^547]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^548]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^549]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^550]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^551]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^552]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^553]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)


[^554]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^555]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^556]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)


[^557]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^558]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^559]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^560]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)


[^561]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^562]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^563]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^564]: [Malwarebytes AvosLocker Jul 2021](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)


[^565]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)


[^566]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^567]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^568]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^569]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^570]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^571]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^572]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^573]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^574]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^575]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^576]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^577]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^578]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)


[^579]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^580]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^581]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)


[^582]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)


[^583]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^584]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^585]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^586]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^587]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^588]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^589]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^590]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)


[^591]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^592]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^593]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^594]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^595]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)


[^596]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^597]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^598]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^599]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^600]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^601]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^602]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^603]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)


[^604]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^605]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^606]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^607]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^608]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^609]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)


[^610]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^611]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^612]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^613]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^614]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)


[^615]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^616]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^617]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^618]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^619]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^620]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^621]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^622]: [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)


[^623]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^624]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


[^625]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^626]: [FireEye Hacking Team](https://www.fireeye.com/blog/threat-research/2015/07/demonstrating_hustle.html)


[^627]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^628]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^629]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^630]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^631]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^632]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^633]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^634]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^635]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)


[^636]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^637]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


[^638]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^639]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^640]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^641]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^642]: [Trend Micro TeamTNT](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)


[^643]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^644]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^645]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)


[^646]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^647]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^648]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^649]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^650]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^651]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)


[^652]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^653]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^654]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^655]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^656]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^657]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^658]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^659]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^660]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^661]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^662]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^663]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^664]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^665]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^666]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^667]: [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)


[^668]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^669]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^670]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^671]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^672]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^673]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^674]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^675]: [Sygnia ESXi Ransomware 2025](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)


[^676]: [Industroyer2 Mandiant April 2022](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)


[^677]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^678]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^679]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^680]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^681]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


