---
aliases: 
    - TeamTNT
mitre-attack: https://attack.mitre.org/groups/G0139
---

## G0139

[TeamTNT](https://attack.mitre.org/groups/G0139) is a threat group that has primarily targeted cloud and containerized environments. The group as been active since at least October 2019 and has mainly focused its efforts on leveraging cloud and container resources to deploy cryptocurrency miners in victim environments.[^10] [^7] [^11] [^1] [^13] [^3] [^2] [^5] [^4] 

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for disk partition and logical volume information.[^2] [^12]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [TeamTNT](https://attack.mitre.org/groups/G0139) has disabled `iptables`.[^5]  |
| [[External Remote Services\|T1133]] | External Remote Services | [TeamTNT](https://attack.mitre.org/groups/G0139) has used open-source tools such as Weave Scope to target exposed Docker API ports and gain initial access to victim environments.[^11] [^12]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also targeted exposed kubelets for Kubernetes environments.[^13]  |
| [[Remote Access Tools\|T1219]] | Remote Access Tools | [TeamTNT](https://attack.mitre.org/groups/G0139) has established tmate sessions for C2 communications.[^13] [^12]  |
| [[Systemctl\|T1569.003]] | Systemctl | [TeamTNT](https://attack.mitre.org/groups/G0139) has created system services to execute cryptocurrency mining software.[^12]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [TeamTNT](https://attack.mitre.org/groups/G0139) has replaced .dockerd and .dockerenv with their own scripts and cryptocurrency mining software.[^12]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [TeamTNT](https://attack.mitre.org/groups/G0139) has modified the permissions on binaries with `chattr`.[^3] [^12]  |
| [[File Deletion\|T1070.004]] | File Deletion | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a payload that removes itself after running. [TeamTNT](https://attack.mitre.org/groups/G0139) also has deleted locally staged files for collecting credentials or scan results for local IP addresses after exfiltrating them.[^2] [^12]  |
| [[Container Administration Command\|T1609]] | Container Administration Command | [TeamTNT](https://attack.mitre.org/groups/G0139) executed [Hildegard](https://attack.mitre.org/software/S0601) through the kubelet API run command and by executing commands on running containers.[^13]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [TeamTNT](https://attack.mitre.org/groups/G0139) has used shell scripts for execution.[^3] [^12]  |
| [[Registry Run Keys ／ Startup Folder\|T1547.001]] | Registry Run Keys ／ Startup Folder | [TeamTNT](https://attack.mitre.org/groups/G0139) has added batch scripts to the startup folder.[^2]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has established persistence through the creation of a cryptocurrency mining system service using `systemctl`.[^3] [^12]  |
| [[Local Account\|T1136.001]] | Local Account | [TeamTNT](https://attack.mitre.org/groups/G0139) has created local privileged users on victim machines.[^11]  |
| [[System Service Discovery\|T1007]] | System Service Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for services such as Alibaba Cloud Security's aliyun service and BMC Helix Cloud Security's bmc-agent service in order to disable them.[^12]  |
| [[System Network Connections Discovery\|T1049]] | System Network Connections Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has run `netstat -anp` to search for rival malware connections.[^3]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also used `libprocesshider` to modify `/etc/ld.so.preload`.[^2]  |
| [[Windows Service\|T1543.003]] | Windows Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has used malware that adds cryptocurrency miners as a service.[^2]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [TeamTNT](https://attack.mitre.org/groups/G0139) has uploaded backdoored Docker images to Docker Hub.[^7]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [TeamTNT](https://attack.mitre.org/groups/G0139) has used batch scripts to download tools and executing cryptocurrency miners.[^2]  |
| [[Deploy Container\|T1610]] | Deploy Container | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed different types of containers into victim environments to facilitate execution.[^11] [^3]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also transferred cryptocurrency mining software to Kubernetes clusters discovered within local IP address ranges.[^12]  |
| [[Container and Resource Discovery\|T1613]] | Container and Resource Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has checked for running containers with `docker ps` and for specific container names with `docker inspect`.[^3]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also searched for Kubernetes pods running in a local network.[^12]  |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [TeamTNT](https://attack.mitre.org/groups/G0139) has sent locally staged files with collected credentials to C2 servers using cURL.[^12]  |
| [[Process Discovery\|T1057]] | Process Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for rival malware and removes it if found.[^3]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also searched for running processes containing the strings aliyun or liyun to identify machines running Alibaba Cloud Security tools.[^12]  |
| [[PowerShell\|T1059.001]] | PowerShell | [TeamTNT](https://attack.mitre.org/groups/G0139) has executed PowerShell commands in batch scripts.[^2]  |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | [TeamTNT](https://attack.mitre.org/groups/G0139) has queried the AWS instance metadata service for credentials.[^3] [^12]  |
| [[Clear Command History\|T1070.003]] | Clear Command History | [TeamTNT](https://attack.mitre.org/groups/G0139) has cleared command history with `history -c`.[^3] [^12]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [TeamTNT](https://attack.mitre.org/groups/G0139) has aggregated collected credentials in text files before exfiltrating.[^12]  |
| [[Vulnerability Scanning\|T1595.002]] | Vulnerability Scanning | [TeamTNT](https://attack.mitre.org/groups/G0139) has scanned for vulnerabilities in IoT devices and other related resources such as the Docker API.[^3]  |
| [[Container CLI／API\|T1059.013]] | Container CLI／API | TeamTNT targeted misconfigured containers and used container CLI tools.[^8]  |
| [[Software Packing\|T1027.002]] | Software Packing | [TeamTNT](https://attack.mitre.org/groups/G0139) has used UPX and Ezuri packer to pack its binaries.[^3]  |
| [[Malicious Image\|T1204.003]] | Malicious Image | [TeamTNT](https://attack.mitre.org/groups/G0139) has relied on users to download and execute malicious Docker images.[^7]  |
| [[Rootkit\|T1014]] | Rootkit | [TeamTNT](https://attack.mitre.org/groups/G0139) has used rootkits such as the open-source Diamorphine rootkit and their custom bots to hide cryptocurrency mining activities on the machine.[^3]  [^12]  |
| [[Private Keys\|T1552.004]] | Private Keys | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for unsecured SSH keys.[^1] [^3]  |
| [[Escape to Host\|T1611]] | Escape to Host | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed privileged containers that mount the filesystem of victim machine.[^11] [^5]  |
| [[Scanning IP Blocks\|T1595.001]] | Scanning IP Blocks | [TeamTNT](https://attack.mitre.org/groups/G0139) has scanned specific lists of target IP addresses.[^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [TeamTNT](https://attack.mitre.org/groups/G0139) has the `curl` and `wget` commands as well as batch scripts to download new tools.[^11] [^12]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for security products on infected machines.[^2] [^12]  |
| [[Compute Hijacking\|T1496.001]] | Compute Hijacking | [TeamTNT](https://attack.mitre.org/groups/G0139) has deployed XMRig Docker images to mine cryptocurrency.[^7] [^1]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also infected Docker containers and Kubernetes clusters with XMRig, and used RainbowMiner and lolMiner for mining cryptocurrency.[^12]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a script that checks `/proc/*/environ` for environment variables related to AWS.[^12]  |
| [[SSH\|T1021.004]] | SSH | [TeamTNT](https://attack.mitre.org/groups/G0139) has used SSH to connect back to victim machines.[^11]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also used SSH to transfer tools and payloads onto victim hosts and execute them.[^12]  |
| [[Masquerading\|T1036]] | Masquerading | [TeamTNT](https://attack.mitre.org/groups/G0139) has disguised their scripts with docker-related file names.[^12]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [TeamTNT](https://attack.mitre.org/groups/G0139) has used a script that decodes a Base64-encoded version of WeaveWorks Scope.[^12]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for system version, architecture, and hostname information.[^2] [^12]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [TeamTNT](https://attack.mitre.org/groups/G0139) has encrypted its binaries via AES and encoded files using Base64.[^3] [^5]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has enumerated the host machine’s IP address.[^3]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has used masscan to search for open Docker API ports and Kubernetes clusters.[^1] [^13] [^12]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also used malware that utilizes zmap and zgrab to search for vulnerable services in cloud environments.[^10]  |
| [[Peripheral Device Discovery\|T1120]] | Peripheral Device Discovery | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for attached VGA devices using lspci.[^12]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [TeamTNT](https://attack.mitre.org/groups/G0139) has disabled and uninstalled security tools such as Alibaba, Tencent, and BMC cloud monitoring agents on cloud-based infrastructure.[^2] [^12]  |
| [[Application Layer Protocol\|T1071]] | Application Layer Protocol | [TeamTNT](https://attack.mitre.org/groups/G0139) has used an IRC bot for C2 communications.[^3]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [TeamTNT](https://attack.mitre.org/groups/G0139) has added RSA keys in `authorized_keys`.[^5] [^12]  |
| [[Domains\|T1583.001]] | Domains | [TeamTNT](https://attack.mitre.org/groups/G0139) has obtained domains to host their payloads.[^10]  |
| [[Cloud API\|T1059.009]] | Cloud API | [TeamTNT](https://attack.mitre.org/groups/G0139) has leveraged AWS CLI to enumerate cloud environments with compromised credentials.[^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [TeamTNT](https://attack.mitre.org/groups/G0139) has the `curl` command to send credentials over HTTP and the `curl` and `wget` commands to download new software.[^11] [^1] [^12]  [TeamTNT](https://attack.mitre.org/groups/G0139) has also used a custom user agent HTTP header in shell scripts.[^3]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [TeamTNT](https://attack.mitre.org/groups/G0139) has searched for unsecured AWS credentials and Docker API credentials.[^1] [^3] [^12]  |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | [TeamTNT](https://attack.mitre.org/groups/G0139) has removed system logs from `/var/log/syslog`.[^5]  |
| [[Malware\|T1587.001]] | Malware | [TeamTNT](https://attack.mitre.org/groups/G0139) has developed custom malware such as [Hildegard](https://attack.mitre.org/software/S0601).[^13]  |
| [[Web Service\|T1102]] | Web Service | [TeamTNT](https://attack.mitre.org/groups/G0139) has leveraged iplogger.org to send collected data back to C2.[^5] [^12]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[MimiPenguin\|S0179]] | MimiPenguin | [^10]  |
| [[Peirates\|S0683]] | Peirates | [^6]  |
| [[LaZagne\|S0349]] | LaZagne | [^2]  |
| [[Hildegard\|S0601]] | Hildegard | [^13]  |



## References

[^1]: [Cado Security TeamTNT Worm August 2020](https://www.cadosecurity.com/team-tnt-the-first-crypto-mining-worm-to-steal-aws-credentials/)


[^2]: [ATT TeamTNT Chimaera September 2020](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)


[^3]: [Trend Micro TeamTNT](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)


[^4]: [Intezer TeamTNT Explosion September 2021](https://www.intezer.com/wp-content/uploads/2021/09/TeamTNT-Cryptomining-Explosion.pdf)


[^5]: [Aqua TeamTNT August 2020](https://blog.aquasec.com/container-security-tnt-container-attack)


[^6]: [TeamTNT Cloud Enumeration](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments)


[^7]: [Lacework TeamTNT May 2021](https://www.lacework.com/blog/taking-teamtnt-docker-images-offline)


[^8]: [Cisco Talos Blog](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^9]: [Talos TeamTNT](https://blog.talosintelligence.com/2022/04/teamtnt-targeting-aws-alibaba.html)


[^10]: [Palo Alto Black-T October 2020](https://unit42.paloaltonetworks.com/black-t-cryptojacking-variant/)


[^11]: [Intezer TeamTNT September 2020](https://www.intezer.com/blog/cloud-security/attackers-abusing-legitimate-cloud-monitoring-tools-to-conduct-cyber-attacks/)


[^12]: [Cisco Talos Intelligence Group](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)


[^13]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)


