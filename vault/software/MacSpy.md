---
aliases: 
    - S0282
    
mitre-attack: https://attack.mitre.org/software/S0282
---

## S0282

[MacSpy](https://attack.mitre.org/software/S0282) is a malware-as-a-service offered on the darkweb  [^2] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File Deletion\|T1070.004]] | File Deletion | [MacSpy](https://attack.mitre.org/software/S0282) deletes any temporary files it creates[^1]  |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [MacSpy](https://attack.mitre.org/software/S0282) uses [Tor](https://attack.mitre.org/software/S0183) for command and control.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [MacSpy](https://attack.mitre.org/software/S0282) uses HTTP for command and control.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [MacSpy](https://attack.mitre.org/software/S0282) persists via a Launch Agent.[^2]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [MacSpy](https://attack.mitre.org/software/S0282) can steal clipboard contents.[^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [MacSpy](https://attack.mitre.org/software/S0282) stores itself in `~/Library/.DS_Stores/` [^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [MacSpy](https://attack.mitre.org/software/S0282) can record the sounds from microphones on a computer.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [MacSpy](https://attack.mitre.org/software/S0282) can capture screenshots of the desktop over multiple monitors.[^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [MacSpy](https://attack.mitre.org/software/S0282) captures keystrokes.[^2]  |




## References

[^1]: [alientvault macspy](https://www.alienvault.com/blogs/labs-research/macspy-os-x-rat-as-a-service)


[^2]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


[^3]: MacSpy


