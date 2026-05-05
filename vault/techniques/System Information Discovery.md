---
aliases: 
    - T1082
mitre-attack: https://attack.mitre.org/techniques/T1082
tactic: 
     - Discovery
platforms:
     - ESXi - IaaS - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1082

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [Local Storage Discovery](https://attack.mitre.org/techniques/T1680) which is an adversary's discovery of local drive, disks and/or volumes.<br><br>Tools such as [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather detailed system information (e.g. `show version`).[^204]  On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.[^388] [^31] <br><br>Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.[^239] [^97] [^134] <br><br>[System Information Discovery](https://attack.mitre.org/techniques/T1082) combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.[^226] [^308]  


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Covenant\|S1155]] | Covenant | [Covenant](https://attack.mitre.org/software/S1155) implants can gather basic information on infected systems.[^682]  |
| [[Diskpart\|S9002]] | Diskpart | [Diskpart](https://attack.mitre.org/software/S9002) can show information about the selected disk, partition, volume, or virtual hard disk (VHD).[^627]   |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the operating system name and specific Windows version of an infected machine.[^513]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including OS version.[^337]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^266] [^374]  |
| [[dsquery\|S0105]] | dsquery | [dsquery](https://attack.mitre.org/software/S0105) has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.[^681]  |
| [[PoshC2\|S0378]] | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^357]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can collect the OS version and process architecture of compromised hosts.[^665]  |
| [[Systeminfo\|S0096]] | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather information about the operating system.[^51]  |
| [[cmd\|S0106]] | cmd | [cmd](https://attack.mitre.org/software/S0106) can be used to find information about the operating system.[^384]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can obtain the OS version and build, computer name, and processor architecture from a compromised host.[^123]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can grab a system’s information including the OS version, architecture, etc.[^213]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can gather system information from the victim’s machine including the OS type.[^783]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) gathers the OS version, machine name, CPU type, amount of RAM available, and UEFI/BIOS firmware information from the victim’s machine.[^757] [^794] [^479] [^455]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get information about the victim's name, build, version, serial number, and memory usage.[^150]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has collected from a victim machine the system name, processor information, and OS version.[^518]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can obtain the computer name and information on the OS from targeted hosts.[^331] [^465]  |
| [[Pikabot\|S1145]] | Pikabot | [Pikabot](https://attack.mitre.org/software/S1145) performs a variety of system checks and gathers system information, including commands such as `whoami`.[^325] [^299]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can gather system information from a compromised host.[^389]  |
| [[Spark\|S0543]] | Spark | [Spark](https://attack.mitre.org/software/S0543) can collect the hostname, keyboard layout, and language from the system.[^366]   |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) gathers computer names, OS version info, and also checks installed keyboard layouts to estimate if it has been launched from a certain list of countries.[^781]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can enumerate the OS version and domain on a targeted system.[^405] [^12] [^596]  |
| [[MURKYTOP\|S0233]] | MURKYTOP | [MURKYTOP](https://attack.mitre.org/software/S0233) has the capability to retrieve information about the OS.[^570]  |
| [[GRIFFON\|S0417]] | GRIFFON | [GRIFFON](https://attack.mitre.org/software/S0417) has used a reconnaissance module that can be used to retrieve information about a victim's computer, including the resolution of the workstation .[^383]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) has collected the computer name and OS version from a compromised machine.[^225] [^708]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) collects the OS version, country name, MAC address, computer name, and physical memory statistics.[^282]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can gather the victim OS version and whether it is 64 or 32 bit.[^765]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) can gather information on the operating system on the victim’s machine.[^801]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) gathers the computer name, CPU information, Microsoft Windows version, and runs the command `systeminfo`.[^257]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about the OS and computer name.[^241] [^439]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) collects system information including computer and domain names, OS version, and S7P paths.[^712]  |
| [[IronWind\|S9029]] | IronWind | [IronWind](https://attack.mitre.org/software/S9029) can capture the OS version and computer name of the compromised host.[^165]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) executes a set of commands to collect device information, including `uname`.  Another example is the `cat /etc/*release | uniq` command used to collect the current OS distribution.[^540]  |
| [[Get2\|S0460]] | Get2 | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify the computer name and Windows version of an infected host.[^514]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) may collect information about the system by running `hostname` and `systeminfo` on a victim.[^311]  |
| [[SharpStage\|S0546]] | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546) has checked the system settings to see if Arabic is the configured language.[^586]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to collect the computer name, and CPU manufacturer name from a compromised machine. [Sardonic](https://attack.mitre.org/software/S1085) also has the ability to execute the `ver` and `systeminfo` commands.[^62]  |
| [[HALFBAKED\|S0151]] | HALFBAKED | [HALFBAKED](https://attack.mitre.org/software/S0151) can obtain information about the OS, processor, and BIOS.[^321]  |
| [[Misdat\|S0083]] | Misdat | The initial beacon packet for [Misdat](https://attack.mitre.org/software/S0083) contains the operating system version of the victim.[^755]  |
| [[Emissary\|S0082]] | Emissary | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute ver and systeminfo commands.[^118]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) has the capability to collect the computer name, language settings, the OS version, CPU information, and time elapsed since system start.[^345]  |
| [[BUBBLEWRAP\|S0043]] | BUBBLEWRAP | [BUBBLEWRAP](https://attack.mitre.org/software/S0043) collects system information, including the operating system version and hostname.[^449]  |
| [[HAWKBALL\|S0391]] | HAWKBALL | [HAWKBALL](https://attack.mitre.org/software/S0391) can collect the OS version, architecture information, and computer name.[^633]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used [Systeminfo](https://attack.mitre.org/software/S0096) to gather system information.[^746]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can collect system profile information from a compromised host.[^576]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) can retrieve information about virtual machines.[^430]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) has the ability to enumerate system information.[^755]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) can gather extended system information including the hostname, OS version number, platform, memory information, time elapsed since system startup, and CPU information.[^484] [^135]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034) has collected the machine’s MAC address, total memory, GPU information and other system information.[^685]   |
| [[LITTLELAMB.WOOLTEA\|S1121]] | LITTLELAMB.WOOLTEA | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can check the type of Ivanti VPN device it is running on by executing `first_run()` to identify the first four bytes of the motherboard serial number.[^9]  |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) collects the system information, including hostname and OS version, and sends it to the C2 server.[^218]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) collects the OS version, system architecture, computer name, product ID, install date, and information on the keyboard mapping to determine the language used on the system.[^393] [^100]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can gather system information including hostname, domain, and OS details.[^480]  |
| [[CARROTBAT\|S0462]] | CARROTBAT | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to determine the operating system of the compromised host and whether Windows is being run with x86 or x64 architecture.[^713] [^799]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) collects the MAC address, computer name, and CPU information.[^75]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected OS type, hostname and system version through the "pay" module.[^276] [^82]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also queried the victim device using Python scripts to obtain the User and Hostname.[^599] [^355]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) gathers system information, network addresses, and the operation system version.[^807] [^136]  |
| [[HAPPYWORK\|S0214]] | HAPPYWORK | can collect system information, including computer name, system manufacturer, IsDebuggerPresent state, and execution path.[^124]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) collects general system enumeration data about the infected machine and checks the OS version.[^838]  |
| [[Pony\|S0453]] | Pony | [Pony](https://attack.mitre.org/software/S0453) has collected the Service Pack, language, and region information to send to the C2.[^730] 	 |
| [[WinMM\|S0059]] | WinMM | [WinMM](https://attack.mitre.org/software/S0059) collects the system name, OS version including service pack, and system install date and sends the information to the C2 server.[^578]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has the ability to retrieve the name of the infected machine.[^272] [^424] [^409]  |
| [[Kasidet\|S0088]] | Kasidet | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to obtain a victim's system name and operating system version.[^36]  |
| [[OceanSalt\|S0346]] | OceanSalt | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the computer name from the system.[^197]  |
| [[Brave Prince\|S0252]] | Brave Prince | [Brave Prince](https://attack.mitre.org/software/S0252) collects hard drive content and system configuration information.[^491]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has collected data from the SMBIOS firmware table using `GetSystemFirmwareTable`.[^639]    |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can identify the OS version of a targeted system.[^789]  |
| [[macOS.OSAMiner\|S1048]] | macOS.OSAMiner | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) can gather the device serial number.[^46]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can discover and collect victim system information.[^656]  |
| [[EnvyScout\|S0634]] | EnvyScout | [EnvyScout](https://attack.mitre.org/software/S0634) can determine whether the ISO payload was received by a Windows or iOS device.[^552]  |
| [[SslMM\|S0058]] | SslMM | [SslMM](https://attack.mitre.org/software/S0058) sends information to its hard-coded C2, including OS version, service pack information, processor speed, system name, and OS install date.[^578]  |
| [[IMAPLoader\|S1152]] | IMAPLoader | [IMAPLoader](https://attack.mitre.org/software/S1152) uses WMI queries to gather information about the victim machine.[^39]  |
| [[Gomir\|S1198]] | Gomir | [Gomir](https://attack.mitre.org/software/S1198) collects information on infected systems such as hostname, username, CPU, and RAM information.[^664]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the hostname, computer name, Windows version, processor speed, and machine GUID on a compromised host.[^206]  |
| [[BOLDMOVE\|S1184]] | BOLDMOVE | [BOLDMOVE](https://attack.mitre.org/software/S1184) performs system survey actions following initial execution.[^504]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect the victim PC name and operating system.[^177] [^244] [^83]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) reads the value of the infected system's `HKLM\SYSTEM\Microsoft\Cryptography\MachineGUID` value.[^709]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can retrieve system information including OS version, memory usage, local hostname, and system adapter information.[^662]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can obtain current system information from a compromised machine such as the `SHELL PID`, `PSVERSION`, `HOSTNAME`, `LOGONSERVER`, `LASTBOOTUP`, OS type/version, bitness, and hostname.[^561] [^493]   |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) collects the hostname of the target computer.[^258]   |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the hostname, OS version, and OS architecture of an infected host.[^381]  |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) has the ability to identify the OS architecture on a compromised host.[^259]  |
| [[Prikormka\|S0113]] | Prikormka | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about Windows OS version, computer name, battery info, and physical memory.[^35]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has collected and sent system information including volume serial number, computer name, and system uptime to designated C2.[^33] [^272]   [PUBLOAD](https://attack.mitre.org/software/S1228) has also used several commands executed in sequence via `cmd` in a short interval to gather system information about the infected host including `systeminfo`.[^634]  [PUBLOAD](https://attack.mitre.org/software/S1228) has decrypted shellcode that collects the computer name.[^227]  |
| [[SystemBC\|S9001]] | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) has collected username  , build number and serial number, then sent the information to the C2 server.[^16] [^126]  [SystemBC](https://attack.mitre.org/software/S9001) has also gathered device name, operating system, and processor type.[^669]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) can inspect the User-Agent string in GET request header information to determine the operating system of targeted systems.[^806]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can retrieve the hostname of a compromised host.[^456]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can identify the computer name of a compromised host.[^399] [^720]  |
| [[DropBook\|S0547]] | DropBook | [DropBook](https://attack.mitre.org/software/S0547) has checked for the presence of Arabic language in the infected machine's settings.[^394]   |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve the following information from an infected machine: OS, architecture, computer name, OS build version, and environment variables.[^212]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can collect the computer name of a compromised host.[^41] [^533]  |
| [[KARAE\|S0215]] | KARAE | [KARAE](https://attack.mitre.org/software/S0215) can collect system information.[^124]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has gathered victim computer information and configurations.[^469]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has identified the OS and MAC address of victim device through host fingerprinting scripting.[^728]  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer | [AuTo Stealer](https://attack.mitre.org/software/S1029) has the ability to collect the hostname and OS information from an infected host.[^381]  |
| [[ShrinkLocker\|S1178]] | ShrinkLocker | [ShrinkLocker](https://attack.mitre.org/software/S1178) uses WMI queries to gather various information about the victim machine and operating system.[^90] [^553]  |
| [[Hildegard\|S0601]] | Hildegard | [Hildegard](https://attack.mitre.org/software/S0601) has collected the host's OS, CPU, and memory information.[^542]  |
| [[SLOWDRIFT\|S0218]] | SLOWDRIFT | [SLOWDRIFT](https://attack.mitre.org/software/S0218) collects and sends system information to its C2.[^124]  |
| [[SHUTTERSPEED\|S0217]] | SHUTTERSPEED | [SHUTTERSPEED](https://attack.mitre.org/software/S0217) can collect system information.[^124]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) can execute `getinfo` to enumerate the computer name and OS version of a compromised system.[^815]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can collect the victim's operating system and computer name during the initial infection.[^55]  |
| [[Snip3\|S1086]] | Snip3 | [Snip3](https://attack.mitre.org/software/S1086) has the ability to query `Win32_ComputerSystem` for system information. [^56]   |
| [[Rifdoor\|S0433]] | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the Windows version on the compromised host.[^140]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed collecting victim machine information like OS version.[^661]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can gather information about the OS version and hardware on compromised hosts.[^370] [^835]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to upload to its C2 server victim mobile device information, including IMEI, IMSI, SIM card serial number, phone number, Android version, and other information.[^10]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can gather information on the OS version, computer name, DEP policy, and memory size.[^306] [^93]  |
| [[Naid\|S0205]] | Naid | [Naid](https://attack.mitre.org/software/S0205) collects a unique identifier (UID) from a compromised host.[^641]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can gather system information, the computer name, OS version, drive and serial information from the victim's machine.[^833] [^322] [^585]  |
| [[WINERACK\|S0219]] | WINERACK | [WINERACK](https://attack.mitre.org/software/S0219) can gather information about the host.[^124]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) gathers the victim's computer name, Windows version, and system language, and then sends it to its C2 server.[^96]  |
| [[AcidPour\|S1167]] | AcidPour | [AcidPour](https://attack.mitre.org/software/S1167) can identify various system locations and mapped devices on Linux systems as a precursor to wiping activity.[^460]  |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to check whether the infected system’s OS is Debian or RHEL/CentOS to determine which cryptocurrency miner it should use.[^744]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) can collect computer name, locale information, and information about the OS and architecture.[^615]  |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) has discovered the OS version, CPU model, and RAM size of the system it has been installed on.[^408]  |
| [[Line Dancer\|S1186]] | Line Dancer | [Line Dancer](https://attack.mitre.org/software/S1186) can gather system configuration information by running the native `show configuration` command.[^723]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can collect the OS version and computer name from a compromised host.[^215]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) performs several system checks as part of anti-analysis mechanisms, including querying the operating system build number, processor vendor and type, video controller, and CPU temperature.[^29]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) collects the OS version, computer name, and language ID.[^624]  |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) can collect the computer name and OS version from the system.[^824]  |
| [[RustyWater\|S9037]] | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) has gathered the victim machine’s computer name.[^67]      |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) can obtain the computer name and UUID.[^66]  |
| [[Fysbis\|S0410]] | Fysbis | [Fysbis](https://attack.mitre.org/software/S0410) has used the command `ls /etc | egrep -e"fedora\*|debian\*|gentoo\*|mandriva\*|mandrake\*|meego\*|redhat\*|lsb-\*|sun-\*|SUSE\*|release"` to determine which Linux OS version is running.[^644]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) has the ability to identify the computer name and OS version on a compromised host.[^73] [^24]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) collects the OS name, machine name, and architecture information.[^771]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on the victim system such as CPU and Computer name as well as device drivers.[^122]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can obtain the computer name from a compromised host.[^101]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has collected system information on the infected host.[^827]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on the system.[^642]  |
| [[NavRAT\|S0247]] | NavRAT | [NavRAT](https://attack.mitre.org/software/S0247) uses `systeminfo` on a victim’s machine.[^626]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) can collect the computer name, RAM used, and operating system version from the victim’s machine.[^506] [^498]  |
| [[POORAIM\|S0216]] | POORAIM | [POORAIM](https://attack.mitre.org/software/S0216) can identify system information, including battery status.[^124]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can collect the user name, Windows version, computer name, and available space on discs from a compromised host.[^485]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can collect the computer name, system architecture, default language, and processor frequency of a compromised host.[^372]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) has used [Systeminfo](https://attack.mitre.org/software/S0096) to gather the OS version, as well as information on the system configuration, BIOS, the motherboard, and the processor.[^463] [^727]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can obtain the victim PC name and OS version.[^471]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can detect the computer name and operating system.[^245] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) has the ability to obtain the computer name of a compromised host.[^802]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has captured victim computer name, memory space, and CPU details.[^715]  |
| [[ObliqueRAT\|S0644]] | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) has the ability to check for blocklisted computer names on infected endpoints.[^81]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) has the ability to enumerate system information including the victim computer name.[^580] [^466] [^652]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) can identify the system name of a compromised host.[^734]  |
| [[XAgentOSX\|S0161]] | XAgentOSX | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getInstalledAPP function to run `ls -la /Applications` to gather what applications are installed.[^470]  |
| [[Green Lambert\|S0690]] | Green Lambert | [Green Lambert](https://attack.mitre.org/software/S0690) can use `uname` to identify the operating system name, version, and processor type.[^149] [^706]    |
| [[LightSpy\|S1185]] | LightSpy | [LightSpy](https://attack.mitre.org/software/S1185)'s second stage implant uses the `DeviceInformation` class to collect system information, including CPU usage, battery statistics, memory allocations, screen size, etc.[^87]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can gather system information such as computer names.[^796] 	 |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) can gather extended system information, such as information about the operating system and memory.[^251] [^283]  |
| [[MiniDuke\|S0051]] | MiniDuke | [MiniDuke](https://attack.mitre.org/software/S0051) can gather the hostname on a compromised machine.[^485]  |
| [[Anchor\|S0504]] | Anchor | [Anchor](https://attack.mitre.org/software/S0504) can determine the hostname and linux version on a compromised host.[^616]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) can obtain system information by querying the `Win32_ComputerSystem`, `Win32_BIOS`, `Win32_MotherboardDevice`, `Win32_PnPEntity`, and `Win32_DiskDrive` WMI objects.[^52]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has been known to collect basic system information.[^276] [^355]  [BeaverTail](https://attack.mitre.org/software/S1246) has also collected data to include hostname and current timestamp prior to uploading data to the API endpoint `/uploads` on the C2 server.[^82]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can gather the hostname and the OS version to ensure it doesn’t run on a Windows XP or Windows Server 2003 systems.[^160] [^313] [^330] [^450] [^724] [^511]  |
| [[CORESHELL\|S0137]] | CORESHELL | [CORESHELL](https://attack.mitre.org/software/S0137) collects hostname and OS version data from the victim and sends the information to its C2 server.[^811]  |
| [[RunningRAT\|S0253]] | RunningRAT | [RunningRAT](https://attack.mitre.org/software/S0253) gathers the OS version and processor information.[^491]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) can collect the OS version, system architecture, and computer name.[^302]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify the computer name, OS version, and hardware configuration on a compromised host.[^759]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has collected system information including OS version, processor information, RAM size, location, host name, IP, and screen size of the infected host.[^788]  |
| [[Reaver\|S0172]] | Reaver | [Reaver](https://attack.mitre.org/software/S0172) collects system information from the victim, including CPU speed, computer name, ANSI code page, OEM code page identifier for the OS, Microsoft Windows version, and memory information.[^168]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has used commands and API calls to gather system information.[^537] [^280] [^214]  |
| [[NOOPLDR\|S9025]] | NOOPLDR | [NOOPLDR](https://attack.mitre.org/software/S9025) can discover the device ID and hostname from the targeted machine to use for encryption keys.[^818]  |
| [[S-Type\|S0085]] | S-Type | The initial beacon packet for [S-Type](https://attack.mitre.org/software/S0085) contains the operating system version and file system of the victim.[^755]  |
| [[Lumma Stealer\|S1213]] | Lumma Stealer | [Lumma Stealer](https://attack.mitre.org/software/S1213) has gathered various system information from victim machines.[^89] [^830] [^703]  |
| [[DustySky\|S0062]] | DustySky | [DustySky](https://attack.mitre.org/software/S0062) extracts basic information about the operating system.[^166]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) can obtain the OS version information, computer name, processor architecture, machine role, and OS edition.[^397]  |
| [[Explosive\|S0569]] | Explosive | [Explosive](https://attack.mitre.org/software/S0569) has collected the computer name from the infected host.[^434]   |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) collects the OS version, hardware information, computer name, available system memory status, and system and user language settings.[^797]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) gathers the victim computer name using the Win32 API call `GetComputerName`.[^769]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can discover the hostname, computer name, and Windows version of a targeted machine.[^630] [^180]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can enumerate a targeted system's SerialNumber and Version.[^193] [^294]  |
| [[Akira\|S1129]] | Akira | [Akira](https://attack.mitre.org/software/S1129) uses the `GetSystemInfo` Windows function to determine the number of processors on a victim machine.[^671]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) will gather various system information such as domain, display adapter description, operating system type and version, processor type, and RAM amount.[^795] [^474]  |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) can retrieve the hostname via `gethostbyname`.[^837] <br> |
| [[NanHaiShu\|S0228]] | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) can gather the victim computer name and serial number.[^765]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can enumerate system hostname and domain.[^780]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) has the ability to collect information such as computer name, computer manufacturer, BIOS, operating system, and firmware, including through the use of `systeminfo.exe`.[^617]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can retrieve information such as computer name, OS version, processor speed, memory size, and CPU speed.[^304]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the IP address, machine name, and OS of the compromised host.[^534]  |
| [[Ferocious\|S0679]] | Ferocious | [Ferocious](https://attack.mitre.org/software/S0679) can use `GET.WORKSPACE` in Microsoft Excel to determine the OS version of the compromised host.[^538]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to gather information from the compromised asset, including the computer version, computer name, IIS version, and more.[^255]   |
| [[Netwalker\|S0457]] | Netwalker | [Netwalker](https://attack.mitre.org/software/S0457) can determine the system architecture it is running on to choose which version of the DLL to use.[^127]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) executes `systeminfo` after initial communication is made to the remote server.[^668]  |
| [[Latrodectus\|S1160]] | Latrodectus | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can gather operating system information.[^432] [^176] [^176] [^476]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can identify the OS version, CPU, and other details from a victim's machine.[^336]  |
| [[Pay2Key\|S0556]] | Pay2Key | [Pay2Key](https://attack.mitre.org/software/S0556) has the ability to gather the hostname of the victim machine.[^638]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) has collected system information, including the machine name and OS version.[^182]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can disover machine information including OS architecture, the ANSI code page (ACP) identifier, and hostname.[^13] [^377]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can enumerate the OS version and computer name on a targeted system.[^287]  |
| [[Bundlore\|S0482]] | Bundlore | [Bundlore](https://attack.mitre.org/software/S0482) will enumerate the macOS version to determine which follow-on behaviors to execute using `/usr/bin/sw_vers -productVersion`.[^158] [^308]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can obtain the computer name from the victim's system.[^478]  |
| [[KOMPROGO\|S0156]] | KOMPROGO | [KOMPROGO](https://attack.mitre.org/software/S0156) is capable of retrieving information about the infected system.[^113]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used the `systeminfo` command on a compromised host.[^380]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) gathers information from the infected system such as hostname.[^443]  |
| [[Sys10\|S0060]] | Sys10 | [Sys10](https://attack.mitre.org/software/S0060) collects the computer name, OS versioning information, and OS install date and sends the information to the C2.[^578]  |
| [[Royal\|S1073]] | Royal |  [Royal](https://attack.mitre.org/software/S1073) can use `GetNativeSystemInfo` to enumerate system processors.[^69] [^419]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has the ability to check the OS of the victim host.[^689] [^65]   [GlassWorm](https://attack.mitre.org/software/S9010) has checked whether the OS platform value includes `darwin` prior to execution of macOS specific scripts.[^689] [^65]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to gather basic system information and run the POSIX API `gethostbyname`.[^237]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has collected the hostname and operating system version from the compromised host.[^603] [^592] [^310]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can capture information regarding the victim's OS, security, and hardware configuration.[^737]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) can collect and send OS version and computer name as a part of its C2 beacon.[^179]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) collects basic system information from victim machines.[^420]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) can gather the OS version, architecture information, hostname, and RAM size information from the victim’s machine and has used `cmd /c systeminfo` command to get a snapshot of the current system state of the target machine.[^550] [^412] [^152]  |
| [[T9000\|S0098]] | T9000 | [T9000](https://attack.mitre.org/software/S0098) gathers and beacons the operating system build number and CPU Architecture (32-bit/64-bit) during installation.[^131]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) has gathered system architecture, processor, OS configuration, and installed hardware information.[^71]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) obtains the victim's operating system version and keyboard layout and sends the information to the C2 server.[^483] [^423]  |
| [[MoleNet\|S0553]] | MoleNet | [MoleNet](https://attack.mitre.org/software/S0553) can collect information about the about the system.[^394]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) has collected the computer name and OS version from victim machines.[^775]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) collects the computer name of the victim's system during the initial infection.[^220]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) gathers the hostname and OS version from the victim’s machine.[^691] [^293]  |
| [[Kerrdown\|S0585]] | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) has the ability to determine if the compromised host is running a 32 or 64 bit OS architecture.[^625]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) can collect information about the local system.[^263] [^694] [^467] [^269]  |
| [[Black Basta\|S1070]] | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) can collect system boot configuration and CPU information.[^386] [^153]  |
| [[StoneDrill\|S0380]] | StoneDrill | [StoneDrill](https://attack.mitre.org/software/S0380) has the capability to discover the system OS, Windows version, architecture and environment.[^137] 	 |
| [[OopsIE\|S0264]] | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) checks for information on the CPU fan, temperature, mouse, hard disk, and motherboard as part of its anti-VM checks.[^440]  |
| [[4H RAT\|S0065]] | 4H RAT | [4H RAT](https://attack.mitre.org/software/S0065) sends an OS version identifier in its beacons.[^116]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) gathers BIOS versions and manufacturers, the number of CPU cores, the total physical memory, and the computer name.[^582]  |
| [[LitePower\|S0680]] | LitePower | [LitePower](https://attack.mitre.org/software/S0680) has the ability to enumerate the OS architecture.[^538]  |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to enumerate system information.[^468]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to identify the OS version, OS bit information and computer name.[^514] [^225]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can obtain the computer name, OS version, and default language identifier.[^111]  |
| [[Derusbi\|S0021]] | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) gathers the name of the local host, version of GNU Compiler Collection (GCC), and the system information about the CPU, machine, and operating system.[^809]  |
| [[BlackByte Ransomware\|S1180]] | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) gathers victim system information to generate a unique victim identifier.[^387]  |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) can enumerate the host name and OS version on a target system.[^817]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) variants collect victim system information for exfiltration.[^297]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can collect the computer name and OS version from a compromised host.[^145]  |
| [[LiteDuke\|S0513]] | LiteDuke | [LiteDuke](https://attack.mitre.org/software/S0513) can enumerate the CPUID and BIOS version on a compromised system.[^485]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) has collected the host name and operating system product name from a compromised machine.[^358]   |
| [[WINDSHIELD\|S0155]] | WINDSHIELD | [WINDSHIELD](https://attack.mitre.org/software/S0155) can gather the victim computer name.[^113]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) can collect the GUID of a targeted machine.[^139] [^575]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can fingerprint architecture, computer name, and OS version on the compromised host. [Bazar](https://attack.mitre.org/software/S0534) can also check if the Russian language is installed on the infected machine and terminate if it is found.[^68] [^252]  |
| [[Kobalos\|S0641]] | Kobalos | [Kobalos](https://attack.mitre.org/software/S0641) can record the hostname and kernel version of the target machine.[^349]  |
| [[BadPatch\|S0337]] | BadPatch | [BadPatch](https://attack.mitre.org/software/S0337) collects the OS system, OS version, MAC address, and the computer name from the victim’s machine.[^457]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) gathers information about the OS architecture, OS name, and OS version/Service pack.[^224] [^61]  |
| [[XLoader\|S1207]] | XLoader | [XLoader](https://attack.mitre.org/software/S1207) can collect system information and supported language information from the victim machine.[^676]  |
| [[SOUNDBITE\|S0157]] | SOUNDBITE | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of gathering system information.[^113]  |
| [[BADCALL\|S0245]] | BADCALL | [BADCALL](https://attack.mitre.org/software/S0245) collects the computer name and host name on the compromised system.[^545]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) can obtain the victim hostname, Windows version, RAM amount, and screen resolution.[^188]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can enumerate the hostname and username of the compromised system.[^451] [^818] [^593]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) can determine the OS version and bitness on a targeted host.[^338] [^636] [^719] [^648]  |
| [[Final1stspy\|S0355]] | Final1stspy | [Final1stspy](https://attack.mitre.org/software/S0355) obtains victim Microsoft Windows version information and CPU architecture.[^776]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) utilizes WinAPI calls and registry queries to gather system information.[^21]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can enumerate system information including hostname and domain information.[^770] [^307]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) collects the OS version and computer name. [Zebrocy](https://attack.mitre.org/software/S0251) also runs the `systeminfo` command to gather system information. [^536] [^736] [^753] [^350] [^343] [^635] [^836]  |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) checks if the victim OS is 32 or 64-bit.[^2] [^190]  |
| [[SpeakUp\|S0374]] | SpeakUp | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `cat /proc/cpuinfo | grep -c “cpu family” 2>&1` command to gather system information. [^303]  |
| [[LunarMail\|S1142]] | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) can capture environmental variables on compromised hosts.[^569]  |
| [[Cadelspy\|S0454]] | Cadelspy | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to discover information about the compromised host.[^37]  |
| [[SampleCheck5000\|S1168]] | SampleCheck5000 | [SampleCheck5000](https://attack.mitre.org/software/S1168) can create unique victim identifiers by using the compromised system’s computer name.[^398]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) collected hostname and OS version.[^114] [^47]  |
| [[Wingbird\|S0176]] | Wingbird | [Wingbird](https://attack.mitre.org/software/S0176) checks the victim OS version after executing to determine where to drop files based on whether the victim is 32-bit or 64-bit.[^228]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to determine if the current user is an administrator, Windows product name, processor name, screen resolution, and physical RAM of the infected host.[^70]  |
| [[ServHelper\|S0382]] | ServHelper | [ServHelper](https://attack.mitre.org/software/S0382) will attempt to enumerate Windows version and system architecture.[^161]  |
| [[Unknown Logger\|S0130]] | Unknown Logger | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim computer name, physical memory, country, and date.[^435]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can identify the username, machine name, system language, keyboard layout, and OS version on a compromised host.[^428] [^541] [^400] [^233] [^233] [^461] [^18] [^84]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) can determine the Windows version and computer name on a compromised host.[^525] [^686]  |
| [[PinchDuke\|S0048]] | PinchDuke | [PinchDuke](https://attack.mitre.org/software/S0048) gathers system configuration information.[^495]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can enumerate the targeted machine's name and GUID.[^139] [^575]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) collects processor information, memory information, computer name, hardware UUID, serial number, and operating system version. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used the `ioreg` command to gather some of this information.[^528] [^515] [^308]  |
| [[OilBooster\|S1172]] | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) can identify the compromised system's hostname which is used to create a unique identifier.[^398]  |
| [[CaddyWiper\|S0693]] | CaddyWiper | [CaddyWiper](https://attack.mitre.org/software/S0693) can use `DsRoleGetPrimaryDomainInformation` to determine the role of the infected machine. [CaddyWiper](https://attack.mitre.org/software/S0693) can also halt execution if the compromised host is identified as a domain controller.[^454] [^731]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to query device information.[^502]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify hardware information, the computer name, and OS information on an infected host.[^369]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) gathers information on infected systems such as operating system, processor information, RAM, and display information.[^277] [^201]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) can collect the hostname, Microsoft Windows version, and processor architecture from a victim machine.[^340]  |
| [[BISCUIT\|S0017]] | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to collect the processor type, operation system, computer name, and whether the system is a laptop or PC.[^143]  |
| [[Solar\|S1166]] | Solar | [Solar](https://attack.mitre.org/software/S1166) can send basic information about the infected host to C2.[^48]  |
| [[Pisloader\|S0124]] | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) has a command to collect victim system information, including the system name and OS version.[^763]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) has gathered operating system information.[^792] 	 |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) collects endpoint information using the `systeminfo` command.[^491]  |
| [[AshTag\|S9031]] | AshTag | The [AshTag](https://attack.mitre.org/software/S9031) loader and AshenOrchestrator components can collect reconnaissance data from victim machines.[^125]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) has collected the operating system version from the infected system.[^503]  |
| [[NKAbuse\|S1107]] | NKAbuse | [NKAbuse](https://attack.mitre.org/software/S1107) conducts multiple system checks and includes these in subsequent "heartbeat" messages to the malware's command and control server.[^704]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) collects the CPU information, OS information, and system language.[^621]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can collect information about a compromised computer, including: Hardware UUID, Mac serial number, and macOS version.[^60]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the OS version and computer name.[^793] [^109]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can collect a system's architecture, operating system version, and hostname.[^187] [^172]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) has the ability to gather the victim's computer name.[^554]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) collects OS version information such as registered owner details, manufacturer details, processor type, available storage, installed patches, hostname, version info, system date, and other system information by using the commands `systeminfo`, `net config workstation`, `hostname`, `ver`, `set`, and `date /t`.[^768]  |
| [[BoomBox\|S0635]] | BoomBox | [BoomBox](https://attack.mitre.org/software/S0635) can enumerate the hostname, domain, and IP of a compromised host.[^552]  |
| [[DEADEYE\|S1052]] | DEADEYE | [DEADEYE](https://attack.mitre.org/software/S1052) can enumerate a victim computer's volume serial number and host name.[^681]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) has the ability to execute Windows commands returned from C2 to gather system information.[^173] [^804]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) can collect the machine name of a compromised system which is later used as part of a unique victim identifier.[^48]  |
| [[InnaputRAT\|S0259]] | InnaputRAT | [InnaputRAT](https://attack.mitre.org/software/S0259) gathers system information.[^268]  |
| [[Kessel\|S0487]] | Kessel | [Kessel](https://attack.mitre.org/software/S0487) has collected the system architecture, OS version, and MAC address information.[^408]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can collect the OS, and build version on a compromised host.[^688]  |
| [[YAHOYAH\|S0388]] | YAHOYAH | [YAHOYAH](https://attack.mitre.org/software/S0388) checks for the system’s Windows OS version and hostname.[^742]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the computer name and Windows product name/version.[^509]  |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) can perform a language check of the infected system and can query the CPU information (cupid).[^154] [^595]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to gather information about the compromised host.[^448]  |
| [[StealBit\|S1200]] | StealBit | [StealBit](https://attack.mitre.org/software/S1200) can enumerate the computer name and domain membership of the compromised system.[^530]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) collects the victim’s computer name, processor architecture, OS version, and system type.[^194] [^312]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can collect the local hostname, operating system details, CPU speed, and total physical memory.[^601]   |
| [[RIFLESPINE\|S1222]] | RIFLESPINE | [RIFLESPINE](https://attack.mitre.org/software/S1222) can collect system information after installation on infected systems.[^174]  |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) obtains the victim computer name and encrypts the information to send over its C2 channel.[^305]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) can report the file system type of a compromised host to C2.[^249]  |
| [[SPAWNCHIMERA\|S9024]] | SPAWNCHIMERA | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has obtained system information such as release, uptime, and current time.[^413]    |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `ver` command.[^421] 	 |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) can gather system information from the victim’s machine such as the OS version, and machine name.[^736] [^350]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can determine if the OS on a compromised host is newer than Windows XP.[^716]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) can collect local system information.[^564] [^664]  |
| [[Meteor\|S0688]] | Meteor | [Meteor](https://attack.mitre.org/software/S0688) has the ability to discover the hostname of a compromised host.[^739]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) enumerates the victim operating system and computer name during the initial infection.[^102]  |
| [[Maze\|S0449]] | Maze | [Maze](https://attack.mitre.org/software/S0449) has checked the language of the infected system using the "GetUSerDefaultUILanguage" function.[^587]  |
| [[TURNEDUP\|S0199]] | TURNEDUP | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of gathering system information.[^209]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) collects the victim hostname, window resolution, and Microsoft Windows version.[^146] [^484]  |
| [[Manjusaka\|S1156]] | Manjusaka | [Manjusaka](https://attack.mitre.org/software/S1156) performs basic system profiling actions to fingerprint and register the victim system with the C2 controller.[^453]  |
| [[IceApple\|S1022]] | IceApple | The [IceApple](https://attack.mitre.org/software/S1022) Server Variable Dumper module iterates over all server variables present for the current request and returns them to the adversary.[^692]  |
| [[Shai-Hulud\|S9008]] | Shai-Hulud | [Shai-Hulud](https://attack.mitre.org/software/S9008) has gathered victim system information.[^747] [^58]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can obtain system information such as OS version and disk space.[^816]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can collect the computer name from a compromised host.[^533]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) can collect the computer name of a targeted system.[^254]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has checked the OS version using `wmic.exe` and the `find` command.[^123]  |
| [[Mis-Type\|S0084]] | Mis-Type | The initial beacon packet for [Mis-Type](https://attack.mitre.org/software/S0084) contains the operating system version and file system of the victim.[^755]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can use WMI queries and shell commands such as systeminfo.exe to collect the operating system, BIOS version, and domain name of the targeted system.[^569]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) identifies the macOS version and uses `ioreg` to determine serial number.[^342]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can collect the computer name, OS version, and OS architecture information.[^640]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can detect whether a system is running FreeBSD, VMkernel (ESXi), Nutanix AHV, or a standard Linux distribution to enable platform-specific encryption behaviors.[^618]  |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) has collected the victim host information after infection.[^236]  |
| [[SoreFang\|S0516]] | SoreFang | [SoreFang](https://attack.mitre.org/software/S0516) can collect the hostname, operating system configuration, and product ID on victim machines by executing [Systeminfo](https://attack.mitre.org/software/S0096).[^344]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) can gather the computer name of an infected host.[^422] [^155]  |
| [[MirageFox\|S0280]] | MirageFox | [MirageFox](https://attack.mitre.org/software/S0280) can collect CPU and architecture information from the victim’s machine.[^364]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604) collects the victim machine’s Windows GUID.[^725]  |
| [[LazyWiper\|S9039]] | LazyWiper | [LazyWiper](https://attack.mitre.org/software/S9039) has used `[System.Net.Dns]::GetHostName()` and `$env:COMPUTERNAME` to enumerate the hostname of a system and determine if it is a domain controller.[^314]  |
| [[DownPaper\|S0186]] | DownPaper | [DownPaper](https://attack.mitre.org/software/S0186) collects the victim host name and serial number, and then sends the information to the C2 server.[^522]  |
| [[CozyCar\|S0046]] | CozyCar | A system info module in [CozyCar](https://attack.mitre.org/software/S0046) gathers information on the victim host’s configuration.[^557]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can enumerate the OS version and hostname of a targeted machine.[^130]  |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the system's computer name and also has the capability to collect information on the processor, memory, OS, and video card from the system.[^628] [^764] [^54]  |
| [[Pasam\|S0208]] | Pasam | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can retrieve information like hostname.[^782]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve OS name/architecture and computer/domain name information from compromised hosts.[^481] [^534]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can retrieve system information.[^403]  |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) has discovered system information including memory status, CPU frequency, and OS versions.[^445]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) collects the machine name and keyboard language from the system. [^584] [^250]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can collect system information including the OS version and domain on a compromised host.[^612] [^415] [^230] [^178]  |
| [[SYSCON\|S0464]] | SYSCON | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to use [Systeminfo](https://attack.mitre.org/software/S0096) to identify system information.[^799]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can determine the operating system and whether a targeted machine has a 32 or 64 bit architecture.[^802]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) collects information about the OS (version, build type, install date) as well as system up-time upon receiving a connection from a backdoor.[^492]  |
| [[Dridex\|S0384]] | Dridex | [Dridex](https://attack.mitre.org/software/S0384) has collected the computer name and OS architecture information from the system.[^452]  |
| [[OSX／Shlayer\|S0402]] | OSX／Shlayer | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has collected the IOPlatformUUID, session UID, and the OS version using the command `sw_vers -productVersion`.[^677] [^517]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) collects OS information and the computer name from the victim’s machine.[^610] [^767]  |
| [[SplatCloak\|S1234]] | SplatCloak | [SplatCloak](https://attack.mitre.org/software/S1234) has collected the Windows build number using the windows kernel API `RtlGetVersion` to determine if the response is 19000 or higher (Windows 10 version 2004 or later).[^147]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) collects the hostname of the victim machine.[^821]  |
| [[OSInfo\|S0165]] | OSInfo | [OSInfo](https://attack.mitre.org/software/S0165) discovers information about the infected machine.[^674]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) can collect the computer name from the machine.[^546] [^702]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) can collect the victim's computer name, hostname and adapter information to create a unique identifier.[^401] [^385]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) has monitored CPU usage.[^59] 	 |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can collect the machine information, system architecture, the OS version, computer name, Windows product name, the number of CPU cores, video card information, and the system language.[^211] [^371]  |
| [[BACKSPACE\|S0031]] | BACKSPACE | During its initial execution, [BACKSPACE](https://attack.mitre.org/software/S0031) extracts operating system information from the infected host.[^462]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the system’s hostname and OS version.[^411] [^4]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) can run [Systeminfo](https://attack.mitre.org/software/S0096) to gather information about the victim.[^438] [^19]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can collect the OS version, architecture, and machine name to create a unique token for the infected host.[^167]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can collect compromised host information, including OS version, PC name, RAM size, and CPU details.[^295]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has collected system name, OS version, adapter information, and memory usage from a victim machine.[^169]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) can collect operating system (OS) version information, processor information, and system name from the victim.[^535]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has the ability to collect the hostname, OS Username, Geolocation, and OS version of an infected host.[^78]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged `cmd.exe` to identify system info `cmd.exe /c systeminfo`.[^43]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [Systeminfo](https://attack.mitre.org/software/S0096) and similar commands to acquire detailed configuration information of a victim's machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also utilized the PowerShell cmdlet `Get-ADComputer` to collect DNS hostnames, last logon dates, and operating system information from Active Directory.[^772] [^144]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used csvde.exe, which is a built-in Windows command line tool, to export system information. Additionally, WsTaskLoad has gathered system information, such as operating system and hostname.[^351]   |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has run `hostname` and `systeminfo` on a victim.[^175] [^274] [^373] [^254] [^301] <br>	 |
| [[Lazarus Group\|G0032]] | Lazarus Group | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families collect information on the type and version of the victim OS, as well as the victim computer name and CPU information.[^651] [^512] [^324] [^402] [^282] [^745]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has used native OS commands to understand privilege levels and system details.[^779]  |
| [[Daggerfly\|G1034]] | Daggerfly | [Daggerfly](https://attack.mitre.org/groups/G1034) utilizes victim machine operating system information to create custom User Agent strings for subsequent command and control communication.[^122]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for system version, architecture, and hostname information.[^205] [^199]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) has used a reconnaissance module to gather information about the operating system and hardware on the infected host.[^208]  |
| [[admin@338\|G0018]] | admin@338 | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following commands after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to obtain information about the OS: `ver >> %temp%\download` `systeminfo >> %temp%\download`[^449]  |
| [[APT42\|G1044]] | APT42 | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect system information.[^248]   |
| [[Malteiro\|G1026]] | Malteiro | [Malteiro](https://attack.mitre.org/groups/G1026) collects the machine information, system architecture, the OS version, computer name, and Windows product name.[^354]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has enumerated OS type, OS version, and other information using a script or the "systeminfo" command.[^787] [^707]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also obtained system information such as OS type, OS version, and system type through querying various Windows Management Instrumentation (WMI) classes including `Win32_OperatingSystem`.[^216] [^159]  |
| [[Play\|G1040]] | Play | <br>[Play](https://attack.mitre.org/groups/G1040) has leveraged tools to enumerate system information.[^346]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) used a backdoor to enumerate information about the infected system's operating system.[^247] [^477] 	 |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover operating system configuration details using the `systeminfo` and `set` commands.[^654] [^200]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) collected the victim computer name, OS version, and architecture type and sent the information to its C2 server.[^500] [^305]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has collected the hostname of a compromised machine.[^130]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the hostname, OS version, service pack version, and the processor architecture from the victim’s machine.[^171] [^577]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) performs operating system information discovery using `systeminfo` and has used implants to identify the system language and computer name.[^148] [^362] [^215]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used a PowerShell command to check the victim system architecture to determine if it is an x64 machine. Other malware has obtained the OS version, UUID, and computer/host name to send to the C2 server.[^774] [^442] [^523]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s OS version and machine name.[^762] [^427] [^741] [^607] [^232]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has attempted to get detailed information about a compromised host, including the operating system, version, patches, hotfixes, and service packs.[^760]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has collected the OS version and computer name from victims. One of the group's backdoors can also query the Windows Registry to gather system information, and another macOS backdoor performs a fingerprint of the machine on its first connection to the C&C server. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to identify the name of the infected host.[^63] [^298] [^288] [^565]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has gathered system information using `systeminfo`.[^348]  |
| [[TA2541\|G1018]] | TA2541 | [TA2541](https://attack.mitre.org/groups/G1018) has collected system information prior to downloading malware on the targeted host.[^309]  |
| [[Storm-0501\|G1053]] | Storm-0501 | [Storm-0501](https://attack.mitre.org/groups/G1053) has leveraged native Windows tools and commands such as `systeminfo` and open-source tools including OSQuery and ossec-win32 to query details about the endpoint.[^598]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has detected a target system’s OS version.[^742] [^743]  |
| [[Mustard Tempest\|G1020]] | Mustard Tempest | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used implants to perform system reconnaissance on targeted systems.[^178]  |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) collected system architecture information. [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to gather the hostname and CPU information from the victim’s machine.[^85] [^133]  |
| [[Moses Staff\|G1009]] | Moses Staff | [Moses Staff](https://attack.mitre.org/groups/G1009) collected information about the infected host, including the machine names and OS architecture.[^487] <br> |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers system information via WMI, including the system directory, build number, serial number, version, manufacturer, model, and total physical memory.[^464]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has employed malicious macros and native Windows tools such as csvde.exe, nltest.exe and quser.exe for discovery.[^377] [^818] [^593]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) collects the computer name, the BIOS model, and execution path.[^458]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has gathered system information and disseminated it back to C2.[^699]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) uses multiple built-in commands such as `systeminfo` and `net config Workstation` to enumerate victim system basic configuration information.[^472]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has collected local host information by utilizing Windows commands `systeminfo`, `fsutil`, and `fsinfo`. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantex Altiris console and LanDesk account to retrieve host information.[^414] [^508]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used PowerShell Scripts to check the architecture of a compromised machine before the selection of a 32-bit or 64-bit version of a malicious .NET loader.[^447]  |
| [[Rocke\|G0106]] | Rocke | [Rocke](https://attack.mitre.org/groups/G0106) has used uname -m to collect the name and information about the infected system's kernel.[^826]  |
| [[Scattered Spider\|G1015]] | Scattered Spider | [Scattered Spider](https://attack.mitre.org/groups/G1015) has executed scripts to identify the underlying operating system to ensure it uses the correct installation package for malicious payloads.[^605]  |
| [[CURIUM\|G1012]] | CURIUM | [CURIUM](https://attack.mitre.org/groups/G1012) deploys information gathering tools focused on capturing IP configuration, running application, system information, and network connectivity information.[^812]  |
| [[Windigo\|G0124]] | Windigo | [Windigo](https://attack.mitre.org/groups/G0124) has used a script to detect which Linux distribution and version is currently installed on the system.[^408]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has collected hardware details for the victim's system, including CPU and memory information.[^436]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has collected information about the target system, such as system information and list of network connections.[^531] [^650]    |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has configured malicious webpages to identify the victim’s operating system by reviewing the details of the victims User-Agent of their browser.[^572]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to collect the computer name, OS version, installed hotfixes, as well as information regarding the memory and processor on a compromised host.[^444] [^25]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) collected the system GUID and computer name.[^473] [^156]  |
| [[Windshift\|G0112]] | Windshift | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the computer name of a compromised host.[^77]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) used various system commands and tools to pull system information during operations.[^151] [^238] [^378]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can gather the victim's computer name and drive serial numbers to send to a C2 server.[^583] [^368] [^475] [^15] [^643]   |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim systems.[^320]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can obtain information about the local system.[^674] [^57]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the processor architecture of a compromised host in order to register it with C2.[^705]  |
| [[Sowbug\|G0054]] | Sowbug | [Sowbug](https://attack.mitre.org/groups/G0054) obtained OS version and hardware configuration from a victim.[^588]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) script execution includes basic victim information gathering steps which are then transmitted to command and control servers.[^606]  |
| [[SideCopy\|G1008]] | SideCopy | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the OS version of a compromised host.[^381]  |
| [[APT18\|G0026]] | APT18 | [APT18](https://attack.mitre.org/groups/G0026) can collect system information from the victim’s machine.[^437]  |







## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^5]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^6]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^7]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^8]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^9]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


[^10]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^11]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^12]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^13]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^14]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^15]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^16]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^17]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^18]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)


[^19]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^20]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^21]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^22]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^23]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^24]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^25]: [Rewterz Sidewinder COVID-19 June 2020](https://www.rewterz.com/articles/analysis-on-sidewinder-apt-group-covid-19)


[^26]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^27]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^28]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^29]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)


[^30]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^31]: [Varonis](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)


[^32]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^33]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^34]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^35]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^36]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^37]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


[^38]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^39]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)


[^40]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^41]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^42]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^43]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^44]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^45]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^46]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)


[^47]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^48]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^49]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^50]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^51]: [TechNet Systeminfo](https://technet.microsoft.com/en-us/library/bb491007.aspx)


[^52]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^53]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^54]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)


[^55]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)


[^56]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


[^57]: [evolution of pirpi](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)


[^58]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)


[^59]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^60]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^61]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^62]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^63]: [ESET OceanLotus](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)


[^64]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^65]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)


[^66]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^67]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^68]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^69]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^70]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)


[^71]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)


[^72]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^73]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)


[^74]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^75]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^76]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^77]: [BlackBerry Bahamut](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)


[^78]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^79]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^80]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^81]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^82]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^83]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^84]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^85]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^86]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^87]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^88]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^89]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)


[^90]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)


[^91]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^92]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^93]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^94]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^95]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^96]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^97]: [Google Instances Resource](https://cloud.google.com/compute/docs/reference/rest/v1/instances)


[^98]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^99]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^100]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^101]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^102]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^103]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^104]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^105]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^106]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^107]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^108]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^109]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^110]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^111]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^112]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^113]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^114]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^115]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^116]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^117]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^118]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^119]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^120]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^121]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^122]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^123]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^124]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^125]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^126]: [AhnLab_SystemBC_Apr2022](https://asec.ahnlab.com/en/33600/)


[^127]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)


