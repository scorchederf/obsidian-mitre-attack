---
aliases: 
    - S9036
    
mitre-attack: https://attack.mitre.org/software/S9036
---

## S9036

[LP-Notes](https://attack.mitre.org/software/S9036) is a C/C++ Windows credential stealer used by [MuddyWater](https://attack.mitre.org/groups/G0069). [LP-Notes](https://attack.mitre.org/software/S9036) was named after the `lp-notes.txt` file that is used to store stolen credentials.[^1]   

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Native API\|T1106]] | Native API | [LP-Notes](https://attack.mitre.org/software/S9036) has used the `ImpersonateLoggedOnUser` API to impersonate the security context of the taskhostw.exe process.[^1]  Additionally, [LP-Notes](https://attack.mitre.org/software/S9036) has also used the `CredUIPromptForWindowsCredentialsW` API to obtain Windows credentials.[^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [LP-Notes](https://attack.mitre.org/software/S9036) has displayed a fake Windows Security dialog box to prompt for Windows credentials.[^1]  |
| [[Valid Accounts\|T1078]] | Valid Accounts | [LP-Notes](https://attack.mitre.org/software/S9036) has used stolen Windows credentials to log in as the users.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [LP-Notes](https://attack.mitre.org/software/S9036) has decrypted strings with lengths ranging from 15 to 19 characters using the same decryption key for each string.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [LP-Notes](https://attack.mitre.org/software/S9036) has stored collected credentials in ` C:\Users\Public\Downloads\lp-notes.txt`.[^1]   |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [LP-Notes](https://attack.mitre.org/software/S9036) has encrypted collected credentials using AES-CBC from the CNG API and the key ED15C8344B45DAED1E0578F8BC1A32411812C61F4CB45D89B107287DE0E09FFC<br>and the initialization vector 91A4E6F6D51DAEE773A8F00279792578.[^1]   |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [LP-Notes](https://attack.mitre.org/software/S9036) has dynamically resolved API functions during the C runtime startup.[^1]   |
| [[PowerShell\|T1059.001]] | PowerShell | [LP-Notes](https://attack.mitre.org/software/S9036) has been downloaded and executed by PowerShell’s`Invoke-WebRequest` and `Invoke-Expression` cmdlets.[^1]   |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [LP-Notes](https://attack.mitre.org/software/S9036) has impersonated the security context of the taskhostw.exe process via the `ImpersonateLoggedOnUser` API.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [LP-Notes](https://attack.mitre.org/software/S9036) has searched for the process taskhostw.exe.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [LP-Notes](https://attack.mitre.org/software/S9036) has used a custom addition-based function and a string stacking function for string encryption.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


