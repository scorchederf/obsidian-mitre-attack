---
aliases: 
    - S0072
    
mitre-attack: https://attack.mitre.org/software/S0072
---

## S0072

[OwaAuth](https://attack.mitre.org/software/S0072) is a Web shell and credential stealer deployed to Microsoft Exchange servers that appears to be exclusively used by [Threat Group-3390](https://attack.mitre.org/groups/G0027). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Shell\|T1505.003]] | Web Shell | [OwaAuth](https://attack.mitre.org/software/S0072) is a Web shell that appears to be exclusively used by [Threat Group-3390](https://attack.mitre.org/groups/G0027). It is installed as an ISAPI filter on Exchange servers and shares characteristics with the [China Chopper](https://attack.mitre.org/software/S0020) Web shell.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [OwaAuth](https://attack.mitre.org/software/S0072) uses the filename owaauth.dll, which is a legitimate file that normally resides in `%ProgramFiles%\Microsoft\Exchange Server\ClientAccess\Owa\Auth\`; the malicious file by the same name is saved in `%ProgramFiles%\Microsoft\Exchange Server\ClientAccess\Owa\bin\`.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [OwaAuth](https://attack.mitre.org/software/S0072) captures and DES-encrypts credentials before writing the username and password to a log file, `C:\log.txt`.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [OwaAuth](https://attack.mitre.org/software/S0072) has a command to list its directory and logical drives.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [OwaAuth](https://attack.mitre.org/software/S0072) has a command to timestop a file or directory.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [OwaAuth](https://attack.mitre.org/software/S0072) DES-encrypts captured credentials using the key 12345678 before writing the credentials to a log file.[^1]  |
| [[IIS Components\|T1505.004]] | IIS Components | [OwaAuth](https://attack.mitre.org/software/S0072) has been loaded onto Exchange servers and disguised as an ISAPI filter (owaauth.dll). The IIS w3wp.exe process then loads the malicious DLL.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OwaAuth](https://attack.mitre.org/software/S0072) uses incoming HTTP requests with a username keyword and commands and handles them as instructions to perform actions.[^1]  |




## References

[^1]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


