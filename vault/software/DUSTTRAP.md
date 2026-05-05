---
aliases: 
    - S1159
    
mitre-attack: https://attack.mitre.org/software/S1159
---

## S1159

[DUSTTRAP](https://attack.mitre.org/software/S1159) is a multi-stage plugin framework associated with [APT41](https://attack.mitre.org/groups/G0096) operations with multiple components.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Domain Account\|T1087.002]] | Domain Account | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate domain accounts.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate Registry items.[^1]  |
| [[Group Policy Discovery\|T1615]] | Group Policy Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can identify victim environment Group Policy information.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [DUSTTRAP](https://attack.mitre.org/software/S1159) compromises the `.text` section of a legitimate system DLL in `%windir%` to hold the contents of retrieved plug-ins.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DUSTTRAP](https://attack.mitre.org/software/S1159) can perform keylogging operations.[^1]  |
| [[Indicator Removal\|T1070]] | Indicator Removal | [DUSTTRAP](https://attack.mitre.org/software/S1159) restores the `.text` section of compromised DLLs after malicious code is loaded into memory and before the file is closed.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DUSTTRAP](https://attack.mitre.org/software/S1159) begins with an initial launcher that decrypts an AES-128-CFB encrypted file on disk and executes it in memory.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate running processes.[^1]  |
| [[Local Account\|T1087.001]] | Local Account | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate local user accounts.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [DUSTTRAP](https://attack.mitre.org/software/S1159) can capture screenshots.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can identify security software.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DUSTTRAP](https://attack.mitre.org/software/S1159) deobfuscates embedded payloads.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DUSTTRAP](https://attack.mitre.org/software/S1159) can retrieve and load additional payloads.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate files and directories.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [DUSTTRAP](https://attack.mitre.org/software/S1159) can gather data from infected systems.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate infected system network information.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [DUSTTRAP](https://attack.mitre.org/software/S1159) can execute commands via `cmd.exe`.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can enumerate running application windows.[^1]  |
| [[Network Share Connection Removal\|T1070.005]] | Network Share Connection Removal | [DUSTTRAP](https://attack.mitre.org/software/S1159) can remove network shares from infected systems.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [DUSTTRAP](https://attack.mitre.org/software/S1159) can exfiltrate collected data over C2 channels.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) reads the infected system's current time and writes it to a log file during execution.[^1]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can identify Active Directory information and related items.[^1]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [DUSTTRAP](https://attack.mitre.org/software/S1159) can delete infected system log information.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) reads the value of the infected system's `HKLM\SYSTEM\Microsoft\Cryptography\MachineGUID` value.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [DUSTTRAP](https://attack.mitre.org/software/S1159) contains additional embedded DLLs and configuration files that are loaded into memory during execution.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can use `ping` to identify remote hosts within the victim network.[^1]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [DUSTTRAP](https://attack.mitre.org/software/S1159) can identify infected system log information.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [DUSTTRAP](https://attack.mitre.org/software/S1159) decryption relies on the infected machine's `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGUID` value.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [DUSTTRAP](https://attack.mitre.org/software/S1159) can identify and enumerate victim system network shares.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT41\|G0096]] | APT41 |



## References

[^1]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)


