---
aliases: 
    - T1036.005
mitre-attack: https://attack.mitre.org/techniques/T1036/005
tactic: 
     - Stealth
platforms:
     - Containers - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## T1036.005

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation. <br><br>This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: `svchost.exe`). Alternatively, a Windows Registry key may be given a close approximation to a key used by a legitimate program. In containerized environments, a threat actor may create a resource in a trusted namespace or one that matches the naming convention of a container pod or cluster.[^451] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) spoofed itself as `AlphaZawgyl_font.exe`, a specialized Unicode font.[^319]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) has been named `wuauclt.exe` to appear as the legitimate Windows Update AutoUpdate Client.[^215]  |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used a payload file named OneDrive.update to appear benign.[^386]  |
| [[MCMD\|S0500]] | MCMD | [MCMD](https://attack.mitre.org/software/S0500) has been named Readme.txt to appear legitimate.[^373]  |
| [[EKANS\|S0605]] | EKANS | [EKANS](https://attack.mitre.org/software/S0605) has been disguised as `update.exe` to appear as a valid executable.[^396]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has attempted to hide its payload by using legitimate file names such as "iconcache.db".[^321]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) has used legitimate looking filenames for its loader including update.dll and x64.dll.[^293]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has named component DLLs "RapportGP.dll" to match those used by the security company Trusteer.[^239]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has appeared to resemble legitimate processes to include the vCenter process `vami-http`.[^420] [^266] [^542]  [BRICKSTORM](https://attack.mitre.org/software/S9015) has also leveraged legitimate names of VMware vSphere platform such as `vmsrc` or `vmware-sphere`.[^228]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) is written to %LOCALAPPDATA%\MicroSoft Updatea\svServiceUpdate.exe prior being executed in a new process in an apparent attempt to masquerade as a legitimate folder and file.[^519]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) has used the filename `systemd-daemon` in an attempt to appear legitimate.[^37]  |
| [[Chinoxy\|S1041]] | Chinoxy | [Chinoxy](https://attack.mitre.org/software/S1041) has used the name `eoffice.exe` in attempt to appear as a legitimate file.[^215]  |
| [[Misdat\|S0083]] | Misdat | [Misdat](https://attack.mitre.org/software/S0083) saves itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^493] [^134]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used strings from legitimate system files and existing folders for its file, folder, and Registry entry names.[^486]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) chooses its payload creation path from a randomly selected service name from netsvc.[^367]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) mimics the resource version information of legitimate Realtek Semiconductor, Nvidia, or Synaptics modules.[^493]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034) has disguised its MSI installer as a fake installer for popular games and software.[^443]   |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) has masqueraded as legitimate Adobe Content Management System files.[^120]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) has been bundled with legitimate software installation files for disguise.[^275]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) uses functions named `StartUserModeBrowserInjection` and `StopUserModeBrowserInjection` indicating that it's trying to imitate chrome_frame_helper.dll.[^338]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has renamed malicious files to mimic legitimate file names and file extensions.[^153]  [TONESHELL](https://attack.mitre.org/software/S1239) has also masqueraded as legitimate file names to include LogMeIn.dll.[^264]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) has used names to mimic legitimate software including "vmtoolsd.exe" to spoof Vmtools.[^338]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) has the ability to rename its payload to ESTCommon.dll to masquerade as a DLL belonging to ESTsecurity.[^511]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) has masqueraded as legitimate software including TeamViewer and macOS Finder.[^183]  |
| [[TinyTurla\|S0668]] | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) has been deployed as `w64time.dll` to appear legitimate.[^529]  |
| [[PyDCrypt\|S1032]] | PyDCrypt | [PyDCrypt](https://attack.mitre.org/software/S1032) has dropped [DCSrv](https://attack.mitre.org/software/S1033) under the `svchost.exe` name to disk.[^301] <br> |
| [[J-magic\|S1203]] | J-magic | [J-magic](https://attack.mitre.org/software/S1203) can rename itself as “[nfsiod 0]” to masquerade as the local Network File System (NFS) asynchronous I/O server.[^232]  |
| [[OLDBAIT\|S0138]] | OLDBAIT | [OLDBAIT](https://attack.mitre.org/software/S0138) installs itself in `%ALLUSERPROFILE%\\Application Data\Microsoft\MediaPlayer\updatewindws.exe`; the directory name is missing a space and the file name is missing the letter "o."[^530]  |
| [[Bad Rabbit\|S0606]] | Bad Rabbit | [Bad Rabbit](https://attack.mitre.org/software/S0606) has masqueraded as a Flash Player installer through the executable file `install_flash_player.exe`.[^107] [^9]  |
| [[SslMM\|S0058]] | SslMM | To establish persistence, [SslMM](https://attack.mitre.org/software/S0058) identifies the Start Menu Startup directory and drops a link to its own executable disguised as an “Office Start,” “Yahoo Talk,” “MSN Gaming Z0ne,” or “MSN Talk” shortcut.[^368]  |
| [[STATICPLUGIN\|S1238]] | STATICPLUGIN | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has leveraged naming conventions that match legitimate services to include AdobePlugins.exe.[^401]  |
| [[TEARDROP\|S0560]] | TEARDROP | [TEARDROP](https://attack.mitre.org/software/S0560) files had names that resembled legitimate Window file and directory names.[^75] [^84]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) renamed payloads to masquerade as legitimate Google Chrome, Java, Dropbox, Adobe Reader and Python executables.[^172] [^514]  |
| [[DUSTPAN\|S1158]] | DUSTPAN | [DUSTPAN](https://attack.mitre.org/software/S1158) is often disguised as a legitimate Windows binary such as `w3wp.exe` or `conn.exe`.[^459]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has renamed malicious files to mimic legitimate file names such as adobe_wf.exe.[^153]  |
| [[CANONSTAGER\|S1237]] | CANONSTAGER | [CANONSTAGER](https://attack.mitre.org/software/S1237) has leveraged naming conventions of its malicious DLL to match legitimate services to include cnmpaui.dll which matches the legitimate executable cnmpaui.exe that is aligned with a Canon Ink Jet Printer Assistant Tool.[^401]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has masqueraded and typosquatted as legitimate code repository packages and projects.[^408] [^472]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | <br>[Cuckoo Stealer](https://attack.mitre.org/software/S1153) has copied and renamed itself to DumpMediaSpotifyMusicConverter.[^247] [^549]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) has disguised its droppers as legitimate software or documents, matching their original names and locations, and saved its files as mpr.dll in the Windows folder.[^204] [^60]  |
| [[CLAIMLOADER\|S1236]] | CLAIMLOADER | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has imitated legitimate software directories through the creation and storage of the EXE and DLL in `C:\ProgramData\` and the use of legitimate looking names of software.[^186]  |
| [[QUIETEXIT\|S1084]] | QUIETEXIT | [QUIETEXIT](https://attack.mitre.org/software/S1084) has attempted to change its name to `cron` upon startup. During incident response, [QUIETEXIT](https://attack.mitre.org/software/S1084) samples have been identified that were renamed to blend in with other legitimate files.[^548]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) has masqueraded as VMware.exe.[^439] 	 |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has created a fake `rm` binary to replace the legitimate Linux binary.[^485]  |
| [[TRANSLATEXT\|S1201]] | TRANSLATEXT | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has been named `GoogleTranslate.crx` to masquerade as a legitimate Chrome extension.[^461]   |
| [[SameCoin\|S9030]] | SameCoin | [SameCoin](https://attack.mitre.org/software/S9030) has named files to appear legitimate such as "MicrosoftEdge.exe."[^102]  |
| [[Raindrop\|S0565]] | Raindrop | [Raindrop](https://attack.mitre.org/software/S0565) was installed under names that resembled legitimate Windows file and directory names.[^424] [^84]  |
| [[Doki\|S0600]] | Doki | [Doki](https://attack.mitre.org/software/S0600) has disguised a file as a Linux kernel module.[^41]  |
| [[RustyWater\|S9037]] | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) has used reddit.exe as its file name and a Cloudflare logo.[^46]      |
| [[Fysbis\|S0410]] | Fysbis | [Fysbis](https://attack.mitre.org/software/S0410) has masqueraded as trusted software rsyncd and dbus-inotifier.[^413]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) has modified legitimate .dll files to include malicious code.[^245]  |
| [[MarkiRAT\|S0652]] | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) can masquerade as `update.exe` and `svehost.exe`; it has also mimicked legitimate Telegram and Chrome files.[^65]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) has dropped itself onto victim machines with file names such as WinDefender.Exe and winupdate.exe in an apparent attempt to masquerade as a legitimate file.[^315]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) has been named `Flash.exe`, and its dropper has been named `IExplorer`.[^335]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) has been named `AutoUpdater.js` to mimic legitimate update files.[^370]  |
| [[Green Lambert\|S0690]] | Green Lambert | [Green Lambert](https://attack.mitre.org/software/S0690) has been disguised as a Growl help file.[^93] [^458]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) mimics filenames from %SYSTEM%\System32 to hide DLLs in %WINDIR% and/or %TEMP%.[^151] [^515]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) has used filenames that matched the system name, and appeared as a scheduled task impersonating systems management software within the corresponding ProgramData subfolder.[^288] [^289]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has been disguised as legitimate Adobe and PotPlayer files.[^502]  [PlugX](https://attack.mitre.org/software/S0013) has also imitated legitimate software directories and file names through the creation and storage of a legitimate EXE and the malicious DLLs.[^509] [^19] [^516] [^98]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has renamed malicious code to `msacm32.dll` to hide within a legitimate library; earlier versions were disguised as `winhelp`.[^138]   |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) may save itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^493] [^134]  |
| [[Remsec\|S0125]] | Remsec | The [Remsec](https://attack.mitre.org/software/S0125) loader implements itself with the name Security Support Provider, a legitimate Windows function. Various [Remsec](https://attack.mitre.org/software/S0125) .exe files mimic legitimate file names used by Microsoft, Symantec, Kaspersky, Hewlett-Packard, and VMWare. [Remsec](https://attack.mitre.org/software/S0125) also disguised malicious modules using similar filenames as custom network encryption software on victims.[^476] [^208]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) has used filenames associated with Exchange and Outlook for binary and configuration files, such as `winmail.dat`.[^500]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) has been disguised as legitimate 360 Total Security Antivirus and OpenVPN programs.[^28]   |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) has used multiple file names to appear legitimate such as firefox\firefox.exe, Google\chrome.exe, and Taskmgr.exe.[^124]  |
| [[ThiefQuest\|S0595]] | ThiefQuest | [ThiefQuest](https://attack.mitre.org/software/S0595) prepends a copy of itself to the beginning of an executable file while maintaining the name of the executable.[^192] [^363]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) can be disguised as a Visual Studio file such as `Windows.Data.TimeZones.zh-PH.pri` to evade detection. Also, [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can mimic a genuine `dll` file that carries out the same import functions as the legitimate Windows `version.dll` file.[^227]  |
| [[Elise\|S0081]] | Elise | If installing itself as a service fails, [Elise](https://attack.mitre.org/software/S0081) instead writes itself as a file named svchost.exe saved in %APPDATA%\Microsoft\Network.[^428]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) has been packed to appear as a component to Bitdefender’s kernel-mode driver, TRUFOS.SYS.[^109]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has been disguised as a legitimate executable, including as Windows SDK.[^226]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) has used an unsigned, crafted DLL module named `hha.dll` that was designed to look like a legitimate 32-bit Windows DLL.[^113]  |
| [[Bundlore\|S0482]] | Bundlore | [Bundlore](https://attack.mitre.org/software/S0482) has disguised a malicious .app file as a Flash Player update.[^97]  |
| [[Fooder\|S9033]] | Fooder | [Fooder](https://attack.mitre.org/software/S9033) has frequently masqueraded as the Snake game, using strings such as “Welcome to snake Game” and mutexes such as “SNAKE_G.”[^118]     |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) used the PowerShell filenames `Office365DCOMCheck.ps1` and `SystemDiskClean.ps1`.[^155]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | The [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) main executable has disguised itself as Microsoft’s Narrator.[^38]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has disguised an MSI file as the Adobe Acrobat Reader Installer and has masqueraded payloads as OneDrive, WhatsApp, or Spotify, for example.[^313] [^207]   |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) modules are stored on disk with seemingly benign names including use of a file extension associated with a popular word processor.[^110]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) stores configuration data in files and file paths mimicking legitimate operating system resources.[^270]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has created a shortcut called "Anti virus service.lnk" in an apparent attempt to masquerade as a legitimate file.[^346]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) has masqueraded as a legitimate Windows tool.[^143]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) has used registry values and file names associated with Adobe software, such as AcroRd32.exe.[^145]  |
| [[Black Basta\|S1070]] | Black Basta | The [Black Basta](https://attack.mitre.org/software/S1070) dropper has mimicked an application for creating USB bootable drivers.[^541]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) has chosen file names to appear legitimate including EsetUpdate-0117583943.exe for its dropper.[^539]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) payloads have tailored filenames to include names identical to the name of the targeted organization or company.[^201]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) has named malicious browser extensions and update files to appear legitimate.[^457] [^92]  |
| [[Starloader\|S0188]] | Starloader | [Starloader](https://attack.mitre.org/software/S0188) has masqueraded as legitimate software update packages such as Adobe Acrobat Reader and Intel.[^375]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) has downloaded a DLL to the `C:\windows\system32\drivers\` folder and renamed it with a `.sys` extension.[^288]  |
| [[Tarrask\|S1011]] | Tarrask | [Tarrask](https://attack.mitre.org/software/S1011) has masqueraded as executable files such as `winupdate.exe`, `date.exe`, or `win.exe`.[^332]     |
| [[GoBear\|S1197]] | GoBear | [GoBear](https://attack.mitre.org/software/S1197) is installed through droppers masquerading as legitimate, signed software installers.[^425]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) binaries have been named `audioddg.pdb` and `Winlangdb.pdb` in order to appear legitimate.[^87]  |
| [[Bazar\|S0534]] | Bazar | The [Bazar](https://attack.mitre.org/software/S0534) loader has named malicious shortcuts "adobe" and mimicked communications software.[^47] [^169] [^478]  |
| [[SUGARDUMP\|S1042]] | SUGARDUMP | [SUGARDUMP](https://attack.mitre.org/software/S1042) has been named `CrashReporter.exe` to appear as a legitimate Mozilla executable.[^12]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has constructed legitimate appearing installation folder paths by calling `GetWindowsDirectoryW` and then inserting a null byte at the fourth character of the path. For Windows Vista or higher, the path would appear as `C:\Users\Public`.[^39]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) has used the name `postgressql.exe` to mask a malicious payload.[^467]  |
| [[Pysa\|S0583]] | Pysa | [Pysa](https://attack.mitre.org/software/S0583) has executed a malicious executable by naming it svchost.exe.[^150]  |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) renames one of its .dll files to uxtheme.dll in an apparent attempt to masquerade as a legitimate file.[^4] [^122]  |
| [[OwaAuth\|S0072]] | OwaAuth | [OwaAuth](https://attack.mitre.org/software/S0072) uses the filename owaauth.dll, which is a legitimate file that normally resides in `%ProgramFiles%\Microsoft\Exchange Server\ClientAccess\Owa\Auth\`; the malicious file by the same name is saved in `%ProgramFiles%\Microsoft\Exchange Server\ClientAccess\Owa\bin\`.[^438]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) created VBScripts that were named after existing services or folders to blend into legitimate activities.[^84]   |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can mimic the names of known executables.[^253]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) has created the directory `%COMMONPROGRAMFILES%\Microsoft Shared\wmi\` to contain DLLs for loading successive stages.[^221]  |
| [[USBStealer\|S0136]] | USBStealer | [USBStealer](https://attack.mitre.org/software/S0136) mimics a legitimate Russian program called USB Disk Security.[^504]  |
| [[SUPERNOVA\|S0578]] | SUPERNOVA | [SUPERNOVA](https://attack.mitre.org/software/S0578) has masqueraded as a legitimate SolarWinds DLL.[^125] [^164]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) can rename its running process to `[kworker:0/1]` to masquerade as a Linux kernel thread. [Cyclops Blink](https://attack.mitre.org/software/S0687) has also named RC scripts used for persistence after WatchGuard artifacts.[^311]  |
| [[Daserf\|S0187]] | Daserf | [Daserf](https://attack.mitre.org/software/S0187) uses file and folder names related to legitimate programs in order to blend in, such as HP, Intel, Adobe, and perflogs.[^140]  |
| [[DanBot\|S1014]] | DanBot | [DanBot](https://attack.mitre.org/software/S1014) files have been named `UltraVNC.exe` and `WINVNC.exe` to appear as legitimate VNC tools.[^87]  |
| [[Calisto\|S0274]] | Calisto | [Calisto](https://attack.mitre.org/software/S0274)'s installation file is an unsigned DMG image under the guise of Intego’s security solution for mac.[^397]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493)'s setup file installs initial executables under the folder `%WinDir%\System32\PluginManager`.[^510] 	 |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) has masqueraded as a 7zip installer.[^283] [^10] 	 |
| [[AshTag\|S9031]] | AshTag | [AshTag](https://attack.mitre.org/software/S9031) has masqueraded as a legitimate VisualServer utility.[^81]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) has masqueraded as Windows system file names, as well as "chkntfs.exe" and "syscron.exe".[^312] [^233]  |
| [[SUNSPOT\|S0562]] | SUNSPOT | [SUNSPOT](https://attack.mitre.org/software/S0562) was identified on disk with a filename of `taskhostsvc.exe` and it created an encrypted log file at `C:\Windows\Temp\vmware-vmdmp.log`.[^280]   |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) attempts to download and execute [Saint Bot](https://attack.mitre.org/software/S1018) to a statically-defined location attempting to mimic svchost: `%TEMP%\\svjhost.exe`.[^479]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) has hidden malicious payloads in `%USERPROFILE%\Adobe\Driver\dwg\` and mimicked the legitimate DHCP service binary.[^351]  |
| [[PowGoop\|S1046]] | PowGoop | [PowGoop](https://attack.mitre.org/software/S1046) has used a DLL named Goopdate.dll to impersonate a legitimate Google update file.[^94]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) payloads have been disguised with legitimate looking filenames including AI_generator_uncensored_Canvas_PRO_v0.9.exe and AI_image_generator_v0.95.exe.[^108] [^522]  |
| [[InnaputRAT\|S0259]] | InnaputRAT | [InnaputRAT](https://attack.mitre.org/software/S0259) variants have attempted to appear legitimate by using the file names SafeApp.exe and NeutralApp.exe.[^182]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) has a C2 proxy tool that masquerades as `GUP.exe`, which is software used by Notepad++.[^292]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) has mimicked the Cron binary to hide itself on compromised systems.[^166]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | A [Winnti for Windows](https://attack.mitre.org/software/S0141) implant file was named ASPNET_FILTER.DLL, mimicking the legitimate ASP.NET ISAPI filter DLL with the same name.[^537]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) is typically installed via a dropper file that masquerades as a legitimate security program installation file.[^358] [^425]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) copies itself to an .exe file with a filename that is likely intended to imitate Norton Antivirus but has several letters reversed (e.g. notron.exe).[^299]  |
| [[ANDROMEDA\|S1074]] | ANDROMEDA | [ANDROMEDA](https://attack.mitre.org/software/S1074) has been installed to `C:\Temp\TrustedInstaller.exe` to mimic a legitimate Windows installer service.[^45]  |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022) .NET assemblies have used `App_Web_` in their file names to appear legitimate.[^447]  |
| [[Shai-Hulud\|S9008]] | Shai-Hulud | [Shai-Hulud](https://attack.mitre.org/software/S9008) has masqueraded as a legitimate Bun installer.[^56] [^42]  |
| [[VIRTUALPITA\|S1217]] | VIRTUALPITA | [VIRTUALPITA](https://attack.mitre.org/software/S1217) samples have been found in `/usr/libexec/setconf/ksmd` and `/usr/bin/ksmd`, named to spoof the legitimate Kernel Same-Page Merging Daemon binary. [^263]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has been disguised as legitimate software programs associated with the travel and airline industries.[^152]   |
| [[MechaFlounder\|S0459]] | MechaFlounder | [MechaFlounder](https://attack.mitre.org/software/S0459) has been downloaded as a file named lsass.exe, which matches the legitimate Windows file.[^440]  |
| [[HTTPBrowser\|S0070]] | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070)'s installer contains a malicious file named navlu.dll to decrypt and run the RAT. navlu.dll is also the name of a legitimate Symantec DLL.[^403]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) saves itself as a file named `msdtc.exe`, which is also the name of the legitimate Microsoft Distributed Transaction Coordinator service binary.[^493] [^134]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) has been disguised as legitimate programs, such as Java and Telegram Messenger.[^405] [^382]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) has named its payload file TeamViewer_Host_Setup to disguise itself as a legitimate TeamViewer file.[^538]  |
| [[BADNEWS\|S0128]] | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) attempts to hide its payloads using legitimate filenames.[^336]  |
| [[Goopy\|S0477]] | Goopy | [Goopy](https://attack.mitre.org/software/S0477) has impersonated the legitimate goopdate.dll, which was dropped on the target system with a legitimate GoogleUpdate.exe.[^499]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) has named malicious binaries `serv.exe`, `winprint.dll`, and `chrome_elf.dll` and has set its persistence in the Registry with the key value `Chrome Update` to appear legitimate.[^520]  |
| [[OSX／Shlayer\|S0402]] | OSX／Shlayer | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can masquerade as a Flash Player update.[^432] [^73]  |
| [[Dtrack\|S0567]] | Dtrack | One of [Dtrack](https://attack.mitre.org/software/S0567) can hide in replicas of legitimate programs like OllyDbg, 7-Zip, and FileZilla.[^254]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) has been named `calc.exe` to appear as a legitimate calculator program.[^104]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has mimicked the names of known executables, such as mediaplayer.exe.[^105]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has leveraged legitimate package names to mimic frequently utilized tools to entice victims to download and execute malicious payloads.[^51]  |
| [[Small Sieve\|S1035]] | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) can use variations of Microsoft and Outlook spellings, such as "Microsift", in its file names to avoid detection.[^372]  |
| [[HermeticWizard\|S0698]] | HermeticWizard | [HermeticWizard](https://attack.mitre.org/software/S0698) has been named `exec_32.dll` to mimic a legitimate MS Outlook .dll.[^467]  |
| [[Indrik Spider\|G0119]] | Indrik Spider | [Indrik Spider](https://attack.mitre.org/groups/G0119) used fake updates for FlashPlayer plugin and Google Chrome as initial infection vectors.[^49]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has disguised their exfiltration malware as `ZoomVideoApp.exe`.[^524]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has attempted to run Darkside ransomware with the filename sleep.exe.[^337]  Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has mimicked WsTaskLoad.exe, which is associated with the Wondershare software suite, by using a malicious executable under the same name.[^235]    |
| [[Velvet Ant\|G1047]] | Velvet Ant | [Velvet Ant](https://attack.mitre.org/groups/G1047) used a malicious DLL, `iviewers.dll`, that mimics the legitimate "OLE/COM Object Viewer" within Windows.[^230]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has used security service provider naming conventions such as ESET and Kasperky ("Kaspersky Update Agent") in order to appear legitimate.[^339] [^102]  |
| [[APT-C-36\|G0099]] | APT-C-36 | [APT-C-36](https://attack.mitre.org/groups/G0099) has disguised malicious executables to appear as legitimate files.[^173]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has named a downloaded copy of the Plink tunneling utility as \ProgramData\Adobe.exe.[^203]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has named binaries and configuration files svhost and dllhost respectively to appear legitimate.[^205]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has renamed malicious code to disguise it as Microsoft's narrator and other legitimate files.[^38] [^374]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) renamed or moved malicious binaries to legitimate locations to evade defenses and blend into victim environments.[^180]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has replaced .dockerd and .dockerenv with their own scripts and cryptocurrency mining software.[^130]  |
| [[admin@338\|G0018]] | admin@338 | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command to rename one of their tools to a benign file name: `ren "%temp%\upload" audiodg.exe`[^287]  |
| [[APT42\|G1044]] | APT42 | [APT42](https://attack.mitre.org/groups/G1044) has masqueraded the VINETHORN payload as a VPN application.[^167]   |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `move [file path] c:\windows\system32\spool\prtprocs\x64\spool.dll` to move and register a malicious DLL name as a Windows print processor, which eventually was loaded by the Print Spooler service.[^434]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has renamed malware to legitimate names such as `ESTCommon.dll` or `patch.dll`.[^149]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also disguised payloads using legitimate file names including a PowerShell payload named chrome.ps1. [^141]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also used a malicious QR code that masqueraded as a legitimate package delivery service.[^496]      |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has avoided detection by naming a malicious binary explorer.exe.[^44] [^296]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has named components of [LunarWeb](https://attack.mitre.org/software/S1141) to mimic Zabbix agent logs.[^362]  |
| [[Ember Bear\|G1003]] | Ember Bear | [Ember Bear](https://attack.mitre.org/groups/G1003) has renamed tools to match legitimate utilities, such as renaming GOST tunneling instances to `java` in victim environments.[^349]  |
| [[Silence\|G0091]] | Silence | [Silence](https://attack.mitre.org/groups/G0091) has named its backdoor "WINWORD.exe".[^135]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) installed its payload in the startup programs folder as "Baidu Software Update." The group also adds its second stage payload to the startup programs as “Net Monitor."[^309]  They have also dropped [QuasarRAT](https://attack.mitre.org/software/S0262) binaries as files named microsoft_network.exe and crome.exe.[^127]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) has changed extensions on files containing exfiltrated data to make them appear benign, and renamed a web shell instance to appear as a legitimate OWA page.[^481]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has used malware that is disguised as a Secure Shell (SSH) tool.[^325]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has dropped their malware into legitimate installed software paths including: `C:\ProgramFiles\Realtek\Audio\HDA\AERTSr.exe`, `C:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitRdr64.exe`, `C:\Program Files (x86)\Adobe\Flash Player\AddIns\airappinstaller\airappinstall.exe`, and `C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd64.exe`.[^139]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used legitimate looking filenames for compressed copies of the ntds.dit database and used names including cisco_up.exe, cl64.exe, vm3dservice.exe, watchdogd.exe, Win.exe, WmiPreSV.exe, and WmiPrvSE.exe for the Earthworm and Fast Reverse Proxy tools.[^285] [^329] [^295]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used `dllhost.exe` to mask Fast Reverse Proxy (FRP) and `MicrosoftOutLookUpdater.exe` for Plink.[^282] [^326] [^474]  |
| [[APT29\|G0016]] | APT29 | [APT29](https://attack.mitre.org/groups/G0016) has renamed malicious DLLs with legitimate names to appear benign; they have also created an Azure AD certificate with a Common Name that matched the display name of the compromised service principal.[^525] [^390]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has used malware disguised as Mozilla Firefox and a tool named mfevtpse.exe to proxy C2 communications, closely mimicking a legitimate McAfee file mfevtps.exe.[^414] [^168]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has disguised malicious executables and used filenames and Registry key names associated with Windows Defender.[^297] [^274] [^286]  |
| [[Transparent Tribe\|G0134]] | Transparent Tribe | [Transparent Tribe](https://attack.mitre.org/groups/G0134) can mimic legitimate Windows directories by using the same icons and names.[^162]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has renamed a NetCat binary to kb-10233.exe to masquerade as a Windows update. [APT32](https://attack.mitre.org/groups/G0050) has also renamed a Cobalt Strike beacon payload to install_flashplayers.exe. [^499] [^404]  |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has given malware the same name as an existing file on the file share server to cause users to unwittingly launch and install the malware on additional systems.[^112]  |
| [[APT5\|G1023]] | APT5 | [APT5](https://attack.mitre.org/groups/G1023) has named exfiltration archives to mimic Windows Updates at times using filenames with a `KB<digits>.zip` pattern.[^348]  |
| [[BackdoorDiplomacy\|G0135]] | BackdoorDiplomacy | [BackdoorDiplomacy](https://attack.mitre.org/groups/G0135) has dropped implants in folders named for legitimate software.[^421]  |
| [[Storm-1811\|G1046]] | Storm-1811 | [Storm-1811](https://attack.mitre.org/groups/G1046) has disguised [Cobalt Strike](https://attack.mitre.org/software/S0154) installers as a malicious DLL masquerading as part of a legitimate 7zip installation package.[^96]  |
| [[Akira\|G1024]] | Akira | [Akira](https://attack.mitre.org/groups/G1024) has used legitimate names and locations for files to evade defenses.[^16]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used names like `adobeupdate.dat` and `PotPlayerDB.dat` to disguise [PlugX](https://attack.mitre.org/software/S0013), and a file named `OneDrive.exe` to load a [Cobalt Strike](https://attack.mitre.org/software/S0154) payload.[^445]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also masqueraded legitimate browser plugin updates to include AdobePlugins.exe.[^401]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has renamed malware to GoogleUpdate.exe and WinRAR to jucheck.exe, RecordedTV.ms, teredo.tmp, update.exe, and msadcs1.exe.[^15]  |
| [[TA2541\|G1018]] | TA2541 | [TA2541](https://attack.mitre.org/groups/G1018) has used file names to mimic legitimate Windows files or system functionality.[^206]  |
| [[ToddyCat\|G1022]] | ToddyCat | [ToddyCat](https://attack.mitre.org/groups/G1022) has used the name `debug.exe` for malware components.[^221]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has been seen changing malicious files to appear legitimate.[^271]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has hidden payloads in Flash directories and fake installer files.[^484]  |
| [[Mustard Tempest\|G1020]] | Mustard Tempest | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used the filename `AutoUpdater.js` to mimic legitimate update files and has also used the Cyrillic homoglyph characters С `(0xd0a1)` and а `(0xd0b0)`, to produce the filename `Сhrome.Updаte.zip`.[^294] [^370]  |
| [[VOID MANTICORE\|G1055]] | VOID MANTICORE | [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has masqueraded malicious payloads to resemble legitimate applications.[^550] [^454]  [VOID MANTICORE](https://attack.mitre.org/groups/G1055) has leveraged malicious payloads that use nomenclature associated with common applications that include Pictory, KeePass, WhatsApp, and Telegram.[^454]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) attempted to masquerade their files as popular anti-virus software.[^177] [^216]  |
| [[INC Ransom\|G1032]] | INC Ransom | [INC Ransom](https://attack.mitre.org/groups/G1032) has named a [PsExec](https://attack.mitre.org/software/S0029) executable winupd to mimic a legitimate Windows update file.[^14] [^290]  |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has masqueraded WAR files to look like legitimate packages such as, wsexample.war, wsexamples.com, examples.war, and exampl3s.war.[^317]  |
| [[Rocke\|G0106]] | Rocke | [Rocke](https://attack.mitre.org/groups/G0106) has used shell scripts which download mining executables and saves them with the filename "java".[^423]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has masqueraded their XMRIG payload name by naming it wercplsupporte.dll after the legitimate wercplsupport.dll file.[^279]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) mimicked legitimate file names and scheduled tasks, e.g. ` MicrosoftCurrentupdatesCheck` and<br>`MdMMaintenenceTask` to mask malicious files and scheduled tasks.[^333] [^411]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has named malicious files `rekeywiz.exe` to match the name of a legitimate Windows executable.[^22]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used legitimate process names to hide malware including `svchosst`.[^103]  Additionally, [Gamaredon Group](https://attack.mitre.org/groups/G0047) disguised malicious ZIP archives as Office documents that are related to the invasion.[^460]  |
| [[APT1\|G0006]] | APT1 | The file name AcroRD32.exe, a legitimate process name for Adobe's Acrobat Reader, was used by [APT1](https://attack.mitre.org/groups/G0006) as a name for malware.[^88] [^528]  |
| [[Naikon\|G0019]] | Naikon | [Naikon](https://attack.mitre.org/groups/G0019) has disguised malicious programs as Google Chrome, Adobe, and VMware executables.[^338]  |
| [[Sowbug\|G0054]] | Sowbug | [Sowbug](https://attack.mitre.org/groups/G0054) named its tools to masquerade as Windows or Adobe Reader software, such as by using the file name adobecms.exe and the directory `CSIDL_APPDATA\microsoft\security`.[^375]  |
| [[Machete\|G0095]] | Machete | [Machete](https://attack.mitre.org/groups/G0095)'s [Machete](https://attack.mitre.org/software/S0409) MSI installer has masqueraded as a legitimate Adobe Acrobat Reader installer.[^2]  |
| [[SideCopy\|G1008]] | SideCopy | [SideCopy](https://attack.mitre.org/groups/G1008) has used a legitimate DLL file name, `Duser.dll` to disguise a malicious remote access tool.[^251]  |
| [[Whitefly\|G0107]] | Whitefly | [Whitefly](https://attack.mitre.org/groups/G0107) has named the malicious DLL the same name as DLLs belonging to legitimate software from various security vendors.[^163]  |
| [[Carbanak\|G0008]] | Carbanak | [Carbanak](https://attack.mitre.org/groups/G0008) has named malware "svchost.exe," which is the name of the Windows shared service host program.[^91]  |
| [[Poseidon Group\|G0033]] | Poseidon Group | [Poseidon Group](https://attack.mitre.org/groups/G0033) tools attempt to spoof anti-virus processes as a means of self-defense.[^388]  |
| [[PROMETHIUM\|G0056]] | PROMETHIUM | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has disguised malicious installer files by bundling them with legitimate software installers.[^275] [^471]  |
| [[Ferocious Kitten\|G0137]] | Ferocious Kitten | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has named malicious files `update.exe` and loaded them into the compromise host's “Public” folder.[^65]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Execution Prevention\|M1038]] | Execution Prevention | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[Code Signing\|M1045]] | Code Signing | Require signed binaries and images. |
| [[Restrict File and Directory Permissions\|M1022]] | Restrict File and Directory Permissions | Use file system access controls to protect folders such as `C:\Windows\System32`. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^5]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^6]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^7]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^8]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^9]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)


[^10]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^11]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^12]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


[^13]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^14]: [Huntress INC Ransom Group August 2023](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)


[^15]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^16]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^17]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^18]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^19]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)


[^20]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^21]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^22]: [Rewterz Sidewinder COVID-19 June 2020](https://www.rewterz.com/articles/analysis-on-sidewinder-apt-group-covid-19)


[^23]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^24]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^25]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^26]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^27]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^28]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^29]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^30]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^31]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^32]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^33]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^34]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^35]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^36]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^37]: [netlab360 rotajakiro vs oceanlotus](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)


[^38]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^39]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^40]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^41]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)


[^42]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)


[^43]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^44]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


[^45]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^46]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^47]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^48]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^49]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^50]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^51]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^52]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^53]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^54]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^55]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^56]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)


[^57]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^58]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^59]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^60]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^61]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^62]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^63]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^64]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^65]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)


[^66]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^67]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^68]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^69]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^70]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^71]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^72]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^73]: [Intego Shlayer Feb 2018](https://www.intego.com/mac-security-blog/osxshlayer-new-mac-malware-comes-out-of-its-shell/)


[^74]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^75]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^76]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^77]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^78]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^79]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^80]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^81]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^82]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^83]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^84]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^85]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^86]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^87]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^88]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^89]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^90]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^91]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^92]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^93]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)


[^94]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^95]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^96]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^97]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)


[^98]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)


[^99]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^100]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^101]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^102]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^103]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)


[^104]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^105]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^106]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^107]: [ESET Bad Rabbit](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)


[^108]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^109]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^110]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^111]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^112]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^113]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^114]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^115]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^116]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^117]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^118]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^119]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^120]: [ATT Felismus](https://levelblue.com/blogs/security-essentials/the-felismus-rat-powerful-threat-mysterious-purpose)


[^121]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^122]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^123]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^124]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^125]: [Guidepoint SUPERNOVA Dec 2020](https://www.guidepointsecurity.com/supernova-solarwinds-net-webshell-analysis/)


[^126]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^127]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^128]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^129]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^130]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^131]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^132]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^133]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^134]: [Microsoft DTC](https://technet.microsoft.com/en-us/library/cc759136(v=ws.10).aspx)


[^135]: [Group IB Silence Sept 2018](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)


[^136]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^137]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^138]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^139]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^140]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)


[^141]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^142]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^143]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^144]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^145]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^146]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^147]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^148]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^149]: [Kimsuky Malwarebytes](https://www.malwarebytes.com/blog/threat-intelligence/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor)


[^150]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)


[^151]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^152]: [Arghire LazyScripter](https://www.securityweek.com/new-lazyscripter-hacking-group-targets-airlines/)


[^153]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^154]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^155]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^156]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^157]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^158]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^159]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^160]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^161]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^162]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^163]: [Symantec Whitefly March 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)


[^164]: [Unit42 SUPERNOVA Dec 2020](https://unit42.paloaltonetworks.com/solarstorm-supernova/)


[^165]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^166]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^167]: [Mandiant APT42-charms](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)


[^168]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^169]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^170]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^171]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^172]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^173]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^174]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^175]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^176]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^177]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^178]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^179]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^180]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^181]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^182]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^183]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^184]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^185]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^186]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^187]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^188]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^189]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^190]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^191]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^192]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)


[^193]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^194]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^195]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^196]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^197]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^198]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^199]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^200]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^201]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^202]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^203]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^204]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^205]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^206]: [Proofpoint TA2541 February 2022](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)


[^207]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^208]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)


[^209]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^210]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^211]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^212]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^213]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^214]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^215]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^216]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^217]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^218]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^219]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^220]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^221]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^222]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^223]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^224]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^225]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^226]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^227]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^228]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^229]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^230]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)


[^231]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^232]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)


[^233]: [Trusteer Carberp October 2010](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)


[^234]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^235]: [BlackBerry_FIN7_April2024](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)


[^236]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^237]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^238]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^239]: [Medium Ali Salem Bumblebee April 2022](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)


[^240]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^241]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^242]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^243]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^244]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^245]: [Trendmicro_IcedID](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)


[^246]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^247]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^248]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^249]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^250]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^251]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^252]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^253]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)


[^254]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^255]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^256]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^257]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^258]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^259]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^260]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^261]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^262]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^263]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^264]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


[^265]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^266]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)


[^267]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^268]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^269]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^270]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^271]: [District Court of NY APT10 Indictment December 2018](https://www.justice.gov/opa/page/file/1122671/download)


[^272]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^273]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^274]: [Talos MuddyWater May 2019](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)


[^275]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^276]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^277]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^278]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^279]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^280]: [CrowdStrike SUNSPOT Implant January 2021](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)


[^281]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^282]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^283]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)


[^284]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^285]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^286]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)


[^287]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^288]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^289]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


[^290]: [SOCRadar INC Ransom January 2024](https://socradar.io/dark-web-profile-inc-ransom/)


[^291]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^292]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^293]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^294]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^295]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^296]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^297]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^298]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^299]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^300]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^301]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^302]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^303]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^304]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^305]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^306]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^307]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^308]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^309]: [Cymmetria Patchwork](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)


[^310]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^311]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^312]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^313]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^314]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^315]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^316]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^317]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^318]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^319]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^320]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^321]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^322]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^323]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^324]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^325]: [Microsoft DUBNIUM June 2016](https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/)


[^326]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^327]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^328]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^329]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^330]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^331]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^332]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


[^333]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^334]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^335]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^336]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)


[^337]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^338]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^339]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^340]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^341]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^342]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^343]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^344]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^345]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^346]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^347]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^348]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^349]: [CISA GRU29155 2024](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)


[^350]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^351]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^352]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^353]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^354]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^355]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^356]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^357]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^358]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^359]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^360]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^361]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^362]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^363]: [reed thiefquest ransomware analysis](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)


[^364]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^365]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^366]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^367]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^368]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^369]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^370]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^371]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^372]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^373]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)


[^374]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^375]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^376]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^377]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^378]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^379]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^380]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^381]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^382]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)


[^383]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^384]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^385]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^386]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^387]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^388]: [Kaspersky Poseidon Group](https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/)


[^389]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^390]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^391]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^392]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^393]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^394]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^395]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^396]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)


[^397]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)


[^398]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^399]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^400]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^401]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


[^402]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^403]: [ZScaler Hacking Team](http://research.zscaler.com/2015/08/chinese-cyber-espionage-apt-group.html)


[^404]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)


[^405]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^406]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^407]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^408]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


[^409]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^410]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^411]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^412]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^413]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)


[^414]: [BitDefender Chafer May 2020](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)


[^415]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^416]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^417]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^418]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^419]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^420]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)


[^421]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^422]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^423]: [Talos Rocke August 2018](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)


[^424]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)


[^425]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^426]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^427]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^428]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^429]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^430]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^431]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^432]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)


[^433]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^434]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^435]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^436]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^437]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^438]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^439]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^440]: [Unit 42 MechaFlounder March 2019](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)


[^441]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^442]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^443]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)


[^444]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^445]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^446]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^447]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^448]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^449]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^450]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^451]: [Aquasec Kubernetes Backdoor 2023](https://www.aquasec.com/blog/leveraging-kubernetes-rbac-to-backdoor-clusters/)


[^452]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^453]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^454]: [FBI IC3 Flash VOID MANTICORE Handala Hack March 2026](https://www.ic3.gov/CSA/2026/260320.pdf)


[^455]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^456]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^457]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)


[^458]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)


[^459]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^460]: [VenereCiscoTalos_Gamaredon_Mar2025](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)


[^461]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)


[^462]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^463]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^464]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^465]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^466]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^467]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^468]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^469]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^470]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^471]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^472]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^473]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^474]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^475]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^476]: [ComputerWeekly Strider](https://www.computerweekly.com/news/450302128/Strider-cyber-attack-group-deploying-malware-for-espionage)


[^477]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^478]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^479]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^480]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^481]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^482]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^483]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^484]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^485]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^486]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)


[^487]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^488]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^489]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^490]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^491]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^492]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^493]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^494]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^495]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^496]: [EnkiWhiteHat_KimsukyDOCSWAP_Dec2025](https://www.enki.co.kr/en/media-center/blog/kimsuky-distributing-malicious-mobile-app-via-qr-code)


[^497]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^498]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^499]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^500]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^501]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^502]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^503]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^504]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)


[^505]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^506]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^507]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^508]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^509]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^510]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^511]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^512]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^513]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^514]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)


[^515]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)


[^516]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)


[^517]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^518]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^519]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^520]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^521]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^522]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^523]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^524]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^525]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)


[^526]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^527]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^528]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^529]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^530]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^531]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^532]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^533]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^534]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^535]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^536]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^537]: [Microsoft Winnti Jan 2017](https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/)


[^538]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^539]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^540]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^541]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)


[^542]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)


[^543]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^544]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^545]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^546]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^547]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^548]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)


[^549]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)


[^550]: [DOJ FBI Handala Hack March 2026](https://www.justice.gov/opa/media/1431956/dl?inline)


[^551]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^552]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^553]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


