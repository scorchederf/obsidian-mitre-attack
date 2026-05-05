---
aliases: 
    - S0247
    
mitre-attack: https://attack.mitre.org/software/S0247
---

## S0247

[NavRAT](https://attack.mitre.org/software/S0247) is a remote access tool designed to upload, download, and execute files. It has been observed in attacks targeting South Korea. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [NavRAT](https://attack.mitre.org/software/S0247) writes multiple outputs to a TMP file using the >> method.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [NavRAT](https://attack.mitre.org/software/S0247) can download files remotely.[^2]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [NavRAT](https://attack.mitre.org/software/S0247) uses the email platform, Naver, for C2 communications, leveraging SMTP.[^2]  |
| [[Process Injection\|T1055]] | Process Injection | [NavRAT](https://attack.mitre.org/software/S0247) copies itself into a running Internet Explorer process to evade detection.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NavRAT](https://attack.mitre.org/software/S0247) uses `systeminfo` on a victim’s machine.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [NavRAT](https://attack.mitre.org/software/S0247) logs the keystrokes on the targeted system.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [NavRAT](https://attack.mitre.org/software/S0247) leverages cmd.exe to perform discovery techniques.[^2]  [NavRAT](https://attack.mitre.org/software/S0247) loads malicious shellcode and executes it in memory.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [NavRAT](https://attack.mitre.org/software/S0247) creates a Registry key to ensure a file gets executed upon reboot in order to establish persistence.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [NavRAT](https://attack.mitre.org/software/S0247) uses `tasklist /v` to check running processes.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: NavRAT


[^2]: [Talos NavRAT May 2018](https://blog.talosintelligence.com/2018/05/navrat.html)


