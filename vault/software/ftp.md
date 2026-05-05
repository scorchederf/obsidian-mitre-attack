---
aliases: 
    - S0095
    
mitre-attack: https://attack.mitre.org/software/S0095
---

## S0095

[ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.[^5] [^7] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Lateral Tool Transfer\|T1570]] | Lateral Tool Transfer | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files between systems within a compromised environment.[^5] [^7]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [ftp](https://attack.mitre.org/software/S0095) may be used to exfiltrate data separate from the main command and control protocol.[^5] [^7]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files from an external system into a compromised environment.[^5] [^7]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Naikon\|G0019]] | Naikon |
| [[APT39\|G0087]] | APT39 |
| [[APT41\|G0096]] | APT41 |
| [[APT33\|G0064]] | APT33 |
| [[OilRig\|G0049]] | OilRig |



## References

[^1]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)


[^2]: [FireEye APT41 March 2020](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)


[^3]: [FBI FLASH APT39 September 2020](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)


[^4]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)


[^5]: [Microsoft FTP](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)


[^6]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)


[^7]: [Linux FTP](https://linux.die.net/man/1/ftp)


