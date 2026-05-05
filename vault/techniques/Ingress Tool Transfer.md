---
aliases: 
    - T1105
mitre-attack: https://attack.mitre.org/techniques/T1105
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1105

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [ftp](https://attack.mitre.org/software/S0095). Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570)). <br><br>On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [certutil](https://attack.mitre.org/software/S0160), and [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands such as `IEX(New-Object Net.WebClient).downloadString()` and `Invoke-WebRequest`. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.[^107]   A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).[^662] <br><br>Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [User Execution](https://attack.mitre.org/techniques/T1204) (typically after interacting with [Phishing](https://attack.mitre.org/techniques/T1566) lures).[^86] <br><br>Files can also be transferred using various [Web Service](https://attack.mitre.org/techniques/T1102)s as well as native or otherwise present tools on the victim system.[^252]  In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.[^148] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[RemoteUtilities\|S0592]] | RemoteUtilities | [RemoteUtilities](https://attack.mitre.org/software/S0592) can upload and download files to and from a target machine.[^684]  |
| [[certutil\|S0160]] | certutil | [certutil](https://attack.mitre.org/software/S0160) can be used to download files from a given URL.[^125] [^511]  |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) had the ability to download additional payloads.[^570]  |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can download additional content and files from the [Sliver](https://attack.mitre.org/software/S0633) server to the client residing on the victim machine using the `upload` command.[^221] [^630]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can load additional files and tools, including [Mimikatz](https://attack.mitre.org/software/S0002).[^393]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can upload and download to and from a victim machine.[^305]  |
| [[CSPY Downloader\|S0527]] | CSPY Downloader | [CSPY Downloader](https://attack.mitre.org/software/S0527) can download additional tools to a compromised host.[^254]  |
| [[CARROTBALL\|S0465]] | CARROTBALL | [CARROTBALL](https://attack.mitre.org/software/S0465) has the ability to download and install a remote payload.[^892]  |
| [[BITSAdmin\|S0190]] | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files.[^926]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to download files including over SFTP.[^542] [^367]  |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can download files to compromised hosts.[^686] [^92]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can upload and download files to and from the victim’s machine.[^797] [^746]  |
| [[MCMD\|S0500]] | MCMD | [MCMD](https://attack.mitre.org/software/S0500) can upload additional files to a compromised host.[^657]  |
| [[Donut\|S0695]] | Donut | [Donut](https://attack.mitre.org/software/S0695) can download and execute previously staged shellcode payloads.[^352]  |
| [[cmd\|S0106]] | cmd | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected external system.[^455]  |
| [[esentutl\|S0404]] | esentutl | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files from a given URL.[^432]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can download additional files and tools.[^812] [^140]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) can upload and download to/from a victim machine.[^246]  |
| [[ftp\|S0095]] | ftp | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files from an external system into a compromised environment.[^784] [^881]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can download files to the victim’s machine and execute them.[^876] [^224]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) downloads several additional files and saves them to the victim's machine.[^389] [^132]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to download a file.[^171]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has downloaded files to a victim machine.[^576]  |
| [[Wiarp\|S0206]] | Wiarp | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can download files.[^624]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) has the ability to drop additional files to an infected machine.[^447]  |
| [[QuietSieve\|S0686]] | QuietSieve | [QuietSieve](https://attack.mitre.org/software/S0686) can download and execute payloads on a target host.[^70]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can download and execute additional payloads including through the use of a `Dex` command.[^463] [^11] [^672]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has the ability to download files from the Adversaries C2 server to the compromised system.[^394] [^473] [^99] [^928]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) can download and execute files to further infect a host machine with additional malware.[^790]  |
| [[NICECURL\|S1192]] | NICECURL | [NICECURL](https://attack.mitre.org/software/S1192) has the ability to download additional content onto an infected machine, e.g. by using `curl`.[^567]   |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can download files onto the victim.[^857]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) has downloaded a remote module for execution.[^894]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can download additional modules from C2.[^501]  |
| [[DOGCALL\|S0213]] | DOGCALL | [DOGCALL](https://attack.mitre.org/software/S0213) can download and execute additional payloads.[^867]  |
| [[Downdelph\|S0134]] | Downdelph | After downloading its main config file, [Downdelph](https://attack.mitre.org/software/S0134) downloads multiple payloads from C2 servers.[^74]  |
| [[SEASHARPEE\|S0185]] | SEASHARPEE | [SEASHARPEE](https://attack.mitre.org/software/S0185) can download remote files onto victims.[^609]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) can download or upload files from its C2 server.[^353]  |
| [[TDTESS\|S0164]] | TDTESS | [TDTESS](https://attack.mitre.org/software/S0164) has a command to download and execute an additional file.[^647]  |
| [[SharpStage\|S0546]] | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546) has the ability to download and execute additional payloads via a DropBox API.[^452] [^661]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to upload additional malicious files to a compromised machine.[^73]  |
| [[Smoke Loader\|S0226]] | Smoke Loader | [Smoke Loader](https://attack.mitre.org/software/S0226) downloads a new version of itself once it has installed. It also downloads additional plugins.[^898]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) is capable of downloading files from the C2.[^849]  |
| [[reGeorg\|S1187]] | reGeorg | [reGeorg](https://attack.mitre.org/software/S1187) has the ability to download files to targeted systems.[^322]  |
| [[Emissary\|S0082]] | Emissary | [Emissary](https://attack.mitre.org/software/S0082) has the capability to download files from the C2 server.[^66]  |
| [[Exaramel for Linux\|S0401]] | Exaramel for Linux | [Exaramel for Linux](https://attack.mitre.org/software/S0401) has a command to download a file from  and to a remote C2 server.[^56] [^626]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) can upload files to the victim’s machine and can download additional payloads.[^402]  |
| [[TAMECAT\|S1193]] | TAMECAT | [TAMECAT](https://attack.mitre.org/software/S1193) has used `wget` and `curl` to download additional content.[^567]   |
| [[PS1\|S0613]] | PS1 | [CostaBricks](https://attack.mitre.org/software/S0614) can download additional payloads onto a compromised host.[^911]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has dropped payload and configuration files to disk. [Ursnif](https://attack.mitre.org/software/S0386) has also been used to download and execute additional payloads.[^792] [^362]  |
| [[CASTLETAP\|S1224]] | CASTLETAP | [CASTLETAP](https://attack.mitre.org/software/S1224) can transfer files to compromised network devices.[^191]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can download additional tools to enable lateral movement.[^649]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) has the ability to download files.[^849]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) is capable of downloading a file from a specified URL.[^537]  |
| [[POWERSOURCE\|S0145]] | POWERSOURCE | [POWERSOURCE](https://attack.mitre.org/software/S0145) has been observed being used to download [TEXTMATE](https://attack.mitre.org/software/S0146) and the Cobalt Strike Beacon payload onto victims.[^588]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034)’s loader component has downloaded the zip file node-v18.17.0-win-x64.zip from the official Node.js website, as well as pm2, a Node.js process management tool.[^767]  |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) can download files from remote servers.[^255]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) can download additional malware plug-in modules and execute them on the victim’s machine.[^113]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) has the ability to upload files to infected systems.[^717] [^58]  |
| [[CARROTBAT\|S0462]] | CARROTBAT | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to download and execute a remote file via [certutil](https://attack.mitre.org/software/S0160).[^798]  |
| [[WEBC2\|S0109]] | WEBC2 | [WEBC2](https://attack.mitre.org/software/S0109) can download and execute a file.[^157]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has downloaded “AnyDesk.exe” into the user’s home directory from the C2 server when checks for the service fail to identify its presence in the victim environment.[^96]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also been configured to download additional payloads using a command which calls to the /bow URI.[^206] [^409]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) uploads files and secondary payloads to the victim's machine.[^151]  |
| [[SharpDisco\|S1089]] | SharpDisco | [SharpDisco](https://attack.mitre.org/software/S1089) has been used to download a Python interpreter to `C:\Users\Public\WinTN\WinTN.exe` as well as other plugins from external sources.[^924]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) can download files to specified targets.[^811]  |
| [[HAPPYWORK\|S0214]] | HAPPYWORK | can download and execute a second-stage payload.[^142]  |
| [[xCaon\|S0653]] | xCaon | [xCaon](https://attack.mitre.org/software/S0653) has a command to download files to the victim's machine.[^476]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) has downloaded and executed additional plugins.[^942]  |
| [[Pony\|S0453]] | Pony | [Pony](https://attack.mitre.org/software/S0453) can download additional files onto the infected system.[^818] 	 |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can download files from C2.[^604]  |
| [[AuditCred\|S0347]] | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) can download files and additional malware.[^927]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has the ability to download additional files to the victim device.[^386]  |
| [[Kasidet\|S0088]] | Kasidet | [Kasidet](https://attack.mitre.org/software/S0088) has the ability to download and execute additional files.[^38]  |
| [[Hannotog\|S1211]] | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) can download additional files to the victim machine.[^82]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can download files to a compromised host.[^604]  |
| [[Ecipekac\|S0624]] | Ecipekac | [Ecipekac](https://attack.mitre.org/software/S0624) can download additional payloads to a compromised host.[^913]  |
| [[BUSHWALK\|S1118]] | BUSHWALK | [BUSHWALK](https://attack.mitre.org/software/S1118) can write malicious payloads sent through a web request’s command parameter.[^253] [^8]  |
| [[macOS.OSAMiner\|S1048]] | macOS.OSAMiner | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `curl` to download a [Stripped Payloads](https://attack.mitre.org/techniques/T1027/008) from a public facing adversary-controlled webpage.  |
| [[LOWBALL\|S0042]] | LOWBALL | [LOWBALL](https://attack.mitre.org/software/S0042) uses the Dropbox API to request two files, one of which is the same file as the one dropped by the malicious email attachment. This is most likely meant to be a mechanism to update the compromised host with a new version of the [LOWBALL](https://attack.mitre.org/software/S0042) malware.[^510]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can downloaded payloads from C2 to the compromised host.[^460] [^194]  |
| [[TinyTurla\|S0668]] | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) has the ability to act as a second-stage dropper used to infect the system with additional malware.[^907]  |
| [[PowerExchange\|S1173]] | PowerExchange | [PowerExchange](https://attack.mitre.org/software/S1173) can decode Base64-encoded files and call `WriteAllBytes` to write the files to compromised hosts.[^343]  |
| [[IMAPLoader\|S1152]] | IMAPLoader | [IMAPLoader](https://attack.mitre.org/software/S1152) is a loader used to retrieve follow-on payload encoded in email messages for execution on victim systems.[^42]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) can download additional modules and payloads.[^355]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to download additional payloads from C2.[^236]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) can download follow-on payloads and items via malicious `url` parameters in obfuscated PowerShell code.[^80]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) contains a command to retrieve files from its C2 server.[^201] [^278] [^97]  |
| [[Tomiris\|S0671]] | Tomiris | [Tomiris](https://attack.mitre.org/software/S0671) can download files and execute them on a victim's system.[^637]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can retrieve and load additional payloads.[^791]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can download additional files and tools from its C2.[^741]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) has the ability to load a second stage malicious DLL file onto a compromised machine.[^633]   |
| [[Machete\|S0409]] | Machete |  [Machete](https://attack.mitre.org/software/S0409) can download additional files for execution on the victim’s machine.[^294]   |
| [[PowerLess\|S1012]] | PowerLess | [PowerLess](https://attack.mitre.org/software/S1012) can download additional payloads to a compromised host.[^281]  |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to download additional payloads onto an infected machine.[^437]  |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) has the ability to download files from C2 to a compromised host.[^296]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has acted as a stager that can download the next-stage payload from its C2 server.[^163] [^731] [^311] [^266] [^35]  [PUBLOAD](https://attack.mitre.org/software/S1228) has also delivered FDMTP as a secondary control tool and PTSOCKET for exfiltration to some infected systems.[^713]  |
| [[SystemBC\|S9001]] | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) has downloaded additional files for execution on the victim’s machine.[^17] [^522]  The server component of [SystemBC](https://attack.mitre.org/software/S9001) has the ability to send additional files to victim machines.[^522]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) can fetch second stage code from hardcoded web domains.[^901] [^521]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can write files to a compromised host.[^457] [^805]  |
| [[Dacls\|S0497]] | Dacls | [Dacls](https://attack.mitre.org/software/S0497) can download its payload from a C2 server.[^923] [^289]  |
| [[DropBook\|S0547]] | DropBook | [DropBook](https://attack.mitre.org/software/S0547) can download and execute additional files.[^452] [^661]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can download files from its C2 server, including the .NET DLLs, `WoodySharpExecutor` and `WoodyPowerSession`.[^244]   |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can download additional files onto the compromised host.[^597]  |
| [[KARAE\|S0215]] | KARAE | [KARAE](https://attack.mitre.org/software/S0215) can upload and download files, including second-stage malware.[^142]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has downloaded and executed additional encoded payloads.[^525] [^836]  |
| [[PolyglotDuke\|S0518]] | PolyglotDuke | [PolyglotDuke](https://attack.mitre.org/software/S0518) can retrieve payloads from the C2 server.[^538]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has been used to download a malicious payload to include [BeaverTail](https://attack.mitre.org/software/S1246).[^727] [^89] [^813]  |
| [[Hildegard\|S0601]] | Hildegard | [Hildegard](https://attack.mitre.org/software/S0601) has downloaded additional scripts that build and run Monero cryptocurrency miners.[^611]  |
| [[Agent.btz\|S0092]] | Agent.btz | [Agent.btz](https://attack.mitre.org/software/S0092) attempts to download an encrypted binary from a specified domain.[^172]  |
| [[SLOWDRIFT\|S0218]] | SLOWDRIFT | [SLOWDRIFT](https://attack.mitre.org/software/S0218) downloads additional payloads.[^142]  |
| [[SHUTTERSPEED\|S0217]] | SHUTTERSPEED | [SHUTTERSPEED](https://attack.mitre.org/software/S0217) can download and execute an arbitary executable.[^142]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) has the ability to download and execute additional payloads.[^911] [^742] [^751]  |
| [[ODAgent\|S1170]] | ODAgent | [ODAgent](https://attack.mitre.org/software/S1170) has the ability to download and execute files on compromised systems.[^456]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) can transfer files from C2.[^264]  |
| [[Snip3\|S1086]] | Snip3 | [Snip3](https://attack.mitre.org/software/S1086) can download additional payloads to compromised systems.[^64] [^646]  |
| [[FYAnti\|S0628]] | FYAnti | [FYAnti](https://attack.mitre.org/software/S0628) can download additional payloads to a compromised host.[^913] 	  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has the ability to connect to a remote host in order to upload and download files.[^740] 	 |
| [[GuLoader\|S0561]] | GuLoader | [GuLoader](https://attack.mitre.org/software/S0561) can download further malware for execution on the victim's machine.[^715]  |
| [[MobileOrder\|S0079]] | MobileOrder | [MobileOrder](https://attack.mitre.org/software/S0079) has a command to download a file from the C2 server to the victim mobile device's SD card.[^9]  |
| [[RegDuke\|S0511]] | RegDuke | [RegDuke](https://attack.mitre.org/software/S0511) can download files from C2.[^538]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can upload files to the victim's machine for operations.[^348] [^109]  |
| [[P.A.S. Webshell\|S0598]] | P.A.S. Webshell | [P.A.S. Webshell](https://attack.mitre.org/software/S0598) can upload and download files to and from compromised hosts.[^626]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can download remote files and additional payloads to the victim's machine.[^934] [^366] [^660]  |
| [[WhisperGate\|S0689]] | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) can download additional stages of malware from a Discord CDN channel.[^591] [^896] [^771] [^680]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) can download additional payloads onto the victim.[^112]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) can download files via DNS.[^762] 	 |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has the ability to download files on an infected host.[^837]   |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) has built-in commands for uploading, downloading, and executing files to the system.[^694]  |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) can download additional modules from the C2 server.[^467]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can download additional files onto a compromised host.[^248]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) retrieves its second stage payload in a variety of ways such as through msiexec.exe abuse, or running the curl command to download the payload to the victim's `%AppData%` folder.[^29] [^725]  |
| [[RemoteCMD\|S0166]] | RemoteCMD | [RemoteCMD](https://attack.mitre.org/software/S0166) copies a file over to the remote system before execution.[^754]  |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) can receive configuration updates and additional payloads including wscpy.exe from C2.[^922]  |
| [[Doki\|S0600]] | Doki | [Doki](https://attack.mitre.org/software/S0600) has downloaded scripts from C2.[^60]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) has the ability to download additional modules and a configuration file from C2.[^85] [^869] [^24] [^492]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) can download and upload files to the victim's machine.[^863]  |
| [[UBoatRAT\|S0333]] | UBoatRAT | [UBoatRAT](https://attack.mitre.org/software/S0333) can upload and download files to the victim’s machine.[^906]  |
| [[HTTPTroy\|S9007]] | HTTPTroy | [HTTPTroy](https://attack.mitre.org/software/S9007) has the ability to download files from C2 using the `down <FILENAME>` command.[^242]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can download additional files and tools from its C2 server, including through the use of [BITSAdmin](https://attack.mitre.org/software/S0190).[^116]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) downloads additional plug-ins to load on the victim’s machine, including the ability to upgrade and replace its own binary.[^722]  |
| [[NavRAT\|S0247]] | NavRAT | [NavRAT](https://attack.mitre.org/software/S0247) can download files remotely.[^706]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) can load any files onto the infected machine to execute.[^563] [^552]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can download additional files from C2.[^809]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can download and execute a replica of itself using [certutil](https://attack.mitre.org/software/S0160).[^428]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) can deploy additional tools onto an infected machine.[^598]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) can download additional files.[^570]  |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can download its code from C2.[^895]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has download files from its C2 server.[^801]  |
| [[Conficker\|S0608]] | Conficker | [Conficker](https://attack.mitre.org/software/S0608) downloads an HTTP server to the infected machine.[^712]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) can download additional malware to infected hosts.[^524] [^732]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) can download additional malware from the C2 server.[^173]  |
| [[Hi-Zor\|S0087]] | Hi-Zor | [Hi-Zor](https://attack.mitre.org/software/S0087) has the ability to upload and download files from its C2 server.[^299]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) can download malicious files from threat actor controlled AWS URL's.[^825]  |
| [[China Chopper\|S0020]] | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020)'s server component can download remote files.[^642] [^860] [^371] [^847] [^384]  |
| [[LightSpy\|S1185]] | LightSpy | On macOS, [LightSpy](https://attack.mitre.org/software/S1185) downloads a `.json` file from the C2 server. The `.json` file contains metadata about the plugins to be downloaded, including their URL, name, version, and MD5 hash. [LightSpy](https://attack.mitre.org/software/S1185) retrieves the plugins specified in the `.json` file, which are compiled `.dylib` files. These `.dylib` files provide task and platform specific functionality. [LightSpy](https://attack.mitre.org/software/S1185) also imports open-source libraries to manage socket connections.[^102]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can download additional files and payloads to compromised hosts.[^265] [^889]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) can download and execute additional files.[^513] [^222]  |
| [[CostaBricks\|S0614]] | CostaBricks | [CostaBricks](https://attack.mitre.org/software/S0614) has been used to load [SombRAT](https://attack.mitre.org/software/S0615) onto a compromised host.[^911]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) has a download and upload functionality.[^285] [^323]  |
| [[POSHSPY\|S0150]] | POSHSPY | [POSHSPY](https://attack.mitre.org/software/S0150) downloads and executes additional PowerShell code and Windows binaries.[^589]  |
| [[MiniDuke\|S0051]] | MiniDuke | [MiniDuke](https://attack.mitre.org/software/S0051) can download additional encrypted backdoors onto the victim via GIF files.[^840] [^538]  |
| [[HyperBro\|S0398]] | HyperBro | [HyperBro](https://attack.mitre.org/software/S0398) has the ability to download additional files.[^445]  |
| [[Anchor\|S0504]] | Anchor | [Anchor](https://attack.mitre.org/software/S0504) can download additional payloads.[^533] [^695]  |
| [[Pteranodon\|S0147]] | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) can download and execute additional files.[^656] [^590] [^186]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) can download additional packages for keylogging, cryptocurrency mining, and other capabilities; it can also retrieve malicious payloads such as [Agent Tesla](https://attack.mitre.org/software/S0331), AsyncRat, [NanoCore](https://attack.mitre.org/software/S0336), RedLine, [Cobalt Strike](https://attack.mitre.org/software/S0154), and Metasploit.[^57]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has been used to download a malicious payload to include Python based malware [InvisibleFerret](https://attack.mitre.org/software/S1245).[^315] [^89] [^813] [^96] [^409] [^448]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can retrieve additional malicious payloads from its C2 server.[^181] [^512] [^808] [^568]  |
| [[CORESHELL\|S0137]] | CORESHELL | [CORESHELL](https://attack.mitre.org/software/S0137) downloads another dropper from its C2 server.[^908]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) has a command to download and executes additional files.[^179]  |
| [[BlackMould\|S0564]] | BlackMould | [BlackMould](https://attack.mitre.org/software/S0564) has the ability to download files to the victim's machine.[^425]  |
| [[Javali\|S0528]] | Javali | [Javali](https://attack.mitre.org/software/S0528) can download payloads from remote C2 servers.[^162]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has a module to download and execute files on the compromised machine.[^490] [^170] [^719] [^868]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has the capability to download files to execute on the victim’s machine.[^606] [^320] [^247]   |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) can download additional files onto a compromised host.[^849]  |
| [[SeaDuke\|S0053]] | SeaDuke | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of uploading and downloading files.[^650]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) contains a network loader to receive executable modules from remote attackers and run them on the local victim. It can also upload and download files over HTTP and HTTPS.[^439] [^458]  |
| [[Explosive\|S0569]] | Explosive | [Explosive](https://attack.mitre.org/software/S0569) has a function to download a file to the infected system.[^497]   |
| [[Xbash\|S0341]] | Xbash | [Xbash](https://attack.mitre.org/software/S0341) can download additional malicious files from its C2 server.[^368]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) has the ability to download and execute additional files.[^861]  |
| [[Peppy\|S0643]] | Peppy | [Peppy](https://attack.mitre.org/software/S0643) can download and execute remote files.[^201]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can download files from its C2 server.[^37]  |
| [[DEATHRANSOM\|S0616]] | DEATHRANSOM | [DEATHRANSOM](https://attack.mitre.org/software/S0616) can download files to a compromised host.[^742]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can download additional payloads for execution on the compromised host.[^219] [^335]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) retrieves cryptocurrency mining payloads and commands in encrypted traffic from its command and control server.[^886]  [DarkGate](https://attack.mitre.org/software/S1111) uses Windows Batch scripts executing the `curl` command to retrieve follow-on payloads.[^930]  [DarkGate](https://attack.mitre.org/software/S1111) has stolen `sitemanager.xml` and `recentservers.xml` from `%APPDATA%\FileZilla\` if present.[^529]   |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) can download files to targeted systems.[^941]  |
| [[NanHaiShu\|S0228]] | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) can download additional files from URLs.[^857]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) has the ability to download additional tools such as the RedLine Stealer to an infected host.[^696]  |
| [[ThiefQuest\|S0595]] | ThiefQuest | [ThiefQuest](https://attack.mitre.org/software/S0595) can download and execute payloads in-memory or from disk.[^324]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) can receive additional malicious components from an actor controlled C2 server and execute them on a compromised AD FS server.[^392]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can download files and additional malware components.[^13] [^346]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to upload and download files.[^599]  |
| [[CreepyDrive\|S1023]] | CreepyDrive | [CreepyDrive](https://attack.mitre.org/software/S1023) can download files to the compromised host.[^634]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a module to download and upload files to the system.[^290]   |
| [[Netwalker\|S0457]] | Netwalker | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used psexec and certutil to retrieve the [Netwalker](https://attack.mitre.org/software/S0457) payload.[^745]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) can download additional files from the C2 server for execution.[^354]  |
| [[Gazer\|S0168]] | Gazer | [Gazer](https://attack.mitre.org/software/S0168) can execute a task to download a file.[^127] [^249]  |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to upload and download files to and from the infected host.[^187]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can download and execute PEs, DLLs, and shellcode from C2.[^492] [^197] [^530]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can download additional files onto a compromised host.[^823]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) can download additional files onto an infected machine.[^208]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) has the ability to download additional files from the C2.[^12] [^262] [^431]  |
| [[Briba\|S0204]] | Briba | [Briba](https://attack.mitre.org/software/S0204) downloads files onto infected hosts.[^193]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to download additional modules to a compromised host.[^328]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to download files from the C2 server. Additionally, [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to download a file in chunks with sleep time between each chunk.[^215]       |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) can upload and download files to the victim’s machine.[^718]  |
| [[Bundlore\|S0482]] | Bundlore | [Bundlore](https://attack.mitre.org/software/S0482) can download and execute new versions of itself.[^177]  |
| [[P8RAT\|S0626]] | P8RAT | [P8RAT](https://attack.mitre.org/software/S0626) can download additional payloads to a target system.[^913]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can download and upload files to the victim's computer.[^903] [^532]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has used Powershell to download UltraVNC and [ngrok](https://attack.mitre.org/software/S0508) from third-party file sharing sites.[^435]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can download additional modules from its C2 server.[^54]  |
| [[BendyBear\|S0574]] | BendyBear | [BendyBear](https://attack.mitre.org/software/S0574) is designed to download an implant from a C2 server.[^344]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has downloaded additional payloads from C2.[^749] [^474] [^772] [^78]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can use a `Put` command to write files to an infected machine.[^273]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has used MSI files to download additional files to execute.[^560] [^678] [^667] [^351]   |
| [[Spica\|S1140]] | Spica | [Spica](https://attack.mitre.org/software/S1140) can upload and download files to and from compromised hosts.[^698]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can upload, download, and execute files on the victim.[^275] [^829]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) can download files to the system.[^373]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) can install additional modules via C2 commands.[^202]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) can import and execute additional payloads.[^480]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) can download files and execute them on the victim’s machine.[^618] [^174]   |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) has the ability to deploy modules directly from command and control (C2) servers, possibly for remote command execution, file exfiltration, and socks5 proxying on the infected host. [^756]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) can download files to the victim’s machine.[^416] [^83]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) can download an executable to run on the victim.[^536]  |
| [[DnsSystem\|S1021]] | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) can download files to compromised systems after receiving a command with the string `downloaddd`.[^735]  |
| [[MoleNet\|S0553]] | MoleNet | [MoleNet](https://attack.mitre.org/software/S0553) can download additional payloads from the C2.[^452]   |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [JHUHUGIT](https://attack.mitre.org/software/S0044) can retrieve an additional payload from its C2 server.[^153] [^62]  [JHUHUGIT](https://attack.mitre.org/software/S0044) has a command to download files to the victim’s machine.[^104]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) can download additional files onto the host.[^866]   |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to download and execute code from remote servers.[^254]  |
| [[down_new\|S0472]] | down_new | [down_new](https://attack.mitre.org/software/S0472) has the ability to download files to the compromised host.[^296]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) can download and execute additional files.[^258]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) can download and execute an executable from the C2 server.[^774] [^334]  |
| [[Kerrdown\|S0585]] | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) can download specific payloads to a compromised host based on OS architecture.[^705]  |
| [[RARSTONE\|S0055]] | RARSTONE | [RARSTONE](https://attack.mitre.org/software/S0055) downloads its backdoor component from a C2 server and loads it directly into memory.[^482]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has the ability download additional payloads.[^302] [^307]  |
| [[VBShower\|S0442]] | VBShower | [VBShower](https://attack.mitre.org/software/S0442) has the ability to download VBS files to the target computer.[^918]  |
| [[StoneDrill\|S0380]] | StoneDrill | [StoneDrill](https://attack.mitre.org/software/S0380) has downloaded and dropped temporary files containing scripts; it additionally has a function to upload files from the victims machine.[^152] 	 |
| [[OopsIE\|S0264]] | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) can download files from its C2 server to the victim's machine.[^103] [^502]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) can save a new file to the system from the C2 server.[^654] [^387]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438) can download additional plugins, updates and other files. [^821]  |
| [[SQLRat\|S0390]] | SQLRat | [SQLRat](https://attack.mitre.org/software/S0390) can make a direct SQL connection to a Microsoft database controlled by the attackers, retrieve an item from the bindata table, then write and execute the file on disk.[^50] 	 |
| [[LitePower\|S0680]] | LitePower | [LitePower](https://attack.mitre.org/software/S0680) has the ability to download payloads containing system commands to a compromised host.[^610]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) can download files.[^476]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can load multiple additional plugins on an infected host.[^924]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to download a DLL from C2 to a compromised host.[^571]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) can upload and download files to the victim.[^600]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can download additional files.[^128] [^63]  |
| [[PHPsert\|S9028]] | PHPsert | [PHPsert](https://attack.mitre.org/software/S9028) has the ability to retrieve remote payloads.[^581]  |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) has the ability to download additional payloads from C2 to the targeted system.[^913]  |
| [[Hikit\|S0009]] | Hikit | [Hikit](https://attack.mitre.org/software/S0009) has the ability to download files to a compromised host.[^781]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) installers have used obfuscated PowerShell scripts to retrieve follow-on payloads from WebDAV servers.[^339]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can download its second stage from a hardcoded URL within the loader's code.[^785] [^165]  |
| [[WellMail\|S0515]] | WellMail | [WellMail](https://attack.mitre.org/software/S0515) can receive data and executable scripts from C2.[^498]  |
| [[LiteDuke\|S0513]] | LiteDuke | [LiteDuke](https://attack.mitre.org/software/S0513) has the ability to download files.[^538]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) has the capability to download files.[^312]  |
| [[VaporRage\|S0636]] | VaporRage | [VaporRage](https://attack.mitre.org/software/S0636) has the ability to download malicious shellcode to compromised systems.[^620]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) can download and execute a payload onto a compromised system.[^513]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) can download and execute additional files.[^412]  |
| [[Caminho\|S9016]] | Caminho | [Caminho](https://attack.mitre.org/software/S9016) has the ability to download files onto compromised hosts.[^873]  |
| [[Drovorub\|S0502]] | Drovorub | [Drovorub](https://attack.mitre.org/software/S0502) can download files to a compromised host.[^494]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019)  can download additional files from its C2 via HTTP or DNS.[^155] [^648]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can download and deploy additional payloads, including ransomware and post-exploitation frameworks such as [Cobalt Strike](https://attack.mitre.org/software/S0154).[^81] [^692] [^287] [^824]  |
| [[BadPatch\|S0337]] | BadPatch | [BadPatch](https://attack.mitre.org/software/S0337) can download and execute or update malware.[^517]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) uploads and downloads information.[^263] [^72]  |
| [[Nidiran\|S0118]] | Nidiran | [Nidiran](https://attack.mitre.org/software/S0118) can download and execute files.[^19]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can download files from the C2 to victim systems.[^915] [^671]  |
| [[Cryptoistic\|S0498]] | Cryptoistic | [Cryptoistic](https://attack.mitre.org/software/S0498) has the ability to send and receive files.[^923]  |
| [[ABK\|S0469]] | ABK | [ABK](https://attack.mitre.org/software/S0469) has the ability to download files from C2.[^296]  |
| [[OilCheck\|S1171]] | OilCheck | [OilCheck](https://attack.mitre.org/software/S1171) can download staged payloads from an actor-controlled infrastructure.[^456]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) obtains additional code to execute on the victim's machine, including the downloading of a secondary payload.[^603] [^828] [^400] [^714]  |
| [[Pandora\|S0664]] | Pandora | [Pandora](https://attack.mitre.org/software/S0664) can load additional drivers and files onto a victim machine.[^214]  |
| [[SpeakUp\|S0374]] | SpeakUp | [SpeakUp](https://attack.mitre.org/software/S0374) downloads and executes additional files from a remote server. [^345]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can deliver additional payloads to victim machines.[^556] [^25]  |
| [[SampleCheck5000\|S1168]] | SampleCheck5000 | [SampleCheck5000](https://attack.mitre.org/software/S1168) can download additional payloads to compromised hosts.[^47] [^456]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) delivered different payloads, including [TEARDROP](https://attack.mitre.org/software/S0560) in at least one instance.[^133]  |
| [[EvilBunny\|S0396]] | EvilBunny | [EvilBunny](https://attack.mitre.org/software/S0396) has downloaded additional Lua scripts from the C2.[^509]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to upload a file from the command and control (C2) server to the victim machine.[^160]  |
| [[ServHelper\|S0382]] | ServHelper | [ServHelper](https://attack.mitre.org/software/S0382) may download additional files to execute.[^182] [^141]  |
| [[Unknown Logger\|S0130]] | Unknown Logger | [Unknown Logger](https://attack.mitre.org/software/S0130) is capable of downloading remote files.[^499]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can download a copy of itself from an attacker controlled IP address to the victim machine.[^682] [^270] [^440]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) has downloaded a variety of modules and payloads to the compromised host, including [IcedID](https://attack.mitre.org/software/S0483) and NetSupport Manager RAT-based malware.[^518] [^585]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) has been used to deploy other malware including [Ninja](https://attack.mitre.org/software/S1100).[^384]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) has received files from C2 and stored them in log folders beginning with the character sequence `a9850d2f`.[^155]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has a command to download and execute a file on the victim’s machine.[^593] [^574]  |
| [[OilBooster\|S1172]] | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) can download and execute files from an actor-controlled OneDrive account.[^456]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) has downloaded additional files onto a compromised host.[^839]  |
| [[Kivars\|S0437]] | Kivars | [Kivars](https://attack.mitre.org/software/S0437) has the ability to download and execute files.[^337]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) has the ability to download files to target systems.[^557] [^914]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can upload files.[^286]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) has a command to download additional files.[^905] [^905]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) has the capability to download and activate additional modules for execution.[^851] [^470]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to upload and download files to and from an infected host.[^411]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) downloads various library files enabling interaction with various data stores and structures to facilitate follow-on information theft.[^317] [^231]  |
| [[Daserf\|S0187]] | Daserf | [Daserf](https://attack.mitre.org/software/S0187) can download remote files.[^167] [^204]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) can download and execute additional payloads.[^397]  |
| [[DanBot\|S1014]] | DanBot | [DanBot](https://attack.mitre.org/software/S1014) can download additional files to a targeted system.[^291]  |
| [[BISCUIT\|S0017]] | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to download a file from the C2 server.[^905]  |
| [[Calisto\|S0274]] | Calisto | [Calisto](https://attack.mitre.org/software/S0274) has the capability to upload and download files to the victim's machine.[^229]  |
| [[Solar\|S1166]] | Solar | [Solar](https://attack.mitre.org/software/S1166) has the ability to download and execute files.[^47]  |
| [[Pisloader\|S0124]] | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) has a command to upload a file to the victim machine.[^856]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) constantly attempts to download and execute files from the remote C2, including [GoldenSpy](https://attack.mitre.org/software/S0493) itself if not found on the system.[^882] 	 |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) can download additional components from the C2 server.[^545]  |
| [[RGDoor\|S0258]] | RGDoor | [RGDoor](https://attack.mitre.org/software/S0258) uploads and downloads files to and from the victim’s machine.[^627]  |
| [[Neo-reGeorg\|S1189]] | Neo-reGeorg | [Neo-reGeorg](https://attack.mitre.org/software/S1189) has the ability to download files to targeted systems.[^322]  |
| [[AshTag\|S9031]] | AshTag | The [AshTag](https://attack.mitre.org/software/S9031) stager component can retrieve and execute the main payload.[^143]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) can download and execute new plugins from the C2 server. [^558] [^403]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) has the ability to upload and download files.[^702]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) has downloaded additional files, including an exploit for used privilege escalation.[^71] [^144]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can download additional files onto a compromised host.[^375]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) can download and launch additional payloads.[^885] [^124]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) has the ability to download files to a compromised host.[^214] [^195]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) can download files from its C2 server.[^823]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) can download and execute additional payloads on a compromised host.[^622]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) downloads additional files from C2 servers.[^131]  |
| [[Nerex\|S0210]] | Nerex | [Nerex](https://attack.mitre.org/software/S0210) creates a backdoor through which remote attackers can download files onto a compromised host.[^408]  |
| [[BoomBox\|S0635]] | BoomBox | [BoomBox](https://attack.mitre.org/software/S0635) has the ability to download next stage malware components to a compromised system.[^620]  |
| [[WIREFIRE\|S1115]] | WIREFIRE | [WIREFIRE](https://attack.mitre.org/software/S1115) has the ability to download files to compromised devices.[^764]  |
| [[Kessel\|S0487]] | Kessel | [Kessel](https://attack.mitre.org/software/S0487) can download additional modules from the C2 server.[^467]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) has the ability to download and execute additional payloads.[^768]  |
| [[STEADYPULSE\|S1112]] | STEADYPULSE | [STEADYPULSE](https://attack.mitre.org/software/S1112) can add lines to a Perl script on a targeted server to import additional Perl modules.[^161]  |
| [[PHASEJAM\|S9014]] | PHASEJAM | [PHASEJAM](https://attack.mitre.org/software/S9014) has the ability to upload files onto the compromised appliance.[^424]  |
| [[YAHOYAH\|S0388]] | YAHOYAH | [YAHOYAH](https://attack.mitre.org/software/S0388) uses HTTP GET requests to download other files that are executed in memory.[^835]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) downloaded several staged items onto the victim's machine.[^340]   |
| [[CallMe\|S0077]] | CallMe | [CallMe](https://attack.mitre.org/software/S0077) has the capability to download a file to the victim from the C2 server.[^9]  |
| [[CloudDuke\|S0054]] | CloudDuke | [CloudDuke](https://attack.mitre.org/software/S0054) downloads and executes additional malware from either a Web address or a Microsoft OneDrive account.[^547]  |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) has the ability to download files from its C2 server.[^874] [^178]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has the ability to copy files and download/upload files into C2 channels using FTP and HTTPS.[^514] [^168]  |
| [[CHOPSTICK\|S0023]] | CHOPSTICK | [CHOPSTICK](https://attack.mitre.org/software/S0023) is capable of performing remote file transmission.[^256]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) downloads and uploads files to and from the victim’s machine.[^220] [^355]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) has a command to transfer files from a remote host.[^676]   |
| [[RIFLESPINE\|S1222]] | RIFLESPINE | [RIFLESPINE](https://attack.mitre.org/software/S1222) can download and execute files.[^196]  |
| [[SLIGHTPULSE\|S1110]] | SLIGHTPULSE | [RAPIDPULSE](https://attack.mitre.org/software/S1113) can transfer files to and from compromised hosts.[^621]  |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) can download and execute a file from given URL.[^347]  |
| [[CoinTicker\|S0369]] | CoinTicker | [CoinTicker](https://attack.mitre.org/software/S0369) executes a Python script to download its second stage.[^553]  |
| [[DDKONG\|S0255]] | DDKONG | [DDKONG](https://attack.mitre.org/software/S0255) downloads and uploads files on the victim’s machine.[^942]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) can execute the command code `do_download` to retrieve remote files from C2.[^282]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has downloaded additional files from the C2.[^423] [^488]  |
| [[Cannon\|S0351]] | Cannon | [Cannon](https://attack.mitre.org/software/S0351) can download a payload for execution.[^828]  |
| [[build_downer\|S0471]] | build_downer | [build_downer](https://attack.mitre.org/software/S0471) has the ability to download files from C2 to the infected host.[^296]  |
| [[Melcoz\|S0530]] | Melcoz | [Melcoz](https://attack.mitre.org/software/S0530) has the ability to download additional files to a compromised host.[^162]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | The [Winnti for Windows](https://attack.mitre.org/software/S0141) dropper can place malicious payloads on targeted systems.[^802]  |
| [[PowerPunch\|S0685]] | PowerPunch | [PowerPunch](https://attack.mitre.org/software/S0685) can download payloads from adversary infrastructure.[^70]  |
| [[BONDUPDATER\|S0360]] | BONDUPDATER | [BONDUPDATER](https://attack.mitre.org/software/S0360) can download or upload files from its C2 server.[^716]  |
| [[Kinsing\|S0599]] | Kinsing | [Kinsing](https://attack.mitre.org/software/S0599) has downloaded additional lateral movement scripts from C2.[^188]  |
| [[Meteor\|S0688]] | Meteor | [Meteor](https://attack.mitre.org/software/S0688) has the ability to download additional files for execution on the victim's machine.[^831]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can download files to the victim’s machine.[^117] [^228]  [APT-C-36](https://attack.mitre.org/groups/G0099) has used modified versions of [njRAT](https://attack.mitre.org/software/S0385) to enable the download of .NET assemblies.[^295]  |
| [[ZIPLINE\|S1114]] | ZIPLINE | [ZIPLINE](https://attack.mitre.org/software/S1114) can download files to be saved on the compromised system.[^764] [^253]  |
| [[TURNEDUP\|S0199]] | TURNEDUP | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of downloading additional files.[^240]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) is capable of downloading files, including additional modules.[^166] [^372] [^369]  |
| [[ANDROMEDA\|S1074]] | ANDROMEDA | [ANDROMEDA](https://attack.mitre.org/software/S1074) can download additional payloads from C2.[^77]  |
| [[Shai-Hulud\|S9008]] | Shai-Hulud | [Shai-Hulud](https://attack.mitre.org/software/S9008) has downloaded packages from code repositories.[^846] [^308] [^65] [^436]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also downloaded and executed the secrets-discovery tool [TruffleHog](https://attack.mitre.org/software/S9009) to gather sensitive data.[^561] [^308] [^937] [^65] [^436]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can download files and upgrade itself.[^912]  |
| [[VIRTUALPITA\|S1217]] | VIRTUALPITA | [VIRTUALPITA](https://attack.mitre.org/software/S1217) has the ability to upload and download files.[^465]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can download files onto compromised systems.[^40] [^597]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to download additional files.[^292]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has executed a PowerShell command to download a file to the system.[^140]  |
| [[MechaFlounder\|S0459]] | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to upload and download files to and from a compromised host.[^763]  |
| [[Psylo\|S0078]] | Psylo | [Psylo](https://attack.mitre.org/software/S0078) has a command to download a file to the system from its C2 server.[^9]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of writing a file to the compromised system from the C2 server.[^761]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) has downloaded additional malware and files onto a compromised host.[^849]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) downloads browser specific AppleScript modules using a constructed URL with the `curl` command, `https://" & domain & "/agent/scripts/" & moduleName & ".applescript`.[^399]  |
| [[Disco\|S1088]] | Disco | [Disco](https://attack.mitre.org/software/S1088) can download files to targeted systems via SMB.[^924]  |
| [[Dipsind\|S0200]] | Dipsind | [Dipsind](https://attack.mitre.org/software/S0200) can download remote files.[^912]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can download additional files and tools onto the victim’s machine.[^721] [^79] [^675]  |
| [[SoreFang\|S0516]] | SoreFang | [SoreFang](https://attack.mitre.org/software/S0516) can download additional payloads from C2.[^401] [^939]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604) downloads a shellcode payload from a remote C2 server and loads it into memory.[^697]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can download files to the compromised host.[^147]  |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can download additional files for execution on the victim’s machine.[^377] [^471]  |
| [[Pasam\|S0208]] | Pasam | [Pasam](https://attack.mitre.org/software/S0208) creates a backdoor through which remote attackers can upload files.[^875]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve and execute additional [PowerShell](https://attack.mitre.org/techniques/T1059/001) payloads from the C2 server.[^534]  |
| [[BADNEWS\|S0128]] | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) is capable of downloading additional files through C2 channels, including a new version of itself.[^499] [^601] [^347]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can download files onto compromised hosts.[^466]  |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) has downloaded code from a C2 server.[^938]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) uses [certutil](https://attack.mitre.org/software/S0160) and [BITSAdmin](https://attack.mitre.org/software/S0190) to download additional malware. [^659] [^284] [^162]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) has the ability to download additional components and malware.[^61] [^699] [^443] [^135] [^688] [^267]  |
| [[DOWNIISSA\|S9021]] | DOWNIISSA | [DOWNIISSA](https://attack.mitre.org/software/S9021) can download files to the compromised host.[^364]  |
| [[CookieMiner\|S0492]] | CookieMiner | [CookieMiner](https://attack.mitre.org/software/S0492) can download additional scripts from a web server.[^707]  |
| [[Hancitor\|S0499]] | Hancitor | [Hancitor](https://attack.mitre.org/software/S0499) has the ability to download additional files from C2.[^595]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can download additional plug-ins to a compromised host.[^895]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) can download and execute files.[^816] [^602] [^546]  |
| [[Helminth\|S0170]] | Helminth | [Helminth](https://attack.mitre.org/software/S0170) can download additional files.[^198]  |
| [[BBK\|S0470]] | BBK | [BBK](https://attack.mitre.org/software/S0470) has the ability to download files from C2 to the infected host.[^296]  |
| [[OSX／Shlayer\|S0402]] | OSX／Shlayer | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can download payloads, and extract bytes from files. [OSX/Shlayer](https://attack.mitre.org/software/S0402) uses the `curl -fsL "$url" >$tmp_path` command to download malicious payloads into a temporary directory.[^757] [^575] [^350] [^489]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) deploys additional backdoors and hacking tools to the system.[^859]  |
| [[Waterbear\|S0579]] | Waterbear | [Waterbear](https://attack.mitre.org/software/S0579) can receive and load executables from remote C2 servers.[^426]  |
| [[Vasport\|S0207]] | Vasport | [Vasport](https://attack.mitre.org/software/S0207) can download files.[^862]  |
| [[JSS Loader\|S0648]] | JSS Loader | [JSS Loader](https://attack.mitre.org/software/S0648) has the ability to download malicious executables to a compromised host.[^605]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) can download additional plugins, files, and tools.[^614] [^787] [^890]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567)’s can download and upload a file to the victim’s computer.[^459] [^442]  |
| [[H1N1\|S0132]] | H1N1 | [H1N1](https://attack.mitre.org/software/S0132) contains a command to download and execute a file from a remotely hosted URL using WinINet HTTP requests.[^853]  |
| [[Seth-Locker\|S0639]] | Seth-Locker | [Seth-Locker](https://attack.mitre.org/software/S0639) has the ability to download and execute files on a compromised host.[^815]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) used SCP to update the miner from the C2.[^67]  |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can download and execute additional files. [Azorult](https://attack.mitre.org/software/S0344) has also downloaded a ransomware payload called Hermes.[^239] [^427]  |
| [[Zox\|S0672]] | Zox | [Zox](https://attack.mitre.org/software/S0672) can download files to a compromised machine.[^781]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) can download and upload files to and from the victim’s machine.[^472] [^551] [^2] <br> |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can download updates and auxiliary modules.[^189]  |
| [[Mivast\|S0080]] | Mivast | [Mivast](https://attack.mitre.org/software/S0080) has the capability to download and execute .exe files.[^468]  |
| [[HiddenWasp\|S0394]] | HiddenWasp | [HiddenWasp](https://attack.mitre.org/software/S0394) downloads a tar compressed archive from a download server to the system.[^800]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can download and execute additional files.[^336]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has downloaded files onto a victim machine.[^190]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has been used to download a malicious payload to include [BeaverTail](https://attack.mitre.org/software/S1246).[^89]  |
| [[Small Sieve\|S1035]] | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) has the ability to download files.[^653]  |
| [[Indrik Spider\|G0119]] | Indrik Spider | [Indrik Spider](https://attack.mitre.org/groups/G0119) has downloaded additional scripts, malware, and tools onto a compromised host.[^87] [^462] [^418]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has downloaded additional malware and tools onto a compromised host.[^900] [^668]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [certutil](https://attack.mitre.org/software/S0160), PowerShell, and Windows Command to download additional tools to include RMM services.[^44]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also engaged in “Bring Your Own Vulnerable Driver” (BYOVD) and downloaded vulnerable or signed drivers to the victim environment to disable security tools.[^44] [^235]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) can transfer malicious payloads such as ransomware to compromised machines.[^164]  |
| [[Elderwood\|G0066]] | Elderwood | The Ritsol backdoor trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) can download files onto a compromised host from a remote location.[^408]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has downloaded additional malware to execute on the victim's machine, including by using a PowerShell script to launch shellcode that retrieves an additional payload.[^363] [^584] [^559] [^33]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has downloaded PowerShell code from the C2 server to be executed.[^93]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has copied and installed tools for operations once in the victim environment.[^156]  |
| [[APT-C-36\|G0099]] | APT-C-36 | [APT-C-36](https://attack.mitre.org/groups/G0099) has downloaded binary data from a specified domain after the malicious document is opened.[^486]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) had downloaded remote files onto victim infrastructure.[^353] [^130]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has downloaded additional tools including [PsExec](https://attack.mitre.org/software/S0029) directly to endpoints.[^349]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has downloaded files, malware, and tools from its C2 onto a compromised host.[^730] [^569] [^374] [^923] [^289] [^649] [^483] [^838] [^663] [^887]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has downloaded additional malware onto compromised hosts.[^872]  |
| [[Daggerfly\|G1034]] | Daggerfly | [Daggerfly](https://attack.mitre.org/groups/G1034) has used PowerShell and [BITSAdmin](https://attack.mitre.org/software/S0190) to retrieve follow-on payloads from external locations for execution on victim machines.[^655]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has the `curl` and `wget` commands as well as batch scripts to download new tools.[^382] [^230]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has downloaded additional malware to execute on victim systems.[^333] [^141] [^519]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has downloaded additional scripts, tools, and malware onto victim systems.[^789] [^516] [^250] [^180]  |
| [[Play\|G1040]] | Play | [Play](https://attack.mitre.org/groups/G1040) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to download files to compromised machines.[^404]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has pushed additional malicious tools onto an infected system to steal user credentials, move laterally, and destroy data.[^76] [^531]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has used shellcode to download Meterpreter after compromising a victim.[^515]  |
| [[Silence\|G0091]] | Silence | [Silence](https://attack.mitre.org/groups/G0091) has downloaded additional modules and malware to victim’s machines.[^237] 	 |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) payloads download additional files from the C2 server.[^31] [^347]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has downloaded additional files, including by using a first-stage downloader to contact the C2 server to obtain the second-stage implant.[^20] [^342] [^714] [^670] [^827]  |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has downloaded files, including [Cobalt Strike](https://attack.mitre.org/software/S0154), to compromised hosts.[^441]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has downloaded additional payloads and malicious scripts onto a compromised host.[^147]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has used first-stage payloads that download additional malware from C2 servers.[^580]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has used tools to download files to compromised machines.[^248]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has downloaded an outdated version of comsvcs.dll to a compromised domain controller in a non-standard folder.[^528]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has downloaded additional code and files from servers onto victims.[^865] [^504] [^582] [^817]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has downloaded additional tools and malware onto compromised networks.[^395] [^457] [^547] [^936]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used public sites such as github.com and sendspace.com to upload files and then download them to victim computers.[^55] [^252]  The group's JavaScript backdoor is also capable of downloading files.[^690]  |
| [[Andariel\|G0138]] | Andariel | [Andariel](https://attack.mitre.org/groups/G0138) has downloaded additional tools and malware onto compromised hosts.[^523]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has downloaded malware and tools--including Nishang and PowerCat--onto a compromised host.[^496] [^847]   |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has downloaded tools to compromised hosts.[^795] [^283]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that can upload additional files to the victim’s machine.[^855] [^150] [^833] [^684]  [MuddyWater](https://attack.mitre.org/groups/G0069) has used PowerShell commands to install remote management and monitoring (RMM) software on the victim’s machine to conduct espionage and to exfiltrate data.[^207]   |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) used a backdoor, NESTEGG, that has the capability to download and upload files to and from a victim’s machine.[^199]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has downloaded other payloads onto a victim’s machine.[^446]   |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has added JavaScript to victim websites to download additional frameworks that profile and compromise website visitors.[^245]  |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used various tools to download files, including DGet (a similar tool to wget).[^204]  |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has downloaded additional files and tools onto a compromised host.[^741]  |
| [[Leviathan\|G0065]] | Leviathan | [Leviathan](https://attack.mitre.org/groups/G0065) has downloaded additional scripts and files from adversary-controlled servers.[^857] [^642]  |
| [[Storm-1811\|G1046]] | Storm-1811 | [Storm-1811](https://attack.mitre.org/groups/G1046) has used scripted `cURL` commands, [BITSAdmin](https://attack.mitre.org/software/S0190), and other mechanisms to retrieve follow-on batch scripts and tools for execution on victim devices.[^786] [^176] [^53]  |
| [[Ajax Security Team\|G0130]] | Ajax Security Team | [Ajax Security Team](https://attack.mitre.org/groups/G0130) has used Wrapper/Gholee, custom-developed malware, which downloaded additional malware to the infected system.[^68]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has downloaded additional executables following the initial infection stage.[^880] [^34] [^770] [^888]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged Visual Studio Code `code.exe` and Dev Tunnels using `DevTunnel.exe` to propagate additional tools and payloads.[^607]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has remotely copied tools and malware onto targeted systems.[^16]  |
| [[TA2541\|G1018]] | TA2541 | <br>[TA2541](https://attack.mitre.org/groups/G1018) has used malicious scripts and macros with the ability to download additional payloads.[^526] <br> |
| [[BITTER\|G1002]] | BITTER | [BITTER](https://attack.mitre.org/groups/G1002) has downloaded additional malware and tools onto a compromised host.[^412] [^69]   |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has installed updates and new malware on victims.[^316] [^481]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used a delivered trojan to download additional files.[^834]  |
| [[Mustard Tempest\|G1020]] | Mustard Tempest | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has deployed secondary payloads and third stage implants to compromised hosts.[^200]  |
| [[Moses Staff\|G1009]] | Moses Staff | [Moses Staff](https://attack.mitre.org/groups/G1009) has downloaded and installed web shells to following path `C:\inetpub\wwwroot\aspnet_client\system_web\IISpool.aspx`.[^540]  |
| [[Molerats\|G0021]] | Molerats | [Molerats](https://attack.mitre.org/groups/G0021) used executables to download malicious files from different sources.[^98] [^420]   |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) has downloaded second stage malware from compromised websites.[^142] [^383] [^866] [^808]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has deployed additional payloads from dedicated C2 servers.[^640] [^940] [^780]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has also downloaded legitimate tools and software from publicly available services.[^640]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) had utilized VeraCrypt a legitimate disk encrypting utility that was downloaded directly from the website.[^640]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) used [certutil](https://attack.mitre.org/software/S0160) to download additional files.[^586] [^516] [^376]  [APT41](https://attack.mitre.org/groups/G0096) downloaded post-exploitation tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) via command shell following initial access.[^527]  [APT41](https://attack.mitre.org/groups/G0096) has uploaded Procdump   and NATBypass to a staging directory and has used these tools in follow-on activities.[^169]  |
| [[INC Ransom\|G1032]] | INC Ransom | [INC Ransom](https://attack.mitre.org/groups/G1032) has downloaded tools to compromised servers including Advanced IP Scanner. [^15] [^632]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has downloaded additional tools and malware to compromised systems.[^475] [^565]  |
| [[PLATINUM\|G0068]] | PLATINUM | [PLATINUM](https://attack.mitre.org/groups/G0068) has transferred files using the Intel® Active Management Technology (AMT) Serial-over-LAN (SOL) channel.[^49]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) dropped additional tools to victims during their operation, including portqry.exe, a renamed cmd.exe file, winrar, and [HTRAN](https://attack.mitre.org/software/S0040).[^485] [^425]  |
| [[Winnti Group\|G0044]] | Winnti Group | [Winnti Group](https://attack.mitre.org/groups/G0044) has downloaded an auxiliary program named ff.exe to infected machines.[^507]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used remote code execution to download subsequent payloads.[^658] [^225]  |
| [[Rocke\|G0106]] | Rocke | [Rocke](https://attack.mitre.org/groups/G0106) used malware to download additional malicious files to the target system.[^744] 	 |
| [[Scattered Spider\|G1015]] | Scattered Spider | [Scattered Spider](https://attack.mitre.org/groups/G1015) has downloaded the Teleport remote access tool to compromised VMware vCenter Servers.[^681]  |
| [[Gorgon Group\|G0078]] | Gorgon Group | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can download additional files from C2 servers.[^572]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used LNK files to download remote files to the victim's network.[^505] [^51]  |
| [[Windshift\|G0112]] | Windshift | [Windshift](https://attack.mitre.org/groups/G0112) has used tools to deploy additional payloads to compromised hosts.[^91]  |
| [[Confucius\|G0142]] | Confucius | [Confucius](https://attack.mitre.org/groups/G0142) has downloaded additional files and payloads onto a compromised host following initial access.[^365] [^819]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) has transferred tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) to victim environments from file sharing and hosting websites.[^433]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has downloaded additional malware and tools, including through the use of `certutil`, onto a compromised host .[^761] [^709]  |
| [[Tonto Team\|G0131]] | Tonto Team | [Tonto Team](https://attack.mitre.org/groups/G0131) has downloaded malicious DLLs which served as a [ShadowPad](https://attack.mitre.org/software/S0596) loader.[^205]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has downloaded additional malware and tools onto a compromised host.[^656] [^422] [^213] [^70] [^723] [^793]  For example, [Gamaredon Group](https://attack.mitre.org/groups/G0047) uses a backdoor script to retrieve and decode additional payloads once in victim environments.[^298]   |
| [[Rancor\|G0075]] | Rancor | [Rancor](https://attack.mitre.org/groups/G0075) has downloaded additional malware, including by using [certutil](https://attack.mitre.org/software/S0160).[^942]  |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) retrieved a final stage payload from command and control infrastructure during initial installation on victim systems.[^361]  |
| [[TA551\|G0127]] | TA551 | [TA551](https://attack.mitre.org/groups/G0127) has retrieved DLLs and installer binaries for malware execution from C2.[^100]  |
| [[Nomadic Octopus\|G0133]] | Nomadic Octopus | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has used malicious macros to download additional files to the victim's machine.[^675]   |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can copy files to remote machines.[^508]  |
| [[Metador\|G1013]] | Metador | [Metador](https://attack.mitre.org/groups/G1013) has downloaded tools and malware onto a compromised system.[^40]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used tools to download malicious files to compromised hosts.[^788]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) executed PowerShell scripts to create scheduled tasks to retrieve remotely-hosted payloads.[^683]  |
| [[SideCopy\|G1008]] | SideCopy | [SideCopy](https://attack.mitre.org/groups/G1008) has delivered trojanized executables via spearphishing emails that contacts actor-controlled servers to download malicious payloads.[^437]  |
| [[APT33\|G0064]] | APT33 | [APT33](https://attack.mitre.org/groups/G0064) has downloaded additional files and programs from its C2 server.[^243] [^921] 	<br> |
| [[Volatile Cedar\|G0123]] | Volatile Cedar | [Volatile Cedar](https://attack.mitre.org/groups/G0123) can deploy additional tools.[^290]  |
| [[Evilnum\|G0120]] | Evilnum | [Evilnum](https://attack.mitre.org/groups/G0120) can deploy additional components or tools as needed.[^903]  |
| [[Whitefly\|G0107]] | Whitefly | [Whitefly](https://attack.mitre.org/groups/G0107) has the ability to download additional tools from the C2.[^279]  |
| [[APT18\|G0026]] | APT18 | [APT18](https://attack.mitre.org/groups/G0026) can upload a file to the victim’s machine.[^500]  |
| [[LazyScripter\|G0140]] | LazyScripter | [LazyScripter](https://attack.mitre.org/groups/G0140) had downloaded additional tools to a compromised host.[^140]  |
| [[IndigoZebra\|G0136]] | IndigoZebra | [IndigoZebra](https://attack.mitre.org/groups/G0136) has downloaded additional files and tools from its C2 server.[^476]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Network Intrusion Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools.[^274]  |
| [[Filter Network Traffic\|M1037]] | Filter Network Traffic | Use network filtering to block outbound traffic from compromised systems to unapproved external destinations. Restricting access to known, trusted IP addresses and protocols can prevent attackers from downloading malicious tools or payloads onto compromised servers after gaining initial access. |





## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


[^9]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^10]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^11]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^12]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^13]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^14]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^15]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^16]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^17]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^18]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^19]: [Symantec Backdoor.Nidiran](https://www.symantec.com/security_response/writeup.jsp?docid=2015-120123-5521-99)


[^20]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^21]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^22]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^23]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^24]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^25]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^26]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^27]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^28]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^29]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)


[^30]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^31]: [Securelist Dropping Elephant](https://securelist.com/the-dropping-elephant-actor/75328/)


[^32]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^33]: [Gemini_FIN7_Jan2022](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)


[^34]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^35]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^36]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^37]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^38]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^39]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^40]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^41]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^42]: [PWC Yellow Liderc 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)


[^43]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^44]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^45]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^46]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^47]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^48]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^49]: [Microsoft PLATINUM June 2017](https://cloudblogs.microsoft.com/microsoftsecure/2017/06/07/platinum-continues-to-evolve-find-ways-to-maintain-invisibility/?source=mmpc)


[^50]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)


[^51]: [Cyble Sidewinder September 2020](https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/)


[^52]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^53]: [RedCanary June Insights 2024](https://redcanary.com/blog/threat-intelligence/intelligence-insights-june-2024/)


[^54]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^55]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^56]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^57]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^58]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)


[^59]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^60]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


[^61]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)


[^62]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^63]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)


[^64]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


[^65]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)


[^66]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^67]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^68]: [Check Point Rocket Kitten](https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf)


[^69]: [Forcepoint BITTER Pakistan Oct 2016](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)


[^70]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^71]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^72]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^73]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^74]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^75]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^76]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


[^77]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^78]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)


[^79]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)


[^80]: [Pincus Emotet 2020](https://medium.com/picus-security/an-analysis-of-emotet-malware-powershell-unobfuscation-4f46b50dcf2b)


[^81]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^82]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^83]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)


[^84]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^85]: [IBM IcedID November 2017](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)


[^86]: [T1105: Trellix_search-ms](https://www.trellix.com/blogs/research/beyond-file-search-a-novel-method/)


[^87]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^88]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^89]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^90]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^91]: [BlackBerry Bahamut](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)


[^92]: [Rapid7 Fake W2 July 2024](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)


[^93]: [Lab52 WIRTE Apr 2019](https://lab52.io/blog/wirte-group-attacking-the-middle-east/)


[^94]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^95]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^96]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^97]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)


[^98]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)


[^99]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)


[^100]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^101]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^102]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^103]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^104]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^105]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^106]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^107]: [t1105_lolbas](https://lolbas-project.github.io/#t1105)


[^108]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^109]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^110]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^111]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^112]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^113]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^114]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^115]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^116]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^117]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^118]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^119]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^120]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^121]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^122]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^123]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^124]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^125]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)


[^126]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^127]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)


[^128]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^129]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^130]: [Trend Micro Earth Simnavaz October 2024](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)


[^131]: [Symantec Security Center Trojan.Kwampirs](https://www.symantec.com/security-center/writeup/2016-081923-2700-99)


[^132]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)


[^133]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^134]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^135]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)


[^136]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^137]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^138]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^139]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^140]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^141]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)


[^142]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^143]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^144]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)


[^145]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^146]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^147]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^148]: [Dropbox Malware Sync](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)


[^149]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^150]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)


[^151]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^152]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)


[^153]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^154]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^155]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^156]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^157]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^158]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^159]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^160]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^161]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^162]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


[^163]: [Lab52 MUSTANG PANDA PUBLOAD MAY 2023](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)


[^164]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^165]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^166]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^167]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)


[^168]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)


[^169]: [apt41_dcsocytec_dec2022](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)


[^170]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^171]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^172]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)


[^173]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^174]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^175]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^176]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^177]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)


[^178]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)


[^179]: [Symantec Dyre June 2015](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)


[^180]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^181]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)


[^182]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^183]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^184]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^185]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^186]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^187]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^188]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)


[^189]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^190]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^191]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^192]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^193]: [Symantec Briba May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)


[^194]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)


[^195]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^196]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^197]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^198]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^199]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^200]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^201]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^202]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^203]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^204]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^205]: [ESET Exchange Mar 2021](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/)


