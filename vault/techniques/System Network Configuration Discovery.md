---
aliases: 
    - T1016
mitre-attack: https://attack.mitre.org/techniques/T1016
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1016

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [Arp](https://attack.mitre.org/software/S0099), [ipconfig](https://attack.mitre.org/software/S0100)/[ifconfig](https://attack.mitre.org/software/S0101), [nbtstat](https://attack.mitre.org/software/S0102), and [route](https://attack.mitre.org/software/S0103).<br><br>Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. `show ip route`, `show ip interface`).[^149] [^264]  On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.[^497] <br><br>Adversaries may use the information from [System Network Configuration Discovery](https://attack.mitre.org/techniques/T1016) during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[ShimRatReporter\|S0445]] | ShimRatReporter | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host.[^375]  |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) has the ability to gather network configuration information.[^217]  |
| [[evilginx2\|S9003]] | evilginx2 | [evilginx2](https://attack.mitre.org/software/S9003) can capture information from each session with a victim including the public IP used to access the server and the user agent.[^578]  |
| [[ipconfig\|S0100]] | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |
| [[Arp\|S0099]] | Arp | [Arp](https://attack.mitre.org/software/S0099) can be used to display ARP configuration information on the host.[^342]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^201] [^283]  |
| [[ifconfig\|S0101]] | ifconfig | [ifconfig](https://attack.mitre.org/software/S0101) can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) can obtain the proxy settings of a compromised machine using `InternetQueryOptionA` and its IP address by running `nslookup myip.opendns.comresolver1.opendns.com\r\n`.[^245]  |
| [[PoshC2\|S0378]] | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate network adapter information.[^273]  |
| [[AsyncRAT\|S1087]] | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) can enumerate the NetBIOS name on targeted machines.[^240]  |
| [[Nltest\|S0359]] | Nltest | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate the parent domain of a local machine using `/parentdomain`.[^589]  |
| [[nbtstat\|S0102]] | nbtstat | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover local NetBIOS domain names. |
| [[NBTscan\|S0590]] | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) can be used to collect MAC addresses.[^610] [^176] 	 |
| [[route\|S0103]] | route | [route](https://attack.mitre.org/software/S0103) can be used to discover routing configuration information. |
| [[CrackMapExec\|S0488]] | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488) can collect DNS information from the targeted system.[^55]  |
| [[Koadic\|S0250]] | Koadic | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the contents of the IP routing table as well as information about the Windows domain.[^536] [^88]  |
| [[Pupy\|S0192]] | Pupy | [Pupy](https://attack.mitre.org/software/S0192) has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^156]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^36]  |
| [[AdFind\|S0552]] | AdFind | [AdFind](https://attack.mitre.org/software/S0552) can extract subnet information from Active Directory.[^78] [^180] [^443]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) obtains the IP address, location, and other relevant network information from the victim’s machine.[^559] [^103] [^349]  |
| [[cd00r\|S1204]] | cd00r | [cd00r](https://attack.mitre.org/software/S1204) can discover the IP for the network interface on the compromised device.[^304]  |
| [[PowerDuke\|S0139]] | PowerDuke | [PowerDuke](https://attack.mitre.org/software/S0139) has a command to get the victim's domain and NetBIOS name.[^111]  |
| [[EKANS\|S0605]] | EKANS | [EKANS](https://attack.mitre.org/software/S0605) can determine the domain of a compromised host.[^290]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has collected the victim machine's local IP address information and MAC address.[^379]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can enumerate the IP address on compromised systems.[^252]  |
| [[Pikabot\|S1145]] | Pikabot | [Pikabot](https://attack.mitre.org/software/S1145) gathers victim network information through commands such as `ipconfig` and `ipconfig /all`.[^246]  |
| [[Amadey\|S1025]] | Amadey | [Amadey](https://attack.mitre.org/software/S1025) can identify the IP address of a victim machine.[^522]  |
| [[Proxysvc\|S0238]] | Proxysvc | [Proxysvc](https://attack.mitre.org/software/S0238) collects the network adapter information and domain/username information based on current remote sessions.[^213]  |
| [[Orz\|S0229]] | Orz | [Orz](https://attack.mitre.org/software/S0229) can gather victim proxy information.[^566]  |
| [[Torisma\|S0678]] | Torisma | [Torisma](https://attack.mitre.org/software/S0678) can collect the local MAC address using `GetAdaptersInfo` as well as the system's IP address.[^151]  |
| [[NOKKI\|S0353]] | NOKKI | [NOKKI](https://attack.mitre.org/software/S0353) can gather information on the victim IP address.[^592]  |
| [[yty\|S0248]] | yty | [yty](https://attack.mitre.org/software/S0248) runs `ipconfig /all` and collects the domain name.[^191]  |
| [[Backdoor.Oldrea\|S0093]] | Backdoor.Oldrea | [Backdoor.Oldrea](https://attack.mitre.org/software/S0093) collects information about the Internet adapter configuration.[^177] [^328]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) collects the IP address of a compromised system.[^526]  |
| [[POWRUNER\|S0184]] | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) may collect network configuration data by running `ipconfig /all` on a victim.[^229]  |
| [[KOPILUWAK\|S1075]] | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) can use [Arp](https://attack.mitre.org/software/S0099) to discover a target's network configuration setttings.[^46]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to execute the `ipconfig` command.[^44]  |
| [[Emissary\|S0082]] | Emissary | [Emissary](https://attack.mitre.org/software/S0082) has the capability to execute the command `ipconfig /all`.[^83]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) gathers the MAC address of the victim’s machine.[^265]  |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) can obtain information about network parameters.[^353]  |
| [[Felismus\|S0171]] | Felismus | [Felismus](https://attack.mitre.org/software/S0171) collects the victim LAN IP address and sends it to the C2 server.[^161]  |
| [[GeminiDuke\|S0049]] | GeminiDuke | [GeminiDuke](https://attack.mitre.org/software/S0049) collects information on network settings and Internet proxy settings from the victim.[^361]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) has a module for network enumeration including determining IP addresses.[^468]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) collects the victim IP address, MAC address, as well as the victim account domain name.[^53]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has collected the local IP address, and external IP.[^59] [^271]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) can identify the IP address of a compromised host.[^320]  |
| [[xCaon\|S0653]] | xCaon | [xCaon](https://attack.mitre.org/software/S0653) has used the GetAdaptersInfo() API call to get the victim's MAC address.[^311]  |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) uses the `ipconfig /all` command to gather the victim’s IP address.[^621]  |
| [[OceanSalt\|S0346]] | OceanSalt | [OceanSalt](https://attack.mitre.org/software/S0346) can collect the victim’s IP address.[^144]  |
| [[Brave Prince\|S0252]] | Brave Prince | [Brave Prince](https://attack.mitre.org/software/S0252) gathers network configuration information as well as the ARP cache.[^360]  |
| [[AppleSeed\|S0622]] | AppleSeed | [AppleSeed](https://attack.mitre.org/software/S0622) can identify the IP of a targeted system.[^586]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can collect the IP address of a compromised host.[^203] [^125]  |
| [[J-magic\|S1203]] | J-magic | [J-magic](https://attack.mitre.org/software/S1203) can compare the host and remote IPs to check if a received packet is from the infected machine.[^261]  |
| [[iKitten\|S0278]] | iKitten | [iKitten](https://attack.mitre.org/software/S0278) will look for the current IP address.[^445]  |
| [[Gomir\|S1198]] | Gomir | [Gomir](https://attack.mitre.org/software/S1198) collects network information on infected systems such as listing interface names, MAC and IP addresses, and IPv6 addresses.[^489]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has the ability to identify the location, public IP address, and domain name on a compromised host.[^150]  |
| [[Olympic Destroyer\|S0365]] | Olympic Destroyer | [Olympic Destroyer](https://attack.mitre.org/software/S0365) uses API calls to enumerate the infected system's ARP table.[^50]  |
| [[BOLDMOVE\|S1184]] | BOLDMOVE | [BOLDMOVE](https://attack.mitre.org/software/S1184) enumerates network interfaces on the infected host.[^368]  |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) contains a command to collect the victim MAC address and LAN IP.[^129] [^181]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate infected system network information.[^523]  |
| [[Turian\|S0647]] | Turian | [Turian](https://attack.mitre.org/software/S0647) can retrieve the internal IP address of a compromised host.[^487]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) collects the MAC address of the target computer and other network configuration information.[^192] [^2]  |
| [[Action RAT\|S1028]] | Action RAT | [Action RAT](https://attack.mitre.org/software/S1028) has the ability to collect the MAC address of an infected host.[^288]  |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) can identify the domain of the compromised host.[^193]  |
| [[Prikormka\|S0113]] | Prikormka | A module in [Prikormka](https://attack.mitre.org/software/S0113) collects information from the victim about its IP addresses and MAC addresses.[^26]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has obtained information about local networks through the `ipconfig /all` command.[^467]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) can use an embedded script to check the IP address of potential victims visiting compromised websites.[^341]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can retrieve the IP address of a compromised host.[^339]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can identify the IP address and user domain on the target machine.[^300] [^531]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can retrieve network interface and proxy information.[^155]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can use the `GetAdaptersInfo` function to retrieve information about network adapters and the `GetIpNetTable` function to retrieve the IPv4 to physical network address mapping table.[^28]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has collected the victim’s external IP address.[^346]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has leveraged server-side client configurations to identify the public IP of the victim host.[^537]  |
| [[ShrinkLocker\|S1178]] | ShrinkLocker | [ShrinkLocker](https://attack.mitre.org/software/S1178) captures the IP address of the victim system and sends this to the attacker following encryption.[^62]  |
| [[Agent.btz\|S0092]] | Agent.btz | [Agent.btz](https://attack.mitre.org/software/S0092) collects the network adapter’s IP and MAC address as well as IP addresses of the network adapter’s default gateway, primary/secondary WINS, DHCP, and DNS servers, and saves them into a log file.[^112]  |
| [[Rifdoor\|S0433]] | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) has the ability to identify the IP address of the compromised host.[^104]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) gathers information on the IP forwarding table, MAC address, configured proxy, and network SSID.[^228] [^65]  |
| [[Naid\|S0205]] | Naid | [Naid](https://attack.mitre.org/software/S0205) collects the domain name from a compromised host.[^472]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) can gather the IP address from the victim's machine.[^433]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) gathers the victim's IP address and domain information, and then sends it to its C2 server.[^68]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) can collect network information, including the host IP address, DNS, and proxy information.[^454]  |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) can find the external IP address of the infected host.[^305]  |
| [[Neoichor\|S0691]] | Neoichor | [Neoichor](https://attack.mitre.org/software/S0691) can gather the IP address from an infected host.[^158]    |
| [[Conti\|S0575]] | Conti | [Conti](https://attack.mitre.org/software/S0575) can retrieve the ARP cache from the local system by using the `GetIpNetTable()` API call and check to ensure IP addresses it connects to are for local, non-Internet, systems.[^554]   |
| [[Diavol\|S0659]] | Diavol | [Diavol](https://attack.mitre.org/software/S0659) can enumerate victims' local and external IPs when registering with C2.[^613]  |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) used the `ipconfig /all` command and a batch script to gather network information.[^17]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) gathers the local IP address.[^573]  |
| [[Nightdoor\|S1147]] | Nightdoor | [Nightdoor](https://attack.mitre.org/software/S1147) gathers information on victim system network configuration such as MAC addresses.[^87]  |
| [[PowerShower\|S0441]] | PowerShower | [PowerShower](https://attack.mitre.org/software/S0441) has the ability to identify the current Windows domain of the infected host.[^608]  |
| [[Kazuar\|S0265]] | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) gathers information about network adapters.[^473]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can identify the MAC address on the target computer.[^354]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can collect the IP address of a compromised host.[^282]  |
| [[BlackEnergy\|S0089]] | BlackEnergy | [BlackEnergy](https://attack.mitre.org/software/S0089) has gathered information about network IP configurations using [ipconfig](https://attack.mitre.org/software/S0100).exe and about routing tables using [route](https://attack.mitre.org/software/S0103).exe.[^343] [^535]  |
| [[zwShell\|S0350]] | zwShell | [zwShell](https://attack.mitre.org/software/S0350) can obtain the victim IP address.[^347]  |
| [[Rising Sun\|S0448]] | Rising Sun | [Rising Sun](https://attack.mitre.org/software/S0448) can detect network adapter and IP address information.[^182] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can enumerate the IP address of a compromised host.[^593]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has captured victim IP address details.[^528]  |
| [[Avaddon\|S0640]] | Avaddon | [Avaddon](https://attack.mitre.org/software/S0640) can collect the external IP address of the victim.[^572]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) has the ability to enumerate the domain name of a victim, as well as if the host is a member of an Active Directory domain.[^428] [^345] [^479]  |
| [[Flagpro\|S0696]] | Flagpro | [Flagpro](https://attack.mitre.org/software/S0696) has been used to execute the `ipconfig /all` command on a victim system.[^114]  |
| [[SpicyOmelette\|S0646]] | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) can identify the IP of a compromised system.[^542]  |
| [[Green Lambert\|S0690]] | Green Lambert | [Green Lambert](https://attack.mitre.org/software/S0690) can obtain proxy information from a victim's machine using system environment variables.[^110] [^520]   |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) retrieved a list of the system's network interface after execution.[^337]  |
| [[KeyBoy\|S0387]] | KeyBoy | [KeyBoy](https://attack.mitre.org/software/S0387) can determine the public or WAN IP address for the system.[^186]  |
| [[Anchor\|S0504]] | Anchor | [Anchor](https://attack.mitre.org/software/S0504) can determine the public IP and location of a compromised host.[^455]  |
| [[Dyre\|S0024]] | Dyre | [Dyre](https://attack.mitre.org/software/S0024) has the ability to identify network settings on a compromised host.[^562]  |
| [[LunarLoader\|S1143]] | LunarLoader | [LunarLoader](https://attack.mitre.org/software/S1143) can verify the targeted host's DNS name which is then used in the creation of a decyrption key.[^421]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has captured victim IP address details of the targeted machine.[^584] [^109]  |
| [[Reaver\|S0172]] | Reaver | [Reaver](https://attack.mitre.org/software/S0172) collects the victim's IP address.[^122]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) can execute `ipconfig` on the victim’s machine.[^396] [^211] [^157]   |
| [[S-Type\|S0085]] | S-Type | [S-Type](https://attack.mitre.org/software/S0085) has used `ipconfig /all` on a compromised host.[^557]  |
| [[Duqu\|S0038]] | Duqu | The reconnaissance modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on network configuration.[^37]  |
| [[Remsec\|S0125]] | Remsec | [Remsec](https://attack.mitre.org/software/S0125) can obtain information about network configuration, including the routing table, ARP cache, and DNS cache.[^298]  |
| [[Sykipot\|S0018]] | Sykipot | [Sykipot](https://attack.mitre.org/software/S0018) may use `ipconfig /all` to gather system network configuration details.[^406]  |
| [[Explosive\|S0569]] | Explosive |  [Explosive](https://attack.mitre.org/software/S0569) has collected the MAC address from the victim's machine.[^325]   |
| [[Xbash\|S0341]] | Xbash | [Xbash](https://attack.mitre.org/software/S0341) can collect IP addresses and local intranet information from a victim’s machine.[^241]  |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) uses the `nbtstat -n` and `nbtstat -s` commands on the victim’s machine.[^481]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) gathers information about network adapters using the Win32 API call `GetAdaptersInfo`.[^570]  |
| [[Cuba\|S0625]] | Cuba | [Cuba](https://attack.mitre.org/software/S0625) can retrieve the ARP cache from the local system by using `GetIpNetTable`.[^24]   |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can enumerate the IP address of a compromised machine.[^464] [^132]  |
| [[NanHaiShu\|S0228]] | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) can gather information about the victim proxy server.[^566]  |
| [[NGLite\|S1106]] | NGLite | [NGLite](https://attack.mitre.org/software/S1106) identifies the victim system MAC and IPv4 addresses and uses these to establish a victim identifier.[^594]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) creates a backdoor through which remote attackers can retrieve IP addresses of compromised machines.[^10] [^227]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) has the ability to identify the domain of the compromised host.[^392]  |
| [[Caterpillar WebShell\|S0572]] | Caterpillar WebShell | [Caterpillar WebShell](https://attack.mitre.org/software/S0572) can gather the IP address from the victim's machine using the IP config command.[^188]   |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) executes `ipconfig /all` after initial communication is made to the remote server.[^492] [^230]  |
| [[USBferry\|S0452]] | USBferry | [USBferry](https://attack.mitre.org/software/S0452) can detect the infected machine's network topology using `ipconfig` and `arp`.[^547] 	 |
| [[WannaCry\|S0366]] | WannaCry | [WannaCry](https://attack.mitre.org/software/S0366) will attempt to determine the local network segment it is a part of.[^309]  |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to identify the IP of the infected host.[^121]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can discover the IP and MAC address of a targeted host.[^128] [^348]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) can collect the IP address of a victim machine.[^257]  |
| [[Pay2Key\|S0556]] | Pay2Key | [Pay2Key](https://attack.mitre.org/software/S0556) can identify the IP and MAC addresses of the compromised host.[^470]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can enumerate the MAC address of the compromised host.[^238]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) has the ability to use `ipconfig` to enumerate system network settings.[^218]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) gathers the current domain the victim system belongs to.[^171]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) will gather system information such as MAC and IP addresses.[^331]  |
| [[Sys10\|S0060]] | Sys10 | [Sys10](https://attack.mitre.org/software/S0060) collects the local IP address of the victim and sends it to the C2.[^426]  |
| [[Royal\|S1073]] | Royal | [Royal](https://attack.mitre.org/software/S1073) can enumerate IP addresses using `GetIpAddrTable`.[^48]  |
| [[Trojan.Karagany\|S0094]] | Trojan.Karagany | [Trojan.Karagany](https://attack.mitre.org/software/S0094) can gather information on the network configuration of a compromised host.[^544]  |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) has a command to get the public IP address from a system.[^243]   |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) can collect and send the local IP address, RDP information, and the network adapter physical address as a part of its C2 beacon.[^131]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) collects system network information using commands such as `ipconfig /all`.[^315]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) can collect the IP address from the victim’s machine.[^407]  |
| [[T9000\|S0098]] | T9000 | [T9000](https://attack.mitre.org/software/S0098) gathers and beacons the MAC and IP addresses during installation.[^92]  |
| [[Shamoon\|S0140]] | Shamoon | [Shamoon](https://attack.mitre.org/software/S0140) obtains the target's IP address and local network segment.[^352] [^580]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | A [JHUHUGIT](https://attack.mitre.org/software/S0044) variant gathers network interface card information.[^225]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) can collect IP information from the victim’s machine.[^576]  |
| [[down_new\|S0472]] | down_new | [down_new](https://attack.mitre.org/software/S0472) has the ability to identify the MAC address of a compromised host.[^193]  |
| [[Ixeshe\|S0015]] | Ixeshe | [Ixeshe](https://attack.mitre.org/software/S0015) enumerates the IP address, network proxy settings, and domain name from a victim's system.[^163]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) can enumeate information about victims’ systems including IP addresses.[^197]  |
| [[Catchamas\|S0261]] | Catchamas | [Catchamas](https://attack.mitre.org/software/S0261) gathers the Mac address, IP address, and the network adapter information from the victim’s machine.[^258]  |
| [[RogueRobin\|S0270]] | RogueRobin | [RogueRobin](https://attack.mitre.org/software/S0270) gathers the IP address and domain from the victim’s machine.[^431]  |
| [[BoxCaon\|S0651]] | BoxCaon | [BoxCaon](https://attack.mitre.org/software/S0651) can collect the victim's MAC address by using the `GetAdaptersInfo` API.[^311]  |
| [[SDBbot\|S0461]] | SDBbot | [SDBbot](https://attack.mitre.org/software/S0461) has the ability to determine the domain name and whether a proxy is configured on a compromised host.[^376]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) uses the `ipconfig` command.[^393]  |
| [[QUIETCANARY\|S1076]] | QUIETCANARY | [QUIETCANARY](https://attack.mitre.org/software/S1076) can identify the default proxy setting on a compromised host.[^46]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | [Grandoreiro](https://attack.mitre.org/software/S0531) can determine the IP and physical location of the compromised host via IPinfo.[^107]  |
| [[WellMail\|S0515]] | WellMail | [WellMail](https://attack.mitre.org/software/S0515) can identify the IP address of the victim system.[^326]  |
| [[LiteDuke\|S0513]] | LiteDuke | [LiteDuke](https://attack.mitre.org/software/S0513) has the ability to discover the proxy configuration of Firefox and/or Opera.[^354]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) checked if the compromised system is configured to use proxies.[^337]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can collect the IP address and NetBIOS name of an infected machine.[^47]  |
| [[Kobalos\|S0641]] | Kobalos | [Kobalos](https://attack.mitre.org/software/S0641) can record the IP address of the target machine.[^268]  |
| [[RATANKBA\|S0241]] | RATANKBA | [RATANKBA](https://attack.mitre.org/software/S0241) gathers the victim’s IP address via the `ipconfig -all` command.[^167] [^43]  |
| [[BADCALL\|S0245]] | BADCALL | [BADCALL](https://attack.mitre.org/software/S0245) collects the network adapter information.[^401]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) obtains the victim IP address.[^138]  |
| [[Ryuk\|S0446]] | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) has called `GetIpNetTable` in attempt to identify all mounted drives and hosts that have Address Resolution Protocol (ARP) entries.[^38] [^105]   |
| [[Pysa\|S0583]] | Pysa | [Pysa](https://attack.mitre.org/software/S0583) can perform network reconnaissance using the Advanced IP Scanner tool.[^168]  |
| [[Zebrocy\|S0251]] | Zebrocy | [Zebrocy](https://attack.mitre.org/software/S0251) runs the `ipconfig /all` command.[^262]  |
| [[SpeakUp\|S0374]] | SpeakUp | [SpeakUp](https://attack.mitre.org/software/S0374) uses the `ifconfig -a` command. [^226]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) can determine the NetBios name and  the IP addresses of targets machines including domain controllers.[^349] [^18]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) collected all network interface MAC addresses that are up and not loopback devices, as well as IP address, DHCP configuration, and domain information.[^80]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has the ability to identify the IP address of the compromised machine.[^49]  |
| [[Unknown Logger\|S0130]] | Unknown Logger | [Unknown Logger](https://attack.mitre.org/software/S0130) can obtain information about the victim's IP address.[^327]  |
| [[Valak\|S0476]] | Valak | [Valak](https://attack.mitre.org/software/S0476) has the ability to identify the domain and the MAC and IP addresses of an infected machine.[^385]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can run `C:\Windows\system32\cmd.exe /c cmd /c ipconfig /all 2>&1` to discover network settings.[^98]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can collect the network interface MAC address on the infected host.[^389] [^377]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) has collected the MAC address of a compromised host; it can also use `GetAdaptersInfo` to identify network adapters.[^548] [^598]  |
| [[Cyclops Blink\|S0687]] | Cyclops Blink | [Cyclops Blink](https://attack.mitre.org/software/S0687) can use the Linux API `if_nameindex` to gather network interface names.[^367] [^605]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) gathers the IP address from the victim’s machine.[^561]  |
| [[TajMahal\|S0467]] | TajMahal | [TajMahal](https://attack.mitre.org/software/S0467) has the ability to identify the MAC address on an infected host.[^281]  |
| [[Carbon\|S0335]] | Carbon | [Carbon](https://attack.mitre.org/software/S0335) can collect the IP address of the victims and other computers on the network using the commands: `ipconfig -all` `nbtstat -n`, and `nbtstat -s`.[^239] [^620]  |
| [[Calisto\|S0274]] | Calisto | [Calisto](https://attack.mitre.org/software/S0274) runs the `ifconfig` command to obtain the IP address from the victim’s machine.[^462]  |
| [[Pisloader\|S0124]] | Pisloader | [Pisloader](https://attack.mitre.org/software/S0124) has a command to collect the victim's IP address.[^565]  |
| [[Ramsay\|S0458]] | Ramsay | [Ramsay](https://attack.mitre.org/software/S0458) can use [ipconfig](https://attack.mitre.org/software/S0100) and [Arp](https://attack.mitre.org/software/S0099) to collect network configuration information, including routing information and ARP tables.[^8]  |
| [[Revenge RAT\|S0379]] | Revenge RAT | [Revenge RAT](https://attack.mitre.org/software/S0379) collects the IP address and MAC address from the system.[^459]  |
| [[MacMa\|S1016]] | MacMa | [MacMa](https://attack.mitre.org/software/S1016) can collect IP addresses from a compromised host.[^42]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can parse the `ProxyServer` string in the Registry to discover http proxies.[^245]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) has the capability to gather the IP address from the victim's machine.[^585]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can collected the IP address and domain name of a compromised host.[^126]   |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) collects network adapter and interface information by using the commands `ipconfig /all`, `arp -a` and `route print`. It also collects the system's MAC address with `getmac` and domain configuration with `net config workstation`.[^569]  |
| [[DEADEYE\|S1052]] | DEADEYE | [DEADEYE](https://attack.mitre.org/software/S1052) can discover the DNS domain name of a targeted system.[^504]  |
| [[LAMEHUG\|S9035]] | LAMEHUG | [LAMEHUG](https://attack.mitre.org/software/S9035) can enumerate network information on compromised hosts.[^596]  |
| [[Kessel\|S0487]] | Kessel | [Kessel](https://attack.mitre.org/software/S0487) has collected the DNS address of the infected host.[^305]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can enumerate the IP and domain of a target system.[^507]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has the ability to discover the domain name of the infected host.[^373]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) collects information about the network including the IP address and DHCP server.[^231]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) can report the IP of the compromised host to attacker controlled infrastructure.[^184]  |
| [[BabyShark\|S0414]] | BabyShark | [BabyShark](https://attack.mitre.org/software/S0414) has executed the `ipconfig /all` command.[^316] 	 |
| [[CreepySnail\|S1024]] | CreepySnail | [CreepySnail](https://attack.mitre.org/software/S1024) can use `getmac` and `Get-NetIPAddress` to enumerate network settings.[^414]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) collects the MAC address of victim devices.[^417]  |
| [[Manjusaka\|S1156]] | Manjusaka | [Manjusaka](https://attack.mitre.org/software/S1156) gathers information about current network connections, local and remote addresses associated with them, and associated processes.[^338]  |
| [[IceApple\|S1022]] | IceApple | The [IceApple](https://attack.mitre.org/software/S1022) [ifconfig](https://attack.mitre.org/software/S0101) module can iterate over all network interfaces on the host and retrieve the name, description, MAC address, DNS suffix, DNS servers, gateways, IPv4 addresses, and subnet masks.[^510]  |
| [[JPIN\|S0201]] | JPIN | [JPIN](https://attack.mitre.org/software/S0201) can obtain network information, including DNS, IP, and proxies.[^604]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) has the ability to collect the domain name on a compromised host.[^189]  |
| [[Mis-Type\|S0084]] | Mis-Type | [Mis-Type](https://attack.mitre.org/software/S0084) may create a file containing the results of the command `cmd.exe /c ipconfig /all`.[^557]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can use shell commands to discover network adapters and configuration.[^421]  |
| [[Octopus\|S0340]] | Octopus | [Octopus](https://attack.mitre.org/software/S0340) can collect the host IP address from the victim’s machine.[^471]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can accept a command line argument identifying specific IPs.[^322]  |
| [[SoreFang\|S0516]] | SoreFang | [SoreFang](https://attack.mitre.org/software/S0516) can collect the TCP/IP, DNS, DHCP, and network adapter configuration on a compromised host via `ipconfig.exe /all`.[^263]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) has the ability to collect the IP address of an infected host.[^115]  |
| [[Industroyer\|S0604]] | Industroyer | [Industroyer](https://attack.mitre.org/software/S0604)’s 61850 payload component enumerates connected network adapters and their corresponding IP addresses.[^450]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) can collect the MAC address and other information from a victim machine using `ipconfig/all`.[^91]  |
| [[Agent Tesla\|S0331]] | Agent Tesla | [Agent Tesla](https://attack.mitre.org/software/S0331) can collect the IP address of the victim machine and spawn instances of netsh.exe to enumerate wireless settings.[^307] [^96]   |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) can retrieve IP, network adapter configuration information, and domain from compromised hosts.[^350] [^392]  |
| [[ShadowPad\|S0596]] | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) has collected the domain name of the victim system.[^333]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) collects the external IP address from the system. [^432]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can use `net config workstation`, `arp -a`, `nslookup`, and `ipconfig /all` to gather network configuration information.[^452] [^448] [^169] [^540] [^130]  |
| [[jRAT\|S0283]] | jRAT | [jRAT](https://attack.mitre.org/software/S0283) can gather victim internal and external IPs.[^394]  |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) uses `ipconfig` to gather the IP address from the system.[^568]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) uses `ipconfig /all` and `route PRINT` to identify network adapter and interface information.[^609]  |
| [[OSInfo\|S0165]] | OSInfo | [OSInfo](https://attack.mitre.org/software/S0165) discovers the current domain information.[^496]  |
| [[Lizar\|S0681]] | Lizar | [Lizar](https://attack.mitre.org/software/S0681) has retrieved network information from a compromised host, such as the MAC address.[^402] [^518]  |
| [[Dtrack\|S0567]] | Dtrack | [Dtrack](https://attack.mitre.org/software/S0567) can collect the host's IP addresses using the `ipconfig` command.[^299] [^291]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) used a script to gather the IP address of the infected machine before sending to the C2.[^41]  |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can collect host IP information from the victim’s machine.[^153]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) has the capability to gather the victim's proxy information.[^308]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) collects MAC address and local IP address information from the victim.[^395]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has leveraged webservices to identify the public IP of the victim host.[^56]  |
| [[Small Sieve\|S1035]] | Small Sieve | [Small Sieve](https://attack.mitre.org/software/S1035) can obtain the IP address of a victim host.[^430]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has obtained host network details utilizing the command `cmd.exe /c ipconfig /all`.[^31]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [ipconfig](https://attack.mitre.org/software/S0100) to identify the network configuration of a victim machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used the PowerShell cmdlet `Get-ADComputer` to collect IP address data from Active Directory.[^571] [^106]  |
| [[Dragonfly\|G0035]] | Dragonfly | [Dragonfly](https://attack.mitre.org/groups/G0035) has used batch scripts to enumerate network information, including information about trusts, zones, and the domain.[^99]  |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has run `ipconfig /all` on a victim.[^127] [^207]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) malware IndiaIndia obtains and sends to its C2 server information about the first network interface card’s configuration, including IP address, gateways, subnet mask, DHCP information, and whether WINS is available.[^478] [^244]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has enumerated the host machine’s IP address.[^597]  |
| [[admin@338\|G0018]] | admin@338 | [admin@338](https://attack.mitre.org/groups/G0018) actors used the following command after exploiting a machine with [LOWBALL](https://attack.mitre.org/software/S0042) malware to acquire information about local networks: `ipconfig /all >> %temp%\download`[^336]  |
| [[APT42\|G1044]] | APT42 | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect network information.[^185]   |
| [[Earth Lusca\|G1006]] | Earth Lusca | [Earth Lusca](https://attack.mitre.org/groups/G1006) used the command `ipconfig` to obtain information about network configurations.[^499]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has used `ipconfig/all` and web beacons sent via email to gather network configuration information.[^521] [^409]  [Kimsuky](https://attack.mitre.org/groups/G0094) has also identified Host IP addresses leveraging the WMI class `Win32_NetworkAdapterConfiguration`.[^159]  |
| [[Play\|G1040]] | Play | <br>[Play](https://attack.mitre.org/groups/G1040) has used the information-stealing tool Grixba to enumerate network information.[^95] <br> |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover network configuration details using the `arp -a`, `nbtstat -n`, `net config`, `ipconfig /all`, and `route` commands, as well as [NBTscan](https://attack.mitre.org/software/S0590).[^481] [^387] [^146]  [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also retrieved registered RPC interface information from process memory.[^369]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has used [Ping](https://attack.mitre.org/software/S0097) and `tracert` for network discovery.[^91]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has collected the IP address and network adapter information from the victim’s machine.[^124] [^425]  |
| [[Ke3chang\|G0004]] | Ke3chang | [Ke3chang](https://attack.mitre.org/groups/G0004) has performed local network configuration discovery using `ipconfig`.[^108] [^277] [^158]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has executed multiple commands to enumerate network topology and settings including  `ipconfig`, `netsh interface firewall show all`, and `netsh interface portproxy show all`.[^335]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware gathers the victim's local IP address, MAC address, and external IP address.[^575] [^330] [^383]  |
| [[HAFNIUM\|G0125]] | HAFNIUM | [HAFNIUM](https://attack.mitre.org/groups/G0125) has collected IP information via IPInfo.[^555]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used malware to collect the victim’s IP address and domain name.[^564]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) used the `ipconfig /all` command to gather the IP address from the system.[^568]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has used `ipconfig` and `arp` to determine network configuration information.[^267]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also utilized SharpNBTScan to scan the victim environment.[^397]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has used [ipconfig](https://attack.mitre.org/software/S0100), [Ping](https://attack.mitre.org/software/S0097), and `tracert` to enumerate the IP address and network environment and settings of the local host.[^435]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has used several tools to scan for open NetBIOS nameservers and enumerate NetBIOS sessions.[^353]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has used scripts to collect the host's network topology.[^547] 	 |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) used an HTTP malware variant and a Port 22 malware variant to collect the MAC address and IP address from the victim’s machine.[^94]  |
| [[Moses Staff\|G1009]] | Moses Staff | [Moses Staff](https://attack.mitre.org/groups/G1009) has collected the domain name of a compromised network.[^356]  |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers the Address Resolution Protocol (ARP) table from the victim.[^344]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used [ipconfig](https://attack.mitre.org/software/S0100) for reconnaissance.[^438]  |
| [[APT41\|G0096]] | APT41 | [APT41](https://attack.mitre.org/groups/G0096) collected MAC addresses from victim machines.[^198] [^247]   |
| [[FIN13\|G1016]] | FIN13 | [FIN13](https://attack.mitre.org/groups/G1016) has used `nslookup` and `ipconfig` for network reconnaissance efforts. [FIN13](https://attack.mitre.org/groups/G1016) has also utilized a compromised Symantec Altiris console and LanDesk account to retrieve network information.[^310] [^372]  |
| [[GALLIUM\|G0093]] | GALLIUM | [GALLIUM](https://attack.mitre.org/groups/G0093) used `ipconfig /all` to obtain information about the victim network configuration. The group also ran a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers.[^318]  |
| [[Scattered Spider\|G1015]] | Scattered Spider | [Scattered Spider](https://attack.mitre.org/groups/G1015) has used network reconnaissance commands for discovery including `ping` and `nltest`.[^14]    |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used malware to collect information on network interfaces, including the MAC address.[^332]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) used `ipconfig` to gather network configuration information.[^116] [^456]  |
| [[BlackByte\|G1043]] | BlackByte | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Arp](https://attack.mitre.org/software/S0099) to pull system network information and identify connected devices.[^113] [^286]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use [NBTscan](https://attack.mitre.org/software/S0590) to discover vulnerable systems.[^503]  |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has gathered information on victim network configuration.[^237]  |
| [[APT3\|G0022]] | APT3 | A keylogging tool used by [APT3](https://attack.mitre.org/groups/G0022) gathers network information from the victim, including the MAC address, IP address, WINS, DHCP server, and gateway.[^496] [^40]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to enumerate proxy settings in the target environment.[^519]  |
| [[APT1\|G0006]] | APT1 | [APT1](https://attack.mitre.org/groups/G0006) used the `ipconfig /all` command to gather network configuration information.[^100]  |
| [[Naikon\|G0019]] | Naikon | [Naikon](https://attack.mitre.org/groups/G0019) uses commands such as `netsh interface show` to discover network interface settings.[^426]  |
| [[SideCopy\|G1008]] | SideCopy | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the IP address of a compromised host.[^288]  |
| [[Lotus Blossom\|G0030]] | Lotus Blossom | [Lotus Blossom](https://attack.mitre.org/groups/G0030) has used commands such as `ipconfig` and `netstat` to gather network information on compromised hosts.[^331]  |






### Sub-techniques
| ID | Name |
| --- | --- |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery |
| [[Wi-Fi Discovery\|T1016.002]] | Wi-Fi Discovery |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)


[^9]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^10]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)


[^11]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^12]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^13]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^14]: [Mandiant UNC3944 May 2025](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)


[^15]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^16]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^17]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)


[^18]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)


[^19]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^20]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^21]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^22]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^23]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^24]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)


[^25]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^26]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^27]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^28]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^29]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^30]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^31]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^32]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^33]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^34]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^35]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^36]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^37]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)


[^38]: [CrowdStrike Ryuk January 2019](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)


[^39]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^40]: [evolution of pirpi](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)


[^41]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^42]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)


[^43]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)


[^44]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^45]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^46]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^47]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^48]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)


[^49]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)


[^50]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)


[^51]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^52]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^53]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^54]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^55]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)


[^56]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^57]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^58]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^59]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^60]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^61]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^62]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)


[^63]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^64]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^65]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)


[^66]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^67]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^68]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^69]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^70]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^71]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^72]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^73]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^74]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^75]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^76]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^77]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^78]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)


[^79]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^80]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^81]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^82]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^83]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^84]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^85]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^86]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^87]: [ESET EvasivePanda 2024](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)


[^88]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^89]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^90]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^91]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^92]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)


[^93]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^94]: [Unit 42 C0d0so0 Jan 2016](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)


[^95]: [CISA Play Ransomware Advisory December 2023](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)


[^96]: [SentinelLabs Agent Tesla Aug 2020](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)


[^97]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^98]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^99]: [US-CERT TA18-074A](https://www.us-cert.gov/ncas/alerts/TA18-074A)


[^100]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)


[^101]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^102]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^103]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)


[^104]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^105]: [Bleeping Computer - Ryuk WoL](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)


[^106]: [Mandiant FIN12 Oct 2021](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)


[^107]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^108]: [Mandiant Operation Ke3chang November 2014](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)


[^109]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)


[^110]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)


[^111]: [Volexity PowerDuke November 2016](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)


[^112]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)


[^113]: [FBI BlackByte 2022](https://www.ic3.gov/CSA/2022/220211.pdf)


[^114]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)


[^115]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^116]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^117]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^118]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^119]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^120]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^121]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^122]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


[^123]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^124]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^125]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)


[^126]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^127]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^128]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^129]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^130]: [Microsoft Ransomware as a Service](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)


[^131]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^132]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)


[^133]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^134]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^135]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^136]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^137]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^138]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^139]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^140]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^141]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^142]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^143]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^144]: [McAfee Oceansalt Oct 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)


