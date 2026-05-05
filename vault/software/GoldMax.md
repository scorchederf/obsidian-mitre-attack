---
aliases: 
    - S0588
    
mitre-attack: https://attack.mitre.org/software/S0588
---

## S0588

[GoldMax](https://attack.mitre.org/software/S0588) is a second-stage C2 backdoor written in Go with Windows and Linux variants that are nearly identical in functionality. [GoldMax](https://attack.mitre.org/software/S0588) was discovered in early 2021 during the investigation into the [SolarWinds Compromise](https://attack.mitre.org/campaigns/C0024), and has likely been used by [APT29](https://attack.mitre.org/groups/G0016) since at least mid-2019. [GoldMax](https://attack.mitre.org/software/S0588) uses multiple defense evasion techniques, including avoiding virtualization execution and masking malicious traffic.[^5] [^9] [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [GoldMax](https://attack.mitre.org/software/S0588) has used scheduled tasks to maintain persistence.[^5]  |
| [[Software Packing\|T1027.002]] | Software Packing | [GoldMax](https://attack.mitre.org/software/S0588) has been packed for obfuscation.[^9]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | The [GoldMax](https://attack.mitre.org/software/S0588) Linux variant has been executed with the `nohup` command to ignore hangup signals and continue to run if the terminal session was terminated.[^8]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [GoldMax](https://attack.mitre.org/software/S0588) can check the current date-time value of the compromised system, comparing it to the hardcoded execution trigger and can send the current timestamp to the C2 server.[^5] [^9]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [GoldMax](https://attack.mitre.org/software/S0588) retrieved a list of the system's network interface after execution.[^5]  |
| [[Cron\|T1053.003]] | Cron | The [GoldMax](https://attack.mitre.org/software/S0588) Linux variant has used a crontab entry with a `@reboot` line to gain persistence.[^8]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [GoldMax](https://attack.mitre.org/software/S0588) has RSA-encrypted its communication with the C2 server.[^5]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [GoldMax](https://attack.mitre.org/software/S0588) can spawn a command shell, and execute native commands.[^5] [^9]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [GoldMax](https://attack.mitre.org/software/S0588) has decoded and decrypted the configuration file when executed.[^5] [^9]  |
| [[Junk Data\|T1001.001]] | Junk Data | [GoldMax](https://attack.mitre.org/software/S0588) has used decoy traffic to surround its malicious network traffic to avoid detection.[^5]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [GoldMax](https://attack.mitre.org/software/S0588) has written AES-encrypted and Base64-encoded configuration files to disk.[^5] [^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [GoldMax](https://attack.mitre.org/software/S0588) has used HTTPS and HTTP GET requests with custom HTTP cookies for C2.[^5] [^9]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [GoldMax](https://attack.mitre.org/software/S0588) can download and execute additional files.[^5] [^9]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [GoldMax](https://attack.mitre.org/software/S0588) has used filenames that matched the system name, and appeared as a scheduled task impersonating systems management software within the corresponding ProgramData subfolder.[^5] [^8]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [GoldMax](https://attack.mitre.org/software/S0588) has set an execution trigger date and time, stored as an ASCII Unix/Epoch time value.[^5]  |
| [[System Checks\|T1497.001]] | System Checks | [GoldMax](https://attack.mitre.org/software/S0588) will check if it is being run in a virtualized environment by comparing the collected MAC address to `c8:27:cc:c2:37:5a`.[^5] [^9]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [GoldMax](https://attack.mitre.org/software/S0588) can exfiltrate files over the existing C2 channel.[^5] [^9]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [GoldMax](https://attack.mitre.org/software/S0588) has impersonated systems management software to avoid detection.[^5]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)


[^2]: SUNSHUTTLE


[^3]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)


[^4]: [Secureworks IRON RITUAL Profile](https://www.sophos.com/en-us/threat-profiles/iron-ritual)


[^5]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^6]: GoldMax


[^7]: [MSTIC NOBELIUM May 2021](https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/)


[^8]: [CrowdStrike StellarParticle January 2022](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)


[^9]: [FireEye SUNSHUTTLE Mar 2021](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)


