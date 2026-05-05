---
aliases: 
    - S0009
    
mitre-attack: https://attack.mitre.org/software/S0009
---

## S0009

[Hikit](https://attack.mitre.org/software/S0009) is malware that has been used by [Axiom](https://attack.mitre.org/groups/G0001) for late-stage persistence and exfiltration after the initial compromise.[^3] [^5] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Phishing\|T1566]] | Phishing | [Hikit](https://attack.mitre.org/software/S0009) has been spread through spear phishing.[^3]  |
| [[DLL\|T1574.001]] | DLL | [Hikit](https://attack.mitre.org/software/S0009) has used [DLL](https://attack.mitre.org/techniques/T1574/001) to load `oci.dll` as a persistence mechanism.[^5]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Hikit](https://attack.mitre.org/software/S0009) performs XOR encryption.[^3]  |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | [Hikit](https://attack.mitre.org/software/S0009) has attempted to disable driver signing verification by tampering with several Registry keys prior to the loading of a rootkit driver component.[^4]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Hikit](https://attack.mitre.org/software/S0009) has the ability to create a remote shell and run given commands.[^4]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Hikit](https://attack.mitre.org/software/S0009) has used HTTP for C2.[^4]  |
| [[Install Root Certificate\|T1553.004]] | Install Root Certificate | [Hikit](https://attack.mitre.org/software/S0009) installs a self-generated certificate to the local trust store as a root CA and Trusted Publisher.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Hikit](https://attack.mitre.org/software/S0009) is a [Rootkit](https://attack.mitre.org/techniques/T1014) that has been used by [Axiom](https://attack.mitre.org/groups/G0001).[^5]  [^4]   |
| [[Internal Proxy\|T1090.001]] | Internal Proxy | [Hikit](https://attack.mitre.org/software/S0009) supports peer connections.[^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | [Hikit](https://attack.mitre.org/software/S0009) can upload files from compromised machines.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hikit](https://attack.mitre.org/software/S0009) has the ability to download files to a compromised host.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Axiom\|G0001]] | Axiom |



## References

[^1]: [Sood and Enbody](https://www.techtarget.com/searchsecurity/feature/Targeted-Cyber-Attacks)


[^2]: [Cisco Group 72](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)


[^3]: [Novetta-Axiom](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)


[^4]: [FireEye HIKIT Rootkit Part 2](https://web.archive.org/web/20210920172620/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-2.html)


[^5]: [FireEye Hikit Rootkit](https://web.archive.org/web/20190216180458/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-1.html)


