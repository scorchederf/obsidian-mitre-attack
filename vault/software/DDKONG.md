---
aliases: 
    - S0255
    
mitre-attack: https://attack.mitre.org/software/S0255
---

## S0255

[DDKONG](https://attack.mitre.org/software/S0255) is a malware sample that was part of a campaign by [Rancor](https://attack.mitre.org/groups/G0075). [DDKONG](https://attack.mitre.org/software/S0255) was first seen used in February 2017. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [DDKONG](https://attack.mitre.org/software/S0255) downloads and uploads files on the victim’s machine.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [DDKONG](https://attack.mitre.org/software/S0255) decodes an embedded configuration using XOR.[^1]  |
| [[Rundll32\|T1218.011]] | Rundll32 | [DDKONG](https://attack.mitre.org/software/S0255) uses Rundll32 to ensure only a single instance of itself is running at once.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [DDKONG](https://attack.mitre.org/software/S0255) lists files on the victim’s machine.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Rancor\|G0075]] | Rancor |



## References

[^1]: [Rancor Unit42 June 2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)


