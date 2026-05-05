---
aliases: 
    - S0530
    
mitre-attack: https://attack.mitre.org/software/S0530
---

## S0530

[Melcoz](https://attack.mitre.org/software/S0530) is a banking trojan family built from the open source tool Remote Access PC. [Melcoz](https://attack.mitre.org/software/S0530) was first observed in attacks in Brazil and since 2018 has spread to Chile, Mexico, Spain, and Portugal.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Transmitted Data Manipulation\|T1565.002]] | Transmitted Data Manipulation | [Melcoz](https://attack.mitre.org/software/S0530) can monitor the clipboard for cryptocurrency addresses and change the intended address to one controlled by the adversary.[^1]  |
| [[AutoHotKey & AutoIT\|T1059.010]] | AutoHotKey & AutoIT | [Melcoz](https://attack.mitre.org/software/S0530) has been distributed through an AutoIt loader script.[^1]  |
| [[Msiexec\|T1218.007]] | Msiexec | [Melcoz](https://attack.mitre.org/software/S0530) can use MSI files with embedded VBScript for execution.[^1]  |
| [[Browser Session Hijacking\|T1185]] | Browser Session Hijacking | [Melcoz](https://attack.mitre.org/software/S0530) can monitor the victim's browser for online banking sessions and display an overlay window to manipulate the session in the background.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Melcoz](https://attack.mitre.org/software/S0530) has the ability to download additional files to a compromised host.[^1]  |
| [[DLL\|T1574.001]] | DLL | [Melcoz](https://attack.mitre.org/software/S0530) can use DLL hijacking to bypass security controls.[^1]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [Melcoz](https://attack.mitre.org/software/S0530) has the ability to steal credentials from web browsers.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [Melcoz](https://attack.mitre.org/software/S0530) can use VBS scripts to execute malicious DLLs.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Melcoz](https://attack.mitre.org/software/S0530) has been packed with VMProtect and Themida.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [Melcoz](https://attack.mitre.org/software/S0530) can monitor content saved to the clipboard.[^1]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Melcoz](https://attack.mitre.org/software/S0530) has gained execution through victims opening malicious links.[^1]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Melcoz](https://attack.mitre.org/software/S0530) has been spread through malicious links embedded in e-mails.[^1]  |




## References

[^1]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)


