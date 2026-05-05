---
aliases: 
    - Evilnum
mitre-attack: https://attack.mitre.org/groups/G0120
---

## G0120

[Evilnum](https://attack.mitre.org/groups/G0120) is a financially motivated threat group that has been active since at least 2018.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Checks\|T1497.001]] | System Checks | [Evilnum](https://attack.mitre.org/groups/G0120) has used a component called TerraLoader to check certain hardware and file information to detect sandboxed environments. [^2]  |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | [EVILNUM](https://attack.mitre.org/software/S0568) has used the malware variant, TerraTV, to run a legitimate TeamViewer application to connect to compromised machines.[^2]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [Evilnum](https://attack.mitre.org/groups/G0120) can steal cookies and session information from browsers.[^2]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Evilnum](https://attack.mitre.org/groups/G0120) has sent spearphishing emails containing a link to a zip file hosted on Google Drive.[^2]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Evilnum](https://attack.mitre.org/groups/G0120) has used PowerShell to bypass UAC.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Evilnum](https://attack.mitre.org/groups/G0120) has deleted files used during infection.[^2]  |
| [[DLL\|T1574.001]] | DLL | [Evilnum](https://attack.mitre.org/groups/G0120) has used the malware variant, TerraTV, to load a malicious DLL placed in the TeamViewer directory, instead of the original Windows DLL located in a system folder.[^2]   |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Evilnum](https://attack.mitre.org/groups/G0120) has sent spearphishing emails designed to trick the recipient into opening malicious shortcut links which downloads a .LNK file.[^2]  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | [Evilnum](https://attack.mitre.org/groups/G0120) can collect email credentials from victims.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Evilnum](https://attack.mitre.org/groups/G0120) can deploy additional components or tools as needed.[^2]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Evilnum](https://attack.mitre.org/groups/G0120) has used malicious JavaScript files on the victim's machine.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[LaZagne\|S0349]] | LaZagne | [^2]  |
| [[EVILNUM\|S0568]] | EVILNUM | [^3]  |
| [[More_eggs\|S0284]] | More_eggs | [^2]  |



## References

[^1]: Evilnum


[^2]: [ESET EvilNum July 2020](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)


[^3]: [Prevailion EvilNum May 2020](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)


