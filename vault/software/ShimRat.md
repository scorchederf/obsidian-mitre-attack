---
aliases: 
    - S0444
    
mitre-attack: https://attack.mitre.org/software/S0444
---

## S0444

[ShimRat](https://attack.mitre.org/software/S0444) has been used by the suspected China-based adversary [Mofang](https://attack.mitre.org/groups/G0103) in campaigns targeting multiple countries and sectors including government, military, critical infrastructure, automobile, and weapons development. The name "[ShimRat](https://attack.mitre.org/software/S0444)" comes from the malware's extensive use of Windows Application Shimming to maintain persistence. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ShimRat](https://attack.mitre.org/software/S0444) can download additional files.[^1]  |
| [[External Proxy\|T1090.002]] | External Proxy | [ShimRat](https://attack.mitre.org/software/S0444) can use pre-configured HTTP proxies.[^1]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [ShimRat](https://attack.mitre.org/software/S0444) has hijacked the cryptbase.dll within migwiz.exe to escalate privileges. This prevented the User Access Control window from appearing.[^1]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [ShimRat](https://attack.mitre.org/software/S0444) can hijack the cryptbase.dll within migwiz.exe to escalate privileges and bypass UAC controls.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [ShimRat](https://attack.mitre.org/software/S0444) has installed a registry based start-up key `HKCU\Software\microsoft\windows\CurrentVersion\Run` to maintain persistence should other methods fail.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [ShimRat](https://attack.mitre.org/software/S0444) can impersonate Windows services and antivirus products to avoid detection on compromised systems.[^1]  |
| [[Scheduled Transfer\|T1029]] | Scheduled Transfer | [ShimRat](https://attack.mitre.org/software/S0444) can sleep when instructed to do so by the C2.[^1] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [ShimRat](https://attack.mitre.org/software/S0444) can uninstall itself from compromised hosts, as well create and modify directories, delete, move, copy, and rename files.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [ShimRat](https://attack.mitre.org/software/S0444) communicated over HTTP and HTTPS with C2 servers.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [ShimRat](https://attack.mitre.org/software/S0444) can be issued a command shell function from the C2.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [ShimRat](https://attack.mitre.org/software/S0444) has decompressed its core DLL using shellcode once an impersonated antivirus component was running on a system.[^1]  |
| [[Application Shimming\|T1546.011]] | Application Shimming | [ShimRat](https://attack.mitre.org/software/S0444) has installed shim databases in the `AppPatch` folder.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [ShimRat](https://attack.mitre.org/software/S0444) has used a secondary C2 location if the first was unavailable.[^1] 	 |
| [[Software Packing\|T1027.002]] | Software Packing | [ShimRat](https://attack.mitre.org/software/S0444)'s loader has been packed with the compressed [ShimRat](https://attack.mitre.org/software/S0444) core DLL and the legitimate DLL for it to hijack.[^1]  |
| [[Compression\|T1027.015]] | Compression | [ShimRat](https://attack.mitre.org/software/S0444) has been delivered as a package that includes compressed DLL and shellcode payloads within a .dat file.[^1]  |
| [[Native API\|T1106]] | Native API | [ShimRat](https://attack.mitre.org/software/S0444) has used Windows API functions to install the service and shim.[^1] 	 |
| [[Windows Service\|T1543.003]] | Windows Service | [ShimRat](https://attack.mitre.org/software/S0444) has installed a Windows service to maintain persistence on victim machines.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [ShimRat](https://attack.mitre.org/software/S0444) can enumerate connected drives for infected host machines.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [ShimRat](https://attack.mitre.org/software/S0444) has the capability to upload collected files to a C2.[^1] 	 |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [ShimRat](https://attack.mitre.org/software/S0444) can list directories.[^1]  |
| [[Modify Registry\|T1112]] | Modify Registry | [ShimRat](https://attack.mitre.org/software/S0444) has registered two registry keys for shim databases.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mofang\|G0103]] | Mofang |



## References

[^1]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)


