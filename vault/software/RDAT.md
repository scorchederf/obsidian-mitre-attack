---
aliases: 
    - S0495
    
mitre-attack: https://attack.mitre.org/software/S0495
---

## S0495

[RDAT](https://attack.mitre.org/software/S0495) is a backdoor used by the suspected Iranian threat group [OilRig](https://attack.mitre.org/groups/G0049). [RDAT](https://attack.mitre.org/software/S0495) was originally identified in 2017 and targeted companies in the telecommunications sector.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [RDAT](https://attack.mitre.org/software/S0495) can use HTTP communications for C2, as well as using the WinHTTP library to make requests to the Exchange Web Services API.[^1]  |
| [[Steganography\|T1027.003]] | Steganography | [RDAT](https://attack.mitre.org/software/S0495) can also embed data within a BMP image prior to exfiltration.[^1] 	 |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [RDAT](https://attack.mitre.org/software/S0495) has used Windows Video Service as a name for malicious services.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [RDAT](https://attack.mitre.org/software/S0495) has executed commands using `cmd.exe /c`.[^1] 	 |
| [[DNS\|T1071.004]] | DNS | [RDAT](https://attack.mitre.org/software/S0495) has used DNS to communicate with the C2.[^1] 	 |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [RDAT](https://attack.mitre.org/software/S0495) has masqueraded as VMware.exe.[^1] 	 |
| [[Screen Capture\|T1113]] | Screen Capture | [RDAT](https://attack.mitre.org/software/S0495) can take a screenshot on the infected system.[^1] 	 |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [RDAT](https://attack.mitre.org/software/S0495) can communicate with the C2 via base32-encoded subdomains.[^1] 	 |
| [[Non-Standard Encoding\|T1132.002]] | Non-Standard Encoding | [RDAT](https://attack.mitre.org/software/S0495) can communicate with the C2 via subdomains that utilize base64 with character substitutions.[^1] 	 |
| [[Windows Service\|T1543.003]] | Windows Service | [RDAT](https://attack.mitre.org/software/S0495) has created a service when it is installed on the victim machine.[^1] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RDAT](https://attack.mitre.org/software/S0495) can deobfuscate the base64-encoded and AES-encrypted files downloaded from the C2 server.[^1] 	 |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RDAT](https://attack.mitre.org/software/S0495) has used AES ciphertext to encode C2 communications.[^1]  |
| [[Mail Protocols\|T1071.003]] | Mail Protocols | [RDAT](https://attack.mitre.org/software/S0495) can use email attachments for C2 communications.[^1]  |
| [[Steganography\|T1001.002]] | Steganography | [RDAT](https://attack.mitre.org/software/S0495) can process steganographic images attached to email messages to send and receive C2 commands. [RDAT](https://attack.mitre.org/software/S0495) can also embed additional messages within BMP images to communicate with the [RDAT](https://attack.mitre.org/software/S0495) operator.[^1] 	 |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [RDAT](https://attack.mitre.org/software/S0495) can upload a file via HTTP POST response to the C2 split into 102,400-byte portions. [RDAT](https://attack.mitre.org/software/S0495) can also download data from the C2 which is split into 81,920-byte portions.[^1] 	 |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [RDAT](https://attack.mitre.org/software/S0495) can download files via DNS.[^1] 	 |
| [[File Deletion\|T1070.004]] | File Deletion | [RDAT](https://attack.mitre.org/software/S0495) can issue SOAP requests to delete already processed C2 emails. [RDAT](https://attack.mitre.org/software/S0495) can also delete itself from the infected system.[^1] 	 |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [RDAT](https://attack.mitre.org/software/S0495) can exfiltrate data gathered from the infected system via the established Exchange Web Services API C2 channel.[^1]  |
| [[Fallback Channels\|T1008]] | Fallback Channels | [RDAT](https://attack.mitre.org/software/S0495) has used HTTP if DNS C2 communications were not functioning.[^1] 	 |
| [[Data Obfuscation\|T1001]] | Data Obfuscation | [RDAT](https://attack.mitre.org/software/S0495) has used encoded data within subdomains as AES ciphertext to communicate from the host to the C2.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)


