---
aliases: 
    - S0037
    
mitre-attack: https://attack.mitre.org/software/S0037
---

## S0037

[HAMMERTOSS](https://attack.mitre.org/software/S0037) is a backdoor that was used by [APT29](https://attack.mitre.org/groups/G0016) in 2015. [^2]  [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration to Cloud Storage\|T1567.002]] | Exfiltration to Cloud Storage | [HAMMERTOSS](https://attack.mitre.org/software/S0037) exfiltrates data by uploading it to accounts created by the actors on Web cloud storage providers for the adversaries to retrieve later.[^2]  |
| [[Steganography\|T1001.002]] | Steganography | [HAMMERTOSS](https://attack.mitre.org/software/S0037) is controlled via commands that are appended to image files.[^2]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [HAMMERTOSS](https://attack.mitre.org/software/S0037) has used `-WindowStyle hidden` to conceal [PowerShell](https://attack.mitre.org/techniques/T1059/001) windows.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | Before being appended to image files, [HAMMERTOSS](https://attack.mitre.org/software/S0037) commands are encrypted with a key composed of both a hard-coded value and a string contained on that day's tweet. To decrypt the commands, an investigator would need access to the intended malware sample, the day's tweet, and the image file containing the command.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | The "Uploader" variant of [HAMMERTOSS](https://attack.mitre.org/software/S0037) visits a hard-coded server over HTTP/S to download the images [HAMMERTOSS](https://attack.mitre.org/software/S0037) uses to receive commands.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [HAMMERTOSS](https://attack.mitre.org/software/S0037) is known to use PowerShell.[^2]  |
| [[One-Way Communication\|T1102.003]] | One-Way Communication | The "tDiscoverer" variant of [HAMMERTOSS](https://attack.mitre.org/software/S0037) establishes a C2 channel by downloading resources from Web services like Twitter and GitHub. [HAMMERTOSS](https://attack.mitre.org/software/S0037) binaries contain an algorithm that generates a different Twitter handle for the malware to check for instructions every day.[^2]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [Secureworks IRON HEMLOCK Profile](http://www.secureworks.com/research/threat-profiles/iron-hemlock)


[^2]: [FireEye APT29](https://services.google.com/fh/files/misc/rpt-apt29-hammertoss-stealthy-tactics-define-en.pdf)


[^3]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)


