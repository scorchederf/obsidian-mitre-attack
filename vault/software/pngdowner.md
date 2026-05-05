---
aliases: 
    - S0067
    
mitre-attack: https://attack.mitre.org/software/S0067
---

## S0067

[pngdowner](https://attack.mitre.org/software/S0067) is malware used by [Putter Panda](https://attack.mitre.org/groups/G0024). It is a simple tool with limited functionality and no persistence mechanism, suggesting it is used only as a simple "download-and-<br>execute" utility. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Web Protocols\|T1071.001]] | Web Protocols | [pngdowner](https://attack.mitre.org/software/S0067) uses HTTP for command and control.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [pngdowner](https://attack.mitre.org/software/S0067) deletes content from C2 communications that was saved to the user's temporary directory.[^1]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | If an initial connectivity check fails, [pngdowner](https://attack.mitre.org/software/S0067) attempts to extract proxy details and credentials from Windows Protected Storage and from the IE Credentials Store. This allows the adversary to use the proxy credentials for subsequent requests if they enable outbound HTTP access.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Putter Panda\|G0024]] | Putter Panda |



## References

[^1]: [CrowdStrike Putter Panda](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)


