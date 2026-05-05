---
aliases: 
    - S0263
    
mitre-attack: https://attack.mitre.org/software/S0263
---

## S0263

[TYPEFRAME](https://attack.mitre.org/software/S0263) is a remote access tool that has been used by [Lazarus Group](https://attack.mitre.org/groups/G0032). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [TYPEFRAME](https://attack.mitre.org/software/S0263) can install and store encrypted configuration data under the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellCompatibility\Applications\laxhost.dll` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrintConfigs`.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TYPEFRAME](https://attack.mitre.org/software/S0263) can upload and download files to the victim’s machine.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | APIs and strings in some [TYPEFRAME](https://attack.mitre.org/software/S0263) variants are RC4 encrypted. Another variant is encoded with XOR.[^1]  |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | [TYPEFRAME](https://attack.mitre.org/software/S0263) can open the Windows Firewall on the victim’s machine to allow incoming connections.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | A Word document delivering [TYPEFRAME](https://attack.mitre.org/software/S0263) prompts the user to enable macro execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | One [TYPEFRAME](https://attack.mitre.org/software/S0263) variant decrypts an archive using an RC4 key, then decompresses and installs the decrypted malicious DLL module. Another variant decodes the embedded file by XORing it with the value "0x35".[^1]  |
| [[Proxy\|T1090]] | Proxy | A [TYPEFRAME](https://attack.mitre.org/software/S0263) variant can force the compromised system to function as a proxy server.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [TYPEFRAME](https://attack.mitre.org/software/S0263) has used a malicious Word document for delivery with VBA macros for execution.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [TYPEFRAME](https://attack.mitre.org/software/S0263) variants can add malicious DLL modules as new services.[TYPEFRAME](https://attack.mitre.org/software/S0263) can also delete services from the victim’s machine.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [TYPEFRAME](https://attack.mitre.org/software/S0263) can install encrypted configuration data under the Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellCompatibility\Applications\laxhost.dll` and `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrintConfigs`.[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [TYPEFRAME](https://attack.mitre.org/software/S0263) can gather the disk volume information.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [TYPEFRAME](https://attack.mitre.org/software/S0263) has used ports 443, 8080, and 8443 with a FakeTLS method.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TYPEFRAME](https://attack.mitre.org/software/S0263) can uninstall malware components using a batch script.[^1]  [TYPEFRAME](https://attack.mitre.org/software/S0263) can execute commands using a shell.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [TYPEFRAME](https://attack.mitre.org/software/S0263) can delete files off the system.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TYPEFRAME](https://attack.mitre.org/software/S0263) can search directories for files on the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |



## References

[^1]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)


[^2]: TYPEFRAME


