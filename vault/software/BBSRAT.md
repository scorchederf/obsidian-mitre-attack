---
aliases: 
    - S0127
    
mitre-attack: https://attack.mitre.org/software/S0127
---

## S0127

[BBSRAT](https://attack.mitre.org/software/S0127) is malware with remote access tool functionality that has been used in targeted compromises. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BBSRAT](https://attack.mitre.org/software/S0127) uses [Expand](https://attack.mitre.org/software/S0361) to decompress a CAB file into executable content.[^1]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [BBSRAT](https://attack.mitre.org/software/S0127) can compress data with ZLIB prior to sending it back to the C2 server.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [BBSRAT](https://attack.mitre.org/software/S0127) has been loaded through DLL side-loading of a legitimate Citrix executable that is set to persist through the Registry Run key location `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ssonsvr.exe`. |
| [[System Service Discovery\|T1007]] | System Service Discovery | [BBSRAT](https://attack.mitre.org/software/S0127) can query service configuration information.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [BBSRAT](https://attack.mitre.org/software/S0127) can start, stop, or delete services.[^1]  |
| [[DLL\|T1574.001]] | DLL | DLL side-loading has been used to execute [BBSRAT](https://attack.mitre.org/software/S0127) through a legitimate Citrix executable, ssonsvr.exe. The Citrix executable was dropped along with [BBSRAT](https://attack.mitre.org/software/S0127) by the dropper.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [BBSRAT](https://attack.mitre.org/software/S0127) uses GET and POST requests over HTTP or HTTPS for command and control to obtain commands and send ZLIB compressed data back to the C2 server.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BBSRAT](https://attack.mitre.org/software/S0127) uses a custom encryption algorithm on data sent back to the C2 server over HTTP.[^1]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [BBSRAT](https://attack.mitre.org/software/S0127) has been seen persisting via COM hijacking through replacement of the COM object for MruPidlList `{42aedc87-2188-41fd-b9a3-0c966feabec1}` or Microsoft WBEM New Event Subsystem `{F3130CDB-AA52-4C3A-AB32-85FFC23AF9C1}` depending on the system's CPU architecture.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [BBSRAT](https://attack.mitre.org/software/S0127) can list file and directory information.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [BBSRAT](https://attack.mitre.org/software/S0127) can delete files and directories.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [BBSRAT](https://attack.mitre.org/software/S0127) can modify service configurations.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [BBSRAT](https://attack.mitre.org/software/S0127) can list running processes.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [BBSRAT](https://attack.mitre.org/software/S0127) has been seen loaded into msiexec.exe through process hollowing to hide its execution.[^1]  |




## References

[^1]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)


