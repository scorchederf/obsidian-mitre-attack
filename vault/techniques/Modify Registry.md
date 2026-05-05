---
aliases: 
    - T1112
mitre-attack: https://attack.mitre.org/techniques/T1112
tactic: 
     - Defense Impairment - Persistence
platforms:
     - Windows
permissions required:
     - none
---

## T1112

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.<br><br>Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility [Reg](https://attack.mitre.org/software/S0075) may be used for local or remote Registry modification.[^90]  Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.<br><br>The Registry may be modified in order to hide configuration information or malicious payloads via [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027).[^281] [^498] [^39] [^136]  The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.[^37] [^281] <br><br>The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system.[^175]  Often [Valid Accounts](https://attack.mitre.org/techniques/T1078) are required, along with access to the remote system's [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) for RPC communication.<br><br>Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via [Reg](https://attack.mitre.org/software/S0075) or other utilities using the Win32 API.[^74]  Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.[^96] [^489] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[NPPSPY\|S1131]] | NPPSPY | [NPPSPY](https://attack.mitre.org/software/S1131) modifies the Registry to record the malicious listener for output from the Winlogon process.[^171]  |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^234]  |
| [[AADInternals\|S0677]] | AADInternals | [AADInternals](https://attack.mitre.org/software/S0677) can modify registry keys as part of setting a new pass-through authentication agent.[^322]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can delete its persistence mechanisms from the registry.[^222]  |
| [[CSPY Downloader\|S0527]] | CSPY Downloader | [CSPY Downloader](https://attack.mitre.org/software/S0527) can write to the Registry under the `%windir%` variable to execute tasks.[^145]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) has full control of the Registry, including the ability to modify it.[^461] [^433]  |
| [[CrackMapExec\|S0488]] | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488) can create a registry key using wdigest.[^46]  |
| [[Reg\|S0075]] | Reg | [Reg](https://attack.mitre.org/software/S0075) may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.[^90]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) has a command to edit the Registry on the victim’s machine.[^502] [^33]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) can modify registry entries.[^95]  |
| [[RCSession\|S0662]] | RCSession | [RCSession](https://attack.mitre.org/software/S0662) can write its configuration file to the Registry.[^407] [^264]  |
| [[SynAck\|S0242]] | SynAck | [SynAck](https://attack.mitre.org/software/S0242) can manipulate Registry keys.[^500]  |
| [[Exaramel for Windows\|S0343]] | Exaramel for Windows | [Exaramel for Windows](https://attack.mitre.org/software/S0343) adds the configuration to the Registry in XML format.[^34]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) has overwritten registry keys for persistence.[^458]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can perform Registry operations.[^492]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) can create registry keys to load driver files.[^463]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) has a command to create Registry entries for storing data under `HKEY_CURRENT_USER\SOFTWARE\Microsoft\WABE\DataPath`.[^239]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used Registry modifications as part of its installation routine.[^218] [^195]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can modify the Registry to save its configuration data as the following RC4-encrypted Registry key: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\GameCon`.[^378]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) modifies several Registry keys under `HKCU\Software\Microsoft\Internet Explorer\ PhishingFilter\` to disable phishing filters.[^58]  |
| [[Prestige\|S1058]] | Prestige | [Prestige](https://attack.mitre.org/software/S1058) has the ability to register new registry keys for a new extension handler via `HKCR\.enc` and `HKCR\enc\shell\open\command`.[^417]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) writes data into the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Pniumj`.[^89]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) uses `reg add` to add a Registry Run key for persistence.[^540]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can modify the Registry to store its configuration information.[^183]  |
| [[TinyTurla\|S0668]] | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) can set its configuration parameters in the Registry.[^520]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has modified Registry key values as part of its created service `DeviceSync`. [^342]  |
| [[HyperStack\|S0537]] | HyperStack | [HyperStack](https://attack.mitre.org/software/S0537) can add the name of its communication pipe to `HKLM\SYSTEM\\CurrentControlSet\\Services\\lanmanserver\\parameters\NullSessionPipes`.[^15]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) modifies conditions in the Registry and adds keys.[^212]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can set a Registry key to determine how long it has been installed and possibly to indicate the version number.[^112]  |
| [[TEARDROP\|S0560]] | TEARDROP | [TEARDROP](https://attack.mitre.org/software/S0560) modified the Registry to create a Windows service for itself on a compromised host.[^338]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can manipulate the system registry on a compromised host.[^351]  |
| [[PolyglotDuke\|S0518]] | PolyglotDuke | [PolyglotDuke](https://attack.mitre.org/software/S0518) can write encrypted JSON configuration files to the Registry.[^312]  |
| [[ShrinkLocker\|S1178]] | ShrinkLocker | [ShrinkLocker](https://attack.mitre.org/software/S1178) modifies various registry keys associated with system logon and BitLocker functionality to effectively lock-out users following disk encryption.[^52] [^363]  |
| [[BlackByte 2.0 Ransomware\|S1181]] | BlackByte 2.0 Ransomware | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) modifies the victim Registry to allow for elevated execution.[^256]  |
| [[HOPLIGHT\|S0376]] | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) has modified Managed Object Format (MOF) files within the Registry to run specific commands and create persistence on the system.[^431] 	 |
| [[WastedLocker\|S0612]] | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) can modify registry values within the `Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry key.[^509]  |
| [[RegDuke\|S0511]] | RegDuke | [RegDuke](https://attack.mitre.org/software/S0511) can create seemingly legitimate Registry key to store its encryption key.[^312]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) has a command to create, set, copy, or delete a specified Registry key or value.[^210] [^55]  |
| [[Naid\|S0205]] | Naid | [Naid](https://attack.mitre.org/software/S0205) creates Registry entries that store information about a created service and point to a malicious DLL dropped to disk.[^416]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) modifies the Registry to store an encoded configuration file in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Security`.[^219] [^382]  |
| [[TRANSLATEXT\|S1201]] | TRANSLATEXT | [TRANSLATEXT](https://attack.mitre.org/software/S1201) has modified the following registry key to install itself as the value, granting permission to install specified extensions: ` HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist`.[^459]   |
| [[Regin\|S0019]] | Regin | [Regin](https://attack.mitre.org/software/S0019) appears to have functionality to modify remote Registry information.[^386]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) has the ability to configure browser settings by modifying Registry entries under `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer`.[^142]  |
| [[BlackCat\|S1068]] | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) has the ability to add the following registry key on compromised networks to maintain persistence: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services \LanmanServer\Paramenters`[^39]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has added a registry key so future powershell.exe instances are spawned off-screen by default, and has removed all registry entries that are left behind during the dropper process.[^531]  |
| [[DarkComet\|S0334]] | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) adds a Registry value for its installation routine to the Registry Key `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System Enable LUA=”0”` and `HKEY_CURRENT_USER\Software\DC3_FEXEC`.[^329] [^321]  |
| [[CHIMNEYSWEEP\|S1149]] | CHIMNEYSWEEP | [CHIMNEYSWEEP](https://attack.mitre.org/software/S1149) can use the Windows Registry Environment key to change the `%windir%` variable to point to `c:\Windows` to enable payload execution.[^469] <br> |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can modify the Registry.[^306]  |
| [[DCSrv\|S1033]] | DCSrv | [DCSrv](https://attack.mitre.org/software/S1033) has created Registry keys for persistence.[^314]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) has registered two registry keys for shim databases.[^335]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) modifies several registry keys for persistence and UAC bypass.[^535]  |
| [[Conficker\|S0608]] | Conficker | [Conficker](https://attack.mitre.org/software/S0608) adds keys to the Registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services` and various other Registry locations.[^411] [^538]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) has modified registry keys for persistence.[^35]  |
| [[ROKRAT\|S0240]] | ROKRAT | [ROKRAT](https://attack.mitre.org/software/S0240) can modify the `HKEY_CURRENT_USER\Software\Microsoft\Office\` registry key so it can bypass the VB object model (VBOM) on a compromised host.[^333]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) can modify Registry values to store configuration strings, keylogger, and output of components.[^207]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has a module to create, delete, or modify Registry keys.[^506] [^285] [^99]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has deleted Registry keys to clean up its prior activity.[^141]   |
| [[NOOPLDR\|S9025]] | NOOPLDR | [NOOPLDR](https://attack.mitre.org/software/S9025) can store its payload in the Registry using a random hex string in `HKCU\SOFTWARE\Microsoft\COM3`.[^523]  |
| [[Explosive\|S0569]] | Explosive | [Explosive](https://attack.mitre.org/software/S0569) has a function to write itself to Registry values.[^289]   |
| [[Rover\|S0090]] | Rover | [Rover](https://attack.mitre.org/software/S0090) has functionality to remove Registry Run key persistence as a cleanup procedure.[^274]  |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can set and delete Registry keys.[^407]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can change the Registry values for Group Policy refresh time, to disable SmartScreen, and to disable Windows Defender.[^499] [^155] <br><br> |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a Registry subkey to register its created service, and can also uninstall itself later by deleting this value. [Hydraq](https://attack.mitre.org/software/S0203)'s backdoor also enables remote attackers to modify and delete subkeys.[^8] [^208]  |
| [[Ferocious\|S0679]] | Ferocious | [Ferocious](https://attack.mitre.org/software/S0679) has the ability to add a Class ID in the current user Registry hive to enable persistence mechanisms.[^353]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) has a command to modify a Registry key.[^172]  |
| [[Netwalker\|S0457]] | Netwalker | [Netwalker](https://attack.mitre.org/software/S0457) can add the following registry entry: `HKEY_CURRENT_USER\SOFTWARE\{8 random characters}`.[^82]  |
| [[Chaes\|S0631]] | Chaes | [Chaes](https://attack.mitre.org/software/S0631) can modify Registry values to stored information and establish persistence.[^116]   |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can remove persistence-related artifacts from the Registry.[^196]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to clear the Registry values in the Windows Startup folder that were previously set for persistence.[^123]       |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) can install encrypted configuration data under the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellCompatibility\Applications\laxhost.dll` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrintConfigs`.[^413]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can make modifications to the Regsitry for persistence.[^309]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has modified registry keys for persistence, to enable credential caching for credential access, and to facilitate lateral movement via RDP.[^258]  |
| [[Mori\|S1047]] | Mori | [Mori](https://attack.mitre.org/software/S1047) can write data to `HKLM\Software\NFC\IPA` and `HKLM\Software\NFC\` and delete Registry values.[^101] [^513]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) modifies an HKCU Registry key to store a session identifier unique to the compromised system as well as a pre-shared key used for encrypting and decrypting C2 communications.[^158]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can store configuration information in the Registry including the initialization vector and AES key needed to find and decrypt other [Uroburos](https://attack.mitre.org/software/S0022) components.[^163]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has written process names to the Registry, disabled IE browser features, deleted Registry keys, and changed the ExtendedUIHoverTime key.[^326] [^389] [^395] [^211]  |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has modified and deleted Registry keys to add services, and to disable Security Solutions such as Windows Defender.[^140]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) has modified the Registry to store its encrypted payload.[^113]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has modified registry keys of ComSysApp, Svchost, and xmlProv on the machine to gain persistence.[^277] [^100]   |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) has altered the InstallTime subkey.[^40]  |
| [[Shamoon\|S0140]] | Shamoon | Once [Shamoon](https://attack.mitre.org/software/S0140) has access to a network share, it enables the RemoteRegistry service on the target system. It will then connect to the system with RegConnectRegistryW and modify the Registry to disable UAC remote restrictions by setting `SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy` to 1.[^331] [^311] [^501]  |
| [[Black Basta\|S1070]] | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) has modified the Registry to enable itself to run in safe mode, to change the icons and file extensions for encrypted files, and to add the malware path for persistence.[^261] [^102] [^143] [^475] [^373] [^220]  |
| [[Catchamas\|S0261]] | Catchamas | [Catchamas](https://attack.mitre.org/software/S0261) creates three Registry keys to establish persistence by adding a [Windows Service](https://attack.mitre.org/techniques/T1543/003).[^233]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can modify the Run registry key.[^473]  |
| [[MegaCortex\|S0576]] | MegaCortex | [MegaCortex](https://attack.mitre.org/software/S0576) has added entries to the Registry for ransom contact information.[^44]  |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) has the ability to modify the Registry.[^305]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) can modify the Registry to set the ServiceDLL for a service created by the malware for persistence.[^529] <br> |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) can modify Registry keys under `HKCU\Software\Microsoft\[dllname]` to store configuration values. [Mosquito](https://attack.mitre.org/software/S0256) also modifies Registry keys under `HKCR\CLSID\...\InprocServer32` with a path to the launcher.[^352]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) can delete all Registry entries created during its execution.[^69]  |
| [[BlackByte Ransomware\|S1180]] | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) modifies the victim Registry to prevent system recovery.[^262]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can modify the Registry to store its configuration at `HKCU\Software\` under frequently changing names including `%USERNAME%` and `ToolTech-RM`.[^98]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) has modified the Registry to install a second-stage script in the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\sibot`.[^298]  |
| [[Tarrask\|S1011]] | Tarrask | [Tarrask](https://attack.mitre.org/software/S1011) is able to delete the Security Descriptor (`SD`) registry subkey in order to “hide” scheduled tasks.[^349]  |
| [[SOUNDBITE\|S0157]] | SOUNDBITE | [SOUNDBITE](https://attack.mitre.org/software/S0157) is capable of modifying the Registry.[^72]  |
| [[BADCALL\|S0245]] | BADCALL | [BADCALL](https://attack.mitre.org/software/S0245) modifies the firewall Registry key `SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfileGloballyOpenPorts\\List`.[^358]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) can store its configuration file in the Registry.[^390]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to modify Registry keys to disable crash dumps, colors for compressed files, and pop-up information about folders and desktop items.[^235] [^414] [^423]  |
| [[Pysa\|S0583]] | Pysa | [Pysa](https://attack.mitre.org/software/S0583) has modified the registry key “SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System” and added the ransom note.[^152]   |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) writes persistent configuration information to the victim host registry.[^14]  |
| [[LockBit 2.0\|S1199]] | LockBit 2.0 | [LockBit 2.0](https://attack.mitre.org/software/S1199) can create Registry keys to bypass UAC and for persistence.[^494]  |
| [[Pandora\|S0664]] | Pandora | [Pandora](https://attack.mitre.org/software/S0664) can write an encrypted token to the Registry to enable processing of remote commands.[^121]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can modify Registry values within `HKEY_CURRENT_USER\Software\Microsoft\Office\<Excel Version>\Excel\Security\AccessVBOM\` to enable the execution of additional code.[^325]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) had commands that allow an attacker to write or delete registry keys, and was observed stopping services by setting their `HKLM\SYSTEM\CurrentControlSet\services\\[service_name]\\Start` registry entries to value 4.[^73] [^30]  It also deleted previously-created Image File Execution Options (IFEO) Debugger registry values and registry keys related to HTTP proxy to clean up traces of its activity.[^85]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) can modify the Registry to save encryption parameters and system information.[^355] [^270] [^160] [^303] [^49]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) has the ability to modify the Registry key `HKCU\Software\ApplicationContainer\Appsw64` to store information regarding the C2 server and downloads.[^344] [^300] [^446]  |
| [[Samurai\|S1099]] | Samurai | The [Samurai](https://attack.mitre.org/software/S1099) loader component can create multiple Registry keys to force the svchost.exe process to load the final backdoor.[^228]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) has the ability to modify the Registry on compromised hosts using `RegDeleteValueA` and `RegCreateKeyExA`.[^515]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a Registry subkey that registers a new system device.[^169]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) has the capability to edit the Registry.[^487] [^276]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) can set the `KeepPrintedJobs` attribute for configured printers in `SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\Printers` to enable document stealing.[^251]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) can make arbitrary changes to registry keys based on provided input.[^260]  |
| [[LoJax\|S0397]] | LoJax | [LoJax](https://attack.mitre.org/software/S0397) has modified the Registry key `‘HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute’` from `‘autocheck autochk *’` to `‘autocheck autoche *’`.[^454]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) sets `HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load` to point to its executable.[^237]  |
| [[Pillowmint\|S0517]] | Pillowmint | [Pillowmint](https://attack.mitre.org/software/S0517) has modified the Registry key `HKLM\SOFTWARE\Microsoft\DRM` to store a malicious payload.[^255]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can write its configuration file to `Software\Classes\scConfig` in either `HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_USER`.[^121]  |
| [[Nerex\|S0210]] | Nerex | [Nerex](https://attack.mitre.org/software/S0210) creates a Registry subkey that registers a new service.[^480]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) can make modifications to Registry keys.[^114]   |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has modified the Registry as part of its UAC bypass process.[^203]   |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has made registry modifications to alter its behavior upon execution.[^296]  |
| [[CHOPSTICK\|S0023]] | CHOPSTICK | [CHOPSTICK](https://attack.mitre.org/software/S0023) may modify Registry keys to store RC4 encrypted configuration information.[^297]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) deletes the Registry key `HKCU\Software\Classes\Applications\rundll32.exe\shell\open`.[^127]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can create Registry entries to enable services to run.[^393]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) can create, delete, or modify a specified Registry key or value.[^61] [^131]  |
| [[HIUPAN\|S1230]] | HIUPAN | [HIUPAN](https://attack.mitre.org/software/S1230) has modified registry keys to ensure hidden files and extensions are not visible through the modification of `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced`.[^186] [^412]  |
| [[ComRAT\|S0126]] | ComRAT | [ComRAT](https://attack.mitre.org/software/S0126) has modified Registry values to store encrypted orchestrator code and payloads.[^132] [^533]   |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can write the process ID of a target process into the `HKEY_LOCAL_MACHINE\SOFTWARE\DDE\tpid` Registry value as part of its reflective loading activity.[^351]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has added and deleted keys from the Registry.[^81]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can make Registry modifications to share networked drives between elevated and non-elevated processes and to increase the number of outstanding network requests per client.[^334] [^104]  [Qilin](https://attack.mitre.org/software/S1242) can also modify `HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper` to enable posting of ransom messages.[^528] <br> |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can achieve persistence by modifying Registry key entries.[^88]   |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) can modify the Registry to store and maintain a configuration block and virtual file system.[^294] [^440]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can modify the Registry to store its configuration information in a randomly named subkey under `HKCU\Software\Microsoft`.[^80] [^156]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can modify the Registry to store its components.[^512]  |
| [[Waterbear\|S0579]] | Waterbear | [Waterbear](https://attack.mitre.org/software/S0579) has deleted certain values from the Registry to load a malicious DLL.[^252]   |
| [[PHOREAL\|S0158]] | PHOREAL | [PHOREAL](https://attack.mitre.org/software/S0158) is capable of manipulating the Registry.[^72]  |
| [[BitPaymer\|S0570]] | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) can set values in the Registry to help in execution.[^42]   |
| [[BACKSPACE\|S0031]] | BACKSPACE | [BACKSPACE](https://attack.mitre.org/software/S0031) is capable of deleting Registry keys, sub-keys, and values on a victim system.[^304]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) is capable of setting and deleting Registry values.[^12]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can create `HKCU\Software\Classes\Folder\shell\open\command` as a new registry key during privilege escalation.[^147] [^201]   |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) can add, modify, and/or delete registry keys. It has changed the proxy configuration of a victim system by modifying the `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` registry.[^109]  |
| [[Indrik Spider\|G0119]] | Indrik Spider | [Indrik Spider](https://attack.mitre.org/groups/G0119) has modified registry keys to prepare for ransomware execution and to disable common administrative utilities.[^248]  |
| [[LuminousMoth\|G1014]] | LuminousMoth | [LuminousMoth](https://attack.mitre.org/groups/G1014) has used malware that adds Registry keys for persistence.[^517] [^387]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has modified Registry keys to elevate privileges, maintain persistence and allow remote access.[^27]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has modified the Registry key `HKLM\System\CurrentControlSet\Control\SecurityProviders\WDigest` by setting the `UseLogonCredential` registry value to `1` in order to force credentials to be stored in clear text in memory. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also modified the WDigest registry key to allow plaintext credentials to be cached in memory.[^452] [^97]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has modified the Registry to perform multiple techniques through the use of [Reg](https://attack.mitre.org/software/S0075).[^92]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has used reg.exe to modify system configuration.[^206] [^71]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) modified the victim registry to enable the `RestrictedAdmin` mode feature, allowing for pass the hash behaviors to function via RDP.[^181]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has used malware to disable Windows Defender through modification of the Registry.[^153]  |
| [[APT42\|G1044]] | APT42 | [APT42](https://attack.mitre.org/groups/G1044) has modified Registry keys to maintain persistence.[^168]   |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) modified the registry using the command `reg add “HKEY_CURRENT_USER\Environment” /v UserInitMprLogonScript /t REG_SZ /d “[file path]”` for persistence.[^440]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has modified Registry settings for default file associations to enable all macros and for persistence.[^284] [^299] [^457] [^149]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also modified the registry entry for `HKCU:\Software\Microsoft\Windows\CurrentVersion\Run` registry key for persistence with the name WindowsSecurityCheck.[^105]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has modified Registry values to store payloads.[^327] [^346]  |
| [[Ember Bear\|G1003]] | Ember Bear | [Ember Bear](https://attack.mitre.org/groups/G1003) modifies registry values for anti-forensics and defense evasion purposes.[^301]  |
| [[Silence\|G0091]] | Silence | [Silence](https://attack.mitre.org/groups/G0091) can create, delete, or modify a specified Registry key or value.[^137]  |
| [[Patchwork\|G0040]] | Patchwork | A [Patchwork](https://attack.mitre.org/groups/G0040) payload deletes Resiliency Registry keys created by Microsoft Office applications in an apparent effort to trick users into thinking there were no issues during application runs.[^209]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | <br>[Volt Typhoon](https://attack.mitre.org/groups/G1017) has used `netsh` to create a PortProxy Registry modification on a compromised server running the Paessler Router Traffic Grapher (PRTG).[^307]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has modified Registry settings for security tools.[^292]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) uses a tool called CLEANTOAD that has the capability to modify Registry keys.[^111]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050)'s backdoor has modified the Windows Registry to store the backdoor's configuration. [^204] 	 |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) uses a Port 22 malware variant to modify several Registry keys.[^87]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) used a malware variant called GOODLUCK to modify the registry in order to steal credentials.[^178] [^223]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has deleted Registry keys during post compromise cleanup activities.[^154]  |
| [[Saint Bear\|G1031]] | Saint Bear | [Saint Bear](https://attack.mitre.org/groups/G1031) will leverage malicious Windows batch scripts to modify registry values associated with Windows Defender functionality.[^476]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has used Windows Registry modifications to specify a DLL payload.[^290] 	 |
| [[Gorgon Group\|G0078]] | Gorgon Group | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can deactivate security mechanisms in Microsoft Office by editing several keys and values under `HKCU\Software\Microsoft\Office\`.[^336]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) performed Registry modifications to escalate privileges and disable security tools.[^419] [^410]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool has created new Registry keys under `HKEY_CURRENT_USER\Software\Classes\` and `HKLM\SYSTEM\CurrentControlSet\services`.[^381] [^121]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has removed security settings for VBA macro execution by changing registry values `HKCU\Software\Microsoft\Office\&lt;version&gt;\&lt;product&gt;\Security\VBAWarnings` and `HKCU\Software\Microsoft\Office\&lt;version&gt;\&lt;product&gt;\Security\AccessVBOM`.[^122] [^308] [^418]  [Gamaredon Group](https://attack.mitre.org/groups/G0047) has also modified Registry keys to hide folders and system files and to add the C2 address under `HKEY_CURRENT_USER\Console\WindowsUpdate`. [^10]   |
| [[Lotus Blossom\|G0030]] | Lotus Blossom | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has installed tools such as [Sagerunex](https://attack.mitre.org/software/S1210) by writing them to the Windows registry.[^293]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Restrict Registry Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |





## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^8]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^9]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^10]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^11]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^12]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^13]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^14]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^15]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


[^16]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^17]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^18]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^19]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^20]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^21]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^22]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^23]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^24]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^25]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^26]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^27]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^28]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^29]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^30]: [Microsoft Analyzing Solorigate Dec 2020](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)


[^31]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^32]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^33]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^34]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^35]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^36]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^37]: [CISA LockBit 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a)


[^38]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^39]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)


[^40]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)


[^41]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^42]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^43]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^44]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^45]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^46]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


[^47]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^48]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^49]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^50]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^51]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^52]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)


[^53]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^54]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^55]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^56]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^57]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^58]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^59]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^60]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^61]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)


[^62]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^63]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^64]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^65]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^66]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^67]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^68]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^69]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^70]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^71]: [Trend Micro Earth Simnavaz October 2024](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)


[^72]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^73]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^74]: [Microsoft Reghide NOV 2006](https://docs.microsoft.com/sysinternals/downloads/reghide)


[^75]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^76]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^77]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^78]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^79]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^80]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)


[^81]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^82]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)


[^83]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^84]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^85]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^86]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^87]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^88]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)


[^89]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^90]: [Microsoft Reg](https://technet.microsoft.com/en-us/library/cc732643.aspx)


[^91]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^92]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^93]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^94]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^95]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)


[^96]: [TrendMicro POWELIKS AUG 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/poweliks-malware-hides-in-windows-registry/)


[^97]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^98]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^99]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^100]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^101]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^102]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)


[^103]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^104]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)


[^105]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^106]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^107]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^108]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^109]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^110]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^111]: [FireEye APT38 Oct 2018](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)


[^112]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^113]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^114]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)


[^115]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^116]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)


[^117]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^118]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^119]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^120]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^121]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^122]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^123]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^124]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^125]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^126]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^127]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^128]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^129]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^130]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^131]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^132]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^133]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^134]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^135]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^136]: [CISA Russian Gov Critical Infra 2018](https://www.cisa.gov/news-events/alerts/2018/03/15/russian-government-cyber-activity-targeting-energy-and-other-critical-infrastructure-sectors)


[^137]: [Group IB Silence Sept 2018](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)


[^138]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^139]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^140]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^141]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^142]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^143]: [Trend Micro Black Basta May 2022](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)


[^144]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^145]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^146]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^147]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)


[^148]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^149]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)


[^150]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^151]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^152]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)


[^153]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^154]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^155]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)


[^156]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^157]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^158]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^159]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^160]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^161]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^162]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^163]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^164]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^165]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^166]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^167]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^168]: [Mandiant APT42-charms](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)


[^169]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^170]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^171]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)


[^172]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^173]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^174]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^175]: [Microsoft Remote](https://technet.microsoft.com/en-us/library/cc754820.aspx)


[^176]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^177]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^178]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^179]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^180]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^181]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^182]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^183]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^184]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^185]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^186]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^187]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^188]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^189]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^190]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^191]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^192]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^193]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^194]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^195]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)


[^196]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^197]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^198]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^199]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^200]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^201]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^202]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^203]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^204]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^205]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^206]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^207]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^208]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^209]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^210]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^211]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^212]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^213]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^214]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^215]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^216]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^217]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^218]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)


[^219]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^220]: [Palo Alto Networks Black Basta August 2022](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)


[^221]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^222]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^223]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^224]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^225]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^226]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^227]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^228]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^229]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^230]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^231]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^232]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^233]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)


[^234]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^235]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)


[^236]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^237]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^238]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^239]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^240]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^241]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^242]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^243]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^244]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^245]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^246]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^247]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^248]: [Mandiant_UNC2165](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)


[^249]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^250]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^251]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^252]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


[^253]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^254]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^255]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)


[^256]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^257]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^258]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^259]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^260]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^261]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)


[^262]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^263]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^264]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)


[^265]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^266]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^267]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^268]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^269]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^270]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^271]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^272]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^273]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^274]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)


[^275]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^276]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^277]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^278]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^279]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^280]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^281]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^282]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^283]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^284]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)


[^285]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^286]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^287]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^288]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^289]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^290]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^291]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^292]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^293]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^294]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^295]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^296]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)


[^297]: [FireEye APT28](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^298]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^299]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^300]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^301]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^302]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^303]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^304]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^305]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^306]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^307]: [CISA AA24-038A PRC Critical Infrastructure February 2024](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)


[^308]: [CERT-EE Gamaredon January 2021](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)


[^309]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^310]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^311]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^312]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^313]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^314]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^315]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^316]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^317]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^318]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^319]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^320]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^321]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)


[^322]: [AADInternals Documentation](https://o365blog.com/aadinternals)


[^323]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^324]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^325]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^326]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^327]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^328]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^329]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)


[^330]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^331]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)


[^332]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^333]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)


[^334]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)


[^335]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^336]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


[^337]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^338]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)


[^339]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^340]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^341]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^342]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


[^343]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^344]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^345]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^346]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^347]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^348]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^349]: [Tarrask scheduled task](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)


[^350]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^351]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^352]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^353]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)


[^354]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^355]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)


[^356]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^357]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^358]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^359]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^360]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^361]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^362]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^363]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)


[^364]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^365]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^366]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^367]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^368]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^369]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^370]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^371]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^372]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^373]: [Deep Instinct Black Basta August 2022](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)


[^374]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^375]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^376]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^377]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^378]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^379]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^380]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^381]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^382]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^383]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^384]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^385]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^386]: [Kaspersky Regin](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)


[^387]: [Bitdefender LuminousMoth July 2021](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)


[^388]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^389]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)


[^390]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^391]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^392]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^393]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^394]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^395]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)


[^396]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^397]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^398]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^399]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^400]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^401]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^402]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^403]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^404]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^405]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^406]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^407]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^408]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^409]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^410]: [Cisco BlackByte 2024](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)


[^411]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)


[^412]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^413]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^414]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)


[^415]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^416]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)


[^417]: [Microsoft Prestige ransomware October 2022](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)


[^418]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^419]: [Picus BlackByte 2022](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)


[^420]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^421]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^422]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^423]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)


[^424]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^425]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^426]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^427]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^428]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^429]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^430]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^431]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^432]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^433]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^434]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^435]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^436]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^437]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^438]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^439]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^440]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^441]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^442]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^443]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^444]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^445]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^446]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)


[^447]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^448]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^449]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^450]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^451]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^452]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^453]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^454]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^455]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^456]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^457]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^458]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^459]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)


[^460]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^461]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)


[^462]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^463]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^464]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^465]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^466]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^467]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^468]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^469]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^470]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^471]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^472]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^473]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^474]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^475]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)


[^476]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^477]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^478]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^479]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^480]: [Symantec Nerex May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3445-99)


[^481]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^482]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^483]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^484]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^485]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^486]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^487]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)


[^488]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^489]: [SpectorOps Hiding Reg Jul 2017](https://posts.specterops.io/hiding-registry-keys-with-psreflect-b18ec5ac8353)


[^490]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^491]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^492]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^493]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^494]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)


[^495]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^496]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^497]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^498]: [Avaddon Ransomware 2021](https://arxiv.org/pdf/2102.04796)


[^499]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^500]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)


[^501]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)


[^502]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^503]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^504]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^505]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^506]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^507]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^508]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^509]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^510]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^511]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^512]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^513]: [CYBERCOM Iranian Intel Cyber January 2022](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)


[^514]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^515]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^516]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^517]: [Kaspersky LuminousMoth July 2021](https://securelist.com/apt-luminousmoth/103332/)


[^518]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^519]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^520]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)


[^521]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^522]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^523]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^524]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^525]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^526]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^527]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^528]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)


[^529]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^530]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^531]: [Unit 42 Inception November 2018](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)


[^532]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^533]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)


[^534]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^535]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)


[^536]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^537]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^538]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)


[^539]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^540]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^541]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^542]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^543]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