[^206]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^207]: [NaumaanProofpoint_GlobalClickFix_April2025](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)


[^208]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^209]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^210]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^211]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^212]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^213]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^214]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^215]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^216]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^217]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^218]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^219]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^220]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^221]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)


[^222]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)


[^223]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^224]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^225]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^226]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^227]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^228]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^229]: [Symantec Calisto July 2018](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)


[^230]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^231]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^232]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^233]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^234]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^235]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)


[^236]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^237]: [Group IB Silence Sept 2018](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)


[^238]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^239]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^240]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^241]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^242]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^243]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^244]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^245]: [Volexity OceanLotus Nov 2017](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)


[^246]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^247]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^248]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^249]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^250]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^251]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^252]: [PTSecurity Cobalt Dec 2016](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)


[^253]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


[^254]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^255]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^256]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^257]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^258]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^259]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^260]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^261]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^262]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)


[^263]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^264]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^265]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^266]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^267]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^268]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^269]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^270]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^271]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^272]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^273]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^274]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^275]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^276]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^277]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^278]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^279]: [Symantec Whitefly March 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)


[^280]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^281]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)


[^282]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^283]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^284]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^285]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^286]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^287]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^288]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^289]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


[^290]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^291]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^292]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^293]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^294]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^295]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^296]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^297]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^298]: [unit42_gamaredon_dec2022](https://unit42.paloaltonetworks.com/trident-ursa/)


[^299]: [Fidelis INOCNATION](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)


[^300]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^301]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^302]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)


