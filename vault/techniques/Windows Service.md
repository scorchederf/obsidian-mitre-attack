---
aliases: 
    - T1543.003
mitre-attack: https://attack.mitre.org/techniques/T1543/003
tactic: 
     - Persistence - Privilege Escalation
platforms:
     - Windows
permissions required:
     - none
---

## T1543.003

Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence. When Windows boots up, it starts programs or applications called services that perform background system functions.[^346]  Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Windows Registry.<br><br>Adversaries may install a new service or modify an existing service to execute at startup in order to persist on a system. Service configurations can be set or modified using system utilities (such as sc.exe), by directly modifying the Registry, or by interacting directly with the Windows API. <br><br>Adversaries may also use services to install and execute malicious drivers. For example, after dropping a driver file (ex: `.sys`) to disk, the payload can be loaded and registered via [Native API](https://attack.mitre.org/techniques/T1106) functions such as `CreateServiceW()` (or manually via functions such as `ZwLoadDriver()` and `ZwSetValueKey()`), by creating the required service Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)), or by using command-line utilities such as `PnPUtil.exe`.[^98] [^362] [^32]  Adversaries may leverage these drivers as [Rootkit](https://attack.mitre.org/techniques/T1014)s to hide the presence of malicious activity on a system. Adversaries may also load a signed yet vulnerable driver onto a compromised machine (known as "Bring Your Own Vulnerable Driver" (BYOVD)) as part of [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).[^53] [^32] <br><br>Services may be created with administrator privileges but are executed under SYSTEM privileges, so an adversary may also use a service to escalate privileges. Adversaries may also directly start services through [Service Execution](https://attack.mitre.org/techniques/T1569/002).<br><br>To make detection analysis more challenging, malicious services may also incorporate [Masquerade Task or Service](https://attack.mitre.org/techniques/T1036/004) (ex: using a service and/or payload name related to a legitimate OS or benign software component). Adversaries may also create ‘hidden’ services (i.e., [Hide Artifacts](https://attack.mitre.org/techniques/T1564)), for example by using the `sc sdset` command to set service permissions via the Service Descriptor Definition Language (SDDL). This may hide a Windows service from the view of standard service enumeration methods such as `Get-Service`, `sc query`, and `services.exe`.[^410] [^19] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[SILENTTRINITY\|S0692]] | SILENTTRINITY | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish persistence by creating a new service.[^213]  |
| [[PowerSploit\|S0194]] | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.[^136] [^298]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can utilize built-in modules to modify service binaries and restore them to their original state.[^161]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can terminate, suspend, and resume a process by PID.[^382]  |
| [[PsExec\|S0029]] | PsExec | [PsExec](https://attack.mitre.org/software/S0029) can leverage Windows services to escalate privileges from administrator to SYSTEM with the `-s` argument.[^372]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) establishes persistence by creating an autostart service that allows it to run whenever the machine boots.[^87]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can create the services `httpsvc` and `w3esvc` for persistence .[^204]  |
| [[Wiarp\|S0206]] | Wiarp | [Wiarp](https://attack.mitre.org/software/S0206) creates a backdoor through which remote attackers can create a service.[^317]  |
| [[Exaramel for Windows\|S0343]] | Exaramel for Windows | The [Exaramel for Windows](https://attack.mitre.org/software/S0343) dropper creates and starts a Windows service named wsmprovav with the description “Windows Check AV.”[^36]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) uses a driver registered as a boot start service as the main load-point.[^413]  |
| [[TDTESS\|S0164]] | TDTESS | If running as administrator, [TDTESS](https://attack.mitre.org/software/S0164) installs itself as a new service named bmwappushservice to establish persistence.[^330]  |
| [[Emissary\|S0082]] | Emissary | [Emissary](https://attack.mitre.org/software/S0082) is capable of configuring itself as a service.[^71]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has registered itself as a system service in the Registry for automatic execution at system startup.[^409]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) can run in memory and register its payload as a Windows service.[^331]  |
| [[ZLib\|S0086]] | ZLib | [ZLib](https://attack.mitre.org/software/S0086) creates Registry keys to allow itself to run as various services.[^437]  |
| [[Bankshot\|S0239]] | Bankshot | [Bankshot](https://attack.mitre.org/software/S0239) can terminate a specific process by its process id.[^463] [^81]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) has created new services and modified existing services for persistence.[^256]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can create a service to establish persistence.[^306]  |
| [[AuditCred\|S0347]] | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) is installed as a new service on the system.[^476]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has created a malicious service DISMsrv to maintain persistence.[^206]  |
| [[Hannotog\|S1211]] | Hannotog | [Hannotog](https://attack.mitre.org/software/S1211) creates a new service for persistence.[^41]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has created a new PowerShell process using the `CreateProcessA` API.[^365]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can use services to establish persistence.[^306]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has created a service named `Microsoft Windows DeviceSync Service` at `HKLM\SYSTEM\CurrentControlSet\Services\DeviceSync\` to trigger execution when the system starts and to maintain persistence. [^299]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [CosmicDuke](https://attack.mitre.org/software/S0050) uses Windows services typically named "javamtsup" for persistence.[^268]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) chooses a service, drops a DLL file, and writes it to that serviceDLL Registry key.[^188]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has been observed creating new services to maintain persistence.[^207] [^450] [^80]   |
| [[TEARDROP\|S0560]] | TEARDROP | [TEARDROP](https://attack.mitre.org/software/S0560) ran as a Windows service from the `c:\windows\syswow64` folder.[^294] [^68]  |
| [[DUSTPAN\|S1158]] | DUSTPAN | [DUSTPAN](https://attack.mitre.org/software/S1158) can persist as a Windows Service in operations.[^408]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) has the ability to install itself as a service.[^266]  |
| [[SUGARUSH\|S1049]] | SUGARUSH | [SUGARUSH](https://attack.mitre.org/software/S1049) has created a service named `Service1` for persistence.[^9]  |
| [[WastedLocker\|S0612]] | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) created and established a service that runs until the encryption process is complete.[^456]   |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) can register a Windows service named CsPower as part of its execution chain, and a Windows service named clr_optimization_v2.0.51527_X86 to achieve persistence.[^53]  |
| [[Naid\|S0205]] | Naid | [Naid](https://attack.mitre.org/software/S0205) creates a new service to establish.[^367]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) installs a copy of itself in a randomly selected service, then overwrites the ServiceDLL entry in the service's Registry entry. Some [Volgmer](https://attack.mitre.org/software/S0180) variants also install .dll files as services with names generated by a list of hard-coded strings.[^481] [^194] [^336]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) can add a new service to ensure [PlugX](https://attack.mitre.org/software/S0013) persists on the system when delivered as another payload onto the system.[^56]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) has created a service when it is installed on the victim machine.[^394] 	 |
| [[Okrum\|S0439]] | Okrum | To establish persistence, [Okrum](https://attack.mitre.org/software/S0439) can install itself as a new service named NtmSsvc.[^352]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) can install itself as a new service.[^368]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used sc.exe to create a new service for the VirtualBox driver.[^274]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | One variant of [BlackEnergy](https://attack.mitre.org/software/S0089) creates a new service using either a hard-coded or randomly generated name.[^269]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) has established persistence by adding itself as a new service.[^271]  |
| [[DCSrv\|S1033]] | DCSrv | [DCSrv](https://attack.mitre.org/software/S1033) has created new services for persistence by modifying the Registry.[^278]  |
| [[ShimRat\|S0444]] | ShimRat | [ShimRat](https://attack.mitre.org/software/S0444) has installed a Windows service to maintain persistence on victim machines.[^291]  |
| [[Conficker\|S0608]] | Conficker | [Conficker](https://attack.mitre.org/software/S0608) copies itself into the `%systemroot%\system32` directory and registers as a service.[^361]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) installs a service pointing to a malicious DLL dropped to disk.[^174]  |
| [[Anchor\|S0504]] | Anchor | [Anchor](https://attack.mitre.org/software/S0504) can establish persistence by creating a service.[^272] 	 |
| [[SplatDropper\|S1232]] | SplatDropper | [SplatDropper](https://attack.mitre.org/software/S1232) has created a service to execute a payload.[^90]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) registers itself as a service by adding several Registry keys.[^94]  |
| [[BBSRAT\|S0127]] | BBSRAT | [BBSRAT](https://attack.mitre.org/software/S0127) can modify service configurations.[^366]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) can be added as a service to establish persistence. [PlugX](https://attack.mitre.org/software/S0013) also has a module to change service configurations as well as start, control, and delete services.[^258] [^173] [^276] [^196] [^56]  |
| [[Reaver\|S0172]] | Reaver | [Reaver](https://attack.mitre.org/software/S0172) installs itself as a new service.[^99]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has been modified to be used as a Windows service.[^130]   |
| [[Duqu\|S0038]] | Duqu | [Duqu](https://attack.mitre.org/software/S0038) creates a new service that loads a malicious driver when the system starts. When Duqu is active, the operating system believes that the driver is legitimate, as it has been signed with a valid private key.[^35]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can modify services by using the `OpenService` and `ChangeServiceConfig` functions.[^24]   |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can register itself as a system service to gain persistence.[^106]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can install system services for persistence.[^401]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates new services to establish persistence.[^11] [^186] [^187]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) configures itself as a service.[^385]  |
| [[WannaCry\|S0366]] | WannaCry | [WannaCry](https://attack.mitre.org/software/S0366) creates the service "mssecsvc2.0" with the display name "Microsoft Security Center (2.0) Service."[^73] [^121]  |
| [[Briba\|S0204]] | Briba | [Briba](https://attack.mitre.org/software/S0204) installs a service pointing to a malicious DLL dropped to disk.[^102]  |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | [TYPEFRAME](https://attack.mitre.org/software/S0263) variants can add malicious DLL modules as new services.[TYPEFRAME](https://attack.mitre.org/software/S0263) can also delete services from the victim’s machine.[^363]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) has registered a service, typically named `WerFaultSvc`, to decrypt and find a kernel driver and kernel driver loader to maintain persistence.[^144]  |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has created persistence through the DLL variant of the MDeployer toolkit by creating a service called irnagentd that launches after the system is rebooted in Safe Mode.[^129]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) can establish persistence by registering a malicious DLL as an alternative Print Processor which is loaded when the print spooler service starts.[^104]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has registered itself as a service using its export function.[^92]   |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) can create a new service to establish persistence.[^225] [^42]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) creates a new service named “ntssrv” to execute the payload. Newer versions create the "MaintenaceSrv" and "hdv_725x" services.[^275] [^252]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [JHUHUGIT](https://attack.mitre.org/software/S0044) has registered itself as a service to establish persistence.[^82]  |
| [[Black Basta\|S1070]] | Black Basta | [Black Basta](https://attack.mitre.org/software/S1070) can create a new service to establish persistence.[^236] [^105]  |
| [[Catchamas\|S0261]] | Catchamas | [Catchamas](https://attack.mitre.org/software/S0261) adds a new service named NetAdapter to establish persistence.[^212]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438)'s dispatcher can establish persistence by registering a new service.[^424]  |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) establishes persistence by installing a new service pointing to its DLL and setting the service to auto-start.[^270]  |
| [[NightClub\|S1090]] | NightClub | [NightClub](https://attack.mitre.org/software/S1090) has created a Windows service named `WmdmPmSp` to establish persistence.[^474]  |
| [[Sakula\|S0074]] | Sakula | Some [Sakula](https://attack.mitre.org/software/S0074) samples install themselves as services for persistence by calling WinExec with the `net start` argument.[^167]  |
| [[RawPOS\|S0169]] | RawPOS | [RawPOS](https://attack.mitre.org/software/S0169) installs itself as a service to maintain persistence.[^209] [^265] [^228]  |
| [[hcdLoader\|S0071]] | hcdLoader | [hcdLoader](https://attack.mitre.org/software/S0071) installs itself as a service for persistence.[^91] [^137]  |
| [[Nidiran\|S0118]] | Nidiran | [Nidiran](https://attack.mitre.org/software/S0118) can create a new service named msamger (Microsoft Security Accounts Manager).[^13]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) installs itself as a new service with automatic startup to establish persistence. The service checks every 60 seconds to determine if the malware is running; if not, it will spawn a new instance.[^113]  |
| [[CorKLOG\|S1235]] | CorKLOG | [CorKLOG](https://attack.mitre.org/software/S1235) has created a service to establish persistence.[^90]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) can load drivers by creating a new service using the `CreateServiceW` API.[^362]  |
| [[Pandora\|S0664]] | Pandora | [Pandora](https://attack.mitre.org/software/S0664) has the ability to gain system privileges through Windows services.[^112]  |
| [[FinFisher\|S0182]] | FinFisher | [FinFisher](https://attack.mitre.org/software/S0182) creates a new Windows service with the malicious executable for persistence.[^2] [^115]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can install a new service.[^127]  |
| [[Wingbird\|S0176]] | Wingbird | [Wingbird](https://attack.mitre.org/software/S0176) uses services.exe to register a new autostart service named "Audit Service" using a copy of the local lsass.exe file.[^139] [^357]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) can create a service at `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SvcHost` to trigger execution and maintain persistence.[^204]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) creates a Registry subkey that registers a new service. [PoisonIvy](https://attack.mitre.org/software/S0012) also creates a Registry entry modifying the Logical Disk Manager service to point to a malicious DLL dropped to disk.[^151]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) is capable of installing itself as a service.[^466]  |
| [[Carbon\|S0335]] | Carbon | [Carbon](https://attack.mitre.org/software/S0335) establishes persistence by creating a service and naming it based off the operating system version running on the current machine.[^195]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493) has established persistence by running in the background as an autostart service.[^453] 	 |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) has established persistence by running `sc.exe` and by setting the `WSearch` service to run automatically.[^198]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can create a service to establish persistence.[^112]  |
| [[TinyZBot\|S0004]] | TinyZBot | [TinyZBot](https://attack.mitre.org/software/S0004) can install as a Windows service for persistence.[^334]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) creates a new service named WmiApSrvEx to establish persistence.[^444]  |
| [[Nerex\|S0210]] | Nerex | [Nerex](https://attack.mitre.org/software/S0210) creates a Registry subkey that registers a new service.[^430]  |
| [[InnaputRAT\|S0259]] | InnaputRAT | Some [InnaputRAT](https://attack.mitre.org/software/S0259) variants create a new Windows service to establish persistence.[^164]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) can create a new service using the service parser function ProcessScCommand.[^343]   |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) sets its DLL file as a new service in the Registry to establish persistence.[^473]  |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) can install itself as a service.[^143]   |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to create the following Windows service to establish persistence on an infected host: `sc create Windowscarpstss binpath= "cmd.exe /c cscript.exe c:\\windows\\system32\\w7_1.wsf humpback_whale" start= "auto" obj= "LocalSystem"`.[^251]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604) can use an arbitrary system service to load at system boot for persistence and replaces the ImagePath registry value of a Windows service with a new backdoor binary.[^419]   |
| [[CozyCar\|S0046]] | CozyCar | One persistence mechanism used by [CozyCar](https://attack.mitre.org/software/S0046) is to register itself as a Windows service.[^318]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can remotely create a temporary service on a target host.[^426]  |
| [[Gelsemium\|S0666]] | Gelsemium | [Gelsemium](https://attack.mitre.org/software/S0666) can drop itself in `C:\Windows\System32\spool\prtprocs\x64\winprint.dll` as an alternative Print Processor to be loaded automatically when the spoolsv Windows service starts.[^459]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) can add a service called WBService to establish persistence.[^237]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) can automatically launch a Linux virtual machine as a service at startup if the AutoStart option is enabled in the VBoxVmService configuration file.[^38]  |
| [[BitPaymer\|S0570]] | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) has attempted to install itself as a service to maintain persistence.[^44]  |
| [[SLOTHFULMEDIA\|S0533]] | SLOTHFULMEDIA | [SLOTHFULMEDIA](https://attack.mitre.org/software/S0533) has created a service on victim machines named "TaskFrame" to establish persistence.[^100]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) has been installed as a Windows service.[^143]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has used vulnerable or signed drivers to modify security solutions on victim devices.[^29]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has installed [TrickBot](https://attack.mitre.org/software/S0266) as a service named ControlServiceA in order to establish persistence.[^403] [^89]   |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) created new Windows services and added them to the startup directories for persistence.[^292]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has used a compromised Domain Controller to create a service on a remote host.[^185] <br> |
| [[Lazarus Group\|G0032]] | Lazarus Group | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families install themselves as new services.[^374] [^290]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) created new Windows services for persistence that masqueraded as legitimate Windows services via name change.[^160]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has used malware that adds cryptocurrency miners as a service.[^125]  |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) created a service using the command `sc create “SysUpdate” binpath= “cmd /c start “[file path]””&&sc config “SysUpdate” start= auto&&net<br>start SysUpdate` for persistence.[^390]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has created new services for persistence.[^452] [^255]  |
| [[Cinnamon Tempest\|G1021]] | Cinnamon Tempest | [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) has created system services to establish persistence for deployed tooling.[^235]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) backdoor RoyalDNS established persistence through adding a service called `Nwsapagent`.[^223]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) has created new services to establish persistence.[^460]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has installed a new Windows service to establish persistence.[^440]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) modified Windows Services to ensure PowerShell scripts were loaded on the system. [APT32](https://attack.mitre.org/groups/G0050) also creates a Windows service to establish persistence.[^39] [^443] [^183]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has installed a service pointing to a malicious DLL dropped to disk.[^150]  |
| [[APT19\|G0073]] | APT19 | An [APT19](https://attack.mitre.org/groups/G0073) Port 22 malware variant registers itself as a service.[^79]  |
| [[DarkVishnya\|G0105]] | DarkVishnya | [DarkVishnya](https://attack.mitre.org/groups/G0105) created new services for shellcode loaders distribution.[^66]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) modified legitimate Windows services to install malware backdoors.[^157] [^199]  [APT41](https://attack.mitre.org/groups/G0096) created the StorSyncSvc service to provide persistence for [Cobalt Strike](https://attack.mitre.org/software/S0154).[^301]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has made their XMRIG payloads persistent as a Windows Service.[^261]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) modified multiple services on victim machines to enable encryption operations.[^145]  [BlackByte](https://attack.mitre.org/groups/G1043) has installed tools such as AnyDesk as a service on victim machines.[^231]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027)'s malware can create a new service, sometimes naming it after the config information, to gain persistence.[^335] [^103]  |
| [[Agrius\|G1030]] | Agrius | [Agrius](https://attack.mitre.org/groups/G1030) has deployed [IPsec Helper](https://attack.mitre.org/software/S1132) malware post-exploitation and registered it as a service for persistence.[^234]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that creates a new service for persistence.[^86]  |
| [[Lotus Blossom\|G0030]] | Lotus Blossom | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has configured tools such as [Sagerunex](https://attack.mitre.org/software/S1210) to run as Windows services.[^263]  |
| [[Carbanak\|G0008]] | Carbanak | [Carbanak](https://attack.mitre.org/groups/G0008) malware installs itself as a service to provide persistence and SYSTEM privileges.[^88]  |
| [[PROMETHIUM\|G0056]] | PROMETHIUM | [PROMETHIUM](https://attack.mitre.org/groups/G0056) has created new services and modified existing services for persistence.[^421]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Operating System Configuration\|M1028]] | Operating System Configuration | Ensure that Driver Signature Enforcement is enabled to restrict unsigned drivers from being installed.  |
| [[Code Signing\|M1045]] | Code Signing | Enforce registration and execution of only legitimately signed service drivers where possible. |
| [[Behavior Prevention on Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent an application from writing a signed vulnerable driver to the system.[^177]  On Windows 10 and 11, enable Microsoft Vulnerable Driver Blocklist to assist in hardening against third party-developed service drivers.[^158]    |
| [[User Account Management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations.  |
| [[Audit\|M1047]] | Audit | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them.  |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)


[^10]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^11]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^12]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^13]: [Symantec Backdoor.Nidiran](https://www.symantec.com/security_response/writeup.jsp?docid=2015-120123-5521-99)


[^14]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^15]: [Microsoft 4697 APR 2017](https://docs.microsoft.com/windows/security/threat-protection/auditing/event-4697)


[^16]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^17]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^18]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^19]: [SANS 2](https://www.sans.org/blog/defense-spotlight-finding-hidden-windows-services/)


[^20]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^21]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^22]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^23]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^24]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^25]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^26]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^27]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^28]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^29]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^30]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^31]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^32]: [Unit42 AcidBox June 2020](https://unit42.paloaltonetworks.com/acidbox-rare-malware/)


[^33]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^34]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^35]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)


[^36]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^37]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^38]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^39]: [ESET OceanLotus](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)


[^40]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^41]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^42]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)


[^43]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^44]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^45]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^46]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^47]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^48]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^49]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^50]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^51]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^52]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^53]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^54]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^55]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^56]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^57]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^58]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^59]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^60]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^61]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^62]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^63]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^64]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^65]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^66]: [Securelist DarkVishnya Dec 2018](https://securelist.com/darkvishnya/89169/)


[^67]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^68]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^69]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^70]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^71]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^72]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^73]: [LogRhythm WannaCry](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)


