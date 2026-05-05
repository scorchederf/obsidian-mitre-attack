---
aliases: 
    - S1113
    
mitre-attack: https://attack.mitre.org/software/S1113
---

## S1113

[RAPIDPULSE](https://attack.mitre.org/software/S1113) is a web shell that exists as a modification to a legitimate Pulse Secure file that has been used by [APT5](https://attack.mitre.org/groups/G1023) since at least 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [RAPIDPULSE](https://attack.mitre.org/software/S1113) listens for specific HTTP query parameters in received communications. If specific parameters match, a hard-coded RC4 key is used to decrypt the HTTP query paremter `hmacTime`. This decrypts to a filename that is then open, read, encrypted with the same RC4 key, base64-encoded, written to standard out, then passed as a response to the HTTP request.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [RAPIDPULSE](https://attack.mitre.org/software/S1113) retrieves files from the victim system via encrypted commands sent to the web shell.[^1]  |
| [[Web Shell\|T1505.003]] | Web Shell | [RAPIDPULSE](https://attack.mitre.org/software/S1113) is a web shell that is capable of arbitrary file read on targeted web servers to exfiltrate items of interest on the victim device.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [RAPIDPULSE](https://attack.mitre.org/software/S1113) has the ability to RC4 encrypt and base64 encode decrypted files on compromised servers prior to writing them to stdout.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT5\|G1023]] | APT5 |



## References

[^1]: [Mandiant Pulse Secure Update May 2021](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)


