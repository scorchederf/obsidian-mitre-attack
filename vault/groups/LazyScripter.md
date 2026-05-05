---
aliases: 
    - LazyScripter
mitre-attack: https://attack.mitre.org/groups/G0140
---

## G0140

[LazyScripter](https://attack.mitre.org/groups/G0140) is threat group that has mainly targeted the airlines industry since at least 2018, primarily using open-source toolsets.[^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Malicious Link\|T1204.001]] | Malicious Link | [LazyScripter](https://attack.mitre.org/groups/G0140) has relied upon users clicking on links to malicious files.[^2]  |
| [[Mshta\|T1218.005]] | Mshta | [LazyScripter](https://attack.mitre.org/groups/G0140) has used `mshta.exe` to execute [Koadic](https://attack.mitre.org/software/S0250) stagers.[^2]   |
| [[Upload Malware\|T1608.001]] | Upload Malware | [LazyScripter](https://attack.mitre.org/groups/G0140) has hosted open-source remote access Trojans used in its operations in GitHub.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [LazyScripter](https://attack.mitre.org/groups/G0140) has lured users to open malicious email attachments.[^2]  |
| [[Web Service\|T1102]] | Web Service | [LazyScripter](https://attack.mitre.org/groups/G0140) has used GitHub to host its payloads to operate spam campaigns.[^2]   |
| [[JavaScript\|T1059.007]] | JavaScript | [LazyScripter](https://attack.mitre.org/groups/G0140) has used JavaScript in its attacks.[^2]   |
| [[Domains\|T1583.001]] | Domains | [LazyScripter](https://attack.mitre.org/groups/G0140) has used dynamic DNS providers to create legitimate-looking subdomains for C2.[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [LazyScripter](https://attack.mitre.org/groups/G0140) has used VBScript to execute malicious code.[^2]  |
| [[DNS\|T1071.004]] | DNS | [LazyScripter](https://attack.mitre.org/groups/G0140) has leveraged dynamic DNS providers for C2 communications.[^2]   |
| [[Malware\|T1588.001]] | Malware | [LazyScripter](https://attack.mitre.org/groups/G0140) has used a variety of open-source remote access Trojans for its operations.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [LazyScripter](https://attack.mitre.org/groups/G0140) had downloaded additional tools to a compromised host.[^2]  |
| [[Masquerading\|T1036]] | Masquerading | [LazyScripter](https://attack.mitre.org/groups/G0140) has used several different security software icons to disguise executables.[^2]   |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [LazyScripter](https://attack.mitre.org/groups/G0140) has used spam emails weaponized with archive or document files as its initial infection vector.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [LazyScripter](https://attack.mitre.org/groups/G0140) has used PowerShell scripts to execute malicious code.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LazyScripter](https://attack.mitre.org/groups/G0140) has used batch files to deploy open-source and multi-stage RATs.[^2]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [LazyScripter](https://attack.mitre.org/groups/G0140) has leveraged the BatchEncryption tool to perform advanced batch script obfuscation and encoding techniques.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [LazyScripter](https://attack.mitre.org/groups/G0140) has achieved persistence via writing a PowerShell script to the autorun registry key.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [LazyScripter](https://attack.mitre.org/groups/G0140) has used `rundll32.exe` to execute [Koadic](https://attack.mitre.org/software/S0250) stagers.[^2]   |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [LazyScripter](https://attack.mitre.org/groups/G0140) has used spam emails that contain a link that redirects the victim to download a malicious document.[^2]  |
| [[Web Services\|T1583.006]] | Web Services | [LazyScripter](https://attack.mitre.org/groups/G0140) has established GitHub accounts to host its toolsets.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[ngrok\|S0508]] | ngrok | [^2]  |
| [[Empire\|S0363]] | Empire | [^2]  |
| [[Remcos\|S0332]] | Remcos | [LazyScripter](https://attack.mitre.org/groups/G0140) dropped [Remcos](https://attack.mitre.org/software/S0332) during operations.[^2]  |
| [[Koadic\|S0250]] | Koadic | [^2]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^2]  |
| [[njRAT\|S0385]] | njRAT | [^2]  |
| [[KOCTOPUS\|S0669]] | KOCTOPUS | [^2]  |



## References

[^1]: LazyScripter


[^2]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)


