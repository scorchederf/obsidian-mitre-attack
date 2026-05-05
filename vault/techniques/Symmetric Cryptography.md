---
aliases: 
    - T1573.001
mitre-attack: https://attack.mitre.org/techniques/T1573/001
tactic: 
     - Command and Control
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## T1573.001

Adversaries may employ a known symmetric encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Symmetric encryption algorithms use the same key for plaintext encryption and ciphertext decryption. Common symmetric encryption algorithms include AES, DES, 3DES, Blowfish, and RC4.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can use AES-GCM-256 to encrypt a session key for C2 message exchange.[^20]  |
| [[FRP\|S1144]] | FRP | [FRP](https://attack.mitre.org/software/S1144) can use STCP (Secret TCP) with a preshared key to encrypt services exposed to public networks.[^266]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) uses AES with a hardcoded pre-shared key to encrypt network communication.[^472] [^123] [^39]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) uses a custom crypter leveraging Microsoft’s CryptoAPI to encrypt C2 traffic.[^480] Newer versions of [TrickBot](https://attack.mitre.org/software/S0266) have been known to use `bcrypt` to encrypt and digitally sign responses to their C2 server. [^171]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has encrypted its C2 traffic with RC4.[^316]  |
| [[Ninja\|S1100]] | Ninja | [Ninja](https://attack.mitre.org/software/S1100) can XOR and AES encrypt C2 messages.[^218]  |
| [[Pikabot\|S1145]] | Pikabot | Earlier [Pikabot](https://attack.mitre.org/software/S1145) variants use a custom encryption procedure leveraging multiple mechanisms including AES with multiple rounds of Base64 encoding for its command and control communication.[^213]  Later [Pikabot](https://attack.mitre.org/software/S1145) variants eliminate the use of AES and instead use RC4 encryption for transmitted information.[^195]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) can encrypt C2 requests and responses with RC4[^10]  |
| [[Torisma\|S0678]] | Torisma | [Torisma](https://attack.mitre.org/software/S0678) has encrypted its C2 communications using XOR and VEST-32.[^129]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) encodes the payload of system information sent to the command and control servers using a one byte 0xFF XOR key. [Stuxnet](https://attack.mitre.org/software/S0603) also uses a 31-byte long static byte string to XOR data sent to command and control servers. The servers use a different static key to encrypt replies to the implant.[^435]  |
| [[Downdelph\|S0134]] | Downdelph | [Downdelph](https://attack.mitre.org/software/S0134) uses RC4 to encrypt C2 responses.[^45]  |
| [[RotaJakiro\|S1078]] | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) encrypts C2 communication using a combination of AES, XOR, ROTATE encryption, and ZLIB compression.[^333]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) has the ability to use an RC4 key to encrypt communications to and from actor-controlled C2 servers.[^44]  |
| [[Emissary\|S0082]] | Emissary | The C2 server response to a beacon sent by a variant of [Emissary](https://attack.mitre.org/software/S0082) contains a 36-character GUID value that is used as an encryption key for subsequent network communications. Some variants of [Emissary](https://attack.mitre.org/software/S0082) use various XOR operations to encrypt C2 data.[^43]  |
| [[KEYMARBLE\|S0271]] | KEYMARBLE | [KEYMARBLE](https://attack.mitre.org/software/S0271) uses a customized XOR algorithm to encrypt C2 communications.[^230]  |
| [[TAMECAT\|S1193]] | TAMECAT | [TAMECAT](https://attack.mitre.org/software/S1193) has used AES to encrypt C2 traffic.[^313]  |
| [[CASTLETAP\|S1224]] | CASTLETAP | [CASTLETAP](https://attack.mitre.org/software/S1224) can receive a 9-byte XOR encrypted activation string in the payload of an ICMP echo request packet.[^103] <br> |
| [[RedLeaves\|S0153]] | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) has encrypted C2 traffic with RC4, previously using keys of 88888888 and babybear.[^297]  |
| [[Felismus\|S0171]] | Felismus | Some [Felismus](https://attack.mitre.org/software/S0171) samples use a custom encryption method for C2 traffic that utilizes AES and multiple keys.[^140]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) can send an AES encrypted check-in request to the C2 server.[^94] [^295]  |
| [[xCaon\|S0653]] | xCaon | [xCaon](https://attack.mitre.org/software/S0653) has encrypted data sent to the C2 server using a XOR key.[^268]   |
| [[PLAINTEE\|S0254]] | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) encodes C2 beacons using XOR.[^511]  |
| [[Nebulae\|S0630]] | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) can use RC4 and XOR to encrypt C2 communications.[^330]  |
| [[Lurid\|S0010]] | Lurid | [Lurid](https://attack.mitre.org/software/S0010) performs XOR encryption.[^137]  |
| [[TONESHELL\|S1239]] | TONESHELL | [TONESHELL](https://attack.mitre.org/software/S1239) has used RC4 encryption in C2 communications.[^147]  [TONESHELL](https://attack.mitre.org/software/S1239) variants used a randomly generated variable length (0x20 - 0x200 bytes) rolling XOR key to encrypt and decrypt network packets.[^262]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) can use RC4 to encrypt C2 communications.[^330]  |
| [[NETWIRE\|S0198]] | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) can use AES encryption for C2 data transferred.[^173]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has used encryption and compression algorithms to obfuscate the traffic between the system and C2 server, methods observed included RC4, AES, XOR with 0x5a, and LZO. [^320]  |
| [[HyperStack\|S0537]] | HyperStack | [HyperStack](https://attack.mitre.org/software/S0537) has used RSA encryption for C2 communications.[^17]  |
| [[HAMMERTOSS\|S0037]] | HAMMERTOSS | Before being appended to image files, [HAMMERTOSS](https://attack.mitre.org/software/S0037) commands are encrypted with a key composed of both a hard-coded value and a string contained on that day's tweet. To decrypt the commands, an investigator would need access to the intended malware sample, the day's tweet, and the image file containing the command.[^77]  |
| [[CosmicDuke\|S0050]] | CosmicDuke | [CosmicDuke](https://attack.mitre.org/software/S0050) contains a custom version of the RC4 algorithm that includes a programming error.[^288]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) encrypts communications using AES256.[^202]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) is known to use RSA keys for encrypting C2 traffic. [^464]  |
| [[SNUGRIDE\|S0159]] | SNUGRIDE | [SNUGRIDE](https://attack.mitre.org/software/S0159) encrypts C2 traffic using AES with a static key.[^209]  |
| [[THINCRUST\|S1223]] | THINCRUST | [THINCRUST](https://attack.mitre.org/software/S1223) can process RSA encryted C2 commands.[^103]  |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) has used AES to exfiltrate documents.[^164]  |
| [[Prikormka\|S0113]] | Prikormka | [Prikormka](https://attack.mitre.org/software/S0113) encrypts some C2 traffic with the Blowfish cipher.[^28]  |
| [[PUBLOAD\|S1228]] | PUBLOAD | [PUBLOAD](https://attack.mitre.org/software/S1228) has used RC4 encryption in C2 communications.[^26] [^293] [^147]  |
| [[SystemBC\|S9001]] | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) has encrypted its C2 traffic with RC4.[^406] [^13]  |
| [[PingPull\|S1031]] | PingPull | [PingPull](https://attack.mitre.org/software/S1031) can use AES, in cipher block chaining (CBC) mode padded with PKCS5, to encrypt C2 server communications.[^286]  |
| [[WellMess\|S0514]] | WellMess | [WellMess](https://attack.mitre.org/software/S0514) can encrypt HTTP POST data using RC6 and a dynamically generated AES key encrypted with a hard coded RSA public key.[^257] [^282] [^442]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) can use AES-CBC to encrypt data sent to its C2 server.[^134]   |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) can encrypt its C2 traffic with RC4.[^30]  |
| [[SombRAT\|S0615]] | SombRAT | [SombRAT](https://attack.mitre.org/software/S0615) has encrypted its C2 communications with AES.[^495]  |
| [[FlawedAmmyy\|S0381]] | FlawedAmmyy | [FlawedAmmyy](https://attack.mitre.org/software/S0381) has used SEAL encryption during the initial C2 handshake.[^42]  |
| [[Rifdoor\|S0433]] | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) has encrypted command and control (C2) communications with a stream cipher.[^90]  |
| [[InvisiMole\|S0260]] | InvisiMole | [InvisiMole](https://attack.mitre.org/software/S0260) uses variations of a simple XOR encryption routine for C&C communications.[^199]  |
| [[Volgmer\|S0180]] | Volgmer | [Volgmer](https://attack.mitre.org/software/S0180) uses a simple XOR cipher to encrypt traffic and files.[^208]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) has used RC4 to encrypt C2 traffic.[^142] [^62]  |
| [[RDAT\|S0495]] | RDAT | [RDAT](https://attack.mitre.org/software/S0495) has used AES ciphertext to encode C2 communications.[^415]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439) uses AES to encrypt network traffic. The key can be hardcoded or negotiated with the C2 server in the registration phase. [^376]  |
| [[Bonadan\|S0486]] | Bonadan | [Bonadan](https://attack.mitre.org/software/S0486) can XOR-encrypt C2 communications.[^263]  |
| [[RustyWater\|S9037]] | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) has encrypted encoded data with XOR before sending it to the C2 server.[^48]     |
| [[UBoatRAT\|S0333]] | UBoatRAT | [UBoatRAT](https://attack.mitre.org/software/S0333) encrypts instructions in its C2 network payloads using a simple XOR cipher.[^491]  |
| [[HTTPTroy\|S9007]] | HTTPTroy | [HTTPTroy](https://attack.mitre.org/software/S9007) has obfuscated request communications utilizing XOR encryption.[^133]  |
| [[NETEAGLE\|S0034]] | NETEAGLE | [NETEAGLE](https://attack.mitre.org/software/S0034) will decrypt resources it downloads with HTTP requests by using RC4 with the key "ScoutEagle."[^289]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can AES encrypt C2 communications.[^298]  |
| [[Lucifer\|S0532]] | Lucifer | [Lucifer](https://attack.mitre.org/software/S0532) can perform a decremental-xor encryption on the initial C2 request before sending it over the wire.[^245]  |
| [[Hi-Zor\|S0087]] | Hi-Zor | [Hi-Zor](https://attack.mitre.org/software/S0087) encrypts C2 traffic with a double XOR using two distinct single-byte keys.[^436]  |
| [[Chaos\|S0220]] | Chaos | [Chaos](https://attack.mitre.org/software/S0220) provides a reverse shell connection on 8338/TCP, encrypted via AES.[^285]  |
| [[LIGHTWIRE\|S1119]] | LIGHTWIRE | [LIGHTWIRE](https://attack.mitre.org/software/S1119) can RC4 encrypt C2 commands.[^139]  |
| [[CORESHELL\|S0137]] | CORESHELL | [CORESHELL](https://attack.mitre.org/software/S0137) C2 messages are encrypted with custom stream ciphers using six-byte or eight-byte keys.[^492]  |
| [[BBSRAT\|S0127]] | BBSRAT | [BBSRAT](https://attack.mitre.org/software/S0127) uses a custom encryption algorithm on data sent back to the C2 server over HTTP.[^388]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) can use RC4 encryption in C2 communications.[^477] [^468]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) variants reported on in 2014 and 2015 used a simple XOR cipher for C2. Some [Bisonal](https://attack.mitre.org/software/S0268) samples encrypt C2 communications with RC4.[^331] [^181] [^135]   |
| [[SeaDuke\|S0053]] | SeaDuke | [SeaDuke](https://attack.mitre.org/software/S0053) C2 traffic has been encrypted with RC4 and AES.[^224] [^358]  |
| [[Duqu\|S0038]] | Duqu | The [Duqu](https://attack.mitre.org/software/S0038) command and control protocol's data stream can be encrypted with AES-CBC.[^40]  |
| [[Explosive\|S0569]] | Explosive | [Explosive](https://attack.mitre.org/software/S0569) has encrypted communications with the RC4 method.[^161]   |
| [[Epic\|S0091]] | Epic | [Epic](https://attack.mitre.org/software/S0091) encrypts commands from the C2 server using a hardcoded key.[^396]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) uses AES to encrypt C2 traffic.[^466]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) can use AES to encrypt system information sent to the C2.[^192]  |
| [[Mongall\|S1026]] | Mongall | [Mongall](https://attack.mitre.org/software/S1026) has the ability to RC4 encrypt C2 communications.[^510]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | [LockBit 3.0](https://attack.mitre.org/software/S1202) can encrypt C2 communications with AES.[^471]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) has used a dynamic XOR key and custom XOR methodology for C2 communications.[^223]    |
| [[NGLite\|S1106]] | NGLite | [NGLite](https://attack.mitre.org/software/S1106) will use an AES encrypted channel for command and control purposes, in one case using the key `WHATswrongwithUu`.[^484]  |
| [[Carbanak\|S0030]] | Carbanak | [Carbanak](https://attack.mitre.org/software/S0030) encrypts the message body of HTTP traffic with RC2 (in CBC mode). [Carbanak](https://attack.mitre.org/software/S0030) also uses XOR with random keys for its communications.[^95] [^87]  |
| [[Hydraq\|S0203]] | Hydraq | [Hydraq](https://attack.mitre.org/software/S0203) C2 traffic is encrypted using bitwise NOT and XOR operations.[^198]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) encrypts exfiltrated data with RC4.[^405]  |
| [[Gazer\|S0168]] | Gazer | [Gazer](https://attack.mitre.org/software/S0168) uses custom encryption for C2 that uses 3DES.[^73] [^136]  |
| [[TSCookie\|S0436]] | TSCookie | [TSCookie](https://attack.mitre.org/software/S0436) has encrypted network communications with RC4.[^101]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) can send RC4 encrypted data over C2 channels.[^276] [^107] [^294]  |
| [[LODEINFO\|S9020]] | LODEINFO | [LODEINFO](https://attack.mitre.org/software/S9020) can encrypt C2 communication with a hardcoded (NV4HDOeOVyL) Vigenere cipher key.[^11]  |
| [[CharmPower\|S0674]] | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) can send additional modules over C2 encrypted with a simple substitution cipher.[^187]  |
| [[MuddyViper\|S9032]] | MuddyViper | [MuddyViper](https://attack.mitre.org/software/S9032) has the ability to encrypt C2 communication using AES-CBC using the CNG API, the key `0608101047106453101617106423101013101012101083109710108585106969`, and the initialization vector `0`.[^117]       |
| [[3PARA RAT\|S0066]] | 3PARA RAT | [3PARA RAT](https://attack.mitre.org/software/S0066) command and control commands are encrypted within the HTTP C2 channel using the DES algorithm in CBC mode with a key derived from the MD5 hash of the string HYF54&%9&jkMCXuiS. [3PARA RAT](https://attack.mitre.org/software/S0066) will use an 8-byte XOR key derived from the string HYF54&%9&jkMCXuiS if the DES decoding fails[^79]  |
| [[VIRTUALPIE\|S1218]] | VIRTUALPIE | [VIRTUALPIE](https://attack.mitre.org/software/S1218) can use a custom RC4 encrypted protocol for C2 communications.[^261] [^106]  |
| [[SMOKEDHAM\|S0649]] | SMOKEDHAM | [SMOKEDHAM](https://attack.mitre.org/software/S0649) has encrypted its C2 traffic with RC4.[^249]  |
| [[TAINTEDSCRIBE\|S0586]] | TAINTEDSCRIBE | [TAINTEDSCRIBE](https://attack.mitre.org/software/S0586) uses a Linear Feedback Shift Register (LFSR) algorithm for network encryption.[^38]  |
| [[Sys10\|S0060]] | Sys10 | [Sys10](https://attack.mitre.org/software/S0060) uses an XOR 0x1 loop to encrypt its C2 domain.[^360]  |
| [[BendyBear\|S0574]] | BendyBear | [BendyBear](https://attack.mitre.org/software/S0574) communicates to a C2 server over port 443 using modified RC4 and XOR-encrypted chunks.[^197]   |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can encrypt the data beneath its http2 or tcp encryption at the session layer with CAST-128, using a different key for incoming and outgoing data.[^154]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has encrypted C2 commands with AES-256.[^201]   |
| [[Bandook\|S0234]] | Bandook | [Bandook](https://attack.mitre.org/software/S0234) has used AES encryption for C2 communication.[^212]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) communications are RC4 encrypted.[^109]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) has used AES to encrypt C2 traffic.[^382]  |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) has used a custom TCP protocol with four-byte XOR for command and control (C2).[^410]  |
| [[gh0st RAT\|S0032]] | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) uses RC4 and XOR to encrypt C2 traffic.[^240]  |
| [[down_new\|S0472]] | down_new | [down_new](https://attack.mitre.org/software/S0472) has the ability to AES encrypt C2 communications.[^165]  |
| [[4H RAT\|S0065]] | 4H RAT | [4H RAT](https://attack.mitre.org/software/S0065) obfuscates C2 communication using a 1-byte XOR with the key 0xBE.[^79]  |
| [[Attor\|S0438]] | Attor | [Attor](https://attack.mitre.org/software/S0438) has encrypted data symmetrically using a randomly generated Blowfish (OFB) key which is encrypted with a public RSA key.[^448]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) uses a custom encryption algorithm, which consists of XOR and a stream that is similar to the Blum Blum Shub algorithm.[^327]  |
| [[RTM\|S0148]] | RTM | [RTM](https://attack.mitre.org/software/S0148) encrypts C2 traffic with a custom RC4 variant.[^74]  |
| [[QUIETCANARY\|S1076]] | QUIETCANARY | [QUIETCANARY](https://attack.mitre.org/software/S1076) can RC4 encrypt C2 communications.[^47]  |
| [[Derusbi\|S0021]] | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) obfuscates C2 traffic with variable 4-byte XOR keys.[^489]  |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) can use RC4 to encrypt C2 communications.[^497]  |
| [[Hikit\|S0009]] | Hikit | [Hikit](https://attack.mitre.org/software/S0009) performs XOR encryption.[^429]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) encodes C2 traffic with single-byte XOR keys.[^176]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can send C2 communications with XOR encryption.[^159]  |
| [[Kobalos\|S0641]] | Kobalos | [Kobalos](https://attack.mitre.org/software/S0641)'s post-authentication communication channel uses a 32-byte-long password with RC4 for inbound and outbound traffic.[^481] [^232]   |
| [[BADCALL\|S0245]] | BADCALL | [BADCALL](https://attack.mitre.org/software/S0245) encrypts C2 traffic using an XOR/ADD cipher.[^336]  |
| [[MoonWind\|S0149]] | MoonWind | [MoonWind](https://attack.mitre.org/software/S0149) encrypts C2 traffic using RC4 with a static key.[^118]  |
| [[HiddenFace\|S9023]] | HiddenFace |  [HiddenFace](https://attack.mitre.org/software/S9023) can use a randomly selected symmetric encryption algorithm for C2.[^284]  |
| [[Pandora\|S0664]] | Pandora | [Pandora](https://attack.mitre.org/software/S0664) has the ability to encrypt communications with D3DES.[^116]  |
| [[Cobalt Strike\|S0154]] | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) has the ability to use AES-256 symmetric encryption in CBC mode with HMAC-SHA-256 to encrypt task commands and XOR to encrypt shell code and configuration data.[^309]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) encrypted C2 traffic using a single-byte-XOR cipher.[^76]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has compressed network communications and encrypted them with a custom stream cipher.[^90] [^49]  |
| [[RIPTIDE\|S0003]] | RIPTIDE | [APT12](https://attack.mitre.org/groups/G0005) has used the [RIPTIDE](https://attack.mitre.org/software/S0003) RAT, which communicates over HTTP with a payload encrypted with RC4.[^505]  |
| [[Samurai\|S1099]] | Samurai | [Samurai](https://attack.mitre.org/software/S1099) can encrypt C2 communications with AES.[^218]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) encrypts data sent back to the C2 using AES in CBC mode with a null initialization vector (IV) and a key sent from the server that is padded to 32 bytes.[^474]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) uses RC4 to encrypt the message body of HTTP content.[^453] [^486]  |
| [[PoisonIvy\|S0012]] | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) uses the Camellia cipher to encrypt communications.[^55]  |
| [[NanoCore\|S0336]] | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) uses DES to encrypt the C2 traffic.[^265]  |
| [[PLEAD\|S0435]] | PLEAD | [PLEAD](https://attack.mitre.org/software/S0435) has used RC4 encryption to download modules.[^236]  |
| [[Daserf\|S0187]] | Daserf | [Daserf](https://attack.mitre.org/software/S0187) uses RC4 encryption to obfuscate HTTP traffic.[^111]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) uses a secret key with a series of XOR and addition operations to encrypt C2 traffic.[^226]  |
| [[Solar\|S1166]] | Solar | [Solar](https://attack.mitre.org/software/S1166) can XOR encrypt C2 communications.[^35]  |
| [[FakeM\|S0076]] | FakeM | The original variant of [FakeM](https://attack.mitre.org/software/S0076) encrypts C2 traffic using a custom encryption cipher that uses an XOR key of “YHCRA” and bit rotation between each XOR operation. Some variants of [FakeM](https://attack.mitre.org/software/S0076) use RC4 to encrypt C2 traffic.[^8]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) has used an RC4-based encryption method for its C2 communications.[^71]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) has used DES to encrypt all C2 communications.[^105]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) can receive XOR-encrypted commands from C2.[^35]  |
| [[WIREFIRE\|S1115]] | WIREFIRE | [WIREFIRE](https://attack.mitre.org/software/S1115) can AES encrypt process output sent from compromised devices to C2.[^416]  |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can use an AES key to encrypt C2 communications.[^419]  |
| [[LookBack\|S0582]] | LookBack | [LookBack](https://attack.mitre.org/software/S0582) uses a modified version of RC4 for data transfer.[^290]  |
| [[CallMe\|S0077]] | CallMe | [CallMe](https://attack.mitre.org/software/S0077) uses AES to encrypt C2 traffic.[^8]  |
| [[CHOPSTICK\|S0023]] | CHOPSTICK | [CHOPSTICK](https://attack.mitre.org/software/S0023) encrypts C2 communications with RC4.[^280]  |
| [[RIFLESPINE\|S1222]] | RIFLESPINE | [RIFLESPINE](https://attack.mitre.org/software/S1222) can use the AES algorithm to encrypt C2 data.[^106]  |
| [[SLIGHTPULSE\|S1110]] | SLIGHTPULSE | [SLIGHTPULSE](https://attack.mitre.org/software/S1110) can RC4 encrypt all incoming and outgoing C2 messages.[^93]  |
| [[NDiskMonitor\|S0272]] | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) uses AES to encrypt certain information sent over its C2 channel.[^200]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) can XOR encrypt C2 traffic.[^439]  |
| [[Troll Stealer\|S1196]] | Troll Stealer | [Troll Stealer](https://attack.mitre.org/software/S1196) encrypts data sent to command and control infrastructure using a combination of RC4 and RSA-4096 algorithms.[^348]  |
| [[Ebury\|S0377]] | Ebury | [Ebury](https://attack.mitre.org/software/S0377) has encrypted C2 traffic using the client IP address, then encoded it as a hexadecimal string.[^292]  |
| [[ZIPLINE\|S1114]] | ZIPLINE | [ZIPLINE](https://attack.mitre.org/software/S1114) can use AES-128-CBC to encrypt data for both upload and download.[^139]  |
| [[ChChes\|S0144]] | ChChes | [ChChes](https://attack.mitre.org/software/S0144) can encrypt C2 traffic with AES or RC4.[^96] [^211]  |
| [[IceApple\|S1022]] | IceApple | The [IceApple](https://attack.mitre.org/software/S1022) Result Retriever module can AES encrypt C2 responses.[^423]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) can encrypt the data that it sends and receives from the C2 server using an RC4 encryption algorithm.[^30] [^328]  |
| [[SideTwist\|S0610]] | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) can encrypt C2 communications with a randomly generated key.[^162]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can send AES encrypted C2 commands.[^352]  |
| [[XCSSET\|S0658]] | XCSSET | [XCSSET](https://attack.mitre.org/software/S0658) uses RC4 encryption over TCP to communicate with its C2 server.[^228]    |
| [[Dipsind\|S0200]] | Dipsind | [Dipsind](https://attack.mitre.org/software/S0200) encrypts C2 data with AES256 in ECB mode.[^496]  |
| [[httpclient\|S0068]] | httpclient | [httpclient](https://attack.mitre.org/software/S0068) encrypts C2 content with XOR using a single byte, 0x12.[^79]  |
| [[POWERTON\|S0371]] | POWERTON | [POWERTON](https://attack.mitre.org/software/S0371) has used AES for encrypting C2 traffic.[^272]  |
| [[StarProxy\|S1227]] | StarProxy | [StarProxy](https://attack.mitre.org/software/S1227) has leveraged two 256-byte XOR keys to encrypt and decrypt  network packets using a custom algorithm.[^262]  |
| [[BADNEWS\|S0128]] | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) encrypts C2 data with a ROR by 3 and an XOR by 0x23.[^279] [^200]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can RC4 encrypt strings in C2 communication.[^372]  |
| [[Helminth\|S0170]] | Helminth | [Helminth](https://attack.mitre.org/software/S0170) encrypts data sent to its C2 server over HTTP with RC4.[^108]  |
| [[Dridex\|S0384]] | Dridex | [Dridex](https://attack.mitre.org/software/S0384) has encrypted traffic with RC4.[^146]  |
| [[Komplex\|S0162]] | Komplex | The [Komplex](https://attack.mitre.org/software/S0162) C2 channel uses an 11-byte XOR algorithm to hide data.[^386]  |
| [[Comnie\|S0244]] | Comnie | [Comnie](https://attack.mitre.org/software/S0244) encrypts command and control communications with RC4.[^500]  |
| [[H1N1\|S0132]] | H1N1 | [H1N1](https://attack.mitre.org/software/S0132) encrypts C2 traffic using an RC4 key.[^460]  |
| [[Azorult\|S0344]] | Azorult | [Azorult](https://attack.mitre.org/software/S0344) can encrypt C2 traffic using XOR.[^131] [^244]  |
| [[UPPERCUT\|S0275]] | UPPERCUT | Some versions of [UPPERCUT](https://attack.mitre.org/software/S0275) have used the hard-coded string “this is the encrypt key” for Blowfish encryption when communicating with a C2. Later versions have hard-coded keys uniquely for each C2 address.[^267]  [UPPERCUT](https://attack.mitre.org/software/S0275) has also used custom ChaCha20, XOR, and LZO algorithms for C2 communication.[^306] [^2]  |
| [[ADVSTORESHELL\|S0045]] | ADVSTORESHELL | A variant of [ADVSTORESHELL](https://attack.mitre.org/software/S0045) encrypts some C2 with 3DES.[^15]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can encrypt C2 traffic using XOR with a hard coded key.[^102]  |
| [[HiddenWasp\|S0394]] | HiddenWasp | [HiddenWasp](https://attack.mitre.org/software/S0394) uses an RC4-like algorithm with an already computed PRGA generated key-stream for network communication.[^438]  |
| [[WarzoneRAT\|S0670]] | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) can encrypt its C2 with RC4 with the password `warzone160\x00`.[^193]  |
| [[FALLCHILL\|S0181]] | FALLCHILL | [FALLCHILL](https://attack.mitre.org/software/S0181) encrypts C2 data with RC4 encryption.[^329] [^153]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | Several [Lazarus Group](https://attack.mitre.org/groups/G0032) malware families encrypt C2 traffic using custom code that uses XOR with an ADD operation and XOR with a SUB operation. Another [Lazarus Group](https://attack.mitre.org/groups/G0032) malware sample XORs C2 traffic. Other [Lazarus Group](https://attack.mitre.org/groups/G0032) malware uses Caracachs encryption to encrypt C2 payloads. [Lazarus Group](https://attack.mitre.org/groups/G0032) has also used AES to encrypt C2 traffic.[^394] [^314] [^258] [^183]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) has encrypted network communications with AES.[^81]  |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) installed a Delphi backdoor that used a custom algorithm for C2 communications.[^229]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has used AES-256 and 3DES for C2 communications.[^357]  |
| [[Volt Typhoon\|G1017]] | Volt Typhoon | [Volt Typhoon](https://attack.mitre.org/groups/G1017) has used a version of the Awen web shell that employed AES encryption and decryption for C2 communications.[^323]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used AES to encrypt C2 responses.[^150]  |
| [[BRONZE BUTLER\|G0060]] | BRONZE BUTLER | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has used RC4 encryption (for Datper malware) and AES (for xxmm malware) to obfuscate HTTP traffic. [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) has also used a tool called RarStar that encodes data with a custom XOR algorithm when posting it to a C2 server.[^111]  |
| [[Mustang Panda\|G0129]] | Mustang Panda | [Mustang Panda](https://attack.mitre.org/groups/G0129) has encrypted C2 communications with RC4.[^477] [^421]  [Mustang Panda](https://attack.mitre.org/groups/G0129) has also leveraged encryption and compression algorithms to obfuscate the traffic between the system and C2 server, methods observed included RC4, AES, XOR with 0x5a, and LZO.[^320]  |
| [[Stealth Falcon\|G0038]] | Stealth Falcon | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware encrypts C2 traffic using RC4 with a hard-coded key.[^291]  |
| [[RedCurl\|G1039]] | RedCurl | [RedCurl](https://attack.mitre.org/groups/G1039) has used AES-128 CBC to encrypt C2 communications.[^393]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has encrypted C2 traffic using RC4.[^354] <br> |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) used AES-128 to encrypt C2 traffic.[^377]  |
| [[ZIRCONIUM\|G0128]] | ZIRCONIUM | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used AES encrypted communications in C2.[^432]  |
| [[APT33\|G0064]] | APT33 | [APT33](https://attack.mitre.org/groups/G0064) has used AES for encryption of command and control traffic.[^272]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Network Intrusion Prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)


[^9]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^10]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^11]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^12]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^13]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)


[^14]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^15]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^16]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^17]: [Accenture HyperStack October 2020](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)


[^18]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^19]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^20]: [GitHub Sliver Encryption](https://github.com/BishopFox/sliver/wiki/Transport-Encryption)


[^21]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^22]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^23]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^24]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^25]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^26]: [Cisco Talos MUSTANG PANDA PLUGX PUBLOAD MAY 2022](https://blog.talosintelligence.com/mustang-panda-targets-europe/)


[^27]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^28]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^29]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^30]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^31]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^32]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^33]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^34]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^35]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^36]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^37]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^38]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)


[^39]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)


[^40]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)


[^41]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^42]: [Proofpoint TA505 Mar 2018](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)


[^43]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^44]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^45]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)


[^46]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^47]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)


[^48]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^49]: [US-CERT HOTCROISSANT February 2020](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)


[^50]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^51]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^52]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^53]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^54]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^55]: [FireEye Poison Ivy](https://www.mandiant.com/sites/default/files/2021-09/rpt-poison-ivy.pdf)


[^56]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^57]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^58]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^59]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^60]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^61]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^62]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^63]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^64]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^65]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^66]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^67]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^68]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^69]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^70]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^71]: [Security Intelligence More Eggs Aug 2019](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)


[^72]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^73]: [ESET Gazer Aug 2017](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)


[^74]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)


[^75]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^76]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^77]: [FireEye APT29](https://services.google.com/fh/files/misc/rpt-apt29-hammertoss-stealthy-tactics-define-en.pdf)


[^78]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^79]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^80]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^81]: [Kaspersky Cloud Atlas December 2014](https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/)


[^82]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^83]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^84]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^85]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^86]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^87]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)


[^88]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^89]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^90]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^91]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^92]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^93]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)


[^94]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)


[^95]: [Kaspersky Carbanak](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)


[^96]: [Palo Alto menuPass Feb 2017](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)


[^97]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^98]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^99]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^100]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^101]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^102]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^103]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)


[^104]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^105]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^106]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^107]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^108]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^109]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^110]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^111]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)


