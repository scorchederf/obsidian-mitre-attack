---
aliases: 
    - S9035
    
mitre-attack: https://attack.mitre.org/software/S9035
---

## S9035

[LAMEHUG](https://attack.mitre.org/software/S9035) is Python-based information stealer first identified in July 2025 by Ukraine's Computer Emergency Response Team (CERT-UA) in phishing emails targeting Ukrainian government officials. [LAMEHUG](https://attack.mitre.org/software/S9035) is the first known malware to integrate artificial intelligence (AI) directly into its attack workflow by querying large language models (LLMs) hosted on Hugging Face to dynamically generate reconnaissance, data theft, and system manipulation commands in real time.  [LAMEHUG](https://attack.mitre.org/software/S9035) has been attributed to [APT28](https://attack.mitre.org/groups/G0007). [^1] [^4] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [LAMEHUG](https://attack.mitre.org/software/S9035) can exfiltrate collected system information and documents to C2.[^1] [^4]  |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [LAMEHUG](https://attack.mitre.org/software/S9035) can use wmic to collect system information.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) has the ability to execute Windows commands returned from C2 to gather system information.[^1] [^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [LAMEHUG](https://attack.mitre.org/software/S9035) can use HTTP POST requests to exfiltrate data from compromised hosts to C2.[^1] <br> |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can use `whoami` to enumerate the system user.[^1]  |
| [[Data Encoding\|T1132]] | Data Encoding | [LAMEHUG](https://attack.mitre.org/software/S9035) can encode queries sent to LLMs.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [LAMEHUG](https://attack.mitre.org/software/S9035) payloads have been disguised with legitimate looking filenames including AI_generator_uncensored_Canvas_PRO_v0.9.exe and AI_image_generator_v0.95.exe.[^1] [^4]  |
| [[Domain Account\|T1087.002]] | Domain Account | [LAMEHUG](https://attack.mitre.org/software/S9035) can use [dsquery](https://attack.mitre.org/software/S0105) to enumerate domain user information.[^3]  |
| [[Domain Trust Discovery\|T1482]] | Domain Trust Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can gather Active Directory domain information.[^4]  |
| [[Data from Local System\|T1005]] | Data from Local System | [LAMEHUG](https://attack.mitre.org/software/S9035) has the ability to collect system information and files of interest from compromised systems.[^1] [^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LAMEHUG](https://attack.mitre.org/software/S9035) can decode and drop a decoy file attached to spearphishing emails.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [LAMEHUG](https://attack.mitre.org/software/S9035) can use SSH to transfer information to C2.[^1]  |
| [[Domain Groups\|T1069.002]] | Domain Groups | [LAMEHUG](https://attack.mitre.org/software/S9035) can use [dsquery](https://attack.mitre.org/software/S0105) to gather domain group information.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can enumerate network information on compromised hosts.[^4]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can gather process information on targeted systems.[^4] [^3]  |
| [[Malicious File\|T1204.002]] | Malicious File | [LAMEHUG](https://attack.mitre.org/software/S9035) has been executed through victim interaction with malicious email attachments made to look like legitimate AI applications or documents.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [LAMEHUG](https://attack.mitre.org/software/S9035) can use `cmd.exe` to display a decoy file to spearphishing victims.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [LAMEHUG](https://attack.mitre.org/software/S9035) can recursively copy files from targeted directories on victim hosts.[^1] [^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [LAMEHUG](https://attack.mitre.org/software/S9035) has been distributed through spearphishing emails with various AI-themed malicious attachments.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [LAMEHUG](https://attack.mitre.org/software/S9035) can save collected data and files of interest in `C:\ProgramData\info\` to consolidate for exfiltration.[^1] [^4]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can gather service information on targeted systems.[^4] [^3]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [LAMEHUG](https://attack.mitre.org/software/S9035) has used the Hugging Face API to query the Qwen2.5-Coder-32B-Instruct LLM to generate one-line Windows commands for the collection of system information and documents in specific folders on compromised hosts. [LAMEHUG](https://attack.mitre.org/software/S9035) subsequently executed the returned commands and exfiltrated the collected files and information to adversary-controlled C2 servers.[^4] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LAMEHUG](https://attack.mitre.org/software/S9035) can target directories on victim machines for file collection.[^1] [^4]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [LAMEHUG](https://attack.mitre.org/software/S9035) can xcopy for file collection on targeted systems.[^1]  |
| [[Python\|T1059.006]] | Python | [LAMEHUG](https://attack.mitre.org/software/S9035) can use Python scripts for execution.[^1] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)


[^2]: PROMPTSTEAL


[^3]: [Cato LAMEHUG JUL 2025](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)


[^4]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)


