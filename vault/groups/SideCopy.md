---
aliases: 
    - SideCopy
mitre-attack: https://attack.mitre.org/groups/G1008
---

## G1008

[SideCopy](https://attack.mitre.org/groups/G1008) is a Pakistani threat group that has primarily targeted South Asian countries, including Indian and Afghani government personnel, since at least 2019. [SideCopy](https://attack.mitre.org/groups/G1008)'s name comes from its infection chain that tries to mimic that of [Sidewinder](https://attack.mitre.org/groups/G0121), a suspected Indian threat group.[^1] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[System Location Discovery\|T1614]] | System Location Discovery | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the country location of a compromised host.[^1]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [SideCopy](https://attack.mitre.org/groups/G1008) uses a loader DLL file to collect AV product names from an infected host.[^1]  |
| [[Domains\|T1584.001]] | Domains | [SideCopy](https://attack.mitre.org/groups/G1008) has compromised domains for some of their infrastructure, including for C2 and staging malware.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [SideCopy](https://attack.mitre.org/groups/G1008) has delivered trojanized executables via spearphishing emails that contacts actor-controlled servers to download malicious payloads.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the IP address of a compromised host.[^1]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [SideCopy](https://attack.mitre.org/groups/G1008) has used compromised domains to host its malicious payloads.[^1]  |
| [[Native API\|T1106]] | Native API |  [SideCopy](https://attack.mitre.org/groups/G1008) has executed malware by calling the API function `CreateProcessW`.[^1]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [SideCopy](https://attack.mitre.org/groups/G1008) has sent Microsoft Office Publisher documents to victims that have embedded malicious macros that execute an hta file via calling `mshta.exe`.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [SideCopy](https://attack.mitre.org/groups/G1008) has collected browser information from a compromised host.[^1]  |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [SideCopy](https://attack.mitre.org/groups/G1008) has sent spearphishing emails with malicious hta file attachments.[^1]  |
| [[DLL\|T1574.001]] | DLL | [SideCopy](https://attack.mitre.org/groups/G1008) has used a malicious loader DLL file to execute the `credwiz.exe` process and side-load the malicious payload `Duser.dll`.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [SideCopy](https://attack.mitre.org/groups/G1008) has attempted to lure victims into clicking on malicious embedded archive files sent via spearphishing campaigns.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [SideCopy](https://attack.mitre.org/groups/G1008) has identified the OS version of a compromised host.[^1]  |
| [[Spearphishing Attachment\|T1598.002]] | Spearphishing Attachment | [SideCopy](https://attack.mitre.org/groups/G1008) has crafted generic lures for spam campaigns to collect emails and credentials for targeting efforts.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [SideCopy](https://attack.mitre.org/groups/G1008) has used a legitimate DLL file name, `Duser.dll` to disguise a malicious remote access tool.[^1]  |
| [[Mshta\|T1218.005]] | Mshta | [SideCopy](https://attack.mitre.org/groups/G1008) has utilized `mshta.exe` to execute a malicious hta file.[^1]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Action RAT\|S1028]] | Action RAT |  |
| [[AuTo Stealer\|S1029]] | AuTo Stealer |  |



## References

[^1]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)