[^74]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^75]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^76]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^77]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^78]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^79]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^80]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)


[^81]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)


[^82]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^83]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^84]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^85]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^86]: [FireEye Operation Double Tap](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)


[^87]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)


[^88]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^89]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^90]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^91]: [Dell Lateral Movement](http://www.secureworks.com/resources/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems/)


[^92]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^93]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^94]: [Symantec Dyre June 2015](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)


[^95]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^96]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^97]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^98]: [Symantec W.32 Stuxnet Dossier](https://www.wired.com/images_blogs/threatlevel/2010/11/w32_stuxnet_dossier.pdf)


[^99]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


[^100]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)


[^101]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^102]: [Symantec Briba May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)


[^103]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^104]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^105]: [Avertium Black Basta June 2022](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)


[^106]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^107]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^108]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^109]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^110]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^111]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^112]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^113]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^114]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^115]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)


[^116]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^117]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^118]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^119]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^120]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^121]: [FireEye WannaCry 2017](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)


[^122]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^123]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^124]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^125]: [ATT TeamTNT Chimaera September 2020](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)


[^126]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^127]: [Cobalt Strike TTPs Dec 2017](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)


[^128]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^129]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^130]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^131]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^132]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^133]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^134]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^135]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^136]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^137]: [ThreatStream Evasion Analysis](https://www.threatstream.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


[^138]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^139]: [Microsoft SIR Vol 21](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)


