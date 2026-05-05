---
aliases: 
    - S0179
    
mitre-attack: https://attack.mitre.org/software/S0179
---

## S0179

[MimiPenguin](https://attack.mitre.org/software/S0179) is a credential dumper, similar to [Mimikatz](https://attack.mitre.org/software/S0002), designed specifically for Linux platforms. [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Proc Filesystem\|T1003.007]] | Proc Filesystem | [MimiPenguin](https://attack.mitre.org/software/S0179) can use the `<PID>/maps` and `<PID>/mem` file to search for regex patterns and dump the process memory.[^2] [^3]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TeamTNT\|G0139]] | TeamTNT |



## References

[^1]: [Palo Alto Black-T October 2020](https://unit42.paloaltonetworks.com/black-t-cryptojacking-variant/)


[^2]: [MimiPenguin GitHub May 2017](https://github.com/huntergregal/mimipenguin)


[^3]: [Picus Labs Proc cump 2022](https://www.picussecurity.com/resource/the-mitre-attck-t1003-os-credential-dumping-technique-and-its-adversary-use)


