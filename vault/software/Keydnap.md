---
aliases: 
    - S0276
    
mitre-attack: https://attack.mitre.org/software/S0276
---

## S0276

This piece of malware steals the content of the user's keychain while maintaining a permanent backdoor  [^1] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Multi-hop Proxy\|T1090.003]] | Multi-hop Proxy | [Keydnap](https://attack.mitre.org/software/S0276) uses a copy of tor2web proxy for HTTPS communications.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Keydnap](https://attack.mitre.org/software/S0276) uses HTTPS for command and control.[^3]  |
| [[Securityd Memory\|T1555.002]] | Securityd Memory | [Keydnap](https://attack.mitre.org/software/S0276) uses the keychaindump project to read securityd memory.[^3]  |
| [[Resource Forking\|T1564.009]] | Resource Forking | [Keydnap](https://attack.mitre.org/software/S0276) uses a resource fork to present a macOS JPEG or text file icon rather than the executable's icon assigned by the operating system.[^1]  |
| [[Setuid and Setgid\|T1548.001]] | Setuid and Setgid | [Keydnap](https://attack.mitre.org/software/S0276) adds the setuid flag to a binary so it can easily elevate in the future.[^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Keydnap](https://attack.mitre.org/software/S0276) prompts the users for credentials.[^3]  |
| [[Space after Filename\|T1036.006]] | Space after Filename | [Keydnap](https://attack.mitre.org/software/S0276) puts a space after a false .jpg extension so that execution actually goes through the Terminal.app program.[^3]  |
| [[Python\|T1059.006]] | Python | [Keydnap](https://attack.mitre.org/software/S0276) uses Python for scripting to execute additional commands.[^3]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Keydnap](https://attack.mitre.org/software/S0276) uses a Launch Agent to persist.[^3]  |




## References

[^1]: [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)


[^2]: OSX/Keydnap


[^3]: [synack 2016 review](https://objective-see.org/blog/blog_0x16.html)


[^4]: Keydnap