[^112]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^113]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^114]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^115]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^116]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^117]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^118]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)


[^119]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^120]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^121]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^122]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^123]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)


[^124]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^125]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^126]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^127]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^128]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^129]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)


[^130]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^131]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)


[^132]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^133]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^134]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^135]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^136]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^137]: [Villeneuve 2011](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_dissecting-lurid-apt.pdf)


[^138]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^139]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


[^140]: [Forcepoint Felismus Mar 2017](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)


[^141]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^142]: [Proofpoint TA459 April 2017](https://www.proofpoint.com/us/threat-insight/post/apt-targets-financial-analysts)


[^143]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^144]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^145]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^146]: [Kaspersky Dridex May 2017](https://securelist.com/dridex-a-history-of-evolution/78531/)


[^147]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)


[^148]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^149]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^150]: [Talos MuddyWater Jan 2022](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)


[^151]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^152]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^153]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^154]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^155]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^156]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^157]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^158]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^159]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^160]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^161]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)


[^162]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)


[^163]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^164]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^165]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^166]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^167]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^168]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^169]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^170]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^171]: [Bitdefender Trickbot C2 infra Nov 2020](https://www.bitdefender.com/blog/labs/trickbot-is-dead-long-live-trickbot/)


[^172]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^173]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^174]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^175]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^176]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^177]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^178]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^179]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^180]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^181]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^182]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^183]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)


