---
aliases: 
    - T1059.003
mitre-attack: https://attack.mitre.org/techniques/T1059/003
tactic: 
     - Execution
platforms:
     - Windows
permissions required:
     - none
---

## T1059.003

Adversaries may abuse the Windows command shell for execution. The Windows command shell ([cmd](https://attack.mitre.org/software/S0106)) is the primary command prompt on Windows systems. The Windows command prompt can be used to control almost any aspect of a system, with various permission levels required for different subsets of commands. The command prompt can be invoked remotely via [Remote Services](https://attack.mitre.org/techniques/T1021) such as [SSH](https://attack.mitre.org/techniques/T1021/004).[^566] <br><br>Batch files (ex: .bat or .cmd) also provide the shell with a list of sequential commands to run, as well as normal scripting operations such as conditionals and loops. Common uses of batch files include long or repetitive tasks, or the need to run the same set of commands on multiple systems.<br><br>Adversaries may leverage [cmd](https://attack.mitre.org/software/S0106) to execute various commands and payloads. Common uses include [cmd](https://attack.mitre.org/software/S0106) to execute a single command, or abusing [cmd](https://attack.mitre.org/software/S0106) interactively with input and output forwarded over a command and control channel.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Covenant\|S1155]] | Covenant | [Covenant](https://attack.mitre.org/software/S1155) provides access to a Command Shell in Windows environments for follow-on command execution and tasking.[^623]  |
| [[Diskpart\|S9002]] | Diskpart | [Diskpart](https://attack.mitre.org/software/S9002) can execute a disk partition script file, which attempts to mount a virtual hard disk.[^438]  [Diskpart](https://attack.mitre.org/software/S9002) can also assign and mount virtual disks.[^438]     |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `cmd.exe` to enable lateral movement using DCOM.[^309]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) has modules for executing scripts.[^244]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can execute `cmd` commands on a compromised host.[^296]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) can be deployed via batch script.[^291]  |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use cmd.exe for execution.[^557]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can launch a remote command line to execute commands on the victim’s machine.[^101] [^607]  |
| [[Out1\|S0594]] | Out1 | [Out1](https://attack.mitre.org/software/S0594) can use native command line for execution.[^555]  |
| [[MCMD\|S0500]] | MCMD | [MCMD](https://attack.mitre.org/software/S0500) can launch a console process (cmd.exe) with redirected standard input and output.[^532]  |
| [[cmd\|S0106]] | cmd | [cmd](https://attack.mitre.org/software/S0106) is used to execute programs and other actions at the command-line interface.[^198]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can open an interactive command-shell to perform command line functions on victim machines. [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (Jscript) and to run arbitrary shellcode.[^655] [^104]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) can launch a remote shell to execute commands on the victim’s machine.[^701] [^46]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) has used macros in Excel documents to download and deploy the malware on the user’s machine.[^711]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) runs `cmd.exe /c` and sends the output to its C2.[^130]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has executed commands via cmd.exe.[^459]  |
| [[Pikabot\|S1145]] | Pikabot | [Pikabot](https://attack.mitre.org/software/S1145) can execute Windows shell commands via `cmd.exe`.[^297]  |
| [[Wiarp\|S0206]] | Wiarp | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can open a command line interface.[^501]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can use `cmd.exe` for execution on compromised hosts.[^575]  |
| [[Spark\|S0543]] | Spark | [Spark](https://attack.mitre.org/software/S0543) can use cmd.exe to run commands.[^331]   |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can use `cmd.exe` to drop and run files.[^363] [^10]  |
| [[MURKYTOP\|S0233]] | MURKYTOP | [MURKYTOP](https://attack.mitre.org/software/S0233) uses the command-line interface.[^518]  |
| [[Exaramel for Windows\|S0343]] | Exaramel for Windows | [Exaramel for Windows](https://attack.mitre.org/software/S0343) has a command to launch a remote shell and executes commands on the victim’s machine.[^48]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) executes a binary on the system and logs the results into a temp file by using: `cmd.exe /c "<file_path> > %temp%\PM* .tmp 2>&1"`.[^260]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can execute shell commands.[^687]  [Orz](https://attack.mitre.org/software/S0229) can execute commands with JavaScript.[^687]  |
| [[IronWind\|S9029]] | IronWind | [IronWind](https://attack.mitre.org/software/S9029) has used the Windows command shell to execute malicious files.[^144]  |
| [[SEASHARPEE\|S0185]] | SEASHARPEE | [SEASHARPEE](https://attack.mitre.org/software/S0185) can execute commands on victims.[^486]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) can execute commands from its C2 server.[^283]  |
| [[RobbinHood\|S0400]] | RobbinHood | [RobbinHood](https://attack.mitre.org/software/S0400) uses cmd.exe on the victim's computer.[^645]  |
| [[TDTESS\|S0164]] | TDTESS | [TDTESS](https://attack.mitre.org/software/S0164) provides a reverse shell on the victim.[^523]  |
| [[SharpStage\|S0546]] | SharpStage | [SharpStage](https://attack.mitre.org/software/S0546) can execute arbitrary commands with the command line.[^352] [^533]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to run `cmd.exe` or other interactive processes on a compromised computer.[^403]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) is capable of providing shell functionality to the attacker to execute commands.[^681]  |
| [[adbupd\|S0202]] | adbupd | [adbupd](https://attack.mitre.org/software/S0202) can run a copy of cmd.exe.[^735]  |
| [[Emissary\|S0082]] | Emissary | [Emissary](https://attack.mitre.org/software/S0082) has the capability to create a remote shell and execute specified commands.[^53]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) can execute shell commands using cmd.exe.[^315]  |
| [[HAWKBALL\|S0391]] | HAWKBALL | [HAWKBALL](https://attack.mitre.org/software/S0391) has created a cmd.exe reverse shell, executed commands, and uploaded output via the command line.[^578]  |
| [[TAMECAT\|S1193]] | TAMECAT | [TAMECAT](https://attack.mitre.org/software/S1193) has used `cmd.exe` to run the `curl` command.[^451]   |
| [[HeartCrypt\|S9018]] | HeartCrypt | [HeartCrypt](https://attack.mitre.org/software/S9018) can use the `reg add` command via `cmd.exe` for Registry modification.[^395]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) can use `cmd.exe` to execute multiple commands on infected hosts.[^388]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) has the ability to execute shell commands.[^681]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) can receive and execute commands with cmd.exe. It can also provide a reverse shell.[^425] [^292]  |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) uses command line for execution.[^200]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) can launch an interface where it can execute several commands on the victim’s PC.[^80]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can execute commands via `cmd.exe`.[^582] [^51]  |
| [[CARROTBAT\|S0462]] | CARROTBAT | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to execute command line arguments on a compromised host.[^715]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) executes commands remotely on the infected host.[^64]  |
| [[WEBC2\|S0109]] | WEBC2 | [WEBC2](https://attack.mitre.org/software/S0109) can open an interactive command shell.[^121]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) uses the command-line interface to execute arbitrary commands.[^725] [^117]  |
| [[SharpDisco\|S1089]] | SharpDisco | [SharpDisco](https://attack.mitre.org/software/S1089) can use `cmd.exe` to execute plugins and to send command output to  specified SMB shares.[^743]  |
| [[xCaon\|S0653]] | xCaon | [xCaon](https://attack.mitre.org/software/S0653) has a command to start an interactive shell.[^373]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) uses cmd.exe to execute commands on the victim’s machine.[^757]  |
| [[Pony\|S0453]] | Pony | [Pony](https://attack.mitre.org/software/S0453) has used batch scripts to delete itself after execution.[^658] 	 |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can use CMD to execute a process.[^482]  |
| [[AuditCred\|S0347]] | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) can open a reverse shell on the system to execute commands.[^745]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has created a reverse shell using `cmd.exe`.[^250] [^367]  |
| [[Kasidet\|S0088]] | Kasidet | [Kasidet](https://attack.mitre.org/software/S0088) can execute commands using cmd.exe.[^32]  |
| [[Hannotog\|S1211]] | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) can execute various `cmd.exe /c %s` commands.[^59]  |
| [[OceanSalt\|S0346]] | OceanSalt | [OceanSalt](https://attack.mitre.org/software/S0346) can create a reverse shell on the infected endpoint using cmd.exe.[^181]  [OceanSalt](https://attack.mitre.org/software/S0346) has been executed via malicious macros.[^181]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has used `cmd.exe` to execute command on an infected host.[^36] [^586]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can use the Windows Command Shell for execution.[^482]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can issue commands using cmd.exe.[^247] [^152]  |
| [[TinyTurla\|S0668]] | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) has been installed using a .bat file.[^732]  |
| [[PyDCrypt\|S1032]] | PyDCrypt | [PyDCrypt](https://attack.mitre.org/software/S1032) has used `cmd.exe` for execution.[^427]  |
| [[EnvyScout\|S0634]] | EnvyScout | [EnvyScout](https://attack.mitre.org/software/S0634) can use cmd.exe to execute malicious files on compromised hosts.[^497]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) uses cmd.exe to execute itself in-memory.[^284]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has used cmd.exe to run a PowerShell script. [^541]  |
| [[SNUGRIDE\|S0159]] | SNUGRIDE | [SNUGRIDE](https://attack.mitre.org/software/S0159) is capable of executing commands and spawning a reverse shell.[^292]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) has the ability to execute commands with the COMSPEC environment variable.[^223]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can execute commands via `cmd.exe`.[^642]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can create a remote shell and execute commands using [cmd](https://attack.mitre.org/software/S0106).[^604]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) can use `cmd.exe` to execute commands on a compromised host.[^508] [^432]   |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) can use `cmd.exe` to execute commands on an infected host.[^340]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has used several commands executed in sequence via `cmd`. [^579]  |
| [[SystemBC\|S9001]] | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) has used `cmd.exe` to execute VBS scripts, BAT scripts and CMD scripts.[^14]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can use `cmd.exe` to run various commands as a reverse shell.[^408]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can execute command line scripts received from C2.[^356]  |
| [[DropBook\|S0547]] | DropBook | [DropBook](https://attack.mitre.org/software/S0547) can execute arbitrary shell commands on the victims' machines.[^352] [^533]   |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can execute commands using `cmd.exe`.[^196]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can execute shell commands using `cmd.exe`.[^479]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has used `cmd.exe` for execution.[^672]  |
| [[Umbreon\|S0221]] | Umbreon | [Umbreon](https://attack.mitre.org/software/S0221) provides access using both standard facilities like SSH and additional access using its backdoor Espeon, providing a reverse shell upon receipt of a special packet[^717]  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer |  [AuTo Stealer](https://attack.mitre.org/software/S1029) can use `cmd.exe` to execute a created batch file.[^340]  |
| [[ODAgent\|S1170]] | ODAgent | [ODAgent](https://attack.mitre.org/software/S1170) can execute a specified command line passed via API.[^355]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used `cmd` to execute commands on a compromised host.[^210]  |
| [[SUGARUSH\|S1049]] | SUGARUSH | [SUGARUSH](https://attack.mitre.org/software/S1049) has used `cmd` for execution on an infected host.[^11]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) can launch cmd.exe to execute commands on the system.[^603] 	 |
| [[WastedLocker\|S0612]] | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) has used [cmd](https://attack.mitre.org/software/S0106) to execute commands on the system.[^713]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can launch a remote shell to execute commands.[^280] [^77]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can execute commands on the victim's machine.[^753] [^290]  |
| [[WhisperGate\|S0689]] | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) can use `cmd.exe` to execute commands.[^721]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) has executed commands using `cmd.exe /c`.[^622] 	 |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439)'s backdoor has used cmd.exe to execute arbitrary commands as well as batch scripts to update itself to a newer version.[^565]  |
| [[SamSam\|S0370]] | SamSam | [SamSam](https://attack.mitre.org/software/S0370) uses custom batch scripts to execute some of its components.[^755]  |
| [[Conti\|S0575]] | Conti | [Conti](https://attack.mitre.org/software/S0575) can utilize command line options to allow an attacker control over how it scans and encrypts files.[^678] [^358]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses cmd.exe to read and execute a file stored on an infected USB device as part of initial installation.[^590]  |
| [[Megazord\|S1191]] | Megazord | <br>[Megazord](https://attack.mitre.org/software/S1191) can execute multiple commands post infection via `cmd.exe`.[^550]  |
| [[TEXTMATE\|S0146]] | TEXTMATE | [TEXTMATE](https://attack.mitre.org/software/S0146) executes cmd.exe to provide a reverse shell to adversaries.[^469] [^282]  |
| [[Siloscape\|S0623]] | Siloscape | [Siloscape](https://attack.mitre.org/software/S0623) can run cmd through an IRC channel.[^454]  |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) can execute commands on a compromised network with the use of `cmd.exe`.[^57]  |
| [[UBoatRAT\|S0333]] | UBoatRAT | [UBoatRAT](https://attack.mitre.org/software/S0333) can start a command shell.[^731]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) creates a cmd.exe shell to send and receive commands from the command and control server via open pipes.[^8]  |
| [[HTTPTroy\|S9007]] | HTTPTroy | [HTTPTroy](https://attack.mitre.org/software/S9007) has the ability to generate a reverse shell using the command `conn <IP_ADDRESS> <PORT>`.[^194]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can utilize cmd.exe to execute commands in a victim's environment.[^83]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) uses cmd.exe to execute commands on the victim’s machine.[^588]  |
| [[NavRAT\|S0247]] | NavRAT | [NavRAT](https://attack.mitre.org/software/S0247) leverages cmd.exe to perform discovery techniques.[^573]  [NavRAT](https://attack.mitre.org/software/S0247) loads malicious shellcode and executes it in memory.[^573]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) can launch a remote shell to execute commands on the victim’s machine.[^437]  |
| [[NETEAGLE\|S0034]] | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) allows adversaries to execute shell commands on the infected host.[^412]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used cmd.exe and batch scripts to execute commands.[^424]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can issue shell commands to download and execute additional payloads.[^335]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can launch command-line shells.[^416]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) has executed commands using `cmd.exe /c “<command> > <%temp%>\AM<random>. tmp” 2>&1`.[^224]   |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) can be issued a command shell function from the C2.[^453]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) can use `cmd.exe` to execute commands received from C2.[^131]  |
| [[Hi-Zor\|S0087]] | Hi-Zor | [Hi-Zor](https://attack.mitre.org/software/S0087) has the ability to create a reverse shell.[^238]  |
| [[China Chopper\|S0020]] | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020)'s server component is capable of opening a command terminal.[^175] [^690] [^294]  |
| [[CALENDAR\|S0025]] | CALENDAR | [CALENDAR](https://attack.mitre.org/software/S0025) has a command to run cmd.exe to execute commands.[^730]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) can spawn a command shell, and execute native commands.[^406] [^176]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) can launch interactive shells for communicating with the victim machine.[^228] [^261]  |
| [[Anchor\|S0504]] | Anchor | [Anchor](https://attack.mitre.org/software/S0504) has used cmd.exe to run its self deletion routine.[^422]  |
| [[Pteranodon\|S0147]] | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) can use `cmd.exe` for execution on victim systems.[^531] [^470]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) can use `cmd.exe` to add registry keys for persistence.[^49]  |
| [[RunningRAT\|S0253]] | RunningRAT | [RunningRAT](https://attack.mitre.org/software/S0253) uses a batch file to kill a security program task and then attempts to remove itself.[^431]  |
| [[Babuk\|S0638]] | Babuk | [Babuk](https://attack.mitre.org/software/S0638) has the ability to use the command line to control execution on compromised hosts.[^534] [^692]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) can use `cmd.exe` to execute commands.[^277]  |
| [[BlackMould\|S0564]] | BlackMould | [BlackMould](https://attack.mitre.org/software/S0564) can run cmd.exe with parameters.[^334]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) allows actors to spawn a reverse shell on a victim.[^707] [^384] [^619] [^18] [^584] [^712]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has launched cmd.exe and used the ShellExecuteW() API function to execute commands on the system.[^483] [^258] [^197]  |
| [[MultiLayer Wiper\|S1135]] | MultiLayer Wiper | [MultiLayer Wiper](https://attack.mitre.org/software/S1135) uses a batch script launched via a scheduled task to delete Windows Event Logs.[^235]  |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) has provided the ability to execute shell commands on a compromised host.[^681]  |
| [[SeaDuke\|S0053]] | SeaDuke | [SeaDuke](https://attack.mitre.org/software/S0053) is capable of executing commands.[^525]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) is capable of executing commands via cmd.exe.[^691]  |
| [[Peppy\|S0643]] | Peppy | [Peppy](https://attack.mitre.org/software/S0643) has the ability to execute shell commands.[^158]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) has used `cmd.exe /c` and batch files for execution.[^30]   |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can use cmd.exe for command execution.[^575]  |
| [[Akira\|S1129]] | Akira | [Akira](https://attack.mitre.org/software/S1129) executes from the Windows command line and can take various arguments for execution.[^611]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) uses a malicious Windows Batch script to run the Windows `code` utility to retrieve follow-on script payloads.[^748]  [DarkGate](https://attack.mitre.org/software/S1111) has also used `cmd.exe` to create a remote shell.[^419]   |
| [[Carbanak\|S0030]] | Carbanak | [Carbanak](https://attack.mitre.org/software/S0030) has a command to create a reverse shell.[^111]  |
| [[XTunnel\|S0117]] | XTunnel | [XTunnel](https://attack.mitre.org/software/S0117) has been used to execute remote commands.[^202]  |
| [[HOMEFRY\|S0232]] | HOMEFRY | [HOMEFRY](https://attack.mitre.org/software/S0232) uses a command-line interface.[^518]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can run commands on the compromised asset with CMD functions.[^232]  |
| [[Netwalker\|S0457]] | Netwalker | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used batch scripts to retrieve the [Netwalker](https://attack.mitre.org/software/S0457) payload.[^605]  |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can execute various Windows commands.[^671] 	 |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to execute shell commands on the infected host.[^146]  |
| [[Latrodectus\|S1160]] | Latrodectus | The [Latrodectus](https://attack.mitre.org/software/S1160) command handler can use `cmdexe` to run multiple discovery commands.[^154] [^421]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has used `cmd.exe` and `.bat` scripts for execution.[^663]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) has used [cmd](https://attack.mitre.org/software/S0106) to execute tasks on the system.[^163]   |
| [[CharmPower\|S0674]] | CharmPower | The C# implementation of  the [CharmPower](https://attack.mitre.org/software/S0674) command execution module can use `cmd`.[^265]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has used cmd.exe to launch a reverse shell.[^169]   |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) can uninstall malware components using a batch script.[^583]  [TYPEFRAME](https://attack.mitre.org/software/S0263) can execute commands using a shell.[^583]  |
| [[KOMPROGO\|S0156]] | KOMPROGO | [KOMPROGO](https://attack.mitre.org/software/S0156) is capable of creating a reverse shell.[^96]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) uses cmd.exe to execute scripts and commands on the victim’s machine.[^213]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) can enable Windows CLI access and execute files.[^45]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) has the ability to use the command line for execution on the targeted system.[^218]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has used `cmd.exe /c` to execute files.[^445]   |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has utilized a BAT script to disable security solutions.[^195]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can perform reconnaissance commands on a victim machine via a cmd.exe process.[^666]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) is capable of spawning a Windows command shell.[^149] [^295]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) allows for the execution of arbitrary commands on the victim system.[^379]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has used cmd.exe to execute arbitrary commands on the infected host across different stages of the infection chain.[^495] [^371] [^133]   |
| [[DnsSystem\|S1021]] | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) can use `cmd.exe` for execution.[^598]  |
| [[MoleNet\|S0553]] | MoleNet | [MoleNet](https://attack.mitre.org/software/S0553) can execute commands via the command line utility.[^352]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [JHUHUGIT](https://attack.mitre.org/software/S0044) uses a .bat file to execute a .dll.[^73]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) has the ability to set a Registry key to run a cmd.exe command.[^201]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) is capable of executing commands via [cmd](https://attack.mitre.org/software/S0106).[^204]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) creates a command-line shell using cmd.exe.[^270]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has executed windows [cmd](https://attack.mitre.org/software/S0106) using `ErrorHandler.cmd` to create scheduled tasks.[^310]  |
| [[Black Basta\|S1070]] | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) can use `cmd.exe` to enable shadow copy deletion.[^514]  |
| [[OopsIE\|S0264]] | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) uses the command prompt to execute commands on the victim's machine.[^72] [^397]  |
| [[4H RAT\|S0065]] | 4H RAT | [4H RAT](https://attack.mitre.org/software/S0065) has the capability to create a remote shell.[^98]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) uses Windows Script Components.[^305] [^530]  |
| [[DealersChoice\|S0243]] | DealersChoice | [DealersChoice](https://attack.mitre.org/software/S0243) makes modifications to open-source scripts from GitHub and executes them on the victim’s machine.[^351]  |
| [[SQLRat\|S0390]] | SQLRat | [SQLRat](https://attack.mitre.org/software/S0390) has used SQL to execute JavaScript and VB scripts on the host system.[^43]  |
| [[MegaCortex\|S0576]] | MegaCortex | [MegaCortex](https://attack.mitre.org/software/S0576) has used `.cmd` scripts on the victim's system.[^63]   |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to remotely execute commands.[^415]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) can execute arbitrary commands and utilize the "ComSpec" environment variable.[^373]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to use the command shell to execute commands on a compromised host.[^456]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) executes cmd.exe and uses a pipe to read the results and send back the output to the C2 server.[^480]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) uses the command line and rundll32.exe to execute.[^94]  |
| [[Hikit\|S0009]] | Hikit | [Hikit](https://attack.mitre.org/software/S0009) has the ability to create a remote shell and run given commands.[^494]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) has included BAT files in some instances for installation.[^115] [^273]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) calls cmd.exe to run various DLL files via rundll32 and also to perform file cleanup. [Sakula](https://attack.mitre.org/software/S0074) also has the capability to invoke a reverse shell.[^251]  |
| [[Tarrask\|S1011]] | Tarrask | [Tarrask](https://attack.mitre.org/software/S1011) may abuse the Windows schtasks command-line tool to create "hidden" scheduled tasks.[^476]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) has the ability to use `CMD` to execute commands.[^119] [^524]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can launch cmd.exe to perform reconnaissance commands.[^58] [^563]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) uses cmd.exe to execute commands.[^209] [^55]  |
| [[hcdLoader\|S0071]] | hcdLoader | [hcdLoader](https://attack.mitre.org/software/S0071) provides command-line access to the compromised system.[^128]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) can execute commands via an interactive command shell.[^170]  [MoonWind](https://attack.mitre.org/software/S0149) uses batch scripts for various purposes, including to restart and uninstall itself.[^170]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has used `cmd.exe` to create a Registry entry to establish persistence.[^50]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) can use `cmd.exe /Q/c move CSIDL_SYSTEM_DRIVE\temp\sys.tmp1 CSIDL_WINDOWS\policydefinitions\postgresql.exe 1> \\127.0.0.1\ADMIN$\_1636727589.6007507 2>&1` to deploy on an infected system.[^650]  |
| [[ABK\|S0469]] | ABK | [ABK](https://attack.mitre.org/software/S0469) has the ability to use [cmd](https://attack.mitre.org/software/S0106) to run a Portable Executable (PE) on the compromised host.[^236]  |
| [[ccf32\|S1043]] | ccf32 | [ccf32](https://attack.mitre.org/software/S1043) has used `cmd.exe` for archiving data and deleting files.[^296]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) allows for arbitrary Windows command execution.[^19]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can use the Windows command shell for multiple post-compromise actions on objective.[^693] [^278] [^409]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) uses cmd.exe to execute commands on the system.[^314] [^756]   |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) uses a command-line interface to interact with systems.[^191] [^443] [^22] [^660]  |
| [[SampleCheck5000\|S1168]] | SampleCheck5000 | [SampleCheck5000](https://attack.mitre.org/software/S1168) can call cmd.exe to execute C2 command line strings.[^41] [^355]  |
| [[EvilBunny\|S0396]] | EvilBunny | [EvilBunny](https://attack.mitre.org/software/S0396) has an integrated scripting engine to download and execute Lua scripts.[^404]  |
| [[Cobian RAT\|S0338]] | Cobian RAT | [Cobian RAT](https://attack.mitre.org/software/S0338) can launch a remote command shell interface for executing commands.[^473]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) can remotely open applications on the infected host with the `ShellExecuteA` command.[^125]  |
| [[ServHelper\|S0382]] | ServHelper | [ServHelper](https://attack.mitre.org/software/S0382) can execute shell commands against [cmd](https://attack.mitre.org/software/S0106).[^140] [^105]  |
| [[JCry\|S0389]] | JCry | [JCry](https://attack.mitre.org/software/S0389) has used `cmd.exe` to launch PowerShell.[^718] 	 |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can use the Windows command line to delete volume shadow copies and disable recovery.[^487] [^554] [^343] [^69]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) can use a remote command module for execution via the Windows command line.[^303]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can use `cmd.exe` for discovery actions on a targeted system.[^119]  |
| [[OilBooster\|S1172]] | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) has the ability to execute shell commands and exfiltrate the results.[^355]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) can copy cmd.exe into the system temp folder.[^723]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a backdoor through which remote attackers can open a command-line interface.[^229]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) uses cmd.exe to create a reverse shell on the infected endpoint.[^730]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) can open a remote command-line interface and execute commands.[^369]  [NanoCore](https://attack.mitre.org/software/S0336) uses JavaScript files.[^629]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has the ability to execute shell commands on the compromised host.[^322]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) can run arbitrary commands passed to it through `cmd.exe`.[^342]  |
| [[Daserf\|S0187]] | Daserf | [Daserf](https://attack.mitre.org/software/S0187) can execute shell commands.[^127] [^161]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) can execute commands.[^312]  |
| [[DanBot\|S1014]] | DanBot | [DanBot](https://attack.mitre.org/software/S1014) has the ability to execute arbitrary commands via `cmd.exe`.[^230] [^119]  |
| [[BISCUIT\|S0017]] | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) has a command to launch a command shell on the system.[^730]  |
| [[Pisloader\|S0124]] | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) uses cmd.exe to set the Registry Run key value. It also has a command to spawn a command shell.[^686]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) can execute remote commands via the command-line interface.[^708] 	 |
| [[Gold Dragon\|S0249]] | Gold Dragon | [Gold Dragon](https://attack.mitre.org/software/S0249) uses cmd.exe to execute commands for discovery.[^431]  |
| [[RGDoor\|S0258]] | RGDoor | [RGDoor](https://attack.mitre.org/software/S0258) uses cmd.exe to execute commands on the victim’s machine.[^503]  |
| [[HARDRAIN\|S0246]] | HARDRAIN | [HARDRAIN](https://attack.mitre.org/software/S0246) uses cmd.exe to execute `netsh`commands.[^339]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) uses cmd.exe to execute commands and run scripts on the victim's machine.[^183]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can use `cmd.exe` for execution on remote hosts.[^296]  |
| [[ROADSWEEP\|S1150]] | ROADSWEEP | [ROADSWEEP](https://attack.mitre.org/software/S1150) can open cmd.exe to enable command execution.[^653] [^114]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) has used cmd.exe for execution.[^91] [^727]  |
| [[TinyZBot\|S0004]] | TinyZBot | [TinyZBot](https://attack.mitre.org/software/S0004) supports execution from the command-line.[^528]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) has used `cmd.exe` to scan a compromised host for specific file extensions.[^663]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) can download and run batch files to execute commands on a compromised host.[^499]  |
| [[DEADEYE\|S1052]] | DEADEYE | [DEADEYE](https://attack.mitre.org/software/S1052) can run `cmd /c copy /y /b C:\Users\public\syslog_6-*.dat C:\Users\public\syslog.dll` to combine separated sections of code into a single DLL prior to execution.[^620]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can use `cmd.exe` to display a decoy file to spearphishing victims.[^153]  |
| [[InnaputRAT\|S0259]] | InnaputRAT | [InnaputRAT](https://attack.mitre.org/software/S0259) launches a shell to execute commands on the victim’s machine.[^246]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can use the Windows Command Shell to execute commands, including its own removal.[^627]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) executes the `cmd.exe` command.[^413]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) can use cmd.exe to help execute commands on the system.[^159]   |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has used `cmd /c` commands embedded within batch scripts.[^274]   |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) has used batch files for execution and can launch Internet Explorer from cmd.exe.[^134] [^700]   |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has called cmd through a Word document macro.[^129]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) executes batch scripts on the victim’s machine, and can launch a reverse shell for command execution.[^174] [^284]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can launch a reverse command shell.[^241] [^552] [^93]  |
| [[CoinTicker\|S0369]] | CoinTicker | [CoinTicker](https://attack.mitre.org/software/S0369) executes a bash script to establish a reverse shell.[^439]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has used cmd.exe to execute commands.[^380] 	 |
| [[BONDUPDATER\|S0360]] | BONDUPDATER | [BONDUPDATER](https://attack.mitre.org/software/S0360) can read batch commands in a file sent from its C2 server and execute them with cmd.exe.[^581]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) can create and execute Windows batch scripts.[^511]  |
| [[BLACKCOFFEE\|S0069]] | BLACKCOFFEE | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) has the capability to create a reverse shell.[^215]  |
| [[Meteor\|S0688]] | Meteor | [Meteor](https://attack.mitre.org/software/S0688) can run `set.bat`, `update.bat`, `cache.bat`, `bcd.bat`, `msrun.bat`, and similar scripts.[^670]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can launch a command shell interface for executing commands.[^84]  |
| [[Maze\|S0449]] | Maze | The [Maze](https://attack.mitre.org/software/S0449) encryption process has used batch scripts with various commands.[^396] [^464]  |
| [[ComRAT\|S0126]] | ComRAT | [ComRAT](https://attack.mitre.org/software/S0126) has used `cmd.exe` to execute commands.[^184]  |
| [[TURNEDUP\|S0199]] | TURNEDUP | [TURNEDUP](https://attack.mitre.org/software/S0199) is capable of creating a reverse shell.[^192]  |
| [[Manjusaka\|S1156]] | Manjusaka | [Manjusaka](https://attack.mitre.org/software/S1156) can execute arbitrary commands passed to it from the C2 controller via `cmd.exe /c`.[^407]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can use the command-line utility cacls.exe to change file permissions.[^735]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) can execute shell commands on a compromised host.[^233]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has used `cmd.exe` and batch files for execution.[^104]  |
| [[MechaFlounder\|S0459]] | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) has the ability to run commands on a compromised host.[^624]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of spawning a reverse shell on a victim.[^619]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) has used `cmd.exe` to run commands on a compromised host.[^681]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can run shell commands using a BAT file with a name matching `%TEMP%\<⁠random_9_alnum_chars>.batfile` or through cmd.exe with the `/c` and `/U` option for Unicode output.[^517]  |
| [[Dipsind\|S0200]] | Dipsind | [Dipsind](https://attack.mitre.org/software/S0200) can spawn remote shells.[^735]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) has run `cmd /C [PsExec] -accepteula \\IP Address -c -f -h -d -i<br>C:\Users\xxx\<encryptor_1>.exe --password [PASSWORD] --spread --spread-process` to execute its encryptor to target multiple network shares.[^742]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to execute commands via `cmd.exe`.[^378]  |
| [[MirageFox\|S0280]] | MirageFox | [MirageFox](https://attack.mitre.org/software/S0280) has the capability to execute commands using cmd.exe.[^328]  |
| [[DownPaper\|S0186]] | DownPaper | [DownPaper](https://attack.mitre.org/software/S0186) uses the command line.[^463]  |
| [[CozyCar\|S0046]] | CozyCar | A module in [CozyCar](https://attack.mitre.org/software/S0046) allows arbitrary commands to be executed by invoking `C:\Windows\System32\cmd.exe`.[^504]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can use a renamed image of `cmd.exe` for execution.[^112]  |
| [[httpclient\|S0068]] | httpclient | [httpclient](https://attack.mitre.org/software/S0068) opens cmd.exe on the victim.[^98]  |
| [[ECCENTRICBANDWAGON\|S0593]] | ECCENTRICBANDWAGON | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) can use [cmd](https://attack.mitre.org/software/S0106) to execute commands on a victim’s machine.[^332]  |
| [[BADNEWS\|S0128]] | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) is capable of executing commands via cmd.exe.[^390] [^279]  |
| [[Linfo\|S0211]] | Linfo | [Linfo](https://attack.mitre.org/software/S0211) creates a backdoor through which remote attackers can start a remote shell.[^360]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has the ability to use cmd.exe to execute commands passed from an Outlook C2 channel.[^689] 	 |
| [[Remexi\|S0375]] | Remexi | [Remexi](https://attack.mitre.org/software/S0375) silently executes received commands with cmd.exe.[^225]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) spawns a CMD process to execute commands. [^227]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can use cmd.exe to launch itself and to execute multiple C2 commands.[^568] [^374] [^559] [^660]  |
| [[SYSCON\|S0464]] | SYSCON | [SYSCON](https://attack.mitre.org/software/S0464) has the ability to execute commands through [cmd](https://attack.mitre.org/software/S0106) on a compromised host.[^715]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can use a batch script to delete itself.[^719]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) has command line access.[^481]  |
| [[Helminth\|S0170]] | Helminth | [Helminth](https://attack.mitre.org/software/S0170) can provide a remote shell. One version of [Helminth](https://attack.mitre.org/software/S0170) uses batch scripting.[^155]  |
| [[BBK\|S0470]] | BBK | [BBK](https://attack.mitre.org/software/S0470) has the ability to use [cmd](https://attack.mitre.org/software/S0106) to run a Portable Executable (PE) on the compromised host.[^236]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) can launch a remote shell to execute arbitrary commands on the victim’s machine.[^746] [^689]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) executes BAT scripts.[^739]  |
| [[PHOREAL\|S0158]] | PHOREAL | [PHOREAL](https://attack.mitre.org/software/S0158) is capable of creating reverse shell.[^96]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) has a command to open the command-line on the infected system.[^362] [^490]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) has used `cmd.exe` to add a persistent service.[^344]  |
| [[H1N1\|S0132]] | H1N1 | [H1N1](https://attack.mitre.org/software/S0132) kills and disables services by using cmd.exe.[^683]  |
| [[Seth-Locker\|S0639]] | Seth-Locker | [Seth-Locker](https://attack.mitre.org/software/S0639) can execute commands via the command line shell.[^657]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) used a batch script to run the Linux virtual machine as a service.[^54]  |
| [[BACKSPACE\|S0031]] | BACKSPACE | Adversaries can direct [BACKSPACE](https://attack.mitre.org/software/S0031) to execute from the command line on infected hosts, or have [BACKSPACE](https://attack.mitre.org/software/S0031) create a reverse shell.[^412]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) uses cmd.exe to execute commands on the victim’s machine.[^370]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) can create a remote shell and run a given command.[^394] [^16]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can execute shell commands using `cmd.exe`.[^147]  |
| [[Mivast\|S0080]] | Mivast | [Mivast](https://attack.mitre.org/software/S0080) has the capability to open a remote shell and run basic commands.[^366]  |
| [[HiddenWasp\|S0394]] | HiddenWasp | [HiddenWasp](https://attack.mitre.org/software/S0394) uses a script to automate tasks on the victim's machine and to assist in execution.[^647]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can use `cmd.exe` to execute malicious code.[^271]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can open a command line to execute commands.[^148]  |
| [[Small Sieve\|S1035]] | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) can use `cmd.exe` to execute commands on a victim's system.[^529]  |
| [[HermeticWizard\|S0698]] | HermeticWizard | [HermeticWizard](https://attack.mitre.org/software/S0698) can use `cmd.exe` for execution on compromised hosts.[^650]  |
| [[Indrik Spider\|G0119]] | Indrik Spider | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used batch scripts on victim's machines.[^61] [^329]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has used Windows Command Prompt to control and execute commands on the system to include ingress, network, and filesystem enumeration activities.[^38]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used `cmd.exe` to execute commands on a victim's machine.[^694] [^126]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) used the command prompt to launch commands on the victim’s machine.[^455] [^43] [^444]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used cmd.exe to open the Run dialog by sending the “Windows + R” keys through malicious USBs acting as virtual keyboards.[^28]   |
| [[UNC3886\|G1048]] | UNC3886 |  [UNC3886](https://attack.mitre.org/groups/G1048) has executed Windows commands on guest virtual machines through `vmtoolsd.exe`.[^365]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has used the Windows command line as part of infection chains to open documents.[^144]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has used various types of scripting to perform operations, including batch scripts.[^120]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has used macros to deliver malware such as [QUADAGENT](https://attack.mitre.org/software/S0269) and [OopsIE](https://attack.mitre.org/software/S0264).[^283] [^254] [^72] [^213] [^298]  [OilRig](https://attack.mitre.org/groups/G0049) has used batch scripts.[^283] [^254] [^72] [^213] [^298]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used cmd.exe likely as a password changing mechanism.[^281]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware uses cmd.exe to execute commands on a compromised host.[^595] [^452] [^359] [^536] [^535]  A Destover-like variant used by [Lazarus Group](https://attack.mitre.org/groups/G0032) uses a batch file mechanism to delete its binaries from the system.[^260]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has attempted and failed to run Bash commands on a Windows host by passing them to `cmd /C`.[^699]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has used batch scripts to download tools and executing cryptocurrency miners.[^188]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has executed commands using `cmd.exe`.[^67]  |
| [[admin@338\|G0018]] | admin@338 | Following exploitation with [LOWBALL](https://attack.mitre.org/software/S0042) malware, [admin@338](https://attack.mitre.org/groups/G0018) actors created a file containing a list of commands to be executed on the compromised computer.[^405]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has executed Windows commands by using `cmd` and running batch scripts.[^641] [^206]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used `cmd.exe` to automatically open downloaded decoy pdf documents with the system’s default PDF viewer.[^139]  [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized malicious payloads to create reverse shells within the victim environment.[^194]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used batch scripts to eventually run [QuasarRAT](https://attack.mitre.org/software/S0262).[^162]  |
| [[Play\|G1040]] | Play | <br>[Play](https://attack.mitre.org/groups/G1040) has used a batch script to remove indicators of its presence on compromised hosts.[^316]  |
| [[TA577\|G1037]] | TA577 | [TA577](https://attack.mitre.org/groups/G1037) has used BAT files in malware execution chains.[^386]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have used cmd.exe to execute commands.[^446] [^472]  |
| [[Suckfly\|G0039]] | Suckfly | Several tools used by [Suckfly](https://attack.mitre.org/groups/G0039) have been command-line driven.[^106]  |
| [[FIN6\|G0037]] | FIN6 | [FIN6](https://attack.mitre.org/groups/G0037) has used `kill.bat` script to disable security tools.[^222]  |
| [[Silence\|G0091]] | Silence | [Silence](https://attack.mitre.org/groups/G0091) has used Windows command-line to run commands.[^484] [^401] [^189]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) ran a reverse shell with Meterpreter.[^441]  [Patchwork](https://attack.mitre.org/groups/G0040) used JavaScript code and .SCT files on victim machines.[^279] [^178]  |
| [[APT28\|G0007]] | APT28 | An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan uses a cmd.exe and batch script to run its payload.[^276]  The group has also used macros to execute payloads.[^73] [^664] [^580] [^545]  |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has executed ransomware using batch scripts deployed via GPO.[^157]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has dropped an mspaint.lnk shortcut to disk which launches a shell script that downloads and executes a file.[^151]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has used batch scripts in its malware to install persistence mechanisms.[^326]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used the Windows command line to perform hands-on-keyboard activities in targeted environments including for discovery.[^750] [^402] [^471] [^417] <br> |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used the command-line interface for code execution.[^696] [^399] [^465]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used a JavaScript backdoor that is capable of launching cmd.exe to execute shell commands.[^561]  The group has used an exploit toolkit known as Threadkit that launches .bat files.[^706] [^47] [^720] [^561] [^621] [^391]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `cmd.exe` to execute commands on the victim's machine.[^679]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used a custom tool for creating reverse shells.[^138]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has used a command-line tunneler, NACHOCHEESE, to give them shell access to a victim’s machine.[^156]  Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used batch scripts.[^347]   |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has used cmd.exe for execution.[^689]   |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used batch scripts and the command-line interface for execution.[^161]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has used cmd.exe for execution on compromised systems.[^498]  |
| [[Storm-1811\|G1046]] | Storm-1811 | [Storm-1811](https://attack.mitre.org/groups/G1046) has used multiple batch scripts during initial access and subsequent actions on victim machines.[^638] [^137]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has executed HTA files via cmd.exe, and used batch scripts for collection.[^108] [^318]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized cmd.exe to execute commands on an infected host such as `cmd.exe /c ping.exe 8.8.8.8 -n 70&&"%temp%\FontEDL.exe"`.[^29]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used the Windows Command Shell and batch scripts for execution on compromised hosts.[^538]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has used .bat scripts and `cmd` for execution on compromised hosts.[^414]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) executes commands using a command-line interface and reverse shell. The group has used a modified version of pentesting script wmiexec.vbs to execute commands.[^255] [^425] [^661] [^370]  [menuPass](https://attack.mitre.org/groups/G0045) has used malicious macros embedded inside Office documents to execute files.[^116] [^370]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used Windows command scripts.[^671] 	 |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used `cmd.exe` for malware execution, file discovery, and manual file manipulation.[^736] [^436] [^543] [^543]  |
| [[APT37\|G0067]] | APT37 | [APT37](https://attack.mitre.org/groups/G0067) has used the command-line interface.[^107] [^410]  |
| [[Threat Group-1314\|G0028]] | Threat Group-1314 | [Threat Group-1314](https://attack.mitre.org/groups/G0028) actors spawned shells on remote systems on a victim network to execute commands.[^668]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) used `cmd.exe /c` to execute commands on remote machines.[^241] <br>[APT41](https://attack.mitre.org/groups/G0096) used a batch file to install persistence for the [Cobalt Strike](https://attack.mitre.org/software/S0154) BEACON loader.[^467]  |
| [[INC Ransom\|G1032]] | INC Ransom | [INC Ransom](https://attack.mitre.org/groups/G1032) has used `cmd.exe` to launch malicious payloads.[^13]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has leveraged `xp_cmdshell` and Windows Command Shell to execute commands on a compromised machine. [FIN13](https://attack.mitre.org/groups/G1016) has also attempted to leverage the ‘xp_cmdshell’ SQL procedure to execute remote commands on internal MS-SQL servers.[^372] [^449]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used the Windows command shell to execute commands.[^382]  |
| [[FIN10\|G0051]] | FIN10 | [FIN10](https://attack.mitre.org/groups/G0051) has executed malicious .bat files containing PowerShell commands.[^587]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used a Batch file to automate frequently executed post compromise cleanup activities.[^211]  [FIN8](https://attack.mitre.org/groups/G0061) has also executed commands remotely via `cmd.exe`.[^546] [^179] [^403]  |
| [[Saint Bear\|G1031]] | Saint Bear | [Saint Bear](https://attack.mitre.org/groups/G1031) initial loaders will also drop a malicious Windows batch file, available via open source GitHub repositories, that disables Microsoft Defender functionality.[^663]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used batch script files to automate execution and deployment of payloads.[^392]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has used the Windows Command Prompt to execute commands.[^477] [^594] [^728]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has utilized VBS scripts to open cmd.exe and run commands to include the go_batch.bat batch file.[^520]  |
| [[Gorgon Group\|G0078]] | Gorgon Group | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can use cmd.exe to download and execute payloads and to execute commands on the system.[^457]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) used `cmd.exe` for execution.[^135] [^567] [^418]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) executed ransomware using the Windows command shell.[^132]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used command-line interfaces for execution.[^175] [^346]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used various batch scripts to establish C2 and download additional files. [Gamaredon Group](https://attack.mitre.org/groups/G0047)'s backdoor malware has also been written to a batch file.[^531] [^168] [^420] [^145]  |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) uses [ASPXSpy](https://attack.mitre.org/software/S0073) web shells to enable follow-on command execution via `cmd.exe`.[^342]  |
| [[Rancor\|G0075]] | Rancor | [Rancor](https://attack.mitre.org/groups/G0075) has used cmd.exe to execute commmands.[^757]  |
| [[TA551\|G0127]] | TA551 | [TA551](https://attack.mitre.org/groups/G0127) has used `cmd.exe` to execute commands.[^70]  |
| [[Dark Caracal\|G0070]] | Dark Caracal | [Dark Caracal](https://attack.mitre.org/groups/G0070) has used macros in Word documents that would download a second stage if executed.[^516]  |
| [[Nomadic Octopus\|G0133]] | Nomadic Octopus | [Nomadic Octopus](https://attack.mitre.org/groups/G0133) used `cmd.exe /c` within a malicious macro.[^549]  |
| [[APT3\|G0022]] | APT3 | An [APT3](https://attack.mitre.org/groups/G0022) downloader uses the Windows command `"cmd.exe" /C whoami`. The group also uses a tool to execute commands on remote computers.[^124] [^614]  |
| [[Metador\|G1013]] | Metador | [Metador](https://attack.mitre.org/groups/G1013) has used the Windows command line to execute commands.[^34]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to open a Windows Command Shell on a remote host.[^640]  |
| [[APT1\|G0006]] | APT1 | [APT1](https://attack.mitre.org/groups/G0006) has used the Windows command shell to execute commands, and batch scripting to automate execution.[^121]  |
| [[Sowbug\|G0054]] | Sowbug | [Sowbug](https://attack.mitre.org/groups/G0054) has used command line during its intrusions.[^539]  |
| [[Machete\|G0095]] | Machete | [Machete](https://attack.mitre.org/groups/G0095) has used batch files to initiate additional downloads of malicious files.[^2]  |
| [[Winter Vivern\|G1035]] | Winter Vivern | [Winter Vivern](https://attack.mitre.org/groups/G1035) distributed Windows batch scripts disguised as virus scanners to prompt download of malicious payloads using built-in system tools.[^704] [^357]  |
| [[APT18\|G0026]] | APT18 | [APT18](https://attack.mitre.org/groups/G0026) uses cmd.exe to execute commands on the victim’s machine.[^393] [^639]  |
| [[LazyScripter\|G0140]] | LazyScripter | [LazyScripter](https://attack.mitre.org/groups/G0140) has used batch files to deploy open-source and multi-stage RATs.[^104]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Execution Prevention\|M1038]] | Execution Prevention | Use application control where appropriate. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)


[^9]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^10]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^11]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


[^12]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^13]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^14]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^15]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^16]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^17]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^18]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^19]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^20]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^21]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^22]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^23]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^24]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^25]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^26]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^27]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^28]: [Gemini_FIN7_Jan2022](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)


[^29]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^30]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^31]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^32]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)


[^33]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^34]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^35]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^36]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^37]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^38]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^39]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^40]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^41]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^42]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^43]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)


[^44]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^45]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^46]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^47]: [PTSecurity Cobalt Group Aug 2017](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)


[^48]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^49]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^50]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^51]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)


[^52]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^53]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^54]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^55]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^56]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^57]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^58]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^59]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^60]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^61]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^62]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^63]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^64]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^65]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^66]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^67]: [Trend Micro TA505 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)


[^68]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^69]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^70]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^71]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^72]: [Unit 42 OopsIE! Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)


[^73]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^74]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^75]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^76]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^77]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^78]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^79]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^80]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^81]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^82]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^83]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^84]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^85]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^86]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^87]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^88]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^89]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^90]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^91]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^92]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^93]: [Secureworks BRONZEUNION Feb 2019](https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox)


[^94]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^95]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^96]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^97]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^98]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^99]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^100]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^101]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)


[^102]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^103]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^104]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^105]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)


[^106]: [Symantec Suckfly May 2016](http://www.symantec.com/connect/blogs/indian-organizations-targeted-suckfly-attacks)


[^107]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^108]: [Anomali MUSTANG PANDA October 2019](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)


[^109]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^110]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^111]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)


[^112]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^113]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^114]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)


[^115]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)


[^116]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


[^117]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^118]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^119]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^120]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^121]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^122]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^123]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^124]: [FireEye Operation Double Tap](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)


