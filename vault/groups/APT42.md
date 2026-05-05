---
aliases: 
    - APT42
mitre-attack: https://attack.mitre.org/groups/G1044
---

## G1044

[APT42](https://attack.mitre.org/groups/G1044) is an Iranian-sponsored threat group that conducts cyber espionage and surveillance.[^1]  The group primarily focuses on targets in the Middle East region, but has targeted a variety of industries and countries since at least 2015.[^1]  [APT42](https://attack.mitre.org/groups/G1044) starts cyber operations through spearphishing emails and/or the PINEFLOWER Android malware, then monitors and collects information from the compromised systems and devices.[^1]  Finally, [APT42](https://attack.mitre.org/groups/G1044) exfiltrates data using native features and open-source tools.[^2]  <br><br>[APT42](https://attack.mitre.org/groups/G1044) activities have been linked to [Magic Hound](https://attack.mitre.org/groups/G0059) by other commercial vendors. While there are behavior and software overlaps between [Magic Hound](https://attack.mitre.org/groups/G0059) and [APT42](https://attack.mitre.org/groups/G1044), they appear to be distinct entities and are tracked as separate entities by their originating vendor. 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [APT42](https://attack.mitre.org/groups/G1044) has downloaded and executed PowerShell payloads.[^1]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used Windows Management Instrumentation (WMI) to check for anti-virus products.[^2]   |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [APT42](https://attack.mitre.org/groups/G1044) has masqueraded the VINETHORN payload as a VPN application.[^1]   |
| [[Indicator Removal\|T1070]] | Indicator Removal | [APT42](https://attack.mitre.org/groups/G1044) has cleared Chrome browser history.[^2]   |
| [[Input Capture\|T1056]] | Input Capture | [APT42](https://attack.mitre.org/groups/G1044) has used credential harvesting websites.[^2]   |
| [[Domains\|T1583.001]] | Domains | [APT42](https://attack.mitre.org/groups/G1044) has registered domains, several of which masqueraded as news outlets and login services, for use in operations.[^1] [^3]    |
| [[Standard Encoding\|T1132.001]] | Standard Encoding |  [APT42](https://attack.mitre.org/groups/G1044) has encoded C2 traffic with Base64.[^2]   |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [APT42](https://attack.mitre.org/groups/G1044) has collected data from Microsoft 365 environments.[^2] [^1]     |
| [[Visual Basic\|T1059.005]] | Visual Basic | [APT42](https://attack.mitre.org/groups/G1044) has used a VBScript to query anti-virus products.[^2]   |
| [[Screen Capture\|T1113]] | Screen Capture | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to take screenshots.[^1]   |
| [[Impersonation\|T1684.001]] | Impersonation | [APT42](https://attack.mitre.org/groups/G1044) has impersonated legitimate people in phishing emails to gain credentials.[^1] [^3]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect network information.[^1]   |
| [[Local Account\|T1087.001]] | Local Account | [APT42](https://attack.mitre.org/groups/G1044) has used the PowerShell-based POWERPOST script to collect local account names from the victim machine.[^1]   |
| [[Email Accounts\|T1585.002]] | Email Accounts | [APT42](https://attack.mitre.org/groups/G1044) has created email accounts to use in spearphishing operations.[^3]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [APT42](https://attack.mitre.org/groups/G1044) has used scheduled tasks for persistence.[^1]   |
| [[Query Public AI Services\|T1682]] | Query Public AI Services | APT42 has leveraged LLMs to search for official emails to build target lists, and conduct reconnaissance on potential business partners.[^4]  |
| [[Clear Mailbox Data\|T1070.008]] | Clear Mailbox Data | [APT42](https://attack.mitre.org/groups/G1044) has deleted login notification emails and has cleared the Sent folder to cover their tracks.[^1]   |
| [[Keylogging\|T1056.001]] | Keylogging | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to log keystrokes.[^1]   |
| [[Web Service\|T1102]] | Web Service | [APT42](https://attack.mitre.org/groups/G1044) has used various links, such as links with typo-squatted domains, links to Dropbox files and links to fake Google sites, in spearphishing operations.[^2] [^1] [^3]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [APT42](https://attack.mitre.org/groups/G1044) has used malware, such as GHAMBAR and POWERPOST, to collect system information.[^1]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [APT42](https://attack.mitre.org/groups/G1044) has used tools such as [NICECURL](https://attack.mitre.org/software/S1192) with command and control communication taking place over HTTPS.[^2]   |
| [[Virtual Private Server\|T1583.003]] | Virtual Private Server | [APT42](https://attack.mitre.org/groups/G1044) has used anonymized infrastructure and Virtual Private Servers (VPSs) to interact with the victim’s environment.[^1] [^2]   |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [APT42](https://attack.mitre.org/groups/G1044) has used tools such as [NICECURL](https://attack.mitre.org/software/S1192) with command and control communication taking place over HTTPS.[^2]   |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [APT42](https://attack.mitre.org/groups/G1044) has used Windows Management Instrumentation (WMI) to query anti-virus products.[^2]   |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to steal login and cookie data from common browsers.[^1]   |
| [[Upload Malware\|T1608.001]] | Upload Malware | [APT42](https://attack.mitre.org/groups/G1044) has used its infrastructure for C2 and for staging the VINETHORN payload, which masqueraded as a VPN application.[^1]   |
| [[Tool\|T1588.002]] | Tool | [APT42](https://attack.mitre.org/groups/G1044) has used built-in features in the Microsoft 365 environment and publicly available tools to avoid detection.[^2]   |
| [[Multi-Factor Authentication Interception\|T1111]] | Multi-Factor Authentication Interception | [APT42](https://attack.mitre.org/groups/G1044) has intercepted SMS-based one-time passwords and has set up two-factor authentication.[^1]  Additionally, [APT42](https://attack.mitre.org/groups/G1044) has used cloned or fake websites to capture MFA tokens.[^2]   |
| [[Boot or Logon Autostart Execution\|T1547]] | Boot or Logon Autostart Execution | [APT42](https://attack.mitre.org/groups/G1044) has modified the Registry to maintain persistence.[^1]   |
| [[Modify Registry\|T1112]] | Modify Registry | [APT42](https://attack.mitre.org/groups/G1044) has modified Registry keys to maintain persistence.[^1]   |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [APT42](https://attack.mitre.org/groups/G1044) has sent spearphishing emails containing malicious links.[^1] [^2] [^3]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [APT42](https://attack.mitre.org/groups/G1044) has used custom malware to steal credentials.[^1]   |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[NICECURL\|S1192]] | NICECURL | [^2]  |
| [[TAMECAT\|S1193]] | TAMECAT | [^2]  |



## References

[^1]: [Mandiant APT42-charms](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)


[^2]: [Mandiant APT42-untangling](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)


[^3]: [TAG APT42](https://blog.google/threat-analysis-group/iranian-backed-group-steps-up-phishing-campaigns-against-israel-us/)


[^4]: [GTIG AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)


