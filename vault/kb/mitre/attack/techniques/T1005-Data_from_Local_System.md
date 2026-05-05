---
aliases: 
    - T1005
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1005-Data_from_Local_System
tactic: 
     - Collection
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.<br><br>Adversaries may do this using a [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|Command and Scripting Interpreter]], such as [[kb/mitre/attack/software/S0106-cmd\|cmd]] as well as a [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]], which have functionality to interact with the file system to gather information.[^16]  Adversaries may also use [[kb/mitre/attack/techniques/T1119-Automated_Collection\|Automated Collection]] on the local system.<br>


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0193-Forfiles\|S0193]] | Forfiles | [[kb/mitre/attack/software/S0193-Forfiles\|Forfiles]] can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).[^18]  |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^3] [^17]  |
| [[kb/mitre/attack/software/S0250-Koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-Koadic\|Koadic]] can download files off the target system to send back to the server.[^8] [^1]  |
| [[kb/mitre/attack/software/S0262-QuasarRAT\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-QuasarRAT\|QuasarRAT]] can retrieve files from compromised client machines.[^6]  |
| [[kb/mitre/attack/software/S0404-esentutl\|S0404]] | esentutl | [[kb/mitre/attack/software/S0404-esentutl\|esentutl]] can be used to collect data from local file systems.[^10]  |
| [[kb/mitre/attack/software/S0500-MCMD\|S0500]] | MCMD | [[kb/mitre/attack/software/S0500-MCMD\|MCMD]] has the ability to upload files from an infected device.[^12]  |
| [[kb/mitre/attack/software/S0594-Out1\|S0594]] | Out1 | [[kb/mitre/attack/software/S0594-Out1\|Out1]] can copy files and Registry data from compromised hosts.[^7]  |
| [[kb/mitre/attack/software/S0645-Wevtutil\|S0645]] | Wevtutil | [[kb/mitre/attack/software/S0645-Wevtutil\|Wevtutil]] can be used to export events from a specific log.[^11] [^15]  |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can collect files and information from a compromised host.[^13]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | <br>[[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has the ability to upload files from a compromised system.[^5]  |
| [[kb/mitre/attack/software/S1131-NPPSPY\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-NPPSPY\|NPPSPY]] records data entered from the local system logon at Winlogon to capture credentials in cleartext.[^4]  |
| [[kb/mitre/attack/software/S9009-TruffleHog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-TruffleHog\|TruffleHog]] has gathered data from home directories of the victim environment.[^2]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1057-Data_Loss_Prevention\|M1057]] | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |






> [!info]- References
> [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)

> [^2]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)

> [^3]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)

> [^4]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)

> [^5]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^6]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)

> [^7]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)

> [^8]: [Github Koadic](https://github.com/offsecginger/koadic)

> [^9]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^10]: [Red Canary 2021 Threat Detection Report March 2021](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)

> [^11]: [Wevtutil Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)

> [^12]: [Secureworks MCMD July 2019](https://www.secureworks.com/research/mcmd-malware-analysis)

> [^13]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^14]: [Mandiant APT41 Global Intrusion ](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)

> [^15]: [F-Secure Lazarus Cryptocurrency Aug 2020](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)

> [^16]: [show_run_config_cmd_cisco](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733)

> [^17]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^18]: [Überwachung APT28 Forfiles June 2015](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)


