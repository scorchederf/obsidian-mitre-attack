---
aliases: 
    - T1027.010
mitre-attack: https://attack.mitre.org/techniques/T1027/010
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1027.010

Adversaries may obfuscate content during command execution to impede detection. Command-line obfuscation is a method of making strings and patterns within commands and scripts more difficult to signature and analyze. This type of obfuscation can be included within commands executed by delivered payloads (e.g., [Phishing](https://attack.mitre.org/techniques/T1566) and [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)) or interactively via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059).[^72] [^231] <br><br>For example, adversaries may abuse syntax that utilizes various symbols and escape characters (such as spacing,  `^`, `+`. `$`, and `%`) to make commands difficult to analyze while maintaining the same intended functionality.[^37]  Many languages support built-in obfuscation in the form of base64 or URL encoding.[^320]  Adversaries may also manually implement command obfuscation via string splitting (`“Wor”+“d.Application”`), order and casing of characters (`rev <<<'dwssap/cte/ tac'`), globing (`mkdir -p '/tmp/:&$NiA'`), as well as various tricks involving passing strings through tokens/environment variables/input streams.[^60] [^288] <br><br>Adversaries may also use tricks such as directory traversals to obfuscate references to the binary being invoked by a command (`C:\voi\pcw\..\..\Windows\tei\qs\k\..\..\..\system32\erool\..\wbem\wg\je\..\..\wmic.exe shadowcopy delete`).[^365] <br><br>Tools such as `Invoke-Obfuscation` and `Invoke-DOSfucation` have also been used to obfuscate commands.[^100] [^225] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[PowerSploit\|S0194]] | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of ScriptModification modules that compress and encode scripts and payloads.[^119] [^250]  |
| [[Empire\|S0363]] | Empire | [Empire](https://attack.mitre.org/software/S0363) has the ability to obfuscate commands using `Invoke-Obfuscation`.[^142]  |
| [[IronWind\|S9029]] | IronWind | [IronWind](https://attack.mitre.org/software/S9029) has used Base64 encoding and XOR encryption with the key “53” to obfuscate command strings.[^89]  |
| [[Sardonic\|S1085]] | Sardonic | [Sardonic](https://attack.mitre.org/software/S1085) PowerShell scripts can be encrypted with RC4 and compressed using Gzip.[^34]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) droppers execute base64 encoded [PowerShell](https://attack.mitre.org/techniques/T1059/001) commands.[^148]  |
| [[Tsundere Botnet\|S9034]] | Tsundere Botnet | [Tsundere Botnet](https://attack.mitre.org/software/S9034)’s MSI installer has Base64-encoded command execution.[^339]  |
| [[Zeus Panda\|S0330]] | Zeus Panda | [Zeus Panda](https://attack.mitre.org/software/S0330) obfuscates the macro commands in its initial payload.[^203]  |
| [[Havoc\|S1229]] | Havoc | [Havoc](https://attack.mitre.org/software/S1229) has utilized XOR encryption with the key “01-01-1900” to obfuscate command strings.[^89]  |
| [[CARROTBAT\|S0462]] | CARROTBAT | [CARROTBAT](https://attack.mitre.org/software/S0462) has the ability to execute obfuscated commands on the infected host.[^353]  |
| [[Emotet\|S0367]] | Emotet | [Emotet](https://attack.mitre.org/software/S0367) has obfuscated macros within malicious documents to hide the URLs hosting the malware,  CMD.exe arguments, and PowerShell scripts. [^135] [^379] [^285] [^249]  |
| [[BADHATCH\|S1081]] | BADHATCH | [BADHATCH](https://attack.mitre.org/software/S1081) malicious PowerShell commands can be encoded with base64.[^234]   |
| [[Machete\|S0409]] | Machete | [Machete](https://attack.mitre.org/software/S0409) has used pyobfuscate, zlib compression, and base64 encoding for obfuscation. [Machete](https://attack.mitre.org/groups/G0095) has also used some visual obfuscation techniques by naming variables as combinations of letters to hinder analysis.[^258] [^136]  |
| [[FruitFly\|S0277]] | FruitFly | [FruitFly](https://attack.mitre.org/software/S0277) executes and stores obfuscated Perl scripts.[^295]  |
| [[DarkWatchman\|S0673]] | DarkWatchman | [DarkWatchman](https://attack.mitre.org/software/S0673) has used Base64 to encode PowerShell commands.[^162]  |
| [[SHARPSTATS\|S0450]] | SHARPSTATS | [SHARPSTATS](https://attack.mitre.org/software/S0450) has used base64 encoding and XOR to obfuscate PowerShell scripts.[^256]  |
| [[Netwalker\|S0457]] | Netwalker | [Netwalker](https://attack.mitre.org/software/S0457)'s PowerShell script has been obfuscated with multiple layers including base64 and hexadecimal encoding and XOR-encryption, as well as obfuscated PowerShell functions and variables.[^74] [^325]  |
| [[QUADAGENT\|S0269]] | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) was likely obfuscated using `Invoke-Obfuscation`.[^122] [^302]  |
| [[RedLine Stealer\|S1240]] | RedLine Stealer | [RedLine Stealer](https://attack.mitre.org/software/S1240) has obfuscated scripts within text files used in execution.[^179]  |
| [[RogueRobin\|S0270]] | RogueRobin | The PowerShell script with the [RogueRobin](https://attack.mitre.org/software/S0270) payload was obfuscated using the COMPRESS technique in `Invoke-Obfuscation`.[^283] [^302]  |
| [[SQLRat\|S0390]] | SQLRat | [SQLRat](https://attack.mitre.org/software/S0390) has used a character insertion obfuscation technique, making the script appear to contain Chinese characters.[^29]  |
| [[Sibot\|S0589]] | Sibot | [Sibot](https://attack.mitre.org/software/S0589) has obfuscated scripts used in execution.[^223]  |
| [[BackConfig\|S0475]] | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) has used compressed and decimal encoded VBS scripts.[^267]  |
| [[PHASEJAM\|S9014]] | PHASEJAM | [PHASEJAM](https://attack.mitre.org/software/S9014) has encoded commands with Base64.[^193]  |
| [[PoetRAT\|S0428]] | PoetRAT | [PoetRAT](https://attack.mitre.org/software/S0428) has `pyminifier` to obfuscate scripts.[^84]  |
| [[PowerPunch\|S0685]] | PowerPunch | [PowerPunch](https://attack.mitre.org/software/S0685) can use Base64-encoded scripts.[^33]  |
| [[ComRAT\|S0126]] | ComRAT | [ComRAT](https://attack.mitre.org/software/S0126) has used encryption and base64 to obfuscate its orchestrator code in the Registry. [ComRAT](https://attack.mitre.org/software/S0126) has also used encoded PowerShell scripts.[^106] [^408]   |
| [[IceApple\|S1022]] | IceApple | [IceApple](https://attack.mitre.org/software/S1022) can use Base64 and "junk" JavaScript code to obfuscate information.[^342]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [KOCTOPUS](https://attack.mitre.org/software/S0669) has obfuscated scripts with the BatchEncryption tool.[^70]  |
| [[POWERSTATS\|S0223]] | POWERSTATS | [POWERSTATS](https://attack.mitre.org/software/S0223) uses character replacement, [PowerShell](https://attack.mitre.org/techniques/T1059/001) environment variables, and XOR encoding to obfuscate code. [POWERSTATS](https://attack.mitre.org/software/S0223)'s backdoor code is a multi-layer obfuscated, encoded, and compressed blob. [^227] [^78]  [POWERSTATS](https://attack.mitre.org/software/S0223) has used PowerShell code with custom string obfuscation [^256]  |
| [[Astaroth\|S0373]] | Astaroth | [Astaroth](https://attack.mitre.org/software/S0373) has obfuscated and randomized parts of the JScript code it is initiating.[^132]  |
| [[QakBot\|S0650]] | QakBot | [QakBot](https://attack.mitre.org/software/S0650) can use obfuscated and encoded scripts.[^65] [^363]  |
| [[CookieMiner\|S0492]] | CookieMiner | [CookieMiner](https://attack.mitre.org/software/S0492) has used base64 encoding to obfuscate scripts on the system.[^308]   |
| [[Denis\|S0354]] | Denis | [Denis](https://attack.mitre.org/software/S0354) has encoded its PowerShell commands in Base64.[^381]  |
| [[LoudMiner\|S0451]] | LoudMiner | [LoudMiner](https://attack.mitre.org/software/S0451) has obfuscated various scripts.[^32] 	 |
| [[XORIndex Loader\|S1248]] | XORIndex Loader | [XORIndex Loader](https://attack.mitre.org/software/S1248) has obfuscated strings using ASCII buffers and TextDecoder.[^40]  |
| [[Medusa Group\|G1051]] | Medusa Group | [Medusa Group](https://attack.mitre.org/groups/G1051) has obfuscated PowerShell scripts with Base64 encoding.[^25]  [Medusa Group](https://attack.mitre.org/groups/G1051) has also obfuscated the code of dropped kernel drivers using a software known as Safengine Shielden which randomized the code through code mutations and then leveraged an embedded virtual machine interpreter to execute the code.[^23]  |
| [[Wizard Spider\|G0102]] | Wizard Spider | [Wizard Spider](https://attack.mitre.org/groups/G0102) used Base64 encoding to obfuscate an [Empire](https://attack.mitre.org/software/S0363) service and PowerShell commands.[^293] [^382]  |
| [[FIN7\|G0046]] | FIN7 | [FIN7](https://attack.mitre.org/groups/G0046) has used fragmented strings, environment variables, standard input (stdin), and native character-replacement functionalities to obfuscate commands.[^288] [^244] [^257]  |
| [[WIRTE\|G0090]] | WIRTE | [WIRTE](https://attack.mitre.org/groups/G0090) has XOR encrypted command line strings to conceal malware execution chains.[^89]  |
| [[Fox Kitten\|G0117]] | Fox Kitten | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded scripts to avoid detection.[^164]  |
| [[Aquatic Panda\|G0143]] | Aquatic Panda | [Aquatic Panda](https://attack.mitre.org/groups/G0143) has encoded PowerShell commands in Base64.[^387]  |
| [[TA505\|G0092]] | TA505 | [TA505](https://attack.mitre.org/groups/G0092) has used base64 encoded PowerShell commands.[^159] [^71]  |
| [[Kimsuky\|G0094]] | Kimsuky | [Kimsuky](https://attack.mitre.org/groups/G0094) has encoded malicious PowerShell scripts using Base64.[^112]  |
| [[Play\|G1040]] | Play | [Play](https://attack.mitre.org/groups/G1040) has used Base64-encoded PowerShell scripts for post exploit activities on compromised hosts.[^182]  |
| [[Sandworm Team\|G0034]] | Sandworm Team | [Sandworm Team](https://attack.mitre.org/groups/G0034) has used ROT13 encoding, AES encryption and compression with the zlib library for their Python-based backdoor.[^36]  |
| [[Turla\|G0010]] | Turla | [Turla](https://attack.mitre.org/groups/G0010) has used encryption (including salted 3DES via [PowerSploit](https://attack.mitre.org/software/S0194)'s `Out-EncryptedScript.ps1`), random variable names, and base64 encoding to obfuscate PowerShell commands and payloads.[^240]  |
| [[FIN6\|G0037]] | FIN6 | [FIN6](https://attack.mitre.org/groups/G0037) has used encoded PowerShell commands.[^329]  |
| [[Silence\|G0091]] | Silence | [Silence](https://attack.mitre.org/groups/G0091) has used environment variable string substitution for obfuscation.[^259]  |
| [[Patchwork\|G0040]] | Patchwork | [Patchwork](https://attack.mitre.org/groups/G0040) has obfuscated a script with Crypto Obfuscator.[^163]  |
| [[HEXANE\|G1001]] | HEXANE | [HEXANE](https://attack.mitre.org/groups/G1001) has used Base64-encoded scripts.[^76]  |
| [[Leafminer\|G0077]] | Leafminer | [Leafminer](https://attack.mitre.org/groups/G0077) obfuscated scripts that were used on victim machines.[^83]  |
| [[Magic Hound\|G0059]] | Magic Hound | [Magic Hound](https://attack.mitre.org/groups/G0059) has used base64-encoded commands.[^384] [^361]  |
| [[Cobalt Group\|G0080]] | Cobalt Group | [Cobalt Group](https://attack.mitre.org/groups/G0080) obfuscated several scriptlets and code used on the victim’s machine, including through use of XOR and RC4.[^391] [^300]  |
| [[MuddyWater\|G0069]] | MuddyWater | [MuddyWater](https://attack.mitre.org/groups/G0069) has used Daniel Bohannon’s Invoke-Obfuscation framework and obfuscated PowerShell scripts.[^118] [^302]  The group has also used other obfuscation methods, including Base64 obfuscation of VBScripts and PowerShell commands.[^118] [^227] [^378] [^216] [^206] [^296] [^124]  |
| [[APT32\|G0050]] | APT32 | [APT32](https://attack.mitre.org/groups/G0050) has used the `Invoke-Obfuscation` framework to obfuscate their PowerShell.[^63] [^302] [^381]  |
| [[Chimera\|G0114]] | Chimera | [Chimera](https://attack.mitre.org/groups/G0114) has encoded PowerShell commands.[^10] 	 |
| [[APT19\|G0073]] | APT19 | [APT19](https://attack.mitre.org/groups/G0073) used Base64 to obfuscate executed commands.[^45]  |
| [[FIN8\|G0061]] | FIN8 | [FIN8](https://attack.mitre.org/groups/G0061) has used environment variables and standard input (stdin) to obfuscate command-line arguments. [FIN8](https://attack.mitre.org/groups/G0061) also obfuscates malicious macros delivered as payloads.[^288] [^120] [^103]  |
| [[Contagious Interview\|G1052]] | Contagious Interview | [Contagious Interview](https://attack.mitre.org/groups/G1052) has obfuscated JavaScript code using Base64 and variable substitutions.[^44] [^80] [^130] [^92]  |
| [[Sidewinder\|G0121]] | Sidewinder | [Sidewinder](https://attack.mitre.org/groups/G0121) has used base64 encoding for scripts.[^221] [^198]  |
| [[Gamaredon Group\|G0047]] | Gamaredon Group | [Gamaredon Group](https://attack.mitre.org/groups/G0047) has used obfuscated or encrypted scripts.[^97] [^33] [^9] [^313]     |
| [[TA551\|G0127]] | TA551 | [TA551](https://attack.mitre.org/groups/G0127) has used obfuscated variable names in a JavaScript configuration file.[^224]  |
| [[GOLD SOUTHFIELD\|G0115]] | GOLD SOUTHFIELD | [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) has executed base64 encoded PowerShell scripts on compromised hosts.[^350]  |
| [[LazyScripter\|G0140]] | LazyScripter | [LazyScripter](https://attack.mitre.org/groups/G0140) has leveraged the BatchEncryption tool to perform advanced batch script obfuscation and encoding techniques.[^70]  |




### Mitigations
| ID | Name | Descrption |
| --- | --- | --- |
| [[Behavior Prevention on Endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10+, enable Attack Surface Reduction (ASR) rules to block execution of potentially obfuscated scripts.[^243]  |
| [[Antivirus／Antimalware\|M1049]] | Antivirus／Antimalware | Consider utilizing the Antimalware Scan Interface (AMSI) on Windows 10+ to analyze commands after being processed/interpreted.  |




### Sub-techniques
| ID | Name |
| --- | --- |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation |



## References

[^1]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^2]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^3]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^4]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^5]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^6]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^7]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^8]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^9]: [SymantecCarbonBlack_ShuckwormUSB_Apr2025](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)


[^10]: [Cycraft Chimera April 2020](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)


[^11]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^12]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^13]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^14]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^15]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^16]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^17]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^18]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^19]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^20]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^21]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^22]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^23]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)


[^24]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^25]: [CISA Medusa Group Medusa Ransomware March 2025](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)


[^26]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^27]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^28]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^29]: [Flashpoint FIN 7 March 2019](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)


[^30]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^31]: [Unit 42 Global Incident Response Report 2026](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)


[^32]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


[^33]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)


[^34]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)


[^35]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^36]: [ESET Telebots Dec 2016](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)


[^37]: [RC PowerShell](https://redcanary.com/threat-detection-report/techniques/powershell/)


[^38]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^39]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^40]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)


[^41]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^42]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^43]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^44]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)


[^45]: [FireEye APT19](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)


[^46]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^47]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^48]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^49]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^50]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^51]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^52]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^53]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^54]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^55]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^56]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^57]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^58]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^59]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^60]: [Bashfuscator Command Obfuscators](https://bashfuscator.readthedocs.io/en/latest/Mutators/command_obfuscators/index.html)


[^61]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^62]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^63]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)


[^64]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^65]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)


[^66]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^67]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^68]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^69]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^70]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


[^71]: [Deep Instinct TA505 Apr 2019](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)


[^72]: [Akamai JS](https://www.akamai.com/blog/security/catch-me-if-you-can-javascript-obfuscation)


[^73]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^74]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)


[^75]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^76]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)


