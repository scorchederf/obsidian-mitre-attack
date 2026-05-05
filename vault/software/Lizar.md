---
aliases: 
    - S0681
    
mitre-attack: https://attack.mitre.org/software/S0681
---

## S0681

[Lizar](https://attack.mitre.org/software/S0681) is a modular remote access tool written using the .NET Framework that shares structural similarities to [Carbanak](https://attack.mitre.org/software/S0030). It has likely been used by [FIN7](https://attack.mitre.org/groups/G0046) since at least February 2021.[^3] [^7] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Injection\|T1055]] | Process Injection | [Lizar](https://attack.mitre.org/software/S0681) can migrate the loader into another process.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Lizar](https://attack.mitre.org/software/S0681) has a command to open the command-line on the infected system.[^7] [^3]  |
| [[Browser Information Discovery\|T1217]] | Browser Information Discovery | [Lizar](https://attack.mitre.org/software/S0681) can retrieve browser history and database files.[^7] [^3]   |
| [[Python\|T1059.006]] | Python | [Lizar](https://attack.mitre.org/software/S0681) has used Python scripts (ps2x.py script and ps2p.py) to execute files on remote hosts using the [Impacket](https://attack.mitre.org/software/S0357) library.[^3]   |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | [Lizar](https://attack.mitre.org/software/S0681) has used the PowerKatz plugin that can be loaded into the address space of a PowerShell process through reflective DLL loading.[^3]   |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [Lizar](https://attack.mitre.org/software/S0681) has used a raw TCP connection to communicate with the C2 server.[^9]     |
| [[Native API\|T1106]] | Native API | [Lizar](https://attack.mitre.org/software/S0681) has used various Windows API functions on a victim's machine.[^3]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Lizar](https://attack.mitre.org/software/S0681) has obfuscated the fingerprint of the victim system, the local IP address, and the Fowler-Noll-V 1 (FNV-1) hash of the local IP address using an XOR operation. The data is then sent to the C2 server.[^9]   |
| [[LSASS Memory\|T1003.001]] | LSASS Memory | [Lizar](https://attack.mitre.org/software/S0681) can run [Mimikatz](https://attack.mitre.org/software/S0002) to harvest credentials.[^7] [^3]  |
| [[Windows Credential Manager\|T1555.004]] | Windows Credential Manager | [Lizar](https://attack.mitre.org/software/S0681) has a plugin that can retrieve credentials from Internet Explorer and Microsoft Edge using `vaultcmd.exe` and another that can collect RDP access credentials using the `CredEnumerateW` function.[^3]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Lizar](https://attack.mitre.org/software/S0681) can take JPEG screenshots of an infected system.[^7] [^3]  [Lizar](https://attack.mitre.org/software/S0681) has also used a plugin to take a screenshot of the infected system.[^3]   |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Lizar](https://attack.mitre.org/software/S0681) can collect the username from the system.[^3] [^9]   |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Lizar](https://attack.mitre.org/software/S0681) has decrypted its configuration data, such as the C2 IP address, ports and other network communication.[^3] [^9]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Lizar](https://attack.mitre.org/software/S0681) has used PowerShell scripts.[^3]  |
| [[Portable Executable Injection\|T1055.002]] | Portable Executable Injection | [Lizar](https://attack.mitre.org/software/S0681) can execute PE files in the address space of the specified process.[^3]   |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Lizar](https://attack.mitre.org/software/S0681) can download additional plugins, files, and tools.[^3] [^9] [^4]  |
| [[Email Account\|T1087.003]] | Email Account | [Lizar](https://attack.mitre.org/software/S0681) can collect email accounts from Microsoft Outlook and Mozilla Thunderbird.[^3]   |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Lizar](https://attack.mitre.org/software/S0681) can collect the computer name from the machine.[^3] [^9]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [Lizar](https://attack.mitre.org/software/S0681) can search for processes associated with an anti-virus product from list.[^3]   |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Lizar](https://attack.mitre.org/software/S0681) has a module to collect usernames and passwords stored in browsers.[^3]  |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | [Lizar](https://attack.mitre.org/software/S0681) can support encrypted communications between the client and server.[^7] [^3] [^4]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Lizar](https://attack.mitre.org/software/S0681) has used the Reflective DLL injection module from Github to inject itself into a process’s memory.[^9]   |
| [[Tool\|T1588.002]] | Tool | [FIN7](https://attack.mitre.org/groups/G0046) has obtained and used tools such as [Impacket](https://attack.mitre.org/software/S0357), [Mimikatz](https://attack.mitre.org/software/S0002), and [PsExec](https://attack.mitre.org/software/S0029).[^3]   |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Lizar](https://attack.mitre.org/software/S0681) has retrieved network information from a compromised host, such as the MAC address.[^3] [^9]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Lizar](https://attack.mitre.org/software/S0681) has a plugin designed to obtain a list of processes.[^7] [^3]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Lizar](https://attack.mitre.org/software/S0681) has used a complex XOR operation to obfuscate C2 communications.[^9]   |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Lizar](https://attack.mitre.org/software/S0681) has encrypted data before sending it to the server.[^3]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [Lizar](https://attack.mitre.org/software/S0681) has a plugin to retrieve information about all active network sessions on the infected server.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[FIN7\|G0046]] | FIN7 |



## References

[^1]: [Gemini FIN7 Oct 2021](https://geminiadvisory.io/fin7-ransomware-bastion-secure/)


[^2]: DiceLoader


[^3]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)


[^4]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)


[^5]: Tirion


[^6]: Lizar


[^7]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)


[^8]: Icebot


[^9]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)


