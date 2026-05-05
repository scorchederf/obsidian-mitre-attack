---
aliases: 
    - M1022
    
mitre-attack: https://attack.mitre.org/mitigations/M1022
---

## M1022

Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.<br><br>Enforce Least Privilege Permissions:<br><br>- Remove unnecessary write permissions on sensitive files and directories.<br>- Use file ownership and groups to control access for specific roles.<br><br>Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs.<br><br>Harden File Shares:<br><br>- Disable anonymous access to shared folders.<br>- Enforce NTFS permissions for shared folders on Windows.<br><br>Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access.<br><br>On Linux, apply:<br>`chmod 750 /etc/sensitive.conf`<br>`chown root:admin /etc/sensitive.conf`<br><br>File Integrity Monitoring (FIM):<br><br>- Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions.<br><br>Audit File System Access:<br><br>- Enable auditing to track permission changes or unauthorized access attempts.<br>- Use auditd (Linux) or Event Viewer (Windows) to log activities.<br><br>Restrict Startup Directories:<br><br>- Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`.<br><br>Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`.<br><br>- On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F`<br>- On Linux, monitor permissions using tools like `lsattr` or `auditd`.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | Use file system access controls to protect folders such as `C:\Windows\System32`. |
| [[Stored Data Manipulation\|T1565.001]] | Stored Data Manipulation | Ensure least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. |
| [[RC Scripts\|T1037.004]] | RC Scripts | Limit privileges of user accounts so only authorized users can edit the `rc.common` file. |
| [[Linux and Mac Permissions\|T1222.002]] | Linux and Mac Permissions | Applying more restrictive permissions to files and directories could prevent adversaries from modifying the access control lists. |
| [[Startup Items\|T1037.005]] | Startup Items | Since StartupItems are deprecated, preventing all users from writing to the `/Library/StartupItems` directory would prevent any startup items from getting registered. |
| [[Systemd Timers\|T1053.006]] | Systemd Timers | Restrict read/write access to systemd `.timer` unit files to only select privileged users who have a legitimate need to manage system services. |
| [[Control Panel\|T1218.002]] | Control Panel | Restrict storage and execution of Control Panel items to protected directories, such as `C:\Windows`, rather than user directories. |
| [[Time Providers\|T1547.003]] | Time Providers | Consider using Group Policy to configure and block additions/modifications to W32Time DLLs. [^1]  |
| [[Dylib Hijacking\|T1574.004]] | Dylib Hijacking | Set directory access controls to prevent file writes to the search paths for applications, both in the folders where applications are run from and the standard dylib folders. |
| [[Windows Permissions\|T1222.001]] | Windows Permissions | Applying more restrictive permissions to files and directories could prevent adversaries from modifying the access control lists. |
| [[Network Logon Script\|T1037.003]] | Network Logon Script | Restrict write access to logon scripts to specific administrators. |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[SSH Authorized Keys\|T1098.004]] | SSH Authorized Keys | Restrict access to the `authorized_keys` file. |
| [[Runtime Data Manipulation\|T1565.003]] | Runtime Data Manipulation | Prevent critical business and system processes from being replaced, overwritten, or reconfigured to load potentially malicious code. |
| [[Private Keys\|T1552.004]] | Private Keys | Ensure permissions are properly set on folders containing sensitive private keys to prevent unintended access. Additionally, on Cisco devices, set the `nonexportable` flag during RSA key pair generation.[^4]  |
| [[Proc Memory\|T1055.009]] | Proc Memory | Restrict the permissions on sensitive files such as `/proc/[pid]/maps` or `/proc/[pid]/mem`.  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[Path Interception by PATH Environment Variable\|T1574.007]] | Path Interception by PATH Environment Variable | Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory `C:` and system directories, such as `C:\Windows\`, to reduce places where malicious files could be placed for execution. Require that all executables be placed in write-protected directories. |
| [[XDG Autostart Entries\|T1547.013]] | XDG Autostart Entries | Restrict write access to XDG autostart entries to only select privileged users. |
| [[NTFS File Attributes\|T1564.004]] | NTFS File Attributes | Consider adjusting read and write permissions for NTFS EA, though this should be tested to ensure routine OS operations are not impeded. [^6]  |
| [[Launch Agent\|T1543.001]] | Launch Agent | Set group policies to restrict file permissions to the `~/launchagents` folder.[^3]  |
| [[Path Interception by Search Order Hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory `C:` and system directories, such as `C:\Windows\`, to reduce places where malicious files could be placed for execution. Require that all executables be placed in write-protected directories. |
| [[PowerShell Profile\|T1546.013]] | PowerShell Profile | Making PowerShell profiles immutable and only changeable by certain administrators will limit the ability for adversaries to easily create user level persistence. |
| [[Indicator Removal\|T1070]] | Indicator Removal | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[Account Manipulation\|T1098]] | Account Manipulation | Restrict access to potentially sensitive files that deal with authentication and/or authorization. |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | Install software in write-protected locations. Set directory access controls to prevent file writes to the search paths for applications, both in the folders where applications are run from and the standard library folders. |
| [[Masquerading\|T1036]] | Masquerading | Use file system access controls to protect folders such as C:\\Windows\\System32. |
| [[Shortcut Modification\|T1547.009]] | Shortcut Modification | Applying strict permissions to directories where shortcuts are stored, such as the startup folder, can prevent unauthorized modifications. |
| [[File and Directory Permissions Modification\|T1222]] | File and Directory Permissions Modification | Applying more restrictive permissions to files and directories could prevent adversaries from modifying their access control lists. Additionally, ensure that user settings regarding local and remote symbolic links are properly set or disabled where unneeded.[^5]  |
| [[Scheduled Task／Job\|T1053]] | Scheduled Task／Job | Restrict access by setting directory and file permissions that are not specific to users or privileged accounts. |
| [[SSH Hijacking\|T1563.001]] | SSH Hijacking | Ensure proper file permissions are set and harden system to prevent root privilege escalation opportunities. |
| [[Clear Mailbox Data\|T1070.008]] | Clear Mailbox Data | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities.  |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | The sudoers file should be strictly edited such that passwords are always required and that users can't spawn risky processes as users with higher privilege. |
| [[Clear Persistence\|T1070.009]] | Clear Persistence | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities.  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | Restrict file shares to specific directories with access only to necessary users. |
| [[Systemd Service\|T1543.002]] | Systemd Service | Restrict read/write access to systemd unit files to only select privileged users who have a legitimate need to manage system services. |
| [[Clear Command History\|T1070.003]] | Clear Command History | Preventing users from deleting or writing to certain files can stop adversaries from maliciously altering their `~/.bash_history` or `ConsoleHost_history.txt` files. |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | Restrict read/write access to system-level process files to only select privileged users who have a legitimate need to manage system services. |
| [[Login Hook\|T1037.002]] | Login Hook | Restrict write access to logon scripts to specific administrators. |
| [[Clear Linux or Mac System Logs\|T1685.006]] | Clear Linux or Mac System Logs | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Restrict write access to the `/Library/Security/SecurityAgentPlugins` directory. |
| [[Abuse Elevation Control Mechanism\|T1548]] | Abuse Elevation Control Mechanism | The sudoers file should be strictly edited such that passwords are always required and that users can't spawn risky processes as users with higher privilege. |
| [[Unix Shell Configuration Modification\|T1546.004]] | Unix Shell Configuration Modification | Making these files immutable and only changeable by certain administrators will limit the ability for adversaries to easily create user level persistence. |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | Use access control lists on storage systems and objects. |
| [[AppDomainManager\|T1574.014]] | AppDomainManager | Install .NET applications and related software in write-protected locations. Set directory access controls to prevent file writes to the search paths for .NET applications, both in the folders where applications are run from and the standard resources folders. |
| [[Path Interception by Unquoted Path\|T1574.009]] | Path Interception by Unquoted Path | Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory `C:` and system directories, such as `C:\Windows\`, to reduce places where malicious files could be placed for execution. Require that all executables be placed in write-protected directories. |
| [[Data Manipulation\|T1565]] | Data Manipulation | Ensure least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. |
| [[System Services\|T1569]] | System Services | Ensure that high permission level service binaries cannot be replaced or modified by users with a lower permission level. |
| [[Service Execution\|T1569.002]] | Service Execution | Ensure that high permission level service binaries cannot be replaced or modified by users with a lower permission level. |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | Restrict write access to logon scripts to specific administrators. |
| [[Clear Windows Event Logs\|T1685.005]] | Clear Windows Event Logs | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[Service Stop\|T1489]] | Service Stop | Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | Use access control lists on cloud storage systems and objects.  |
| [[Rename Legitimate Utilities\|T1036.003]] | Rename Legitimate Utilities | Use file system access controls to protect folders such as `C:\Windows\System32`.  |
| [[Taint Shared Content\|T1080]] | Taint Shared Content | Protect shared folders by minimizing users who have write access. |
| [[SIP and Trust Provider Hijacking\|T1553.003]] | SIP and Trust Provider Hijacking | Restrict storage and execution of SIP DLLs to protected directories, such as C:\\Windows, rather than user directories. |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with logging or deleting or modifying .evtx logging files. Ensure .evtx files, which are located at `C:\Windows\system32\Winevt\Logs`[^2] , have the proper file permissions for limited, legitimate access and audit policies for detection.  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | Restrict file shares to specific directories with access only to necessary users. |
| [[TCC Manipulation\|T1548.006]] | TCC Manipulation | When using an MDM, ensure the permissions granted are specific to the requirements of the binary. Full Disk Access should be restricted to only necessary binaries in alignment with policy.  |


## References

[^1]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^2]: [win_xml_evt_log](https://forensicswiki.xyz/wiki/index.php?title=Windows_XML_Event_Log_(EVTX))


[^3]: [piazza launch agent mitigation](https://antman1p-30185.medium.com/defeating-malicious-launch-persistence-156e2b40fc67)


[^4]: [cisco_deploy_rsa_keys](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_conn_pki/configuration/xe-17/sec-pki-xe-17-book/sec-deploy-rsa-pki.html#GUID-1CB802D8-9DE3-447F-BECE-CF22F5E11436)


[^5]: [create_sym_links](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)


[^6]: [InsiderThreat NTFS EA Oct 2017](https://blog.stealthbits.com/attack-step-3-persistence-ntfs-extended-attributes-file-system-attacks)


