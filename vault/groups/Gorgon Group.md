---
aliases: 
    - Gorgon Group
mitre-attack: https://attack.mitre.org/groups/G0078
---

## G0078

[Gorgon Group](https://attack.mitre.org/groups/G0078) is a threat group consisting of members who are suspected to be Pakistan-based or have other connections to Pakistan. The group has performed a mix of criminal and targeted attacks, including campaigns against government organizations in the United Kingdom, Spain, Russia, and the United States. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can use process hollowing to inject one of its trojans into another process.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can attempt to disable security features in Microsoft Office and Windows Defender using the `taskkill` command.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can decode contents from a payload that was Base64 encoded and write the contents to a file.[^2]  |
| [[Native API\|T1106]] | Native API | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can leverage the Windows API call, CreateProcessA(), for execution.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can create a .lnk file and add a Registry Run key to establish persistence.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can use PowerShell commands to download and execute a payload and open a decoy document on the victim’s machine.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can use cmd.exe to download and execute payloads and to execute commands on the system.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can download additional files from C2 servers.[^2]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Gorgon Group](https://attack.mitre.org/groups/G0078) sent emails to victims with malicious Microsoft Office documents attached.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [Gorgon Group](https://attack.mitre.org/groups/G0078) has used `-W Hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows by setting the WindowStyle parameter to hidden. [^2]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can download a remote access tool, [ShiftyBug](https://attack.mitre.org/software/S0294), and inject into another process.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can deactivate security mechanisms in Microsoft Office by editing several keys and values under `HKCU\Software\Microsoft\Office\`.[^2]  |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | [Gorgon Group](https://attack.mitre.org/groups/G0078) malware can create a .lnk file and add a Registry Run key to establish persistence.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Gorgon Group](https://attack.mitre.org/groups/G0078) attempted to get users to launch malicious Microsoft Office attachments delivered via spearphishing emails.[^2]  |
| [[Tool\|T1588.002]] | Tool | [Gorgon Group](https://attack.mitre.org/groups/G0078) has obtained and used tools such as [QuasarRAT](https://attack.mitre.org/software/S0262) and [Remcos](https://attack.mitre.org/software/S0332).[^2]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Gorgon Group](https://attack.mitre.org/groups/G0078) has used macros in [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001)s as well as executed VBScripts on victim machines.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Remcos\|S0332]] | Remcos | [Gorgon Group](https://attack.mitre.org/groups/G0078) has used [Remcos](https://attack.mitre.org/software/S0332) as the final payload during operations.[^2]  |
| [[QuasarRAT\|S0262]] | QuasarRAT | [^2]  |
| [[NanoCore\|S0336]] | NanoCore | [^2]  |
| [[njRAT\|S0385]] | njRAT | [^2]  |



## References

[^1]: Gorgon Group


[^2]: [Unit 42 Gorgon Group Aug 2018](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)


