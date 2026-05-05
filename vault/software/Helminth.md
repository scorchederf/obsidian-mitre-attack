---
aliases: 
    - S0170
    
mitre-attack: https://attack.mitre.org/software/S0170
---

## S0170

[Helminth](https://attack.mitre.org/software/S0170) is a backdoor that has at least two variants - one written in VBScript and PowerShell that is delivered via a macros in Excel spreadsheets, and one that is a standalone Windows executable. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [Helminth](https://attack.mitre.org/software/S0170) has used a scheduled task for persistence.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Helminth](https://attack.mitre.org/software/S0170) samples have been signed with legitimate, compromised code signing certificates owned by software company AI Squared.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [Helminth](https://attack.mitre.org/software/S0170) config file is encrypted with RC4.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Helminth](https://attack.mitre.org/software/S0170) establishes persistence by creating a shortcut in the Start Menu folder.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Helminth](https://attack.mitre.org/software/S0170) encrypts data sent to its C2 server over HTTP with RC4.[^1]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Helminth](https://attack.mitre.org/software/S0170) establishes persistence by creating a shortcut.[^1]  |
| [[DNS\|T1071.004]] | DNS | [Helminth](https://attack.mitre.org/software/S0170) can use DNS for C2.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Helminth](https://attack.mitre.org/software/S0170) can use HTTP for C2.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | One version of [Helminth](https://attack.mitre.org/software/S0170) uses a PowerShell script.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Helminth](https://attack.mitre.org/software/S0170) has used [Tasklist](https://attack.mitre.org/software/S0057) to get information on processes.[^3]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | One version of [Helminth](https://attack.mitre.org/software/S0170) consists of VBScript scripts.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | The executable version of [Helminth](https://attack.mitre.org/software/S0170) has a module to log keystrokes.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Helminth](https://attack.mitre.org/software/S0170) can download additional files.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [Helminth](https://attack.mitre.org/software/S0170) creates folders to store output from batch scripts prior to sending the information to its C2 server.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | The executable version of [Helminth](https://attack.mitre.org/software/S0170) has a module to log clipboard contents.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Helminth](https://attack.mitre.org/software/S0170) can provide a remote shell. One version of [Helminth](https://attack.mitre.org/software/S0170) uses batch scripting.[^1]  |
| [[Local Groups\|T1069.001]] | Local Groups | [Helminth](https://attack.mitre.org/software/S0170) has checked the local administrators group.[^3]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [Helminth](https://attack.mitre.org/software/S0170) has checked for the domain admin group and Exchange Trusted Subsystem groups using the commands `net group Exchange Trusted Subsystem /domain` and `net group domain admins /domain`.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | A [Helminth](https://attack.mitre.org/software/S0170) VBScript receives a batch script to execute a set of commands in a command prompt.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | For C2 over HTTP, [Helminth](https://attack.mitre.org/software/S0170) encodes data with base64 and sends it via the "Cookie" field of HTTP requests. For C2 over DNS, [Helminth](https://attack.mitre.org/software/S0170) converts ASCII characters into their hexadecimal values and sends the data in cleartext.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Helminth](https://attack.mitre.org/software/S0170) splits data into chunks up to 23 bytes and sends the data in DNS queries to its C2 server.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)


[^2]: [ClearSky OilRig Jan 2017](http://www.clearskysec.com/oilrig/)


[^3]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)


[^4]: Helminth


[^5]: [FireEye APT34 Webinar Dec 2017](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)


[^6]: [Crowdstrike Helix Kitten Nov 2018](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/)