[^77]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^78]: [ClearSky MuddyWater Nov 2018](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)


[^79]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^80]: [SecurityScorecard Contagious Interview October 2024](https://securityscorecard.com/blog/inside-a-north-korean-phishing-operation-targeting-devops-employees/)


[^81]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^82]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^83]: [Symantec Leafminer July 2018](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)


[^84]: [Talos PoetRAT October 2020](https://blog.talosintelligence.com/2020/10/poetrat-update.html)


[^85]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^86]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^87]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^88]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^89]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)


[^90]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^91]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^92]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)


[^93]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^94]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^95]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^96]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^97]: [ESET Gamaredon June 2020](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)


[^98]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^99]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^100]: [Invoke-DOSfuscation](https://github.com/danielbohannon/Invoke-DOSfuscation)


[^101]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^102]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^103]: [Bitdefender FIN8 July 2021](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)


[^104]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^105]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^106]: [ESET ComRAT May 2020](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)


[^107]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^108]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^109]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^110]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^111]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^112]: [Securonix Kimsuky February 2025](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)


[^113]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^114]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^115]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^116]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^117]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^118]: [Unit 42 MuddyWater Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-muddying-the-water-targeted-attacks-in-the-middle-east/)


[^119]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


[^120]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


[^121]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^122]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)


