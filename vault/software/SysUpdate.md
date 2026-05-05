---
aliases: 
    - S0663
    
mitre-attack: https://attack.mitre.org/software/S0663
---

## S0663

[SysUpdate](https://attack.mitre.org/software/S0663) is a backdoor written in C++ that has been used by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2020.[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[DNS\|T1071.004]] | DNS | [SysUpdate](https://attack.mitre.org/software/S0663) has used DNS TXT requests as for its C2 communication.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [SysUpdate](https://attack.mitre.org/software/S0663) has used DES to encrypt all C2 communications.[^2]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collect a list of services on a victim machine.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [SysUpdate](https://attack.mitre.org/software/S0663) can deobfuscate packed binaries in memory.[^4]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collect a system's drive information.[^4] [^2]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [SysUpdate](https://attack.mitre.org/software/S0663) has used Base64 to encode its C2 traffic.[^2]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collect the username from a compromised host.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collect information about running processes.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [SysUpdate](https://attack.mitre.org/software/S0663) has been signed with stolen digital certificates.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [SysUpdate](https://attack.mitre.org/software/S0663) can collect information and files from a compromised host.[^2]  |
| [[Fileless Storage\|T1027.011]] | Fileless Storage | [SysUpdate](https://attack.mitre.org/software/S0663) can store its encoded configuration file within `Software\Classes\scConfig` in either `HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_USER`.[^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can search files on a compromised host.[^4] [^2]  |
| [[Internet Connection Discovery\|T1016.001]] | Internet Connection Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can contact the DNS server operated by Google as part of its C2 establishment process.[^2]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SysUpdate](https://attack.mitre.org/software/S0663) has the ability to download files to a compromised host.[^4] [^2]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [SysUpdate](https://attack.mitre.org/software/S0663) has named their unit configuration file similarly to other unit files residing in the same directory, `/usr/lib/systemd/system/`, to appear benign.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SysUpdate](https://attack.mitre.org/software/S0663) has exfiltrated data over its C2 channel.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [SysUpdate](https://attack.mitre.org/software/S0663) can encrypt and encode its configuration file.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collect a system's architecture, operating system version, and hostname.[^4] [^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [SysUpdate](https://attack.mitre.org/software/S0663) has the ability to capture screenshots.[^4]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [SysUpdate](https://attack.mitre.org/software/S0663) can copy a script to the user owned `/usr/lib/systemd/system/` directory with a symlink mapped to a `root` owned directory, `/etc/ystem/system`, in the unit configuration file's `ExecStart` directive to establish persistence and elevate privileges.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SysUpdate](https://attack.mitre.org/software/S0663) can delete its configuration file from the targeted system.[^4]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SysUpdate](https://attack.mitre.org/software/S0663) can write its configuration file to `Software\Classes\scConfig` in either `HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_USER`.[^4]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [SysUpdate](https://attack.mitre.org/software/S0663) has the ability to set file attributes to hidden.[^4]  |
| [[DLL\|T1574.001]] | DLL | [SysUpdate](https://attack.mitre.org/software/S0663) can load DLLs through vulnerable legitimate executables.[^4] <br> |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SysUpdate](https://attack.mitre.org/software/S0663) can use a Registry Run key to establish persistence.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SysUpdate](https://attack.mitre.org/software/S0663) can collected the IP address and domain name of a compromised host.[^2]   |
| [[Software Packing\|T1027.002]] | Software Packing | [SysUpdate](https://attack.mitre.org/software/S0663) has been packed with VMProtect.[^4] [^2]  |
| [[Native API\|T1106]] | Native API | [SysUpdate](https://attack.mitre.org/software/S0663) can call the `GetNetworkParams` API as part of its C2 establishment process.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [SysUpdate](https://attack.mitre.org/software/S0663) can manage services and processes.[^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SysUpdate](https://attack.mitre.org/software/S0663) can use WMI for execution on a compromised host.[^4]  |
| [[Windows Service\|T1543.003]] | Windows Service | [SysUpdate](https://attack.mitre.org/software/S0663) can create a service to establish persistence.[^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |



## References

[^1]: Soldier


[^2]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)


[^3]: FOCUSFJORD


[^4]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^5]: HyperSSL