[^140]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^141]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^142]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^143]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^144]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^145]: [Symantec BlackByte 2022](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)


[^146]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^147]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^148]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^149]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^150]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^151]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)


[^152]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^153]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^154]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^155]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^156]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^157]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^158]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^159]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^160]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^161]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^162]: [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)


[^163]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^164]: [ASERT InnaputRAT April 2018](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)


[^165]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^166]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^167]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^168]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^169]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^170]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^171]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^172]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^173]: [Lastline PlugX Analysis](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)


[^174]: [Rapid7 KeyBoy Jun 2013](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)


[^175]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^176]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^177]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^178]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^179]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^180]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^181]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^182]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^183]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^184]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^185]: [Symantec Crambus OCT 2023](https://www.security.com/threat-intelligence/crambus-middle-east-government)


[^186]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^187]: [Symantec Hydraq Persistence Jan 2010](https://www.symantec.com/connect/blogs/how-trojanhydraq-stays-your-computer)


[^188]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^189]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^190]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^191]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^192]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^193]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^194]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^195]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)


[^196]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^197]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^198]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^199]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^200]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^201]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^202]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^203]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^204]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^205]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^206]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)


[^207]: [US-CERT Emotet Jul 2018](https://www.us-cert.gov/ncas/alerts/TA18-201A)


[^208]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^209]: [Kroll RawPOS Jan 2017](https://www.kroll.com/en/insights/publications/malware-analysis-report-rawpos-malware)


[^210]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^211]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^212]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)