[^123]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^124]: [Talos MuddyWater Jan 2022](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)


[^125]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^126]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^127]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^128]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^129]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^130]: [Securonix Contagious Interview DEVPOPPER April 2024](https://www.securonix.com/blog/analysis-of-devpopper-new-attack-campaign-targeting-software-developers-likely-associated-with-north-korean-threat-actors/)


[^131]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^132]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)


[^133]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^134]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^135]: [Talos Emotet Jan 2019](https://blog.talosintelligence.com/2019/01/return-of-emotet.html)


[^136]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)


[^137]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^138]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^139]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^140]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^141]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^142]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)


[^143]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^144]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^145]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^146]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^147]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^148]: [Bromium Ursnif Mar 2017](https://www.bromium.com/how-ursnif-evades-detection/)


[^149]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^150]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^151]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^152]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^153]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^154]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^155]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^156]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^157]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^158]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^159]: [Cybereason TA505 April 2019](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)


[^160]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^161]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^162]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)


[^163]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)


[^164]: [CISA AA20-259A Iran-Based Actor September 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)


[^165]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^166]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^167]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^168]: [W3C](https://www.w3.org/TR/fingerprinting-guidance/)


[^169]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^170]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^171]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^172]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^173]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^174]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^175]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^176]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^177]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^178]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^179]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)


