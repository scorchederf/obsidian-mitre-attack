---
aliases: 
    - T1033
mitre-attack: https://attack.mitre.org/techniques/T1033
tactic: 
     - Discovery
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1033

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from [System Owner/User Discovery](https://attack.mitre.org/techniques/T1033) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Various utilities and commands may acquire this information, including `whoami`. In macOS and Linux, the currently logged in user can be identified with `w` and `who`. On macOS the `dscl . list /Users | grep -v '_'` command can also be used to enumerate user accounts. Environment variables, such as `%USERNAME%` and `$USER`, may also be used to access this information.<br><br>On network devices, [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as `show users` and `show ssh` can be used to display users currently logged into the device.[^201] [^283] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[BloodHound\|S0521]] | BloodHound | [BloodHound](https://attack.mitre.org/software/S0521) can collect information on user sessions.[^392]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather a list of logged on users.[^234]   |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can enumerate the username on targeted hosts.[^254]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) can check if the current user of a compromised system is an administrator. [^391]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can enumerate the username on targeted hosts.[^453]  |
| [[NBTscan\|S0590]] | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) can list active users on the system.[^564] [^165] 	 |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can identify logged in users across the domain and views user sessions.[^496] [^82]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^147]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can enumerate the username and account type.[^32]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) can identify the user and groups the user belongs to on a compromised host.[^317]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has commands to get the current user's name and SID.[^99]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can gather system owner information, including user and administrator privileges.[^263]  |
| [[Spark\|S0543]] | Spark | [Spark](https://attack.mitre.org/software/S0543) has run the whoami command and has a built-in command to identify the user logged in.[^250]   |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) gathers user names from infected hosts.[^534]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to identify the user name.[^273]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) has collected the user name from a compromised host using `GetUserNameA`.[^484]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) can collect the username from the victim’s machine.[^546]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) collects the victim’s username.[^177]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects the current username from the victim.[^166]  |
| [[IronWind\|S9029]] | IronWind | [IronWind](https://attack.mitre.org/software/S9029) can enumerate the username on victim's systems.[^111]  |
| [[Get2\|S0460]] | Get2 | [Get2](https://attack.mitre.org/software/S0460) has the ability to identify the current username of an infected host.[^343]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) may collect information about the currently logged in user by running `whoami` on a victim.[^214]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) can conduct basic network reconnaissance on the victim machine with `whoami`, to get user details.[^40]  |
| [[Linux Rabbit\|S0362]] | Linux Rabbit | [Linux Rabbit](https://attack.mitre.org/software/S0362) opens a socket on port 22 and if it receives a response it attempts to obtain the machine's hostname and Top-Level Domain. [^493]  |
| [[Exaramel for Linux\|S0401]] | Exaramel for Linux | [Exaramel for Linux](https://attack.mitre.org/software/S0401) can run `whoami` to identify the system owner.[^375]  |
| [[HAWKBALL\|S0391]] | HAWKBALL | [HAWKBALL](https://attack.mitre.org/software/S0391) can collect the user name of the system.[^432]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) can obtain information about the logged on user both locally and for Remote Desktop sessions.[^320]  |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) collects the current username and sends it to the C2 server.[^151]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can trigger exection of `whoami` on the target host to display the current user.[^97] [^318]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) collects the victim username along with other account information (account type, description, full name, SID and status).[^45]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has identified the user’s UUID and username through the "pay" module.[^193] [^52] [^241]   |
| [[HAPPYWORK\|S0214]] | HAPPYWORK | can collect the victim user name.[^83]  |
| [[WinMM\|S0059]] | WinMM | [WinMM](https://attack.mitre.org/software/S0059) uses NetUser-GetInfo to identify that it is running under an “Admin” account on the local system.[^393]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has obtained the username from an infected host.[^158]  |
| [[PyDCrypt\|S1032]] | PyDCrypt | [PyDCrypt](https://attack.mitre.org/software/S1032) has probed victim machines with `whoami` and has collected the username from the machine.[^323]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has obtained the username from an infected host. [^349]  |
| [[SslMM\|S0058]] | SslMM | [SslMM](https://attack.mitre.org/software/S0058) sends the logged-on username to its hard-coded C2.[^393]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the username on a compromised host.[^142]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has enumerated all users connected to network shares. |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can identify the user on a targeted system.[^121] [^169] [^53]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can retrieve usernames.[^451]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can obtain logged user information from a compromised machine and can execute the command `whoami.exe`.[^328]  |
| [[Action RAT\|S1028]] | Action RAT |  [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the username from an infected host.[^260]  |
| [[Prikormka\|S0113]] | Prikormka | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about the current user name.[^21]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has obtained the username from an infected host.[^19] [^310] [^189] [^158]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can collect the username on the victim machine to send to C2.[^490]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve a list of user accounts and usernames from an infected machine.[^146]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can collect the username from a compromised host.[^358]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) can collect the user name from a compromised host.[^309]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has collected the username from the victim host.[^497]  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer | [AuTo Stealer](https://attack.mitre.org/software/S1029) has the ability to collect the username from an infected host.[^260]  |
| [[Agent.btz\|S0092]] | Agent.btz | [Agent.btz](https://attack.mitre.org/software/S0092) obtains the victim username and saves it to a file.[^100]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) can execute `getinfo`  to identify the username on a compromised host.[^557] [^458]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) enumerates the current user during the initial infection.[^35] [^157]  |
| [[Rifdoor\|S0433]] | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the username on the compromised host.[^93]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can discover and send the username from a compromised host to C2.[^252]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) lists local users and session information.[^212]  |
| [[WINERACK\|S0219]] | WINERACK | [WINERACK](https://attack.mitre.org/software/S0219) can gather information on the victim username.[^83]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) can collect the victim username.[^420]  |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) has discovered the username of the user running the backdoor.[^276]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can collect the user name from a victim's machine.[^148]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) determines whether it is successfully running on a victim system by querying the running account information to determine if it is running in Session 0, indicating running with elevated privileges.[^479]  |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) can collect the username from a compromised host.[^567]  |
| [[RustyWater\|S9037]] | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) has gathered the victim machine’s username.[^42]     |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) can utilize `net use` commands to discover the user name on a compromised host.[^41]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) gathers the username from the victim’s machine.[^528]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on victim system users and usernames.[^81]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can retrieve the victim’s username.[^62]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to identify the current user on the infected host.[^563]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) gathers information on users.[^437]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) gathers the username from the victim’s machine.[^337]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) has included the victim's computer name and username in C2 messages sent to actor-owned infrastructure.[^494]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) has the ability to identify the username on a compromised host.[^253]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can obtain the name of the logged-in user on the victim.[^311]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) can obtain a list of users from an infected machine.[^359]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can detect the username of the infected host.[^170] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can retrieve the username from a targeted system.[^547]  |
| [[ObliqueRAT\|S0644]] | ObliqueRAT | [ObliqueRAT](https://attack.mitre.org/software/S0644) can check for blocklisted usernames on infected endpoints.[^51]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) can use `whoami` to obtain the username from a compromised host.[^395] [^308] [^443]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) has been used to run the `whoami` command on the system.[^101]  |
| [[XAgentOSX\|S0161]] | XAgentOSX | [XAgentOSX](https://attack.mitre.org/software/S0161) contains the getInfoOSX function to return the OS X version as well as the current user.[^313]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can collect the username from a compromised host.[^341]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) has collected the username from a victim machine.[^209]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify the users on a compromised host.[^520]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has the ability to gather the username from the victim’s machine.[^539]  |
| [[Reaver\|S0172]] | Reaver | [Reaver](https://attack.mitre.org/software/S0172) collects the victim's username.[^114]  |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) has run tests to determine the privilege level of the compromised user.[^517]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) can obtain information about the current user.[^269]  |
| [[Explosive\|S0569]] | Explosive | [Explosive](https://attack.mitre.org/software/S0569) has collected the username from the infected host.[^292]   |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) collects the user name from the victim’s machine.[^543]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can identify the username on a compromised host.[^429] [^122]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can retrieve the username from targeted machines.[^206]  |
| [[NanHaiShu\|S0228]] | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) collects the username from the victim.[^112]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) can collect the username from an infected host.[^421]  |
| [[NGLite\|S1106]] | NGLite | [NGLite](https://attack.mitre.org/software/S1106) will run the `whoami` command to gather system information and return this to the command and control server.[^548]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the username on the compromised host.[^360]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can obtain a list of user accounts from a victim's machine.[^175]  |
| [[Gazer\|S0168]] | Gazer | [Gazer](https://attack.mitre.org/software/S0168) obtains the current user's security identifier.[^149]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can discover the username of an infected host.[^120]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can collect the username from a compromised host.[^233]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) has collected the username and UID from the infected machine.[^124]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can identify the associated username on targeted machines.[^257]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can obtain the username from the victim's machine.[^316]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used `whoami` commands to identify system owners.[^259]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) gathers the victim username.[^160]  |
| [[Sys10\|S0060]] | Sys10 | [Sys10](https://attack.mitre.org/software/S0060) collects the account name of the logged-in user and sends it to the C2.[^393]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has collected the username from the victim's machine.[^213]   |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can gather information about the user on a compromised host.[^504]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) can collect the username from the victim’s machine.[^370]  |
| [[T9000\|S0098]] | T9000 | [T9000](https://attack.mitre.org/software/S0098) gathers and beacons the username of the logged in account during installation. It will also gather the username of running processes to determine if it is running as SYSTEM.[^87]  |
| [[DnsSystem\|S1021]] | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) can use the Windows user name to create a unique identification for infected users and systems.[^446]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect the username on a compromised host.[^531]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) collects the username from the victim’s machine.[^153]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) collects the username from the victim’s machine.[^471]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has obtained the username from the victim’s machine.[^474] [^306] [^186]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) collects the victim’s username and whether that user is an admin.[^398]  |
| [[LitePower\|S0680]] | LitePower | [LitePower](https://attack.mitre.org/software/S0680) can determine if the current user has admin privileges.[^362]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to identify the user on a compromised host.[^343]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) runs `whoami` on the victim’s machine.[^361]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can obtain the victim username and permissions.[^72]  |
| [[Derusbi\|S0021]] | Derusbi | A Linux version of [Derusbi](https://attack.mitre.org/software/S0021) checks if the victim user ID is anything other than zero (normally used for root), and the malware will not execute if it does not have root privileges. [Derusbi](https://attack.mitre.org/software/S0021) also gathers the username of the victim.[^552]  |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) can identify the username on a compromised host.[^559]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can collect the username from the victim's machine.[^98]  |
| [[WellMail\|S0515]] | WellMail | [WellMail](https://attack.mitre.org/software/S0515) can identify the current username on the victim system.[^293]  |
| [[LiteDuke\|S0513]] | LiteDuke | [LiteDuke](https://attack.mitre.org/software/S0513) can enumerate the account name on a targeted system.[^321]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) can collect the username from a compromised host.[^243]  |
| [[WINDSHIELD\|S0155]] | WINDSHIELD | [WINDSHIELD](https://attack.mitre.org/software/S0155) can gather the victim user name.[^74]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can identify the username of the infected user.[^172]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) runs the `whoami` and `query user` commands.[^37]  |
| [[XLoader\|S1207]] | XLoader | [XLoader](https://attack.mitre.org/software/S1207) can identify the username from a victim machine.[^456]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) obtains the victim username.[^129]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can collect the username associated with the compromised host.[^303] <br> |
| [[Cryptoistic\|S0498]] | Cryptoistic | [Cryptoistic](https://attack.mitre.org/software/S0498) can gather data on the user of a compromised host.[^568]  |
| [[MgBot\|S1146]] | MgBot | [MgBot](https://attack.mitre.org/software/S1146) includes modules for identifying local users and administrators on victim machines.[^399]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) gets the username from the system.[^515] [^575]  |
| [[SpeakUp\|S0374]] | SpeakUp | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `whoami` command. [^210]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) collected the username from a compromised host.[^75] [^28]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to collect the username on the infected host.[^93]  |
| [[ServHelper\|S0382]] | ServHelper | [ServHelper](https://attack.mitre.org/software/S0382) will attempt to enumerate the username of the victim.[^107]  |
| [[Unknown Logger\|S0130]] | Unknown Logger | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim usernames.[^294]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) can gather information regarding the user.[^352]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can identify users registered to a targeted machine.[^91]  |
| [[OilBooster\|S1172]] | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) can identify the compromised system's username which is then used as part of a unique identifier.[^270]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) gathers information on the infected system owner and user.[^194] [^11] [^137]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) can collect the username from a victim machine.[^236]  |
| [[BISCUIT\|S0017]] | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to gather the username from the system.[^554]  |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) collects the endpoint victim's username and uses it as a basis for downloading additional components from the C2 server.[^327]  |
| [[RGDoor\|S0258]] | RGDoor | [RGDoor](https://attack.mitre.org/software/S0258) executes the `whoami` on the victim’s machine.[^376]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) gathers the username from the system.[^424]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can collect the username from the compromised machine.[^36]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) has the ability to gather user information from the targeted system using `whoami/upn&whoami/fqdn&whoami/logonid&whoami/all`.[^224]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the username from the victim's machine.[^540] [^70]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can collect the username from a compromised host.[^117]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) collects registered owner details by using the commands `systeminfo` and `net config workstation`.[^526]  |
| [[BoomBox\|S0635]] | BoomBox | [BoomBox](https://attack.mitre.org/software/S0635) can enumerate the username on a compromised host.[^372]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can use `whoami` to enumerate the system user.[^118]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) can collect the user name from a compromised system which is used to create a unique victim identifier.[^29]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can identify the user id on a target machine.[^469]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the username on the infected host.[^339]  |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) has used tools to gather information about users.[^105]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) sent username, computer name, and the previously generated UUID in reply to a "who" command from C2.[^302]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) collects the username from the victim’s machine.[^133] [^215]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can collect the owner and organization information from the target workstation.[^409]   |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) obtains the victim username and encrypts the information to send over its C2 channel.[^211]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `whoami` command.[^285]  |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) can gather the username from the system.[^502]  |
| [[CreepySnail\|S1024]] | CreepySnail | [CreepySnail](https://attack.mitre.org/software/S1024) can execute `getUsername` on compromised systems.[^380]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) enumerates the current user during the initial infection.[^63]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can obtain the victim user name.[^558]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can collect the username from a compromised host.[^358]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) can collect the username on a targeted system.[^174]  |
| [[MechaFlounder\|S0459]] | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to identify the username and hostname on a compromised host.[^466]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) runs tests to determine the privilege level of the compromised user.[^517]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can collect user information from the targeted host.[^387]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can collect the username from the victim’s machine.[^435]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) can gather the username from an infected host.[^284] [^102]   |
| [[MirageFox\|S0280]] | MirageFox | [MirageFox](https://attack.mitre.org/software/S0280) can gather the username from the victim’s machine.[^248]  |
| [[DownPaper\|S0186]] | DownPaper | [DownPaper](https://attack.mitre.org/software/S0186) collects the victim username and sends it to the C2 server.[^348]  |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the username from the victim’s machine.[^278] [^427] [^34]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) has the ability to identify the username on the compromised host.[^360]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has the ability to enumerate the infected system's user name.[^525]  |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the username of the victim system.[^297]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can identify the user name on a compromised system.[^415] [^500]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) has the ability to distinguish between a standard user and an administrator on a compromised host.[^547]  |
| [[Komplex\|S0162]] | Komplex | The OsInfo function in [Komplex](https://attack.mitre.org/software/S0162) collects the current running username.[^433]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) enumerates and collects the username from the victim’s machine.[^416] [^525]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) can collect the username from the system.[^366] [^482]   |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can collect the username from the victim’s machine.[^144]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to collect the current logged on user’s username from a machine.[^280]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can collect the user name from the victim's machine.[^113]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has collected the username from a victim machine.[^115]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has collected the username from the victim host.[^48]  |
| [[Small Sieve\|S1035]] | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) can obtain the id of a logged in user.[^397]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used a malicious DLL to collect the username from compromised hosts.[^405]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute `quser` to discover the user session information.[^141]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used "whoami" to identify the local user and their privileges.[^527]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used the command `cmd.exe /C quser` to collect user session information.[^335]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) used the command `query user` on victim hosts.[^92]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has run `whoami` on a victim.[^119] [^191] [^174]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | Various [Lazarus Group](https://attack.mitre.org/groups/G0032) malware enumerates logged-on users.[^442] [^342] [^223] [^279] [^271] [^568] [^508]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) gathers information on recently logged-in users on victim devices.[^184]  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) collected information on user accounts via the `whoami` command.[^462]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has gathered the identity of the user by querying `System.Security.Principal` namespace using the `GetCurrent()` method.[^106]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has collected the username from a compromised host.[^315]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) collected the victim username and whether it was running as admin, then sent the information to its C2 server.[^333] [^211]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has run `whoami` on compromised machines to identify the current user.[^86]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has used implants capable of collecting the signed-in username.[^148]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used public tools and executed the PowerShell command `Get-EventLog security -instanceid 4624` to identify associated user and computer account names.[^300] [^354] [^314]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has obtained the victim username and sent it to the C2 server.[^530] [^296] [^350]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `whoami` to gather user information.[^514]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) used [Remexi](https://attack.mitre.org/software/S0375) to collect usernames from the system.[^22]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can collect the victim’s username.[^523] [^412]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has identified primary users, currently logged in users, sets of users that commonly use a system, or inactive users.[^521]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) collected the victim's username and executed the `whoami` command on the victim's machine. [APT32](https://attack.mitre.org/groups/G0050) executed shellcode to collect the username on the victim's machine. [^383] [^38] [^525]  |
| [[Storm-1811\|G1046]] | Storm-1811 | [Storm-1811](https://attack.mitre.org/groups/G1046) has used `whoami.exe` to determine if the active user on a compromised system is an administrator.[^104]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used the `quser` command to show currently logged on users.[^402]   |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) used `letmein` to scan for saved usernames on the target system.[^507]  |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to collect the victim’s username.[^89]  |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers the registered user and primary owner name via WMI.[^307]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Windows native tools to enumerate user information.[^560]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) identifies the victim username.[^304]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) has executed `whoami` commands, including using the WMIEXEC utility to execute this on remote machines.[^181] [^312]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used `whoami` and `query user` to obtain information about the victim user.[^287]  |
| [[FIN10\|G0051]] | FIN10 | [FIN10](https://attack.mitre.org/groups/G0051) has used Meterpreter to enumerate users on remote systems.[^436]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has executed the command `quser` to display the session details of a compromised machine.[^301]   |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used tools to identify the user of a compromised host.[^298]  |
| [[Windshift\|G0112]] | Windshift | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the username on a compromised host.[^47]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `whoami` to collect system user information.[^429]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can gather the victim's username to send to a C2 server.[^400]  |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) deployed various malware such as YouieLoader that can perform system user discovery actions.[^221]  |
| [[APT3\|G0022]] | APT3 | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command `"cmd.exe" /C whoami` to verify that it is running with the elevated privileges of “System.”[^96]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the username on a compromised host in order to register it with C2.[^483]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) PowerShell scripts execute `whoami` to identify the executing user.[^537]  |







## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^8]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^9]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^10]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^11]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)


[^12]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^13]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^14]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^15]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^16]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^17]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^18]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^19]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^20]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^21]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^22]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


[^23]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^24]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^25]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^26]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^27]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^28]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^29]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^30]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^31]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^32]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^33]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^34]: [Malwarebytes Agent Tesla April 2020](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)


