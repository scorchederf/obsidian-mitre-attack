---
aliases: 
    - S1120
    
mitre-attack: https://attack.mitre.org/software/S1120
---

## S1120

[FRAMESTING](https://attack.mitre.org/software/S1120) is a Python web shell that was used during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to embed into an Ivanti Connect Secure Python package for command execution.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Protocol or Service Impersonation\|T1001.003]] | Protocol or Service Impersonation | [FRAMESTING](https://attack.mitre.org/software/S1120) uses a cookie named `DSID` to mimic the name of a cookie used by Ivanti Connect Secure appliances for maintaining VPN sessions.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FRAMESTING](https://attack.mitre.org/software/S1120) can retrieve C2 commands from values stored in the `DSID` cookie from the current HTTP request or from decompressed zlib data within the request's `POST` data.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [FRAMESTING](https://attack.mitre.org/software/S1120) is a web shell capable of enabling arbitrary command execution on compromised Ivanti Connect Secure VPNs.[^1]  |
| [[Python\|T1059.006]] | Python | [FRAMESTING](https://attack.mitre.org/software/S1120) is a Python web shell that can embed in the Ivanti Connect Secure CAV Python package.[^1]  |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [FRAMESTING](https://attack.mitre.org/software/S1120) can send and receive zlib compressed data within `POST` requests.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FRAMESTING](https://attack.mitre.org/software/S1120) can decompress data received within `POST` requests.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [FRAMESTING](https://attack.mitre.org/software/S1120) can embed itself in the CAV Python package of an Ivanti Connect Secure VPN located in `/home/venv3/lib/python3.6/site-packages/cav-0.1-py3.6.egg/cav/api/resources/category.py.`[^1]  |




## References

[^1]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)