[^184]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^185]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^186]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^187]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)


[^188]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^189]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^190]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^191]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^192]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^193]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)


[^194]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^195]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)


[^196]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^197]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)


[^198]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)


[^199]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)


[^200]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^201]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^202]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^203]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^204]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^205]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^206]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^207]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^208]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^209]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)


[^210]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^211]: [JPCERT ChChes Feb 2017](https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html)


[^212]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^213]: [Zscaler Pikabot 2023](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)


[^214]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^215]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^216]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^217]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^218]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^219]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^220]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^221]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^222]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^223]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^224]: [Mandiant No Easy Breach](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)


[^225]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^226]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^227]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^228]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^229]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)


[^230]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)


[^231]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^232]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)


[^233]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^234]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^235]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^236]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^237]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^238]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^239]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^240]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)


[^241]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^242]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^243]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^244]: [Proofpoint Azorult July 2018](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)


[^245]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)


[^246]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^247]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^248]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^249]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)


[^250]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^251]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^252]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^253]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^254]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^255]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^256]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^257]: [PWC WellMess July 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)


[^258]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^259]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^260]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^261]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^262]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)


[^263]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^264]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^265]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)


[^266]: [FRP GitHub](https://github.com/fatedier/frp)


[^267]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^268]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)


[^269]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^270]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^271]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^272]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^273]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^274]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^275]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^276]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^277]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^278]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^279]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^280]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)


