---
aliases: 
    - S1194
    
mitre-attack: https://attack.mitre.org/software/S1194
---

## S1194

[Akira _v2](https://attack.mitre.org/software/S1194) is a Rust-based variant of [Akira](https://attack.mitre.org/software/S1129) ransomware that has been in use since at least 2024. [Akira _v2](https://attack.mitre.org/software/S1194) is designed to target VMware ESXi servers and includes a new command-line argument set and other expanded capabilities.[^3] [^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | <br>[Akira _v2](https://attack.mitre.org/software/S1194) can create a child process for encryption.[^3]  |
| [[Log Enumeration\|T1654]] | Log Enumeration | [Akira _v2](https://attack.mitre.org/software/S1194) can enumerate the trace, debug, error, info, and warning logs on targeted systems.[^2] [^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | The [Akira _v2](https://attack.mitre.org/software/S1194) encryptor targets the `/vmfs/volumes/` path by default and can use the rust-crypto 0.2.36 library crate for the encryption processes.[^2] [^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Akira _v2](https://attack.mitre.org/software/S1194) can target specific files and folders for encryption.[^3] [^2] [^1]  |
| [[Service Stop\|T1489]] | Service Stop | [Akira _v2](https://attack.mitre.org/software/S1194) can stop running virtual machines.[^3] [^2] [^1]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Akira _v2](https://attack.mitre.org/software/S1194) will fail to execute if the targeted `/vmfs/volumes/` path does not exist or is not defined.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Akira\|G1024]] | Akira |



## References

[^1]: [Palo Alto Howling Scorpius DEC 2024](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)


[^2]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^3]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


