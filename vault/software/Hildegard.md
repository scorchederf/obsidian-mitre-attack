---
aliases: 
    - S0601
    
mitre-attack: https://attack.mitre.org/software/S0601
---

## S0601

[Hildegard](https://attack.mitre.org/software/S0601) is malware that targets misconfigured kubelets for initial access and runs cryptocurrency miner operations. The malware was first observed in January 2021. The TeamTNT activity group is believed to be behind [Hildegard](https://attack.mitre.org/software/S0601). [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [Hildegard](https://attack.mitre.org/software/S0601) has used an IRC channel for C2 communications.[^1]  |
| [[Private Keys\|T1552.004]] | Private Keys | [Hildegard](https://attack.mitre.org/software/S0601) has searched for private keys in .ssh.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [Hildegard](https://attack.mitre.org/software/S0601) has deleted scripts after execution.[^1]   |
| [[Container Administration Command\|T1609]] | Container Administration Command | [Hildegard](https://attack.mitre.org/software/S0601) was executed through the kubelet API run command and by executing commands on running containers.[^1]  |
| [[Container and Resource Discovery\|T1613]] | Container and Resource Discovery | [Hildegard](https://attack.mitre.org/software/S0601) has used masscan to search for kubelets and the kubelet API for additional running containers.[^1]   |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [Hildegard](https://attack.mitre.org/software/S0601) has modified /etc/ld.so.preload to intercept shared library import functions.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Hildegard](https://attack.mitre.org/software/S0601) has used masscan to look for kubelets in the internal Kubernetes network.[^1]  |
| [[External Remote Services\|T1133]] | External Remote Services | [Hildegard](https://attack.mitre.org/software/S0601) was executed through an unsecure kubelet that allowed anonymous access to the victim environment.[^1]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Hildegard](https://attack.mitre.org/software/S0601) has searched for SSH keys, Docker credentials, and Kubernetes service tokens.[^1]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Hildegard](https://attack.mitre.org/software/S0601) has packed ELF files into other binaries.[^1]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Hildegard](https://attack.mitre.org/software/S0601) has disguised itself as a known Linux process.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Hildegard](https://attack.mitre.org/software/S0601) has collected the host's OS, CPU, and memory information.[^1]  |
| [[Web Service\|T1102]] | Web Service | [Hildegard](https://attack.mitre.org/software/S0601) has downloaded scripts from GitHub.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Hildegard](https://attack.mitre.org/software/S0601) has modified DNS resolvers to evade DNS monitoring tools.[^1]  |
| [[Rootkit\|T1014]] | Rootkit | [Hildegard](https://attack.mitre.org/software/S0601) has modified /etc/ld.so.preload to overwrite readdir() and readdir64().[^1]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [Hildegard](https://attack.mitre.org/software/S0601) has used history -c to clear script shell logs.[^1]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [Hildegard](https://attack.mitre.org/software/S0601) has established tmate sessions for C2 communications.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Hildegard](https://attack.mitre.org/software/S0601) has decrypted ELF files with AES.[^1]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [Hildegard](https://attack.mitre.org/software/S0601) has used xmrig to mine cryptocurrency.[^1]  |
| [[Local Account\|T1136.001]] | Local Account | [Hildegard](https://attack.mitre.org/software/S0601) has created a user named “monerodaemon”.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Hildegard](https://attack.mitre.org/software/S0601) has downloaded additional scripts that build and run Monero cryptocurrency miners.[^1]  |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | [Hildegard](https://attack.mitre.org/software/S0601) has queried the Cloud Instance Metadata API for cloud credentials.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Hildegard](https://attack.mitre.org/software/S0601) has encrypted an ELF file.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Hildegard](https://attack.mitre.org/software/S0601) has started a monero service.[^1]  |
| [[Escape to Host\|T1611]] | Escape to Host | [Hildegard](https://attack.mitre.org/software/S0601) has used the BOtB tool that can break out of containers. [^1]   |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [Hildegard](https://attack.mitre.org/software/S0601) has used the BOtB tool which exploits CVE-2019-5736.[^1]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Hildegard](https://attack.mitre.org/software/S0601) has used shell scripts for execution.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TeamTNT\|G0139]] | TeamTNT |



## References

[^1]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)


