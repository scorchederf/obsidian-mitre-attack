---
aliases: 
    - S0391
    
mitre-attack: https://attack.mitre.org/software/S0391
---

## S0391

[HAWKBALL](https://attack.mitre.org/software/S0391) is a backdoor that was observed in targeting of the government sector in Central Asia.[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic Data Exchange\|T1559.002]] | Dynamic Data Exchange | [HAWKBALL](https://attack.mitre.org/software/S0391) has used an OLE object that uses Equation Editor to drop the embedded shellcode.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [HAWKBALL](https://attack.mitre.org/software/S0391) has encrypted the payload with an XOR-based algorithm.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [HAWKBALL](https://attack.mitre.org/software/S0391) can collect the OS version, architecture information, and computer name.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HAWKBALL](https://attack.mitre.org/software/S0391) has used HTTP to communicate with a single hard-coded C2 server.[^2]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [HAWKBALL](https://attack.mitre.org/software/S0391) can collect the user name of the system.[^2]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [HAWKBALL](https://attack.mitre.org/software/S0391) has sent system information and files over the C2 channel.[^2]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [HAWKBALL](https://attack.mitre.org/software/S0391) has encrypted data with XOR before sending it over the C2 channel.[^2]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [HAWKBALL](https://attack.mitre.org/software/S0391) has exploited Microsoft Office vulnerabilities CVE-2017-11882 and CVE-2018-0802 to deliver the payload.[^2]   |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HAWKBALL](https://attack.mitre.org/software/S0391) has created a cmd.exe reverse shell, executed commands, and uploaded output via the command line.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HAWKBALL](https://attack.mitre.org/software/S0391) has the ability to delete files.[^2] 	 |
| [[Native API\|T1106]] | Native API | [HAWKBALL](https://attack.mitre.org/software/S0391) has leveraged several Windows API calls to create processes, gather disk information, and detect debugger activity.[^2]  |




## References

[^1]: HAWKBALL


[^2]: [FireEye HAWKBALL Jun 2019](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)