[^145]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^146]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^147]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^148]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^149]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^150]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^151]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)


[^152]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^153]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^154]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^155]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^156]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)


[^157]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^158]: [Microsoft NICKEL December 2021](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)


[^159]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^160]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^161]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^162]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^163]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)


[^164]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^165]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^166]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^167]: [Lazarus RATANKBA](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)


[^168]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)


[^169]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)


[^170]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^171]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^172]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^173]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^174]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^175]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^176]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)


[^177]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)


[^178]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^179]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^180]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)


[^181]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)


[^182]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^183]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^184]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^185]: [Mandiant APT42-charms](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)


[^186]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)


[^187]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^188]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^189]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^190]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^191]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)


[^192]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^193]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^194]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^195]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^196]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^197]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)


[^198]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^199]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^200]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^201]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^202]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^203]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^204]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^205]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^206]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^207]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)


[^208]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^209]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^210]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^211]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^212]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^213]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^214]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^215]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^216]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^217]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)


[^218]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^219]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^220]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^221]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^222]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^223]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^224]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^225]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^226]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


[^227]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^228]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^229]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^230]: [Accenture Dragonfish Jan 2018](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)


[^231]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^232]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^233]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^234]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^235]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^236]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^237]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^238]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


[^239]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)


[^240]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)


