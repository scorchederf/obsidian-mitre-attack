---
aliases: 
    - T1622
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1622-Debugger_Evasion
tactic: 
     - Stealth - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.[^5] <br><br>Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to [[kb/mitre/attack/techniques/T1497-Virtualization_Sandbox_Evasion\|Virtualization/Sandbox Evasion]], if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.<br><br>Specific checks will vary based on the target and/or adversary. On Windows, this may involve [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] function calls such as `IsDebuggerPresent()` and ` NtQueryInformationProcess()`, or manually checking the `BeingDebugged` flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools.[^8] [^10]  Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).[^4] [^3] [^6] <br><br>Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue.[^7] <br><br>Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping [[kb/mitre/attack/techniques/T1106-Native_API\|Native API]] function calls such as `OutputDebugStringW()`.[^1] [^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1087-AsyncRAT\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-AsyncRAT\|AsyncRAT]] can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.[^2]  |








> [!info]- References
> [^1]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)

> [^2]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)

> [^3]: [AlKhaser Debug](https://github.com/LordNoteworthy/al-khaser/tree/master/al-khaser/AntiDebug)

> [^4]: [hasherezade debug](https://github.com/hasherezade/malware_training_vol1/blob/main/slides/module3/Module3_2_fingerprinting.pdf)

> [^5]: [ProcessHacker Github](https://github.com/processhacker/processhacker)

> [^6]: [vxunderground debug](https://web.archive.org/web/20250904153443/https://github.com/vxunderground/VX-API/tree/main#anti-debug)

> [^7]: [Apriorit](https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software)

> [^8]: [Cado Security P2PInfect 2023](https://www.cadosecurity.com/blog/p2pinfect-new-variant-targets-mips-devices)

> [^9]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)

> [^10]: [Positive Technologies Hellhounds 2023](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/hellhounds-operation-lahat)


