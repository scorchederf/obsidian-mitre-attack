---
aliases: 
    - Dark Caracal
mitre-attack: https://attack.mitre.org/groups/G0070
---

## G0070

[Dark Caracal](https://attack.mitre.org/groups/G0070) is threat group that has been attributed to the Lebanese General Directorate of General Security (GDGS) and has operated since at least 2012. [^2] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Dark Caracal](https://attack.mitre.org/groups/G0070) has obfuscated strings in [Bandook](https://attack.mitre.org/software/S0234) by base64 encoding, and then encrypting them.[^2]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Dark Caracal](https://attack.mitre.org/groups/G0070) has used macros in Word documents that would download a second stage if executed.[^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Dark Caracal](https://attack.mitre.org/groups/G0070)'s version of [Bandook](https://attack.mitre.org/software/S0234) communicates with their server over a TCP port using HTTP payloads Base64 encoded and suffixed with the string “&&&”.[^2]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Dark Caracal](https://attack.mitre.org/groups/G0070) makes their malware look like Flash Player, Office, or PDF documents in order to entice a user to click on it.[^2]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Dark Caracal](https://attack.mitre.org/groups/G0070) has used UPX to pack [Bandook](https://attack.mitre.org/software/S0234).[^2]  |
| [[Compiled HTML File\|T1218.001]] | Compiled HTML File | [Dark Caracal](https://attack.mitre.org/groups/G0070) leveraged a compiled HTML file that contained a command to download and run an executable.[^2]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Dark Caracal](https://attack.mitre.org/groups/G0070) leveraged a watering hole to serve up malicious code.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Dark Caracal](https://attack.mitre.org/groups/G0070)'s version of [Bandook](https://attack.mitre.org/software/S0234) adds a registry key to `HKEY_USERS\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Dark Caracal](https://attack.mitre.org/groups/G0070) collected file listings of all default Windows directories.[^2]  |
| [[Spearphishing via Service\|T1566.003]] | Spearphishing via Service | [Dark Caracal](https://attack.mitre.org/groups/G0070) spearphished victims via Facebook and Whatsapp.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Dark Caracal](https://attack.mitre.org/groups/G0070) collected complete contents of the 'Pictures' folder from compromised Windows systems.[^2]  |
| [[Screen Capture\|T1113]] | Screen Capture | [Dark Caracal](https://attack.mitre.org/groups/G0070) took screenshots using their Windows malware.[^2]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Bandook\|S0234]] | Bandook | [^2] [^1]   |
| [[FinFisher\|S0182]] | FinFisher | [^2]  |
| [[CrossRAT\|S0235]] | CrossRAT | [^2]  |



## References

[^1]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)


[^2]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^3]: Dark Caracal


