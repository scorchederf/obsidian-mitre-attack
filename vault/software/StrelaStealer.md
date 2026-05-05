---
aliases: 
    - S1183
    
mitre-attack: https://attack.mitre.org/software/S1183
---

## S1183

[StrelaStealer](https://attack.mitre.org/software/S1183) is an information stealer malware variant first identified in November 2022 and active through late 2024. [StrelaStealer](https://attack.mitre.org/software/S1183) focuses on the automated identification, collection, and exfiltration of email credentials from email clients such as Outlook and Thunderbird.[^1] [^2] [^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [StrelaStealer](https://attack.mitre.org/software/S1183) encrypts the payload of HTTP POST communications using the same XOR key used for the malware's DLL payload.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [StrelaStealer](https://attack.mitre.org/software/S1183) exfiltrates collected email credentials via HTTP POST to command and control servers.[^1] [^2] [^4] [^3]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [StrelaStealer](https://attack.mitre.org/software/S1183) variants have included excessive mathematical functions padding the binary and slowing execution for anti-analysis and sandbox evasion purposes.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [StrelaStealer](https://attack.mitre.org/software/S1183) communicates externally via HTTP POST with encrypted content.[^1] [^4] [^3]  |
| [[Debugger Evasion\|T1622]] | Debugger Evasion | [StrelaStealer](https://attack.mitre.org/software/S1183) variants include functionality to identify and evade debuggers.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [StrelaStealer](https://attack.mitre.org/software/S1183) has been distributed in ISO archives.[^1]  [StrelaStealer](https://attack.mitre.org/software/S1183) has been delivered in encrypted, password-protected ZIP archives.[^3]  |
| [[Code Signing\|T1553.002]] | Code Signing | [StrelaStealer](https://attack.mitre.org/software/S1183) variants have used valid code signing certificates.[^3]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [StrelaStealer](https://attack.mitre.org/software/S1183) variants only execute if the keyboard layout or language matches a set list of variables.[^4] [^3]  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | [StrelaStealer](https://attack.mitre.org/software/S1183) has used a renamed, legitimate `msinfo32.exe` executable to sideload the [StrelaStealer](https://attack.mitre.org/software/S1183) payload during initial installation.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [StrelaStealer](https://attack.mitre.org/software/S1183) relies on user execution of a malicious file for installation.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [StrelaStealer](https://attack.mitre.org/software/S1183) uses XOR-encoded strings to obfuscate items.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [StrelaStealer](https://attack.mitre.org/software/S1183) has been distributed as a malicious JavaScript object.[^2] [^4] [^3]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [StrelaStealer](https://attack.mitre.org/software/S1183) DLL payloads have been executed via `rundll32.exe`.[^2] [^3]  |
| [[Software Discovery\|T1518]] | Software Discovery | [StrelaStealer](https://attack.mitre.org/software/S1183) variants use COM objects to enumerate installed applications from the "AppsFolder" on victim machines.[^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [StrelaStealer](https://attack.mitre.org/software/S1183) variants have used packers to obfuscate payloads and make analysis more difficult.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [StrelaStealer](https://attack.mitre.org/software/S1183) variants have used PowerShell scripts to download or drop payloads, including obfuscated variants to connect to a WebDAV server to download and executed an encrypted DLL for installation.[^3]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [StrelaStealer](https://attack.mitre.org/software/S1183) has included BAT files in some instances for installation.[^4] [^3]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [StrelaStealer](https://attack.mitre.org/software/S1183) payloads have used control flow obfuscation techniques such as excessively long code blocks of mathematical instructions to defeat sandboxing and related analysis methods.[^2] [^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [StrelaStealer](https://attack.mitre.org/software/S1183) has been distributed as a spearphishing attachment.[^1]  |
| [[Compression\|T1027.015]] | Compression | [StrelaStealer](https://attack.mitre.org/software/S1183) has been delivered via JScript files in a ZIP archive.[^2] [^4]   |
| [[Credentials in Registry\|T1552.002]] | Credentials in Registry | [StrelaStealer](https://attack.mitre.org/software/S1183) enumerates the registry key `HKCU\SOFTWARE\Microsoft\Office\16.0\Outlook\Profiles\Outlook\9375CFF0413111d3B88A00104B2A6676\` to identify the values for "IMAP User," "IMAP Server," and "IMAP Password" associated with the Outlook email application.[^1] [^4] [^3]  |
| [[Masquerading\|T1036]] | Masquerading | [StrelaStealer](https://attack.mitre.org/software/S1183) PE executable payloads have used uncommon but legitimate extensions such as `.com` instead of `.exe`.[^3]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [StrelaStealer](https://attack.mitre.org/software/S1183) utilizes a hard-coded XOR key to encrypt the content of HTTP POST requests to command and control infrastructure.[^3]  |
| [[DLL\|T1574.001]] | DLL | [StrelaStealer](https://attack.mitre.org/software/S1183) has sideloaded a DLL payload using a renamed, legitimate `msinfo32.exe` executable.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [StrelaStealer](https://attack.mitre.org/software/S1183) payloads have tailored filenames to include names identical to the name of the targeted organization or company.[^3]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [StrelaStealer](https://attack.mitre.org/software/S1183) variants check system language settings via keyboard layout or similar mechanisms.[^4] [^3]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [StrelaStealer](https://attack.mitre.org/software/S1183) payloads have included strings encrypted via XOR.[^1]  [StrelaStealer](https://attack.mitre.org/software/S1183) JavaScript payloads utilize Base64-encoded payloads that are decoded via [certutil](https://attack.mitre.org/software/S0160) to create a malicious DLL file.[^2] [^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [StrelaStealer](https://attack.mitre.org/software/S1183) installers have used obfuscated PowerShell scripts to retrieve follow-on payloads from WebDAV servers.[^3]  |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | [StrelaStealer](https://attack.mitre.org/software/S1183) variants include the use of mutex values based on the victim system name to prevent reinfection.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [StrelaStealer](https://attack.mitre.org/software/S1183) variants collect victim system information for exfiltration.[^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [StrelaStealer](https://attack.mitre.org/software/S1183) searches for and if found collects the contents of files such as `logins.json` and `key4.db` in the `$APPDATA%\Thunderbird\Profiles\` directory, associated with the Thunderbird email application.[^1] [^4]  |
| [[Automated Collection\|T1119]] | Automated Collection | [StrelaStealer](https://attack.mitre.org/software/S1183) attempts to identify and collect mail login data from Thunderbird and Outlook following execution.[^1] [^2] [^4] [^3]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [StrelaStealer](https://attack.mitre.org/software/S1183) has been distributed as a DLL/HTML polyglot file.[^1] [^3]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | [StrelaStealer](https://attack.mitre.org/software/S1183) automatically sends gathered email credentials following collection to command and control servers via HTTP POST.[^1] [^3]  |




## References

[^1]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)


[^2]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)


[^3]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)


[^4]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)


