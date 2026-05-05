---
aliases: 
    - T1041
mitre-attack: https://attack.mitre.org/techniques/T1041
tactic: 
     - Exfiltration
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## T1041

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) sent generated reports to the C2 via HTTP POST requests.[^324]  |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can exfiltrate files from the victim using the `download` command.[^89]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can transfer files from an infected host to the C2 server.[^226]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can send data gathered from a target through the command and control channel.[^177] [^248]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can upload files and information from a compromised host to its C2 servers.[^216]  |
| [[Imminent Monitor\|S0434]] | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) has uploaded a file containing debugger logs, network information and system information to the C2.[^283]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^141]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) can send information about the compromised host and upload data to a hardcoded C2 server.[^306] [^76]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has sent user and system information to a C2 server via HTTP POST requests.[^99] [^326]  |
| [[Pikabot\|S1145]] | Pikabot | During the initial [Pikabot](https://attack.mitre.org/software/S1145) command and control check-in, [Pikabot](https://attack.mitre.org/software/S1145) will transmit collected system information encrypted using RC4.[^204]  |
| [[Spark\|S0543]] | Spark | [Spark](https://attack.mitre.org/software/S0543) has exfiltrated data over the C2 channel.[^243]   |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can send collected data in JSON format to C2.[^269]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has uploaded files from the victim system to C2 servers.[^422] [^227] [^112] [^274] [^52] [^42] [^534]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) has sent victim data to its C2 servers.[^455]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) performs data exfiltration over the control server channel using a custom protocol.[^189]  |
| [[Torisma\|S0678]] | Torisma | [Torisma](https://attack.mitre.org/software/S0678) can send victim data to an actor-controlled C2 server.[^136]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) sends compromised victim information via HTTP.[^460]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) sends device and other collected data back to the C2 using the established C2 channels over TCP. [^339]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) has exfiltrated collected data to its C2 via POST requests.[^41]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) has uploaded files and data to its C2 servers.[^490]  |
| [[HAWKBALL\|S0391]] | HAWKBALL | [HAWKBALL](https://attack.mitre.org/software/S0391) has sent system information and files over the C2 channel.[^402]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used HTTP POSTs to exfil gathered information.[^482] [^252] [^194]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) has sent data and files from a compromised host to its C2 servers.[^490]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has used HTTP communications to the “/Uploads” URI for file exfiltration.[^118]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) exfiltrates data over its C2 channel.[^521]  |
| [[SharpDisco\|S1089]] | SharpDisco | [SharpDisco](https://attack.mitre.org/software/S1089) can load a plugin to exfiltrate stolen files to SMB shares also used in C2.[^532]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) can exfiltrate collected documents through C2 channels.[^285] [^469]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can exfiltrate files via the C2 channel.[^508]  |
| [[PowerExchange\|S1173]] | PowerExchange | [PowerExchange](https://attack.mitre.org/software/S1173) can exfiltrate files via its email C2 channel.[^206]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has exfiltrated data over its C2 channel.[^495] [^88]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can exfiltrate stolen information over its C2.[^51]  |
| [[Tomiris\|S0671]] | Tomiris |  [Tomiris](https://attack.mitre.org/software/S0671) can upload files matching a hardcoded set of extensions, such as .doc, .docx, .pdf, and .rar, to its C2 server.[^359]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can exfiltrate collected data over C2 channels.[^456]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can exfiltrate data over the C2 channel.[^354] [^312]   |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409)'s collected data is exfiltrated over the same channel used for C2.[^170]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) has the ability to exfiltrate stolen victim data through its C2 channel.[^298]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can exfiltrate files from an infected machine to its C2 server.[^140]   |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can send network system data and files to its C2 server.[^28]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has exfiltrated victim data using HTTP POST requests to its C2 servers.[^303]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^410] [^470]  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer | [AuTo Stealer](https://attack.mitre.org/software/S1029) can exfiltrate data over actor-controlled C2 servers via HTTP or TCP.[^255]  |
| [[ShrinkLocker\|S1178]] | ShrinkLocker | [ShrinkLocker](https://attack.mitre.org/software/S1178) will exfiltrate victim system information along with the encryption key via an HTTP POST.[^60] [^347]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) has uploaded collected data and files from a compromised host to its C2 server.[^526]  |
| [[ODAgent\|S1170]] | ODAgent | [ODAgent](https://attack.mitre.org/software/S1170) can use an attacker-controlled OneDrive account to receive C2 commands and to exfiltrate files.[^265]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has sent data collected from a compromised host to its C2 servers.[^150]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has used its C2 channel to exfiltrate data.[^423] 	 |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) can send information about the targeted system to C2 including captured passwords, OS build, hostname, and username.[^246]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) exfiltrates data to its C2 server over the same protocol as C2 communications.[^7]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) can exfiltrate data gathered from the infected system via the established Exchange Web Services API C2 channel.[^434]  |
| [[Okrum\|S0439]] | Okrum | Data exfiltration is done by [Okrum](https://attack.mitre.org/software/S0439) using the already opened channel with the C2 server.[^390]  |
| [[TRANSLATEXT\|S1201]] | TRANSLATEXT | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has exfiltrated collected credentials to the C2 server.[^457]   |
| [[Line Dancer\|S1186]] | Line Dancer | [Line Dancer](https://attack.mitre.org/software/S1186) exfiltrates collected data via command and control channels.[^466]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) can sends the collected financial data to the C2 server.[^397] [^235]  |
| [[Doki\|S0600]] | Doki | [Doki](https://attack.mitre.org/software/S0600) has used Ngrok to establish C2 and exfiltrate data.[^37]  |
| [[HTTPTroy\|S9007]] | HTTPTroy | [HTTPTroy](https://attack.mitre.org/software/S9007) has exfiltrated encrypted data over the C2 channel using the `up <FILENAME>` command.[^139]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can exfiltrate locally stored data via its C2.[^67]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has used a PowerShell document stealer module to pack and exfiltrate .txt, .pdf, .xls or .doc files smaller than 5MB that were modified during the past two days.[^529]  |
| [[NETEAGLE\|S0034]] | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) is capable of reading files over the C2 channel.[^301]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149)  can upload collected files to the command-and-control server.[^467]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can send data gathered from the infected machine via HTTP POST request to the C2.[^160] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can exfiltrate collected data via C2.[^516]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) has exfiltrated data to the C2 server.[^103]   |
| [[LightSpy\|S1185]] | LightSpy | To exfiltrate data, [LightSpy](https://attack.mitre.org/software/S1185) configures each module to send an obfuscated JSON blob to hardcoded URL endpoints or paths aligned to the module name.[^56]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) can exfiltrate files over the existing C2 channel.[^296] [^127]  |
| [[Line Runner\|S1188]] | Line Runner | [Line Runner](https://attack.mitre.org/software/S1188) utilizes HTTP to retrieve and exfiltrate information staged using [Line Dancer](https://attack.mitre.org/software/S1186).[^466]  |
| [[Pteranodon\|S0147]] | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) exfiltrates screenshot files to its C2 server.[^371]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has exfiltrated data collected from victim devices to C2 servers.[^46] [^236] [^259]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can send collected files back over same C2 channel.[^107]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) has the ability to send information staged on a compromised host externally to C2.[^493]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has exfiltrated stolen data and files to its C2 server.[^102] [^513]  |
| [[Bisonal\|S0268]] | Bisonal |  [Bisonal](https://attack.mitre.org/software/S0268) has added the exfiltrated data to the URL over the C2 channel.[^142]   |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) has uploaded data and files from a compromised host to its C2 servers.[^490]  |
| [[Lumma Stealer\|S1213]] | Lumma Stealer | [Lumma Stealer](https://attack.mitre.org/software/S1213) has exfiltrated collected data over existing HTTP and HTTPS C2 channels.[^43] [^537]  |
| [[DustySky\|S0062]] | DustySky | [DustySky](https://attack.mitre.org/software/S0062) has exfiltrated data to the C2 server.[^53]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) exfiltrates data over its email C2 channel.[^498]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) uses existing command and control channels to retrieve captured cryptocurrency wallet credentials.[^511]  |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) can upload files and information from a compromised host to its C2 server.[^542]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) can send collected data in JSON format to its C2 server.[^391]   |
| [[ThiefQuest\|S0595]] | ThiefQuest | [ThiefQuest](https://attack.mitre.org/software/S0595) exfiltrates targeted file extensions in the `/Users/` folder to the command and control server via unencrypted HTTP. Network packets contain a string with two pieces of information: a file path and the contents of the file in a base64 encoded string.[^190] [^365]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) can remotely exfiltrate sensitive information from a compromised AD FS server.[^225]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can upload files over the C2 channel.[^166]   |
| [[Latrodectus\|S1160]] | Latrodectus | <br>[Latrodectus](https://attack.mitre.org/software/S1160) can exfiltrate encrypted system information to the C2 server.[^287] [^304]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can exfiltrate collected credentials and browser cookies to the C2 server.[^149]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can exfiltrate gathered data to a hardcoded C2 URL via HTTP POST.[^195]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has uploaded files to the C2 server. Additionally, [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to upload the specified file in chunks with sleep time between each chunk.[^123]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can upload files over the C2 channel from the infected host.[^305]   |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has exfiltrated data to its C2 server.[^254]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) encrypts collected system data then exfiltrates via existing command and control channels.[^293]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) can send the data it collects to the C2 server.[^207]   |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) can upload files from a victim's machine over the C2 channel.[^214]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) exfiltrates data via HTTP over existing command and control channels.[^280]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has sent data and files to its C2 server.[^345] [^104] [^398]  |
| [[DnsSystem\|S1021]] | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) can exfiltrate collected data to its C2 server.[^417]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) has exfiltrated data over its C2 channel.[^500]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) can exfiltrate collected information from the host to the C2 server.[^144]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has sent victim data to its C2 server or RedLine panel server.[^444]  |
| [[OopsIE\|S0264]] | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) can upload files from the victim's machine to its C2 server.[^57]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438) has exfiltrated data over the C2 channel.[^474]  |
| [[LitePower\|S0680]] | LitePower | [LitePower](https://attack.mitre.org/software/S0680) can send collected data, including screenshots, over its C2 channel.[^337]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) uploads files and data from a compromised host over the existing C2 channel.[^275]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can use SMTP and DNS for file exfiltration and C2.[^532]  |
| [[Crutch\|S0538]] | Crutch | [Crutch](https://attack.mitre.org/software/S0538) can exfiltrate data over the primary C2 channel (Dropbox HTTP API).[^276]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has sent collected data from a compromised host to its C2 servers.[^150]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) exfiltrates collected email credentials via HTTP POST to command and control servers.[^512] [^98] [^87] [^202]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can send data it retrieves to the C2 server.[^97]  |
| [[Drovorub\|S0502]] | Drovorub | [Drovorub](https://attack.mitre.org/software/S0502) can exfiltrate files over C2 infrastructure.[^289]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) has the ability to upload files from the compromised host over a DNS or HTTP C2 channel.[^91]  |
| [[SUGARDUMP\|S1042]] | SUGARDUMP | [SUGARDUMP](https://attack.mitre.org/software/S1042) has sent stolen credentials and other data to its C2 server.[^9]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) has exfiltrated data to the designated C2 server using HTTP POST requests.[^404] [^541]   |
| [[LunarMail\|S1142]] | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) can use email image attachments with embedded data for receiving C2 commands and data exfiltration.[^364]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to download files from the infected host to the command and control (C2) server.[^93]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can exfiltrate host and malware information to C2 servers.[^54]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) has the ability to exfiltrate data over the C2 channel.[^331] [^299] [^439]  |
| [[OilBooster\|S1172]] | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) can use an actor-controlled OneDrive account for C2 communication and exfiltration.[^265]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to upload exfiltrated files to a C2 server.[^318]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to send collected files over its C2.[^245]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) uses existing HTTP-based command and control channels for exfiltration.[^185] [^15] [^132]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) exfiltrates specific files through its command and control framework.[^257]  |
| [[Solar\|S1166]] | Solar | [Solar](https://attack.mitre.org/software/S1166) can send staged files to C2 for exfiltration.[^32]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) has exfiltrated host environment information to an external C2 domain via port 9006.[^507] 	 |
| [[AshTag\|S9031]] | AshTag | [AshTag](https://attack.mitre.org/software/S9031) has exfiltrated reconnaissance data on targeted systems to C2 servers.[^82]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) has exfiltrated data via HTTP to already established C2 servers.[^319] [^231]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) exfiltrates data from a supplied path over its C2 channel.[^38]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can execute commands, including gathering user information, and send the results to C2.[^216]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) has exfiltrated data over its C2 channel.[^115]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) can upload files from a compromised host over its C2 channel.[^476]   |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can exfiltrate collected system information and documents to C2.[^116] [^518]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) can use its HTTP C2 channel for exfiltration.[^32]  |
| [[Kessel\|S0487]] | Kessel | [Kessel](https://attack.mitre.org/software/S0487) has exfiltrated information gathered from the infected system to the C2 server.[^272]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) has sent data related to a compromise host over its C2 channel.[^438]  |
| [[PHASEJAM\|S9014]] | PHASEJAM | [PHASEJAM](https://attack.mitre.org/software/S9014) has the ability to exfiltrate data from the victim appliance.[^247]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to initiate contact with command and control (C2) to exfiltrate stolen data.[^322]  |
| [[CallMe\|S0077]] | CallMe | [CallMe](https://attack.mitre.org/software/S0077) exfiltrates data to its C2 server over the same protocol as C2 communications.[^7]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has exfiltrated data over the C2 channel.[^100]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) can execute the command code `do_upload` to send files to C2.[^162]  |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) exfiltrates collected data over email via SMTP/S and POP3/S C2 channels.[^477]  |
| [[CreepySnail\|S1024]] | CreepySnail | [CreepySnail](https://attack.mitre.org/software/S1024) can connect to C2 for data exfiltration.[^355]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) exfiltrates collected information to its command and control infrastructure.[^360]  |
| [[Ebury\|S0377]] | Ebury | [Ebury](https://attack.mitre.org/software/S0377) exfiltrates a list of outbound and inbound SSH sessions using OpenSSH's `known_host` files and `wtmp` records. [Ebury](https://attack.mitre.org/software/S0377) can exfiltrate SSH credentials through custom DNS queries or use the command `Xcat` to send the process's ssh session's credentials to the C2 server.[^356] [^350]   |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) has used C2 infrastructure to receive stolen information from the infected machine including screenshots and other system information.[^131] [^171] 	 |
| [[Manjusaka\|S1156]] | Manjusaka | [Manjusaka](https://attack.mitre.org/software/S1156) data exfiltration takes place over HTTP channels.[^297]  |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022)'s Multi File Exfiltrator module can exfiltrate multiple files from a compromised host as an HTTP response over C2.[^442]   |
| [[Shai-Hulud\|S9008]] | Shai-Hulud | [Shai-Hulud](https://attack.mitre.org/software/S9008) has used POST to exfiltrate secrets from the victim environment to an attacker-controlled URL.[^483] [^58] [^179]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can upload collected files and data to its C2 server.[^336]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) has exfiltrated data over its C2 channel.[^167]  |
| [[MechaFlounder\|S0459]] | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to send the compromised user's account name and hostname within a URL to C2.[^435]  |
| [[Psylo\|S0078]] | Psylo | [Psylo](https://attack.mitre.org/software/S0078) exfiltrates data to its C2 server over the same protocol as C2 communications.[^7]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) has transmitted collected files and data to its C2 server.[^490]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) retrieves files that match the pattern defined in the INAME_QUERY variable within the user's home directory, such as `*test.txt`, and are below a specific size limit. It then archives the files and exfiltrates the data over its C2 channel.[^229] [^34]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) has uploaded stolen files and data from a victim's machine over its C2 channel.[^406]  |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) has exfiltrated collected host information to a C2 server.[^155]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) can exfiltrate collected data to its C2 servers.[^105]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604) sends information about hardware profiles and previously-received commands back to the C2 server in a POST-request.[^387]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can send data from the victim host through a DNS C2 channel.[^85]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has the ability to exfiltrate data over the Microsoft Outlook C2 channel.[^497]  |
| [[Remexi\|S0375]] | Remexi | [Remexi](https://attack.mitre.org/software/S0375) performs exfiltration over [BITSAdmin](https://attack.mitre.org/software/S0190), which is also used for the C2 channel.[^159]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) exfiltrates collected information from its r1.log file to the external C2 server. [^164]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can send stolen information to C2 nodes including passwords, accounts, and emails.[^385]  |
| [[BACKSPACE\|S0031]] | BACKSPACE | Adversaries can direct [BACKSPACE](https://attack.mitre.org/software/S0031) to upload files to the C2 Server.[^301]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) exfiltrates data over the same channel used for C2.[^291]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can send data and files from a compromised host to its C2 server.[^111]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can send collected victim data to its C2 server.[^200]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has sent system information to a C2 server via HTTP and HTTPS POST requests.[^113]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has exfiltrated victim data using HTTPS POST requests to its C2 servers.[^46]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that exfiltrates stolen data to its C2 server.[^520]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated domain credentials and network enumeration information over command and control (C2) channels.[^447] [^96]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has exfiltrated collected victim data to C2 infrastructure.[^82]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has exfiltrated data and files over a C2 channel through its various tools and malware.[^413] [^215] [^267]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has exfiltrated data over its C2 channel.[^506] [^454]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has sent system information to its C2 server using HTTP.[^40] 	 |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) transferred compressed and encrypted RAR files containing exfiltration through the established backdoor command and control channel during operations.[^101]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has exfiltrated stolen victim data through C2 communications.[^163]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used C2 infrastructure to receive exfiltrated data.[^481]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has exfiltrated data using the already opened channel with its C&C server.[^203]  |
| [[Leviathan\|G0065]] | Leviathan | [Leviathan](https://attack.mitre.org/groups/G0065) has exfiltrated data over its C2 channel.[^414]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has exfiltrated stolen data and files to its C2 server.[^23] [^14] [^513]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) C2 beacons for data exfiltration.[^373]   |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | After data is collected by [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware, it is exfiltrated over the existing C2 channel.[^302]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) malware has exfiltrated collected data via Telegram bot C2 channels using encrypted communications.[^452]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells and [HTRAN](https://attack.mitre.org/software/S0040) for C2 and to exfiltrate data.[^282]  |
| [[Scattered Spider\|G1015]] | Scattered Spider | [Scattered Spider](https://attack.mitre.org/groups/G1015) has exfiltrated data from compromised VMware vCenter servers through an established C2 channel using the Teleport remote access tool.[^382]  |
| [[CURIUM\|G1012]] | CURIUM | [CURIUM](https://attack.mitre.org/groups/G1012) has used IMAP and SMTPS for exfiltration via tools such as [IMAPLoader](https://attack.mitre.org/software/S1152).[^26]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has exfiltrated data from a compromised host to actor-controlled C2 servers.[^403] [^184] [^378] [^410] [^46] [^470] [^50] [^92] [^236] [^259]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) exfiltrated data over its C2 channel.[^392]  |
| [[Confucius\|G0142]] | Confucius | [Confucius](https://attack.mitre.org/groups/G0142) has exfiltrated stolen files to its C2 server.[^472]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) transmitted collected victim host information via HTTP POST to command and control infrastructure.[^251]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | A [Gamaredon Group](https://attack.mitre.org/groups/G0047) file stealer can transfer collected files to a hardcoded C2 server.[^371] [^407] [^11]  |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) exfiltrated staged data using tools such as Putty and WinSCP, communicating with command and control servers.[^169]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that exfiltrates data over the C2 channel.[^295]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exfiltrated files via the Dropbox API C2.[^453]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP.[^266]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Network Intrusion Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [^156]  |
| [[Data Loss Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |





## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


[^10]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^11]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^12]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^13]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^14]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^15]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)


[^16]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^17]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^18]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^19]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^20]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^21]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^22]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^23]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^24]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^25]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^26]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)


[^27]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^28]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^29]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^30]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^31]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^32]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^33]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^34]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)


[^35]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^36]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^37]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


[^38]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^39]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^40]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


