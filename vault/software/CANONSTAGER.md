---
aliases: 
    - S1237
    
mitre-attack: https://attack.mitre.org/software/S1237
---

## S1237

[CANONSTAGER](https://attack.mitre.org/software/S1237) is a loader known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2025.  [Mustang Panda](https://attack.mitre.org/groups/G0129) utilizes DLL side-loading to execute within the victim environment prior to delivering a follow-on malicious encrypted payload.  [CANONSTAGER](https://attack.mitre.org/software/S1237) leverages Thread Local Storage (TLS) and Native Windows APIs within the victim environment to elude detections. [CANONSTAGER](https://attack.mitre.org/software/S1237) also hides its code utilizing window procedures and message queues.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Dynamic API Resolution\|T1027.007]] | Dynamic API Resolution | [CANONSTAGER](https://attack.mitre.org/software/S1237) has utilized custom API hashing to obfuscate the Windows APIs being used.[^1]  |
| [[Thread Local Storage\|T1055.005]] | Thread Local Storage | [CANONSTAGER](https://attack.mitre.org/software/S1237) uses the Thread Local Storage (TLS) array data structure to store function addresses resolved by its custom API hashing algorithm. The function addresses are later called throughout the binary from offsets into the TLS array.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [CANONSTAGER](https://attack.mitre.org/software/S1237) has leveraged naming conventions of its malicious DLL to match legitimate services to include cnmpaui.dll which matches the legitimate executable cnmpaui.exe that is aligned with a Canon Ink Jet Printer Assistant Tool.[^1]  |
| [[DLL\|T1574.001]] | DLL | [CANONSTAGER](https://attack.mitre.org/software/S1237) has abused legitimate executables to side-load malicious DLLs.[^1]  |
| [[Native API\|T1106]] | Native API | [CANONSTAGER](https://attack.mitre.org/software/S1237) has leveraged Native API calls to execute code within the victim’s system including `GetCurrentDirectoryW`, `RegisterClassW` and `CreateWindowExW`.[^1]  [CANONSTAGER](https://attack.mitre.org/software/S1237) also created a new overlapped window that initiates callback functions to a windows procedure that processes Windows messages until a designated message type of 0x0018 WM_SHOWWINDOW is observed which then initiates the deployment of a subsequent malicious payload.[^1]  |
| [[Hidden Window\|T1564.003]] | Hidden Window | [CANONSTAGER](https://attack.mitre.org/software/S1237) has created a new window with a height and width of zero to remain hidden on the screen.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)


