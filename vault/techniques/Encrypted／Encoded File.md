---
aliases: 
    - T1027.013
mitre-attack: https://attack.mitre.org/techniques/T1027/013
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1027.013

Adversaries may encrypt or encode files to obfuscate strings, bytes, and other specific patterns to impede detection. Encrypting and/or encoding file content aims to conceal malicious artifacts within a file used in an intrusion. Many other techniques, such as [Software Packing](https://attack.mitre.org/techniques/T1027/002), [Steganography](https://attack.mitre.org/techniques/T1027/003), and [Embedded Payloads](https://attack.mitre.org/techniques/T1027/009), share this same broad objective. Encrypting and/or encoding files could lead to a lapse in detection of static signatures, only for this malicious content to be revealed (i.e., [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140)) at the time of execution/use.<br><br>This type of file obfuscation can be applied to many file artifacts present on victim hosts, such as malware log/configuration and payload files.[^97]  Files can be encrypted with a hardcoded or user-supplied key, as well as otherwise obfuscated using standard encoding schemes such as Base64.<br><br>The entire content of a file may be obfuscated, or just specific functions or values (such as C2 addresses). Encryption and encoding may also be applied in redundant layers for additional protection.<br><br>For example, adversaries may abuse password-protected Word documents or self-extracting (SFX) archives as a method of encrypting/encoding a file such as a [Phishing](https://attack.mitre.org/techniques/T1566) payload. These files typically function by attaching the intended archived content to a decompressor stub that is executed when the file is invoked (e.g., [User Execution](https://attack.mitre.org/techniques/T1204)).[^120]  <br><br>Adversaries may also abuse file-specific as well as custom encoding schemes. For example, Byte Order Mark (BOM) headers in text files may be abused to manipulate and obfuscate file content until [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) execution.


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Sliver\|S0633]] | Sliver | [Sliver](https://attack.mitre.org/software/S0633) can encrypt strings at compile time.[^429] [^71]  |
| [[DCRAT\|S9017]] | DCRAT | The [DCRAT](https://attack.mitre.org/software/S9017) configuration file is encrypted using AES-256.[^572]  |
| [[PcShare\|S1050]] | PcShare | [PcShare](https://attack.mitre.org/software/S1050) has been encrypted with XOR using different 32-long Base16 strings.[^256]  |
| [[Remcos\|S0332]] | Remcos | [Remcos](https://attack.mitre.org/software/S0332) can use string encryption to hinder analysis.[^483]  |
| [[Donut\|S0695]] | Donut | [Donut](https://attack.mitre.org/software/S0695) can generate encrypted, compressed/encoded, or otherwise obfuscated code modules.[^241]  |
| [[IronNetInjector\|S0581]] | IronNetInjector | [IronNetInjector](https://attack.mitre.org/software/S0581) can obfuscate variable names, encrypt strings, as well as base64 encode and Rijndael encrypt payloads.[^297]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) uses an AES CBC (256 bits) encryption algorithm for its loader and configuration files.[^554]  |
| [[BLINDINGCAN\|S0520]] | BLINDINGCAN | [BLINDINGCAN](https://attack.mitre.org/software/S0520) has obfuscated code using Base64 encoding.[^376]  |
| [[Ninja\|S1100]] | Ninja | The [Ninja](https://attack.mitre.org/software/S1100) payload is XOR encrypted and compressed.[^347]  [Ninja](https://attack.mitre.org/software/S1100) has also XORed its configuration data with a constant value of `0xAA`.[^262] [^347]  |
| [[BRICKSTORM\|S9015]] | BRICKSTORM | [BRICKSTORM](https://attack.mitre.org/software/S9015) has utilized XOR cipher encryption to hide key strings within their code, to include IPv4 addresses of public DNS-over-HTTPS (DOH) servers.[^268]  |
| [[Torisma\|S0678]] | Torisma | [Torisma](https://attack.mitre.org/software/S0678) has been Base64 encoded and AES encrypted.[^163]  |
| [[DOGCALL\|S0213]] | DOGCALL | [DOGCALL](https://attack.mitre.org/software/S0213) is encrypted using single-byte XOR.[^565]  |
| [[Stuxnet\|S0603]] | Stuxnet | [Stuxnet](https://attack.mitre.org/software/S0603) uses encrypted configuration blocks and writes encrypted files to disk.[^517]  |
| [[MEDUSA\|S1220]] | MEDUSA | [MEDUSA](https://attack.mitre.org/software/S1220) can XOR encrypt configuration strings.[^135]  |
| [[VersaMem\|S1154]] | VersaMem | [VersaMem](https://attack.mitre.org/software/S1154) encrypted captured credentials with AES then Base64 encoded them before writing to local storage.[^38]  |
| [[Chinoxy\|S1041]] | Chinoxy | [Chinoxy](https://attack.mitre.org/software/S1041) has encrypted its configuration file.[^256]  |
| [[PAKLOG\|S1233]] | PAKLOG | [PAKLOG](https://attack.mitre.org/software/S1233) has utilized a simple encoding mechanism to encode characters in the buffer.[^118]    |
| [[Smoke Loader\|S0226]] | Smoke Loader | [Smoke Loader](https://attack.mitre.org/software/S0226) uses a simple one-byte XOR method to obfuscate values in the malware.[^590] [^357]  |
| [[WindTail\|S0466]] | WindTail | [WindTail](https://attack.mitre.org/software/S0466) can be delivered as a compressed, encrypted, and encoded payload.[^169]  |
| [[Emissary\|S0082]] | Emissary | Variants of [Emissary](https://attack.mitre.org/software/S0082) encrypt payloads using various XOR ciphers, as well as a custom algorithm that uses the "srand" and "rand" functions.[^45] [^95]  |
| [[Exaramel for Linux\|S0401]] | Exaramel for Linux | [Exaramel for Linux](https://attack.mitre.org/software/S0401) uses RC4 for encrypting the configuration.[^41] [^408]  |
| [[HAWKBALL\|S0391]] | HAWKBALL | [HAWKBALL](https://attack.mitre.org/software/S0391) has encrypted the payload with an XOR-based algorithm.[^462]  |
| [[PS1\|S0613]] | PS1 | [PS1](https://attack.mitre.org/software/S0613) is distributed as a set of encrypted files and scripts.[^599]  |
| [[HeartCrypt\|S9018]] | HeartCrypt | [HeartCrypt](https://attack.mitre.org/software/S9018) strings are encrypted via a single-byte XOR operation rotating over a hard-coded key, possibly provided by the PaaS customers. [^338]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used an XOR-based algorithm to encrypt Tor clients dropped to disk.[^226] 	[Ursnif](https://attack.mitre.org/software/S0386) droppers have also been delivered as password-protected zip files that execute base64 encoded [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands.[^217]  |
| [[ThreatNeedle\|S0665]] | ThreatNeedle | [ThreatNeedle](https://attack.mitre.org/software/S0665) has been compressed and obfuscated using RC4, AES, or XOR.[^426]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) has an encrypted configuration file.[^331]  |
| [[RedLeaves\|S0153]] | RedLeaves | A [RedLeaves](https://attack.mitre.org/software/S0153) configuration file is encrypted with a simple XOR key, 0x53.[^353]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034)’s loader contained AES-CBC/PKCS7 encrypted blobs, which were descrypted and written to disk.[^611]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) encrypts strings with XOR. [Zeus Panda](https://attack.mitre.org/software/S0330) also encrypts all configuration and settings in AES and RC4.[^309] [^77]  |
| [[CARROTBAT\|S0462]] | CARROTBAT | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to download a base64 encoded payload.[^518]  |
| [[GravityRAT\|S0237]] | GravityRAT | [GravityRAT](https://attack.mitre.org/software/S0237) supports file encryption (AES with the key "lolomycin2017").[^58]  |
| [[InvisibleFerret\|S1245]] | InvisibleFerret | [InvisibleFerret](https://attack.mitre.org/software/S1245) has utilized the XOR and Base64 encoding for each of its modules.[^63]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also obfuscated files with a combination of zlib, Base64 and reverse string order.[^216]  [InvisibleFerret](https://attack.mitre.org/software/S1245) has also utilized the XOR and Base64 encoding some of its Python scripts.[^278]  |
| [[StrongPity\|S0491]] | StrongPity | [StrongPity](https://attack.mitre.org/software/S0491) has used encrypted strings in its dropper component.[^329] [^529]  |
| [[AuditCred\|S0347]] | AuditCred | [AuditCred](https://attack.mitre.org/software/S0347) encrypts the configuration.[^607]  |
| [[ROAMINGHOUSE\|S9026]] | ROAMINGHOUSE | [ROAMINGHOUSE](https://attack.mitre.org/software/S9026) can embed a ZIP file containing [UPPERCUT](https://attack.mitre.org/software/S0275) components into three base64 encoded parts.[^2]  |
| [[UPSTYLE\|S1164]] | UPSTYLE | [UPSTYLE](https://attack.mitre.org/software/S1164) stores primary content as base64-encoded objects.[^102] [^119]  |
| [[Medusa Ransomware\|S1244]] | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has utilized XOR encrypted strings.[^30] [^466]  |
| [[RainyDay\|S0629]] | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) has downloaded as a XOR-encrypted payload.[^392]  |
| [[PyDCrypt\|S1032]] | PyDCrypt | [PyDCrypt](https://attack.mitre.org/software/S1032) has been compiled and encrypted with PyInstaller, specifically using the --key flag during the build phase.[^355]  |
| [[BOOKWORM\|S1226]] | BOOKWORM | [BOOKWORM](https://attack.mitre.org/software/S1226) has utilized Base64 encoding to obfuscate its payload.[^24]  |
| [[EnvyScout\|S0634]] | EnvyScout | [EnvyScout](https://attack.mitre.org/software/S0634) can Base64 encode payloads.[^403]  |
| [[GreyEnergy\|S0342]] | GreyEnergy | [GreyEnergy](https://attack.mitre.org/software/S0342) encrypts its configuration files with AES-256 and also encrypts its strings.[^244]  |
| [[Aria-body\|S0456]] | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) has used an encrypted configuration file for its loader.[^162]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) uses obfuscated URLs to download a ZIP file.[^44]  |
| [[DUSTTRAP\|S1159]] | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) begins with an initial launcher that decrypts an AES-128-CFB encrypted file on disk and executes it in memory.[^514]  |
| [[Avenger\|S0473]] | Avenger | [Avenger](https://attack.mitre.org/software/S0473) has the ability to XOR encrypt files to be sent to C2.[^202]  |
| [[DUSTPAN\|S1158]] | DUSTPAN | [DUSTPAN](https://attack.mitre.org/software/S1158) decrypts an embedded payload.[^514] [^365]  |
| [[Prikormka\|S0113]] | Prikormka | Some resources in [Prikormka](https://attack.mitre.org/software/S0113) are encrypted with a simple XOR operation or encoded with Base64.[^26]  |
| [[Dacls\|S0497]] | Dacls | [Dacls](https://attack.mitre.org/software/S0497) can encrypt its configuration file with AES CBC.[^199]  |
| [[Woody RAT\|S1065]] | Woody RAT | [Woody RAT](https://attack.mitre.org/software/S1065) has used Base64 encoded strings and scripts.[^170]  |
| [[Mafalda\|S1060]] | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) has been obfuscated and contains encrypted functions.[^28]  |
| [[Squirrelwaffle\|S1030]] | Squirrelwaffle | [Squirrelwaffle](https://attack.mitre.org/software/S1030) has been obfuscated with a XOR-based algorithm.[^349] [^543]  |
| [[HexEval Loader\|S1249]] | HexEval Loader | [HexEval Loader](https://attack.mitre.org/software/S1249) has encoded module names and C2 URLs as hexadecimal strings in attempts to evade analysis.[^469] [^530]  |
| [[Hildegard\|S0601]] | Hildegard | [Hildegard](https://attack.mitre.org/software/S0601) has encrypted an ELF file.[^395]  |
| [[FlawedGrace\|S0383]] | FlawedGrace | [FlawedGrace](https://attack.mitre.org/software/S0383) encrypts its C2 configuration files with AES in CBC mode.[^127]  |
| [[Rifdoor\|S0433]] | Rifdoor | [Rifdoor](https://attack.mitre.org/software/S0433) has encrypted strings with a single byte XOR algorithm.[^113]  |
| [[Cuckoo Stealer\|S1153]] | Cuckoo Stealer | [Cuckoo Stealer](https://attack.mitre.org/software/S1153) strings are XOR-encrypted.[^288] [^615]  |
| [[WastedLocker\|S0612]] | WastedLocker | The [WastedLocker](https://attack.mitre.org/software/S0612) payload includes encrypted strings stored within the .bss section of the binary file.[^583]     |
| [[Volgmer\|S0180]] | Volgmer | A [Volgmer](https://attack.mitre.org/software/S0180) variant is encoded using a simple XOR cipher.[^252]  |
| [[WhisperGate\|S0689]] | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) can Base64 encode strings, store downloaded files in reverse byte order,  and use the Eazfuscator tool to obfuscate its third stage.[^501] [^443] [^360]  |
| [[ZeroT\|S0230]] | ZeroT | [ZeroT](https://attack.mitre.org/software/S0230) has encrypted its payload with RC4.[^76]  |
| [[Skidmap\|S0468]] | Skidmap | [Skidmap](https://attack.mitre.org/software/S0468) has encrypted it's main payload using 3DES.[^544]   |
| [[SamSam\|S0370]] | SamSam | [SamSam](https://attack.mitre.org/software/S0370) has been seen using AES or DES to encrypt payloads and payload components.[^616] [^577]  |
| [[Mispadu\|S1122]] | Mispadu | [Mispadu](https://attack.mitre.org/software/S1122) uses a custom algorithm to obfuscate its internal strings and uses hardcoded keys.[^456] <br><br>[Mispadu](https://attack.mitre.org/software/S1122) also uses encoded configuration files and has encoded payloads using Base64.[^456] [^277] [^222]  |
| [[Raindrop\|S0565]] | Raindrop | [Raindrop](https://attack.mitre.org/software/S0565) encrypted its payload using a simple XOR algorithm with a single-byte key.[^482] [^103]  |
| [[RustyWater\|S9037]] | RustyWater | [RustyWater](https://attack.mitre.org/software/S9037) has encrypted all strings in the code using position independent XOR encryption.[^51]  |
| [[Fysbis\|S0410]] | Fysbis | [Fysbis](https://attack.mitre.org/software/S0410) has been encrypted using XOR and RC4.[^474]   |
| [[IcedID\|S0483]] | IcedID | [IcedID](https://attack.mitre.org/software/S0483) has utilzed encrypted binaries and base64 encoded strings.[^567]  |
| [[VERMIN\|S0257]] | VERMIN | [VERMIN](https://attack.mitre.org/software/S0257) is obfuscated using the obfuscation tool called ConfuserEx.[^562]  |
| [[DCSrv\|S1033]] | DCSrv | [DCSrv](https://attack.mitre.org/software/S1033)'s configuration is encrypted.[^355]  |
| [[BOOSTWRITE\|S0415]] | BOOSTWRITE | [BOOSTWRITE](https://attack.mitre.org/software/S0415) has encoded its payloads using a ChaCha stream cipher with a 256-bit key and 64-bit Initialization vector (IV) to evade detection.[^167]  |
| [[Rising Sun\|S0448]] | Rising Sun | Configuration data used by [Rising Sun](https://attack.mitre.org/software/S0448) has been encrypted using an RC4 stream algorithm.[^191] 	 |
| [[Chrommme\|S0667]] | Chrommme | [Chrommme](https://attack.mitre.org/software/S0667) can encrypt sections of its code to evade detection.[^586]  |
| [[SocGholish\|S1124]] | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) has single or double Base-64 encoded references to its second-stage server URLs.[^413]  |
| [[Hi-Zor\|S0087]] | Hi-Zor | [Hi-Zor](https://attack.mitre.org/software/S0087) uses various XOR techniques to obfuscate its components.[^204]  |
| [[LightSpy\|S1185]] | LightSpy | [LightSpy](https://attack.mitre.org/software/S1185) encrypts the C2 configuration file using AES with a static key, while the module `.dylib` files use a rolling one-byte encoding for obfuscation.[^67]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) has written AES-encrypted and Base64-encoded configuration files to disk.[^343] [^153]  |
| [[KeyBoy\|S0387]] | KeyBoy | In one version of [KeyBoy](https://attack.mitre.org/software/S0387), string obfuscation routines were used to hide many of the critical values referenced in the malware.[^295]  |
| [[HyperBro\|S0398]] | HyperBro | [HyperBro](https://attack.mitre.org/software/S0398) can be delivered encrypted to a compromised host.[^459]  |
| [[BeaverTail\|S1246]] | BeaverTail | [BeaverTail](https://attack.mitre.org/software/S1246) has obfuscated strings of code with Base64 encoding within the JavaScript version of the malware.[^63] [^278] [^305]  [BeaverTail](https://attack.mitre.org/software/S1246) has also utilized the open-source tool JavaScript-Obfuscator to obfuscate strings and functions.[^216] [^141]  |
| [[SplatDropper\|S1232]] | SplatDropper | [SplatDropper](https://attack.mitre.org/software/S1232) has also utilized XOR encrypted payload.[^118]  |
| [[PlugX\|S0013]] | PlugX | [PlugX](https://attack.mitre.org/software/S0013) has leveraged XOR encryption with the key of 123456789.[^576]  |
| [[Reaver\|S0172]] | Reaver | [Reaver](https://attack.mitre.org/software/S0172) encrypts some of its files with XOR.[^132]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268)'s DLL file and non-malicious decoy file are encrypted with RC4 and some function name strings are obfuscated.[^393] [^171]  |
| [[NOOPLDR\|S9025]] | NOOPLDR | The [NOOPLDR](https://attack.mitre.org/software/S9025) payload is encrypted with AES256-CBC.[^600]  |
| [[Lumma Stealer\|S1213]] | Lumma Stealer | [Lumma Stealer](https://attack.mitre.org/software/S1213) has used AES-encrypted payloads contained within PowerShell scripts.[^53]  |
| [[Remsec\|S0125]] | Remsec | Some data in [Remsec](https://attack.mitre.org/software/S0125) is encrypted using RC5 in CBC mode, AES-CBC with a hardcoded key, RC4, or Salsa20. Some data is also base64-encoded.[^298] [^312]  |
| [[LightNeuron\|S0395]] | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) encrypts its configuration files with AES-256.[^561]  |
| [[KEYPLUG\|S1051]] | KEYPLUG | [KEYPLUG](https://attack.mitre.org/software/S1051) can use a hardcoded one-byte XOR encoded configuration file.[^497]  |
| [[PureCrypter\|S9019]] | PureCrypter | [PureCrypter](https://attack.mitre.org/software/S9019) has used SmartAssembly and NET-Reactor for string encryption and control flow obfuscation.[^151] [^233]  |
| [[DarkGate\|S1111]] | DarkGate | [DarkGate](https://attack.mitre.org/software/S1111) drops an encrypted PE file, pe.bin, and decrypts it during installation.[^580]  [DarkGate](https://attack.mitre.org/software/S1111) also uses custom base64 encoding schemas in later variations to obfuscate payloads.[^609]  |
| [[NanHaiShu\|S0228]] | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) encodes files in Base64.[^131]  |
| [[LockBit 3.0\|S1202]] | LockBit 3.0 | The [LockBit 3.0](https://attack.mitre.org/software/S1202) payload includes an encrypted main component.[^507] [^571]  |
| [[FoggyWeb\|S0661]] | FoggyWeb | [FoggyWeb](https://attack.mitre.org/software/S0661) has been XOR-encoded.[^267]  |
| [[HOMEFRY\|S0232]] | HOMEFRY | Some strings in [HOMEFRY](https://attack.mitre.org/software/S0232) are obfuscated with XOR x56.[^421]  |
| [[Elise\|S0081]] | Elise | [Elise](https://attack.mitre.org/software/S0081) encrypts several of its files, including configuration files.[^486]  |
| [[Gazer\|S0168]] | Gazer | [Gazer](https://attack.mitre.org/software/S0168) logs its actions into files that are encrypted with 3DES. It also uses RSA to encrypt resources.[^172]  |
| [[Latrodectus\|S1160]] | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) has used a pseudo random number generator (PRNG) algorithm and a rolling XOR key to obfuscate strings.[^333] [^136] [^351]  |
| [[LODEINFO\|S9020]] | LODEINFO | The [LODEINFO](https://attack.mitre.org/software/S9020) loader module contains XOR-encrypted shellcode.[^251] [^9] [^293]  |
| [[TYPEFRAME\|S0263]] | TYPEFRAME | APIs and strings in some [TYPEFRAME](https://attack.mitre.org/software/S0263) variants are RC4 encrypted. Another variant is encoded with XOR.[^464]  |
| [[Sagerunex\|S1210]] | Sagerunex | [Sagerunex](https://attack.mitre.org/software/S1210) can be passed a reference to an XOR-encrypted configuration file at runtime.[^54]  |
| [[LP-Notes\|S9036]] | LP-Notes | [LP-Notes](https://attack.mitre.org/software/S9036) has used a custom addition-based function and a string stacking function for string encryption.[^147]  |
| [[BendyBear\|S0574]] | BendyBear | [BendyBear](https://attack.mitre.org/software/S0574) has encrypted payloads using RC4 and XOR.[^237]  |
| [[GlassWorm\|S9010]] | GlassWorm | [GlassWorm](https://attack.mitre.org/software/S9010) has leveraged AES-256-CBC encryption to obfuscate its malicious JavaScript payload.[^487] [^176] [^502] [^50]   [GlassWorm](https://attack.mitre.org/software/S9010) has also utilized Base64 encoding to obfuscate the C2 details stored in the Solana memo field.[^487] [^176] [^50]  |
| [[Uroburos\|S0022]] | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) can use AES and CAST-128 encryption to obfuscate resources.[^186]  |
| [[Metamorfo\|S0455]] | Metamorfo | [Metamorfo](https://attack.mitre.org/software/S0455) has encrypted payloads and strings.[^369] [^240]  |
| [[Embargo\|S1247]] | Embargo | [Embargo](https://attack.mitre.org/software/S1247) has encrypted both MDeployer and MS4 Killer payloads with RC4.[^168]  |
| [[PipeMon\|S0501]] | PipeMon | [PipeMon](https://attack.mitre.org/software/S0501) modules are stored encrypted on disk.[^139]  |
| [[MagicRAT\|S1182]] | MagicRAT | [MagicRAT](https://attack.mitre.org/software/S1182) stores base64 encoded command and contorl URLs in a configuraiton file, with each URL prefixed with the value `LR02DPt22R`.[^325]  |
| [[TINYTYPHON\|S0131]] | TINYTYPHON | [TINYTYPHON](https://attack.mitre.org/software/S0131) has used XOR with 0x90 to obfuscate its configuration file.[^335]  |
| [[KONNI\|S0356]] | KONNI | [KONNI](https://attack.mitre.org/software/S0356) is heavily obfuscated and includes encrypted configuration files.[^121]  |
| [[Winnti for Linux\|S0430]] | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) can encode its configuration file with single-byte XOR encoding.[^492]  |
| [[RAPIDPULSE\|S1113]] | RAPIDPULSE | [RAPIDPULSE](https://attack.mitre.org/software/S1113) has the ability to RC4 encrypt and base64 encode decrypted files on compromised servers prior to writing them to stdout.[^404]  |
| [[JHUHUGIT\|S0044]] | JHUHUGIT | Many strings in [JHUHUGIT](https://attack.mitre.org/software/S0044) are obfuscated with a XOR algorithm.[^406] [^110] [^69]  |
| [[BLUELIGHT\|S0657]] | BLUELIGHT | [BLUELIGHT](https://attack.mitre.org/software/S0657) has a XOR-encoded payload.[^566]  |
| [[KGH_SPY\|S0526]] | KGH_SPY | [KGH_SPY](https://attack.mitre.org/software/S0526) has used encrypted strings in its installer.[^174]  |
| [[Micropsia\|S0339]] | Micropsia | [Micropsia](https://attack.mitre.org/software/S0339) obfuscates the configuration with a custom Base64 and XOR.[^504] [^232]  |
| [[Kerrdown\|S0585]] | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) can encrypt, encode, and compress multiple layers of shellcode.[^457]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has encrypted and encoded configuration data with Base64 and XOR functions.[^346]  |
| [[StoneDrill\|S0380]] | StoneDrill | [StoneDrill](https://attack.mitre.org/software/S0380) has obfuscated its module with an alphabet-based table or XOR encryption.[^109]  |
| [[Attor\|S0438]] | Attor | Strings in [Attor](https://attack.mitre.org/software/S0438)'s components are encrypted with a XOR cipher, using a hardcoded key and the configuration data, log files and plugins are encrypted using a hybrid encryption scheme of Blowfish-OFB combined with RSA.[^534]  |
| [[Mosquito\|S0256]] | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256)’s installer is obfuscated with a custom crypter to obfuscate the installer.[^389]  |
| [[BlackByte Ransomware\|S1180]] | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is distributed as an encrypted payload.[^302]  |
| [[PHPsert\|S9028]] | PHPsert | [PHPsert](https://attack.mitre.org/software/S9028) can use multiple obfuscation techniques including XOR encoding, hexadecimal character representation, string concatenation, and randomized variable names.[^380]  |
| [[StrelaStealer\|S1183]] | StrelaStealer | [StrelaStealer](https://attack.mitre.org/software/S1183) uses XOR-encoded strings to obfuscate items.[^581]  |
| [[Grandoreiro\|S0531]] | Grandoreiro | The [Grandoreiro](https://attack.mitre.org/software/S0531) payload has been delivered encrypted with a custom XOR-based algorithm and also as a base64-encoded ZIP file.[^116] [^117] [^117]  |
| [[Sakula\|S0074]] | Sakula | [Sakula](https://attack.mitre.org/software/S0074) uses single-byte XOR obfuscation to obfuscate many of its files.[^213]  |
| [[ZxxZ\|S1013]] | ZxxZ | [ZxxZ](https://attack.mitre.org/software/S1013) has been encoded to avoid detection from static analysis tools.[^280]  |
| [[Caminho\|S9016]] | Caminho | [Caminho](https://attack.mitre.org/software/S9016) can use code flattening for payload obfuscation.[^572]  |
| [[Shark\|S1019]] | Shark | [Shark](https://attack.mitre.org/software/S1019) can use encrypted and encoded files for C2 configuration.[^112] [^425]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) has used XOR, RSA2, and RC4 encrypted files.[^52] [^197] [^537]  |
| [[XLoader\|S1207]] | XLoader | [XLoader](https://attack.mitre.org/software/S1207) features encrypted functions using the RC4 algorithm and bytecode operations.[^361] [^588]  |
| [[HiddenFace\|S9023]] | HiddenFace | [HiddenFace](https://attack.mitre.org/software/S9023) has encrypted its payload with AES.[^342] [^436]  |
| [[CorKLOG\|S1235]] | CorKLOG | [CorKLOG](https://attack.mitre.org/software/S1235) has encrypted collected contents using RC4.[^118]   [CorKLOG](https://attack.mitre.org/software/S1235) has also utilized XOR encrypted strings.[^118]  |
| [[Kapeka\|S1190]] | Kapeka | [Kapeka](https://attack.mitre.org/software/S1190) utilizes AES-256 (CBC mode), XOR, and RSA-2048 encryption schemas for various configuration and other objects.[^15]  |
| [[SpeakUp\|S0374]] | SpeakUp | [SpeakUp](https://attack.mitre.org/software/S0374) encodes its second-stage payload with Base64. [^238]  |
| [[LunarMail\|S1142]] | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) has used RC4 and AES to encrypt strings and its exfiltration configuration respectively.[^420]  |
| [[HotCroissant\|S0431]] | HotCroissant | [HotCroissant](https://attack.mitre.org/software/S0431) has encrypted strings with single-byte XOR and base64 encoded RC4.[^113]  |
| [[REvil\|S0496]] | REvil | [REvil](https://attack.mitre.org/software/S0496) has used encrypted strings and configuration files.[^243] [^313] [^183] [^345] [^12] [^300] [^64]  |
| [[Milan\|S1015]] | Milan | [Milan](https://attack.mitre.org/software/S1015) can encode files containing information about the targeted system.[^112] [^104]  |
| [[USBStealer\|S0136]] | USBStealer | Most strings in [USBStealer](https://attack.mitre.org/software/S0136) are encrypted using 3DES and XOR and reversed.[^569]  |
| [[OSX_OCEANLOTUS.D\|S0352]] | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) encrypts its strings in RSA256 and encodes them in a custom base64 scheme and XOR.[^385]  |
| [[Taidoor\|S0011]] | Taidoor | [Taidoor](https://attack.mitre.org/software/S0011) can use encrypted string blocks for obfuscation.[^592]  |
| [[SUPERNOVA\|S0578]] | SUPERNOVA | [SUPERNOVA](https://attack.mitre.org/software/S0578) contained Base64-encoded strings.[^382]  |
| [[Seasalt\|S0345]] | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) obfuscates configuration data.[^596]  |
| [[Raccoon Stealer\|S1148]] | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) uses RC4 encryption for strings and command and control addresses to evade static detection.[^218] [^16] [^158]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) contains an embedded XML configuration file with an encrypted list of command and control servers. These are written to an external configuration file during execution.[^301]  |
| [[Cardinal RAT\|S0348]] | Cardinal RAT | [Cardinal RAT](https://attack.mitre.org/software/S0348) encodes many of its artifacts and is encrypted (AES-128) when downloaded.[^270]   |
| [[DanBot\|S1014]] | DanBot | [DanBot](https://attack.mitre.org/software/S1014) can Base64 encode its payload.[^196]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493)'s uninstaller has base64-encoded its variables. [^557]  |
| [[AshTag\|S9031]] | AshTag | The [AshTag](https://attack.mitre.org/software/S9031) AshenOrchestrator component payload as been Base64 encoded and embedded with HTML content from the C2 server.[^99]  |
| [[Carberp\|S0484]] | Carberp | [Carberp](https://attack.mitre.org/software/S0484) has used XOR-based encryption to mask C2 server locations within the trojan.[^368]  |
| [[FunnyDream\|S1044]] | FunnyDream | [FunnyDream](https://attack.mitre.org/software/S1044) can Base64 encode its C2 address stored in a template binary with the `xyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw_-` or<br>`xyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw_=` character sets.[^256]  |
| [[ROADSWEEP\|S1150]] | ROADSWEEP | The [ROADSWEEP](https://attack.mitre.org/software/S1150) binary contains RC4 encrypted embedded scripts.[^527] [^438] [^106]  |
| [[MOPSLED\|S1221]] | MOPSLED | [MOPSLED](https://attack.mitre.org/software/S1221) can encrypt configuration files with a custom ChaCha20 algorithm.[^135]  |
| [[More_eggs\|S0284]] | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284)'s payload has been encrypted with a key that has the hostname and processor family information appended to the end.[^594]  |
| [[SysUpdate\|S0663]] | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) can encrypt and encode its configuration file.[^146]  |
| [[ANELLDR\|S9027]] | ANELLDR | [ANELLDR](https://attack.mitre.org/software/S9027) can update its encryption key to AES-256-CBC and re-encrypt its payload, overwriting the original payload file with the newly encrypted data.[^2] <br> |
| [[Kwampirs\|S0236]] | Kwampirs | [Kwampirs](https://attack.mitre.org/software/S0236) downloads additional files that are base64-encoded and encrypted with another cipher.[^88]  |
| [[DEADEYE\|S1052]] | DEADEYE | [DEADEYE](https://attack.mitre.org/software/S1052) has encrypted its payload.[^497]  |
| [[Mango\|S1169]] | Mango | [Mango](https://attack.mitre.org/software/S1169) contains a series of base64 encoded substrings.[^35]  |
| [[Kessel\|S0487]] | Kessel | [Kessel](https://attack.mitre.org/software/S0487)'s configuration is hardcoded and RC4 encrypted within the binary.[^318]  |
| [[PHASEJAM\|S9014]] | PHASEJAM | [PHASEJAM](https://attack.mitre.org/software/S9014) has launched a webshell using the `MIME::Base64` module that encoded and decoded Base64 commands.[^289]  |
| [[YAHOYAH\|S0388]] | YAHOYAH | [YAHOYAH](https://attack.mitre.org/software/S0388) encrypts its configuration file using a simple algorithm.[^541]  |
| [[StealBit\|S1200]] | StealBit | [StealBit](https://attack.mitre.org/software/S1200) stores obfuscated DLL file names in its executable.[^387]  |
| [[FELIXROOT\|S0267]] | FELIXROOT | [FELIXROOT](https://attack.mitre.org/software/S0267) encrypts strings in the backdoor using a custom XOR algorithm.[^152] [^244]  |
| [[Penquin\|S0587]] | Penquin | [Penquin](https://attack.mitre.org/software/S0587) has encrypted strings in the binary for obfuscation.[^194]  |
| [[SPAWNCHIMERA\|S9024]] | SPAWNCHIMERA | [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has encoded a private key with XOR.[^551]  [SPAWNCHIMERA](https://attack.mitre.org/software/S9024) has also encrypted data to be extracted using AES encryption.[^283] [^582]  |
| [[Winnti for Windows\|S0141]] | Winnti for Windows | [Winnti for Windows](https://attack.mitre.org/software/S0141) has the ability to encrypt and compress its payload.[^521]  |
| [[njRAT\|S0385]] | njRAT | [njRAT](https://attack.mitre.org/software/S0385) has included a base64 encoded executable.[^157]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059)'s module file has been encrypted via XOR.[^390]  |
| [[Heyoka Backdoor\|S1027]] | Heyoka Backdoor | [Heyoka Backdoor](https://attack.mitre.org/software/S1027) can encrypt its payload.[^617]  |
| [[LunarWeb\|S1141]] | LunarWeb | The [LunarWeb](https://attack.mitre.org/software/S1141) install files have been encrypted with AES-256.[^420]  |
| [[XCSSET\|S0658]] | XCSSET | Older [XCSSET](https://attack.mitre.org/software/S0658) variants use `xxd` to encode modules. Later versions pass an `xxd` or `base64` encoded blob through multiple decoding stages to reconstruct the module name, AppleScript, or shell command. For example, the initial network request uses three layers of hex decoding before executing a curl command in a shell.[^39]  |
| [[Qilin\|S1242]] | Qilin | [Qilin](https://attack.mitre.org/software/S1242) can employ several code obfuscation methods, including renaming functions, altering control flows, and encrypting strings.[^68]  |
| [[STARWHALE\|S1037]] | STARWHALE | [STARWHALE](https://attack.mitre.org/software/S1037) has been obfuscated with hex-encoded strings.[^122]  |
| [[CozyCar\|S0046]] | CozyCar | The payload of [CozyCar](https://attack.mitre.org/software/S0046) is encrypted with simple XOR with a rotating key. The [CozyCar](https://attack.mitre.org/software/S0046) configuration file has been encrypted with RC4 keys.[^409]  |
| [[Kevin\|S1020]] | Kevin | [Kevin](https://attack.mitre.org/software/S1020) has Base64-encoded its configuration file.[^104]  |
| [[DRYHOOK\|S9013]] | DRYHOOK | [DRYHOOK](https://attack.mitre.org/software/S9013) has encrypted stolen credentials strings within a file using both Base64 and RC4 with a hard-coded key.[^289] [^582]  |
| [[Remexi\|S0375]] | Remexi | [Remexi](https://attack.mitre.org/software/S0375) obfuscates its configuration data with XOR.[^190]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) has used an XOR-based algorithm to encrypt payloads twice with different keys.[^116]  |
| [[DOWNIISSA\|S9021]] | DOWNIISSA | [DOWNIISSA](https://attack.mitre.org/software/S9021) code is base64 encoded and XOR encrypted.[^251]  |
| [[Helminth\|S0170]] | Helminth | The [Helminth](https://attack.mitre.org/software/S0170) config file is encrypted with RC4.[^137]  |
| [[DEADWOOD\|S1134]] | DEADWOOD | [DEADWOOD](https://attack.mitre.org/software/S1134) contains an embedded, AES-encrypted resource named `METADATA` that contains configuration information for follow-on execution.[^301]  |
| [[Waterbear\|S0579]] | Waterbear | [Waterbear](https://attack.mitre.org/software/S0579) has used RC4 encrypted shellcode and encrypted functions.[^290]  |
| [[FIVEHANDS\|S0618]] | FIVEHANDS | The [FIVEHANDS](https://attack.mitre.org/software/S0618) payload is encrypted with AES-128.[^480] [^489] [^348]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) has encrypted DMG files.[^46] 	 |
| [[BitPaymer\|S0570]] | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) has used RC4-encrypted strings and string hashes to avoid identifiable strings within the binary.[^56]  |
| [[Zox\|S0672]] | Zox | [Zox](https://attack.mitre.org/software/S0672) has been encoded with Base64.[^511]  |
| [[HiddenWasp\|S0394]] | HiddenWasp | [HiddenWasp](https://attack.mitre.org/software/S0394) encrypts its configuration and payload.[^520]  |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has encoded module names and C2 URLs as hexadecimal strings in attempts to evade analysis.[^60]  |
| [[HermeticWizard\|S0698]] | HermeticWizard | [HermeticWizard](https://attack.mitre.org/software/S0698) has the ability to encrypt PE files with a reverse XOR loop.[^524]  |
| [[Elderwood\|G0066]] | Elderwood | [Elderwood](https://attack.mitre.org/groups/G0066) has encrypted documents and malicious executables.[^32]  |
| [[APT-C-36\|G0099]] | APT-C-36 | [APT-C-36](https://attack.mitre.org/groups/G0099) has used encoded and obfuscated files, images, and executables.[^201] <br> |
| [[OilRig\|G0049]] | OilRig | [OilRig](https://attack.mitre.org/groups/G0049) has encrypted and encoded data in its malware, including by using base64.[^242] [^181] [^454] [^375] [^257]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded payloads to avoid detection.[^239]  |
| [[Lazarus Group\|G0032]] | Lazarus Group | [Lazarus Group](https://attack.mitre.org/groups/G0032) has used multiple types of encryption and encoding for their payloads, including AES, Caracachs, RC4, XOR, Base64, and other tricks such as creating aliases in code for [Native API](https://attack.mitre.org/techniques/T1106) function names.[^472] [^255] [^321] [^314] [^199] [^545] [^432]  |
| [[TeamTNT\|G0139]] | TeamTNT | [TeamTNT](https://attack.mitre.org/groups/G0139) has encrypted its binaries via AES and encoded files using Base64.[^589] [^273]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has password-protected malicious Word documents.[^272]  |
| [[Inception\|G0100]] | Inception | [Inception](https://attack.mitre.org/groups/G0100) has encrypted malware payloads dropped on victim machines with AES and RC4 encryption.[^93]  |
| [[Malteiro\|G1026]] | Malteiro | [Malteiro](https://attack.mitre.org/groups/G1026) has used scripts encoded in Base64 certificates to distribute malware to victims.[^222]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has obfuscated code within files by converting hexadecimal strings to decimal numbers using the `CLng function` in combination with processing arithmetic operations and leveraging the `Chr function` to generate readable characters.[^126]   [Kimsuky](https://attack.mitre.org/groups/G0094) has also encoded files with Base64 and RC4.[^126]  [Kimsuky](https://attack.mitre.org/groups/G0094) has utilized XOR and RC4 to encode malicious payloads.[^166]   |
| [[APT28\|G0007]] | APT28 | [APT28](https://attack.mitre.org/groups/G0007) encrypted a .dll payload using RTL and a custom encryption algorithm. [APT28](https://attack.mitre.org/groups/G0007) has also obfuscated payloads with base64, XOR, and RC4.[^13] [^43] [^391] [^69] [^463]  |
| [[Darkhotel\|G0012]] | Darkhotel | [Darkhotel](https://attack.mitre.org/groups/G0012) has obfuscated code using RC4, XOR, and RSA.[^134] [^427]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used base64-encoded files and has also encrypted embedded strings with AES.[^564] [^532]  |
| [[APT39\|G0087]] | APT39 | [APT39](https://attack.mitre.org/groups/G0087) has used malware to drop encrypted CAB files.[^195]  |
| [[Transparent Tribe\|G0134]] | Transparent Tribe | [Transparent Tribe](https://attack.mitre.org/groups/G0134) has dropped encoded executables on compromised hosts.[^138]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has performed code obfuscation, including encoding payloads using Base64 and using a framework called "Dont-Kill-My-Cat (DKMC). [APT32](https://attack.mitre.org/groups/G0050) also encrypts the library used for network exfiltration with AES-256 in CBC mode in their macOS backdoor.[^89] [^447] [^48] [^606] [^560] [^235] [^227]  |
| [[Leviathan\|G0065]] | Leviathan | [Leviathan](https://attack.mitre.org/groups/G0065) has obfuscated code using base64.[^558]  |
| [[Storm-1811\|G1046]] | Storm-1811 | [Storm-1811](https://attack.mitre.org/groups/G1046) XOR encodes a [Cobalt Strike](https://attack.mitre.org/software/S0154) installation payload in a DLL file that is decoded with a hardcoded key when called by a legitimate 7zip installation process.[^125]  |
| [[TA2541\|G1018]] | TA2541 | <br>[TA2541](https://attack.mitre.org/groups/G1018) has used compressed and char-encoded scripts in operations.[^350] <br> |
| [[BITTER\|G1002]] | BITTER | [BITTER](https://attack.mitre.org/groups/G1002) has used a RAR SFX dropper to deliver malware.[^47]  |
| [[menuPass\|G0045]] | menuPass | [menuPass](https://attack.mitre.org/groups/G0045) has encoded strings in its malware with base64 as well as with a simple, single-byte XOR obfuscation using key 0x40.[^108] [^320] [^401]  |
| [[Tropic Trooper\|G0081]] | Tropic Trooper | [Tropic Trooper](https://attack.mitre.org/groups/G0081) has encrypted configuration files.[^205] [^542]  |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) used Base64 to obfuscate payloads.[^65]  |
| [[Moses Staff\|G1009]] | Moses Staff | [Moses Staff](https://attack.mitre.org/groups/G1009) has used obfuscated web shells in their operations.[^355]  |
| [[MirrorFace\|G1054]] | MirrorFace | [MirrorFace](https://attack.mitre.org/groups/G1054) has used Base64 encoded shellcode in infection chains to evade detection.[^293]  |
| [[Group5\|G0043]] | Group5 | [Group5](https://attack.mitre.org/groups/G0043) disguised its malicious binaries with several layers of obfuscation, including encrypting the files.[^107]  |
| [[Saint Bear\|G1031]] | Saint Bear | [Saint Bear](https://attack.mitre.org/groups/G1031) initial payloads included encoded follow-on payloads located in the resources file of the first-stage loader.[^536]  |
| [[Blue Mockingbird\|G0108]] | Blue Mockingbird | [Blue Mockingbird](https://attack.mitre.org/groups/G0108) has obfuscated the wallet address in the payload binary.[^336]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has used hexadecimal string encoding to hide critical JavaScript module names, function names, and C2 URLs, which are decoded dynamically at runtime.[^469]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used base64 encoding and ECDH-P256 encryption for payloads.[^340] [^299] [^37]  |
| [[Higaisa\|G0126]] | Higaisa | [Higaisa](https://attack.mitre.org/groups/G0126) used Base64 encoded compressed payloads.[^123] [^450]  |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can encrypt payloads using XOR. [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware is also obfuscated using Metasploit’s shikata_ga_nai encoder.[^431] [^254] [^304]  |
| [[Moonstone Sleet\|G1036]] | Moonstone Sleet | [Moonstone Sleet](https://attack.mitre.org/groups/G1036) has used encrypted payloads within files for follow-on execution and defense evasion.[^250]  |
| [[Dark Caracal\|G0070]] | Dark Caracal | [Dark Caracal](https://attack.mitre.org/groups/G0070) has obfuscated strings in [Bandook](https://attack.mitre.org/software/S0234) by base64 encoding, and then encrypting them.[^419]  |
| [[Putter Panda\|G0024]] | Putter Panda | Droppers used by [Putter Panda](https://attack.mitre.org/groups/G0024) use RC4 or a 16-byte XOR key consisting of the bytes 0xA0 – 0xAF to obfuscate payloads.[^91]  |
| [[Metador\|G1013]] | Metador | [Metador](https://attack.mitre.org/groups/G1013) has encrypted their payloads.[^28]  |
| [[Mofang\|G0103]] | Mofang | [Mofang](https://attack.mitre.org/groups/G0103) has encrypted payloads before they are downloaded to victims.[^373]  |
| [[APT33\|G0064]] | APT33 | [APT33](https://attack.mitre.org/groups/G0064) has used base64 to encode payloads.[^326]  |
| [[Whitefly\|G0107]] | Whitefly | [Whitefly](https://attack.mitre.org/groups/G0107) has encrypted the payload used for C2.[^192] 	 |
| [[APT18\|G0026]] | APT18 | [APT18](https://attack.mitre.org/groups/G0026) obfuscates strings in the payload.[^337]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Behavior Prevention on Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10+, enable Attack Surface Reduction (ASR) rules to block execution of potentially obfuscated scripts.[^310] <br><br>Security tools should be configured to analyze the encoding properties of files and detect anomalies that deviate from standard encoding practices. |
| [[Antivirus／Antimalware\|M1049]] | Antivirus／Antimalware | Anti-virus can be used to automatically detect and quarantine suspicious files, including those with high entropy measurements or with otherwise potentially malicious signs of obfuscation. |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)


[^3]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^4]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^5]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^6]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^7]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^8]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^9]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)


[^10]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^11]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^12]: [Group IB Ransomware May 2020](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)


[^13]: [Bitdefender APT28 Dec 2015](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)


[^14]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^15]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)


[^16]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)


[^17]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^18]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^19]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^20]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^21]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^22]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^23]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^24]: [Palo Alto Networks, Unit 42](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)


[^25]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^26]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)


[^27]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^28]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)


[^29]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^30]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^31]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^32]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^33]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^34]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^35]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)


[^36]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^37]: [Cyble Sidewinder September 2020](https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/)


[^38]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)


[^39]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)


[^40]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^41]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)


[^42]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^43]: [Unit 42 Sofacy Feb 2018](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)


[^44]: [emotet_trendmicro_mar2023](https://www.trendmicro.com/en_us/research/23/c/emotet-returns-now-adopts-binary-padding-for-evasion.html)


[^45]: [Lotus Blossom Dec 2015](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)


[^46]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^47]: [Forcepoint BITTER Pakistan Oct 2016](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)


[^48]: [ESET OceanLotus](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)


[^49]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^50]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)


[^51]: [CloudSEK_RustyWater_Jan2026](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)


[^52]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)


[^53]: [Qualys LummaStealer 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)


[^54]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)


[^55]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^56]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)


[^57]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^58]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)


[^59]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^60]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^61]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^62]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^63]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^64]: [Secureworks REvil September 2019](https://www.secureworks.com/research/revil-sodinokibi-ransomware)


[^65]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^66]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^67]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)


[^68]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)


[^69]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)


[^70]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^71]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)


[^72]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^73]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^74]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^75]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^76]: [Proofpoint ZeroT Feb 2017](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)


[^77]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)


[^78]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^79]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^80]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^81]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^82]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^83]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^84]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^85]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^86]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^87]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^88]: [Symantec Security Center Trojan.Kwampirs](https://www.symantec.com/security-center/writeup/2016-081923-2700-99)


[^89]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^90]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^91]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^92]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^93]: [Kaspersky Cloud Atlas December 2014](https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/)


[^94]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^95]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)


[^96]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^97]: [File obfuscation](https://www.crowdstrike.com/blog/shlayer-malvertising-campaigns-still-using-flash-update-disguise/)


[^98]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^99]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)


[^100]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^101]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^102]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)


[^103]: [Microsoft Deep Dive Solorigate January 2021](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)


[^104]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^105]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^106]: [Microsoft Albanian Government Attacks September 2022](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)


[^107]: [Citizen Lab Group5](https://citizenlab.ca/2016/08/group5-syria/)


[^108]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)


[^109]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)


[^110]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)


[^111]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^112]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)


[^113]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)


[^114]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^115]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^116]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


[^117]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)


[^118]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


[^119]: [Palo Alto MidnightEclipse APR 2024](https://unit42.paloaltonetworks.com/cve-2024-3400/)


[^120]: [SFX - Encrypted/Encoded File](https://www.crowdstrike.com/blog/self-extracting-archives-decoy-files-and-their-hidden-payloads/)


[^121]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)


[^122]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^123]: [Malwarebytes Higaisa 2020](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)


[^124]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^125]: [rapid7-email-bombing](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)


[^126]: [Aryaka Kimsuky July 2025](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)


[^127]: [Proofpoint TA505 Jan 2019](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)


[^128]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^129]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^130]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^131]: [fsecure NanHaiShu July 2016](https://www.f-secure.com/documents/996508/1030745/nanhaishu_whitepaper.pdf)


[^132]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)


[^133]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^134]: [Securelist Darkhotel Aug 2015](https://securelist.com/darkhotels-attacks-in-2015/71713/)


[^135]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


[^136]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)


[^137]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^138]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^139]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)


[^140]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^141]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^142]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^143]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^144]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^145]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^146]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^147]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


[^148]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^149]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^150]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^151]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)


[^152]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)


[^153]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)


[^154]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^155]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^156]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^157]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)


[^158]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)


[^159]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^160]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^161]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^162]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)


[^163]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)


[^164]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^165]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^166]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)


[^167]: [FireEye FIN7 Oct 2019](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)


[^168]: [ESET Embargo Ransomware October 2024](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)


[^169]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)


[^170]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)


[^171]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^172]: [Securelist WhiteBear Aug 2017](https://securelist.com/introducing-whitebear/81638/)


[^173]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^174]: [Cybereason Kimsuky November 2020](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)


[^175]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^176]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)


[^177]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^178]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^179]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^180]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^181]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^182]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^183]: [McAfee Sodinokibi October 2019](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)


[^184]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^185]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^186]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)


[^187]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^188]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^189]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^190]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)


[^191]: [McAfee Sharpshooter December 2018](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)


[^192]: [Symantec Whitefly March 2019](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)


[^193]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^194]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)


[^195]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^196]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)


[^197]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^198]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^199]: [TrendMicro macOS Dacls May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)


[^200]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^201]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)


[^202]: [Trend Micro Tick November 2019](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)


[^203]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^204]: [Fidelis INOCNATION](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)


[^205]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)


[^206]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^207]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^208]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^209]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^210]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^211]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^212]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^213]: [Dell Sakula](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)


[^214]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^215]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^216]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)


[^217]: [Bromium Ursnif Mar 2017](https://www.bromium.com/how-ursnif-evades-detection/)


[^218]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)


[^219]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^220]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^221]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^222]: [SCILabs Malteiro Threat Overlap 2023](https://blog.scilabs.mx/en/ursa-mispadu-overlap-analysis-with-other-threats/)


[^223]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^224]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^225]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^226]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)


