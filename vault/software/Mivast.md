---
aliases: 
    - S0080
    
mitre-attack: https://attack.mitre.org/software/S0080
---

## S0080

[Mivast](https://attack.mitre.org/software/S0080) is a backdoor that has been used by [Deep Panda](https://attack.mitre.org/groups/G0009). It was reportedly used in the Anthem breach. [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Mivast](https://attack.mitre.org/software/S0080) creates the following Registry entry: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Micromedia`.[^2]  |
| [[Security Account Manager\|T1003.002]] | Security Account Manager | [Mivast](https://attack.mitre.org/software/S0080) has the capability to gather NTLM password information.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Mivast](https://attack.mitre.org/software/S0080) has the capability to download and execute .exe files.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Mivast](https://attack.mitre.org/software/S0080) has the capability to open a remote shell and run basic commands.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Deep Panda\|G0009]] | Deep Panda |



## References

[^1]: Mivast


[^2]: [Symantec Backdoor.Mivast](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)


[^3]: [Symantec Black Vine](https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf)


