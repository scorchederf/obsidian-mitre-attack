---
aliases: 
    - S1048
    
mitre-attack: https://attack.mitre.org/software/S1048
---

## S1048

[macOS.OSAMiner](https://attack.mitre.org/software/S1048) is a Monero mining trojan that was first observed in 2018; security researchers assessed [macOS.OSAMiner](https://attack.mitre.org/software/S1048) may have been circulating since at least 2015. [macOS.OSAMiner](https://attack.mitre.org/software/S1048) is known for embedding one run-only AppleScript into another, which helped the malware evade full analysis for five years due to a lack of Apple event (AEVT) analysis tools.[^1] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has searched for the Activity Monitor process in the System Events process list and kills the process if running. [macOS.OSAMiner](https://attack.mitre.org/software/S1048) also searches the operating system's `install.log` for apps matching its hardcoded list, killing all matching process names.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `curl` to download a [Stripped Payloads](https://attack.mitre.org/techniques/T1027/008) from a public facing adversary-controlled webpage.  |
| [[Local Storage Discovery\|T1680]] | Local Storage Discovery | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has checked to ensure there is enough disk space using the Unix utility `df`.[^1]  |
| [[System Checks\|T1497.001]] | System Checks | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) can parse the output of the native `system_profiler` tool to determine if the machine is running with 4 cores.[^1]  |
| [[Stripped Payloads\|T1027.008]] | Stripped Payloads | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used run-only Applescripts, a compiled and stripped version of [AppleScript](https://attack.mitre.org/techniques/T1059/002), to remove human readable indicators to evade detection.[^1]  |
| [[Embedded Payloads\|T1027.009]] | Embedded Payloads | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has embedded [Stripped Payloads](https://attack.mitre.org/techniques/T1027/008) within another run-only [Stripped Payloads](https://attack.mitre.org/techniques/T1027/008).[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) can gather the device serial number.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has placed a [Stripped Payloads](https://attack.mitre.org/techniques/T1027/008) with a `plist` extension in the [Launch Agent](https://attack.mitre.org/techniques/T1543/001)'s folder. [^1]  |
| [[Launchctl\|T1569.001]] | Launchctl | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `launchctl` to restart the [Launch Agent](https://attack.mitre.org/techniques/T1543/001).[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `ps ax | grep <name> | grep -v grep | ...` and `ps ax | grep -E...` to conduct process discovery.[^1]  |
| [[AppleScript\|T1059.002]] | AppleScript | [macOS.OSAMiner](https://attack.mitre.org/software/S1048) has used `osascript` to call itself via the `do shell script` command in the [Launch Agent](https://attack.mitre.org/techniques/T1543/001) `.plist` file.[^1]  |




## References

[^1]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)


[^2]: [VMRay OSAMiner dynamic analysis 2021](https://www.vmray.com/cyber-security-blog/osaminer-uses-applescripts-evade-detection-malware-analysis-spotlight/)