[^241]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)


[^242]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^243]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^244]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^245]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^246]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)


[^247]: [Group IB APT 41 June 2021](https://www.group-ib.com/blog/colunmtk-apt41/)


[^248]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^249]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^250]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^251]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^252]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^253]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^254]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^255]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^256]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^257]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)


[^258]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)


[^259]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^260]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^261]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)


[^262]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^263]: [CISA SoreFang July 2016](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)


[^264]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)


[^265]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^266]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^267]: [Avira Mustang Panda January 2020](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)


[^268]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)


[^269]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^270]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^271]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^272]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^273]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)


[^274]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^275]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^276]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^277]: [NCC Group APT15 Alive and Strong](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)


[^278]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^279]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^280]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^281]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)


[^282]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^283]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)


[^284]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^285]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^286]: [Microsoft BlackByte 2023](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)


[^287]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^288]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


[^289]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^290]: [IBM Ransomware Trends September 2020](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)


[^291]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)


[^292]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^293]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^294]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^295]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^296]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^297]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^298]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^299]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)


[^300]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^301]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^302]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^303]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^304]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)


[^305]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^306]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^307]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)


[^308]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^309]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)


[^310]: [Mandiant FIN13 Aug 2022](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)


[^311]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^312]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^313]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^314]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^315]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^316]: [Unit42 BabyShark Feb 2019](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)