[^213]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^214]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^215]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^216]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^217]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^218]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^219]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^220]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^221]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^222]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^223]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^224]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^225]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)


[^226]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^227]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^228]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)


[^229]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^230]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^231]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^232]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^233]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^234]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^235]: [Sygnia Emperor Dragonfly October 2022](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)


[^236]: [Minerva Labs Black Basta May 2022](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)


[^237]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^238]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^239]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^240]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^241]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^242]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^243]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^244]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^245]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^246]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^247]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^248]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^249]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^250]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^251]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


[^252]: [Unit 42 Shamoon3 2018](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)


[^253]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^254]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^255]: [CISA AA20-301A Kimsuky](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)


[^256]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^257]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^258]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)


[^259]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^260]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^261]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^262]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^263]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^264]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^265]: [TrendMicro RawPOS April 2015](http://sjc1-te-ftp.trendmicro.com/images/tex/pdf/RawPOS%20Technical%20Brief.pdf)


[^266]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^267]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^268]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)


[^269]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^270]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^271]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^272]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^273]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^274]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


[^275]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^276]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^277]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^278]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^279]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^280]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^281]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^282]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^283]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^284]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^285]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^286]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^287]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^288]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^289]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^290]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^291]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^292]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^293]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^294]: [Check Point Sunburst Teardrop December 2020](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)


