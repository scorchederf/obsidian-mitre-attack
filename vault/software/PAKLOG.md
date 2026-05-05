---
aliases: 
    - S1233
    
mitre-attack: https://attack.mitre.org/software/S1233
---

## S1233

[PAKLOG](https://attack.mitre.org/software/S1233) is a keylogger known to be leveraged by [Mustang Panda](https://attack.mitre.org/groups/G0129) and was first observed utilized in 2024. [PAKLOG](https://attack.mitre.org/software/S1233) is deployed via a RAR archive (e.g., key.rar), which contains two files: a signed, legitimate binary (PACLOUD.exe) and the malicious [PAKLOG](https://attack.mitre.org/software/S1233) DLL (pa_lang2.dll). The PACLOUD.exe binary is used to side-load the [PAKLOG](https://attack.mitre.org/software/S1233) DLL which starts with the keylogger functionality.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [PAKLOG](https://attack.mitre.org/software/S1233) has utilized a simple encoding mechanism to encode characters in the buffer.[^1]    |
| [[Keylogging\|T1056.001]] | Keylogging | [PAKLOG](https://attack.mitre.org/software/S1233) has captured keystrokes using Windows API.[^1]  |
| [[Clipboard Data\|T1115]] | Clipboard Data | [PAKLOG](https://attack.mitre.org/software/S1233) has monitored and extracted clipboard contents.[^1]  |
| [[Native API\|T1106]] | Native API | [PAKLOG](https://attack.mitre.org/software/S1233) has used Windows API `SetWindowsHookExW` with `idHook` set to `WH_KEYBOARD_LL` and a custom hook procedure to support its keylogging functions.[^1]  |
| [[Code Signing\|T1553.002]] | Code Signing | [PAKLOG](https://attack.mitre.org/software/S1233) has used legitimate signed binaries such as PACLOUD.exe for follow-on execution of malicious DLLs through DLL Side-Loading.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [PAKLOG](https://attack.mitre.org/software/S1233) has stored the captured data in a file located `C:\\Users\\Public\\Libraries\\record.txt`.[^1]  |
| [[Application Window Discovery\|T1010]] | Application Window Discovery | [PAKLOG](https://attack.mitre.org/software/S1233) has used `GetForegroundWindow` to access the foreground window. [^1]   [PAKLOG](https://attack.mitre.org/software/S1233) has also captured text from the foreground windows.[^1]  |
| [[DLL\|T1574.001]] | DLL | [PAKLOG](https://attack.mitre.org/software/S1233) has leveraged legitimate binaries to conduct DLL side-loading.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [PAKLOG](https://attack.mitre.org/software/S1233) has detected and logged the full path of processes active in the foreground using Windows API calls.[^1]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [PAKLOG](https://attack.mitre.org/software/S1233) has collected a timestamp to log the precise time a key was pressed, formatted as %Y-%m-%d %H:%M:%S.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Mustang Panda\|G0129]] | Mustang Panda |



## References

[^1]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)


