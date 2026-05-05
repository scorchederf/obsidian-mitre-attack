---
aliases: 
    - S0118
    
mitre-attack: https://attack.mitre.org/software/S0118
---

## S0118

[Nidiran](https://attack.mitre.org/software/S0118) is a custom backdoor developed and used by [Suckfly](https://attack.mitre.org/groups/G0039). It has been delivered via strategic web compromise. [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Nidiran](https://attack.mitre.org/software/S0118) can download and execute files.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Nidiran](https://attack.mitre.org/software/S0118) can create a new service named msamger (Microsoft Security Accounts Manager), which mimics the legitimate Microsoft database by the same name.[^1] [^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Nidiran](https://attack.mitre.org/software/S0118) can create a new service named msamger (Microsoft Security Accounts Manager).[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Suckfly\|G0039]] | Suckfly |



## References

[^1]: [Symantec Backdoor.Nidiran](https://www.symantec.com/security_response/writeup.jsp?docid=2015-120123-5521-99)


[^2]: [Microsoft SAM](https://support.microsoft.com/en-us/kb/310105)


[^3]: [Symantec Suckfly May 2016](http://www.symantec.com/connect/blogs/indian-organizations-targeted-suckfly-attacks)


[^4]: [Symantec Suckfly March 2016](http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates)