[^128]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^129]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^130]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^131]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)


[^132]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^133]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^134]: [Microsoft Virutal Machine API](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)


[^135]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


[^136]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^137]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)


[^138]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^139]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^140]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^141]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^142]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^143]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^144]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^145]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^146]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^147]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^148]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^149]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)


[^150]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^151]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^152]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^153]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)


[^154]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)


[^155]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^156]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^157]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^158]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)


[^159]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^160]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)


[^161]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^162]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^163]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^164]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^165]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^166]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)


[^167]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^168]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


[^169]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^170]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^171]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^172]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^173]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^174]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^175]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^176]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^177]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^178]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^179]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^180]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^181]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^182]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^183]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^184]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^185]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^186]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^187]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^188]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^189]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^190]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^191]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^192]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^193]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^194]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^195]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^196]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^197]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^198]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^199]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^200]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^201]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^202]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^203]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^204]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^205]: [ATT TeamTNT Chimaera September 2020](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)


[^206]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^207]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^208]: [Symantec Inception Framework March 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)


[^209]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^210]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^211]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^212]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^213]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^214]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^215]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^216]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^217]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^218]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^219]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^220]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^221]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^222]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^223]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^224]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^225]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^226]: [OSX.FairyTale](https://www.sentinelone.com/blog/trail-osx-fairytale-adware-playing-malware/)


[^227]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^228]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^229]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^230]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^231]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^232]: [Talos MuddyWater Jan 2022](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)


