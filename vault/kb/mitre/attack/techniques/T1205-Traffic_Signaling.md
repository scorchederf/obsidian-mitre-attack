---
aliases: 
    - T1205
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/tactic/persistence
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1205-Traffic_Signaling
tactic: 
     - Stealth - Persistence - Command and Control
platforms:
     - Linux - macOS - Network Devices - Windows
permissions required:
     - none
---

## Description

Adversaries may use traffic signaling to hide open ports or other malicious functionality used for persistence or command and control. Traffic signaling involves the use of a magic value or sequence that must be sent to a system to trigger a special response, such as opening a closed port or executing a malicious task. This may take the form of sending a series of packets with certain characteristics before a port will be opened that the adversary can use for command and control. Usually this series of packets consists of attempted connections to a predefined sequence of closed ports (i.e. [[kb/mitre/attack/techniques/T1205.001-Port_Knocking\|Port Knocking]]), but can involve unusual flags, specific strings, or other unique characteristics. After the sequence is completed, opening a port may be accomplished by the host-based firewall, but could also be implemented by custom software.<br><br>Adversaries may also communicate with an already open port, but the service listening on that port will only respond to commands or trigger other malicious functionality if passed the appropriate magic value(s).<br><br>The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r [^6] , is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.<br><br>On network devices, adversaries may use crafted packets to enable [[kb/mitre/attack/techniques/T1556.004-Network_Device_Authentication\|Network Device Authentication]] for standard services offered by the device such as telnet.  Such signaling may also be used to open a closed service port such as telnet, or to trigger module modification of malware implants on the device, adding, removing, or changing malicious capabilities.  Adversaries may use crafted packets to attempt to connect to one or more (open or closed) ports, but may also attempt to connect to a router interface, broadcast, and network address IP on the same port in order to achieve their goals and objectives.[^5] [^4] [^2]   To enable this traffic signaling on embedded devices, adversaries must first achieve and leverage [[kb/mitre/attack/techniques/T1601.001-Patch_System_Image\|Patch System Image]] due to the monolithic nature of the architecture.<br><br>Adversaries may also use the Wake-on-LAN feature to turn on powered off systems. Wake-on-LAN is a hardware feature that allows a powered down system to be powered on, or woken up, by sending a magic packet to it. Once the system is powered on, it may become a target for lateral movement.[^3] [^1] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1037-Filter_Network_Traffic\|M1037]] | Filter Network Traffic | Mitigation of some variants of this technique could be achieved through the use of stateful firewalls, depending upon how it is implemented. |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Disable Wake-on-LAN if it is not needed within an environment. |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1205.001-Port_Knocking\|T1205.001]] | Port Knocking |
| [[kb/mitre/attack/techniques/T1205.002-Socket_Filters\|T1205.002]] | Socket Filters |




> [!info]- References
> [^1]: [AMD Magic Packet](https://www.amd.com/system/files/TechDocs/20213.pdf)

> [^2]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)

> [^3]: [Bleeping Computer - Ryuk WoL](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)

> [^4]: [Mandiant - Synful Knock](https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/)

> [^5]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)

> [^6]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)


