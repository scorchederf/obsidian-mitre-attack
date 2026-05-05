---
aliases: 
    - S0692
    
mitre-attack: https://attack.mitre.org/software/S0692
---

## S0692

[SILENTTRINITY](https://attack.mitre.org/software/S0692) is an open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo. [SILENTTRINITY](https://attack.mitre.org/software/S0692) was used in a 2019 campaign against Croatian government agencies by unidentified cyber actors.[^5] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a module that can extract cached GPP passwords.[^3]   |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^2]    |
| [[Domain Groups\|T1069.002]] | Domain Groups | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.DirectoryServices` namespace to retrieve domain group information.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can load additional files and tools, including [Mimikatz](https://attack.mitre.org/software/S0002).[^3]  |
| [[Change Default File Association\|T1546.001]] | Change Default File Association | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can conduct an image hijack of an `.msc` file extension as part of its UAC bypass process.[^3]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.[^2]    |
| [[Indicator Removal\|T1070]] | Indicator Removal | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove artifacts from the compromised host, including created Registry keys.[^3]  |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a memory dump of LSASS via the `MiniDumpWriteDump Win32` API call.[^3]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate shares on a compromised host.[^3]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to set its window state to hidden.[^3]  |
| [[Windows Service\|T1543.003]] | Windows Service | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish persistence by creating a new service.[^3]  |
| [[Local Groups\|T1069.001]] | Local Groups | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can obtain a list of local groups and members.[^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can take a screenshot of the current desktop.[^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use WMI for lateral movement.[^3]  |
| [[Process Injection\|T1055]] | Process Injection | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can inject shellcode directly into Excel.exe or a specific process.[^3]  |
| [[Modify Registry\|T1112]] | Modify Registry | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^3]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect start time information from a compromised host.[^3]  |
| [[Windows Management Instrumentation Event Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a WMI Event to execute a payload for persistence.[^3]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can find a process owned by a specific user and impersonate the associated token.[^3]  |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.[^3]  |
| [[Query Registry\|T1012]] | Query Registry | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.[^3]  |
| [[Downgrade Attack\|T1689]] | Downgrade Attack | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can downgrade NTLM to capture NTLM hashes.[^2]   |
| [[Domain Account\|T1087.002]] | Domain Account | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System.Security.AccessControl` namespaces to retrieve domain user information.[^3]    |
| [[Remote System Discovery\|T1018]] | Remote System Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate and collect the properties of domain computers.[^3]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can remove files from the compromised host.[^3]  |
| [[Make and Impersonate Token\|T1134.003]] | Make and Impersonate Token | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can make tokens from known credentials.[^2]   |
| [[Python\|T1059.006]] | Python | [SILENTTRINITY](https://attack.mitre.org/software/S0692) is written in Python and can use multiple Python scripts for execution on targeted systems.[^5] [^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can scan for open ports on a compromised machine.[^3]  |
| [[PowerShell\|T1059.001]] | PowerShell | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use PowerShell to execute commands.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect clear text web credentials for Internet Explorer/Edge.[^3]  |
| [[Native API\|T1106]] | Native API | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.[^3]  |
| [[Kerberoasting\|T1558.003]] | Kerberoasting | [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a module to conduct Kerberoasting.[^3]  |
| [[Component Object Model Hijacking\|T1546.015]] | Component Object Model Hijacking | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can add a CLSID key for payload execution through `Registry.CurrentUser.CreateSubKey("Software\\Classes\\CLSID\\{" + clsid + "}\\InProcServer32")`.[^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can transfer files from an infected host to the C2 server.[^3]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather Windows Vault credentials.[^3]   |
| [[Distributed Component Object Model\|T1021.003]] | Distributed Component Object Model | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `System` namespace methods to execute lateral movement using DCOM.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^3]   |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including a list of drives.[^3]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [SILENTTRINITY](https://attack.mitre.org/software/S0692) contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.[^3]     |
| [[Component Object Model\|T1559.001]] | Component Object Model | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can insert malicious shellcode into Excel.exe using a `Microsoft.Office.Interop` object.[^2]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use `cmd.exe` to enable lateral movement using DCOM.[^3]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.[^3]  |
| [[Windows Remote Management\|T1021.006]] | Windows Remote Management | [SILENTTRINITY](https://attack.mitre.org/software/S0692) tracks `TrustedHosts` and can move laterally to these targets via WinRM.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can establish a LNK file in the startup folder for persistence.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^3]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `credphisher.py` module can prompt a current user for their credentials.[^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has a keylogging capability.[^3]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather a list of logged on users.[^3]   |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can determine if an anti-virus product is installed through the resolution of the service's virtual SID.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including OS version.[^3]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can search for modifiable services that could be used for privilege escalation.[^3]  |




## References

[^1]: [Security Affairs SILENTTRINITY July 2019](https://securityaffairs.co/wordpress/88021/apt/croatia-government-silenttrinity-malware.html)


[^2]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)


[^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)


[^4]: SILENTTRINITY


[^5]: [GitHub SILENTTRINITY March 2022](https://github.com/byt3bl33d3r/SILENTTRINITY)


