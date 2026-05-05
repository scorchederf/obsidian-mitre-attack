---
aliases: 
    - M1038
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1038-Execution_Prevention
---

## Description

Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:<br><br>Application Control:<br><br>- Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution.<br>- Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) <br><br><br>Script Blocking:<br><br>- Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources.<br>- Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) <br><br>Executable Blocking:<br><br>- Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories.<br>- Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories.<br><br>Dynamic Analysis Prevention:<br>- Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time.<br>- Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1036-Masquerading\|T1036]] | Masquerading | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[kb/mitre/attack/techniques/T1036.005-Match_Legitimate_Resource_Name_or_Location\|T1036.005]] | Match Legitimate Resource Name or Location | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| [[kb/mitre/attack/techniques/T1036.008-Masquerade_File_Type\|T1036.008]] | Masquerade File Type | Ensure that input sanitization is performed and that files are validated properly before execution; furthermore, implement a strict allow list to ensure that only authorized file types are processed.[^1]  Restrict and/or block execution of files where headers and extensions do not match. <br><br> |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | Use application control configured to block execution of `wmic.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `wmic.exe` application and to prevent abuse.[^13]  |
| [[kb/mitre/attack/techniques/T1059-Command_and_Scripting_Interpreter\|T1059]] | Command and Scripting Interpreter | Use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^27]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | Use application control where appropriate. PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^27]  |
| [[kb/mitre/attack/techniques/T1059.002-AppleScript\|T1059.002]] | AppleScript | Use application control where appropriate. |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | Use application control where appropriate. |
| [[kb/mitre/attack/techniques/T1059.004-Unix_Shell\|T1059.004]] | Unix Shell | Use application control where appropriate. On ESXi hosts, the `execInstalledOnly` feature prevents binaries from being run unless they have been packaged and signed as part of a vSphere installation bundle (VIB).[^15]  |
| [[kb/mitre/attack/techniques/T1059.005-Visual_Basic\|T1059.005]] | Visual Basic | Use application control where appropriate. VBA macros obtained from the Internet, based on the file's Mark of the Web (MOTW) attribute, may be blocked from executing in Office applications (ex: Access, Excel, PowerPoint, Visio, and Word) by default starting in Windows Version 2203.[^21]  |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | Denylist Python where not required. |
| [[kb/mitre/attack/techniques/T1059.007-JavaScript\|T1059.007]] | JavaScript | Denylist scripting where appropriate. |
| [[kb/mitre/attack/techniques/T1059.008-Network_Device_CLI\|T1059.008]] | Network Device CLI | TACACS+ can keep control over which commands administrators are permitted to use through the configuration of authentication and command authorization. [^23]  |
| [[kb/mitre/attack/techniques/T1059.009-Cloud_API\|T1059.009]] | Cloud API | Use application control where appropriate to block use of PowerShell CmdLets or other host based resources to access cloud API resources. |
| [[kb/mitre/attack/techniques/T1059.010-AutoHotKey_AutoIT\|T1059.010]] | AutoHotKey & AutoIT | Use application control to prevent execution of `AutoIt3.exe`, `AutoHotkey.exe`, and other related features that may not be required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1059.011-Lua\|T1059.011]] | Lua | Denylist Lua interpreters where appropriate. |
| [[kb/mitre/attack/techniques/T1059.013-Container_CLI_API\|T1059.013]] | Container CLI／API | Deny scripting where appropriate. Tools such as Python or Go can utilize Kubernetes and Docker within a client library and execute commands within their application. |
| [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|T1068]] | Exploitation for Privilege Escalation | Consider blocking the execution of known vulnerable drivers that adversaries may exploit to execute code in kernel mode. Validate driver block rules in audit mode to ensure stability prior to production deployment.[^16]  |
| [[kb/mitre/attack/techniques/T1080-Taint_Shared_Content\|T1080]] | Taint Shared Content | Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using application control [^20]  tools, like AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | Identify and block potentially malicious software executed that may be executed through this technique by using application control [^20]  tools, like Windows Defender Application Control[^25] , AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1127-Trusted_Developer_Utilities_Proxy_Execution\|T1127]] | Trusted Developer Utilities Proxy Execution | Certain developer utilities should be blocked or restricted if not required. |
| [[kb/mitre/attack/techniques/T1127.001-MSBuild\|T1127.001]] | MSBuild | Use application control configured to block execution of `msbuild.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `msbuild.exe` application and to prevent abuse.[^13]  |
| [[kb/mitre/attack/techniques/T1127.003-JamPlus\|T1127.003]] | JamPlus | Consider blocking or restricting JamPlus if not required. |
| [[kb/mitre/attack/techniques/T1129-Shared_Modules\|T1129]] | Shared Modules | Identify and block potentially malicious software executed through this technique by using application control tools capable of preventing unknown modules from being loaded. |
| [[kb/mitre/attack/techniques/T1176-Software_Extensions\|T1176]] | Software Extensions | Set an extension allow or deny list as appropriate for your security policy.  |
| [[kb/mitre/attack/techniques/T1176.001-Browser_Extensions\|T1176.001]] | Browser Extensions | Set a browser extension allow or deny list as appropriate for your security policy.[^9]  |
| [[kb/mitre/attack/techniques/T1176.002-IDE_Extensions\|T1176.002]] | IDE Extensions | Set an IDE extension allow or deny list as appropriate for your security policy.   |
| [[kb/mitre/attack/techniques/T1204-User_Execution\|T1204]] | User Execution | Application control may be able to prevent the running of executables masquerading as other files. |
| [[kb/mitre/attack/techniques/T1204.002-Malicious_File\|T1204.002]] | Malicious File | Application control may be able to prevent the running of executables masquerading as other files. |
| [[kb/mitre/attack/techniques/T1204.004-Malicious_Copy_and_Paste\|T1204.004]] | Malicious Copy and Paste | Use application control where appropriate. PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^27]  |
| [[kb/mitre/attack/techniques/T1216-System_Script_Proxy_Execution\|T1216]] | System Script Proxy Execution | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1216.001-PubPrn\|T1216.001]] | PubPrn | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1216.002-SyncAppvPublishingServer\|T1216.002]] | SyncAppvPublishingServer | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218-System_Binary_Proxy_Execution\|T1218]] | System Binary Proxy Execution | Consider using application control to prevent execution of binaries that are susceptible to abuse and not required for a given system or network. |
| [[kb/mitre/attack/techniques/T1218.001-Compiled_HTML_File\|T1218.001]] | Compiled HTML File | Consider using application control to prevent execution of hh.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.002-Control_Panel\|T1218.002]] | Control Panel | Identify and block potentially malicious and unknown .cpl files by using application control [^20]  tools, like Windows Defender Application Control[^25] , AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1218.003-CMSTP\|T1218.003]] | CMSTP | Consider using application control configured to block execution of CMSTP.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.004-InstallUtil\|T1218.004]] | InstallUtil | Use application control configured to block execution of InstallUtil.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.005-Mshta\|T1218.005]] | Mshta | Use application control configured to block execution of `mshta.exe` if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the `mshta.exe` application and to prevent abuse.[^13]  |
| [[kb/mitre/attack/techniques/T1218.008-Odbcconf\|T1218.008]] | Odbcconf | Use application control configured to block execution of Odbcconf.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.009-Regsvcs_Regasm\|T1218.009]] | Regsvcs／Regasm | Block execution of Regsvcs.exe and Regasm.exe if they are not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.012-Verclsid\|T1218.012]] | Verclsid | Use application control configured to block execution of verclsid.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.013-Mavinject\|T1218.013]] | Mavinject | Use application control configured to block execution of mavinject.exe if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.014-MMC\|T1218.014]] | MMC | Use application control configured to block execution of MMC if it is not required for a given system or network to prevent potential misuse by adversaries. |
| [[kb/mitre/attack/techniques/T1218.015-Electron_Applications\|T1218.015]] | Electron Applications | Where possible, enforce binary and application integrity with digital signature verification to prevent untrusted code from executing. For example, do not use `shell.openExternal` with untrusted content.<br><br>Where possible, set `nodeIntegration` to false, which disables access to the Node.js function.[^18]  By disabling access to the Node.js function, this may limit the ability to execute malicious commands by injecting JavaScript code.<br><br>Do not disable `webSecurity`, which may allow for users of the application to invoke malicious content from online sources. |
| [[kb/mitre/attack/techniques/T1219-Remote_Access_Tools\|T1219]] | Remote Access Tools | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[kb/mitre/attack/techniques/T1219.001-IDE_Tunneling\|T1219.001]] | IDE Tunneling | Use Group Policies to require user authentication by disabling anonymous tunnel access, preventing any unauthenticated tunnel creation or usage. Disable the Visual Studio Dev Tunnels feature to block tunnel-related commands, allowing only minimal exceptions for utility functions (unset, echo, ping, and user). Restrict tunnel access to approved Microsoft Entra tenant IDs by specifying allowed tenants; all other users are denied access by default.[^26] [^28]  |
| [[kb/mitre/attack/techniques/T1219.002-Remote_Desktop_Software\|T1219.002]] | Remote Desktop Software | Use application control to mitigate installation and use of unapproved software that can be used for remote access. |
| [[kb/mitre/attack/techniques/T1220-XSL_Script_Processing\|T1220]] | XSL Script Processing | If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries. |
| [[kb/mitre/attack/techniques/T1490-Inhibit_System_Recovery\|T1490]] | Inhibit System Recovery | Consider using application control configured to block execution of utilities such as `diskshadow.exe` that may not be required for a given system or network to prevent potential misuse by adversaries.  |
| [[kb/mitre/attack/techniques/T1505.004-IIS_Components\|T1505.004]] | IIS Components | Restrict unallowed ISAPI extensions and filters from running by specifying a list of ISAPI extensions and filters that can run on IIS.[^29]  |
| [[kb/mitre/attack/techniques/T1546.002-Screensaver\|T1546.002]] | Screensaver | Block .scr files from being executed from non-standard locations. |
| [[kb/mitre/attack/techniques/T1546.006-LC_LOAD_DYLIB_Addition\|T1546.006]] | LC_LOAD_DYLIB Addition | Allow applications via known hashes. |
| [[kb/mitre/attack/techniques/T1546.008-Accessibility_Features\|T1546.008]] | Accessibility Features | Adversaries can replace accessibility features binaries with alternate binaries to execute this technique. Identify and block potentially malicious software executed through accessibility features functionality by using application control [^20]  tools, like Windows Defender Application Control[^25] , AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1546.009-AppCert_DLLs\|T1546.009]] | AppCert DLLs | Adversaries install new AppCertDLL binaries to execute this technique. Identify and block potentially malicious software executed through AppCertDLLs functionality by using application control [^20]  tools, like Windows Defender Application Control[^25] , AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1546.010-AppInit_DLLs\|T1546.010]] | AppInit DLLs | Adversaries can install new AppInit DLLs binaries to execute this technique. Identify and block potentially malicious software executed through AppInit DLLs functionality by using application control [^20]  tools, like Windows Defender Application Control[^25] , AppLocker, [^12]  [^10]  or Software Restriction Policies [^5]  where appropriate. [^24]  |
| [[kb/mitre/attack/techniques/T1547.004-Winlogon_Helper_DLL\|T1547.004]] | Winlogon Helper DLL | Identify and block potentially malicious software that may be executed through the Winlogon helper process by using application control [^20]  tools like AppLocker [^12]  [^10]  that are capable of auditing and/or blocking unknown DLLs. |
| [[kb/mitre/attack/techniques/T1547.006-Kernel_Modules_and_Extensions\|T1547.006]] | Kernel Modules and Extensions | Application control and software restriction tools, such as SELinux, KSPP, grsecurity MODHARDEN, and Linux kernel tuning can aid in restricting kernel module loading.[^3] [^2] [^7] [^4] [^8]  |
| [[kb/mitre/attack/techniques/T1547.009-Shortcut_Modification\|T1547.009]] | Shortcut Modification | Prevents malicious shortcuts or LNK files from executing unwanted code by ensuring only authorized applications and scripts are allowed to run. |
| [[kb/mitre/attack/techniques/T1548-Abuse_Elevation_Control_Mechanism\|T1548]] | Abuse Elevation Control Mechanism | System settings can prevent applications from running that haven't been downloaded from legitimate repositories which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| [[kb/mitre/attack/techniques/T1548.004-Elevated_Execution_with_Prompt\|T1548.004]] | Elevated Execution with Prompt | System settings can prevent applications from running that haven't been downloaded through the Apple Store which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| [[kb/mitre/attack/techniques/T1553-Subvert_Trust_Controls\|T1553]] | Subvert Trust Controls | System settings can prevent applications from running that haven't been downloaded through the Apple Store (or other legitimate repositories) which can help mitigate some of these issues. Also enable application control solutions such as AppLocker and/or Device Guard to block the loading of malicious content. |
| [[kb/mitre/attack/techniques/T1553.001-Gatekeeper_Bypass\|T1553.001]] | Gatekeeper Bypass | System settings can prevent applications from running that haven't been downloaded through the Apple Store which can help mitigate some of these issues.  |
| [[kb/mitre/attack/techniques/T1553.003-SIP_and_Trust_Provider_Hijacking\|T1553.003]] | SIP and Trust Provider Hijacking | Enable application control solutions such as AppLocker and/or Device Guard to block the loading of malicious SIP DLLs. |
| [[kb/mitre/attack/techniques/T1553.005-Mark-of-the-Web_Bypass\|T1553.005]] | Mark-of-the-Web Bypass | Consider blocking container file types at web and/or email gateways. Consider unregistering container file extensions in Windows File Explorer.[^11]  |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window | Limit or restrict program execution using anti-virus software. On MacOS, allowlist programs that are allowed to have the plist tag. All other programs should be considered suspicious. |
| [[kb/mitre/attack/techniques/T1564.006-Run_Virtual_Instance\|T1564.006]] | Run Virtual Instance | Use application control to mitigate installation and use of unapproved virtualization software. |
| [[kb/mitre/attack/techniques/T1574-Hijack_Execution_Flow\|T1574]] | Hijack Execution Flow | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[kb/mitre/attack/techniques/T1574.001-DLL\|T1574.001]] | DLL | Identify and block potentially malicious software executed through DLL hijacking by using application control solutions capable of blocking DLLs loaded by legitimate software.[^6]  |
| [[kb/mitre/attack/techniques/T1574.006-Dynamic_Linker_Hijacking\|T1574.006]] | Dynamic Linker Hijacking | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[kb/mitre/attack/techniques/T1574.007-Path_Interception_by_PATH_Environment_Variable\|T1574.007]] | Path Interception by PATH Environment Variable | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^19] [^25] [^12] [^10] [^14] [^22]  |
| [[kb/mitre/attack/techniques/T1574.008-Path_Interception_by_Search_Order_Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^19] [^25] [^12] [^10] [^14] [^22]  |
| [[kb/mitre/attack/techniques/T1574.009-Path_Interception_by_Unquoted_Path\|T1574.009]] | Path Interception by Unquoted Path | Adversaries will likely need to place new binaries in locations to be executed through this weakness. Identify and block potentially malicious software executed path interception by using application control tools, like Windows Defender Application Control, AppLocker, or Software Restriction Policies where appropriate.[^19] [^25] [^12] [^10] [^14] [^22]  |
| [[kb/mitre/attack/techniques/T1574.012-COR_PROFILER\|T1574.012]] | COR_PROFILER | Identify and block potentially malicious unmanaged COR_PROFILER profiling DLLs  by using application control solutions like AppLocker that are capable of auditing and/or blocking unapproved DLLs.[^20] [^12] [^10]  |
| [[kb/mitre/attack/techniques/T1609-Container_Administration_Command\|T1609]] | Container Administration Command | Use read-only containers, read-only file systems, and minimal images when possible to prevent the execution of commands.[^17]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^30]  |
| [[kb/mitre/attack/techniques/T1611-Escape_to_Host\|T1611]] | Escape to Host | Use read-only containers, read-only file systems, and minimal images when possible to prevent the running of commands.[^17]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^30]  |
| [[kb/mitre/attack/techniques/T1674-Input_Injection\|T1674]] | Input Injection | Denylist scripting and use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., `Add-Type`).[^27]  |
| [[kb/mitre/attack/techniques/T1685-Disable_or_Modify_Tools\|T1685]] | Disable or Modify Tools | Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems. |
| [[kb/mitre/attack/techniques/T1685.003-Modify_or_Spoof_Tool_UI\|T1685.003]] | Modify or Spoof Tool UI | Use application controls to mitigate installation and use of payloads that may be utilized to spoof security alerting. |



> [!info]- References
> [^1]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)

> [^2]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)

> [^3]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)

> [^4]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)

> [^5]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))

> [^6]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)

> [^7]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)

> [^8]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)

> [^9]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)

> [^10]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

> [^11]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)

> [^12]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)

> [^13]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)

> [^14]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)

> [^15]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)

> [^16]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)

> [^17]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

> [^18]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)

> [^19]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)

> [^20]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)

> [^21]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)

> [^22]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)

> [^23]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)

> [^24]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)

> [^25]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)

> [^26]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)

> [^27]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)

> [^28]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)

> [^29]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)

> [^30]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


