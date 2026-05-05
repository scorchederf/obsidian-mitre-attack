---
aliases: 
    - S0352
    
mitre-attack: https://attack.mitre.org/software/S0352
---

## S0352

[OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) is a macOS backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First discovered in 2015, [APT32](https://attack.mitre.org/groups/G0050) has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can also determine it's permission level and execute according to access type (`root` or `user`).[^6] [^2] [^8] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) encrypts its strings in RSA256 and encodes them in a custom base64 scheme and XOR.[^2]  |
| [[Non-Application Layer Protocol\|T1095]] | Non-Application Layer Protocol | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used a custom binary protocol over port 443 for C2 traffic.[^6]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has changed permissions of a second-stage payload to an executable via `chmod`.[^3]  |
| [[File Deletion\|T1070.004]] | File Deletion | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has a command to delete a file from the system. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) deletes the app bundle and dropper after execution.[^2] [^8] [^6]  |
| [[System Network Configuration Discovery\|T1016]] | System Network Configuration Discovery | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can collect the network interface MAC address on the infected host.[^2] [^8]  |
| [[System Checks\|T1497.001]] | System Checks | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) checks a number of system parameters to see if it is being run on real hardware or in a virtual machine environment, such as `sysctl hw.model` and the kernel boot time.[^6] [^4] [^9]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) encrypts data sent back to the C2 using AES in CBC mode with a null initialization vector (IV) and a key sent from the server that is padded to 32 bytes.[^6]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses a decode routine combining bit shifting and XOR operations with a variable key that depends on the length of the string that was encoded. If the computation for the variable XOR key turns out to be 0, the default XOR key of 0x1B is used. This routine is also referenced as the `rotate` function in reporting.[^6]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses a shell script as the main executable inside an app bundle and drops an embedded base64-encoded payload to the `/tmp` folder.[^8] [^3]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) collects processor information, memory information, computer name, hardware UUID, serial number, and operating system version. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used the `ioreg` command to gather some of this information.[^2] [^8] [^9]  |
| [[Non-Standard Port\|T1571]] | Non-Standard Port | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used a custom binary protocol over TCP port 443 for C2.[^6]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can create a persistence file in the folder `/Library/LaunchAgents`.[^2] [^8]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has a command to download and execute a file on the victim’s machine.[^2] [^8]  |
| [[Visual Basic\|T1059.005]] | Visual Basic | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses Word macros for execution.[^2]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) sets the main loader file’s attributes to hidden.[^2]  |
| [[Timestomp\|T1070.006]] | Timestomp | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can use the `touch -t` command to change timestamps.[^8] [^9]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can also use use HTTP POST and GET requests to send and receive C2 information.[^8]  |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used `zlib` to compress all data after 0x52 for the custom TCP C2 protocol.[^6]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | If running with `root` permissions, [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can create a persistence file in the folder `/Library/LaunchDaemons`.[^2] [^3]  |
| [[Software Packing\|T1027.002]] | Software Packing | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has a variant that is packed with UPX.[^4]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) scrambles and encrypts data using AES256 before sending it to the C2 server.[^2] [^8]  |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses file naming conventions with associated executable locations to blend in with the macOS TimeMachine and OpenSSL services. Such as, naming a LaunchAgent plist file `com.apple.openssl.plist` which executes [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) from the user's `~/Library/OpenSSL/` folder upon user login.[^6]  |
| [[Data from Local System\|T1005]] | Data from Local System | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has the ability to upload files from a compromised host.[^8]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has used AES in CBC mode to encrypt collected data when saving that data to disk.[^6]  |
| [[Shared Modules\|T1129]] | Shared Modules | For network communications, [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) loads a dynamic library (`.dylib` file) using `dlopen()` and obtains a function pointer to execute within that shared library using `dlsym()`.[^6]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses the command `xattr -d com.apple.quarantine` to remove the quarantine file attribute used by Gatekeeper.[^8] [^9]  |
| [[PowerShell\|T1059.001]] | PowerShell | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) uses PowerShell scripts.[^2]  |
| [[Masquerade File Type\|T1036.008]] | Masquerade File Type | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) has disguised it's true file structure as an application bundle by adding special characters to the filename and using the icon for legitimate Word documents.[^8]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT32\|G0050]] | APT32 |



## References

[^1]: OSX_OCEANLOTUS.D


[^2]: [TrendMicro MacOS April 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)


[^3]: [sentinelone apt32 macOS backdoor 2020](https://www.sentinelone.com/labs/apt32-multi-stage-macos-trojan-innovates-on-crimeware-scripting-technique/)


[^4]: [ESET OceanLotus macOS April 2019](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)


[^5]: Backdoor.MacOS.OCEANLOTUS.F


[^6]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)


[^7]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)


[^8]: [Trend Micro MacOS Backdoor November 2020](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)


[^9]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


