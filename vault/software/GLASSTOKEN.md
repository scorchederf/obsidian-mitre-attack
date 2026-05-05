---
aliases: 
    - S1117
    
mitre-attack: https://attack.mitre.org/software/S1117
---

## S1117

[GLASSTOKEN](https://attack.mitre.org/software/S1117) is a custom web shell used by threat actors during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to execute commands on compromised Ivanti Secure Connect VPNs.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[PowerShell\|T1059.001]] | PowerShell | [GLASSTOKEN](https://attack.mitre.org/software/S1117) can use PowerShell for command execution.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [GLASSTOKEN](https://attack.mitre.org/software/S1117) has the ability to decode hexadecimal and Base64 C2 requests.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [GLASSTOKEN](https://attack.mitre.org/software/S1117) is a web shell capable of tunneling C2 connections and code execution on compromised Ivanti Secure Connect VPNs.[^1]   |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [GLASSTOKEN](https://attack.mitre.org/software/S1117) has hexadecimal and Base64 encoded C2 content.[^1]  |




## References

[^1]: [Volexity Ivanti Zero-Day Exploitation January 2024](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)


