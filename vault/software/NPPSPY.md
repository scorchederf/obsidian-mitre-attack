---
aliases: 
    - S1131
    
mitre-attack: https://attack.mitre.org/software/S1131
---

## S1131

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.[^2] [^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Impersonation\|T1684.001]] | Impersonation | [NPPSPY](https://attack.mitre.org/software/S1131) creates a network listener using the misspelled label `logincontroll` recorded to the Registry key `HKLM\\SYSTEM\\CurrentControlSet\\Control\\NetworkProvider\\Order`.[^2]  |
| [[Modify Registry\|T1112]] | Modify Registry | [NPPSPY](https://attack.mitre.org/software/S1131) modifies the Registry to record the malicious listener for output from the Winlogon process.[^2]  |
| [[Data from Local System\|T1005]] | Data from Local System | [NPPSPY](https://attack.mitre.org/software/S1131) records data entered from the local system logon at Winlogon to capture credentials in cleartext.[^2]  |
| [[Adversary-in-the-Middle\|T1557]] | Adversary-in-the-Middle | [NPPSPY](https://attack.mitre.org/software/S1131) opens a new network listener for the `mpnotify.exe` process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.[^2]  |
| [[Unsecured Credentials\|T1552]] | Unsecured Credentials | [NPPSPY](https://attack.mitre.org/software/S1131) captures credentials by recording them through an alternative network listener registered to the `mpnotify.exe` process, allowing for cleartext recording of logon information.[^2]  |
| [[Input Capture\|T1056]] | Input Capture | [NPPSPY](https://attack.mitre.org/software/S1131) captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.[^2]  |
| [[Automated Collection\|T1119]] | Automated Collection | [NPPSPY](https://attack.mitre.org/software/S1131) collection is automatically recorded to a specified file on the victim machine.[^2]  |




## References

[^1]: [Polak NPPSPY 2004](https://www.blackhat.com/presentations/win-usa-04/bh-win-04-polak/bh-win-04-polak2.pdf)


[^2]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)