[^317]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^318]: [Cybereason Soft Cell June 2019](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)


[^319]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^320]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^321]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^322]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)


[^323]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^324]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^325]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)


[^326]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)


[^327]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^328]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)


[^329]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^330]: [DFIR Report APT35 ProxyShell March 2022](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)


[^331]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)


[^332]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^333]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)


[^334]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^335]: [Joint Cybersecurity Advisory Volt Typhoon June 2023](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)


[^336]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)


[^337]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^338]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)


[^339]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^340]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^341]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)


[^342]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)


[^343]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)


[^344]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^345]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)


[^346]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^347]: [McAfee Night Dragon](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)


[^348]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^349]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)


[^350]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^351]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^352]: [Palo Alto Shamoon Nov 2016](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)


[^353]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^354]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^355]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^356]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^357]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^358]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^359]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^360]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)


[^361]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


[^362]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^363]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^364]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^365]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^366]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^367]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)


[^368]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)


[^369]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^370]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^371]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^372]: [Sygnia Elephant Beetle Jan 2022](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)


[^373]: [FSecure Lokibot November 2019](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)


[^374]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^375]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^376]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)


[^377]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^378]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^379]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^380]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^381]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^382]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^383]: [DFIR Phosphorus November 2021](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)


[^384]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^385]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)


