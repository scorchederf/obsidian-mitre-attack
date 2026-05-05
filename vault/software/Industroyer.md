---
aliases: 
    - S0604
    
mitre-attack: https://attack.mitre.org/software/S0604
---

## S0604

[Industroyer](https://attack.mitre.org/software/S0604) is a sophisticated malware framework designed to cause an impact to the working processes of Industrial Control Systems (ICS), specifically components used in electrical substations.[^1]  [Industroyer](https://attack.mitre.org/software/S0604) was used in the attacks on the Ukrainian power grid in December 2016.[^6]  This is the first publicly known malware specifically designed to target and impact operations in the electric grid.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [Industroyer](https://attack.mitre.org/software/S0604) can use an arbitrary system service to load at system boot for persistence and replaces the ImagePath registry value of a Windows service with a new backdoor binary.[^6]   |
| [[Data Destruction\|T1485]] | Data Destruction | [Industroyer](https://attack.mitre.org/software/S0604)’s data wiper module clears registry keys and overwrites both ICS configuration and Windows files.[^6]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Industroyer](https://attack.mitre.org/software/S0604) uses a custom port scanner to map out a network.[^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [Industroyer](https://attack.mitre.org/software/S0604) can use supplied user credentials to execute processes and stop services.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [Industroyer](https://attack.mitre.org/software/S0604) has used a Trojanized version of the Windows Notepad application for an additional backdoor persistence mechanism.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Industroyer](https://attack.mitre.org/software/S0604) downloads a shellcode payload from a remote C2 server and loads it into memory.[^1]  |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [Industroyer](https://attack.mitre.org/software/S0604) can enumerate remote computers in the compromised network.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Industroyer](https://attack.mitre.org/software/S0604)’s data wiper component enumerates specific files on all the Windows drives.[^1]  |
| [[Protocol Tunneling\|T1572]] | Protocol Tunneling | [Industroyer](https://attack.mitre.org/software/S0604) attempts to perform an HTTP CONNECT via an internal proxy to establish a tunnel.[^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Industroyer](https://attack.mitre.org/software/S0604)’s 61850 payload component enumerates connected network adapters and their corresponding IP addresses.[^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Industroyer](https://attack.mitre.org/software/S0604)’s data wiper module writes zeros into the registry keys in `SYSTEM\CurrentControlSet\Services` to render a system inoperable.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Industroyer](https://attack.mitre.org/software/S0604) sends information about hardware profiles and previously-received commands back to the C2 server in a POST-request.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Industroyer](https://attack.mitre.org/software/S0604)’s main backdoor connected to a remote C2 server using HTTPS.[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Industroyer](https://attack.mitre.org/software/S0604) used [Tor](https://attack.mitre.org/software/S0183) nodes for C2.[^6]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Industroyer](https://attack.mitre.org/software/S0604) collects the victim machine’s Windows GUID.[^6]  |
| [[Application or System Exploitation\|T1499.004]] | Application or System Exploitation | [Industroyer](https://attack.mitre.org/software/S0604) uses a custom DoS tool that leverages CVE-2015-5374 and targets hardcoded IP addresses of Siemens SIPROTEC devices.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Industroyer](https://attack.mitre.org/software/S0604) decrypts code to connect to a remote C2 server.[^1]  |
| [[Query Registry\|T1012]] | Query Registry | [Industroyer](https://attack.mitre.org/software/S0604) has a data wiper component that enumerates keys in the Registry `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Industroyer](https://attack.mitre.org/software/S0604) uses heavily obfuscated code in its Windows Notepad backdoor.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)


[^2]: [Dragos Crashoverride 2018](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)


[^3]: Win32/Industroyer


[^4]: CRASHOVERRIDE


[^5]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


[^6]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)


[^7]: [Secureworks IRON VIKING](https://www.secureworks.com/research/threat-profiles/iron-viking)


