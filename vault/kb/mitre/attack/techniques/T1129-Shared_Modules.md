---
aliases: 
    - T1129
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1129-Shared_Modules
tactic: 
     - Execution
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]]).<br><br>Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.<br><br>The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in `dlfcn.h` in functions such as `dlopen` and `dlsym`. Although macOS can execute `.so` files, common practice uses `.dylib` files.[^4] [^5] [^1] [^3] <br><br>The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in `NTDLL.dll` and is part of the Windows [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] which is called from functions like `LoadLibrary` at run time.[^2] 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Identify and block potentially malicious software executed through this technique by using application control tools capable of preventing unknown modules from being loaded. |






> [!info]- References
> [^1]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)

> [^2]: [Microsoft DLL](https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library)

> [^3]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)

> [^4]: [Apple Dev Dynamic Libraries](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html)

> [^5]: [Linux Shared Libraries](https://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html)