[^295]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^296]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^297]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^298]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^299]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


[^300]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^301]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^302]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^303]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^304]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^305]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^306]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^307]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^308]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^309]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^310]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^311]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^312]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^313]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^314]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^315]: [Microsoft Windows Event Forwarding FEB 2018](https://docs.microsoft.com/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection)


[^316]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^317]: [Symantec Wiarp May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)


[^318]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^319]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^320]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^321]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^322]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^323]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^324]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^325]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^326]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^327]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^328]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^329]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^330]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^331]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^332]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^333]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^334]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)


[^335]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^336]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^337]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^338]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^339]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^340]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^341]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^342]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^343]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^344]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^345]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^346]: [TechNet Services](https://technet.microsoft.com/en-us/library/cc772408.aspx)


[^347]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^348]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^349]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^350]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^351]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^352]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^353]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^354]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^355]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^356]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^357]: [Microsoft Wingbird Nov 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win32/Wingbird.A!dha)


[^358]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^359]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^360]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^361]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)


[^362]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)


[^363]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^364]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^365]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^366]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


[^367]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)


[^368]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^369]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^370]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^371]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^372]: [Russinovich Sysinternals](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)


[^373]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^374]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^375]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^376]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^377]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^378]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^379]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^380]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^381]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^382]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^383]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^384]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^385]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^386]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^387]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^388]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^389]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^390]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^391]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^392]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^393]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^394]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^395]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^396]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^397]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^398]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^399]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^400]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^401]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)


