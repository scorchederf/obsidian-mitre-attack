---
aliases: 
    - S0457
    
mitre-attack: https://attack.mitre.org/software/S0457
---

## S0457

[Netwalker](https://attack.mitre.org/software/S0457) is fileless ransomware written in PowerShell and executed directly in memory.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Modify Registry\|T1112]] | Modify Registry | [Netwalker](https://attack.mitre.org/software/S0457) can add the following registry entry: `HKEY_CURRENT_USER\SOFTWARE\{8 random characters}`.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Netwalker](https://attack.mitre.org/software/S0457) can detect and terminate active security software-related processes on infected systems.[^2] [^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Netwalker](https://attack.mitre.org/software/S0457) can determine the system architecture it is running on to choose which version of the DLL to use.[^2]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used psexec to copy the [Netwalker](https://attack.mitre.org/software/S0457) payload across accessible systems.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Netwalker](https://attack.mitre.org/software/S0457)'s PowerShell script can decode and decrypt multiple layers of obfuscation, leading to the [Netwalker](https://attack.mitre.org/software/S0457) DLL being loaded into memory.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used batch scripts to retrieve the [Netwalker](https://attack.mitre.org/software/S0457) payload.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [Netwalker](https://attack.mitre.org/software/S0457)'s PowerShell script has been obfuscated with multiple layers including base64 and hexadecimal encoding and XOR-encryption, as well as obfuscated PowerShell functions and variables.[^2] [^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Netwalker](https://attack.mitre.org/software/S0457) can detect and terminate active security software-related processes on infected systems.[^2] 	 |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Netwalker](https://attack.mitre.org/software/S0457)'s DLL has been embedded within the PowerShell script in hex format.[^2]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Netwalker](https://attack.mitre.org/software/S0457) can delete the infected system's Shadow Volumes to prevent recovery.[^2] [^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Netwalker](https://attack.mitre.org/software/S0457) has been written in PowerShell and executed directly in memory, avoiding detection.[^2] [^1]  |
| [[Native API\|T1106]] | Native API | [Netwalker](https://attack.mitre.org/software/S0457) can use Windows API functions to inject the ransomware DLL.[^2]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Netwalker](https://attack.mitre.org/software/S0457) can encrypt files on infected machines to extort victims.[^2] 	 |
| [[Service Execution\|T1569.002]] | Service Execution | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used psexec and certutil to retrieve the [Netwalker](https://attack.mitre.org/software/S0457) payload.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Netwalker](https://attack.mitre.org/software/S0457) can use WMI to delete Shadow Volumes.[^2] 	 |
| [[Service Stop\|T1489]] | Service Stop | [Netwalker](https://attack.mitre.org/software/S0457) can terminate system processes and services, some of which relate to backup software.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | Operators deploying [Netwalker](https://attack.mitre.org/software/S0457) have used psexec and certutil to retrieve the [Netwalker](https://attack.mitre.org/software/S0457) payload.[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | The [Netwalker](https://attack.mitre.org/software/S0457) DLL has been injected reflectively into the memory of a legitimate running process.[^2] 	 |




## References

[^1]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)


[^2]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)


