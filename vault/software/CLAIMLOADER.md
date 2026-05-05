---
aliases: 
    - S1236
    
mitre-attack: https://attack.mitre.org/software/S1236
---

## S1236

[CLAIMLOADER](https://attack.mitre.org/software/S1236) is a malware variant that frequently accompanies legitimate executables that are used for DLL side-loading known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2021.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Component Object Model\|T1559.001]] | Component Object Model | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has leveraged Component Object Model (COM) objects to create a scheduled task using `ITaskService` interface.[^1]  |
| [[Native API\|T1106]] | Native API | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has used various Windows API calls during execution, when establishing persistence and defense evasion.[^2] [^1]   [CLAIMLOADER](https://attack.mitre.org/software/S1236) has also leveraged the legitimate API functions to run its shellcode through the callback function, including `GetDC()` and `EnumFontsW()`.[^2]   [CLAIMLOADER](https://attack.mitre.org/software/S1236) established persistence by utilizing the API `SHSetValue()`.[^2]  [CLAIMLOADER](https://attack.mitre.org/software/S1236) has utilized APIs with callback functions such as `EnumpropsExW`, `EnumSystemLanguageGroupsA`, and `EnumCalendarInfoExW`.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has added Registry Run keys to achieve persistence using `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.[^2] [^1]  |
| [[DLL\|T1574.001]] | DLL | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has used a legitimately signed executable to execute a malicious payload within a DLL file.[^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has modified file attributes to remain hidden to a standard user.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has imitated legitimate software directories through the creation and storage of the EXE and DLL in `C:\ProgramData\` and the use of legitimate looking names of software.[^1]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has created hardcoded mutex to ensure only a single instance of the malware is running.[^2] [^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has used tailored decoy documents as part of the installation routine to entice users to open attachments.[^1]  |
| [[Scheduled Task\|T1053.005]] | Scheduled Task | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has created scheduled tasks that execute the loader every five(5) minutes using `schtasks /F /Create /TN \"<fake_software_name>\" /SC minute /MO 5 /TR<br>\"C:\\ProgramData\\<path_to_exe> <hardcoded_argument>\`.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has decoded its payload prior to execution.[^2] [^1]  |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [CLAIMLOADER](https://attack.mitre.org/software/S1236) has utilized XOR-encrypted API names and native APIs of `LdrLoadDll()` and `LderGetProcedureAddress()` to resolve imports dynamically.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)


[^2]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)