[^35]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)


[^36]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^37]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^38]: [ESET OceanLotus](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)


[^39]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^40]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^41]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^42]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^43]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^44]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^45]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^46]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^47]: [BlackBerry Bahamut](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)


[^48]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^49]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^50]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^51]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)


[^52]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^53]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^54]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^55]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^56]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^57]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^58]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^59]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^60]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^61]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^62]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^63]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^64]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^65]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^66]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^67]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^68]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^69]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^70]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^71]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^72]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^73]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^74]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^75]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^76]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^77]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^78]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^79]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^80]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^81]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^82]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^83]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^84]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^85]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^86]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^87]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)


[^88]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^89]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^90]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^91]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^92]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^93]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^94]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^95]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^96]: [FireEye Operation Double Tap](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)


[^97]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)


[^98]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^99]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^100]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)


[^101]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^102]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^103]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^104]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^105]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)


[^106]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^107]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^108]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^109]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^110]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^111]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^112]: [fsecure NanHaiShu July 2016](https://www.f-secure.com/documents/996508/1030745/nanhaishu_whitepaper.pdf)


[^113]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^114]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


[^115]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^116]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^117]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^118]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^119]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^120]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^121]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^122]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^123]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^124]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^125]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^126]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^127]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^128]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^129]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^130]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^131]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^132]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^133]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^134]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^135]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^136]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^137]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^138]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^139]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^140]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^141]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^142]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^143]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^144]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^145]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^146]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^147]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^148]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^149]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^150]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^151]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^152]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^153]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^154]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^155]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^156]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^157]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^158]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^159]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^160]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^161]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^162]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^163]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^164]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^165]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)


