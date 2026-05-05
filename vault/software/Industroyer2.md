---
aliases: 
    - S1072
    
mitre-attack: https://attack.mitre.org/software/S1072
---

## S1072

[Industroyer2](https://attack.mitre.org/software/S1072) is a compiled and static piece of malware that has the ability to communicate over the IEC-104 protocol. It is similar to the IEC-104 module found in [Industroyer](https://attack.mitre.org/software/S0604). Security researchers assess that [Industroyer2](https://attack.mitre.org/software/S1072) was designed to cause impact to high-voltage electrical substations. The initial [Industroyer2](https://attack.mitre.org/software/S1072) sample was compiled on 03/23/2022 and scheduled to execute on 04/08/2022, however it was discovered before deploying, resulting in no impact.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [Industroyer2](https://attack.mitre.org/software/S1072) has the ability to cyclically enumerate running processes such as PServiceControl.exe, PService_PDD.exe, and other targets supplied through a hardcoded configuration.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [Industroyer2 Blackhat ESET](https://www.youtube.com/watch?v=xC9iM5wVedQ)


[^2]: [Industroyer2 ESET April 2022](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/)


[^3]: [Industroyer2 Mandiant April 2022](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)


[^4]: [mandiant_apt44_unearthing_sandworm](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)


