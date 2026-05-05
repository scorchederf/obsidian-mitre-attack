---
aliases: 
    - T1176
tags: 
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1176-Software_Extensions
tactic: 
     - Persistence
platforms:
     - Linux - macOS - Windows
permissions required:
     - none
---

## Description

Adversaries may abuse software extensions to establish persistent access to victim systems. Software extensions are modular components that enhance or customize the functionality of software applications, including web browsers, Integrated Development Environments (IDEs), and other platforms.[^1] [^2]  Extensions are typically installed via official marketplaces, app stores, or manually loaded by users, and they often inherit the permissions and access levels of the host application. <br><br>  <br>Malicious extensions can be introduced through various methods, including social engineering, compromised marketplaces, or direct installation by users or by adversaries who have already gained access to a system. Malicious extensions can be named similarly or identically to benign extensions in marketplaces. Security mechanisms in extension marketplaces may be insufficient to detect malicious components, allowing adversaries to bypass automated scanners or exploit trust established during the installation process. Adversaries may also abuse benign extensions to achieve their objectives, such as using legitimate functionality to tunnel data or bypass security controls. <br><br>The modular nature of extensions and their integration with host applications make them an attractive target for adversaries seeking to exploit trusted software ecosystems. Detection can be challenging due to the inherent trust placed in extensions during installation and their ability to blend into normal application workflows. 




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-User_Training\|M1017]] | User Training | Train users to minimize extension use, and to only install trusted extensions.  |
| [[kb/mitre/attack/mitigations/M1033-Limit_Software_Installation\|M1033]] | Limit Software Installation | Only install extensions from trusted sources that can be verified. |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Set an extension allow or deny list as appropriate for your security policy.  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Ensure extensions that are installed are the intended ones, as many malicious extensions may masquerade as legitimate ones.  |
| [[kb/mitre/attack/mitigations/M1051-Update_Software\|M1051]] | Update Software | Ensure operating systems and software are using the most current version.  |




## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1176.001-Browser_Extensions\|T1176.001]] | Browser Extensions |
| [[kb/mitre/attack/techniques/T1176.002-IDE_Extensions\|T1176.002]] | IDE Extensions |




> [!info]- References
> [^1]: [Chrome Extension C2 Malware](https://web.archive.org/web/20240608001937/https://kjaer.io/extension-malware/)

> [^2]: [Abramovsky VSCode Security](https://blog.checkpoint.com/securing-the-cloud/malicious-vscode-extensions-with-more-than-45k-downloads-steal-pii-and-enable-backdoors/)

> [^3]: [xorrior chrome extensions macOS](https://www.xorrior.com/No-Place-Like-Chrome/)