[^233]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^234]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^235]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^236]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^237]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^238]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


[^239]: [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)


[^240]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^241]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^242]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^243]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^244]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^245]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^246]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^247]: [ESET Telebots July 2017](https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/)


[^248]: [Mandiant APT42-charms](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)


[^249]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^250]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^251]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^252]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^253]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^254]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^255]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^256]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^257]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^258]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^259]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^260]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^261]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^262]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^263]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)


[^264]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^265]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^266]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^267]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^268]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^269]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)


[^270]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^271]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^272]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^273]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^274]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)


[^275]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^276]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^277]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^278]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^279]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^280]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^281]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^282]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^283]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)


[^284]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^285]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^286]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^287]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^288]: [ESET OceanLotus macOS April 2019](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)


[^289]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^290]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^291]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^292]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^293]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^294]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^295]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^296]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^297]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^298]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^299]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)


[^300]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^301]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^302]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^303]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


[^304]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^305]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^306]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^307]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)


[^308]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


[^309]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


[^310]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^311]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^312]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^313]: [Talos ROKRAT 2](https://blog.talosintelligence.com/2017/11/ROKRAT-Reloaded.html)


[^314]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)


[^315]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^316]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^317]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^318]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^319]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^320]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^321]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


[^322]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^323]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^324]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^325]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)


