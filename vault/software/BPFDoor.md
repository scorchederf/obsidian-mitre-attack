---
aliases: 
    - S1161
    
mitre-attack: https://attack.mitre.org/software/S1161
---

## S1161

[BPFDoor](https://attack.mitre.org/software/S1161) is a Linux based passive long-term backdoor used by China-based threat actors. First seen in 2021, [BPFDoor](https://attack.mitre.org/software/S1161) is named after its usage of Berkley Packet Filter (BPF) to execute single task instructions. [BPFDoor](https://attack.mitre.org/software/S1161) supports multiple protocols for communicating with a C2 including TCP, UDP, and ICMP and can start local or reverse shells that bypass firewalls using iptables.[^1] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Indicator Removal\|T1070]] | Indicator Removal | [BPFDoor](https://attack.mitre.org/software/S1161) clears the file location `/proc/<PID>/environ` removing all environment variables for the process.[^1]   |
| [[Mutual Exclusion\|T1480.002]] | Mutual Exclusion | When executed, [BPFDoor](https://attack.mitre.org/software/S1161) attempts to create and lock a runtime file, `/var/run/initd.lock`, and exits if it fails using the specified file, resulting in a makeshift mutex.[^4]  |
| [[Execution Guardrails\|T1480]] | Execution Guardrails | [BPFDoor](https://attack.mitre.org/software/S1161) creates a zero byte PID file at `/var/run/haldrund.pid`. [BPFDoor](https://attack.mitre.org/software/S1161) uses this file to determine if it is already running on a system to ensure only one instance is executing at a time.[^1]   |
| [[Overwrite Process Arguments\|T1036.011]] | Overwrite Process Arguments | [BPFDoor](https://attack.mitre.org/software/S1161) overwrites the `argv[0]` value used by the Linux `/proc` filesystem to determine the command line and command name to display for each process. [BPFDoor](https://attack.mitre.org/software/S1161) selects a name from 10 hardcoded names that resemble Linux system daemons, such as; `/sbin/udevd -d`, `dbus-daemon --system`, `avahi-daemon: chroot helper`, `/sbin/auditd -n`, and `/usr/lib/systemd/systemd-journald`.[^1]  |
| [[Socket Filters\|T1205.002]] | Socket Filters | [BPFDoor](https://attack.mitre.org/software/S1161) uses BPF bytecode to attach a filter to a network socket to view ICMP, UDP, or TCP packets coming through ports 22 (ssh), 80 (http), and 443 (https). When [BPFDoor](https://attack.mitre.org/software/S1161)  finds a packet containing its “magic” bytes, it parses out two fields and forks itself. The parent process continues to monitor filtered traffic while the child process executes the instructions from the parsed fields.[^1] [^4]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [BPFDoor](https://attack.mitre.org/software/S1161) sets its process to ignore the following signals; `SIGHUP`, `SIGINT`, `SIGQUIT`, `SIGPIPE`, `SIGCHLD`, `SIGTTIN`, and `SIGTTOU`.[^4]  |
| [[Break Process Trees\|T1036.009]] | Break Process Trees | After initial execution, [BPFDoor](https://attack.mitre.org/software/S1161) forks itself and runs the fork with the `--init` flag, which allows it to execute secondary clean up operations. The parent process terminates leaving the forked process to be inherited by the legitimate process init.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | After initial setup, [BPFDoor](https://attack.mitre.org/software/S1161)'s original execution process deletes the dropped binary and exits.[^1]   |
| [[Timestomp\|T1070.006]] | Timestomp | [BPFDoor](https://attack.mitre.org/software/S1161) uses the `utimes()` function to change the executable's timestamp.[^1]   |
| [[Unix Shell\|T1059.004]] | Unix Shell | [BPFDoor](https://attack.mitre.org/software/S1161) can create a reverse shell and supports vt100 emulator formatting.[^1]  |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | [BPFDoor](https://attack.mitre.org/software/S1161) starts a shell on a high TCP port starting at 42391 up to 43391, then changes the local `iptables` rules to redirect all packets from the attacker to the shell port.[^1]   |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [BPFDoor](https://attack.mitre.org/software/S1161) can require a password to activate the backdoor and uses RC4 encryption or static library encryption `libtomcrypt`.[^1]  |
| [[Prevent Command History Logging\|T1690]] | Prevent Command History Logging | [BPFDoor](https://attack.mitre.org/software/S1161) sets the `MYSQL_HISTFILE` and `HISTFILE` to `/dev/null` preventing the shell and MySQL from logging history in `/proc/<PID>/environ`.[^1]   |




## References

[^1]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)


[^2]: Backdoor.Solaris.BPFDOOR.ZAJE


[^3]: Backdoor.Linux.BPFDOOR


[^4]: [Deep Instinct BPFDoor 2023](https://www.deepinstinct.com/blog/bpfdoor-malware-evolves-stealthy-sniffing-backdoor-ups-its-game)


[^5]: JustForFun


[^6]: [Harries JustForFun 2022](https://www.crowdstrike.com/blog/how-to-hunt-for-decisivearchitect-and-justforfun-implant/)


[^7]: [Merces BPFDOOR 2023](https://www.trendmicro.com/en_us/research/23/g/detecting-bpfdoor-backdoor-variants-abusing-bpf-filters.html)