[^227]: [ESET OceanLotus macOS April 2019](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)


[^228]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^229]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^230]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^231]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^232]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)


[^233]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)


[^234]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^235]: [ESET OceanLotus Mar 2019](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)


[^236]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^237]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)


[^238]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)


[^239]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^240]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)


[^241]: [Donut Github](https://github.com/TheWover/donut)


[^242]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)


[^243]: [G Data Sodinokibi June 2019](https://www.gdatasoftware.com/blog/2019/06/31724-strange-bits-sodinokibi-spam-cinarat-and-fake-g-data)


[^244]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)


[^245]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^246]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^247]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^248]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^249]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^250]: [Microsoft Moonstone Sleet 2024](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)


[^251]: [Kaspersky LODEINFO OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)


[^252]: [US-CERT Volgmer 2 Nov 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)


[^253]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^254]: [Securelist LuckyMouse June 2018](https://securelist.com/luckymouse-hits-national-data-center/86083/)


[^255]: [Novetta Blockbuster Loaders](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)


[^256]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)


[^257]: [Unit42 OilRig Nov 2018](https://unit42.paloaltonetworks.com/unit42-analyzing-oilrigs-ops-tempo-testing-weaponization-delivery/)


[^258]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^259]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^260]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^261]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^262]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)


[^263]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^264]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^265]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^266]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^267]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