[^166]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^167]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^168]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^169]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^170]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^171]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^172]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^173]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^174]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^175]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^176]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^177]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^178]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^179]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^180]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^181]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^182]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^183]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^184]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^185]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^186]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)


[^187]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^188]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^189]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^190]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^191]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)


[^192]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^193]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^194]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^195]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^196]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^197]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^198]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^199]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^200]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^201]: [show_ssh_users_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html)


[^202]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^203]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^204]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^205]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^206]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^207]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^208]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^209]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^210]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


[^211]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^212]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^213]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^214]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^215]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^216]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^217]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^218]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^219]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^220]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^221]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^222]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^223]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^224]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^225]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^226]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^227]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^228]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^229]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^230]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^231]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^232]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^233]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^234]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^235]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^236]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^237]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^238]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^239]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^240]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^241]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^242]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^243]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^244]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^245]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^246]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^247]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^248]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)


[^249]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^250]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^251]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^252]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^253]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^254]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^255]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^256]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^257]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^258]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^259]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^260]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^261]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^262]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^263]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^264]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^265]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^266]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^267]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^268]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^269]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^270]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^271]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^272]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^273]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^274]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^275]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^276]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^277]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^278]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)


[^279]: [Novetta Blockbuster RATs](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)


[^280]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^281]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^282]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^283]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^284]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


