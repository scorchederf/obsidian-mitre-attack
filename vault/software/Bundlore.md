---
aliases: 
    - S0482
    
mitre-attack: https://attack.mitre.org/software/S0482
---

## S0482

[Bundlore](https://attack.mitre.org/software/S0482) is adware written for macOS that has been in use since at least 2015. Though categorized as adware, [Bundlore](https://attack.mitre.org/software/S0482) has many features associated with more traditional backdoors.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | [Bundlore](https://attack.mitre.org/software/S0482) uses the `curl -s -L -o` command to exfiltrate archived data to a URL.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Bundlore](https://attack.mitre.org/software/S0482) has disguised a malicious .app file as a Flash Player update.[^1]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Bundlore](https://attack.mitre.org/software/S0482) will enumerate the macOS version to determine which follow-on behaviors to execute using `/usr/bin/sw_vers -productVersion`.[^1] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Bundlore](https://attack.mitre.org/software/S0482) has used the `ps` command to list processes.[^1]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Bundlore](https://attack.mitre.org/software/S0482) has leveraged /bin/sh and /bin/bash to execute commands on the victim machine.[^1]  |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [Bundlore](https://attack.mitre.org/software/S0482) uses the `mktemp` utility to make unique file and directory names for payloads, such as `TMP_DIR=`mktemp -d -t x`.[^3]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | [Bundlore](https://attack.mitre.org/software/S0482) has been spread through malicious advertisements on websites.[^1]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [Bundlore](https://attack.mitre.org/software/S0482) creates a new key pair with `ssh-keygen` and drops the newly created user key in `authorized_keys` to enable remote login.[^1]  |
| [[Python\|T1059.006]] | Python | [Bundlore](https://attack.mitre.org/software/S0482) has used Python scripts to execute payloads.[^1]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [Bundlore](https://attack.mitre.org/software/S0482) has used `openssl` to decrypt AES encrypted payload data. [Bundlore](https://attack.mitre.org/software/S0482) has also used base64 and RC4 with a hardcoded key to deobfuscate data.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Bundlore](https://attack.mitre.org/software/S0482) can download and execute new versions of itself.[^1]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | [Bundlore](https://attack.mitre.org/software/S0482) can persist via a LaunchAgent.[^1]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Bundlore](https://attack.mitre.org/software/S0482) can change browser security settings to enable extensions to be installed. [Bundlore](https://attack.mitre.org/software/S0482) uses the `pkill cfprefsd` command to prevent users from inspecting processes.[^1] [^3]  |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Bundlore](https://attack.mitre.org/software/S0482) has obfuscated data with base64, AES, RC4, and bz2.[^1]  |
| [[Software Discovery\|T1518]] | Software Discovery | [Bundlore](https://attack.mitre.org/software/S0482) has the ability to enumerate what browser is being used as well as version information for Safari.[^1]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [Bundlore](https://attack.mitre.org/software/S0482) prompts the user for their credentials.[^1]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Bundlore](https://attack.mitre.org/software/S0482) has attempted to get users to execute a malicious .app file that looks like a Flash Player update.[^1]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [Bundlore](https://attack.mitre.org/software/S0482) can persist via a LaunchDaemon.[^1]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [Bundlore](https://attack.mitre.org/software/S0482) can install malicious browser extensions that are used to hijack user searches.[^1]  |
| [[AppleScript\|T1059.002]] | AppleScript | [Bundlore](https://attack.mitre.org/software/S0482) can use AppleScript to inject malicious JavaScript into a browser.[^1]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Bundlore](https://attack.mitre.org/software/S0482) can execute JavaScript by injecting it into the victim's browser.[^1]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [Bundlore](https://attack.mitre.org/software/S0482) changes the permissions of a payload using the command `chmod -R 755`.[^3]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Bundlore](https://attack.mitre.org/software/S0482) uses HTTP requests for C2.[^1]  |




## References

[^1]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)


[^2]: OSX.Bundlore


[^3]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


