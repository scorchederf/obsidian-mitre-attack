---
aliases: 
    - S0213
    
mitre-attack: https://attack.mitre.org/software/S0213
---

## S0213

[DOGCALL](https://attack.mitre.org/software/S0213) is a backdoor used by [APT37](https://attack.mitre.org/groups/G0067) that has been used to target South Korean government and military organizations in 2017. It is typically dropped using a Hangul Word Processor (HWP) exploit. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Keylogging\|T1056.001]] | Keylogging | [DOGCALL](https://attack.mitre.org/software/S0213) is capable of logging keystrokes.[^2] [^1]  |
| [[Screen Capture\|T1113]] | Screen Capture | [DOGCALL](https://attack.mitre.org/software/S0213) is capable of capturing screenshots of the victim's machine.[^2] [^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DOGCALL](https://attack.mitre.org/software/S0213) can download and execute additional payloads.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DOGCALL](https://attack.mitre.org/software/S0213) is encrypted using single-byte XOR.[^1]  |
| [[Bidirectional Communication\|T1102.002]] | Bidirectional Communication | [DOGCALL](https://attack.mitre.org/software/S0213) is capable of leveraging cloud storage APIs such as Cloud, Box, Dropbox, and Yandex for C2.[^2] [^1]  |
| [[Audio Capture\|T1123]] | Audio Capture | [DOGCALL](https://attack.mitre.org/software/S0213) can capture microphone data from the victim's machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT37\|G0067]] | APT37 |



## References

[^1]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)


[^2]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)


[^3]: DOGCALL


