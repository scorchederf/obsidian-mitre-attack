---
aliases: 
    - T1057
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1057-Process_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from [[kb/mitre/attack/techniques/T1057-Process_Discovery\|Process Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>In Windows environments, adversaries could obtain details on running processes using the [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] utility via [[kb/mitre/attack/software/S0106-cmd\|cmd]] or `Get-Process` via [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]]. Information about processes can also be extracted from the output of [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] calls such as `CreateToolhelp32Snapshot`. In Mac and Linux, this is accomplished with the `ps` command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.[^10] [^3] <br><br>On network devices, [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|Network Device CLI]] commands such as `show processes` can be used to display current running processes.[^8] [^6] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0057-Tasklist\|S0057]] | Tasklist | [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] can be used to discover processes running on a system.[^15]  |
| [[kb/mitre/attack/software/S0192-Pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-Pupy\|Pupy]] can list the running processes and get the process ID and parent process’s ID.[^13]  |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]]'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^5] [^14]  |
| [[kb/mitre/attack/software/S0332-Remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-Remcos\|Remcos]] can discover running processes on compromised machines.[^2] <br> |
| [[kb/mitre/attack/software/S0363-Empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-Empire\|Empire]] can find information about processes running on local and remote systems.[^18] [^1]  |
| [[kb/mitre/attack/software/S0434-Imminent_Monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-Imminent_Monitor\|Imminent Monitor]] has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.[^9]  |
| [[kb/mitre/attack/software/S0445-ShimRatReporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-ShimRatReporter\|ShimRatReporter]] listed all running processes on the machine.[^4]  |
| [[kb/mitre/attack/software/S0581-IronNetInjector\|S0581]] | IronNetInjector | [[kb/mitre/attack/software/S0581-IronNetInjector\|IronNetInjector]] can identify processes via C# methods such as `GetProcessesByName` and running [[kb/mitre/attack/software/S0057-Tasklist\|Tasklist]] with the Python `os.popen` function.[^19]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^11]  |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] includes subprojects that enumerate and identify information about [[kb/mitre/attack/techniques/T1055-Process_Injection\|Process Injection]] candidates.[^16] 	 |
| [[kb/mitre/attack/software/S1050-PcShare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-PcShare\|PcShare]] can obtain a list of running processes on a compromised host.[^12]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] can enumerate all processes and locate specific process IDs (PIDs).[^7]  |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can examine running processes to determine if a debugger is present.[^17]  |








> [!info]- References
> [^1]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)

> [^2]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)

> [^3]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)

> [^4]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)

> [^5]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)

> [^6]: [show_processes_cisco_cmd](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_monitor_permit_list_through_show_process_memory.html#wp3599497760)

> [^7]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)

> [^8]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)

> [^9]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)

> [^10]: [Sygnia ESXi Ransomware 2025](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)

> [^11]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^12]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)

> [^13]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)

> [^14]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^15]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)

> [^16]: [Donut Github](https://github.com/TheWover/donut)

> [^17]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^18]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)

> [^19]: [Unit 42 IronNetInjector February 2021 ](https://unit42.paloaltonetworks.com/ironnetinjector/)