[^285]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^286]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^287]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^288]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^289]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^290]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^291]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^292]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^293]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^294]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^295]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^296]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^297]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^298]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^299]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^300]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^301]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^302]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^303]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^304]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^305]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^306]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)


[^307]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^308]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^309]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^310]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)


[^311]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^312]: [Rostovcev APT41 2021](https://www.group-ib.com/blog/apt41-world-tour-2021/)


[^313]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)


[^314]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^315]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^316]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^317]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^318]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)


[^319]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^320]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^321]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^322]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^323]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^324]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^325]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^326]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^327]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^328]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^329]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^330]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^331]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^332]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^333]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^334]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^335]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^336]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^337]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^338]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^339]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)


[^340]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^341]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^342]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^343]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^344]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^345]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^346]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^347]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^348]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)


[^349]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


[^350]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^351]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^352]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^353]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^354]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^355]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^356]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^357]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^358]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^359]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^360]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^361]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^362]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^363]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^364]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^365]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^366]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^367]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^368]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^369]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^370]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^371]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^372]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^373]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^374]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^375]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^376]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)


[^377]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^378]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^379]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^380]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^381]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^382]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^383]: [FireEye APT32 April 2020](https://www.fireeye.com/blog/threat-research/2020/04/apt32-targeting-chinese-government-in-covid-19-related-espionage.html)


[^384]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^385]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^386]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^387]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^388]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^389]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^390]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^391]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^392]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)