[^125]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^126]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^127]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)


[^128]: [Dell Lateral Movement](http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/)


[^129]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)


[^130]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^131]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^132]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^133]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^134]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)


[^135]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^136]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^137]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^138]: [Symantec MuddyWater Dec 2018](https://www.symantec.com/blogs/threat-intelligence/seedworm-espionage-group)


[^139]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^140]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^141]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^142]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^143]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^144]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^145]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^146]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^147]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^148]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^149]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)


[^150]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^151]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^152]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)


[^153]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^154]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^155]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^156]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^157]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^158]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^159]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)


[^160]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^161]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^162]: [NaumaanProofpoint_GlobalClickFix_April2025](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)


[^163]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^164]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^165]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^166]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^167]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^168]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^169]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^170]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^171]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^172]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^173]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^174]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^175]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


[^176]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)


[^177]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^178]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^179]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^180]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^181]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^182]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^183]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)


[^184]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^185]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^186]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^187]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^188]: [ATT TeamTNT Chimaera September 2020](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)


[^189]: [Group IB Silence Sept 2018](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)


[^190]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^191]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)


[^192]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)


[^193]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^194]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^195]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^196]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^197]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^198]: [TechNet Cmd](https://technet.microsoft.com/en-us/library/bb490880.aspx)


[^199]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^200]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^201]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^202]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^203]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^204]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^205]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^206]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^207]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^208]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^209]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^210]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^211]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^212]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^213]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^214]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^215]: [FireEye APT17](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)


