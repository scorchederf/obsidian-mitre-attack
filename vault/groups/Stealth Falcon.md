---
aliases: 
    - Stealth Falcon
mitre-attack: https://attack.mitre.org/groups/G0038
---

## G0038

[Stealth Falcon](https://attack.mitre.org/groups/G0038) is a threat group that has conducted targeted spyware attacks against Emirati journalists, activists, and dissidents since at least 2012. Circumstantial evidence suggests there could be a link between this group and the United Arab Emirates (UAE) government, but that has not been confirmed. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers passwords from the Windows Credential Vault.[^2]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware uses WMI to script data collection and command execution on the victim.[^2]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers passwords from multiple sources, including Internet Explorer, Firefox, and Chrome.[^2]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers passwords from multiple sources, including Windows Credential Vault and Outlook.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers a list of running processes.[^2]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers the Address Resolution Protocol (ARP) table from the victim.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware encrypts C2 traffic using RC4 with a hard-coded key.[^2]  |
| [[Query Registry\|T1012]] | Query Registry | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware attempts to determine the installed version of .NET by querying the Registry.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware communicates with its C2 server via HTTPS.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers the registered user and primary owner name via WMI.[^2]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers system information via Windows Management Instrumentation (WMI).[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers data from the local victim system.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | After data is collected by [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware, it is exfiltrated over the existing C2 channel.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware uses PowerShell commands to perform various functions, including gathering system information via WMI and executing commands from its C2 server.[^2]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware creates a scheduled task entitled “IE Web Cache” to execute a malicious file hourly.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Stealth Falcon](https://attack.mitre.org/groups/G0038) malware gathers system information via WMI, including the system directory, build number, serial number, version, manufacturer, model, and total physical memory.[^2]  |




## References

[^1]: Stealth Falcon


[^2]: [Citizen Lab Stealth Falcon May 2016](https://citizenlab.org/2016/05/stealth-falcon/)


