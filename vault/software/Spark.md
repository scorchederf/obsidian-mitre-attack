---
aliases: 
    - S0543
    
mitre-attack: https://attack.mitre.org/software/S0543
---

## S0543

<br>[Spark](https://attack.mitre.org/software/S0543) is a Windows backdoor and has been in use since as early as 2017.[^2]  

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Software Packing\|T1027.002]] | Software Packing | [Spark](https://attack.mitre.org/software/S0543) has been packed with Enigma Protector to obfuscate its contents.[^2]   |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [Spark](https://attack.mitre.org/software/S0543) has checked the results of the `GetKeyboardLayoutList` and the language name returned by `GetLocaleInfoA` to make sure they contain the word “Arabic” before executing.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Spark](https://attack.mitre.org/software/S0543) can use cmd.exe to run commands.[^2]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Spark](https://attack.mitre.org/software/S0543) has encoded communications with the C2 server with base64.[^2]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Spark](https://attack.mitre.org/software/S0543) can collect the hostname, keyboard layout, and language from the system.[^2]   |
| [[User Activity Based Checks\|T1497.002]] | User Activity Based Checks | [Spark](https://attack.mitre.org/software/S0543) has used a splash screen to check whether an user actively clicks on the screen before running malicious code.[^2]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Spark](https://attack.mitre.org/software/S0543) has run the whoami command and has a built-in command to identify the user logged in.[^2]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Spark](https://attack.mitre.org/software/S0543) has used a custom XOR algorithm to decrypt the payload.[^2]   |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Spark](https://attack.mitre.org/software/S0543) has exfiltrated data over the C2 channel.[^2]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Spark](https://attack.mitre.org/software/S0543) has used HTTP POST requests to communicate with its C2 server to receive commands.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Molerats\|G0021]] | Molerats |



## References

[^1]: Spark


[^2]: [Unit42 Molerat Mar 2020](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)


[^3]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)


