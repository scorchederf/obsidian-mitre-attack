---
aliases: 
    - S9012
    
mitre-attack: https://attack.mitre.org/software/S9012
---

## S9012

[TRAILBLAZE](https://attack.mitre.org/software/S9012) is an in-memory dropper used to deploy the passive backdoor [BRUSHFIRE](https://attack.mitre.org/software/S9011). First reported in March 2025, TRAILBLAZE has been observed in operations attributed to People's Republic of China (PRC) state-sponsored affiliated actors, including UNC5221 and SYLVANITE. [^3] [^2] [^1]   

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Process Discovery\|T1057]] | Process Discovery | [TRAILBLAZE](https://attack.mitre.org/software/S9012) has conducted process discovery by searching for specific named processes such as `/home/bin/web`.[^2] [^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [TRAILBLAZE](https://attack.mitre.org/software/S9012) has the ability to delete temporary files and contents in specified directories to cover its tracks.[^2] [^1]  |
| [[Process Hollowing\|T1055.012]] | Process Hollowing | [TRAILBLAZE](https://attack.mitre.org/software/S9012) has injected a hook into an existing process to load [BRUSHFIRE](https://attack.mitre.org/software/S9011) in the spaces allocated memory to include the Ivanti Connect Secure (ICS) web process named `web`.[^2] [^1]  |
| [[Native API\|T1106]] | Native API | [TRAILBLAZE](https://attack.mitre.org/software/S9012) has leveraged raw syscalls to execute commands.[^2] [^1]  |




## References

[^1]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)


[^2]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)


[^3]: [Dragos SYLVANITE MuddyWater Electrum March 2026](https://hub.dragos.com/hubfs/2026_YIR_ExecutiveBriefing%20O_G.pdf?hsLang=en)


