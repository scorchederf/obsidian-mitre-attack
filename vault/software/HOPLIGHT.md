---
aliases: 
    - S0376
    
mitre-attack: https://attack.mitre.org/software/S0376
---

## S0376

[HOPLIGHT](https://attack.mitre.org/software/S0376) is a backdoor Trojan that has reportedly been used by the North Korean government.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Device Driver Discovery\|T1652]] | Device Driver Discovery | [HOPLIGHT](https://attack.mitre.org/software/S0376) can enumerate device drivers located in the registry at `HKLM\Software\WBEM\WDM`.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [HOPLIGHT](https://attack.mitre.org/software/S0376) has modified Managed Object Format (MOF) files within the Registry to run specific commands and create persistence on the system.[^1] 	 |
| [[Fallback Channels\|T1008]] | Fallback Channels | [HOPLIGHT](https://attack.mitre.org/software/S0376) has multiple C2 channels in place in case one fails.[^1] 	 |
| [[Query Registry\|T1012]] | Query Registry | A variant of [HOPLIGHT](https://attack.mitre.org/software/S0376) hooks lsass.exe, and lsass.exe then checks the Registry for the data value 'rdpproto' under the key `SYSTEM\CurrentControlSet\Control\Lsa Name`.[^1]  |
| [[Proxy\|T1090]] | Proxy | [HOPLIGHT](https://attack.mitre.org/software/S0376) has multiple proxy options that mask traffic between the malware and the remote operators.[^1] 	<br> |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [HOPLIGHT](https://attack.mitre.org/software/S0376) has connected outbound over TCP port 443 with a FakeTLS method.[^1]  |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed loading several APIs associated with Pass the Hash.[^1] 	 |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [HOPLIGHT](https://attack.mitre.org/software/S0376) has modified the firewall using [netsh](https://attack.mitre.org/software/S0108).[^1] 	 |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed enumerating system drives and partitions.[^1] 	 |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [HOPLIGHT](https://attack.mitre.org/software/S0376) has the capability to harvest credentials and passwords from the SAM database.[^1] 	 |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HOPLIGHT](https://attack.mitre.org/software/S0376) can launch cmd.exe to execute commands on the system.[^1] 	 |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [HOPLIGHT](https://attack.mitre.org/software/S0376) has used its C2 channel to exfiltrate data.[^1] 	 |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [HOPLIGHT](https://attack.mitre.org/software/S0376) has utilized Zlib compression to obfuscate the communications payload. [^1] 	<br> |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed collecting victim machine information like OS version.[^1]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [HOPLIGHT](https://attack.mitre.org/software/S0376) can use WMI event subscriptions to create persistence.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [HOPLIGHT](https://attack.mitre.org/software/S0376) has used svchost.exe to execute a malicious DLL .[^1]  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed collecting victim machine volume information.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HOPLIGHT](https://attack.mitre.org/software/S0376) has the ability to connect to a remote host in order to upload and download files.[^1] 	 |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [HOPLIGHT](https://attack.mitre.org/software/S0376) has used WMI to recompile the Managed Object Format (MOF) files in the WMI repository.[^1] 	 |
| [[System Time Discovery\|T1124]] | System Time Discovery | [HOPLIGHT](https://attack.mitre.org/software/S0376) has been observed collecting system time from victim machines.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [HOPLIGHT](https://attack.mitre.org/software/S0376) has injected into running processes.[^1] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Lazarus Group\|G0032]] | Lazarus Group |
| [[APT38\|G0082]] | APT38 |



## References

[^1]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)


[^2]: [CISA AA20-239A BeagleBoyz August 2020](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)


[^3]: HOPLIGHT