[^216]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^217]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^218]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^219]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^220]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^221]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^222]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^223]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^224]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^225]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^226]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^227]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^228]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^229]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^230]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^231]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^232]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^233]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^234]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^235]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)


[^236]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^237]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^238]: [Fidelis INOCNATION](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)


[^239]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^240]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^241]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^242]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^243]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^244]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^245]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^246]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^247]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^248]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^249]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^250]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^251]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^252]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^253]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^254]: [OilRig ISMAgent July 2017](https://researchcenter.paloaltonetworks.com/2017/07/unit42-oilrig-uses-ismdoor-variant-possibly-linked-greenbug-threat-group/)


[^255]: [PWC Cloud Hopper April 2017](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)


[^256]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^257]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^258]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^259]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^260]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^261]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)


[^262]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^263]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^264]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^265]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^266]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^267]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^268]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^269]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^270]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^271]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^272]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^273]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^274]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^275]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^276]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^277]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^278]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)


[^279]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^280]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^281]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^282]: [Cisco DNSMessenger March 2017](http://blog.talosintelligence.com/2017/03/dnsmessenger.html)


[^283]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^284]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^285]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^286]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^287]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^288]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^289]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^290]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^291]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^292]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^293]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^294]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)


[^295]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^296]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^297]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)


[^298]: [Unit42 OilRig Nov 2018](https://unit42.paloaltonetworks.com/unit42-analyzing-oilrigs-ops-tempo-testing-weaponization-delivery/)


[^299]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^300]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^301]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^302]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^303]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^304]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^305]: [Unit42 DarkHydrus Jan 2019](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)


