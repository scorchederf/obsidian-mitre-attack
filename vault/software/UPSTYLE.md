---
aliases: 
    - S1164
    
mitre-attack: https://attack.mitre.org/software/S1164
---

## S1164

[UPSTYLE](https://attack.mitre.org/software/S1164) is a Python-based backdoor associated with exploitation of Palo Alto firewalls using CVE-2024-3400 in early 2024. [UPSTYLE](https://attack.mitre.org/software/S1164) has only been observed in relation to this exploitation activity, which involved attempted install on compromised devices by the threat actor UTA0218.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [UPSTYLE](https://attack.mitre.org/software/S1164) encodes its main content prior to loading via Python as base64-encoded blobs.[^1] [^2]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [UPSTYLE](https://attack.mitre.org/software/S1164) clears error logs after reading embedded commands for execution.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [UPSTYLE](https://attack.mitre.org/software/S1164) stores primary content as base64-encoded objects.[^1] [^2]  |
| [[Masquerading\|T1036]] | Masquerading | [UPSTYLE](https://attack.mitre.org/software/S1164) has masqueraded filenames using examples such as `update.py`.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [UPSTYLE](https://attack.mitre.org/software/S1164) removes `bootstrap.min.css` after parsing command and control instructions, restoring the file to its original state.[^1]   |
| [[Junk Data\|T1001.001]] | Junk Data | [UPSTYLE](https://attack.mitre.org/software/S1164) retrieves a non-existent webpage from the command and control server then parses commands from the resulting error logs to decode commands to the web shell.[^1]  |
| [[Timestomp\|T1070.006]] | Timestomp | [UPSTYLE](https://attack.mitre.org/software/S1164) restores timestamps to original values following modification.[^1]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | [UPSTYLE](https://attack.mitre.org/software/S1164) parses encoded commands from error logs after attempting to resolve a non-existing webpage from the command and control server.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [UPSTYLE](https://attack.mitre.org/software/S1164) has the ability to read `/proc/self/cmdline` to see if it is running as a monitored process.[^2]  |
| [[Event Triggered Execution\|T1546]] | Event Triggered Execution | [UPSTYLE](https://attack.mitre.org/software/S1164) creates a `.pth` file beginning with the text `import` so that any time another process or script attempts to reference the modified item the malicious code will also run.[^1]  |
| [[Python\|T1059.006]] | Python | [UPSTYLE](https://attack.mitre.org/software/S1164) is a Python-based application.[^1] [^2]  |
| [[Hide Infrastructure\|T1665]] | Hide Infrastructure | [UPSTYLE](https://attack.mitre.org/software/S1164) attempts to retrieve a non-existent webpage from the command and control server resulting in hidden commands sent via resulting error messages.[^1]  |




## References

[^1]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)


[^2]: [Palo Alto MidnightEclipse APR 2024](https://unit42.paloaltonetworks.com/cve-2024-3400/)


