---
aliases: 
    - S0338
    
mitre-attack: https://attack.mitre.org/software/S0338
---

## S0338

[Cobian RAT](https://attack.mitre.org/software/S0338) is a backdoor, remote access tool that has been observed since 2016.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [Cobian RAT](https://attack.mitre.org/software/S0338) has a feature to perform screen capture.[^1]  |
| [[Video Capture\|T1125]] | Video Capture | [Cobian RAT](https://attack.mitre.org/software/S0338) has a feature to access the webcam on the victim’s machine.[^1]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Cobian RAT](https://attack.mitre.org/software/S0338) creates an autostart Registry key to ensure persistence.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Cobian RAT](https://attack.mitre.org/software/S0338) can launch a remote command shell interface for executing commands.[^1]  |
| [[Keylogging\|T1056.001]] | Keylogging | [Cobian RAT](https://attack.mitre.org/software/S0338) has a feature to perform keylogging on the victim’s machine.[^1]  |
| [[DNS\|T1071.004]] | DNS | [Cobian RAT](https://attack.mitre.org/software/S0338) uses DNS for C2.[^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [Cobian RAT](https://attack.mitre.org/software/S0338) has a feature to perform voice recording on the victim’s machine.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Cobian RAT](https://attack.mitre.org/software/S0338) obfuscates communications with the C2 server using Base64 encoding.[^1]  |




## References

[^1]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)


[^2]: Cobian RAT


