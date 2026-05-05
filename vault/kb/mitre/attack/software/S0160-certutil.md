---
aliases: 
    - S0160
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0160-certutil
---

## Description

[[kb/mitre/attack/software/S0160-certutil\|certutil]] is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1105-Ingress_Tool_Transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to download files from a given URL.[^2] [^3]  |
| [[kb/mitre/attack/techniques/T1140-Deobfuscate_Decode_Files_or_Information\|T1140]] | Deobfuscate／Decode Files or Information | [[kb/mitre/attack/software/S0160-certutil\|certutil]] has been used to decode binaries hidden inside certificate files as Base64 information.[^1]  |
| [[kb/mitre/attack/techniques/T1553.004-Install_Root_Certificate\|T1553.004]] | Install Root Certificate | [[kb/mitre/attack/software/S0160-certutil\|certutil]] can be used to install browser root certificates as a precursor to performing [[kb/mitre/attack/techniques/T1557-Adversary-in-the-Middle\|Adversary-in-the-Middle]] between connections to banking websites. Example command: `certutil -addstore -f -user ROOT ProgramData\cert512121.der`.[^4]  |
| [[kb/mitre/attack/techniques/T1560.001-Archive_via_Utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0160-certutil\|certutil]] may be used to Base64 encode collected data.[^2] [^3]  |





> [!info]- References
> [^1]: [Malwarebytes Targeted Attack against Saudi Arabia](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)

> [^2]: [TechNet Certutil](https://technet.microsoft.com/library/cc732443.aspx)

> [^3]: [LOLBAS Certutil](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)

> [^4]: [Palo Alto Retefe](https://researchcenter.paloaltonetworks.com/2015/08/retefe-banking-trojan-targets-sweden-switzerland-and-japan/)


