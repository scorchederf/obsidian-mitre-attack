---
aliases: 
    - S1130
    
mitre-attack: https://attack.mitre.org/software/S1130
---

## S1130

[Raspberry Robin](https://attack.mitre.org/software/S1130) is initial access malware first identified in September 2021, and active through early 2024. The malware is notable for spreading via infected USB devices containing a malicious LNK object that, on execution, retrieves remote hosted payloads for installation. [Raspberry Robin](https://attack.mitre.org/software/S1130) has been widely used against various industries and geographies, and as a precursor to information stealer, ransomware, and other payloads such as [SocGholish](https://attack.mitre.org/software/S1124), [Cobalt Strike](https://attack.mitre.org/software/S0154), [IcedID](https://attack.mitre.org/software/S0483), and [Bumblebee](https://attack.mitre.org/software/S1039).[^1] [^5] [^3]  The DLL componenet in the [Raspberry Robin](https://attack.mitre.org/software/S1130) infection chain is also referred to as "Roshtyak."[^2]  The name "Raspberry Robin" is used to refer to both the malware as well as the threat actor associated with its use, although the Raspberry Robin operators are also tracked as `Storm-0856` by some vendors.[^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Raspberry Robin](https://attack.mitre.org/software/S1130) attempts to identify security software running on the victim machine, such as BitDefender, Avast, and Kaspersky.[^1] [^3]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Raspberry Robin](https://attack.mitre.org/software/S1130) can add an exception to Microsoft Defender that excludes the entire main drive from anti-malware scanning to evade detection.[^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Raspberry Robin](https://attack.mitre.org/software/S1130) performs several system checks as part of anti-analysis mechanisms, including querying the operating system build number, processor vendor and type, video controller, and CPU temperature.[^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Raspberry Robin](https://attack.mitre.org/software/S1130) contains multiple payloads that are packed for defense evasion purposes and unpacked on runtime.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Raspberry Robin](https://attack.mitre.org/software/S1130) second stage payloads can be hosted as RAR files, containing a malicious EXE and DLL, on Discord servers.[^3]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Raspberry Robin](https://attack.mitre.org/software/S1130) will check for the presence of several security products on victim machines and will avoid UAC bypass mechanisms if they are identified.[^1]  [Raspberry Robin](https://attack.mitre.org/software/S1130) can use specific cookie values in HTTP requests to command and control infrastructure to validate that requests for second stage payloads originate from the initial downloader script.[^3]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Raspberry Robin](https://attack.mitre.org/software/S1130) will use a Registry key to achieve persistence through reboot, setting a RunOnce key such as: `HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce<br>{random value name} = “rundll32 shell32 ShellExec_RunDLLA REGSVR /u /s “{dropped copy path and file name}””<br>`.[^1]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | [Raspberry Robin](https://attack.mitre.org/software/S1130) contains an embedded custom [Tor](https://attack.mitre.org/software/S0183) network client that communicates with the primary payload via shared process memory.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [Raspberry Robin](https://attack.mitre.org/software/S1130) will communicate via HTTP over port 8080 for command and control traffic.[^5]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Raspberry Robin](https://attack.mitre.org/software/S1130) contains real and fake second-stage payloads following initial execution, with the real payload only delivered if the malware determines it is not running in a virtualized environment.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Raspberry Robin](https://attack.mitre.org/software/S1130) will execute its payload prior to initializing command and control traffic by impersonating one of several legitimate program names such as dllhost.exe, regsvr32.exe, or rundll32.exe.[^1]  |
| [[Regsvr32\|T1218.010]] | Regsvr32 | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses regsvr32.exe execution without any command line parameters for command and control requests to IP addresses associated with [Tor](https://attack.mitre.org/software/S0183) nodes.[^5]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Raspberry Robin](https://attack.mitre.org/software/S1130) determines whether it is successfully running on a victim system by querying the running account information to determine if it is running in Session 0, indicating running with elevated privileges.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Raspberry Robin](https://attack.mitre.org/software/S1130) retrieves its second stage payload in a variety of ways such as through msiexec.exe abuse, or running the curl command to download the payload to the victim's `%AppData%` folder.[^3] [^5]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [Raspberry Robin](https://attack.mitre.org/software/S1130) will drop a copy of itself to a subfolder in `%Program Data%` or `%Program Data%\\Microsoft\\` to attempt privilege elevation and defense evasion if not running in Session 0.[^1]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [Raspberry Robin](https://attack.mitre.org/software/S1130) has historically been delivered via infected USB drives containing a malicious LNK object masquerading as a legitimate folder.[^5]  |
| [[Replication Through Removable Media\|T1091]] | Replication Through Removable Media | [Raspberry Robin](https://attack.mitre.org/software/S1130) has historically used infected USB media to spread to new victims.[^1] [^5]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses outbound HTTP requests containing victim information for retrieving second stage payloads.[^5]  Variants of [Raspberry Robin](https://attack.mitre.org/software/S1130) can download archive files (such as 7-Zip files) via the victim web browser for second stage execution.[^3]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [Raspberry Robin](https://attack.mitre.org/software/S1130) will execute a legitimate process, then suspend it to inject code for a [Tor](https://attack.mitre.org/software/S0183) client into the process, followed by resumption of the process to enable [Tor](https://attack.mitre.org/software/S0183) client execution.[^1]  |
| [[Domains\|T1583.001]] | Domains | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses newly-registered domains containing only a few characters for command and controll purposes, such as "`v0[.]cx`".[^5]  |
| [[DLL\|T1574.001]] | DLL | [Raspberry Robin](https://attack.mitre.org/software/S1130) can use legitimate, signed EXE files paired with malicious DLL files to load and run malicious payloads while bypassing defenses.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Raspberry Robin](https://attack.mitre.org/software/S1130) can identify processes running on the victim machine, such as security software, during execution.[^1] [^3]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Raspberry Robin](https://attack.mitre.org/software/S1130) can execute via LNK containing a command to run a legitimate executable, such as wmic.exe, to download a malicious Windows Installer (MSI) package.[^1]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [Raspberry Robin](https://attack.mitre.org/software/S1130) creates an elevated COM object for `CMLuaUtil` and uses this to set a registry value that points to the malicious LNK file during execution.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Raspberry Robin](https://attack.mitre.org/software/S1130) will check to see if the initial executing script is located on the user's Desktop as an anti-analysis check.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses cmd.exe to read and execute a file stored on an infected USB device as part of initial installation.[^5]  |
| [[Odbcconf\|T1218.008]] | Odbcconf | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses the Windows utility odbcconf.exe to execute malicious commands, using the `regsvr` flag to execute DLLs and bypass application control mechanisms that are not monitoring for odbcconf.exe abuse.[^5]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses rundll32 execution without any command line parameters to contact command and control infrastructure, such as IP addresses associated with [Tor](https://attack.mitre.org/software/S0183) nodes.[^5]  |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | [Raspberry Robin](https://attack.mitre.org/software/S1130) implements a variation of the `ucmDccwCOMMethod` technique abusing the Windows AutoElevate backdoor to bypass UAC while elevating privileges.[^1]  |
| [[User Execution\|T1204]] | User Execution | [Raspberry Robin](https://attack.mitre.org/software/S1130) execution can rely on users directly interacting with malicious LNK files.[^4]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [Raspberry Robin](https://attack.mitre.org/software/S1130) leverages anti-debugging mechanisms through the use of `ThreadHideFromDebugger`.[^1]  |
| [[Malvertising\|T1583.008]] | Malvertising | [Raspberry Robin](https://attack.mitre.org/software/S1130) variants have been delivered via malicious advertising items that, when interacted with, download a malicious archive file containing the initial payload, hosted on services such as Discord.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Raspberry Robin](https://attack.mitre.org/software/S1130) can delete its initial delivery script from disk during execution.[^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Raspberry Robin](https://attack.mitre.org/software/S1130) contains several layers of obfuscation to hide malicious code from detection and analysis.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [Raspberry Robin](https://attack.mitre.org/software/S1130) performs a variety of system environment checks to determine if it is running in a virtualized or sandboxed environment, such as querying CPU temperature information and network card MAC address information.[^3]  |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses a `RunOnce` Registry key for persistence, where the key is removed after its use on reboot then re-added by the malware after it resumes execution.[^4]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Raspberry Robin](https://attack.mitre.org/software/S1130) is capable of contacting the TOR network for delivering second-stage payloads.[^5] [^1] [^3]  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | [Raspberry Robin](https://attack.mitre.org/software/S1130) will use the legitimate Windows utility fodhelper.exe to run processes at elevated privileges without requiring a User Account Control prompt.[^5]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses mixed-case letters for filenames and commands to evade detection.[^5]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Raspberry Robin](https://attack.mitre.org/software/S1130) uses msiexec.exe for post-installation communication to command and control infrastructure.[^5]  Msiexec.exe is executed referencing a remote resource for second-stage payload retrieval and execution.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Raspberry Robin](https://attack.mitre.org/software/S1130) variants can be delivered via highly obfuscated Windows Script Files (WSF) for initial execution.[^3]  |




## References

[^1]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)


[^2]: [Avast RaspberryRobin 2022](https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/)


[^3]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)


[^4]: [Microsoft RaspberryRobin 2022](https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)


[^5]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)


