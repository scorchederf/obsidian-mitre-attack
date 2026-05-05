---
aliases: 
    - S0629
    
mitre-attack: https://attack.mitre.org/software/S0629
---

## S0629

[RainyDay](https://attack.mitre.org/software/S0629) is a backdoor tool that has been used by [Naikon](https://attack.mitre.org/groups/G0019) since at least 2020.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [RainyDay](https://attack.mitre.org/software/S0629) has used names to mimic legitimate software including "vmtoolsd.exe" to spoof Vmtools.[^1]  |
| [[Native API\|T1106]] | Native API | The file collection tool used by [RainyDay](https://attack.mitre.org/software/S0629) can utilize native API including `ReadDirectoryChangeW` for folder monitoring.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [RainyDay](https://attack.mitre.org/software/S0629) has the ability to uninstall itself by deleting its service and files.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to upload specific files to Dropbox.[^1] 	 <br> |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RainyDay](https://attack.mitre.org/software/S0629) can download files to a compromised host.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RainyDay](https://attack.mitre.org/software/S0629) can decrypt its payload via a XOR key.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RainyDay](https://attack.mitre.org/software/S0629) can use HTTP in C2 communications.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [RainyDay](https://attack.mitre.org/software/S0629) has named services and scheduled tasks to appear benign including "ChromeCheck" and "googleupdate."[^1]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [RainyDay](https://attack.mitre.org/software/S0629) can create and register a service for execution.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RainyDay](https://attack.mitre.org/software/S0629) can enumerate processes on a target system.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to copy files to `C:\ProgramData\Adobe\temp` prior to exfiltration.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [RainyDay](https://attack.mitre.org/software/S0629) can use tools to collect credentials from web browsers.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [RainyDay](https://attack.mitre.org/software/S0629) has downloaded as a XOR-encrypted payload.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [RainyDay](https://attack.mitre.org/software/S0629) has the ability to switch between TCP and HTTP for C2 if one method is not working.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [RainyDay](https://attack.mitre.org/software/S0629) can use services to establish persistence.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RainyDay](https://attack.mitre.org/software/S0629) can use the Windows Command Shell for execution.[^1]  |
| [[Proxy\|T1090]] | Proxy | [RainyDay](https://attack.mitre.org/software/S0629) can use proxy tools including boost_proxy_client for reverse proxy functionality.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [RainyDay](https://attack.mitre.org/software/S0629) has the ability to capture screenshots.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to collect recently changed files with specific extensions.[^1]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [RainyDay](https://attack.mitre.org/software/S0629) can use the QuarksPwDump tool to obtain local passwords and domain cached credentials.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [RainyDay](https://attack.mitre.org/software/S0629) can use scheduled tasks to achieve persistence.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [RainyDay](https://attack.mitre.org/software/S0629) can use TCP in C2 communications.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RainyDay](https://attack.mitre.org/software/S0629) can use RC4 to encrypt C2 communications.[^1]  |
| [[DLL\|T1574.001]] | DLL | [RainyDay](https://attack.mitre.org/software/S0629) can use side-loading to run malicious executables.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [RainyDay](https://attack.mitre.org/software/S0629) can use a file exfiltration tool to collect recently changed files on a compromised host.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |



## References

[^1]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)


