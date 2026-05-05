---
aliases: 
    - S1078
    
mitre-attack: https://attack.mitre.org/software/S1078
---

## S1078

[RotaJakiro](https://attack.mitre.org/software/S1078) is a 64-bit Linux backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First seen in 2018, it uses a plugin architecture to extend capabilities. [RotaJakiro](https://attack.mitre.org/software/S1078) can determine it's permission level and execute according to access type (`root` or `user`).[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RotaJakiro](https://attack.mitre.org/software/S1078) uses the AES algorithm, bit shifts in a function called `rotate`, and an XOR cipher to decrypt resources required for persistence, process guarding, and file locking. It also performs this same function on encrypted stack strings and the `head` and `key` sections in the network packet structure used for C2 communications.[^1]  |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | When executing with non-root level permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) can install persistence by adding a command to the .bashrc file that executes a binary in the  `${HOME}/.gvfsd/.profile/` folder.[^1]  |
| [[Native API\|T1106]] | Native API | When executing with non-root permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) uses the the `shmget` API to create shared memory between other known [RotaJakiro](https://attack.mitre.org/software/S1078) processes. [RotaJakiro](https://attack.mitre.org/software/S1078) also uses the `execvp` API to help its dead process "resurrect".[^1]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [RotaJakiro](https://attack.mitre.org/software/S1078) uses ZLIB Compression to compresses data sent to the C2 server in the `payload` section network communication packet.[^1]  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | Depending on the Linux distribution and when executing with root permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) may install persistence using a `.conf` file in the `/etc/init/` folder.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [RotaJakiro](https://attack.mitre.org/software/S1078) executes a set of commands to collect device information, including `uname`.  Another example is the `cat /etc/*release | uniq` command used to collect the current OS distribution.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | Depending on the Linux distribution and when executing with root permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) may install persistence using a `.service` file under the `/lib/systemd/system/` folder.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [RotaJakiro](https://attack.mitre.org/software/S1078) uses dynamically linked shared libraries (`.so` files) to execute additional functionality using `dlopen()` and `dlsym()`.[^1]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [RotaJakiro](https://attack.mitre.org/software/S1078) uses a custom binary protocol over TCP port 443.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [RotaJakiro](https://attack.mitre.org/software/S1078) uses a custom binary protocol using a type, length, value format over TCP.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [RotaJakiro](https://attack.mitre.org/software/S1078) has used the filename `systemd-daemon` in an attempt to appear legitimate.[^2]  |
| [[Inter-Process Communication\|T1559]] | Inter-Process Communication | When executing with non-root permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) uses the the `shmget API` to create shared memory between other known [RotaJakiro](https://attack.mitre.org/software/S1078) processes. This allows processes to communicate with each other and share their PID.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [RotaJakiro](https://attack.mitre.org/software/S1078) can monitor the `/proc/[PID]` directory of known [RotaJakiro](https://attack.mitre.org/software/S1078) processes as a part of its persistence when executing with non-root permissions. If the process is found dead, it resurrects the process. [RotaJakiro](https://attack.mitre.org/software/S1078) processes can be matched to an associated Advisory Lock, in the `/proc/locks` folder, to ensure it doesn't spawn more than one process.[^1]  |
| [[Automated Collection\|T1119]] | Automated Collection | Depending on the Linux distribution, [RotaJakiro](https://attack.mitre.org/software/S1078) executes a set of commands to collect device information and sends the collected information to the C2 server.[^1]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | When executing with user-level permissions, [RotaJakiro](https://attack.mitre.org/software/S1078) can install persistence using a .desktop file under the `$HOME/.config/autostart/` folder.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [RotaJakiro](https://attack.mitre.org/software/S1078) sends device and other collected data back to the C2 using the established C2 channels over TCP. [^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [RotaJakiro](https://attack.mitre.org/software/S1078) encrypts C2 communication using a combination of AES, XOR, ROTATE encryption, and ZLIB compression.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)


[^2]: [netlab360 rotajakiro vs oceanlotus](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)


