---
aliases: 
    - S1129
    
mitre-attack: https://attack.mitre.org/software/S1129
---

## S1129

[Akira](https://attack.mitre.org/software/S1129) ransomware, written in C++, is most prominently (but not exclusively) associated with the ransomware-as-a-service entity [Akira](https://attack.mitre.org/groups/G1024). [Akira](https://attack.mitre.org/software/S1129) ransomware has been used in attacks across North America, Europe, and Australia, with a focus on critical infrastructure sectors including manufacturing, education, and IT services. [Akira](https://attack.mitre.org/software/S1129) ransomware employs hybrid encryption and threading to increase the speed and efficiency of encryption and runtime arguments for tailored attacks. Notable variants include Rust-based [Megazord](https://attack.mitre.org/software/S1191) for targeting Windows and [Akira _v2](https://attack.mitre.org/software/S1194) for targeting VMware ESXi servers.[^1] [^3] [^2] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [Akira](https://attack.mitre.org/software/S1129) examines files prior to encryption to determine if they meet requirements for encryption and can be encrypted by the ransomware. These checks are performed through native Windows functions such as `GetFileAttributesW`.[^1] [^2]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Akira](https://attack.mitre.org/software/S1129) uses the `GetSystemInfo` Windows function to determine the number of processors on a victim machine.[^1]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Akira](https://attack.mitre.org/software/S1129) will execute PowerShell commands to delete system volume shadow copies.[^1] [^3] <br> |
| [[Windows Management Instrumentation\|T1047]] | Windows Management Instrumentation | [Akira](https://attack.mitre.org/software/S1129) will leverage COM objects accessed through WMI during execution to evade detection.[^1]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Akira](https://attack.mitre.org/software/S1129) executes from the Windows command line and can take various arguments for execution.[^1]  |
| [[Network Share Discovery\|T1135]] | Network Share Discovery | [Akira](https://attack.mitre.org/software/S1129) can identify remote file shares for encryption.[^1]  |
| [[Native API\|T1106]] | Native API | [Akira](https://attack.mitre.org/software/S1129) executes native Windows functions such as `GetFileAttributesW` and `GetSystemInfo`.[^1]  |
| [[Inhibit System Recovery\|T1490]] | Inhibit System Recovery | [Akira](https://attack.mitre.org/software/S1129) will delete system volume shadow copies via PowerShell commands.[^1] [^3]  |
| [[Process Discovery\|T1057]] | Process Discovery | [Akira](https://attack.mitre.org/software/S1129) verifies the deletion of volume shadow copies by checking for the existence of the process ID related to the process created to delete these items.[^1]  |
| [[Data Encrypted for Impact\|T1486]] | Data Encrypted for Impact | [Akira](https://attack.mitre.org/software/S1129) can encrypt victim filesystems for financial extortion purposes including through the use of the ChaCha20 and ChaCha8 stream ciphers.[^1] [^3] [^2] <br> |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Akira\|G1024]] | Akira |



## References

[^1]: [Kersten Akira 2023](https://www.trellix.com/blogs/research/akira-ransomware/)


[^2]: [Cisco Akira Ransomware OCT 2024](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)


[^3]: [CISA Akira Ransomware APR 2024](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)


