---
aliases: 
    - S0658
    
mitre-attack: https://attack.mitre.org/software/S0658
---

## S0658

[XCSSET](https://attack.mitre.org/software/S0658) is a modular macOS malware family delivered through infected Xcode projects and executed when the project is compiled. Active since August 2020, it has been observed installing backdoors, spoofed browsers, collecting data, and encrypting user files. It is composed of SHC-compiled shell scripts and run-only AppleScripts, often hiding in apps that mimic system tools (such as Xcode, Mail, or Notes) or use familiar icons (like Launchpad) to avoid detection.[^6] [^5] [^3] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Hidden Files and Directories\|T1564.001]] | Hidden Files and Directories | [XCSSET](https://attack.mitre.org/software/S0658) uses a hidden folder named `.xcassets` and `.git` to embed itself in Xcode.[^6]  |
| [[Software Discovery\|T1518]] | Software Discovery | [XCSSET](https://attack.mitre.org/software/S0658) uses `ps aux` with the `grep` command to enumerate common browsers and system processes potentially impacting [XCSSET](https://attack.mitre.org/software/S0658)'s exfiltration capabilities.[^6]  |
| [[System Language Discovery\|T1614.001]] | System Language Discovery | [XCSSET](https://attack.mitre.org/software/S0658) uses AppleScript to check the host's language and location with the command `user locale of (get system info)`.[^6]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [XCSSET](https://attack.mitre.org/software/S0658) downloads browser specific AppleScript modules using a constructed URL with the `curl` command, `https://" & domain & "/agent/scripts/" & moduleName & ".applescript`.[^6]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [XCSSET](https://attack.mitre.org/software/S0658) retrieves files that match the pattern defined in the INAME_QUERY variable within the user's home directory, such as `*test.txt`, and are below a specific size limit. It then archives the files and exfiltrates the data over its C2 channel.[^6] [^3]  |
| [[Gatekeeper Bypass\|T1553.001]] | Gatekeeper Bypass | [XCSSET](https://attack.mitre.org/software/S0658) has dropped a malicious applet into an app's `.../Contents/MacOS/` folder of a previously launched app to bypass Gatekeeper's security checks on first launch apps (prior to macOS 13).[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [XCSSET](https://attack.mitre.org/software/S0658) installs malicious application bundles that mimic native macOS apps, such as Safari, by using the legitimate app’s icon and customizing the `Info.plist` to match expected metadata.[^6] [^3]  |
| [[Compromise Software Dependencies and Development Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | [XCSSET](https://attack.mitre.org/software/S0658) adds malicious code to a host's Xcode projects by enumerating CocoaPods `target_integrator.rb` files under the `/Library/Ruby/Gems` folder or enumerates all `.xcodeproj` folders under a given directory. [XCSSET](https://attack.mitre.org/software/S0658) then downloads a script and Mach-O file into the Xcode project folder.[^6]  |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | [XCSSET](https://attack.mitre.org/software/S0658) will create an ssh key if necessary with the `ssh-keygen -t rsa -f $HOME/.ssh/id_rsa -P` command. [XCSSET](https://attack.mitre.org/software/S0658) will upload a private key file to the server to remotely access the host without a password.[^6]   |
| [[Data from Local System\|T1005]] | Data from Local System | [XCSSET](https://attack.mitre.org/software/S0658) collects contacts and application data from files in Desktop, Documents, Downloads, Dropbox, and WeChat folders.[^6]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [XCSSET](https://attack.mitre.org/software/S0658) uses RC4 encryption over TCP to communicate with its C2 server.[^6]    |
| [[Dynamic Linker Hijacking\|T1574.006]] | Dynamic Linker Hijacking | [XCSSET](https://attack.mitre.org/software/S0658) adds malicious file paths to the `DYLD_FRAMEWORK_PATH` and `DYLD_LIBRARY_PATH` environment variables to execute malicious code.[^6]  |
| [[Archive Collected Data\|T1560]] | Archive Collected Data | [XCSSET](https://attack.mitre.org/software/S0658) will compress entire `~/Desktop` folders excluding all `.git` folders, but only if the total data size is under 200MB.[^6]  |
| [[TCC Manipulation\|T1548.006]] | TCC Manipulation | For several modules, [XCSSET](https://attack.mitre.org/software/S0658) attempts to access or list the contents of user folders such as Desktop, Downloads, and Documents. If the folder does not exist or access is denied, it enters a loop where it resets the TCC database and retries access.[^3]  |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | [XCSSET](https://attack.mitre.org/software/S0658) uses the `chmod +x` command to grant executable permissions to the malicious file.[^8]  |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | [XCSSET](https://attack.mitre.org/software/S0658) uses `scp` to access the `~/Library/Cookies/Cookies.binarycookies` file.[^6]  |
| [[GUI Input Capture\|T1056.002]] | GUI Input Capture | [XCSSET](https://attack.mitre.org/software/S0658) prompts the user to input credentials using a native macOS dialog box leveraging the system process `/Applications/Safari.app/Contents/MacOS/SafariForWebKitDevelopment`.[^6]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | [XCSSET](https://attack.mitre.org/software/S0658) has used a zero-day exploit in the ssh launchdaemon to elevate privileges and bypass SIP.[^6]  |
| [[Launchctl\|T1569.001]] | Launchctl | [XCSSET](https://attack.mitre.org/software/S0658) loads a system level launchdaemon using the `launchctl load -w` command from `/System/Librarby/LaunchDaemons/ssh.plist`.[^6]  |
| [[Security Software Discovery\|T1518.001]] | Security Software Discovery | [XCSSET](https://attack.mitre.org/software/S0658) searches firewall configuration files located in `/Library/Preferences/` and uses `csrutil status` to determine if System Integrity Protection is enabled.[^6]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [XCSSET](https://attack.mitre.org/software/S0658) performs AES-CBC encryption on files under `~/Documents`, `~/Downloads`, and<br>`~/Desktop` with a fixed key and renames files to give them a `.enc` extension. Only files with sizes <br>less than 500MB are encrypted.[^6]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [XCSSET](https://attack.mitre.org/software/S0658) identifies the macOS version and uses `ioreg` to determine serial number.[^6]  |
| [[Launch Daemon\|T1543.004]] | Launch Daemon | [XCSSET](https://attack.mitre.org/software/S0658) uses the ssh launchdaemon to elevate privileges, bypass system controls, and enable remote access to the victim.[^6]  |
| [[Plist File Modification\|T1647]] | Plist File Modification | In older versions, [XCSSET](https://attack.mitre.org/software/S0658) uses the `plutil` command to modify the `LSUIElement`, `DFBundleDisplayName`, and `CFBundleIdentifier` keys in the `/Contents/Info.plist` file to change how [XCSSET](https://attack.mitre.org/software/S0658) is visible on the system. In later versions, [XCSSET](https://attack.mitre.org/software/S0658) leverages a third-party notarized `dockutil` tool to modify the `.plist` file responsible for presenting applications to the user in the Dock and LaunchPad to point to a malicious application.[^6] [^3]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | Older [XCSSET](https://attack.mitre.org/software/S0658) variants use `xxd` to encode modules. Later versions pass an `xxd` or `base64` encoded blob through multiple decoding stages to reconstruct the module name, AppleScript, or shell command. For example, the initial network request uses three layers of hex decoding before executing a curl command in a shell.[^3]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [XCSSET](https://attack.mitre.org/software/S0658) has used `mdfind` to enumerate a list of apps known to grant screen sharing permissions and leverages a module to run the command `ls -la ~/Desktop`.[^1] [^3] <br> |
| [[Unix Shell\|T1059.004]] | Unix Shell | [XCSSET](https://attack.mitre.org/software/S0658) uses a shell script to execute Mach-o files and `osacompile` commands such as, `osacompile -x -o xcode.app main.applescript`.[^6]  |
| [[Time Based Checks\|T1497.003]] | Time Based Checks | Using the machine's local time, [XCSSET](https://attack.mitre.org/software/S0658) waits 43200 seconds (12 hours) from the initial creation timestamp of a specific file, `.report`. After the elapsed time, [XCSSET](https://attack.mitre.org/software/S0658) executes additional modules.[^6]  |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | [XCSSET](https://attack.mitre.org/software/S0658) uses a malicious browser application to replace the legitimate browser in order to continuously capture credentials, monitor web traffic, and download additional modules.[^6]  |
| [[Account Discovery\|T1087]] | Account Discovery | [XCSSET](https://attack.mitre.org/software/S0658) attempts to discover accounts from various locations such as a user's Evernote, AppleID, Telegram, Skype, and WeChat data.[^6]  |
| [[Event Triggered Execution\|T1546]] | Event Triggered Execution | [XCSSET](https://attack.mitre.org/software/S0658)'s `dfhsebxzod` module searches for `.xcodeproj` directories within the user’s home folder and subdirectories. For each match, it locates the corresponding `project.pbxproj` file and embeds an encoded payload into a build rule, target configuration, or project setting. The payload is later executed during the build process.[^3] [^5]  |
| [[Screen Capture\|T1113]] | Screen Capture | [XCSSET](https://attack.mitre.org/software/S0658) saves a screen capture of the victim's system with a numbered filename and `.jpg` extension. Screen captures are taken at specified intervals based on the system. [^6]  |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | Using [AppleScript](https://attack.mitre.org/techniques/T1059/002), [XCSSET](https://attack.mitre.org/software/S0658) adds it's executable to the user's `~/.zshrc_aliases` file (`"echo " & payload & " > ~/zshrc_aliases"`), it then adds a line to the .zshrc file to source the `.zshrc_aliases` file (`[ -f $HOME/.zshrc_aliases ] && . $HOME/.zshrc_aliases`). Each time the user starts a new `zsh` terminal session, the `.zshrc` file executes the `.zshrc_aliases` file.[^3]   |




## References

[^1]: [Application Bundle Manipulation Brandon Dalton](https://redcanary.com/blog/mac-application-bundles/)


[^2]: [malwarebyteslabs xcsset dubrobber](https://blog.malwarebytes.com/detections/osx-dubrobber/)


[^3]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)


[^4]: XCSSET


[^5]: [April 2021 TrendMicro XCSSET](https://www.trendmicro.com/en_us/research/21/d/xcsset-quickly-adapts-to-macos-11-and-m1-based-macs.html)


[^6]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^7]: OSX.DubRobber


[^8]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)