[^306]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^307]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^308]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^309]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^310]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)


[^311]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^312]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^313]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^314]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^315]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^316]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^317]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^318]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^319]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^320]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^321]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^322]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^323]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^324]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^325]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^326]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^327]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^328]: [APT15 Intezer June 2018](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)


[^329]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^330]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^331]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^332]: [CISA EB Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)


[^333]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^334]: [Microsoft GALLIUM December 2019](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)


[^335]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^336]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^337]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^338]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^339]: [US-CERT HARDRAIN March 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)


[^340]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^341]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^342]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^343]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)


[^344]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^345]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^346]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^347]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^348]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^349]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^350]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^351]: [Sofacy DealersChoice](https://researchcenter.paloaltonetworks.com/2018/03/unit42-sofacy-uses-dealerschoice-target-european-government-agency/)


[^352]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


[^353]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^354]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^355]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)


[^356]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^357]: [CERT-UA WinterVivern 2023](https://cert.gov.ua/article/3761104)


[^358]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^359]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^360]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)


[^361]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^362]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)


[^363]: [Google EXOTIC LILY March 2022](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)


[^364]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^365]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^366]: [Symantec Backdoor.Mivast](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)


[^367]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


[^368]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^369]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^370]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^371]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^372]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^373]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^374]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^375]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^376]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^377]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^378]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


