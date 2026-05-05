---
aliases: 
    - S1101
    
mitre-attack: https://attack.mitre.org/software/S1101
---

## S1101

[LoFiSe](https://attack.mitre.org/software/S1101) has been used by [ToddyCat](https://attack.mitre.org/groups/G1022) since at least 2023 to identify and collect files of interest on targeted systems.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [LoFiSe](https://attack.mitre.org/software/S1101) can collect files into password-protected ZIP-archives for exfiltration.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LoFiSe](https://attack.mitre.org/software/S1101) can monitor the file system to identify files less than 6.4 MB in size with file extensions including .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf, .rtf, .tif, .odt, .ods, .odp, .eml, and .msg.[^1]  |
| [[DLL\|T1574.001]] | DLL | [LoFiSe](https://attack.mitre.org/software/S1101) has been executed as a file named DsNcDiag.dll through side-loading.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [LoFiSe](https://attack.mitre.org/software/S1101) can save files to be evaluated for further exfiltration in the `C:\Programdata\Microsoft\` and 	`C:\windows\temp\` folders.<br> [^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [LoFiSe](https://attack.mitre.org/software/S1101) can collect files of interest from targeted systems.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | [LoFiSe](https://attack.mitre.org/software/S1101) can collect all the files from the working directory every three hours and place them into a password-protected archive for further exfiltration.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[ToddyCat\|G1022]] | ToddyCat |



## References

[^1]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)


