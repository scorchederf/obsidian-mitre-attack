---
aliases: 
    - S0377
    
mitre-attack: https://attack.mitre.org/software/S0377
---

## S0377

[Ebury](https://attack.mitre.org/software/S0377) is an OpenSSH backdoor and credential stealer targeting Linux servers and container hosts developed by [Windigo](https://attack.mitre.org/groups/G0124). [Ebury](https://attack.mitre.org/software/S0377) is primarily installed through modifying shared libraries (`.so` files) executed by the legitimate OpenSSH program. First seen in 2009, [Ebury](https://attack.mitre.org/software/S0377) has been used to maintain a botnet of servers, deploy additional malware, and steal cryptocurrency wallets, credentials, and credit card details.[^5] [^3] [^4] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Rootkit\|T1014]] | Rootkit | [Ebury](https://attack.mitre.org/software/S0377) acts as a user land rootkit using the SSH service.[^4] [^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Ebury](https://attack.mitre.org/software/S0377) can use the commands `Xcsh` or `Xcls` to open a shell with [Ebury](https://attack.mitre.org/software/S0377) level permissions and `Xxsh` to open a shell with root level.[^2]  |
| [[Pluggable Authentication Modules\|T1556.003]] | Pluggable Authentication Modules | [Ebury](https://attack.mitre.org/software/S0377) can deactivate PAM modules to tamper with the sshd configuration.[^4]  |
| [[DNS\|T1071.004]] | DNS | [Ebury](https://attack.mitre.org/software/S0377) has used DNS requests over UDP port 53 for C2.[^5] 	 |
| [[Fallback Channels\|T1008]] | Fallback Channels | [Ebury](https://attack.mitre.org/software/S0377) has implemented a fallback mechanism to begin using a DGA when the attacker hasn't connected to the infected system for three days.[^4]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Ebury](https://attack.mitre.org/software/S0377) has verified C2 domain ownership by decrypting the TXT record using an embedded RSA public key.[^4]  |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | [Ebury](https://attack.mitre.org/software/S0377) can intercept private keys using a trojanized `ssh-add` function.[^5]  |
| [[Automated Exfiltration\|T1020]] | Automated Exfiltration | If credentials are not collected for two weeks, [Ebury](https://attack.mitre.org/software/S0377) encrypts the credentials using a public key and sends them via UDP to an IP address located in the DNS TXT record.[^6] [^2]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [Ebury](https://attack.mitre.org/software/S0377) has encrypted C2 traffic using the client IP address, then encoded it as a hexadecimal string.[^5]  |
| [[Disable or Modify Linux Audit System Log\|T1685.004]] | Disable or Modify Linux Audit System Log | [Ebury](https://attack.mitre.org/software/S0377) disables OpenSSH, system (`systemd`), and audit logs (`/sbin/auditd`) when the backdoor is active.[^2]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [Ebury](https://attack.mitre.org/software/S0377) modifies the `keyutils` library to add malicious behavior to the OpenSSH client and the curl library.[^5] [^2]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Ebury](https://attack.mitre.org/software/S0377) has obfuscated its strings with a simple XOR encryption with a static key.[^5]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Ebury](https://attack.mitre.org/software/S0377) can disable SELinux Role-Based Access Control and deactivate PAM modules.[^4]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Ebury](https://attack.mitre.org/software/S0377) has encoded C2 traffic in hexadecimal format.[^5] 	 |
| [[Python\|T1059.006]] | Python | [Ebury](https://attack.mitre.org/software/S0377) has used Python to implement its DGA.[^4] 	 |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | When [Ebury](https://attack.mitre.org/software/S0377) is running as an OpenSSH server, it uses LD_PRELOAD to inject its malicious shared module in to programs launched by SSH sessions. [Ebury](https://attack.mitre.org/software/S0377) hooks the following functions from `libc` to inject into subprocesses;  `system`, `popen`, `execve`, `execvpe`, `execv`, `execvp`, and `execl`.[^4] [^2]  |
| [[Shared Modules\|T1129]] | Shared Modules | [Ebury](https://attack.mitre.org/software/S0377) is executed through hooking the keyutils.so file used by legitimate versions of `OpenSSH` and `libcurl`.[^2]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Ebury](https://attack.mitre.org/software/S0377) has installed a self-signed RPM package mimicking the original system package on RPM based systems.[^5]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Ebury](https://attack.mitre.org/software/S0377) has intercepted unencrypted private keys as well as private key pass-phrases.[^5] 	 |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Ebury](https://attack.mitre.org/software/S0377) exfiltrates a list of outbound and inbound SSH sessions using OpenSSH's `known_host` files and `wtmp` records. [Ebury](https://attack.mitre.org/software/S0377) can exfiltrate SSH credentials through custom DNS queries or use the command `Xcat` to send the process's ssh session's credentials to the C2 server.[^6] [^2]   |
| [[Domain Generation Algorithms\|T1568.002]] | Domain Generation Algorithms | [Ebury](https://attack.mitre.org/software/S0377) has used a DGA to generate a domain name for C2.[^5] [^4]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Windigo\|G0124]] | Windigo |



## References

[^1]: Ebury


[^2]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)


[^3]: [BleepingComputer Ebury March 2017](https://www.bleepingcomputer.com/news/security/russian-hacker-pleads-guilty-for-role-in-infamous-linux-ebury-malware/)


[^4]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)


[^5]: [ESET Ebury Feb 2014](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)


[^6]: [ESET Windigo Mar 2014](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)


