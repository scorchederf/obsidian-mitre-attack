---
aliases: 
    - S1121
    
mitre-attack: https://attack.mitre.org/software/S1121
---

## S1121

[LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) is a backdoor that was used by UNC5325 during [Cutting Edge](https://attack.mitre.org/campaigns/C0029) to deploy malware on targeted Ivanti Connect Secure VPNs and to establish persistence across system upgrades and patches.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can function as a stand-alone backdoor communicating over the `/tmp/clientsDownload.sock` socket.[^1]  |
| [[Proxy\|T1090]] | Proxy | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) has the ability to function as a SOCKS proxy.[^1]  |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can communicate over SSL using the private key from the Ivanti Connect Secure web server.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can append malicious components to the `tmp/tmpmnt/bin/samba_upgrade.tar` archive inside the factory reset partition in attempt to persist post reset.[^1]  |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can initialize itself as a daemon to run persistently in the background.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can monitor for system upgrade events by checking for the presence of `/tmp/data/root/dev`.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [LITTLELAMB.WOOLTEA](https://attack.mitre.org/software/S1121) can check the type of Ivanti VPN device it is running on by executing `first_run()` to identify the first four bytes of the motherboard serial number.[^1]  |




## References

[^1]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)