[^41]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^42]: [Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)


[^43]: [Qualys LummaStealer 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)


[^44]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^45]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^46]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^47]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^48]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^49]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^50]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^51]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^52]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)


[^53]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^54]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^55]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^56]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^57]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^58]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)


[^59]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^60]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)


[^61]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^62]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^63]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^64]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^65]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^66]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^67]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^68]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^69]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^70]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^71]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^72]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^73]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^74]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^75]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^76]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)


[^77]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^78]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^79]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^80]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^81]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^82]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^83]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^84]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^85]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^86]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^87]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)


[^88]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)


[^89]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)


[^90]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^91]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^92]: [SecurityScorecard Contagious Interview October 2024](https://securityscorecard.com/blog/inside-a-north-korean-phishing-operation-targeting-devops-employees/)


[^93]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^94]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^95]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^96]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^97]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^98]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)


[^99]: [NHS UK BLINDINGCAN Aug 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)


[^100]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)


[^101]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^102]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^103]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^104]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^105]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^106]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^107]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)


[^108]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^109]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^110]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^111]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^112]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)


[^113]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^114]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^115]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^116]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^117]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^118]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^119]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^120]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^121]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^122]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^123]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^124]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^125]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^126]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^127]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)


[^128]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^129]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^130]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^131]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^132]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^133]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^134]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^135]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^136]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)