[^281]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^282]: [PWC WellMess C2 August 2020](https://www.pwc.co.uk/issues/cyber-security-services/insights/wellmess-analysis-command-control.html)


[^283]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^284]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^285]: [Chaos Stolen Backdoor](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)


[^286]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)


[^287]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^288]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)


[^289]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)


[^290]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)


[^291]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


[^292]: [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)


[^293]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)


[^294]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^295]: [Fortinet Havoc MAR 2025](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)


[^296]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^297]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^298]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^299]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^300]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^301]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^302]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^303]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^304]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^305]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^306]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)


[^307]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^308]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^309]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)


[^310]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^311]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^312]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^313]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


[^314]: [Novetta Blockbuster Destructive Malware](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)


[^315]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^316]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^317]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^318]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^319]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^320]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)


[^321]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^322]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^323]: [Secureworks BRONZE SILHOUETTE May 2023](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)


[^324]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^325]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^326]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^327]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^328]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^329]: [US-CERT FALLCHILL Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318A)


[^330]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^331]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^332]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^333]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)


[^334]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^335]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^336]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)


[^337]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^338]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^339]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^340]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^341]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^342]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^343]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^344]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^345]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^346]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^347]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^348]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)


[^349]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^350]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^351]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^352]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^353]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^354]: [Sekoia ClickFake 2025](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)