[^379]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^380]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^381]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^382]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^383]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^384]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^385]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^386]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^387]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^388]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^389]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^390]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^391]: [TrendMicro Cobalt Group Nov 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/cobalt-spam-runs-use-macros-cve-2017-8759-exploit/)


[^392]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^393]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^394]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^395]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)


[^396]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)


[^397]: [Unit 42 OilRig Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)


[^398]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^399]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^400]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^401]: [SecureList Silence Nov 2017](https://securelist.com/the-silence/83009/)


[^402]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^403]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^404]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)


[^405]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^406]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^407]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


[^408]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^409]: [Cybereason Lockbit 2.0](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)


[^410]: [Talos Group123](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)


[^411]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^412]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^413]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^414]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^415]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^416]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^417]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^418]: [PTSecurity Higaisa 2020](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)


[^419]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)


[^420]: [CERT-EE Gamaredon January 2021](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)


[^421]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^422]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^423]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^424]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


[^425]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^426]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^427]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^428]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^429]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^430]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^431]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^432]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^433]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^434]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^435]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^436]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^437]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^438]: [Halcyon_CloakRansomware_Dec2024](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)


[^439]: [CoinTicker 2019](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)


[^440]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^441]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^442]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^443]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^444]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^445]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^446]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^447]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^448]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^449]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^450]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^451]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


