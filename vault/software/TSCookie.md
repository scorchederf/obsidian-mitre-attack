---
aliases: 
    - S0436
    
mitre-attack: https://attack.mitre.org/software/S0436
---

## S0436

[TSCookie](https://attack.mitre.org/software/S0436) is a remote access tool (RAT) that has been used by [BlackTech](https://attack.mitre.org/groups/G0098) in campaigns against Japanese targets.[^3] [^1] . [TSCookie](https://attack.mitre.org/software/S0436) has been referred to as [PLEAD](https://attack.mitre.org/software/S0435) though more recent reporting indicates a separation between the two.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to execute shell commands on the infected host.[^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to list processes on the infected host.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to upload and download files to and from the infected host.[^3]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [TSCookie](https://attack.mitre.org/software/S0436) can use ICMP to receive information on the destination server.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TSCookie](https://attack.mitre.org/software/S0436) can multiple protocols including HTTP and HTTPS in communication with command and control (C2) servers.[^1] [^3]  |
| [[Process Injection\|T1055]] | Process Injection | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to inject code into the svchost.exe, iexplorer.exe, explorer.exe, and default browser processes.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to decrypt, load, and execute a DLL and its resources.[^3]  |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to steal saved passwords from the Internet Explorer, Edge, Firefox, and Chrome browsers.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to discover drive information on the infected host.[^3]  |
| [[Proxy\|T1090]] | Proxy | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to proxy communications with command and control (C2) servers.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [TSCookie](https://attack.mitre.org/software/S0436) has encrypted network communications with RC4.[^3]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [TSCookie](https://attack.mitre.org/software/S0436) has the ability to identify the IP of the infected host.[^3]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [TSCookie](https://attack.mitre.org/software/S0436) has been executed via malicious links embedded in e-mails spoofing the Ministries of Education, Culture, Sports, Science and Technology of Japan.[^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[BlackTech\|G0098]] | BlackTech |



## References

[^1]: [JPCert BlackTech Malware September 2019](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)


[^2]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


[^3]: [JPCert TSCookie March 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)


