---
aliases: 
    - S1035
    
mitre-attack: https://attack.mitre.org/software/S1035
---

## S1035

[Small Sieve](https://attack.mitre.org/software/S1035) is a Telegram Bot API-based Python backdoor that has been distributed using a Nullsoft Scriptable Install System (NSIS) Installer; it has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least January 2022.[^3] [^4] <br><br>Security researchers have also noted [Small Sieve](https://attack.mitre.org/software/S1035)'s use by UNC3313, which may be associated with [MuddyWater](https://attack.mitre.org/groups/G0069).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Small Sieve](https://attack.mitre.org/software/S1035) can use `cmd.exe` to execute commands on a victim's system.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Small Sieve](https://attack.mitre.org/software/S1035) has the ability to download files.[^4]  |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [Small Sieve](https://attack.mitre.org/software/S1035) can use a custom hex byte swapping encoding scheme to obfuscate tasking traffic.[^3] [^4]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [Small Sieve](https://attack.mitre.org/software/S1035) can only execute correctly if the word `Platypus` is passed to it on the command line.[^4]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Small Sieve](https://attack.mitre.org/software/S1035) can obtain the IP address of a victim host.[^4]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [Small Sieve](https://attack.mitre.org/software/S1035) can use SSL/TLS for its HTTPS Telegram Bot API-based C2 channel.[^3]  |
| [[Python\|T1059.006]] | Python | [Small Sieve](https://attack.mitre.org/software/S1035) can use Python scripts to execute commands.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Small Sieve](https://attack.mitre.org/software/S1035) has the ability to add itself to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\OutlookMicrosift` for persistence.[^4]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Small Sieve](https://attack.mitre.org/software/S1035) can use variations of Microsoft and Outlook spellings, such as "Microsift", in its file names to avoid detection.[^4]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Small Sieve](https://attack.mitre.org/software/S1035) has the ability to use a custom hex byte swapping encoding scheme combined with an obfuscated Base64 function to protect program strings and Telegram credentials.[^4]  |
| [[System Owner／User Discovery\|T1033]] | System Owner／User Discovery | [Small Sieve](https://attack.mitre.org/software/S1035) can obtain the id of a logged in user.[^4]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [Small Sieve](https://attack.mitre.org/software/S1035) has the ability to use the Telegram Bot API from Telegram Messenger to send and receive messages.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Small Sieve](https://attack.mitre.org/software/S1035) can contact actor-controlled C2 servers by using the Telegram API over HTTPS.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: GRAMDOOR


[^2]: [Mandiant UNC3313 Feb 2022](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)


[^3]: [DHS CISA AA22-055A MuddyWater February 2022](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)


[^4]: [NCSC GCHQ Small Sieve Jan 2022](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)


