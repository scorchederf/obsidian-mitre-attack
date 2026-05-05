---
aliases: 
    - S0451
    
mitre-attack: https://attack.mitre.org/software/S0451
---

## S0451

[LoudMiner](https://attack.mitre.org/software/S0451) is a cryptocurrency miner which uses virtualization software to siphon system resources. The miner has been bundled with pirated copies of Virtual Studio Technology (VST) for Windows and macOS.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [LoudMiner](https://attack.mitre.org/software/S0451) used the `ps` command to monitor the running processes on the system.[^1] 	 |
| [[Launchctl\|T1569.001]] | Launchctl | [LoudMiner](https://attack.mitre.org/software/S0451) launched the QEMU services in the `/Library/LaunchDaemons/` folder using `launchctl`. It also uses `launchctl` to unload all [Launch Daemon](https://attack.mitre.org/techniques/T1543/004)s when updating to a newer version of [LoudMiner](https://attack.mitre.org/software/S0451).[^1] 	 |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [LoudMiner](https://attack.mitre.org/software/S0451) has obfuscated various scripts.[^1] 	 |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [LoudMiner](https://attack.mitre.org/software/S0451) has encrypted DMG files.[^1] 	 |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [LoudMiner](https://attack.mitre.org/software/S0451) has set the attributes of the VirtualBox directory and VBoxVmService parent directory to "hidden".[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [LoudMiner](https://attack.mitre.org/software/S0451) used shell scripts to launch various services and to start/stop the QEMU virtualization.[^1] 	 |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [LoudMiner](https://attack.mitre.org/software/S0451) adds plist files with the naming format `com.[random_name].plist` in the `/Library/LaunchDaemons` folder with the RunAtLoad and KeepAlive keys set to `true`.[^1]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [LoudMiner](https://attack.mitre.org/software/S0451) harvested system resources to mine cryptocurrency, using XMRig to mine Monero.[^1] 	 |
| [[Windows Service\|T1543.003]] | Windows Service | [LoudMiner](https://attack.mitre.org/software/S0451) can automatically launch a Linux virtual machine as a service at startup if the AutoStart option is enabled in the VBoxVmService configuration file.[^1]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [LoudMiner](https://attack.mitre.org/software/S0451) is typically bundled with pirated copies of Virtual Studio Technology (VST) for Windows and macOS.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LoudMiner](https://attack.mitre.org/software/S0451) used a script to gather the IP address of the infected machine before sending to the C2.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LoudMiner](https://attack.mitre.org/software/S0451) used SCP to update the miner from the C2.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [LoudMiner](https://attack.mitre.org/software/S0451) started the cryptomining virtual machine as a service on the infected machine.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [LoudMiner](https://attack.mitre.org/software/S0451) deleted installation files after completion.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LoudMiner](https://attack.mitre.org/software/S0451) has monitored CPU usage.[^1] 	 |
| [[Run Virtual Instance\|T1564.006]] | Run Virtual Instance | [LoudMiner](https://attack.mitre.org/software/S0451) has used QEMU and VirtualBox to run a Tiny Core Linux virtual machine, which runs XMRig and makes connections to the C2 server for updates.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [LoudMiner](https://attack.mitre.org/software/S0451) used an MSI installer to install the virtualization software.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LoudMiner](https://attack.mitre.org/software/S0451) used a batch script to run the Linux virtual machine as a service.[^1]  |




## References

[^1]: [ESET LoudMiner June 2019](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)


