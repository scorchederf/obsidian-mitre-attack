---
aliases: 
    - S0499
    
mitre-attack: https://attack.mitre.org/software/S0499
---

## S0499

[Hancitor](https://attack.mitre.org/software/S0499) is a downloader that has been used by [Pony](https://attack.mitre.org/software/S0453) and other information stealing malware.[^2] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Malicious File\|T1204.002]] | Malicious File | [Hancitor](https://attack.mitre.org/software/S0499) has used malicious Microsoft Word documents, sent via email, which prompted the victim to enable macros.[^4]  |
| [[Verclsid\|T1218.012]] | Verclsid | [Hancitor](https://attack.mitre.org/software/S0499) has used verclsid.exe to download and execute a malicious script.[^1]  |
| [[Compression\|T1027.015]] | Compression | [Hancitor](https://attack.mitre.org/software/S0499) has delivered compressed payloads in ZIP files to victims.[^4]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hancitor](https://attack.mitre.org/software/S0499) has the ability to download additional files from C2.[^2]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Hancitor](https://attack.mitre.org/software/S0499) has relied upon users clicking on a malicious link delivered through phishing.[^2]  |
| [[Native API\|T1106]] | Native API | [Hancitor](https://attack.mitre.org/software/S0499) has used `CallWindowProc` and `EnumResourceTypesA` to interpret and execute shellcode.[^4]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Hancitor](https://attack.mitre.org/software/S0499) has been delivered via phishing emails with malicious attachments.[^4]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [Hancitor](https://attack.mitre.org/software/S0499)  has added Registry Run keys to establish persistence.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Hancitor](https://attack.mitre.org/software/S0499) has used PowerShell to execute commands.[^4]  |
| [[Spearphishing Link\|T1566.002]] | Spearphishing Link | [Hancitor](https://attack.mitre.org/software/S0499) has been delivered via phishing emails which contained malicious links.[^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Hancitor](https://attack.mitre.org/software/S0499) has used Base64 to encode malicious links.[^2]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Hancitor](https://attack.mitre.org/software/S0499) has deleted files using the VBA `kill` function.[^4]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Hancitor](https://attack.mitre.org/software/S0499) has used a macro to check that an ActiveDocument shape object in the lure message is present. If this object is not found, the macro will exit without downloading additional payloads.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Hancitor](https://attack.mitre.org/software/S0499) has decoded Base64 encoded URLs to insert a recipient’s name into the filename of the Word document. [Hancitor](https://attack.mitre.org/software/S0499) has also extracted executables from ZIP files.[^2] [^4]  |




## References

[^1]: [Red Canary Verclsid.exe](https://redcanary.com/blog/verclsid-exe-threat-detection/)


[^2]: [Threatpost Hancitor](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)


[^3]: Chanitor


[^4]: [FireEye Hancitor](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)


