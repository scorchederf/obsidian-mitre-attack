---
aliases: 
    - S9025
    
mitre-attack: https://attack.mitre.org/software/S9025
---

## S9025

[NOOPLDR](https://attack.mitre.org/software/S9025) is a shellcode loader with XML/C# and DLL versions that has been used by [MirrorFace](https://attack.mitre.org/groups/G1054) to load [HiddenFace](https://attack.mitre.org/software/S9023).[^2] <br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Injection\|T1055]] | Process Injection | [NOOPLDR](https://attack.mitre.org/software/S9025) can inject decrypted payloads into processes including wuauclt.exe., rdrleakdiag.exe, and tabcal.exe.[^2]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [NOOPLDR](https://attack.mitre.org/software/S9025) can decrypt its payload prior to execution.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | The [NOOPLDR](https://attack.mitre.org/software/S9025) payload is encrypted with AES256-CBC.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [NOOPLDR](https://attack.mitre.org/software/S9025) can delete a file containing configuration instructions after use.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [NOOPLDR](https://attack.mitre.org/software/S9025) can use control flow flattening to help hide malicious code.[^2] [^1]  |
| [[Native API\|T1106]] | Native API | [NOOPLDR](https://attack.mitre.org/software/S9025) can use native APIs `NtProtectVirtualMemory`, `NtWriteVirtualMemory`, and `NtCreateThreadEx` to aid process injection.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [NOOPLDR](https://attack.mitre.org/software/S9025) can store its payload in the Registry using a random hex string in `HKCU\SOFTWARE\Microsoft\COM3`.[^2]  |
| [[DLL\|T1574.001]] | DLL | [NOOPLDR](https://attack.mitre.org/software/S9025) can be executed via sideloading.[^2] [^1]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [NOOPLDR](https://attack.mitre.org/software/S9025) can hide services used to aid execution.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [NOOPLDR](https://attack.mitre.org/software/S9025) can discover the device ID and hostname from the targeted machine to use for encryption keys.[^2]  |
| [[Junk Code Insertion\|T1027.016]] | Junk Code Insertion | [NOOPLDR](https://attack.mitre.org/software/S9025) can insert junk code to obfuscate malicious payloads.[^2] [^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MirrorFace\|G1054]] | MirrorFace |



## References

[^1]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)


[^2]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)