[^386]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^387]: [Symantec Waterbug Jun 2019](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)


[^388]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^389]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^390]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^391]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^392]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^393]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^394]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)


[^395]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^396]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^397]: [Unit42 Chinese VSCode 06 September 2024](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)


[^398]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^399]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^400]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^401]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^402]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^403]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^404]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^405]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^406]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)


[^407]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)


[^408]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^409]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^410]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^411]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^412]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^413]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^414]: [Microsoft POLONIUM June 2022](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)


[^415]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^416]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^417]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^418]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^419]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^420]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^421]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^422]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^423]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^424]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^425]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^426]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^427]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^428]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)


[^429]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^430]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


[^431]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^432]: [Cofense Astaroth Sept 2018](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)


[^433]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)


[^434]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^435]: [NCC Group Chimera January 2021](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)


[^436]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^437]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^438]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^439]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^440]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^441]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^442]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^443]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)


[^444]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^445]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^446]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^447]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^448]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^449]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^450]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^451]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^452]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)


[^453]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^454]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^455]: [Medium Anchor DNS July 2020](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)


[^456]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^457]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^458]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^459]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)


[^460]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^461]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^462]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)


[^463]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^464]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^465]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^466]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^467]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)


[^468]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)


[^469]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^470]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)


[^471]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)


