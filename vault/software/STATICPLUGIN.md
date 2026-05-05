---
aliases: 
    - S1238
    
mitre-attack: https://attack.mitre.org/software/S1238
---

## S1238

[STATICPLUGIN](https://attack.mitre.org/software/S1238) is a downloader known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) has utilized a valid certificate in order to bypass endpoint security protections.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) masqueraded as legitimate software installer by using a custom TForm.  [STATICPLUGIN](https://attack.mitre.org/software/S1238) has been leveraged to deploy a loader that facilitates follow on malware.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Code Signing\|T1553.002]] | Code Signing | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has been signed with a valid Certificate Authority(CA) to circumvent endpoint defenses.[^1]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has masqueraded as a BMP file to hide its true MSI file extension.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has leveraged naming conventions that match legitimate services to include AdobePlugins.exe.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has required user execution to load subsequent malicious payloads.[^1]  |
| [[Component Object Model\|T1559.001]] | Component Object Model | [STATICPLUGIN](https://attack.mitre.org/software/S1238) has utilized Windows COM Installer Object to download an MSI package containing files masqueraded as a BMP file.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