[^268]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)


[^269]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^270]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)


[^271]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^272]: [Proofpoint TA505 Sep 2017](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)


[^273]: [Aqua TeamTNT August 2020](https://blog.aquasec.com/container-security-tnt-container-attack)


[^274]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^275]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^276]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^277]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)


[^278]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)


[^279]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^280]: [Cisco Talos Bitter Bangladesh May 2022](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)


[^281]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^282]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^283]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^284]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^285]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^286]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^287]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^288]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)


[^289]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^290]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)


[^291]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^292]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^293]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)


[^294]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^295]: [CitizenLab KeyBoy Nov 2016](https://citizenlab.ca/2016/11/parliament-keyboy/)


[^296]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^297]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


[^298]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)


[^299]: [Rewterz Sidewinder APT April 2020](https://www.rewterz.com/threats/sidewinder-apt-group-campaign-analysis)


[^300]: [Picus Sodinokibi January 2020](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)


[^301]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^302]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)


[^303]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^304]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)


[^305]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)


[^306]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^307]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^308]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^309]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)


[^310]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^311]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^312]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)


[^313]: [Secureworks GandCrab and REvil September 2019](https://www.secureworks.com/blog/revil-the-gandcrab-connection)


[^314]: [McAfee Lazarus Resurfaces Feb 2018](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)


[^315]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^316]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^317]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^318]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


