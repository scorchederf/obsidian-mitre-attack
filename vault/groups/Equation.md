---
aliases: 
    - Equation
mitre-attack: https://attack.mitre.org/groups/G0020
---

## G0020

[Equation](https://attack.mitre.org/groups/G0020) is a sophisticated threat group that employs multiple remote access tools. The group is known to use zero-day exploits and has developed the capability to overwrite the firmware of hard disk drives. [^3] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Hidden File System\|T1564.005]] | Hidden File System | [Equation](https://attack.mitre.org/groups/G0020) has used an encrypted virtual file system stored in the Windows Registry.[^3]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [Equation](https://attack.mitre.org/groups/G0020) has used tools with the functionality to search for specific information about the attached hard drive that could be used to identify and overwrite the firmware.[^3]  |
| [[Environmental Keying\|T1480.001]] | Environmental Keying | [Equation](https://attack.mitre.org/groups/G0020) has been observed utilizing environmental keying in payload delivery.[^2] [^3]  |
| [[Component Firmware\|T1542.002]] | Component Firmware | [Equation](https://attack.mitre.org/groups/G0020) is known to have the capability to overwrite the firmware on hard drives from some manufacturers.[^3]   |




## References

[^1]: Equation


[^2]: [Kaspersky Gauss Whitepaper](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20134940/kaspersky-lab-gauss.pdf)


[^3]: [Kaspersky Equation QA](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064459/Equation_group_questions_and_answers.pdf)


