---
aliases: 
    - T1574
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1574-Hijack_Execution_Flow
tactic: 
     - Stealth - Execution
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.<br><br>There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-Application_Developer_Guidance\|M1013]] | Application Developer Guidance | When possible, include hash values in manifest files to help prevent side-loading of malicious libraries.[^8]  |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service binary target path locations. Deny execution from user directories such as file download directories and temp directories where able.<br><br>Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory `C:` and system directories, such as `C:\Windows\`, to reduce places where malicious files could be placed for execution. |
| [[kb/mitre/attack/mitigations/M1022-Restrict_File_and_Directory_Permissions\|M1022]] | Restrict File and Directory Permissions | Install software in write-protected locations. Set directory access controls to prevent file writes to the search paths for applications, both in the folders where applications are run from and the standard library folders. |
| [[kb/mitre/attack/mitigations/M1024-Restrict_Registry_Permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[kb/mitre/attack/mitigations/M1040-Behavior_Prevention_on_Endpoint\|M1040]] | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of behaviors related to process injection/memory tampering based on common sequences of indicators (ex: execution of specific API functions). |
| [[kb/mitre/attack/mitigations/M1044-Restrict_Library_Loading\|M1044]] | Restrict Library Loading | Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+.<br><br>Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. `%SYSTEMROOT%`)to be used before local directory DLLs (e.g. a user's home directory)<br><br>The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode. The associated Windows Registry key for this is located at `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode`[^3] [^5]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Use auditing tools capable of detecting hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for hijacking weaknesses.[^2] <br><br>Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software.<br><br>Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^1] [^4] [^7]  |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Update software regularly to include patches that fix DLL side-loading vulnerabilities. |
| [[kb/mitre/attack/mitigations/M1052-User_Account_Control\|M1052]] | User Account Control | Turn off UAC's privilege elevation for standard users `[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]` to automatically deny elevation requests, add: `"ConsentPromptBehaviorUser"=dword:00000000`. Consider enabling installer detection for all users by adding: `"EnableInstallerDetection"=dword:00000001`. This will prompt for a password for installation and also log the attempt. To disable installer detection, instead add: `"EnableInstallerDetection"=dword:00000000`. This may prevent potential elevation of privileges through exploitation during the process of UAC detecting the installer, but will allow the installation process to continue without being logged.  [^6]  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1574.001-DLL\|T1574.001]] | DLL |
| [[kb/mitre/attack/techniques/T1574.004-Dylib_Hijacking\|T1574.004]] | Dylib Hijacking |
| [[kb/mitre/attack/techniques/T1574.005-Executable_Installer_File_Permissions_Weakness\|T1574.005]] | Executable Installer File Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.006-Dynamic_Linker_Hijacking\|T1574.006]] | Dynamic Linker Hijacking |
| [[kb/mitre/attack/techniques/T1574.007-Path_Interception_by_PATH_Environment_Variable\|T1574.007]] | Path Interception by PATH Environment Variable |
| [[kb/mitre/attack/techniques/T1574.008-Path_Interception_by_Search_Order_Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking |
| [[kb/mitre/attack/techniques/T1574.009-Path_Interception_by_Unquoted_Path\|T1574.009]] | Path Interception by Unquoted Path |
| [[kb/mitre/attack/techniques/T1574.010-Services_File_Permissions_Weakness\|T1574.010]] | Services File Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.011-Services_Registry_Permissions_Weakness\|T1574.011]] | Services Registry Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.012-COR_PROFILER\|T1574.012]] | COR_PROFILER |
| [[kb/mitre/attack/techniques/T1574.013-KernelCallbackTable\|T1574.013]] | KernelCallbackTable |
| [[kb/mitre/attack/techniques/T1574.014-AppDomainManager\|T1574.014]] | AppDomainManager |




> [!info]- References
> [^1]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)

> [^2]: [Powersploit](https://github.com/mattifestation/PowerSploit)

> [^3]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)

> [^4]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)

> [^5]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)

> [^6]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)

> [^7]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)

> [^8]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