[^452]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^453]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^454]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)


[^455]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^456]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^457]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^458]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^459]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^460]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^461]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^462]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^463]: [ClearSky Charming Kitten Dec 2017](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)


[^464]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)


[^465]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^466]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^467]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^468]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^469]: [FireEye FIN7 March 2017](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)


[^470]: [Symantec Shuckworm January 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)


[^471]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^472]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^473]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)


[^474]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^475]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^476]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


[^477]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^478]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^479]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^480]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^481]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^482]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^483]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^484]: [Cyber Forensicator Silence Jan 2019](https://web.archive.org/web/20220119133748/https://cyberforensicator.com/2019/01/20/silence-dissecting-malicious-chm-files-and-performing-forensic-analysis/)


[^485]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^486]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^487]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)


[^488]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^489]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^490]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^491]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^492]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^493]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^494]: [FireEye HIKIT Rootkit Part 2](https://web.archive.org/web/20210920172620/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-2.html)


[^495]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^496]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^497]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^498]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^499]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^500]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^501]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)


[^502]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^503]: [Unit 42 RGDoor Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)


[^504]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^505]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^506]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^507]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^508]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)


[^509]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^510]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^511]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^512]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^513]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^514]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)


[^515]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^516]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^517]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^518]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^519]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^520]: [Sekoia ClickFake 2025](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)