[^326]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^327]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^328]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^329]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^330]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^331]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^332]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^333]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^334]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^335]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^336]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^337]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^338]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)


[^339]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^340]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^341]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^342]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^343]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^344]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^345]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^346]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^347]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^348]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^349]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)


[^350]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)


[^351]: [BlackBerry_FIN7_April2024](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)


[^352]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^353]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^354]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)


[^355]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^356]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^357]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


[^358]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^359]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^360]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^361]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^362]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^363]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^364]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)


[^365]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^366]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^367]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^368]: [TrendMicro Gamaredon April 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)


[^369]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^370]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^371]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)


[^372]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^373]: [FireEye APT34 July 2019](https://www.fireeye.com/blog/threat-research/2019/07/hard-pass-declining-apt34-invite-to-join-their-professional-network.html)


[^374]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^375]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^376]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^377]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^378]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^379]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^380]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^381]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^382]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^383]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)


[^384]: [TechNet Dir](https://technet.microsoft.com/en-us/library/cc755121.aspx)


[^385]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^386]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)


[^387]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^388]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^389]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^390]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^391]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^392]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^393]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)


[^394]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^395]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^396]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^397]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^398]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^399]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^400]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^401]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^402]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^403]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^404]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^405]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^406]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^407]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^408]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^409]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


