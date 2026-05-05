---
aliases: 
    - T1497.003
mitre-attack: https://attack.mitre.org/techniques/T1497/003
tactic: 
     - Defense Evasion - Discovery
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## T1497.003

Adversaries may employ various time-based methods to detect and avoid virtualization and analysis environments. This may include enumerating time-based properties, such as uptime or the system clock, as well as the use of timers or other triggers to avoid a virtual machine environment (VME) or sandbox, specifically those that are automated or only operate for a limited amount of time.<br><br>Adversaries may employ various time-based evasions, such as delaying malware functionality upon initial execution using programmatic sleep commands or native system scheduling functionality (ex: [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053)). Delays may also be based on waiting for specific victim conditions to be met (ex: system time, events, etc.) or employ scheduled [Multi-Stage Channels](https://attack.mitre.org/techniques/T1104) to avoid analysis and scrutiny.[^357] <br><br>Benign commands or other operations may also be used to delay malware execution. Loops or otherwise needless repetitions of commands, such as [Ping](https://attack.mitre.org/software/S0097)s, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.[^32] [^196]  Another variation, commonly referred to as API hammering, involves making various calls to [Native API](https://attack.mitre.org/techniques/T1106) functions in order to delay execution (while also potentially overloading analysis environments with junk data).[^322] [^96] <br><br>Adversaries may also use time as a metric to detect sandboxes and analysis environments, particularly those that attempt to manipulate time mechanisms to simulate longer elapses of time. For example, an adversary may be able to identify a sandbox accelerating time by sampling and calculating the expected value for an environment's timestamp before and after execution of a sleep function.[^130] 


### Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[Brute Ratel C4\|S1063]] | Brute Ratel C4 | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call `NtDelayExecution` to pause execution.[^248] [^215]  |
| [[TrickBot\|S0266]] | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) has used `printf` and file I/O loops to delay process execution as part of API hammering.[^96]  |
| [[Bumblebee\|S1039]] | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) has the ability to set a hardcoded and randomized sleep interval.[^39]  |
| [[Ursnif\|S0386]] | Ursnif | [Ursnif](https://attack.mitre.org/software/S0386) has used a 30 minute delay after execution to evade sandbox monitoring tools.[^11]  |
| [[RansomHub\|S1212]] | RansomHub | [RansomHub](https://attack.mitre.org/software/S1212) can sleep for a set number of minutes before beginning execution.[^60]  |
| [[Pony\|S0453]] | Pony | [Pony](https://attack.mitre.org/software/S0453) has delayed execution using a built-in function to avoid detection and analysis.[^222] 	 |
| [[Crimson\|S0115]] | Crimson | [Crimson](https://attack.mitre.org/software/S0115) can determine when it has been installed on a host for at least 15 days before downloading the final payload.[^132]  |
| [[Tomiris\|S0671]] | Tomiris | [Tomiris](https://attack.mitre.org/software/S0671) has the ability to sleep for at least nine minutes to evade sandbox-based analysis systems.[^68]  |
| [[Gootloader\|S1138]] | Gootloader | [Gootloader](https://attack.mitre.org/software/S1138) can designate a sleep period of more than 22 seconds between stages of infection.[^212]  |
| [[Snip3\|S1086]] | Snip3 | [Snip3](https://attack.mitre.org/software/S1086) can execute `WScript.Sleep` to delay execution of its second stage.[^257]  |
| [[GuLoader\|S0561]] | GuLoader | [GuLoader](https://attack.mitre.org/software/S0561) has the ability to perform anti-debugging based on time checks, API calls, and CPUID.[^178]  |
| [[WhisperGate\|S0689]] | WhisperGate | [WhisperGate](https://attack.mitre.org/software/S0689) can pause for 20 seconds to bypass antivirus solutions.[^240] [^137]  |
| [[Okrum\|S0439]] | Okrum | [Okrum](https://attack.mitre.org/software/S0439)'s loader can detect presence of an emulator by using two calls to GetTickCount API, and checking whether the time has been accelerated.[^17]  |
| [[Raindrop\|S0565]] | Raindrop | After initial installation, [Raindrop](https://attack.mitre.org/software/S0565) runs a computation to delay execution.[^216]  |
| [[FatDuke\|S0512]] | FatDuke | [FatDuke](https://attack.mitre.org/software/S0512) can turn itself on or off at random intervals.[^150]  |
| [[DRATzarus\|S0694]] | DRATzarus | [DRATzarus](https://attack.mitre.org/software/S0694) can use the `GetTickCount` and `GetSystemTimeAsFileTime` API calls to measure function timing.[^330]  [DRATzarus](https://attack.mitre.org/software/S0694) can also remotely shut down into sleep mode under specific conditions to evade <br>detection.[^330]  |
| [[BADFLICK\|S0642]] | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) has delayed communication to the actor-controlled IP address by 5 minutes.[^73]  |
| [[GoldMax\|S0588]] | GoldMax | [GoldMax](https://attack.mitre.org/software/S0588) has set an execution trigger date and time, stored as an ASCII Unix/Epoch time value.[^350]  |
| [[DarkTortilla\|S1066]] | DarkTortilla | [DarkTortilla](https://attack.mitre.org/software/S1066) can implement the `kernel32.dll` Sleep function to delay execution for up to 300 seconds before implementing persistence or processing an addon package.[^165]  |
| [[Bisonal\|S0268]] | Bisonal | [Bisonal](https://attack.mitre.org/software/S0268) has checked if the malware is running in a virtual environment with the anti-debug function GetTickCount() to compare the timing.[^351] [^293]   |
| [[Clambling\|S0660]] | Clambling | [Clambling](https://attack.mitre.org/software/S0660) can wait 30 minutes before initiating contact with C2.[^323]  |
| [[SVCReady\|S1064]] | SVCReady | [SVCReady](https://attack.mitre.org/software/S1064) can enter a sleep stage for 30 minutes to evade detection.[^233]  |
| [[ThiefQuest\|S0595]] | ThiefQuest | [ThiefQuest](https://attack.mitre.org/software/S0595) invokes `time` call to check the system's time, executes a `sleep` command, invokes a second `time` call, and then compares the time difference between the two `time` calls and the amount of time the system slept to identify the sandbox.[^278]  |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) has used the command `timeout 20` to pause the execution of its initial loader.[^305]  |
| [[P8RAT\|S0626]] | P8RAT | [P8RAT](https://attack.mitre.org/software/S0626) has the ability to "sleep" for a specified time to evade detection.[^157]  |
| [[BendyBear\|S0574]] | BendyBear | [BendyBear](https://attack.mitre.org/software/S0574) can check for analysis environments and signs of debugging using the Windows API `kernel32!GetTickCountKernel32` call.[^348]   |
| [[SodaMaster\|S0627]] | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) has the ability to put itself to "sleep" for a specified time.[^157]  |
| [[LiteDuke\|S0513]] | LiteDuke | [LiteDuke](https://attack.mitre.org/software/S0513) can wait 30 seconds before executing additional code if security software is detected.[^150]  |
| [[Bazar\|S0534]] | Bazar | [Bazar](https://attack.mitre.org/software/S0534) can use a timer to delay execution of core functionality.[^108]  |
| [[HermeticWiper\|S0697]] | HermeticWiper | [HermeticWiper](https://attack.mitre.org/software/S0697) has the ability to receive a command parameter to sleep prior to carrying out destructive actions on a targeted host.[^309]  |
| [[SUNBURST\|S0559]] | SUNBURST | [SUNBURST](https://attack.mitre.org/software/S0559) remained dormant after initial access for a period of up to two weeks.[^131]  |
| [[EvilBunny\|S0396]] | EvilBunny | [EvilBunny](https://attack.mitre.org/software/S0396) has used time measurements from 3 different APIs before and after performing sleep operations to check and abort if the malware is running in a sandbox.[^146]  |
| [[IPsec Helper\|S1132]] | IPsec Helper | [IPsec Helper](https://attack.mitre.org/software/S1132) will sleep for a random number of seconds, iterating 200 times over sleeps between one to three seconds, before continuing execution flow.[^243]  |
| [[GoldenSpy\|S0493]] | GoldenSpy | [GoldenSpy](https://attack.mitre.org/software/S0493)'s installer has delayed installation of [GoldenSpy](https://attack.mitre.org/software/S0493) for two hours after it reaches a victim system.[^362] 	 |
| [[GrimAgent\|S0632]] | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) can sleep for 195 - 205 seconds after payload execution and before deleting its task.[^205]  |
| [[Clop\|S0611]] | Clop | [Clop](https://attack.mitre.org/software/S0611) has used the `sleep` command to avoid sandbox detection.[^211]  |
| [[Lokibot\|S0447]] | Lokibot | [Lokibot](https://attack.mitre.org/software/S0447) has performed a time-based anti-debug check before downloading its third stage.[^37]  |
| [[Egregor\|S0554]] | Egregor | [Egregor](https://attack.mitre.org/software/S0554) can perform a  long sleep (greater than or equal to 3 minutes) to evade detection.[^47]  |
| [[metaMain\|S1059]] | metaMain | [metaMain](https://attack.mitre.org/software/S1059) has delayed execution for five to six minutes during its persistence establishment process.[^90]  |
| [[LunarWeb\|S1141]] | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) can pause for a number of hours before entering its C2 communication loop.[^62]  |
| [[XCSSET\|S0658]] | XCSSET | Using the machine's local time, [XCSSET](https://attack.mitre.org/software/S0658) waits 43200 seconds (12 hours) from the initial creation timestamp of a specific file, `.report`. After the elapsed time, [XCSSET](https://attack.mitre.org/software/S0658) executes additional modules.[^114]  |
| [[AppleJeus\|S0584]] | AppleJeus | [AppleJeus](https://attack.mitre.org/software/S0584) has waited a specified time before downloading a second stage payload.[^98]  |
| [[QakBot\|S0650]] | QakBot | The [QakBot](https://attack.mitre.org/software/S0650) dropper can delay dropping the payload to evade detection.[^53] [^337]  |
| [[StrifeWater\|S1034]] | StrifeWater | [StrifeWater](https://attack.mitre.org/software/S1034) can modify its sleep time responses from the default of 20-22 seconds.[^167]  |






### Sub-techniques
| ID | Name |
| --- | --- |
| [[Time Based Evasion\|T1497.003]] | Time Based Evasion |



## References

[^1]: [Mandiant Defend UNC2452 White Paper](https://www.mandiant.com/resources/blog/remediation-and-hardening-strategies-for-microsoft-365-to-defend-against-unc2452)


[^2]: [UCF STIG Symbolic Links](https://www.stigviewer.com/stig/windows_server_2008_r2_member_server/2015-06-25/finding/V-26482)


[^3]: [Microsoft Security Alerts for Azure AD Roles](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^4]: [Wikibooks Grsecurity](https://en.wikibooks.org/wiki/Grsecurity/The_RBAC_System)


[^5]: [Crowdstrike Hypervisor Jackpotting Pt 2 2021](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)


[^6]: [Secure Ideas SMB Relay](https://blog.secureideas.com/2018/04/ever-run-a-relay-why-smb-relays-should-be-on-your-mind.html)


[^7]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^8]: [Dormann Dangers of VHD 2019](https://insights.sei.cmu.edu/cert/2019/09/the-dangers-of-vhd-and-vhdx-files.html)


[^9]: [Brining MimiKatz to Unix](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)


[^10]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)


[^11]: [TrendMicro Ursnif File Dec 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)


[^12]: [Kubernetes Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


[^13]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)


[^14]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)


[^15]: [Microsoft Remote Use of Local](https://blogs.technet.microsoft.com/secguide/2018/12/10/remote-use-of-local-accounts-laps-changes-everything/)


[^16]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)


[^17]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)


[^18]: [Cisco IOS Software Integrity Assurance - Image File Verification](https://tools.cisco.com/security/center/resources/integrity_assurance.html#7)


[^19]: [TechNet Moving Beyond EMET](https://blogs.technet.microsoft.com/srd/2017/08/09/moving-beyond-emet-ii-windows-defender-exploit-guard/)


[^20]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)


[^21]: [Cisco IOS Software Integrity Assurance - TACACS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)


[^22]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)


[^23]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^24]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^25]: [AWS RE:Inforce Threat Detection 2024](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)


[^26]: [Cisco IOS Software Integrity Assurance - Secure Boot](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)


[^27]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)


[^28]: [CyberArk Labs Safe Mode 2016](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)


[^29]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)


[^30]: [NIST 800-63-3](https://pages.nist.gov/800-63-3/sp800-63b.html)


[^31]: [Microsoft Tim McMichael Exchange Mail Forwarding 2](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)


[^32]: [Revil Independence Day](https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/)


[^33]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


[^34]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


[^35]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)


[^36]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)


[^37]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)


[^38]: [Microsoft Protected Users Security Group](https://docs.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group)


[^39]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)


[^40]: [Default VBS macros Blocking ](https://techcommunity.microsoft.com/t5/microsoft-365-blog/helping-users-stay-safe-blocking-internet-macros-by-default-in/ba-p/3071805)


[^41]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)


[^42]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)


[^43]: [RedLock Instance Metadata API 2018](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)


[^44]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^45]: [TechNet Applocker vs SRP](https://technet.microsoft.com/en-us/library/ee791851.aspx)


[^46]: [Microsoft Primary Refresh Token](https://learn.microsoft.com/en-us/azure/active-directory/devices/concept-primary-refresh-token)


[^47]: [JoeSecurity Egregor 2020](https://www.joesandbox.com/analysis/326673/0/pdf)


[^48]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^49]: [Microsoft Preauthentication Jul 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc961961(v=technet.10)?redirectedfrom=MSDN)


[^50]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)


[^51]: [CISA Phishing](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)


[^52]: [DNS-msft](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)


[^53]: [Cyberint Qakbot May 2021](https://blog.cyberint.com/qakbot-banking-trojan)


[^54]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^55]: [Cisco IOS Software Integrity Assurance - Credentials Management](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)


[^56]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)


[^57]: [Microsoft AMSI June 2015](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)


[^58]: [NSA Spotting](https://apps.nsa.gov/iaarchive/library/reports/spotting-the-adversary-with-windows-event-log-monitoring.cfm)


[^59]: [Microsoft Using Software Restriction ](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/ee791851(v=ws.11)?redirectedfrom=MSDN)


[^60]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)


[^61]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^62]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)


[^63]: [Microsoft Anti Spoofing](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)


[^64]: [Microsoft Nobelium Admin Privileges](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)


[^65]: [TechNet RDP Gateway](https://technet.microsoft.com/en-us/library/cc731150.aspx)


[^66]: [Kernel.org Restrict Kernel Module](https://patchwork.kernel.org/patch/8754821/)


[^67]: [Kifarunix - Task Scheduling in Linux](https://kifarunix.com/scheduling-tasks-using-at-command-in-linux/)


[^68]: [Kaspersky Tomiris Sep 2021](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)


[^69]: [TechNet Credential Guard](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/credential-guard)


[^70]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)


[^71]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)


[^72]: [mac security virus popup](https://macsecurity.net/view/543-remove-guroshied-mac)


[^73]: [Accenture MUDCARP March 2019](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)


[^74]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)


[^75]: [Microsoft MS14-025](http://support.microsoft.com/kb/2962486)


[^76]: [Cisco IOS Software Integrity Assurance - AAA](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)


[^77]: [Microsoft Preventing SMB](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)


[^78]: [Microsoft ASR Obfuscation](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference#block-execution-of-potentially-obfuscated-scripts)


[^79]: [MDMProfileConfigMacOS](https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf)


[^80]: [Microsoft COM ACL](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)


[^81]: [Microsoft SID Filtering Quarantining Jan 2009](https://technet.microsoft.com/library/cc794757.aspx)


[^82]: [Microsoft - Device Registration](https://www.microsoft.com/security/blog/2022/01/26/evolved-phishing-device-registration-trick-adds-to-phishers-toolbox-for-victims-without-mfa)


[^83]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^84]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)


[^85]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)


[^86]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^87]: [Microsoft_rec_block_rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^88]: [Windows Commands JPCERT](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)


[^89]: [STIG krbtgt reset](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)


[^90]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)


[^91]: [MFA Fatigue Attacks - PortSwigger](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)


[^92]: [Windows Anonymous Enumeration of SAM Accounts](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)


[^93]: [ADSecurity Mimikatz DCSync](https://adsecurity.org/?p=1729)


[^94]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^95]: [SANS Application Whitelisting](https://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^96]: [Joe Sec Trickbot](https://www.joesecurity.org/blog/498839998833561473)


[^97]: [Microsoft TESTSIGNING Feb 2021](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/the-testsigning-boot-configuration-option)


[^98]: [CISA AppleJeus Feb 2021](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)


[^99]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)


[^100]: [HowToGeek ShowExtension](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/)


[^101]: [Microsoft SolarWinds Customer Guidance](https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/)


[^102]: [Wald0 Guide to GPOs](https://wald0.com/?p=179)


[^103]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)


[^104]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


[^105]: [Secure Host Baseline EMET](https://github.com/iadgov/Secure-Host-Baseline/tree/master/EMET)


[^106]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)


[^107]: [AWS Management Account Best Practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)


[^108]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)


[^109]: [Microsoft driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^110]: [Technospot Chrome Extensions GP](http://www.technospot.net/blogs/block-chrome-extensions-using-google-chrome-group-policy-settings/)


[^111]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)


[^112]: [Office 365 Partner Relationships](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)


[^113]: [Powersploit](https://github.com/mattifestation/PowerSploit)


[^114]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)


[^115]: [Mandiant Azure AD Backdoors](https://www.mandiant.com/resources/detecting-microsoft-365-azure-active-directory-backdoors)


[^116]: [AWS DB VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)


[^117]: [ntlm_relaying_kerberos_del](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)


[^118]: [Cisco ARP Poisoning Mitigation 2016](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html)


[^119]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)


[^120]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^121]: [Juniper DAI 2020](https://www.juniper.net/documentation/en_US/junos/topics/task/configuration/understanding-and-using-dai.html)


[^122]: [Electron Security 3](https://medium.com/certik/vulnerability-in-electron-based-application-unintentionally-giving-malicious-code-room-to-run-e2e1447d01b8)


[^123]: [Broadcom Virtual Machine Guest Operations Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)


[^124]: [US-CERT TA18-106A Network Infrastructure Devices 2018](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)


[^125]: [Okta Block Anonymizing Services](https://sec.okta.com/blockanonymizers)


[^126]: [AdSecurity Cracking Kerberos Dec 2015](https://adsecurity.org/?p=2293)


[^127]: [Kernel Self Protection Project](https://www.kernel.org/doc/html/latest/security/self-protection.html)


[^128]: [Microsoft Azure AD Admin Consent](https://docs.microsoft.com/en-us/azure/security/fundamentals/steps-secure-identity#block-end-user-consent)


[^129]: [Microsoft Create Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)


[^130]: [ISACA Malware Tricks](https://www.isaca.org/resources/isaca-journal/issues/2017/volume-6/evasive-malware-tricks-how-malware-evades-detection-by-sandboxes)


[^131]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)


[^132]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)


[^133]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)


[^134]: [Microsoft Sxstrace](https://docs.microsoft.com/windows-server/administration/windows-commands/sxstrace)


[^135]: [FireEye ADFS](https://www.troopers.de/troopers19/agenda/fpxwmn/)


[^136]: [AWS Data Perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/)


[^137]: [RecordedFuture WhisperGate Jan 2022](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)


[^138]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^139]: [Re-Open windows on Mac](https://support.apple.com/en-us/HT204005)


[^140]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)


[^141]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


[^142]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)


[^143]: [Microsoft Get-InboxRule](https://docs.microsoft.com/en-us/powershell/module/exchange/get-inboxrule?view=exchange-ps)


[^144]: [Pfammatter - Hidden Inbox Rules](https://blog.compass-security.com/2018/09/hidden-inbox-rules-in-microsoft-exchange/)


[^145]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)


[^146]: [Cyphort EvilBunny Dec 2014](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)


[^147]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)


[^148]: [TechNet Credential Theft](https://technet.microsoft.com/en-us/library/dn535501.aspx)


[^149]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)


[^150]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)


[^151]: [Microsoft Application Lockdown](https://docs.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10)?redirectedfrom=MSDN)


[^152]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)


[^153]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^154]: [UCF STIG Elevation Account Enumeration](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)


[^155]: [Okta DPoP 2023](https://www.okta.com/blog/2023/06/a-leap-forward-in-token-security-okta-adds-support-for-dpop/)


[^156]: [Microsoft Replication ACL](https://support.microsoft.com/help/303972/how-to-grant-the-replicating-directory-changes-permission-for-the-micr)


[^157]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)


[^158]: [Chromium HSTS](https://www.chromium.org/hsts/)


[^159]: [Microsoft Credential Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-how-it-works)


[^160]: [Microsoft Manage Mail Flow Rules 2023](https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/manage-mail-flow-rules)


[^161]: [SWAT-hospital](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)


[^162]: [MITRE VMware Abuse 2024](https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b)


[^163]: [Microsoft PowerShell CLM](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


[^164]: [Microsoft System Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)


[^165]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)


[^166]: [GitHub SHB Credential Guard](https://github.com/iadgov/Secure-Host-Baseline/tree/master/Credential%20Guard)


[^167]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)


[^168]: [Windows RDP Sessions](https://technet.microsoft.com/en-us/library/cc754272(v=ws.11).aspx)


[^169]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


[^170]: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)


[^171]: [Akamai DGA Mitigation](https://medium.com/@yvyuz/a-death-match-of-domain-generation-algorithms-a5b5dbdc1c6e)


[^172]: [TechRepublic Wireless GPO FEB 2009](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)


[^173]: [Microsoft Process Wide Com Keys](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)


[^174]: [Microsoft runas](https://technet.microsoft.com/en-us/library/bb490994.aspx)


[^175]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)


[^176]: [Seqrite DoubleExtension](https://www.seqrite.com/blog/how-to-avoid-dual-attack-and-vulnerable-files-with-double-extension/)


[^177]: [push notifications -infosecinstitute](https://www.infosecinstitute.com/resources/security-awareness/malicious-push-notifications-is-that-a-real-or-fake-windows-defender-update/)


[^178]: [Medium Eli Salem GuLoader April 2021](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)


[^179]: [Microsoft Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)


[^180]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)


[^181]: [site notifications - krebsonsecurity](https://krebsonsecurity.com/2020/11/be-very-sparing-in-allowing-site-notifications/)


[^182]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


[^183]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)


[^184]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)


[^185]: [Netspi PowerShell Execution Policy Bypass](https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/)


[^186]: [Microsoft Netdom Trust Sept 2012](https://technet.microsoft.com/library/cc835085.aspx)


[^187]: [file_upload_attacks_pt2](https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/)


[^188]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^189]: [Google Workspace External Sharing](https://support.google.com/a/answer/60781)


[^190]: [byt3bl33d3r NTLM Relaying](https://byt3bl33d3r.github.io/practical-guide-to-ntlm-relaying-in-2017-aka-getting-a-foothold-in-under-5-minutes.html)


[^191]: [ACSC Email Spoofing](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)


[^192]: [Obfuscated scripts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-execution-of-potentially-obfuscated-scripts)


[^193]: [Beechey 2010](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)


[^194]: [Microsoft ISAPICGIRestriction 2016](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/security/isapicgirestriction/)


[^195]: [Unit 42 Palo Alto Ransomware in Public Clouds 2022](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)


[^196]: [Netskope Nitol](https://www.netskope.com/blog/nitol-botnet-makes-resurgence-evasive-sandbox-analysis-technique)


[^197]: [Cyber Safety Review Board: Lapsus](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)


[^198]: [Cisco IOS Software Integrity Assurance - Image File Integrity](https://tools.cisco.com/security/center/resources/integrity_assurance.html#30)


[^199]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)


[^200]: [Microsoft Driver Block Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)


[^201]: [TCG Trusted Platform Module](http://www.trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Summary_04292008.pdf)


[^202]: [Microsoft WDAC](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)


[^203]: [Corio 2008](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))


[^204]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)


[^205]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)


[^206]: [Microsoft WMI Filters](https://blogs.technet.microsoft.com/askds/2008/09/11/fun-with-wmi-filters-in-group-policy/)


[^207]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


[^208]: [Enigma Reviving DDE Jan 2018](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)


[^209]: [Microsoft Azure security baseline for Azure Active Directory](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/aad-security-baseline)


[^210]: [TrustedSec OOB Communications](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)


[^211]: [Unit42 Clop April 2021](https://unit42.paloaltonetworks.com/clop-ransomware/)


[^212]: [Sophos Gootloader](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)


[^213]: [Microsoft Disable NTLM Nov 2012](https://technet.microsoft.com/library/jj865668.aspx)


[^214]: [Microsoft AppLocker DLL](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/applocker/dll-rules-in-applocker)


[^215]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)


[^216]: [Symantec RAINDROP January 2021](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)


[^217]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)


[^218]: [Wikipedia HPKP](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning)


[^219]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)


[^220]: [NSA MS AppLocker](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)


[^221]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)


[^222]: [Malwarebytes Pony April 2016](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)


[^223]: [TCC macOS bypass](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)


[^224]: [EnableMPRNotifications](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowslogon)


[^225]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)


[^226]: [Apple TN2459 Kernel Extensions](https://developer.apple.com/library/archive/technotes/tn2459/_index.html)


[^227]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)


[^228]: [Cisco Securing SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)


[^229]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)


[^230]: [dhcp_serv_op_events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn800668(v=ws.11))


[^231]: [Stealthbits Cracking AS-REP Roasting Jun 2019](https://blog.stealthbits.com/cracking-active-directory-passwords-with-as-rep-roasting/)


[^232]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)


[^233]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)


[^234]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)


[^235]: [Sygnia ESXi Ransomware 2024](https://www.sygnia.co/blog/esxi-ransomware-attacks/)


[^236]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^237]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)


[^238]: [Mandiant Cloudy Logs 2023](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)


[^239]: [Microsoft 365 External Sharing](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)


[^240]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)


[^241]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)


[^242]: [Tilbury Windows Credentials](https://www.first.org/resources/papers/conf2017/Windows-Credentials-Attacks-and-Mitigation-Techniques.pdf)


[^243]: [SentinelOne Agrius 2021](https://assets.sentinelone.com/sentinellabs/evol-agrius)


[^244]: [GitHub Certify](https://github.com/GhostPack/Certify/)


[^245]: [Comparitech Replay Attack](https://www.comparitech.com/blog/information-security/what-is-a-replay-attack/)


[^246]: [Microsoft Replace Process Token](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)


[^247]: [Increasing Linux kernel integrity](https://linux-audit.com/increase-kernel-integrity-with-disabled-linux-kernel-modules-loading/)


[^248]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)


[^249]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)


[^250]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)


[^251]: [Azure Subscription Policies](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)


[^252]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)


[^253]: [GitHub IAD Secure Host Baseline UAC Filtering](https://github.com/iadgov/Secure-Host-Baseline/blob/master/Windows/Group%20Policy%20Templates/en-US/SecGuide.adml)


[^254]: [SpecterOps Certified Pre Owned](https://www.specterops.io/assets/resources/Certified_Pre-Owned.pdf)


[^255]: [AdSecurity DCSync Sept 2015](https://adsecurity.org/?p=1729)


[^256]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)


[^257]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)


[^258]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)


[^259]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^260]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)


[^261]: [Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)


[^262]: [Microsoft Enable Cred Guard April 2017](https://docs.microsoft.com/windows/access-protection/credential-guard/credential-guard-manage)


[^263]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)


[^264]: [audits linikatz](https://github.com/CiscoCXSecurity/linikatz/blob/master/blue/audit/audit.rules)


[^265]: [MagicWeb](https://www.microsoft.com/security/blog/2022/08/24/magicweb-nobeliums-post-compromise-trick-to-authenticate-as-anyone/)


[^266]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^267]: [Intel Hardware-based Security Technologies](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/security-technologies-4th-gen-core-retail-paper.pdf)


[^268]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)


[^269]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)


[^270]: [ADSecurity AD Kerberos Attacks](https://adsecurity.org/?p=556)


[^271]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^272]: [store_pwd_rev_enc](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/store-passwords-using-reversible-encryption)


[^273]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)


[^274]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


[^275]: [SourceForge rkhunter](http://rkhunter.sourceforge.net)


[^276]: [Chkrootkit Main](http://www.chkrootkit.org/)


[^277]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)


[^278]: [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)


[^279]: [Apple App Security Overview](https://support.apple.com/guide/security/app-security-overview-sec35dd877d0/1/web/1)


[^280]: [Microsoft GPO Security Filtering](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)


[^281]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)


[^282]: [GitHub PSPKIAudit](https://github.com/GhostPack/PSPKIAudit)


[^283]: [Microsoft Install Password Filter n.d](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)


[^284]: [Rhino S3 Ransomware Part 2](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)


[^285]: [Microsoft Requests for Azure AD Roles in Privileged Identity Management](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/azure-ad-pim-approval-workflow)


[^286]: [Microsoft ASR Nov 2017](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)


[^287]: [Halcyon AWS Ransomware 2025](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)


[^288]: [Wikipedia Control Flow Integrity](https://en.wikipedia.org/wiki/Control-flow_integrity)


[^289]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)


[^290]: [Protecting Microsoft 365 From On-Premises Attacks](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/protect-m365-from-on-premises-attacks)


[^291]: [CloudSploit - Unused AWS Regions](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)


[^292]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)


[^293]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)


[^294]: [TechNet Secure Boot Process](https://docs.microsoft.com/en-us/windows/security/information-protection/secure-the-windows-10-boot-process)


[^295]: [Microsoft Common Conditional Access Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)


[^296]: [SpectorOps Code Signing Dec 2017](https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec)


[^297]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


[^298]: [CERT-EU DDoS March 2017](http://cert.europa.eu/static/WhitePapers/CERT-EU_Security_Whitepaper_DDoS_17-003.pdf)


[^299]: [LKM loading kernel restrictions](https://xorl.wordpress.com/2018/02/17/lkm-loading-kernel-restrictions/)


[^300]: [Microsoft File Folder Exclusions](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)


[^301]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)


[^302]: [Google Workspace Apps Script Restrict OAuth Scopes](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)


[^303]: [Microsoft GPO Bluetooth FEB 2009](https://technet.microsoft.com/library/dd252791.aspx)


[^304]: [AWS - IAM Console Best Practices](https://aws.amazon.com/blogs/security/newly-updated-features-in-the-aws-iam-console-help-you-adhere-to-iam-best-practices/)


[^305]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


[^306]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)


[^307]: [TechNet Least Privilege](https://technet.microsoft.com/en-us/library/dn487450.aspx)


[^308]: [Microsoft Developer Support Power Apps Conditional Access](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)


[^309]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)


[^310]: [Crowdstrike AWS User Federation Persistence](https://www.crowdstrike.com/blog/how-adversaries-persist-with-aws-user-federation/)


[^311]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)


[^312]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)


[^313]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)


[^314]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)


[^315]: [NSA and ASD Detect and Prevent Web Shells 2020](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)


[^316]: [Metcalf 2015](http://adsecurity.org/?p=1275)


[^317]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


[^318]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)


[^319]: [ADSecurity Kerberos and KRBTGT](https://adsecurity.org/?p=483)


[^320]: [Microsoft Securing Privileged Access](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)


[^321]: [Microsoft SMB Packet Signing](https://docs.microsoft.com/en-us/previous-versions/system-center/operations-manager-2005/cc180803(v=technet.10))


[^322]: [Joe Sec Nymaim](https://www.joesecurity.org/blog/3660886847485093803)


[^323]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)


[^324]: [Secureworks - AT.exe Scheduled Task](https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems)


[^325]: [ReasonLabs](https://cyberpedia.reasonlabs.com/EN/dead%20code%20insertion.html)


[^326]: [Microsoft WDigest Mit](https://support.microsoft.com/en-us/help/2871997/microsoft-security-advisory-update-to-improve-credentials-protection-a)


[^327]: [Microsoft PS JEA](https://learn.microsoft.com/powershell/scripting/learn/remoting/jea/overview?view=powershell-7.3)


[^328]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)


[^329]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)


[^330]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)


[^331]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)


[^332]: [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


[^333]: [Cisco Umbrella DGA Brute Force](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)


[^334]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^335]: [Bugcrowd Replay Attack](https://www.bugcrowd.com/glossary/replay-attack/)


[^336]: [TechNet RDP NLA](https://technet.microsoft.com/en-us/library/cc732713.aspx)


[^337]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)


[^338]: [Microsoft Trust Considerations Nov 2014](https://technet.microsoft.com/library/cc755321.aspx)


[^339]: [CISA MFA PrintNightmare](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)


[^340]: [Microsoft ETW May 2018](https://docs.microsoft.com/windows/desktop/etw/event-tracing-portal)


[^341]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)


[^342]: [Cybereason Dissecting DGAs](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)


[^343]: [Microsoft Dev Tunnels Group Policies](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/manage-dev-tunnels-with-group-policies/4149472)


[^344]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)


[^345]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)


[^346]: [Microsoft Dev Tunnels Group Policy Mitigation](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/policies)


[^347]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)


[^348]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)


[^349]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)


[^350]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)


[^351]: [Kaspersky CactusPete Aug 2020](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)


[^352]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)


[^353]: [AdSecurity Kerberos GT Aug 2015](https://adsecurity.org/?p=1640)


[^354]: [reagentc_cmd](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)


[^355]: [Cisco IOS Software Integrity Assurance - Change Control](https://tools.cisco.com/security/center/resources/integrity_assurance.html#31)


[^356]: [US-CERT TA17-156A SNMP Abuse 2017](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)


[^357]: [Deloitte Environment Awareness](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)


[^358]: [US-CERT Alert TA13-175A Risks of Default Passwords on the Internet](https://www.us-cert.gov/ncas/alerts/TA13-175A)


[^359]: [Wikipedia 802.1x](https://en.wikipedia.org/wiki/IEEE_802.1X)


[^360]: [Berkley Secure](https://security.berkeley.edu/node/94)


[^361]: [Microsoft Token Protection 2023](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)


[^362]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)