[^303]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^304]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^305]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^306]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^307]: [Veriti RedLine Stealer MAAS April 2023](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)


[^308]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)


[^309]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^310]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^311]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^312]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^313]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^314]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^315]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^316]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)


[^317]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^318]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^319]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^320]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^321]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^322]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)


[^323]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)


[^324]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)


[^325]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^326]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^327]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^328]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^329]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^330]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^331]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^332]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^333]: [Cybereason TA505 April 2019](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)


[^334]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^335]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^336]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^337]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)


[^338]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^339]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^340]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^341]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^342]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^343]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^344]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)


[^345]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


[^346]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^347]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^348]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^349]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^350]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


[^351]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^352]: [Donut Github](https://github.com/TheWover/donut)


[^353]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^354]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^355]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^356]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^357]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^358]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^359]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^360]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^361]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^362]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)


[^363]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)


[^364]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


[^365]: [Uptycs Confucius APT Jan 2021](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)


[^366]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^367]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^368]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)


[^369]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^370]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^371]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^372]: [JPCERT ChChes Feb 2017](https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html)


[^373]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^374]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^375]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^376]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^377]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)


[^378]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^379]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^380]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^381]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^382]: [Intezer TeamTNT September 2020](https://www.intezer.com/blog/cloud-security/attackers-abusing-legitimate-cloud-monitoring-tools-to-conduct-cyber-attacks/)


[^383]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)


