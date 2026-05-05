---
aliases: 
    - S9033
    
mitre-attack: https://attack.mitre.org/software/S9033
---

## S9033

[Fooder](https://attack.mitre.org/software/S9033) is a custom 64-bit C/C++ loader used by [MuddyWater](https://attack.mitre.org/groups/G0069) that can decrypt and reflectively load embedded payloads such as a go-socks5 proxy utility, the open-source HackBrowserData infostealer, or the [MuddyViper](https://attack.mitre.org/software/S9032) backdoor. [Fooder](https://attack.mitre.org/software/S9033) has frequently masqueraded as an entertainment executable, such as the Snake game (e.g., `Snake_Game.exe`).[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Fooder](https://attack.mitre.org/software/S9033) has stored its embedded payload in encrypted form within the binary, using a hardcoded key modified at runtime to produce the AES decryption key.[^1]  |
| [[Token Impersonation／Theft\|T1134.001]] | Token Impersonation／Theft | [Fooder](https://attack.mitre.org/software/S9033) has used the `DuplicateTokenEx` API to duplicate the token of a specified process, and `CreateProcessAsUserA` to execute its payload.[^1]        |
| [[Native API\|T1106]] | Native API | [Fooder](https://attack.mitre.org/software/S9033) has used the WinCrypt API for payload decryption, `DuplicateTokenEx` to duplicate the token of a specified process, and `CreateProcessAsUserA` for payload execution.[^1]          |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [Fooder](https://attack.mitre.org/software/S9033) has reflectively loaded a payload into memory.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Fooder](https://attack.mitre.org/software/S9033) has frequently masqueraded as the Snake game, using strings such as “Welcome to snake Game” and mutexes such as “SNAKE_G.”[^1]     |
| [[Delay Execution\|T1678]] | Delay Execution | [Fooder](https://attack.mitre.org/software/S9033) has used a custom delay function (`delayExecution(integer)`) and Sleep API calls (`Sleep(integer)`) to slow code execution.[^1]      |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Fooder](https://attack.mitre.org/software/S9033) has decrypted payloads using the WinCrypt API and the AES key.[^1]      |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[MuddyWater\|G0069]] | MuddyWater |



## References

[^1]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)