[^180]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^181]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^182]: [Trend Micro Ransomware Spotlight Play July 2023](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)


[^183]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^184]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^185]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^186]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^187]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^188]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^189]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^190]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^191]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^192]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^193]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^194]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^195]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^196]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^197]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^198]: [Rewterz Sidewinder APT April 2020](https://www.rewterz.com/threats/sidewinder-apt-group-campaign-analysis)


[^199]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^200]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^201]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^202]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^203]: [Talos Zeus Panda Nov 2017](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)


[^204]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^205]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^206]: [ClearSky MuddyWater June 2019](https://www.clearskysec.com/wp-content/uploads/2019/06/Clearsky-Iranian-APT-group-%E2%80%98MuddyWater%E2%80%99-Adds-Exploits-to-Their-Arsenal.pdf)


[^207]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^208]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^209]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^210]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^211]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^212]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^213]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^214]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^215]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^216]: [Talos MuddyWater May 2019](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)


[^217]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^218]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^219]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^220]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^221]: [ATT Sidewinder January 2021](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)


[^222]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^223]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^224]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)


[^225]: [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^226]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^227]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)


[^228]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^229]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^230]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^231]: [Malware Monday VBE](https://bromiley.medium.com/malware-monday-vbscript-and-vbe-files-292252c1a16)


[^232]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^233]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^234]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)