[^410]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^411]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^412]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^413]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^414]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^415]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^416]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^417]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^418]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^419]: [Trend Micro Royal Linux ESXi February 2023](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)


[^420]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^421]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^422]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


[^423]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)


[^424]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)


[^425]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^426]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^427]: [Talos MuddyWater May 2019](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)


[^428]: [Kaspersky Sodin July 2019](https://securelist.com/sodin-ransomware/91473/)


[^429]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^430]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^431]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^432]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^433]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^434]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^435]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^436]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^437]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^438]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^439]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^440]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)


[^441]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^442]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^443]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^444]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^445]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^446]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^447]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^448]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^449]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^450]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^451]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^452]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)


[^453]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


[^454]: [Cisco CaddyWiper March 2022](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)


[^455]: [Eclypsium Trickboot December 2020](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)


[^456]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^457]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)


[^458]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^459]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^460]: [SentinelOne AcidPour 2024](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)


[^461]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^462]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^463]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^464]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^465]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^466]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^467]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)


[^468]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^469]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^470]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^471]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^472]: [Rostovcev APT41 2021](https://www.group-ib.com/blog/apt41-world-tour-2021/)


[^473]: [PTSecurity Higaisa 2020](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)


[^474]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)


[^475]: [CERT-EE Gamaredon January 2021](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)


