---
aliases: 
    - M1051
    
mitre-attack: https://attack.mitre.org/mitigations/M1051
---

## M1051

Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures:<br><br>Regular Operating System Updates<br><br>- Implementation: Apply the latest Windows security updates monthly using WSUS (Windows Server Update Services) or a similar patch management solution. Configure systems to check for updates automatically and schedule reboots during maintenance windows.<br>- Use Case: Prevents exploitation of OS vulnerabilities such as privilege escalation or remote code execution.<br><br>Application Patching<br><br>- Implementation: Monitor Apache's update release notes for security patches addressing vulnerabilities. Schedule updates for off-peak hours to avoid downtime while maintaining security compliance.<br>- Use Case: Prevents exploitation of web application vulnerabilities, such as those leading to unauthorized access or data breaches.<br><br>Firmware Updates<br><br>- Implementation: Regularly check the vendor’s website for firmware updates addressing vulnerabilities. Plan for update deployment during scheduled maintenance to minimize business disruption.<br>- Use Case: Protects against vulnerabilities that adversaries could exploit to gain access to network devices or inject malicious traffic.<br><br>Emergency Patch Deployment<br><br>- Implementation: Use the emergency patch deployment feature of the organization's patch management tool to apply updates to all affected Exchange servers within 24 hours.<br>- Use Case: Reduces the risk of exploitation by rapidly addressing critical vulnerabilities.<br><br>Centralized Patch Management<br><br>- Implementation: Implement a centralized patch management system, such as SCCM or ManageEngine, to automate and track patch deployment across all environments. Generate regular compliance reports to ensure all systems are updated.<br>- Use Case: Streamlines patching processes and ensures no critical systems are missed.<br><br>*Tools for Implementation*<br><br>Patch Management Tools:<br><br>- WSUS: Manage and deploy Microsoft updates across the organization.<br>- ManageEngine Patch Manager Plus: Automate patch deployment for OS and third-party apps.<br>- Ansible: Automate updates across multiple platforms, including Linux and Windows.<br><br>Vulnerability Scanning Tools:<br><br>- OpenVAS: Open-source vulnerability scanning to identify missing patches.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Pass the Hash\|T1550.002]] | Pass the Hash | Apply patch KB2871997 to Windows 7 and higher systems to limit the default access of accounts in the local administrator group.[^7]   |
| [[Network Device Firewall\|T1686.002]] | Network Device Firewall | Ensure the network firewall is up to date with security patches. |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Apply patch KB2962486 which prevents credentials from being stored in GPPs.[^4] [^3]  |
| [[IDE Extensions\|T1176.002]] | IDE Extensions | Ensure operating systems and IDEs are using the most current version.  |
| [[Bypass User Account Control\|T1548.002]] | Bypass User Account Control | Consider updating Windows to the latest version and patch level to utilize the latest protective measures against UAC bypass.[^2]  |
| [[SNMP (MIB Dump)\|T1602.001]] | SNMP (MIB Dump) | Keep system images and software updated and migrate to SNMPv3.[^8]  |
| [[Exploitation for Privilege Escalation\|T1068]] | Exploitation for Privilege Escalation | Update software regularly by employing patch management for internal enterprise endpoints and servers. |
| [[Password Managers\|T1555.005]] | Password Managers | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| [[Firmware Corruption\|T1495]] | Firmware Corruption | Patch the BIOS and other firmware as necessary to prevent successful use of known vulnerabilities. |
| [[Password Guessing\|T1110.001]] | Password Guessing | Upgrade management services to the latest supported and compatible version.  Specifically, any version providing increased password complexity or policy enforcement preventing default or weak passwords.  |
| [[Credentials from Password Stores\|T1555]] | Credentials from Password Stores | Perform regular software updates to mitigate exploitation risk. |
| [[Escape to Host\|T1611]] | Escape to Host | Ensure that hosts are kept up-to-date with security patches.  |
| [[Software Deployment Tools\|T1072]] | Software Deployment Tools | Patch deployment systems regularly to prevent potential remote access through [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068). |
| [[Outlook Home Page\|T1137.004]] | Outlook Home Page | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[^6]  Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[^1]  |
| [[Pre-OS Boot\|T1542]] | Pre-OS Boot | Patch the BIOS and EFI as necessary. |
| [[System Firmware\|T1542.001]] | System Firmware | Patch the BIOS and EFI as necessary. |
| [[Exploitation for Credential Access\|T1212]] | Exploitation for Credential Access | Update software regularly by employing patch management for internal enterprise endpoints and servers. |
| [[Data from Configuration Repository\|T1602]] | Data from Configuration Repository | Keep system images and software updated and migrate to SNMPv3.[^8]  |
| [[Drive-by Compromise\|T1189]] | Drive-by Compromise | Ensuring that all browsers and plugins are kept updated can help prevent the exploit phase of this technique. Use modern browsers with security features turned on.[^5] <br> |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | Perform regular software updates to mitigate exploitation risk. |
| [[Exploitation for Stealth\|T1211]] | Exploitation for Stealth | Update software regularly by employing patch management for internal enterprise endpoints and servers. |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | Update software regularly to include patches that fix DLL side-loading vulnerabilities. |
| [[Browser Extensions\|T1176.001]] | Browser Extensions | Ensure operating systems and browsers are using the most current version.  |
| [[Office Application Startup\|T1137]] | Office Application Startup | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[^6]  Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[^1]  |
| [[Compromise Software Dependencies and Development Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. |
| [[Group Policy Preferences\|T1552.006]] | Group Policy Preferences | Apply patch KB2962486 which prevents credentials from being stored in GPPs.[^4] [^3]  |
| [[Outlook Rules\|T1137.005]] | Outlook Rules | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[^6]  Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[^1]  |
| [[Supply Chain Compromise\|T1195]] | Supply Chain Compromise | A patch management process should be implemented to check unused dependencies, unmaintained and/or previously vulnerable dependencies, unnecessary features, components, files, and documentation. |
| [[Steal Web Session Cookie\|T1539]] | Steal Web Session Cookie | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| [[Credentials from Web Browsers\|T1555.003]] | Credentials from Web Browsers | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| [[Network Device Configuration Dump\|T1602.002]] | Network Device Configuration Dump | Keep system images and software updated and migrate to SNMPv3.[^8]  |
| [[AppInit DLLs\|T1546.010]] | AppInit DLLs | Upgrade to Windows 8 or later and enable secure boot. |
| [[DLL\|T1574.001]] | DLL | Update software regularly to include patches that fix DLL side-loading vulnerabilities. |
| [[Software Extensions\|T1176]] | Software Extensions | Ensure operating systems and software are using the most current version.  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | Perform regular software updates to mitigate exploitation risk. Keeping software up-to-date with the latest security patches helps prevent adversaries from exploiting known vulnerabilities in client software, reducing the risk of successful attacks. |
| [[Component Firmware\|T1542.002]] | Component Firmware | Perform regular firmware updates to mitigate risks of exploitation and/or abuse. |
| [[Outlook Forms\|T1137.003]] | Outlook Forms | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[^6]  Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[^1]  |
| [[Exploit Public-Facing Application\|T1190]] | Exploit Public-Facing Application | Update software regularly by employing patch management for externally exposed applications. |
| [[Compromise Software Supply Chain\|T1195.002]] | Compromise Software Supply Chain | A patch management process should be implemented to check unused applications, unmaintained and/or previously vulnerable software, unnecessary features, components, files, and documentation. |
| [[Exploitation of Remote Services\|T1210]] | Exploitation of Remote Services | Update software regularly by employing patch management for internal enterprise endpoints and servers. |
| [[Application Shimming\|T1546.011]] | Application Shimming | Microsoft released an optional patch update - KB3045645 - that will remove the "auto-elevate" flag within the sdbinst.exe. This will prevent use of application shimming to bypass UAC. |
| [[Event Triggered Execution\|T1546]] | Event Triggered Execution | Perform regular software updates to mitigate exploitation risk. |


## References

[^1]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)


[^2]: [Github UACMe](https://github.com/hfiref0x/UACME)


[^3]: [MS14-025](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)


[^4]: [ADSecurity Finding Passwords in SYSVOL](https://adsecurity.org/?p=2288)


[^5]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)


[^6]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)


[^7]: [NSA Spotting](https://massarobi.wordpress.com/wp-content/uploads/2017/03/spotting-the-adversary-with-windows-event-log-monitoring.pdf)


[^8]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)