[^521]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^522]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^523]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^524]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^525]: [Unit 42 SeaDuke 2015](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)


[^526]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^527]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^528]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


[^529]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^530]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^531]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^532]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


[^533]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)


[^534]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)


[^535]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^536]: [US-CERT SHARPKNOT June 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536.11.WHITE.pdf)


[^537]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^538]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^539]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^540]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^541]: [Picus Emotet Dec 2018](https://www.picussecurity.com/blog/the-christmas-card-you-never-wanted-a-new-wave-of-emotet-is-back-to-wreak-havoc.html)


[^542]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^543]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^544]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^545]: [TrendMicro Pawn Storm Dec 2020](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)


[^546]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)


[^547]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^548]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^549]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^550]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^551]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^552]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^553]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^554]: [Talos Sodinokibi April 2019](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)


[^555]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^556]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^557]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^558]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^559]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^560]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^561]: [Morphisec Cobalt Gang Oct 2018](https://blog.morphisec.com/cobalt-gang-2.0)


[^562]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^563]: [Zscaler Bazar September 2020](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)


[^564]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^565]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^566]: [SSH in Windows](https://docs.microsoft.com/en-us/windows/terminal/tutorials/ssh)


[^567]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^568]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^569]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^570]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^571]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^572]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^573]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


[^574]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^575]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^576]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^577]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^578]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


