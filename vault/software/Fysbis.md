---
aliases: 
    - S0410
    
mitre-attack: https://attack.mitre.org/software/S0410
---

## S0410

[Fysbis](https://attack.mitre.org/software/S0410) is a Linux-based backdoor used by [APT28](https://attack.mitre.org/groups/G0007) that dates back to at least 2014.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Standard Encoding\|T1132.001]] | Standard Encoding | [Fysbis](https://attack.mitre.org/software/S0410) can use Base64 to encode its C2 traffic.[^2]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Fysbis](https://attack.mitre.org/software/S0410) has the ability to search for files.[^2]   |
| [[Keylogging\|T1056.001]] | Keylogging | [Fysbis](https://attack.mitre.org/software/S0410) can perform keylogging.[^1]   |
| [[Masquerade Task or Service\|T1036.004]] | Masquerade Task or Service | [Fysbis](https://attack.mitre.org/software/S0410) has masqueraded as the rsyncd and dbus-inotifier services.[^2]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Fysbis](https://attack.mitre.org/software/S0410) can collect information about running processes.[^2]   |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Fysbis](https://attack.mitre.org/software/S0410) has been encrypted using XOR and RC4.[^2]   |
| [[File Deletion\|T1070.004]] | File Deletion | [Fysbis](https://attack.mitre.org/software/S0410) has the ability to delete files.[^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Fysbis](https://attack.mitre.org/software/S0410) has used the command `ls /etc | egrep -e"fedora\*|debian\*|gentoo\*|mandriva\*|mandrake\*|meego\*|redhat\*|lsb-\*|sun-\*|SUSE\*|release"` to determine which Linux OS version is running.[^1]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Fysbis](https://attack.mitre.org/software/S0410) has established persistence using a systemd service.[^2]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Fysbis](https://attack.mitre.org/software/S0410) has masqueraded as trusted software rsyncd and dbus-inotifier.[^2]  |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | If executing without root privileges, [Fysbis](https://attack.mitre.org/software/S0410) adds a `.desktop` configuration file to the user's `~/.config/autostart` directory.[^3] [^2]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Fysbis](https://attack.mitre.org/software/S0410) has the ability to create and execute commands in a remote shell for CLI.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT28\|G0007]] | APT28 |



## References

[^1]: [Fysbis Palo Alto Analysis](https://researchcenter.paloaltonetworks.com/2016/02/a-look-into-fysbis-sofacys-linux-backdoor/)


[^2]: [Fysbis Dr Web Analysis](https://vms.drweb.com/virus/?i=4276269)


[^3]: [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)


