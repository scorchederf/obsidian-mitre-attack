---
aliases: 
    - S0038
    
mitre-attack: https://attack.mitre.org/software/S0038
---

## S0038

[Duqu](https://attack.mitre.org/software/S0038) is a malware platform that uses a modular approach to extend functionality after deployment within a target network. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [Duqu](https://attack.mitre.org/software/S0038) can track key presses with a keylogger module.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | Modules can be pushed to and executed by [Duqu](https://attack.mitre.org/software/S0038) that copy data to a staging area, compress it, and XOR encrypt it.[^1]  |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Duqu](https://attack.mitre.org/software/S0038) can be configured to have commands relayed over a peer-to-peer network of infected hosts if some of the hosts do not have Internet access.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Duqu](https://attack.mitre.org/software/S0038) has used `msiexec` to execute malicious Windows Installer packages. Additionally, a PROPERTY=VALUE pair containing a 56-bit encryption key has been used to decrypt the main payload from the installer packages.[^2]  |
| [[Local Account\|T1087.001]] | Local Account | The discovery modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on accounts and permissions.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | The discovery modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on process details.[^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | Adversaries can instruct [Duqu](https://attack.mitre.org/software/S0038) to spread laterally by copying itself to shares it has enumerated and for which it has obtained legitimate credentials (via keylogging or other means). The remote host is then infected by using the compromised credentials to schedule a task on remote machines that executes the malware.[^1]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Duqu](https://attack.mitre.org/software/S0038) creates a new service that loads a malicious driver when the system starts. When Duqu is active, the operating system believes that the driver is legitimate, as it has been signed with a valid private key.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Duqu](https://attack.mitre.org/software/S0038) uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | Modules can be pushed to and executed by [Duqu](https://attack.mitre.org/software/S0038) that copy data to a staging area, compress it, and XOR encrypt it.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Duqu](https://attack.mitre.org/software/S0038) will inject itself into different processes to evade detection. The selection of the target process is influenced by the security software that is installed on the system (Duqu will inject into different processes depending on which security suite is installed on the infected host).[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | The [Duqu](https://attack.mitre.org/software/S0038) command and control protocol's data stream can be encrypted with AES-CBC.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Duqu](https://attack.mitre.org/software/S0038) uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | Adversaries can instruct [Duqu](https://attack.mitre.org/software/S0038) to spread laterally by copying itself to shares it has enumerated and for which it has obtained legitimate credentials (via keylogging or other means). The remote host is then infected by using the compromised credentials to schedule a task on remote machines that executes the malware.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | The discovery modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on network connections.[^1]  |
| [[Access Token Manipulation\|T1134]] | Access Token Manipulation | [Duqu](https://attack.mitre.org/software/S0038) examines running system processes for tokens that have specific system privileges. If it finds one, it will copy the token and store it for later use. Eventually it will start new processes with the stored token attached. It can also steal tokens to acquire administrative privileges.[^2]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | The discovery modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on open windows.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | Adversaries can instruct [Duqu](https://attack.mitre.org/software/S0038) to spread laterally by copying itself to shares it has enumerated and for which it has obtained legitimate credentials (via keylogging or other means). The remote host is then infected by using the compromised credentials to schedule a task on remote machines that executes the malware.[^1]  |
| [[Steganography\|T1001.002]] | Steganography | When the [Duqu](https://attack.mitre.org/software/S0038) command and control is operating over HTTP or HTTPS, Duqu uploads data to its controller by appending it to a blank JPG file.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | The reconnaissance modules used with [Duqu](https://attack.mitre.org/software/S0038) can collect information on network configuration.[^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Duqu](https://attack.mitre.org/software/S0038) is capable of loading executable code via process hollowing.[^1]  |




## References

[^1]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)


[^2]: [Kaspersky Duqu 2.0](https://web.archive.org/web/20150906233433/https://securelist.com/files/2015/06/The_Mystery_of_Duqu_2_0_a_sophisticated_cyberespionage_actor_returns.pdf)


