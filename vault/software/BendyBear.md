---
aliases: 
    - S0574
    
mitre-attack: https://attack.mitre.org/software/S0574
---

## S0574

[BendyBear](https://attack.mitre.org/software/S0574) is an x64 shellcode for a stage-zero implant designed to download malware from a C2 server. First discovered in August 2020, [BendyBear](https://attack.mitre.org/software/S0574) shares a variety of features with [Waterbear](https://attack.mitre.org/software/S0579), malware previously attributed to the Chinese cyber espionage group [BlackTech](https://attack.mitre.org/groups/G0098).[^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [BendyBear](https://attack.mitre.org/software/S0574) has decrypted function blocks using a XOR key during runtime to evade detection.[^2]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [BendyBear](https://attack.mitre.org/software/S0574) is designed to download an implant from a C2 server.[^2]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | [BendyBear](https://attack.mitre.org/software/S0574) can check for analysis environments and signs of debugging using the Windows API `kernel32!GetTickCountKernel32` call.[^2]   |
| [[Junk Data\|T1001.001]] | Junk Data | [BendyBear](https://attack.mitre.org/software/S0574) has used byte randomization to obscure its behavior.[^2]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [BendyBear](https://attack.mitre.org/software/S0574) has used a custom RC4 and XOR encrypted protocol over port 443 for C2.[^2]  |
| [[Polymorphic Code\|T1027.014]] | Polymorphic Code | BendyBear changes its runtime footprint during code execution to evade signature-based defenses.[^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [BendyBear](https://attack.mitre.org/software/S0574) communicates to a C2 server over port 443 using modified RC4 and XOR-encrypted chunks.[^2]   |
| [[Query Registry\|T1012]] | Query Registry | [BendyBear](https://attack.mitre.org/software/S0574) can query the host's Registry key at `HKEY_CURRENT_USER\Console\QuickEdit` to retrieve data.[^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [BendyBear](https://attack.mitre.org/software/S0574) has encrypted payloads using RC4 and XOR.[^2]  |
| [[Native API\|T1106]] | Native API | [BendyBear](https://attack.mitre.org/software/S0574) can load and execute modules and Windows Application Programming (API) calls using standard shellcode API hashing.[^2]  |
| [[System Time Discovery\|T1124]] | System Time Discovery | [BendyBear](https://attack.mitre.org/software/S0574) has the ability to determine local time on a compromised host.[^2]   |




## References

[^1]: BendyBear


[^2]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)