[^137]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^138]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^139]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^140]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^141]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^142]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^143]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^144]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^145]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^146]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^147]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^148]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^149]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^150]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^151]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^152]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^153]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^154]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^155]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^156]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^157]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^158]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^159]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^160]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^161]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^162]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^163]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^164]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^165]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^166]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^167]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^168]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^169]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^170]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^171]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^172]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^173]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^174]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^175]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^176]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^177]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^178]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^179]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)


[^180]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^181]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^182]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^183]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^184]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^185]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^186]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^187]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^188]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^189]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^190]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)


[^191]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^192]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^193]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^194]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)


[^195]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^196]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^197]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^198]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^199]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^200]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^201]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^202]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^203]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^204]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)


[^205]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^206]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^207]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^208]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^209]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^210]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^211]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^212]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^213]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^214]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^215]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^216]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^217]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^218]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^219]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^220]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^221]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^222]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^223]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^224]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^225]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^226]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^227]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^228]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^229]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^230]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^231]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)


[^232]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^233]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^234]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^235]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)


[^236]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^237]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^238]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^239]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^240]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^241]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^242]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^243]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^244]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^245]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^246]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^247]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^248]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^249]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^250]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^251]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^252]: [FireEye Ursnif Nov 2017](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)


[^253]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^254]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^255]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^256]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^257]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^258]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^259]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^260]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^261]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^262]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^263]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^264]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^265]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^266]: [CERT-UA WinterVivern 2023](https://cert.gov.ua/article/3761104)


[^267]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^268]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^269]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^270]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^271]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^272]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^273]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^274]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^275]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^276]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)