[^472]: [Symantec Naid June 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)


[^473]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)


[^474]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^475]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^476]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^477]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^478]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^479]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)


[^480]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^481]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^482]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^483]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^484]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^485]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^486]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^487]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)


[^488]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^489]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)


[^490]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^491]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^492]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^493]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^494]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^495]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^496]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)


[^497]: [Trellix Rnasomhouse 2024](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)


[^498]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^499]: [TrendMicro EarthLusca 2022](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)


[^500]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^501]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^502]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^503]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^504]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^505]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^506]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^507]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^508]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^509]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^510]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^511]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^512]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^513]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^514]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^515]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^516]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^517]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^518]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)


[^519]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^520]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)


[^521]: [Talos Kimsuky Nov 2021](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)


[^522]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)


[^523]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^524]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^525]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^526]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^527]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^528]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^529]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^530]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^531]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^532]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^533]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^534]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^535]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)


[^536]: [Github Koadic](https://github.com/offsecginger/koadic)


[^537]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^538]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^539]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^540]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^541]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^542]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)


[^543]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^544]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)


[^545]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^546]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^547]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^548]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)


[^549]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^550]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^551]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^552]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^553]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^554]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)


[^555]: [Rapid7 HAFNIUM Mar 2021](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)


[^556]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^557]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)


