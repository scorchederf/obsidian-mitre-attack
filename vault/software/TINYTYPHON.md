---
aliases: 
    - S0131
    
mitre-attack: https://attack.mitre.org/software/S0131
---

## S0131

[TINYTYPHON](https://attack.mitre.org/software/S0131) is a backdoor  that has been used by the actors responsible for the MONSOON campaign. The majority of its code was reportedly taken from the MyDoom worm. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [TINYTYPHON](https://attack.mitre.org/software/S0131) has used XOR with 0x90 to obfuscate its configuration file.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TINYTYPHON](https://attack.mitre.org/software/S0131) searches through the drive containing the OS, then all drive letters C through to Z, for documents matching certain extensions.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TINYTYPHON](https://attack.mitre.org/software/S0131) installs itself under Registry Run key to establish persistence.[^1]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | When a document is found matching one of the extensions in the configuration, [TINYTYPHON](https://attack.mitre.org/software/S0131) uploads it to the C2 server.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Patchwork\|G0040]] | Patchwork |



## References

[^1]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)


