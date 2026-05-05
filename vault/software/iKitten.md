---
aliases: 
    - S0278
    
mitre-attack: https://attack.mitre.org/software/S0278
---

## S0278

[iKitten](https://attack.mitre.org/software/S0278) is a macOS exfiltration agent  [^3] .

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [iKitten](https://attack.mitre.org/software/S0278) will look for the current IP address.[^3]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [iKitten](https://attack.mitre.org/software/S0278) prompts the user for their credentials.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [iKitten](https://attack.mitre.org/software/S0278) lists the current processes running.[^3]  |
| [[Archive via Utility\|T1560.001]] | Archive via Utility | [iKitten](https://attack.mitre.org/software/S0278) will zip up the /Library/Keychains directory before exfiltrating it.[^3]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [iKitten](https://attack.mitre.org/software/S0278) saves itself with a leading "." so that it's hidden from users by default.[^3]  |
| [[Keychain\|T1555.001]] | Keychain | [iKitten](https://attack.mitre.org/software/S0278) collects the keychains on the system.[^3]  |
| [[RC Scripts\|T1037.004]] | RC Scripts | [iKitten](https://attack.mitre.org/software/S0278) adds an entry to the rc.common file for persistence.[^3]  |




## References

[^1]: OSX/MacDownloader


[^2]: iKitten


[^3]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)


