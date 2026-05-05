---
aliases: 
    - S0454
    
mitre-attack: https://attack.mitre.org/software/S0454
---

## S0454

[Cadelspy](https://attack.mitre.org/software/S0454) is a backdoor that has been used by [APT39](https://attack.mitre.org/groups/G0087).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to identify open windows on the compromised host.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to log keystrokes on the compromised host.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to compress stolen data into a .cab file.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to steal data from the clipboard.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to record audio from the compromised host.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to discover information about the compromised host.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to capture screenshots and webcam photos.[^1]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Cadelspy](https://attack.mitre.org/software/S0454) has the ability to steal information about printers and the documents sent to printers.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT39\|G0087]] | APT39 |



## References

[^1]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)