[^319]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^320]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)


[^321]: [Novetta Blockbuster RATs](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)


[^322]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^323]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^324]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^325]: [Cisco MagicRAT 2022](https://blog.talosintelligence.com/lazarus-magicrat/)


[^326]: [FireEye APT33 Guardrail](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)


[^327]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^328]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^329]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)


[^330]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^331]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^332]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^333]: [Latrodectus APR 2024](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)


[^334]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^335]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


[^336]: [RedCanary Mockingbird May 2020](https://redcanary.com/blog/blue-mockingbird-cryptominer/)


[^337]: [PaloAlto DNS Requests May 2016](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)


[^338]: [Palo Alto HeartCrypt DEC 2024](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)


[^339]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^340]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^341]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^342]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)


[^343]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^344]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^345]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)


[^346]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)


[^347]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


[^348]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)


[^349]: [ZScaler Squirrelwaffle Sep 2021](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)


[^350]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)


[^351]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)


[^352]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^353]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)


[^354]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^355]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)


[^356]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^357]: [Talos Smoke Loader July 2018](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)


[^358]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^359]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^360]: [RecordedFuture WhisperGate Jan 2022](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)


[^361]: [Zscaler XLoader 2025](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)


[^362]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^363]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^364]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^365]: [Google Cloud APT41 2022](https://cloud.google.com/blog/topics/threat-intelligence/apt41-us-state-governments)


[^366]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^367]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^368]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)


