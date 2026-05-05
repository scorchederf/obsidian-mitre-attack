---
aliases: 
    - S9014
    
mitre-attack: https://attack.mitre.org/software/S9014
---

## S9014

[PHASEJAM](https://attack.mitre.org/software/S9014) is a dropper written as a bash shell script that modifies Ivanti Connect Secure appliance components. [PHASEJAM](https://attack.mitre.org/software/S9014) was first reported in January 2025. [PHASEJAM](https://attack.mitre.org/software/S9014) has previously been leveraged by People's Republic of China (PRC)- affiliated actors identified as UNC5221 and SYLVANITE.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [PHASEJAM](https://attack.mitre.org/software/S9014) has modified legitimate components to enable persistence and execution, including inserting a web shell into `getComponent.cgi` and `restAuth.cgi`, modifying `DSUpgrade.pm` to block system upgrades, and overwriting `remotedebug` to execute arbitrary commands when specific parameters are provided.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [PHASEJAM](https://attack.mitre.org/software/S9014) has disabled the `cgi-server` process on Ivanti Connect Secure appliances.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PHASEJAM](https://attack.mitre.org/software/S9014) has the ability to decode Base64 commands and data.[^1]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [PHASEJAM](https://attack.mitre.org/software/S9014) has renamed the file `/home/bin/remotedebug` to `remotedebug.bak`, allowing the threats actors to write a malicious `/home/bin/remotedebug` shell script.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [PHASEJAM](https://attack.mitre.org/software/S9014) has encoded commands with Base64.[^1]  |
| [[Delay Execution\|T1678]] | Delay Execution | [PHASEJAM](https://attack.mitre.org/software/S9014) has used the `sleep` command within its code to generate a fake HTML upgrade progress bar that mimics a running process.[^1]  |
| [[Data Manipulation\|T1565]] | Data Manipulation | [PHASEJAM](https://attack.mitre.org/software/S9014) has blocked legitimate upgrades of Ivanti Connect Secure systems and falsely indicates a successful upgrade while operating on an older version.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PHASEJAM](https://attack.mitre.org/software/S9014) has launched a webshell using the `MIME::Base64` module that encoded and decoded Base64 commands.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PHASEJAM](https://attack.mitre.org/software/S9014) has the ability to upload files onto the compromised appliance.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [PHASEJAM](https://attack.mitre.org/software/S9014) has inserted Perl-based web shells into legitimate files that provided threat actors with remote access and code execution capabilities on the compromised network appliance.[^1]  |
| [[Modify or Spoof Tool UI\|T1685.003]] | Modify or Spoof Tool UI | [PHASEJAM](https://attack.mitre.org/software/S9014) has prevented legitimate Ivanti Connect Secure system upgrades by intercepting the upgrade command and rendering fake HTML upgrade progress bar through a function called `processUpgradeDisplay()` which allowed the compromised device to remain under the control of the adversary.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [PHASEJAM](https://attack.mitre.org/software/S9014) has modified Ivanti Connect Secure appliances and blocks the system upgrades by altering the DSUpgrade.pm file.[^1]  |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | [PHASEJAM](https://attack.mitre.org/software/S9014) has used a bash script to modify components on Ivanti Connect Secure appliances and execute files via `/bin/bash`.[1] It has also used the Linux stream editor (`sed`) to execute commands.[^1]  |
| [[Network Device CLI\|T1059.008]] | Network Device CLI | [PHASEJAM](https://attack.mitre.org/software/S9014) has leveraged native commands associated with the compromised network appliance to execute code.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [PHASEJAM](https://attack.mitre.org/software/S9014) has the ability to exfiltrate data from the victim appliance.[^1]  |




## References

[^1]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^2]: [Dragos SYLVANITE MuddyWater Electrum March 2026](https://hub.dragos.com/hubfs/2026_YIR_ExecutiveBriefing%20O_G.pdf?hsLang=en)