[^476]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^477]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^478]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^479]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^480]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)


[^481]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^482]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^483]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^484]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^485]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^486]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^487]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^488]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^489]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^490]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^491]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^492]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)


[^493]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^494]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^495]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^496]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^497]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^498]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^499]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^500]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^501]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^502]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^503]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^504]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)


[^505]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^506]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^507]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^508]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^509]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)


[^510]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^511]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^512]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^513]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^514]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^515]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^516]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^517]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)


[^518]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^519]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^520]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^521]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^522]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)


[^523]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^524]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^525]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^526]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^527]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^528]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^529]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^530]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


[^531]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^532]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^533]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^534]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^535]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^536]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^537]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^538]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^539]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^540]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)


[^541]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)


[^542]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)


[^543]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^544]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^545]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^546]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^547]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^548]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^549]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^550]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^551]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^552]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^553]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)


[^554]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^555]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^556]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^557]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^558]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^559]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^560]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^561]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)


[^562]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^563]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^564]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^565]: [FireEye APT32 April 2020](https://www.fireeye.com/blog/threat-research/2020/04/apt32-targeting-chinese-government-in-covid-19-related-espionage.html)


[^566]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^567]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^568]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^569]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^570]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^571]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^572]: [Sekoia ClickFake 2025](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)


[^573]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^574]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^575]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^576]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^577]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^578]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^579]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^580]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^581]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^582]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^583]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^584]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)


