---
aliases: 
    - M1024
    
mitre-attack: https://attack.mitre.org/mitigations/M1024
---

## M1024

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:<br><br>Review and Adjust Permissions on Critical Keys<br><br>- Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.<br>- Use tools like `icacls` or `PowerShell` to automate permission adjustments.<br><br>Enable Registry Auditing<br><br>- Enable auditing on sensitive keys to log access attempts.<br>- Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity.<br>- Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable`<br><br>Protect Credential-Related Hives<br><br>- Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access.<br>- Use LSA Protection to add an additional security layer for credential storage.<br><br>Restrict Registry Editor Usage<br><br>- Use Group Policy to restrict access to regedit.exe for non-administrative users.<br>- Block execution of registry editing tools on endpoints where they are unnecessary.<br><br>Deploy Baseline Configuration Tools<br><br>- Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations.<br><br>*Tools for Implementation* <br><br>Registry Permission Tools:<br><br>- Registry Editor (regedit): Built-in tool to manage registry permissions.<br>- PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"`<br>- icacls: Command-line tool to modify ACLs.<br><br>Monitoring Tools:<br><br>- Sysmon: Monitor and log registry events.<br>- Event Viewer: View registry access logs.<br><br>Policy Management Tools:<br><br>- Group Policy Management Console (GPMC): Enforce registry permissions via GPOs.<br>- Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Time Providers\|T1547.003]] | Time Providers | Consider using Group Policy to configure and block modifications to W32Time parameters in the Registry. [^1]  |
| [[COR_PROFILER\|T1574.012]] | COR_PROFILER | Ensure proper permissions are set for Registry hives to prevent users from modifying keys associated with COR_PROFILER. |
| [[Logon Script (Windows)\|T1037.001]] | Logon Script (Windows) | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |
| [[Network Provider DLL\|T1556.008]] | Network Provider DLL | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[Modify Authentication Process\|T1556]] | Modify Authentication Process | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[Disable or Modify System Firewall\|T1686]] | Disable or Modify System Firewall | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[Server Software Component\|T1505]] | Server Software Component | Consider using Group Policy to configure and block modifications to service and other critical server parameters in the Registry.[^2]  |
| [[Terminal Services DLL\|T1505.005]] | Terminal Services DLL | Consider using Group Policy to configure and block modifications to Terminal Services parameters in the Registry.[^2]  |
| [[Disable or Modify Windows Event Log\|T1685.001]] | Disable or Modify Windows Event Log | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering logging. The addition of the MiniNT registry key disables Event Viewer.[^3]  |
| [[Services Registry Permissions Weakness\|T1574.011]] | Services Registry Permissions Weakness | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.  |
| [[Clear Network Connection History and Configurations\|T1070.007]] | Clear Network Connection History and Configurations | Protect generated event files and logs that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[Modify Registry\|T1112]] | Modify Registry | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[Hijack Execution Flow\|T1574]] | Hijack Execution Flow | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[SIP and Trust Provider Hijacking\|T1553.003]] | SIP and Trust Provider Hijacking | Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented.  |
| [[Boot or Logon Initialization Scripts\|T1037]] | Boot or Logon Initialization Scripts | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |
| [[Subvert Trust Controls\|T1553]] | Subvert Trust Controls | Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented. |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[Windows Host Firewall\|T1686.003]] | Windows Host Firewall | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[Service Stop\|T1489]] | Service Stop | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[Code Signing Policy Modification\|T1553.006]] | Code Signing Policy Modification | Ensure proper permissions are set for the Registry to prevent users from modifying keys related to code signing policies. |


## References

[^1]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)


[^2]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)


[^3]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)