[^235]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^236]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^237]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^238]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^239]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^240]: [ESET Turla PowerShell May 2019](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)


[^241]: [Sophos User Interaction](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)


[^242]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^243]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^244]: [FireEye FIN7 Aug 2018](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)


[^245]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^246]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^247]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^248]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^249]: [ESET Emotet Dec 2018](https://www.welivesecurity.com/2018/12/28/analysis-latest-emotet-propagation-campaign/)


[^250]: [PowerSploit Documentation](http://powersploit.readthedocs.io)


[^251]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^252]: [Defending Against Malicious Cyber Activity Originating from Tor](https://www.cisa.gov/sites/default/files/publications/AA20-183A_Defending_Against_Malicious_Cyber_Activity_Originating_from_Tor_S508C.pdf)


[^253]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^254]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^255]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^256]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)


[^257]: [CrowdStrike Carbon Spider August 2021](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)


[^258]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)


[^259]: [Cyber Forensicator Silence Jan 2019](https://web.archive.org/web/20220119133748/https://cyberforensicator.com/2019/01/20/silence-dissecting-malicious-chm-files-and-performing-forensic-analysis/)


[^260]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^261]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^262]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^263]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^264]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^265]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^266]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^267]: [Unit 42 BackConfig May 2020](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)


[^268]: [Proofpoint TA427 April 2024](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)