[^369]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)


[^370]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^371]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^372]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^373]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


[^374]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^375]: [Crowdstrike Helix Kitten Nov 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/)


[^376]: [US-CERT BLINDINGCAN Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)


[^377]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^378]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^379]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^380]: [sentinelone operationDigitalEye Dec 2024](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)


[^381]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^382]: [CISA Supernova Jan 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-027a)


[^383]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^384]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^385]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^386]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^387]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)


[^388]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^389]: [ESET Turla Mosquito Jan 2018](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)


[^390]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^391]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)


[^392]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


[^393]: [Unit 42 Bisonal July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)


[^394]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^395]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)


[^396]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^397]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^398]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^399]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^400]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^401]: [Symantec Cicada November 2020](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)


[^402]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^403]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^404]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


[^405]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^406]: [F-Secure Sofacy 2015](https://labsblog.f-secure.com/2015/09/08/sofacy-recycles-carberp-and-metasploit-code/)


[^407]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^408]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)


[^409]: [F-Secure CozyDuke](https://www.f-secure.com/documents/996508/1030745/CozyDuke)


[^410]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^411]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^412]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^413]: [SentinelOne SocGholish Infrastructure November 2022](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)


[^414]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^415]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^416]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^417]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^418]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^419]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^420]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^421]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)


