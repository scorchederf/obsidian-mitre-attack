---
aliases: 
    - Putter Panda
    - APT2
    - MSUpdater
mitre-attack: https://attack.mitre.org/groups/G0024
---

## G0024

[Putter Panda](https://attack.mitre.org/groups/G0024) is a Chinese threat group that has been attributed to Unit 61486 of the 12th Bureau of the PLA’s 3rd General Staff Department (GSD). [^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | A dropper used by [Putter Panda](https://attack.mitre.org/groups/G0024) installs itself into the ASEP Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` with a value named McUpdate.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | Malware used by [Putter Panda](https://attack.mitre.org/groups/G0024) attempts to terminate processes corresponding to two components of Sophos Anti-Virus (SAVAdminService.exe and SavService.exe).[^1]  |
| [[Dynamic-link Library Injection\|T1055.001]] | Dynamic-link Library Injection | An executable dropped onto victims by [Putter Panda](https://attack.mitre.org/groups/G0024) aims to inject the specified DLL into a process that would normally be accessing the network, including Outlook Express (msinm.exe), Outlook (outlook.exe), Internet Explorer (iexplore.exe), and Firefox (firefox.exe).[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Droppers used by [Putter Panda](https://attack.mitre.org/groups/G0024) use RC4 or a 16-byte XOR key consisting of the bytes 0xA0 – 0xAF to obfuscate payloads.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[3PARA RAT\|S0066]] | 3PARA RAT | [^1]  |
| [[pngdowner\|S0067]] | pngdowner | [^1]  |
| [[4H RAT\|S0065]] | 4H RAT | [^1]  |
| [[httpclient\|S0068]] | httpclient | [^1]  |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


[^2]: MSUpdater


[^3]: [Cylance Putter Panda](https://blogs.blackberry.com/en/2016/01/puttering-into-the-future)


[^4]: Putter Panda


[^5]: APT2


