---
aliases: 
    - S0235
    
mitre-attack: https://attack.mitre.org/software/S0235
---

## S0235

[CrossRAT](https://attack.mitre.org/software/S0235) is a cross platform RAT.

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Screen Capture\|T1113]] | Screen Capture | [CrossRAT](https://attack.mitre.org/software/S0235) is capable of taking screen captures.[^2]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [CrossRAT](https://attack.mitre.org/software/S0235) creates a Launch Agent on macOS.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [CrossRAT](https://attack.mitre.org/software/S0235) can list all files on a system.[^2]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [CrossRAT](https://attack.mitre.org/software/S0235) uses run keys for persistence on Windows.[^2]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | [CrossRAT](https://attack.mitre.org/software/S0235) can use an XDG Autostart to establish persistence.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Dark Caracal\|G0070]] | Dark Caracal |



## References

[^1]: [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


[^2]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)


[^3]: CrossRAT