[^384]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^385]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^386]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^387]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)


[^388]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^389]: [Trend Micro Totbrick Oct 2016](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)


[^390]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^391]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^392]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^393]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^394]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^395]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^396]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^397]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^398]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^399]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^400]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^401]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^402]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^403]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)


[^404]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^405]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^406]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^407]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^408]: [Symantec Ristol May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3909-99)


[^409]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^410]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^411]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^412]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^413]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^414]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^415]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^416]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)


[^417]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^418]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^419]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^420]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^421]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^422]: [TrendMicro Gamaredon April 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)


[^423]: [Unit42 BabyShark Apr 2019](https://unit42.paloaltonetworks.com/babyshark-malware-part-two-attacks-continue-using-kimjongrat-and-pcrat/)


[^424]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^425]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^426]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


[^427]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)


[^428]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^429]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^430]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^431]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^432]: [LOLBAS Esentutl](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)


[^433]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^434]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^435]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^436]: [Socket Shai-Hulud Trufflehog September 2025](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)


[^437]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^438]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^439]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)


[^440]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)


[^441]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^442]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^443]: [Trend Micro Qakbot December 2020](https://success.trendmicro.com/en-US/solution/KA-0011282)


[^444]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^445]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^446]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^447]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^448]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^449]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^450]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^451]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^452]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^453]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^454]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^455]: [TechNet Copy](https://technet.microsoft.com/en-us/library/bb490886.aspx)


[^456]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^457]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^458]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^459]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^460]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)