[^277]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^278]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^279]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^280]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^281]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^282]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^283]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^284]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^285]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^286]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^287]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^288]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^289]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)


[^290]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^291]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^292]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^293]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^294]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^295]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^296]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^297]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


[^298]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^299]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^300]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^301]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^302]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^303]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^304]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^305]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^306]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^307]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^308]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^309]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^310]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^311]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^312]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^313]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^314]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^315]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^316]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^317]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^318]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^319]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^320]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^321]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^322]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)


[^323]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^324]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^325]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^326]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^327]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^328]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^329]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^330]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^331]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^332]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^333]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^334]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^335]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^336]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^337]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^338]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^339]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)


[^340]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^341]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^342]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^343]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^344]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^345]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^346]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^347]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)


[^348]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^349]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^350]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)


[^351]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^352]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^353]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^354]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)


[^355]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^356]: [ESET Windigo Mar 2014](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)


[^357]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^358]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^359]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)


[^360]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^361]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^362]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^363]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^364]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^365]: [reed thiefquest ransomware analysis](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)


[^366]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^367]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^368]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^369]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^370]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^371]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^372]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^373]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^374]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^375]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^376]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^377]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^378]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)


[^379]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^380]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^381]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^382]: [Mandiant VMware vSphere JUL 2025](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)


