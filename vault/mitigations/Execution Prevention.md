---
aliases: 
    - M1038
    
mitre-attack: https://attack.mitre.org/mitigations/M1038
---

## M1038

Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:<br><br>Application Control:<br><br>- Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution.<br>- Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) <br><br><br>Script Blocking:<br><br>- Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources.<br>- Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) <br><br>Executable Blocking:<br><br>- Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories.<br>- Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories.<br><br>Dynamic Analysis Prevention:<br>- Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time.<br>- Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[IDE Tunneling\|T1219.001]] | IDE Tunneling | Use Group Policies to require user authentication by disabling anonymous tunnel access, preventing any unauthenticated tunnel creation or usage. Disable the Visual Studio Dev Tunnels feature to block tunnel-related commands, allowing only minimal exceptions for utility functions (unset, echo, ping, and user). Restrict tunnel access to approved Microsoft Entra tenant IDs by specifying allowed tenants; all other users are denied access by default.[^12] [^4]  |
| [[SyncAppvPublishingServer\|T1216.002]] | SyncAppvPublishingServer | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[SIP and Trust Provider Hijacking\|T1553.003]] | SIP and Trust Provider Hijacking | Enable application control solutions such as AppLocker and/or Device Guard to block the loading of malicious SIP DLLs. |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | Use application control to prevent execution of `AutoIt3.exe`, `AutoHotkey.exe`, and other related features that may not be required for a given system or network to prevent potential misuse by adversaries. |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[Path Interception by Search Order Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^2] [^29] [^20] [^15] [^18] [^26]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[Screensaver\|T1546.002]] | Screensaver | Block .scr files from being executed from non-standard locations. |
| [[Hidden Window\|T1564.003]] | Hidden Window | Limit or restrict program execution using anti-virus software. On MacOS, allowlist programs that are allowed to have the plist tag. All other programs should be considered suspicious. |
| [[Subvert Trust Controls\|T1553]] | Subvert Trust Controls | System settings can prevent applications from running that haven't been downloaded through the Apple Store (or other legitimate repositories) which can help mitigate some of these issues. Also enable application control solutions such as AppLocker and/or Device Guard to block the loading of malicious content. |
| [[IDE Extensions\|T1176.002]] | IDE Extensions | Set an IDE extension allow or deny list as appropriate for your security policy.   |
| [[Mshta\|T1218.005]] | Mshta | Use application control configured to block execution of `mshta.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `mshta.exe` application and to prevent abuse.[^23]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | Use application control where appropriate. VBA macros obtained from the Internet, based on the file's Mark of the Web (MOTW) attribute, may be blocked from executing in Office applications (ex: Access, Excel, PowerPoint, Visio, and Word) by default starting in Windows Version 2203.[^14]  |
| [[InstallUtil\|T1218.004]] | InstallUtil | Use application control configured to block execution of InstallUtil.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[User Execution\|T1204]] | User Execution | Application control may be able to prevent the running of executables masquerading as other files. |
| [[DLL\|T1574.001]] | DLL | Identify and block potentially malicious software executed through DLL hijacking by using application control solutions capable of blocking DLLs loaded by legitimate software.[^30]  |
| [[Malicious Copy and Paste\|T1204.004]] | Malicious Copy and Paste | Use application control where appropriate. PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^22]  |
| [[Shared Modules\|T1129]] | Shared Modules | Identify and block potentially malicious software executed through this technique by using application control tools capable of preventing unknown modules from being loaded. |
| [[Regsvcs／Regasm\|T1218.009]] | Regsvcs／Regasm | Block execution of Regsvcs.exe and Regasm.exe if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | System settings can prevent applications from running that haven't been downloaded from legitimate repositories which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| [[Elevated Execution with Prompt\|T1548.004]] | Elevated Execution with Prompt | System settings can prevent applications from running that haven't been downloaded through the Apple Store which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| [[Escape to Host\|T1611]] | Escape to Host | Use read-only containers, read-only file systems, and minimal images when possible to prevent the running of commands.[^28]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^10]  |
| [[PubPrn\|T1216.001]] | PubPrn | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | Prevents malicious shortcuts or LNK files from executing unwanted code by ensuring only authorized applications and scripts are allowed to run. |
| [[Verclsid\|T1218.012]] | Verclsid | Use application control configured to block execution of verclsid.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Native API\|T1106]] | Native API | Identify and block potentially malicious software executed that may be executed through this technique by using application control [^7]  tools, like Windows Defender Application Control[^29] , AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[JamPlus\|T1127.003]] | JamPlus | Consider blocking or restricting JamPlus if not required. |
| [[Electron Applications\|T1218.015]] | Electron Applications | Where possible, enforce binary and application integrity with digital signature verification to prevent untrusted code from executing. For example, do not use `shell.openExternal` with untrusted content.<br><br>Where possible, set `nodeIntegration` to false, which disables access to the Node.js function.[^6]  By disabling access to the Node.js function, this may limit the ability to execute malicious commands by injecting JavaScript code.<br><br>Do not disable `webSecurity`, which may allow for users of the application to invoke malicious content from online sources. |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[System Script Proxy Execution\|T1216]] | System Script Proxy Execution | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | Use application control configured to block execution of `wmic.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `wmic.exe` application and to prevent abuse.[^23]  |
| [[Input Injection\|T1674]] | Input Injection | Denylist scripting and use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^22]  |
| [[JavaScript\|T1059.007]] | JavaScript | Denylist scripting where appropriate. |
| [[Malicious File\|T1204.002]] | Malicious File | Application control may be able to prevent the running of executables masquerading as other files. |
| [[AppInit DLLs\|T1546.010]] | AppInit DLLs | Adversaries can install new AppInit DLLs binaries to execute this technique. Identify and block potentially malicious software executed through AppInit DLLs functionality by using application control [^7]  tools, like Windows Defender Application Control[^29] , AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | Use application control where appropriate. On ESXi hosts, the `execInstalledOnly` feature prevents binaries from being run unless they have been packaged and signed as part of a vSphere installation bundle (VIB).[^16]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[IIS Components\|T1505.004]] | IIS Components | Restrict unallowed ISAPI extensions and filters from running by specifying a list of ISAPI extensions and filters that can run on IIS.[^9]  |
| [[Winlogon Helper DLL\|T1547.004]] | Winlogon Helper DLL | Identify and block potentially malicious software that may be executed through the Winlogon helper process by using application control [^7]  tools like AppLocker [^20]  [^15]  that are capable of auditing and/or blocking unknown DLLs. |
| [[AppleScript\|T1059.002]] | AppleScript | Use application control where appropriate. |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | System settings can prevent applications from running that haven't been downloaded through the Apple Store which can help mitigate some of these issues.  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | Ensure that input sanitization is performed and that files are validated properly before execution; furthermore, implement a strict allow list to ensure that only authorized file types are processed.[^5]  Restrict and/or block execution of files where headers and extensions do not match. <br><br> |
| [[Odbcconf\|T1218.008]] | Odbcconf | Use application control configured to block execution of Odbcconf.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems. |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | Use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^22]  |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^2] [^29] [^20] [^15] [^18] [^26]  |
| [[Trusted Developer Utilities Proxy Execution\|T1127]] | Trusted Developer Utilities Proxy Execution | Certain developer utilities should be blocked or restricted if not required. |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries.  |
| [[Network Device CLI\|T1059.008]] | Network Device CLI | TACACS+ can keep control over which commands administrators are permitted to use through the configuration of authentication and command authorization. [^24]  |
| [[System Binary Proxy Execution\|T1218]] | System Binary Proxy Execution | Consider using application control to prevent execution of binaries that are susceptible to abuse and not required for a given system or network. |
| [[Control Panel\|T1218.002]] | Control Panel | Identify and block potentially malicious and unknown .cpl files by using application control [^7]  tools, like Windows Defender Application Control[^29] , AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | Use application control where appropriate. |
| [[LC_LOAD_DYLIB Addition\|T1546.006]] | LC_LOAD_DYLIB Addition | Allow applications via known hashes. |
| [[XSL Script Processing\|T1220]] | XSL Script Processing | If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries. |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using application control [^7]  tools, like AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[Cloud API\|T1059.009]] | Cloud API | Use application control where appropriate to block use of PowerShell CmdLets or other host based resources to access cloud API resources. |
| [[Kernel Modules and Extensions\|T1547.006]] | Kernel Modules and Extensions | Application control and software restriction tools, such as SELinux, KSPP, grsecurity MODHARDEN, and Linux kernel tuning can aid in restricting kernel module loading.[^27] [^25] [^21] [^8] [^3]  |
| [[Path Interception by Unquoted Path\|T1574.009]] | Path Interception by Unquoted Path | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^2] [^29] [^20] [^15] [^18] [^26]  |
| [[Python\|T1059.006]] | Python | Denylist Python where not required. |
| [[Container CLI／API\|T1059.013]] | Container CLI／API | Deny scripting where appropriate. Tools such as Python or Go can utilize Kubernetes and Docker within a client library and execute commands within their application. |
| [[Lua\|T1059.011]] | Lua | Denylist Lua interpreters where appropriate. |
| [[MSBuild\|T1127.001]] | MSBuild | Use application control configured to block execution of `msbuild.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `msbuild.exe` application and to prevent abuse.[^23]  |
| [[COR_PROFILER\|T1574.012]] | COR_PROFILER | Identify and block potentially malicious unmanaged COR_PROFILER profiling DLLs  by using application control solutions like AppLocker that are capable of auditing and/or blocking unapproved DLLs.[^7] [^20] [^15]  |
| [[Accessibility Features\|T1546.008]] | Accessibility Features | Adversaries can replace accessibility features binaries with alternate binaries to execute this technique. Identify and block potentially malicious software executed through accessibility features functionality by using application control [^7]  tools, like Windows Defender Application Control[^29] , AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[AppCert DLLs\|T1546.009]] | AppCert DLLs | Adversaries install new AppCertDLL binaries to execute this technique. Identify and block potentially malicious software executed through AppCertDLLs functionality by using application control [^7]  tools, like Windows Defender Application Control[^29] , AppLocker, [^20]  [^15]  or Software Restriction Policies [^17]  where appropriate. [^13]  |
| [[Software Extensions\|T1176]] | Software Extensions | Set an extension allow or deny list as appropriate for your security policy.  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | Consider blocking the execution of known vulnerable drivers that adversaries may exploit to execute code in kernel mode. Validate driver block rules in audit mode to ensure stability prior to production deployment.[^1]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | Set a browser extension allow or deny list as appropriate for your security policy.[^11]  |
| [[Mark-of-the-Web Bypass\|T1553.005]] | Mark-of-the-Web Bypass | Consider blocking container file types at web and/or email gateways. Consider unregistering container file extensions in Windows File Explorer.[^19]  |
| [[CMSTP\|T1218.003]] | CMSTP | Consider using application control configured to block execution of CMSTP.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Remote Desktop Software\|T1219.002]] | Remote Desktop Software | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[Masquerading\|T1036]] | Masquerading | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[MMC\|T1218.014]] | MMC | Use application control configured to block execution of MMC if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | Consider using application control to prevent execution of hh.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Mavinject\|T1218.013]] | Mavinject | Use application control configured to block execution of mavinject.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[Run Virtual Instance\|T1564.006]] | Run Virtual Instance | Use application control to mitigate installation and use of unapproved virtualization software. |
| [[Container Administration Command\|T1609]] | Container Administration Command | Use read-only containers, read-only file systems, and minimal images when possible to prevent the execution of commands.[^28]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^10]  |
| [[Modify or Spoof Tool UI\|T1685.003]] | Modify or Spoof Tool UI | Use application controls to mitigate installation and use of payloads that may be utilized to spoof security alerting. |
| [[PowerShell\|T1059.001]] | PowerShell | Use application control where appropriate. PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^22]  |


## References

[^1]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^2]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^3]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^4]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^5]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^6]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^7]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^8]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^9]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^10]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^11]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^12]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^13]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^14]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^15]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^16]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^17]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^18]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^19]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^20]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^21]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^22]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^23]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^24]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^25]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^26]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^27]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^28]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^29]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^30]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