[^461]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^462]: [Symantec WastedLocker June 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)


[^463]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^464]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^465]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^466]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^467]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^468]: [Symantec Backdoor.Mivast](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)


[^469]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^470]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^471]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)


[^472]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^473]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^474]: [Koi Glassworm Extensions November 2025](https://www.koi.ai/blog/glassworm-returns-new-wave-openvsx-malware-expose-attacker-infrastructure)


[^475]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^476]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^477]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^478]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^479]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^480]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^481]: [District Court of NY APT10 Indictment December 2018](https://www.justice.gov/opa/page/file/1122671/download)


[^482]: [Aquino RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/rarstone-found-in-targeted-attacks/)


[^483]: [Google TAG Lazarus Jan 2021](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/)


[^484]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^485]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^486]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)


[^487]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^488]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)


[^489]: [objectivesee osx.shlayer apple approved 2020](https://objective-see.com/blog/blog_0x4E.html)


[^490]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^491]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^492]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^493]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^494]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)


[^495]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^496]: [Microsoft HAFNIUM March 2020](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)


[^497]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^498]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^499]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^500]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^501]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^502]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)


[^503]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^504]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^505]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^506]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^507]: [Kaspersky Winnti April 2013](https://securelist.com/winnti-more-than-just-a-game/37029/)


[^508]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^509]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)


