---
aliases: 
    - S1222
    
mitre-attack: https://attack.mitre.org/software/S1222
---

## S1222

[RIFLESPINE](https://attack.mitre.org/software/S1222) is a cross-platform backdoor that leverages Google Drive for file transfer and command execution.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [RIFLESPINE](https://attack.mitre.org/software/S1222) can retrieve C2 commands from an encrypted file on Google Drive then upload the results of command execution back to Google Drive.[^1]  |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage |  [RIFLESPINE](https://attack.mitre.org/software/S1222) can upload results from executed C2 commands to cloud storage.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RIFLESPINE](https://attack.mitre.org/software/S1222) can use the AES algorithm to encrypt C2 data.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RIFLESPINE](https://attack.mitre.org/software/S1222) can download and execute files.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [RIFLESPINE](https://attack.mitre.org/software/S1222) can create a systemd service file for execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RIFLESPINE](https://attack.mitre.org/software/S1222) can deobfuscate encrypted files prior to execution on targeted hosts.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RIFLESPINE](https://attack.mitre.org/software/S1222) can collect system information after installation on infected systems.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RIFLESPINE](https://attack.mitre.org/software/S1222) can use HTTP `GET` and `PUT` to upload and download files.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [RIFLESPINE](https://attack.mitre.org/software/S1222) can execute commands with `/bin/sh`.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [RIFLESPINE](https://attack.mitre.org/software/S1222) can stage the output from executed C2 commands to a temporary file.[^1] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[UNC3886\|G1048]] | UNC3886 |



## References

[^1]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)