[^422]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^423]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^424]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^425]: [Accenture Lyceum Targets November 2021](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)


[^426]: [Kaspersky ThreatNeedle Feb 2021](https://securelist.com/lazarus-threatneedle/100803/)


[^427]: [Microsoft DUBNIUM July 2016](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)


[^428]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^429]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)


[^430]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^431]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^432]: [Qualys LolZarus](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)


[^433]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^434]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^435]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^436]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^437]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^438]: [CISA Iran Albanian Attacks September 2022](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)


[^439]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^440]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^441]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^442]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^443]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)


[^444]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^445]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^446]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^447]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^448]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^449]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^450]: [Zscaler Higaisa 2020](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)


[^451]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^452]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^453]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^454]: [Unit42 OilRig Playbook 2023](https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)


[^455]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^456]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)


[^457]: [Unit 42 KerrDown February 2019](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)


[^458]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^459]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^460]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^461]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^462]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


[^463]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)


[^464]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^465]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^466]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)


[^467]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^468]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^469]: [Socket Contagious Interview NPM April 2025](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)


[^470]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^471]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^472]: [Novetta Blockbuster](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)


[^473]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^474]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)


[^475]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^476]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^477]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^478]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^479]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^480]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)


[^481]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^482]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)


[^483]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)


[^484]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^485]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^486]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)


