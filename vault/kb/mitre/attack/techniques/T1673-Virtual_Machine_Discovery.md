---
aliases: 
    - T1673
tags: 
    - attack/domain/enterprise_attack
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1673-Virtual_Machine_Discovery
tactic: 
     - Discovery
platforms:
     - ESXi - Linux - macOS - Windows
permissions required:
     - none
---

## Description

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [[kb/mitre/attack/techniques/T1059.012-Hypervisor_CLI\|Hypervisor CLI]] such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).[^2] [^1]  Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1673-Virtual_Machine_Discovery\|Virtual Machine Discovery]] during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as [[kb/mitre/attack/techniques/T1489-Service_Stop\|Service Stop]] or [[kb/mitre/attack/techniques/T1486-Data_Encrypted_for_Impact\|Data Encrypted for Impact]].[^2] 








> [!info]- References
> [^1]: [TrendMicro Play](https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html)

> [^2]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