[^558]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^559]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^560]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^561]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)


[^562]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)


[^563]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^564]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^565]: [Palo Alto DNS Requests](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^566]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^567]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^568]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^569]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)


[^570]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^571]: [Sophos New Ryuk Attack October 2020](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)


[^572]: [Awake Security Avaddon](https://awakesecurity.com/blog/threat-hunting-for-avaddon-ransomware/)


[^573]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^574]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^575]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^576]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^577]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^578]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)


[^579]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^580]: [McAfee Shamoon December 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)


[^581]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^582]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^583]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^584]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^585]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^586]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)


[^587]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^588]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^589]: [Nltest Manual](https://ss64.com/nt/nltest.html)


[^590]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^591]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^592]: [Unit 42 NOKKI Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)


[^593]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^594]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)


[^595]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^596]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


[^597]: [Trend Micro TeamTNT](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)


[^598]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^599]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^600]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^601]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^602]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^603]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^604]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^605]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)


[^606]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^607]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^608]: [Kaspersky Cloud Atlas August 2019](https://securelist.com/recent-cloud-atlas-activity/92016/)


[^609]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^610]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)


[^611]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^612]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^613]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)


[^614]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^615]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^616]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^617]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^618]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^619]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^620]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)


[^621]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^622]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^623]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^624]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