[^393]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^394]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^395]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^396]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^397]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^398]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^399]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^400]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^401]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^402]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^403]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^404]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^405]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^406]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^407]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^408]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^409]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^410]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^411]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^412]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^413]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^414]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^415]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^416]: [Securelist Denis April 2017](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)


[^417]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^418]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^419]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^420]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^421]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^422]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^423]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^424]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^425]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^426]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^427]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)


[^428]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^429]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^430]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^431]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^432]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


[^433]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)


[^434]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^435]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^436]: [FireEye FIN10 June 2017](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)


[^437]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^438]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^439]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^440]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^441]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^442]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^443]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^444]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^445]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^446]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


[^447]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^448]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^449]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^450]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^451]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^452]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^453]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^454]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^455]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^456]: [Acronis XLoader 2021](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)


[^457]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^458]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^459]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^460]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^461]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^462]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^463]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^464]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^465]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^466]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^467]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^468]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^469]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^470]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^471]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)


[^472]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^473]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^474]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)


[^475]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^476]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^477]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^478]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^479]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)


[^480]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^481]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^482]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)


[^483]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^484]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^485]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^486]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^487]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^488]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^489]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^490]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^491]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^492]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^493]: [Anomali Linux Rabbit 2018](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)


[^494]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^495]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^496]: [Github Koadic](https://github.com/offsecginger/koadic)


[^497]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^498]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^499]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^500]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^501]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^502]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^503]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^504]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^505]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^506]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^507]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


[^508]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^509]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^510]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^511]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^512]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^513]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^514]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^515]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)


[^516]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^517]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^518]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^519]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^520]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)


[^521]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^522]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^523]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^524]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^525]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^526]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^527]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^528]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^529]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^530]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^531]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^532]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^533]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^534]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^535]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^536]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^537]: [SentinelOne WinterVivern 2023](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)


[^538]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^539]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^540]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^541]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^542]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^543]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)


[^544]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^545]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^546]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^547]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^548]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)


[^549]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^550]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^551]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^552]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^553]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^554]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^555]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^556]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^557]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^558]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^559]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^560]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^561]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^562]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^563]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^564]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)


[^565]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^566]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^567]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^568]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^569]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^570]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^571]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^572]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^573]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^574]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^575]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^576]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^577]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^578]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