[^487]: [Koi Glassworm New Tricks December 2025](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)


[^488]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^489]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)


[^490]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^491]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^492]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)


[^493]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^494]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^495]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^496]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^497]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)


[^498]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^499]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^500]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^501]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)


[^502]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)


[^503]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^504]: [Talos Micropsia June 2017](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)


[^505]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^506]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^507]: [Sentinel Labs LockBit 3.0 JUL 2022](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)


[^508]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^509]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^510]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^511]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^512]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^513]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^514]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


[^515]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^516]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^517]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)


[^518]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^519]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^520]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)


[^521]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)


[^522]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^523]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^524]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)


[^525]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^526]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^527]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)


[^528]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^529]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)


[^530]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)


[^531]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^532]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^533]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^534]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)


[^535]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^536]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^537]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)


[^538]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^539]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^540]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^541]: [TrendMicro TropicTrooper 2015](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)


[^542]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)


[^543]: [Netskope Squirrelwaffle Oct 2021](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)


[^544]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)


[^545]: [Lazarus APT January 2022](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)


[^546]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^547]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^548]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^549]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^550]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^551]: [JPCERT SPAWNCHIMERA Ivanti February 2025](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)


[^552]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^553]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^554]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)


[^555]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^556]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^557]: [Trustwave GoldenSpy2 June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/goldenspy-chapter-two-the-uninstaller/)


