---
aliases: 
    - S0231
    
mitre-attack: https://attack.mitre.org/software/S0231
---

## S0231

[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Steganography\|T1027.003]] | Steganography | [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed a PowerShell script within the pixels of a PNG file.[^2]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [Invoke-PSImage](https://attack.mitre.org/software/S0231) can be used to embed payload data within a new image file.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sandworm Team\|G0034]] | Sandworm Team |



## References

[^1]: [US District Court Indictment GRU Unit 74455 October 2020](https://www.justice.gov/opa/press-release/file/1328521/download)


[^2]: [GitHub Invoke-PSImage](https://github.com/peewpw/Invoke-PSImage)


[^3]: [GitHub PSImage](https://github.com/peewpw/Invoke-PSImage)