[^510]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^511]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)


[^512]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)


[^513]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^514]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^515]: [ESET Turla Mosquito May 2018](https://www.welivesecurity.com/2018/05/22/turla-mosquito-shift-towards-generic-tools/)


[^516]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^517]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)


[^518]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^519]: [ProofPoint SettingContent-ms July 2018](https://www.proofpoint.com/us/threat-insight/post/ta505-abusing-settingcontent-ms-within-pdf-files-distribute-flawedammyy-rat)


[^520]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^521]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)


[^522]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)


[^523]: [AhnLab Andariel Subgroup of Lazarus June 2018](https://web.archive.org/web/20230213154832/http://download.ahnlab.com/global/brochure/%5BAnalysis%5DAndariel_Group.pdf)


[^524]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^525]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^526]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)


[^527]: [Rostovcev APT41 2021](https://www.group-ib.com/blog/apt41-world-tour-2021/)


[^528]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^529]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)


[^530]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^531]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^532]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^533]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^534]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^535]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^536]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^537]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^538]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^539]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^540]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^541]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^542]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)


[^543]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^544]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^545]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^546]: [Symantec Frutas Feb 2013](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)


[^547]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^548]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^549]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^550]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^551]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^552]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^553]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)


[^554]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^555]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^556]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^557]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^558]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^559]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^560]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^561]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)


