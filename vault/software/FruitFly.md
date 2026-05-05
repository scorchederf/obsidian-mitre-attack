---
aliases: 
    - S0277
    
mitre-attack: https://attack.mitre.org/software/S0277
---

## S0277

FruitFly is designed to spy on mac users  [^1] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [FruitFly](https://attack.mitre.org/software/S0277) has the ability to list processes on the system.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [FruitFly](https://attack.mitre.org/software/S0277) will delete files on the system.[^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [FruitFly](https://attack.mitre.org/software/S0277) takes screenshots of the user's desktop.[^1]  |
| [[Command Obfuscation\|T1027.010]] | Command Obfuscation | [FruitFly](https://attack.mitre.org/software/S0277) executes and stores obfuscated Perl scripts.[^1]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [FruitFly](https://attack.mitre.org/software/S0277) saves itself with a leading "." to make it a hidden file.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FruitFly](https://attack.mitre.org/software/S0277) looks for specific files and file types.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [FruitFly](https://attack.mitre.org/software/S0277) persists via a Launch Agent.[^1]  |




## References

[^1]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^2]: FruitFly