[^383]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^384]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^385]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^386]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^387]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^388]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^389]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^390]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^391]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^392]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^393]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^394]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^395]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^396]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^397]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^398]: [Malwarebytes KONNI Evolves Jan 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/)


[^399]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^400]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^401]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^402]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


[^403]: [Sentinel One Contagious Interview ClickFix September 2025](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)


[^404]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^405]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^406]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^407]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^408]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^409]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^410]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


[^411]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^412]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^413]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^414]: [CISA AA21-200A APT40 July 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)


[^415]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^416]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^417]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


[^418]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^419]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^420]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^421]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^422]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)


[^423]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^424]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^425]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^426]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^427]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^428]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^429]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^430]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^431]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^432]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^433]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^434]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^435]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^436]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^437]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^438]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^439]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)


[^440]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^441]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^442]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^443]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^444]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)


[^445]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^446]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^447]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^448]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^449]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^450]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^451]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^452]: [Domain Tools Handala Hack Karma Homeland Justice MOIS April 2026](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)


[^453]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^454]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^455]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^456]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^457]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)


[^458]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^459]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^460]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^461]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^462]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^463]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^464]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^465]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^466]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)


[^467]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^468]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^469]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^470]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^471]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^472]: [TrendMicro Confucius APT Aug 2021](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)


[^473]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^474]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^475]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^476]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^477]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^478]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^479]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^480]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^481]: [Reaqta MuddyWater November 2017](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)


[^482]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)


[^483]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)


[^484]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^485]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^486]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^487]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^488]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^489]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^490]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^491]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^492]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^493]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)


[^494]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^495]: [Trend Micro Emotet Jan 2019](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)


[^496]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^497]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^498]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^499]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^500]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^501]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^502]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^503]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^504]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^505]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^506]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^507]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^508]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^509]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^510]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^511]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^512]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)


[^513]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^514]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^515]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^516]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^517]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^518]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^519]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^520]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^521]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^522]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^523]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^524]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^525]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^526]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^527]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^528]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^529]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^530]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^531]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^532]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^533]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^534]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)


[^535]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^536]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^537]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)


[^538]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^539]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^540]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^541]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^542]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^543]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^544]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^545]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


