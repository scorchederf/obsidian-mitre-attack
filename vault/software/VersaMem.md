---
aliases: 
    - S1154
    
mitre-attack: https://attack.mitre.org/software/S1154
---

## S1154

[VersaMem](https://attack.mitre.org/software/S1154) is a web shell designed for deployment to Versa Director servers following exploitation. Discovered in August 2024, [VersaMem](https://attack.mitre.org/software/S1154) was used during [Versa Director Zero Day Exploitation](https://attack.mitre.org/campaigns/C0039) by [Volt Typhoon](https://attack.mitre.org/groups/G1017) to target ISPs and MSPs.  [VersaMem](https://attack.mitre.org/software/S1154) is deployed as a Java Archive (JAR) and allows for credential capture for Versa Director logon activity as well as follow-on execution of arbitrary Java payloads.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Credential API Hooking\|T1056.004]] | Credential API Hooking | [VersaMem](https://attack.mitre.org/software/S1154) hooked and overrided Versa's built-in authentication method, `setUserPassword`, to intercept plaintext credentials when submitted to the server.[^1]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [VersaMem](https://attack.mitre.org/software/S1154) was installed through exploitation of CVE-2024-39717 in Versa Director servers.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [VersaMem](https://attack.mitre.org/software/S1154) encrypted captured credentials with AES then Base64 encoded them before writing to local storage.[^1]  |
| [[File Deletion\|T1070.004]] | File Deletion | [VersaMem](https://attack.mitre.org/software/S1154) deleted files related to initial installation such as temporary files related to the PID of the main web process.[^1]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [VersaMem](https://attack.mitre.org/software/S1154) was delivered as a Java Archive (JAR) that runs by attaching itself to the Apache Tomcat Java servlet and web server.[^1]  |
| [[Local Data Staging\|T1074.001]] | Local Data Staging | [VersaMem](https://attack.mitre.org/software/S1154) staged captured credentials locally at `/tmp/.temp.data`.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [VersaMem](https://attack.mitre.org/software/S1154) hooked the Catalina application filter chain `doFilter` on compromised systems to monitor all inbound requests to the local Tomcat web server, inspecting them for parameters like passwords and follow-on Java modules.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [VersaMem](https://attack.mitre.org/software/S1154) relied on the Java Instrumentation API and Javassist to dynamically modify Java code existing in memory.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[Volt Typhoon\|G1017]] | Volt Typhoon |



## References

[^1]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)


