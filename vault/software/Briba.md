---
aliases: 
    - S0204
    
mitre-attack: https://attack.mitre.org/software/S0204
---

## S0204

[Briba](https://attack.mitre.org/software/S0204) is a trojan used by [Elderwood](https://attack.mitre.org/groups/G0066) to open a backdoor and download files on to compromised hosts. [^2]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Service\|T1543.003]] | Windows Service | [Briba](https://attack.mitre.org/software/S0204) installs a service pointing to a malicious DLL dropped to disk.[^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Briba](https://attack.mitre.org/software/S0204) uses rundll32 within [Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001) entries to execute malicious DLLs.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Briba](https://attack.mitre.org/software/S0204) downloads files onto infected hosts.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Briba](https://attack.mitre.org/software/S0204) creates run key Registry entries pointing to malicious DLLs dropped to disk.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Elderwood\|G0066]] | Elderwood |



## References

[^1]: Briba


[^2]: [Symantec Elderwood Sept 2012](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)


[^3]: [Symantec Briba May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)