[^558]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)


[^559]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^560]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^561]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)


[^562]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)


[^563]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^564]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^565]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^566]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)


[^567]: [Juniper IcedID June 2020](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)


[^568]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^569]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)


[^570]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^571]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)


[^572]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)


[^573]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^574]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^575]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^576]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)


[^577]: [Talos SamSam Jan 2018](https://blog.talosintelligence.com/2018/01/samsam-evolution-continues-netting-over.html)


[^578]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^579]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^580]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)


[^581]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)


[^582]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^583]: [NCC Group WastedLocker June 2020](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)


[^584]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^585]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^586]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)


[^587]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^588]: [ANY.RUN XLoader 2023](https://any.run/cybersecurity-blog/xloader-formbook-encryption-analysis-and-malware-decryption/)


[^589]: [Trend Micro TeamTNT](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)


[^590]: [Malwarebytes SmokeLoader 2016](https://blog.malwarebytes.com/threat-analysis/2016/08/smoke-loader-downloader-with-a-smokescreen-still-alive/)


[^591]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^592]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)


[^593]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^594]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^595]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^596]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)


[^597]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^598]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^599]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)


[^600]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


[^601]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^602]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^603]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^604]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^605]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^606]: [Cybereason Oceanlotus May 2017](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)


[^607]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)


[^608]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^609]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)


[^610]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^611]: [CAL_MuddyWater_Mar2026](https://ctrlaltintel.com/research/MuddyWater/)


[^612]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^613]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^614]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^615]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)


[^616]: [Sophos SamSam Apr 2018](https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf)


[^617]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)


[^618]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^619]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^620]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


