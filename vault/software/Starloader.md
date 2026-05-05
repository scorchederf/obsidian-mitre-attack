---
aliases: 
    - S0188
    
mitre-attack: https://attack.mitre.org/software/S0188
---

## S0188

[Starloader](https://attack.mitre.org/software/S0188) is a loader component that has been observed loading [Felismus](https://attack.mitre.org/software/S0171) and associated tools. [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Starloader](https://attack.mitre.org/software/S0188) decrypts and executes shellcode from a file called Stars.jps.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Starloader](https://attack.mitre.org/software/S0188) has masqueraded as legitimate software update packages such as Adobe Acrobat Reader and Intel.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Sowbug\|G0054]] | Sowbug |



## References

[^1]: [Symantec Sowbug Nov 2017](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)


[^2]: Starloader