[^402]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^403]: [CrowdStrike Grim Spider May 2019](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)


[^404]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^405]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^406]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^407]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^408]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^409]: [TrendMicro PE_URSNIF.A2](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279)


[^410]: [SANS 1](https://www.sans.org/blog/red-team-tactics-hiding-windows-services/)


[^411]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^412]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^413]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^414]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^415]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^416]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^417]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^418]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^419]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)


[^420]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^421]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^422]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^423]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^424]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^425]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^426]: [NCC Group Black Basta June 2022](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)


[^427]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^428]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^429]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^430]: [Symantec Nerex May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3445-99)


[^431]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^432]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^433]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^434]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^435]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^436]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^437]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^438]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^439]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^440]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^441]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^442]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^443]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^444]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^445]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^446]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^447]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^448]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^449]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^450]: [Secureworks Emotet Nov 2018](https://www.secureworks.com/blog/lazy-passwords-become-rocket-fuel-for-emotet-smb-spreader)


[^451]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^452]: [Securelist Kimsuky Sept 2013](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)


[^453]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


[^454]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^455]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^456]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^457]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^458]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^459]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^460]: [Group IB Cobalt Aug 2017](https://www.group-ib.com/blog/cobalt)


[^461]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^462]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^463]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)


[^464]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^465]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^466]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^467]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^468]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^469]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^470]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^471]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^472]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^473]: [Microsoft Winnti Jan 2017](https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/)


[^474]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)


[^475]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^476]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^477]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^478]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^479]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^480]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^481]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)


[^482]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^483]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^484]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^485]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


