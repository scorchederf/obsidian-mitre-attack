---
aliases: 
    - Velvet Ant
mitre-attack: https://attack.mitre.org/groups/G1047
---

## G1047

[Velvet Ant](https://attack.mitre.org/groups/G1047) is a threat actor operating since at least 2021. [Velvet Ant](https://attack.mitre.org/groups/G1047) is associated with complex persistence mechanisms, the targeting of network devices and appliances during operations, and the use of zero day exploits.[^1] [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Velvet Ant](https://attack.mitre.org/groups/G1047) has tunneled traffic from victims through an internal, compromised host to proxy communications to command and control nodes.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Velvet Ant](https://attack.mitre.org/groups/G1047) has used malicious DLLs executed via legitimate EXE files through DLL search order hijacking to launch follow-on payloads such as [PlugX](https://attack.mitre.org/software/S0013).[^1]  |
| [[Data Encoding\|T1132]] | Data Encoding | [Velvet Ant](https://attack.mitre.org/groups/G1047) sent commands to compromised F5 BIG-IP devices in an encoded format requiring a passkey before interpretation and execution.[^1]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Velvet Ant](https://attack.mitre.org/groups/G1047) used the `wmiexec.py` tool within [Impacket](https://attack.mitre.org/software/S0357) for remote process execution via WMI.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Velvet Ant](https://attack.mitre.org/groups/G1047) used a custom tool, VELVETSTING, to parse encoded inbound commands to compromised F5 BIG-IP devices and then execute them via the Unix shell.[^1]   |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Velvet Ant](https://attack.mitre.org/groups/G1047) has used random high number ports for [PlugX](https://attack.mitre.org/software/S0013) listeners on victim devices.[^1]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Velvet Ant](https://attack.mitre.org/groups/G1047) has leveraged access to internet-facing remote services to compromise and retain access to victim environments.[^1]  |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [Velvet Ant](https://attack.mitre.org/groups/G1047) transferred files laterally within victim networks through the [Impacket](https://attack.mitre.org/software/S0357) toolkit.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [Velvet Ant](https://attack.mitre.org/groups/G1047) has used a custom tool, "VELVETTAP", to perform packet capture from compromised F5 BIG-IP devices.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Velvet Ant](https://attack.mitre.org/groups/G1047) has enumerated local files and folders on victim devices.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [Velvet Ant](https://attack.mitre.org/groups/G1047) modified system firewall settings during [PlugX](https://attack.mitre.org/software/S0013) installation using `netsh.exe` to open a listening, random high number port on victim devices.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Velvet Ant](https://attack.mitre.org/groups/G1047) has used a reverse SSH shell to securely communicate with victim devices.[^1]  |
| [[Service Execution\|T1569.002]] | Service Execution | [Velvet Ant](https://attack.mitre.org/groups/G1047) executed and installed [PlugX](https://attack.mitre.org/software/S0013) as a Windows service.[^1]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Velvet Ant](https://attack.mitre.org/groups/G1047) has enumerated existing network connections on victim devices.[^1]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [Velvet Ant](https://attack.mitre.org/groups/G1047) used a modified `/etc/rc.local` file on compromised F5 BIG-IP devices to maintain persistence.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Velvet Ant](https://attack.mitre.org/groups/G1047) attempted to disable local security tools and endpoint detection and response (EDR) software during operations.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [Velvet Ant](https://attack.mitre.org/groups/G1047) initial execution included launching multiple `svchost` processes and injecting code into them.[^1]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Velvet Ant](https://attack.mitre.org/groups/G1047) has used reverse SSH tunnels to communicate to victim devices.[^1]  |
| [[Exploitation for Stealth\|T1211]] | Exploitation for Stealth | [Velvet Ant](https://attack.mitre.org/groups/G1047) exploited CVE-2024-20399 in Cisco Switches to which the threat actor was already able to authenticate in order to escape the NX-OS command line interface and gain access to the underlying operating system for arbitrary command execution.[^2]  |
| [[Local Accounts\|T1078.003]] | Local Accounts | [Velvet Ant](https://attack.mitre.org/groups/G1047) accessed vulnerable Cisco switch devices using accounts with administrator privileges.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Velvet Ant](https://attack.mitre.org/groups/G1047) used a malicious DLL, `iviewers.dll`, that mimics the legitimate "OLE/COM Object Viewer" within Windows.[^1]  |
| [[SMB／Windows Admin Shares\|T1021.002]] | SMB／Windows Admin Shares | [Velvet Ant](https://attack.mitre.org/groups/G1047) has transferred tools within victim environments using SMB.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Impacket\|S0357]] | Impacket | [Velvet Ant](https://attack.mitre.org/groups/G1047) used [Impacket](https://attack.mitre.org/software/S0357) for lateral tool transfer and remote process execution.[^1]  |
| [[PlugX\|S0013]] | PlugX | [Velvet Ant](https://attack.mitre.org/groups/G1047) heavily relies on variants of [PlugX](https://attack.mitre.org/software/S0013) for various phases of operations.[^1]  |



## References

[^1]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)


[^2]: [Sygnia VelvetAnt 2024B](https://www.sygnia.co/threat-reports-and-advisories/china-nexus-threat-group-velvet-ant-exploits-cisco-0-day/)