[^355]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^356]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^357]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^358]: [Unit 42 SeaDuke 2015](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)


[^359]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^360]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^361]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^362]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^363]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^364]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^365]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^366]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^367]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^368]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^369]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^370]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^371]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^372]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^373]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^374]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^375]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^376]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^377]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^378]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^379]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^380]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^381]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^382]: [Malwarebytes KONNI Evolves Jan 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/)


[^383]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^384]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^385]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^386]: [Sofacy Komplex Trojan](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)


[^387]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^388]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


[^389]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^390]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^391]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^392]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^393]: [group-ib_redcurl2](https://www.group-ib.com/resources/research-hub/red-curl-2/)


[^394]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^395]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^396]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)


[^397]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^398]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^399]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^400]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^401]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^402]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^403]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^404]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^405]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^406]: [HarmonProofpoint_SystemBC_Aug2019](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)


[^407]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^408]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^409]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^410]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)


[^411]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^412]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^413]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^414]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^415]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


[^416]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)


[^417]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^418]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^419]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^420]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^421]: [Recorded Future REDDELTA July 2020](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)


[^422]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^423]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^424]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^425]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^426]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^427]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^428]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^429]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^430]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^431]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^432]: [Zscaler APT31 Covid-19 October 2020](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)


[^433]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^434]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^435]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^436]: [Fidelis Hi-Zor](https://www.fidelissecurity.com/threatgeek/archive/introducing-hi-zor-rat/)


[^437]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^438]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)


[^439]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^440]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^441]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^442]: [CISA WellMess July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)


[^443]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^444]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^445]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^446]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^447]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^448]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^449]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^450]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^451]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^452]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^453]: [TrendMicro Taidoor](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)


[^454]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^455]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^456]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^457]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^458]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^459]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^460]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)


[^461]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^462]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^463]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^464]: [Trend Micro Emotet Jan 2019](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)


[^465]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^466]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^467]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^468]: [Proofpoint TA416 Europe March 2022](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)


[^469]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^470]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^471]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^472]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)


[^473]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^474]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)


[^475]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^476]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^477]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^478]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^479]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^480]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)


[^481]: [ESET Kobalos Feb 2021](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)


[^482]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^483]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^484]: [NGLite Trojan](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)


[^485]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^486]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^487]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^488]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^489]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)


[^490]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^491]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)


[^492]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)


[^493]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^494]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^495]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^496]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)


[^497]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^498]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^499]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^500]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)


[^501]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^502]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^503]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^504]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^505]: [Moran 2014](https://www.fireeye.com/blog/threat-research/2014/09/darwins-favorite-apt-group-2.html)


[^506]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^507]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^508]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^509]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^510]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^511]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


[^512]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^513]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^514]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


