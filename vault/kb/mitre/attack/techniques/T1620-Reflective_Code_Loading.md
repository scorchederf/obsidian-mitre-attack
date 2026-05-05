---
aliases: 
    - T1620
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1620-Reflective_Code_Loading
tactic: 
     - Stealth
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [[kb/mitre/attack/techniques/T1129-Shared_Modules\|Shared Modules]]).<br><br>Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).[^2] [^12] [^9] [^5] [^11]  For example, the `Assembly.Load()` method executed by [[kb/mitre/attack/techniques/T1059.001-PowerShell\|PowerShell]] may be abused to load raw code into the running process.[^10] <br><br>Reflective code injection is very similar to [[kb/mitre/attack/techniques/T1055-Process_Injection\|Process Injection]] except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.[^9] [^5] [^6] [^1] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0194-PowerSploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-PowerSploit\|PowerSploit]] reflectively loads a Windows PE file into a process.[^13] [^3]  |
| [[kb/mitre/attack/software/S0692-SILENTTRINITY\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-SILENTTRINITY\|SILENTTRINITY]] can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^7]    |
| [[kb/mitre/attack/software/S0695-Donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-Donut\|Donut]] can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.[^4]  |
| [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-Brute_Ratel_C4\|Brute Ratel C4]] has used reflective loading to execute malicious DLLs.[^8]  |








> [!info]- References
> [^1]: [S1 Old Rat New Tricks](https://www.sentinelone.com/blog/teaching-an-old-rat-new-tricks/)

> [^2]: [Introducing Donut](https://thewover.github.io/Introducing-Donut/)

> [^3]: [PowerSploit Documentation](http://powersploit.readthedocs.io)

> [^4]: [Donut Github](https://github.com/TheWover/donut)

> [^5]: [00sec Droppers](https://0x00sec.org/t/super-stealthy-droppers/3715)

> [^6]: [Intezer ACBackdoor](https://intezer.com/acbackdoor-analysis-of-a-new-multiplatform-backdoor/)

> [^7]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)

> [^8]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)

> [^9]: [Stuart ELF Memory](https://magisterquis.github.io/2018/03/31/in-memory-only-elf-execution.html)

> [^10]: [Microsoft AssemblyLoad](https://learn.microsoft.com/dotnet/api/system.reflection.assembly.load)

> [^11]: [Mandiant BYOL](https://www.mandiant.com/resources/bring-your-own-land-novel-red-teaming-technique)

> [^12]: [S1 Custom Shellcode Tool](https://www.sentinelone.com/blog/building-a-custom-tool-for-shellcode-analysis/)

> [^13]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)