[^585]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^586]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^587]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)


[^588]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^589]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^590]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^591]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^592]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)


[^593]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^594]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^595]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)


[^596]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^597]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^598]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^599]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^600]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^601]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^602]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^603]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)


[^604]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^605]: [Mandiant VMware vSphere JUL 2025](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)


[^606]: [DomainTools WinterVivern 2021](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/)


[^607]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^608]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^609]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^610]: [Securelist Denis April 2017](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)


[^611]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^612]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^613]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^614]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^615]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^616]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)


[^617]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^618]: [Trend Micro Agenda Ransomware OCT 2025](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)


[^619]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^620]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^621]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^622]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^623]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^624]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^625]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


[^626]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


[^627]: [Microsoft_diskpart_Feb2023](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)


[^628]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)


[^629]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^630]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^631]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^632]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^633]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


[^634]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^635]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^636]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)


[^637]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^638]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


[^639]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^640]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^641]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)


[^642]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^643]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^644]: [Fysbis Palo Alto Analysis](https://researchcenter.paloaltonetworks.com/2016/02/a-look-into-fysbis-sofacys-linux-backdoor/)


[^645]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^646]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^647]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^648]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)


[^649]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^650]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^651]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^652]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^653]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^654]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^655]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^656]: [McAfee Netwire Mar 2015](https://securingtomorrow.mcafee.com/mcafee-labs/netwire-rat-behind-recent-targeted-attacks/)


[^657]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^658]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^659]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^660]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^661]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^662]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^663]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^664]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^665]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^666]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^667]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^668]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^669]: [HarmonProofpoint_SystemBC_Aug2019](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)


