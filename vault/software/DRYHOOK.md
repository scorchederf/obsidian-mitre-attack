---
aliases: 
    - S9013
    
mitre-attack: https://attack.mitre.org/software/S9013
---

## S9013

[DRYHOOK](https://attack.mitre.org/software/S9013) is Python script used to steal credentials. [DRYHOOK](https://attack.mitre.org/software/S9013) was first reported in January 2025, and has previously been leveraged by People's Republic of China (PRC) state-affiliated threat actors identified as UNC5221 and SYLVANITE.[^3] [^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [DRYHOOK](https://attack.mitre.org/software/S9013) has the ability to remount the filesystem as “read-write” to make changes and then restores it to “read-only” prior to killing processes to apply the modifications.[^1] [^2]  |
| [[Keylogging\|T1056.001]] | Keylogging | [DRYHOOK](https://attack.mitre.org/software/S9013) has captured user credentials and passwords in plaintext and has encrypted them in a stored file on the network device.[^1] [^2]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [DRYHOOK](https://attack.mitre.org/software/S9013) has stored stolen credentials for future use in the temp folder of a victimized Ivanti Connect Secure VPN device, specifically in the file location `/tmp/cmmmap.kumMW`.[^1] [^2]  |
| [[Network Device CLI\|T1059.008]] | Network Device CLI | [DRYHOOK](https://attack.mitre.org/software/S9013) has the ability to interact with Ivanti Connect Secure environments and to modify system components.[^1] [^2]  |
| [[Modify System Image\|T1601]] | Modify System Image | [DRYHOOK](https://attack.mitre.org/software/S9013) has modified the Ivanti Connect Secure VPN authentication Perl module `DSAuth.pm` by reading its contents in the buffer, then finding and replacing select lines of code.[^1] [^2]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [DRYHOOK](https://attack.mitre.org/software/S9013) has killed all instances of the `cgi-server` process in order for the modified Perl module to be activated.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [DRYHOOK](https://attack.mitre.org/software/S9013) has encrypted stolen credentials strings within a file using both Base64 and RC4 with a hard-coded key.[^1] [^2]  |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | [DRYHOOK](https://attack.mitre.org/software/S9013) has intercepted and logged user credentials by modifying the Perl module in Ivanti Connect Secure VPN edge-devices located within `/home/perl/DSAuth.pm`.[^1] [^2]  |
| [[Python\|T1059.006]] | Python | [DRYHOOK](https://attack.mitre.org/software/S9013) is a Python-based script that executes within the victim environment.[^1] [^2]  |
| [[Service Stop\|T1489]] | Service Stop | [DRYHOOK](https://attack.mitre.org/software/S9013) has terminated all instances of the `cgi-server` process before activating the modified DSAuth.pm file.[^1]  |
| [[Network Device Authentication\|T1556.004]] | Network Device Authentication | [DRYHOOK](https://attack.mitre.org/software/S9013) has patched victim appliances authentication routines to capture credentials in plaintext as users log in.[^1]  |




## References

[^1]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)


[^2]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^3]: [Dragos SYLVANITE MuddyWater Electrum March 2026](https://hub.dragos.com/hubfs/2026_YIR_ExecutiveBriefing%20O_G.pdf?hsLang=en)


