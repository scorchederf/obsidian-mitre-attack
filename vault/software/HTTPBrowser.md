---
aliases: 
    - S0070
    
mitre-attack: https://attack.mitre.org/software/S0070
---

## S0070

[HTTPBrowser](https://attack.mitre.org/software/S0070) is malware that has been used by several threat groups. [^4]  [^2]  It is believed to be of Chinese origin. [^9] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of writing a file to the compromised system from the C2 server.[^2]  |
| [[DLL\|T1574.001]] | DLL | [HTTPBrowser](https://attack.mitre.org/software/S0070) abuses the Windows DLL load order by using a legitimate Symantec anti-virus binary, VPDN_LU.exe, to load a malicious DLL that mimics a legitimate Symantec DLL, navlu.dll.[^3]  [HTTPBrowser](https://attack.mitre.org/software/S0070) has also used DLL side-loading.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [HTTPBrowser](https://attack.mitre.org/software/S0070) has established persistence by setting the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` key value for `wdm` to the path of the executable. It has also used the Registry entry `HKEY_USERS\Software\Microsoft\Windows\CurrentVersion\Run vpdn “%ALLUSERPROFILE%\%APPDATA%\vpdn\VPDN_LU.exe”` to establish persistence.[^3] [^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [HTTPBrowser](https://attack.mitre.org/software/S0070)'s code may be obfuscated through structured exception handling and return-oriented programming.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of spawning a reverse shell on a victim.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [HTTPBrowser](https://attack.mitre.org/software/S0070)'s installer contains a malicious file named navlu.dll to decrypt and run the RAT. navlu.dll is also the name of a legitimate Symantec DLL.[^3]  |
| [[DNS\|T1071.004]] | DNS | [HTTPBrowser](https://attack.mitre.org/software/S0070) has used DNS for command and control.[^2] [^4]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of listing files, folders, and drives on a victim.[^2] [^3]  |
| [[Keylogging\|T1056.001]] | Keylogging | [HTTPBrowser](https://attack.mitre.org/software/S0070) is capable of capturing keystrokes on victims.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [HTTPBrowser](https://attack.mitre.org/software/S0070) has used HTTP and HTTPS for command and control.[^2] [^4]  |
| [[File Deletion\|T1070.004]] | File Deletion | [HTTPBrowser](https://attack.mitre.org/software/S0070) deletes its original installer file once installation is complete.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Threat Group-3390\|G0027]] | Threat Group-3390 |
| [[APT18\|G0026]] | APT18 |



## References

[^1]: HttpDump


[^2]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)


[^3]: [ZScaler Hacking Team](http://research.zscaler.com/2015/08/chinese-cyber-espionage-apt-group.html)


[^4]: [ThreatStream Evasion Analysis](https://www.threatstream.com/blog/evasive-maneuvers-the-wekby-group-attempts-to-evade-analysis-via-custom-rop)


[^5]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)


[^6]: [RSA2017 Detect and Respond Adair](https://web.archive.org/web/20210803040540/https://published-prd.lanyonevents.com/published/rsaus17/sessionsFiles/5009/HTA-F02-Detecting-and-Responding-to-Advanced-Threats-within-Exchange-Environments.pdf)


[^7]: [Nccgroup Emissary Panda May 2018](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)


[^8]: [SecureWorks BRONZE UNION June 2017](https://www.secureworks.com/research/bronze-union)


[^9]: [ThreatConnect Anthem](https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/)


