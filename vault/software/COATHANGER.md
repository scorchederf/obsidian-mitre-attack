---
aliases: 
    - S1105
    
mitre-attack: https://attack.mitre.org/software/S1105
---

## S1105

[COATHANGER](https://attack.mitre.org/software/S1105) is a remote access tool (RAT) targeting FortiGate networking appliances. First used in 2023 in targeted intrusions against military and government entities in the Netherlands along with other victims, [COATHANGER](https://attack.mitre.org/software/S1105) was disclosed in early 2024, with a high confidence assessment linking this malware to a state-sponsored entity in the People's Republic of China. [COATHANGER](https://attack.mitre.org/software/S1105) is delivered after gaining access to a FortiGate device, with in-the-wild observations linked to exploitation of CVE-2022-42475. The name [COATHANGER](https://attack.mitre.org/software/S1105) is based on a unique string in the malware used to encrypt configuration files on disk: `“She took his coat and hung it up”`.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [COATHANGER](https://attack.mitre.org/software/S1105) removes files from victim environments following use in multiple instances.[^1]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [COATHANGER](https://attack.mitre.org/software/S1105) uses ICMP for transmitting configuration information to and from its command and control server.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [COATHANGER](https://attack.mitre.org/software/S1105) will query running process information to determine subsequent program execution flow.[^1]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [COATHANGER](https://attack.mitre.org/software/S1105) will create a daemon for timed check-ins with command and control infrastructure.[^1]  |
| [[Process Injection\|T1055]] | Process Injection | [COATHANGER](https://attack.mitre.org/software/S1105) includes a binary labeled `authd` that can inject a library into a running process and then hook an existing function within that process with a new function from that library.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [COATHANGER](https://attack.mitre.org/software/S1105) provides a BusyBox reverse shell for command and control.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | [COATHANGER](https://attack.mitre.org/software/S1105) is installed following exploitation of a vulnerable FortiGate device. [^1]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [COATHANGER](https://attack.mitre.org/software/S1105) will set the GID of `httpsd` to 90 when infected.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [COATHANGER](https://attack.mitre.org/software/S1105) will survey the contents of system files during installation.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [COATHANGER](https://attack.mitre.org/software/S1105) hooks or replaces multiple legitimate processes and other functions on victim devices.[^1]  |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [COATHANGER](https://attack.mitre.org/software/S1105) copies the malicious file `/data2/.bd.key/preload.so` to `/lib/preload.so`, then launches a child process that executes the malicious file `/data2/.bd.key/authd` as `/bin/authd` with the arguments `/lib/preload.so reboot newreboot 1`.[^1]  This injects the malicious preload.so file into the process with PID 1, and replaces its reboot function with the malicious newreboot function for persistence. |
| [[Software Packing\|T1027.002]] | Software Packing | The first stage of [COATHANGER](https://attack.mitre.org/software/S1105) is delivered as a packed file.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [COATHANGER](https://attack.mitre.org/software/S1105) connects to command and control infrastructure using SSL.[^1]  |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | [COATHANGER](https://attack.mitre.org/software/S1105) will remove and write malicious shared objects associated with legitimate system functions such as `read(2)`.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [COATHANGER](https://attack.mitre.org/software/S1105) uses an HTTP GET request to initialize a follow-on TLS tunnel for command and control.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [COATHANGER](https://attack.mitre.org/software/S1105) decodes configuration items from a bundled file for command and control activity.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [COATHANGER](https://attack.mitre.org/software/S1105) creates and installs itself to a hidden installation directory.[^1]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [COATHANGER](https://attack.mitre.org/software/S1105) can store obfuscated configuration information in the last 56 bytes of the file `/date/.bd.key/preload.so`.[^1]  |




## References

[^1]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)


