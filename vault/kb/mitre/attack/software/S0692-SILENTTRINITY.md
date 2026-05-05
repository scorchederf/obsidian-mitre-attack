---
aliases: 
    - S0692
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0692-SILENTTRINITY
---

## Description

[[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] is an open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo. [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] was used in a 2019 campaign against Croatian government agencies by unidentified cyber actors.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-LSASS_Memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can create a memory dump of LSASS via the `MiniDumpWriteDump Win32` API call.[^3]  |
| [[kb/mitre/attack/techniques/T1007-System_Service_Discovery\|T1007]] | System Service Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can search for modifiable services that could be used for privilege escalation.[^3]  |
| [[kb/mitre/attack/techniques/T1010-Application_Window_Discovery\|T1010]] | Application Window Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.[^3]  |
| [[kb/mitre/attack/techniques/T1012-Query_Registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.[^3]  |
| [[kb/mitre/attack/techniques/T1018-Remote_System_Discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate and collect the properties of domain computers.[^3]  |
| [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|T1021.003]] | Distributed Component Object Model | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use `System` namespace methods to execute lateral movement using DCOM.[^3]  |
| [[kb/mitre/attack/techniques/T1021.006-Windows_Remote_Management\|T1021.006]] | Windows Remote Management | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] tracks `TrustedHosts` and can move laterally to these targets via WinRM.[^3]  |
| [[kb/mitre/attack/techniques/T1033-System_Owner_User_Discovery\|T1033]] | System Owner／User Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can gather a list of logged on users.[^3]   |
| [[kb/mitre/attack/techniques/T1041-Exfiltration_Over_C2_Channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can transfer files from an infected host to the C2 server.[^3]  |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can scan for open ports on a compromised machine.[^3]  |
| [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use WMI for lateral movement.[^3]  |
| [[kb/mitre/attack/techniques/T1055-Process_Injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can inject shellcode directly into Excel.exe or a specific process.[^3]  |
| [[kb/mitre/attack/techniques/T1056.001-Keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has a keylogging capability.[^3]  |
| [[kb/mitre/attack/techniques/T1056.002-GUI_Input_Capture\|T1056.002]] | GUI Input Capture | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]]'s `credphisher.py` module can prompt a current user for their credentials.[^3]  |
| [[kb/mitre/attack/techniques/T1057-Process_Discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.[^3]  |
| [[kb/mitre/attack/techniques/T1059.001-PowerShell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use PowerShell to execute commands.[^3]  |
| [[kb/mitre/attack/techniques/T1059.003-Windows_Command_Shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use `cmd.exe` to enable lateral movement using DCOM.[^3]  |
| [[kb/mitre/attack/techniques/T1059.006-Python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] is written in Python and can use multiple Python scripts for execution on targeted systems.[^2] [^3]  |
| [[kb/mitre/attack/techniques/T1069.001-Local_Groups\|T1069.001]] | Local Groups | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can obtain a list of local groups and members.[^3]  |
| [[kb/mitre/attack/techniques/T1069.002-Domain_Groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use `System.DirectoryServices` namespace to retrieve domain group information.[^3]  |
| [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can remove artifacts from the compromised host, including created Registry keys.[^3]  |
| [[kb/mitre/attack/techniques/T1070.004-File_Deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can remove files from the compromised host.[^3]  |
| [[kb/mitre/attack/techniques/T1082-System_Information_Discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect information related to a compromised host, including OS version.[^3]  |
| [[kb/mitre/attack/techniques/T1083-File_and_Directory_Discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.[^3]   |
| [[kb/mitre/attack/techniques/T1087.002-Domain_Account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can use `System.Security.AccessControl` namespaces to retrieve domain user information.[^3]    |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can load additional files and tools, including [[kb/mitre/attack/software/S0002-Mimikatz\|Mimikatz]].[^3]  |
| [[kb/mitre/attack/techniques/T1106-Native_API\|T1106]] | Native API | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.[^3]  |
| [[kb/mitre/attack/techniques/T1112-Modify_Registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).[^3]  |
| [[kb/mitre/attack/techniques/T1113-Screen_Capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can take a screenshot of the current desktop.[^3]  |
| [[kb/mitre/attack/techniques/T1115-Clipboard_Data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.[^4]    |
| [[kb/mitre/attack/techniques/T1124-System_Time_Discovery\|T1124]] | System Time Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect start time information from a compromised host.[^3]  |
| [[kb/mitre/attack/techniques/T1134.001-Token_Impersonation_Theft\|T1134.001]] | Token Impersonation／Theft | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can find a process owned by a specific user and impersonate the associated token.[^3]  |
| [[kb/mitre/attack/techniques/T1134.003-Make_and_Impersonate_Token\|T1134.003]] | Make and Impersonate Token | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can make tokens from known credentials.[^4]   |
| [[kb/mitre/attack/techniques/T1135-Network_Share_Discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can enumerate shares on a compromised host.[^3]  |
| [[kb/mitre/attack/techniques/T1518.001-Security_Software_Discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can determine if an anti-virus product is installed through the resolution of the service's virtual SID.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-Windows_Service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can establish persistence by creating a new service.[^3]  |
| [[kb/mitre/attack/techniques/T1546.001-Change_Default_File_Association\|T1546.001]] | Change Default File Association | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can conduct an image hijack of an `.msc` file extension as part of its UAC bypass process.[^3]  |
| [[kb/mitre/attack/techniques/T1546.003-Windows_Management_Instrumentation_Event_Subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can create a WMI Event to execute a payload for persistence.[^3]  |
| [[kb/mitre/attack/techniques/T1546.015-Component_Object_Model_Hijacking\|T1546.015]] | Component Object Model Hijacking | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can add a CLSID key for payload execution through `Registry.CurrentUser.CreateSubKey("Software\\Classes\\CLSID\\{" + clsid + "}\\InProcServer32")`.[^3]  |
| [[kb/mitre/attack/techniques/T1547.001-Registry_Run_Keys_Startup_Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can establish a LNK file in the startup folder for persistence.[^3]  |
| [[kb/mitre/attack/techniques/T1548.002-Bypass_User_Account_Control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] contains a number of modules that can bypass UAC, including through Window's Device Manager, Manage Optional Features, and an image hijack on the `.msc` file extension.[^3]     |
| [[kb/mitre/attack/techniques/T1552.006-Group_Policy_Preferences\|T1552.006]] | Group Policy Preferences | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has a module that can extract cached GPP passwords.[^3]   |
| [[kb/mitre/attack/techniques/T1555.003-Credentials_from_Web_Browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect clear text web credentials for Internet Explorer/Edge.[^3]  |
| [[kb/mitre/attack/techniques/T1555.004-Windows_Credential_Manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can gather Windows Vault credentials.[^3]   |
| [[kb/mitre/attack/techniques/T1556-Modify_Authentication_Process\|T1556]] | Modify Authentication Process | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.[^3]  |
| [[kb/mitre/attack/techniques/T1558.003-Kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] contains a module to conduct Kerberoasting.[^3]  |
| [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|T1559.001]] | Component Object Model | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can insert malicious shellcode into Excel.exe using a `Microsoft.Office.Interop` object.[^4]   |
| [[kb/mitre/attack/techniques/T1564.003-Hidden_Window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] has the ability to set its window state to hidden.[^3]  |
| [[kb/mitre/attack/techniques/T1620-Reflective_Code_Loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^4]    |
| [[kb/mitre/attack/techniques/T1680-Local_Storage_Discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can collect information related to a compromised host, including a list of drives.[^3]  |
| [[kb/mitre/attack/techniques/T1685-Disable_or_Modify_Tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]]'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.[^3]  |
| [[kb/mitre/attack/techniques/T1689-Downgrade_Attack\|T1689]] | Downgrade Attack | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can downgrade NTLM to capture NTLM hashes.[^4]   |
| [[kb/mitre/attack/techniques/T1690-Prevent_Command_History_Logging\|T1690]] | Prevent Command History Logging | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory.[^3]  |





> [!info]- References
> [^1]: [Security Affairs SILENTTRINITY July 2019](https://securityaffairs.co/wordpress/88021/apt/croatia-government-silenttrinity-malware.html)

> [^2]: [GitHub SILENTTRINITY March 2022](https://github.com/byt3bl33d3r/SILENTTRINITY)

> [^3]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)

> [^4]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)

> [^5]: SILENTTRINITY