[^670]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^671]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^672]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^673]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^674]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


[^675]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^676]: [Acronis XLoader 2021](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)


[^677]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)


[^678]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^679]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^680]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^681]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^682]: [Github Covenant](https://github.com/cobbr/Covenant)


[^683]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^684]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^685]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)


[^686]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)


[^687]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^688]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^689]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^690]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^691]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)


[^692]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^693]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^694]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)


[^695]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^696]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^697]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^698]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^699]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^700]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^701]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^702]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)


[^703]: [TrendMicro LummaStealer 2025](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)


[^704]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)


[^705]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^706]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)


[^707]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^708]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^709]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^710]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^711]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^712]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^713]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^714]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^715]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^716]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^717]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^718]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^719]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^720]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^721]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^722]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^723]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)


[^724]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^725]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)


[^726]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^727]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)


[^728]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^729]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^730]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


[^731]: [Malwarebytes IssacWiper CaddyWiper March 2022 ](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)


[^732]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^733]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^734]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^735]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^736]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^737]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^738]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^739]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)


[^740]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^741]: [Reaqta MuddyWater November 2017](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)


[^742]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


[^743]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^744]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^745]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^746]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)


[^747]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)


[^748]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^749]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^750]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^751]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^752]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^753]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)


[^754]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^755]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^756]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^757]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^758]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^759]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)


[^760]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^761]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^762]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^763]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^764]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)


[^765]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^766]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^767]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^768]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^769]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^770]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^771]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^772]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^773]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^774]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^775]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^776]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^777]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^778]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^779]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^780]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^781]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^782]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


[^783]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^784]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^785]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^786]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^787]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^788]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^789]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^790]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^791]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^792]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^793]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^794]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)


[^795]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^796]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)


[^797]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)


[^798]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^799]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


[^800]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^801]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^802]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^803]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^804]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^805]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^806]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^807]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^808]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^809]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^810]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^811]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^812]: [Symantec Tortoiseshell 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain)


[^813]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^814]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^815]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^816]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^817]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^818]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^819]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^820]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^821]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^822]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^823]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^824]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^825]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^826]: [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)


[^827]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)


[^828]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^829]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^830]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)


[^831]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^832]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^833]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^834]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^835]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)


[^836]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^837]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^838]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^839]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^840]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^841]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


