---
aliases: 
    - S0196
    
mitre-attack: https://attack.mitre.org/software/S0196
---

## S0196

[PUNCHBUGGY](https://attack.mitre.org/software/S0196) is a backdoor malware used by [FIN8](https://attack.mitre.org/groups/G0061) that has been observed targeting POS networks in the hospitality industry. [^2] [^1]  [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Python\|T1059.006]] | Python | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has used python scripts.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can load a DLL using Rundll32.[^5]  |
| [[AppCert DLLs\|T1546.009]] | AppCert DLLs | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can establish using a AppCertDLLs Registry key.[^5]  |
| [[Shared Modules\|T1129]] | Shared Modules | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can load a DLL using the LoadLibrary API.[^5]  |
| [[Local Account\|T1087.001]] | Local Account | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can gather user names.[^2]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can gather AVs registered in the system.[^2] 	 |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has been observed using a Registry Run key.[^5] [^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) mimics filenames from %SYSTEM%\System32 to hide DLLs in %WINDIR% and/or %TEMP%.[^5] [^2]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has Gzipped information and saved it to a random temp file before exfil.[^2] 	 |
| [[PowerShell\|T1059.001]] | PowerShell | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has used [PowerShell](https://attack.mitre.org/techniques/T1059/001) scripts.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can download additional files and payloads to compromised hosts.[^5] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has saved information to a random temp file before exfil.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) enables remote interaction and can obtain additional code over HTTPS GET and POST requests.[^1] [^5] [^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has used [PowerShell](https://attack.mitre.org/techniques/T1059/001) to decode base64-encoded assembly.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can delete files written to disk.[^5] [^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) has hashed most its code's functions and encrypted payloads with base64 and XOR.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [PUNCHBUGGY](https://attack.mitre.org/software/S0196) can gather system information such as computer names.[^2] 	 |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [FireEye Fin8 May 2016](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)


[^2]: [Morphisec ShellTea June 2019](http://blog.morphisec.com/security-alert-fin8-is-back)


[^3]: PUNCHBUGGY


[^4]: ShellTea


[^5]: [FireEye Know Your Enemy FIN8 Aug 2016](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)