[^269]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^270]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^271]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^272]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^273]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^274]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^275]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^276]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^277]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^278]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^279]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^280]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^281]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^282]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^283]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)


[^284]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^285]: [Picus Emotet Dec 2018](https://www.picussecurity.com/blog/the-christmas-card-you-never-wanted-a-new-wave-of-emotet-is-back-to-wreak-havoc.html)


[^286]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^287]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^288]: [FireEye Obfuscation June 2017](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)


[^289]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^290]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^291]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^292]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^293]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)


[^294]: [SE SentinelOne 2](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)


[^295]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^296]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)


[^297]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^298]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^299]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^300]: [Morphisec Cobalt Gang Oct 2018](https://blog.morphisec.com/cobalt-gang-2.0)


[^301]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^302]: [GitHub Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


[^303]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^304]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^305]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^306]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^307]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^308]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)


[^309]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^310]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^311]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^312]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^313]: [ESET Gamaredon Sept2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)


[^314]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^315]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^316]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^317]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^318]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^319]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^320]: [Microsoft PowerShellB64](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1#-encodedcommand-base64encodedcommand)


[^321]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^322]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^323]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^324]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^325]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)


[^326]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^327]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^328]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^329]: [Visa FIN6 Feb 2019](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)


[^330]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^331]: [Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack)


[^332]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^333]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^334]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^335]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^336]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^337]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^338]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^339]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)


[^340]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^341]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^342]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)


[^343]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^344]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^345]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^346]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^347]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^348]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^349]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^350]: [Tetra Defense Sodinokibi March 2020](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)


[^351]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^352]: [SE - Hackers Target Workday](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)


[^353]: [Unit 42 CARROTBAT November 2018](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)


[^354]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^355]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^356]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^357]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^358]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^359]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^360]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^361]: [Microsoft Iranian Threat Actor Trends November 2021](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)


[^362]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^363]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)


[^364]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^365]: [Twitter Richard WMIC](https://x.com/rfackroyd/status/1639136000755765254)


[^366]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^367]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^368]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^369]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^370]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^371]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^372]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^373]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^374]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^375]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^376]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^377]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^378]: [Securelist MuddyWater Oct 2018](https://securelist.com/muddywater/88059/)


[^379]: [Trend Micro Emotet Jan 2019](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)


[^380]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^381]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)


[^382]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)


[^383]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^384]: [Unit 42 Magic Hound Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)


[^385]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^386]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^387]: [CrowdStrike AQUATIC PANDA December 2021](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)


[^388]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^389]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^390]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^391]: [Talos Cobalt Group July 2018](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)


[^392]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^393]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^394]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^395]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^396]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^397]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^398]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^399]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^400]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^401]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^402]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^403]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^404]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^405]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^406]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^407]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^408]: [CISA ComRAT Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)


[^409]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^410]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^411]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^412]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^413]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^414]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^415]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


