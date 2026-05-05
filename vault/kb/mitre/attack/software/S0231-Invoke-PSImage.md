---
aliases: 
    - S0231
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0231-Invoke-PSImage
---

## Description

[[kb/mitre/attack/software/S0231-Invoke-PSImage\|Invoke-PSImage]] takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1027.003-Steganography\|T1027.003]] | Steganography | [[kb/mitre/attack/software/S0231-Invoke-PSImage\|Invoke-PSImage]] can be used to embed a PowerShell script within the pixels of a PNG file.[^2]  |
| [[kb/mitre/attack/techniques/T1027.009-Embedded_Payloads\|T1027.009]] | Embedded Payloads | [[kb/mitre/attack/software/S0231-Invoke-PSImage\|Invoke-PSImage]] can be used to embed payload data within a new image file.[^1]  |





> [!info]- References
> [^1]: [GitHub PSImage](https://github.com/peewpw/Invoke-PSImage)

> [^2]: [GitHub Invoke-PSImage](https://github.com/peewpw/Invoke-PSImage)


