---
aliases: 
    - S0487
    
mitre-attack: https://attack.mitre.org/software/S0487
---

## S0487

[Kessel](https://attack.mitre.org/software/S0487) is an advanced version of OpenSSH which acts as a custom backdoor, mainly acting to steal credentials and function as a bot. [Kessel](https://attack.mitre.org/software/S0487) has been active since its C2 domain began resolving in August 2018.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Kessel](https://attack.mitre.org/software/S0487)'s configuration is hardcoded and RC4 encrypted within the binary.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Kessel](https://attack.mitre.org/software/S0487) can download additional modules from the C2 server.[^1]  |
| [[Data Transfer Size Limits\|T1030]] | Data Transfer Size Limits | [Kessel](https://attack.mitre.org/software/S0487) can split the data to be exilftrated into chunks that will fit in subdomains of DNS queries.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Kessel](https://attack.mitre.org/software/S0487) can create a reverse shell between the infected host and a specified system.[^1] 	 |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Kessel](https://attack.mitre.org/software/S0487) has decrypted the binary's configuration once the `main` function was launched.[^1]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [Kessel](https://attack.mitre.org/software/S0487) has collected the DNS address of the infected host.[^1]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [Kessel](https://attack.mitre.org/software/S0487) has maliciously altered the OpenSSH binary on targeted systems to create a backdoor.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Kessel](https://attack.mitre.org/software/S0487) has collected the system architecture, OS version, and MAC address information.[^1]  |
| [[Proxy\|T1090]] | Proxy | [Kessel](https://attack.mitre.org/software/S0487) can use a proxy during exfiltration if set in the configuration.[^1]  |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | [Kessel](https://attack.mitre.org/software/S0487) has trojanized the <sode>ssh_login` and `user-auth_pubkey` functions to steal plaintext credentials.[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Kessel](https://attack.mitre.org/software/S0487) has exfiltrated data via hexadecimal-encoded subdomain fields of DNS queries.[^1]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [Kessel](https://attack.mitre.org/software/S0487) can RC4-encrypt credentials before sending to the C2.[^1] 	 |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Kessel](https://attack.mitre.org/software/S0487) has exfiltrated information gathered from the infected system to the C2 server.[^1]  |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [Kessel](https://attack.mitre.org/software/S0487) can exfiltrate credentials and other information via HTTP POST request, TCP, and DNS.[^1]  |




## References

[^1]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)