[^579]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^580]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^581]: [Palo Alto OilRig Sep 2018](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)


[^582]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^583]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^584]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^585]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^586]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^587]: [FireEye FIN10 June 2017](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)


[^588]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^589]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^590]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


[^591]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^592]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^593]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^594]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^595]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^596]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^597]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^598]: [Zscaler Lyceum DnsSystem June 2022](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)


[^599]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^600]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^601]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^602]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^603]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^604]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^605]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)


[^606]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^607]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^608]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^609]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^610]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^611]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^612]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^613]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^614]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


[^615]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^616]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^617]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^618]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^619]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^620]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^621]: [Unit 42 Cobalt Gang Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-new-techniques-uncover-attribute-cobalt-gang-commodity-builders-infrastructure-revealed/)


[^622]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^623]: [Github Covenant](https://github.com/cobbr/Covenant)


[^624]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^625]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^626]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^627]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^628]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^629]: [Cofense NanoCore Mar 2018](https://web.archive.org/web/20240522112705/https://cofense.com/blog/nanocore-rat-resurfaced-sewers/)


[^630]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^631]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^632]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^633]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^634]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^635]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^636]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^637]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^638]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)


[^639]: [Anomali Evasive Maneuvers July 2015](https://www.anomali.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


[^640]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^641]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^642]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^643]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^644]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^645]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)


[^646]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^647]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)


[^648]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^649]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^650]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^651]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^652]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^653]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^654]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^655]: [Github Koadic](https://github.com/offsecginger/koadic)


[^656]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^657]: [Trend Micro Ransomware February 2021](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)


[^658]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


[^659]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^660]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^661]: [Github AD-Pentest-Script](https://github.com/Twi1ight/AD-Pentest-Script/blob/master/wmiexec.vbs)


[^662]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^663]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^664]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)


[^665]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^666]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^667]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^668]: [Dell TG-1314](https://web.archive.org/web/20150626073312/http://www.secureworks.com/resources/blog/living-off-the-land/)


[^669]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^670]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)


[^671]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^672]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)


[^673]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^674]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^675]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^676]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^677]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^678]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^679]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^680]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^681]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^682]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^683]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)


[^684]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^685]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^686]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^687]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^688]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^689]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^690]: [Lee 2013](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)


[^691]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^692]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)


[^693]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^694]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^695]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^696]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^697]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^698]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^699]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^700]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)


[^701]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^702]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^703]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^704]: [SentinelOne WinterVivern 2023](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)


[^705]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^706]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^707]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^708]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^709]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^710]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^711]: [TrendMicro Trickbot Feb 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-adds-remote-application-credential-grabbing-capabilities-to-its-repertoire/)


[^712]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^713]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^714]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^715]: [Unit 42 CARROTBAT January 2020](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)


[^716]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^717]: [Umbreon Trend Micro](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)


[^718]: [Carbon Black JCry May 2019](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)


[^719]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^720]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^721]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)


[^722]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^723]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^724]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^725]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^726]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^727]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^728]: [trendmicro_redcurl](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)


[^729]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^730]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^731]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)


[^732]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^733]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^734]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^735]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^736]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^737]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^738]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^739]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^740]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^741]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^742]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^743]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^744]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^745]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^746]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^747]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^748]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)


[^749]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^750]: [Microsoft Volt Typhoon May 2023](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)


[^751]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^752]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^753]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^754]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^755]: [Sophos SamSam Apr 2018](https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf)


[^756]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)


[^757]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^758]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^759]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^760]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