[^562]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^563]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^564]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^565]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^566]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^567]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


[^568]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^569]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^570]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^571]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^572]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^573]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^574]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^575]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)


[^576]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^577]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^578]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^579]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^580]: [Microsoft DUBNIUM June 2016](https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/)


[^581]: [sentinelone operationDigitalEye Dec 2024](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)


[^582]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^583]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^584]: [DOJ FIN7 Aug 2018](https://www.justice.gov/opa/press-release/file/1084361/download)


[^585]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^586]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^587]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^588]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^589]: [FireEye POSHSPY April 2017](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)


[^590]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)


[^591]: [Microsoft WhisperGate January 2022](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)


[^592]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^593]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^594]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^595]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)


[^596]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^597]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^598]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^599]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^600]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^601]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)


[^602]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^603]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^604]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^605]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^606]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^607]: [Unit42 Chinese VSCode 06 September 2024](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)


[^608]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^609]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^610]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^611]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)


[^612]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^613]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^614]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^615]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^616]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^617]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^618]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^619]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^620]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^621]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^622]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^623]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^624]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)


[^625]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^626]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^627]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)


[^628]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^629]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^630]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)


[^631]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^632]: [Huntress INC Ransomware May 2024](https://www.huntress.com/blog/lolbin-to-inc-ransomware)


[^633]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)


