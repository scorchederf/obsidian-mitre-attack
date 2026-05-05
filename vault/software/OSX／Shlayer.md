---
aliases: 
    - S0402
    
mitre-attack: https://attack.mitre.org/software/S0402
---

## S0402

[OSX/Shlayer](https://attack.mitre.org/software/S0402) is a Trojan designed to install adware on macOS that was first discovered in 2018.[^12] [^4] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hide Artifacts\|T1564]] | Hide Artifacts | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used the `mktemp` utility to make random and unique filenames for payloads, such as `export tmpDir="$(mktemp -d /tmp/XXXXXXXXXXXX)"` or `mktemp -t Installer`.[^11] [^13] [^10]  |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has executed a .command script from a hidden directory in a mounted DMG.[^12]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can use the `chmod` utility to set a file as executable, such as `chmod 777` or `chmod +x`.[^13] [^12] [^10]  |
| [[Malicious File\|T1204.002]] | Malicious File | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has relied on users mounting and executing a malicious DMG file.[^12] [^4]  |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can install malicious Safari browser extensions to serve ads.[^5] [^2]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | If running with elevated privileges, [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used the `spctl` command to disable Gatekeeper protection for a downloaded file. [OSX/Shlayer](https://attack.mitre.org/software/S0402) can also leverage system links pointing to bash scripts in the downloaded DMG file to bypass Gatekeeper, a flaw patched in macOS 11.3 and later versions. [OSX/Shlayer](https://attack.mitre.org/software/S0402) has been Notarized by Apple, resulting in successful passing of additional Gatekeeper checks.[^12] [^10] [^6]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can use bash scripts to check the macOS version, download payloads, and extract bytes from files. [OSX/Shlayer](https://attack.mitre.org/software/S0402) uses the command `sh -c tail -c +1381...` to extract bytes at an offset from a specified file. [OSX/Shlayer](https://attack.mitre.org/software/S0402) uses the `curl -fsL "$url" >$tmp_path` command to download malicious payloads into a temporary directory.[^12] [^11] [^13] [^6]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used the `nohup` command to instruct executed payloads to ignore hangup signals.[^10]  |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can base64-decode and AES-decrypt downloaded payloads.[^12]  Versions of [OSX/Shlayer](https://attack.mitre.org/software/S0402) pass encrypted and password-protected code to `openssl` and then write the payload to the `/tmp` folder.[^11] [^13]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can masquerade as a Flash Player update.[^12] [^4]  |
| [[Resource Forking\|T1564.009]] | Resource Forking | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used a resource fork to hide a compressed binary file of itself from the terminal, Finder, and potentially evade traditional scanners.[^8] [^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has used the command `appDir="$(dirname $(dirname "$currentDir"))"` and `$(dirname "$(pwd -P)")` to construct installation paths.[^11] [^13]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [OSX/Shlayer](https://attack.mitre.org/software/S0402) has collected the IOPlatformUUID, session UID, and the OS version using the command `sw_vers -productVersion`.[^12] [^11]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can download payloads, and extract bytes from files. [OSX/Shlayer](https://attack.mitre.org/software/S0402) uses the `curl -fsL "$url" >$tmp_path` command to download malicious payloads into a temporary directory.[^12] [^11] [^13] [^6]  |
| [[Elevated Execution with Prompt\|T1548.004]] | Elevated Execution with Prompt | [OSX/Shlayer](https://attack.mitre.org/software/S0402) can escalate privileges to root by asking the user for credentials.[^12]  |




## References

[^1]: OSX/Shlayer


[^2]: [Malwarebytes Crossrider Apr 2018](https://blog.malwarebytes.com/threat-analysis/2018/04/new-crossrider-variant-installs-configuration-profiles-on-macs/)


[^3]: [sentinellabs resource named fork 2020](https://www.sentinelone.com/labs/resourceful-macos-malware-hides-in-named-fork/)


[^4]: [Intego Shlayer Feb 2018](https://www.intego.com/mac-security-blog/osxshlayer-new-mac-malware-comes-out-of-its-shell/)


[^5]: [Intego Shlayer Apr 2018](https://www.intego.com/mac-security-blog/new-osxshlayer-malware-variant-found-using-a-dirty-new-trick/)


[^6]: [objectivesee osx.shlayer apple approved 2020](https://objective-see.com/blog/blog_0x4E.html)


[^7]: Crossrider


[^8]: [tau bundlore erika noerenberg 2020](https://blogs.vmware.com/security/2020/06/tau-threat-analysis-bundlore-macos-mm-install-macos.html)


[^9]: Zshlayer


[^10]: [Shlayer jamf gatekeeper bypass 2021](https://www.jamf.com/blog/shlayer-malware-abusing-gatekeeper-bypass-on-macos/)


[^11]: [sentinelone shlayer to zshlayer](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)


[^12]: [Carbon Black Shlayer Feb 2019](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)


[^13]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


