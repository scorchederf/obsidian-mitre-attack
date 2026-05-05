---
aliases: 
    - M1048
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1048-Application_Isolation_and_Sandboxing
---

## Description

Application Isolation and Sandboxing refers to the technique of restricting the execution of code to a controlled and isolated environment (e.g., a virtual environment, container, or sandbox). This method prevents potentially malicious code from affecting the rest of the system or network by limiting access to sensitive resources and critical operations. The goal is to contain threats and minimize their impact. This mitigation can be implemented through the following measures:<br><br>Browser Sandboxing:<br><br>- Use Case: Implement browser sandboxing to isolate untrusted web content and prevent malicious web pages or scripts from accessing sensitive system resources or initiating unauthorized downloads.<br>- Implementation: Use browsers with built-in sandboxing features (e.g., Google Chrome, Microsoft Edge) or deploy enhanced browser security frameworks that limit the execution scope of active content. Consider controls that monitor or restrict script-based file generation and downloads commonly abused in evasion techniques like HTML smuggling.<br><br>Application Virtualization:<br><br>- Use Case: Deploy critical or high-risk applications in a virtualized environment to ensure any compromise does not affect the host system.<br>- Implementation: Use application virtualization platforms to run applications in isolated environments.<br><br>Email Attachment Sandboxing:<br><br>- Use Case: Route email attachments to a sandbox environment to detect and block malware before delivering emails to end-users.<br>- Implementation: Integrate security solutions with sandbox capabilities to analyze email attachments.<br><br>Endpoint Sandboxing:<br><br>- Use Case: Run all downloaded files and applications in a restricted environment to monitor their behavior for malicious activity.<br>- Implementation: Use endpoint protection tools for sandboxing at the endpoint level.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1021.003-Distributed_Component_Object_Model\|T1021.003]] | Distributed Component Object Model | Ensure all COM alerts and Protected View are enabled.[^2]  |
| [[kb/mitre/attack/techniques/T1027.006-HTML_Smuggling\|T1027.006]] | HTML Smuggling | Use Browser Extensions or Built-in Security Tools that:<br><br>- Monitor JavaScript API calls such as `Blob`, `URL.createObjectURL,` and `msSaveOrOpenBlob`<br>- Intercept and analyze HTML5 `download` attributes for suspicious payload generation<br>- Alert or block behaviors that match known HTML smuggling patterns (e.g., blob-to-disk payload construction)<br><br>Apply Content Security Policy (CSP) headers to:<br><br>- Restrict inline JavaScript and dynamic script generation<br>- Disallow downloads from unauthorized sources or blob URIs<br>- Prevent cross-origin resource sharing (CORS) abuse commonly used in smuggling chains<br><br>Enable or enforce enterprise browser security controls, such as:<br><br>- Endpoint's Network Protection and Attack Surface Reduction (ASR) rules, which can block Office and browser processes from creating child processes or writing to disk in suspicious ways<br>- Google Chrome Enterprise Policies, which can control file download behavior, restrict extensions, and isolate risky browsing environments<br><br>Deploy browser sandboxing solutions that can isolate JavaScript execution environments and enforce behavioral policy restrictions |
| [[kb/mitre/attack/techniques/T1027.017-SVG_Smuggling\|T1027.017]] | SVG Smuggling | Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist.  |
| [[kb/mitre/attack/techniques/T1068-Exploitation_for_Privilege_Escalation\|T1068]] | Exploitation for Privilege Escalation | Make it difficult for adversaries to advance their operation through exploitation of undiscovered or unpatched vulnerabilities by using sandboxing. Other types of virtualization and application microsegmentation may also mitigate the impact of some types of exploitation. Risks of additional exploits and weaknesses in these systems may still exist. [^4]  |
| [[kb/mitre/attack/techniques/T1189-Drive-by_Compromise\|T1189]] | Drive-by Compromise | Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist.[^1] [^4] <br><br>Other types of virtualization and application microsegmentation may also mitigate the impact of client-side exploitation. The risks of additional exploits and weaknesses in implementation may still exist for these types of systems.[^4]  |
| [[kb/mitre/attack/techniques/T1190-Exploit_Public-Facing_Application\|T1190]] | Exploit Public-Facing Application | Application isolation will limit what other processes and system features the exploited target can access. |
| [[kb/mitre/attack/techniques/T1203-Exploitation_for_Client_Execution\|T1203]] | Exploitation for Client Execution | Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist. [^1]  [^4] <br><br>Other types of virtualization and application microsegmentation may also mitigate the impact of client-side exploitation. Risks of additional exploits and weaknesses in those systems may still exist. [^4]  |
| [[kb/mitre/attack/techniques/T1210-Exploitation_of_Remote_Services\|T1210]] | Exploitation of Remote Services | Make it difficult for adversaries to advance their operation through exploitation of undiscovered or unpatched vulnerabilities by using sandboxing. Other types of virtualization and application microsegmentation may also mitigate the impact of some types of exploitation. Risks of additional exploits and weaknesses in these systems may still exist. [^4]  |
| [[kb/mitre/attack/techniques/T1211-Exploitation_for_Stealth\|T1211]] | Exploitation for Stealth | Make it difficult for adversaries to advance their operation through exploitation of undiscovered or unpatched vulnerabilities by using sandboxing. Other types of virtualization and application microsegmentation may also mitigate the impact of some types of exploitation. Risks of additional exploits and weaknesses in these systems may still exist. [^4]  |
| [[kb/mitre/attack/techniques/T1212-Exploitation_for_Credential_Access\|T1212]] | Exploitation for Credential Access | Make it difficult for adversaries to advance their operation through exploitation of undiscovered or unpatched vulnerabilities by using sandboxing. Other types of virtualization and application microsegmentation may also mitigate the impact of some types of exploitation. Risks of additional exploits and weaknesses in these systems may still exist.[^4]  |
| [[kb/mitre/attack/techniques/T1559-Inter-Process_Communication\|T1559]] | Inter-Process Communication | Ensure all COM alerts and Protected View are enabled.[^2]  |
| [[kb/mitre/attack/techniques/T1559.001-Component_Object_Model\|T1559.001]] | Component Object Model | Ensure all COM alerts and Protected View are enabled.[^2]  |
| [[kb/mitre/attack/techniques/T1559.002-Dynamic_Data_Exchange\|T1559.002]] | Dynamic Data Exchange | Ensure Protected View is enabled.[^2]  |
| [[kb/mitre/attack/techniques/T1611-Escape_to_Host\|T1611]] | Escape to Host | Consider utilizing seccomp, seccomp-bpf, or a similar solution that restricts certain system calls such as mount. In Kubernetes environments, consider defining Pod Security Standards that limit container access to host process namespaces, the host network, and the host file system.[^3]  |



> [!info]- References
> [^1]: [Windows Blogs Microsoft Edge Sandbox](https://blogs.windows.com/msedgedev/2017/03/23/strengthening-microsoft-edge-sandbox/)

> [^2]: [Microsoft Protected View](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)

> [^3]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

> [^4]: [Ars Technica Pwn2Own 2017 VM Escape](https://arstechnica.com/information-technology/2017/03/hack-that-escapes-vm-by-exploiting-edge-browser-fetches-105000-at-pwn2own/)


