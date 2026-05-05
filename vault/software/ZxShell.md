---
aliases: 
    - S0412
    
mitre-attack: https://attack.mitre.org/software/S0412
---

## S0412

[ZxShell](https://attack.mitre.org/software/S0412) is a remote administration tool and backdoor that can be downloaded from the Internet, particularly from Chinese hacker websites. It has been used since at least 2004.[^5] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[VNC\|T1021.005]] | VNC | [ZxShell](https://attack.mitre.org/software/S0412) supports functionality for VNC sessions.[^2]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [ZxShell](https://attack.mitre.org/software/S0412) can collect the local hostname, operating system details, CPU speed, and total physical memory.[^2]   |
| [[Proxy\|T1090]] | Proxy | [ZxShell](https://attack.mitre.org/software/S0412) can set up an HTTP or SOCKS proxy.[^5] [^2]   |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ZxShell](https://attack.mitre.org/software/S0412) has used HTTP for C2 connections.[^2]   |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [ZxShell](https://attack.mitre.org/software/S0412) can use ports 1985 and 1986 in HTTP/S communication.[^2]  |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [ZxShell](https://attack.mitre.org/software/S0412) hooks several API functions to spawn system threads.[^2]   |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ZxShell](https://attack.mitre.org/software/S0412) has a command to open a file manager and explorer on the system.[^2]   |
| [[Screen Capture\|T1113]] | Screen Capture | [ZxShell](https://attack.mitre.org/software/S0412) can capture screenshots.[^5]  |
| [[Query Registry\|T1012]] | Query Registry | [ZxShell](https://attack.mitre.org/software/S0412) can query the netsvc group value data located in the svchost group Registry key.[^2]   |
| [[Data from Local System\|T1005]] | Data from Local System | [ZxShell](https://attack.mitre.org/software/S0412) can transfer files from a compromised host.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [ZxShell](https://attack.mitre.org/software/S0412) can collect the owner and organization information from the target workstation.[^2]   |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [ZxShell](https://attack.mitre.org/software/S0412) has been dropped through exploitation of CVE-2011-2462, CVE-2013-3163, and CVE-2014-0322.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [ZxShell](https://attack.mitre.org/software/S0412) has a command, ps, to obtain a listing of processes on the system.[^2]   |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [ZxShell](https://attack.mitre.org/software/S0412) can launch port scans.[^5] [^2]   |
| [[Modify Registry\|T1112]] | Modify Registry | [ZxShell](https://attack.mitre.org/software/S0412) can create Registry entries to enable services to run.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [ZxShell](https://attack.mitre.org/software/S0412) can delete files from the system.[^5] [^2]   |
| [[Windows Service\|T1543.003]] | Windows Service | [ZxShell](https://attack.mitre.org/software/S0412) can create a new service using the service parser function ProcessScCommand.[^2]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [ZxShell](https://attack.mitre.org/software/S0412) can kill AV products' processes.[^2]   |
| [[File Transfer Protocols\|T1071.002]] | File Transfer Protocols | [ZxShell](https://attack.mitre.org/software/S0412) has used FTP for C2 connections.[^2]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [ZxShell](https://attack.mitre.org/software/S0412) is injected into a shared SVCHOST process.[^2]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ZxShell](https://attack.mitre.org/software/S0412) can launch a reverse command shell.[^5] [^2] [^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [ZxShell](https://attack.mitre.org/software/S0412) can disable the firewall by modifying the registry key `HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile`.[^2]   |
| [[Remote Desktop Protocol\|T1021.001]] | Remote Desktop Protocol | [ZxShell](https://attack.mitre.org/software/S0412) has remote desktop functionality.[^2]   |
| [[Create Process with Token\|T1134.002]] | Create Process with Token | [ZxShell](https://attack.mitre.org/software/S0412) has a command called RunAs, which creates a new process as another user or process context.[^2]   |
| [[Video Capture\|T1125]] | Video Capture | [ZxShell](https://attack.mitre.org/software/S0412) has a command to perform video device spying.[^2]   |
| [[Rundll32\|T1218.011]] | Rundll32 | [ZxShell](https://attack.mitre.org/software/S0412) has used rundll32.exe to execute other DLLs and named pipes.[^2]   |
| [[Local Account\|T1136.001]] | Local Account | [ZxShell](https://attack.mitre.org/software/S0412) has a feature to create local user accounts.[^2]  |
| [[Endpoint Denial of Service\|T1499]] | Endpoint Denial of Service | [ZxShell](https://attack.mitre.org/software/S0412) has a feature to perform SYN flood attack on a host.[^5] [^2]   |
| [[Native API\|T1106]] | Native API | [ZxShell](https://attack.mitre.org/software/S0412) can leverage native API including `RegisterServiceCtrlHandler ` to register a service.RegisterServiceCtrlHandler  |
| [[Service Execution\|T1569.002]] | Service Execution | [ZxShell](https://attack.mitre.org/software/S0412) can create a new service for execution.[^2]  |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | [ZxShell](https://attack.mitre.org/software/S0412) has a command to clear system event logs.[^2]   |
| [[Keylogging\|T1056.001]] | Keylogging | [ZxShell](https://attack.mitre.org/software/S0412) has a feature to capture a remote computer's keystrokes using a keylogger.[^5] [^2]   |
| [[System Service Discovery\|T1007]] | System Service Discovery | [ZxShell](https://attack.mitre.org/software/S0412) can check the services on the system.[^2]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ZxShell](https://attack.mitre.org/software/S0412) has a command to transfer files from a remote host.[^2]   |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Axiom\|G0001]] | Axiom |
| [[APT41\|G0096]] | APT41 |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |



## References

[^1]: [Secureworks BRONZEUNION Feb 2019](https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox)


[^2]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)


[^3]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^4]: Sensocode


[^5]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)


[^6]: ZxShell