[^634]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^635]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^636]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^637]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)


[^638]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^639]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^640]: [Check Point VOID MANTICORE Handala Hack March 2026](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)


[^641]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^642]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^643]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^644]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^645]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^646]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)


[^647]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^648]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^649]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^650]: [Unit 42 SeaDuke 2015](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)


[^651]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^652]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^653]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^654]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^655]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^656]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^657]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


[^658]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^659]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)


[^660]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^661]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^662]: [Google Cloud Threat Intelligence COSCMICENERGY 2023](https://cloud.google.com/blog/topics/threat-intelligence/cosmicenergy-ot-malware-russian-response/)


[^663]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^664]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^665]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^666]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^667]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)


[^668]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^669]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^670]: [TrendMicro Pawn Storm Dec 2020](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)


[^671]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^672]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^673]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^674]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^675]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^676]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^677]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^678]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)


[^679]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^680]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)


[^681]: [Mandiant VMware vSphere JUL 2025](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)


[^682]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)


[^683]: [DomainTools WinterVivern 2021](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/)


[^684]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^685]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^686]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^687]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^688]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^689]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^690]: [Morphisec Cobalt Gang Oct 2018](https://blog.morphisec.com/cobalt-gang-2.0)


[^691]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^692]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)


[^693]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^694]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^695]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)


[^696]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^697]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^698]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)


[^699]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^700]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^701]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^702]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^703]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^704]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^705]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


[^706]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


[^707]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)


[^708]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^709]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^710]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^711]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^712]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)


[^713]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^714]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^715]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)


[^716]: [Palo Alto OilRig Sep 2018](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)


[^717]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^718]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^719]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^720]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^721]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^722]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^723]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^724]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^725]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


[^726]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^727]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


[^728]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^729]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^730]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^731]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)


[^732]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^733]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^734]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^735]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


[^736]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^737]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^738]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^739]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^740]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^741]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^742]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^743]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^744]: [Talos Rocke August 2018](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)


[^745]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)


[^746]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^747]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^748]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^749]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)


[^750]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^751]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^752]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^753]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^754]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


[^755]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^756]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)


[^757]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)


[^758]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^759]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^760]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^761]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^762]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^763]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^764]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^765]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^766]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^767]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)


[^768]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^769]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^770]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^771]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)


[^772]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^773]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^774]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)


[^775]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^776]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^777]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^778]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^779]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^780]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^781]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^782]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^783]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^784]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)


[^785]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)


[^786]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^787]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)


[^788]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^789]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^790]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^791]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^792]: [TrendMicro PE_URSNIF.A2](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279)


[^793]: [VenereCiscoTalos_Gamaredon_Mar2025](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)


[^794]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^795]: [Symantec Chafer February 2018](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)


[^796]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^797]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)


[^798]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^799]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^800]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)


[^801]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^802]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^803]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^804]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^805]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^806]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^807]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^808]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)


[^809]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^810]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^811]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^812]: [Github Koadic](https://github.com/offsecginger/koadic)


[^813]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^814]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^815]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^816]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)


[^817]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^818]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


[^819]: [TrendMicro Confucius APT Aug 2021](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)


[^820]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^821]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^822]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^823]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^824]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^825]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^826]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^827]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^828]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^829]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^830]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^831]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)


[^832]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^833]: [Reaqta MuddyWater November 2017](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)


[^834]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^835]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


[^836]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)


[^837]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^838]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^839]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)


[^840]: [Securelist MiniDuke Feb 2013](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)


[^841]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^842]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^843]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^844]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^845]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^846]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)


[^847]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^848]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^849]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^850]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^851]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)


[^852]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^853]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)


[^854]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^855]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^856]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^857]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^858]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^859]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^860]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)


[^861]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^862]: [Symantec Vasport May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-5938-99)


[^863]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^864]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^865]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^866]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^867]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^868]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^869]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)


[^870]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^871]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^872]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^873]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


[^874]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)


[^875]: [Symantec Pasam May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)


[^876]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^877]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^878]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^879]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^880]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^881]: [Linux FTP](https://linux.die.net/man/1/ftp)


[^882]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^883]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^884]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^885]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^886]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^887]: [ESET Twitter Ida Pro Nov 2021](https://x.com/ESETresearch/status/1458438155149922312)


[^888]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^889]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)


[^890]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)


[^891]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^892]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


[^893]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^894]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^895]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^896]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)


[^897]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^898]: [Malwarebytes SmokeLoader 2016](https://blog.malwarebytes.com/threat-analysis/2016/08/smoke-loader-downloader-with-a-smokescreen-still-alive/)


[^899]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^900]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^901]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^902]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^903]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^904]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^905]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^906]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)


[^907]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^908]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^909]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^910]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^911]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^912]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^913]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^914]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^915]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^916]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^917]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^918]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^919]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^920]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^921]: [Microsoft Holmium June 2020](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)


[^922]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^923]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)


[^924]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^925]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^926]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)


[^927]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^928]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)


[^929]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^930]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)


[^931]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^932]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^933]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^934]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^935]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^936]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^937]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)


[^938]: [Securelist ShadowPad Aug 2017](https://securelist.com/shadowpad-in-corporate-networks/81432/)


[^939]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)


[^940]: [DOJ FBI Handala Hack March 2026](https://www.justice.gov/opa/media/1431956/dl?inline)


[^941]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^942]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^943]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^944]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^945]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


