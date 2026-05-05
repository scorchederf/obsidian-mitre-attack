---
aliases: 
    - S0481
    
mitre-attack: https://attack.mitre.org/software/S0481
---

## S0481

[Ragnar Locker](https://attack.mitre.org/software/S0481) is a ransomware that has been in use since at least December 2019.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Ragnar Locker](https://attack.mitre.org/software/S0481) encrypts files on the local machine and mapped drives prior to displaying a note demanding a ransom.[^2] [^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Ragnar Locker](https://attack.mitre.org/software/S0481) can delete volume shadow copies using `vssadmin delete shadows /all /quiet`.[^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Ragnar Locker](https://attack.mitre.org/software/S0481) has attempted to terminate/stop processes and services associated with endpoint security products.[^2]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used sc.exe to execute a service that it creates.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used cmd.exe and batch scripts to execute commands.[^2]  |
| [[Run Virtual Instance\|T1564.006]] | Run Virtual Instance | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used VirtualBox and a stripped Windows XP virtual machine to run itself. The use of a shared folder specified in the configuration enables [Ragnar Locker](https://attack.mitre.org/software/S0481) to encrypt files on the host operating system, including files on any mapped drives.[^2]  |
| [[Service Stop\|T1489]] | Service Stop | [Ragnar Locker](https://attack.mitre.org/software/S0481) has attempted to stop services associated with business applications and databases to release the lock on files used by these applications so they may be encrypted.[^2]  |
| [[System Location Discovery\|T1614]] | System Location Discovery | Before executing malicious code, [Ragnar Locker](https://attack.mitre.org/software/S0481) checks the Windows API `GetLocaleInfoW` and doesn't encrypt files if it finds a former Soviet country.[^4]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used regsvr32.exe to execute components of VirtualBox.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used sc.exe to create a new service for the VirtualBox driver.[^2]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Ragnar Locker](https://attack.mitre.org/software/S0481) has been delivered as an unsigned MSI package that was executed with `msiexec.exe`.[^2]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Ragnar Locker](https://attack.mitre.org/software/S0481) has used rundll32.exe to execute components of VirtualBox.[^2]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Ragnar Locker](https://attack.mitre.org/software/S0481) may attempt to connect to removable drives and mapped network drives.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN8\|G0061]] | FIN8 |



## References

[^1]: [Cynet Ragnar Apr 2020](https://www.cynet.com/blog/cynet-detection-report-ragnar-locker-ransomware/)


[^2]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)


[^3]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)


[^4]: [FBI Ragnar Locker 2020](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)


