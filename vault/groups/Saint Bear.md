---
aliases: 
    - Saint Bear
    - Storm-0587
    - TA471
    - UAC-0056
    - Lorec53
mitre-attack: https://attack.mitre.org/groups/G1031
---

## G1031

[Saint Bear](https://attack.mitre.org/groups/G1031) is a Russian-nexus threat actor active since early 2021, primarily targeting entities in Ukraine and Georgia. The group is notable for a specific remote access tool, [Saint Bot](https://attack.mitre.org/software/S1018), and information stealer, [OutSteel](https://attack.mitre.org/software/S1017) in campaigns. [Saint Bear](https://attack.mitre.org/groups/G1031) typically relies on phishing or web staging of malicious documents and related file types for initial access, spoofing government or related entities.[^6] [^2]  [Saint Bear](https://attack.mitre.org/groups/G1031) has previously been confused with [Ember Bear](https://attack.mitre.org/groups/G1003) operations, but analysis of behaviors, tools, and targeting indicates these are distinct clusters.

### Techniques Used
| ID | Name | Description |
| --- | --- | --- |
| [[Spearphishing Attachment\|T1566.001]] | Spearphishing Attachment | [Saint Bear](https://attack.mitre.org/groups/G1031) uses a variety of file formats, such as Microsoft Office documents, ZIP archives, PDF documents, and other items as phishing attachments for initial access.[^6]  |
| [[Exploitation for Client Execution\|T1203]] | Exploitation for Client Execution | [Saint Bear](https://attack.mitre.org/groups/G1031) has leveraged vulnerabilities in client applications such as CVE-2017-11882 in Microsoft Office to enable code execution in victim environments.[^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Saint Bear](https://attack.mitre.org/groups/G1031) has delivered malicious Microsoft Office files containing an embedded JavaScript object that would, on execution, download and execute [OutSteel](https://attack.mitre.org/software/S1017) and [Saint Bot](https://attack.mitre.org/software/S1018).[^6]  |
| [[Email Addresses\|T1589.002]] | Email Addresses | [Saint Bear](https://attack.mitre.org/groups/G1031) gathered victim email information in advance of phishing operations for targeted attacks.[^6]  |
| [[Virtualization／Sandbox Evasion\|T1497]] | Virtualization／Sandbox Evasion | [Saint Bear](https://attack.mitre.org/groups/G1031) contains several anti-analysis and anti-virtualization checks.[^6]  |
| [[Windows Command Shell\|T1059.003]] | Windows Command Shell | [Saint Bear](https://attack.mitre.org/groups/G1031) initial loaders will also drop a malicious Windows batch file, available via open source GitHub repositories, that disables Microsoft Defender functionality.[^6]  |
| [[Code Signing\|T1553.002]] | Code Signing | [Saint Bear](https://attack.mitre.org/groups/G1031) has used an initial loader malware featuring a legitimate code signing certificate associated with "Electrum Technologies GmbH."[^6]  |
| [[Malicious Link\|T1204.001]] | Malicious Link | [Saint Bear](https://attack.mitre.org/groups/G1031) has, in addition to email-based phishing attachments, used malicious websites masquerading as legitimate entities to host links to malicious files for user execution.[^6] [^2]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [Saint Bear](https://attack.mitre.org/groups/G1031) initial payloads included encoded follow-on payloads located in the resources file of the first-stage loader.[^6]  |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Saint Bear](https://attack.mitre.org/groups/G1031) will modify registry entries and scheduled task objects associated with Windows Defender to disable its functionality.[^6]  |
| [[Impersonation\|T1684.001]] | Impersonation | [Saint Bear](https://attack.mitre.org/groups/G1031) has impersonated government and related entities in both phishing activity and developing web sites with malicious links that mimic legitimate resources.[^2]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Saint Bear](https://attack.mitre.org/groups/G1031) relies extensively on PowerShell execution from malicious attachments and related content to retrieve and execute follow-on payloads.[^6]  |
| [[Malicious File\|T1204.002]] | Malicious File | [Saint Bear](https://attack.mitre.org/groups/G1031) relies on user interaction and execution of malicious attachments and similar for initial execution on victim systems.[^6]  |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | [Saint Bear](https://attack.mitre.org/groups/G1031) has used the Windows Script Host (wscript) to execute intermediate files written to victim machines.[^6]  |
| [[Web Services\|T1583.006]] | Web Services | [Saint Bear](https://attack.mitre.org/groups/G1031) has leveraged the Discord content delivery network to host malicious content for retrieval during initial access operations.[^6]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Saint Bear](https://attack.mitre.org/groups/G1031) has used the Discord content delivery network for hosting malicious content referenced in links and emails.[^6]  |
| [[Software Packing\|T1027.002]] | Software Packing | [Saint Bear](https://attack.mitre.org/groups/G1031) clones .NET assemblies from other .NET binaries as well as cloning code signing certificates from other software to obfuscate the initial loader payload.[^6]  |
| [[Modify Registry\|T1112]] | Modify Registry | [Saint Bear](https://attack.mitre.org/groups/G1031) will leverage malicious Windows batch scripts to modify registry values associated with Windows Defender functionality.[^6]  |



### Software
| ID | Name | Description |
| --- | --- | --- |
| [[Saint Bot\|S1018]] | Saint Bot | [Saint Bot](https://attack.mitre.org/software/S1018) is closely correlated with [Saint Bear](https://attack.mitre.org/groups/G1031) operations as a common post-exploitation toolset.[^6]  |
| [[OutSteel\|S1017]] | OutSteel | [OutSteel](https://attack.mitre.org/software/S1017) is uniquely associated with [Saint Bear](https://attack.mitre.org/groups/G1031) as a post-exploitation document collection and exfiltration tool.[^6]  |



## References

[^1]: TA471


[^2]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)


[^3]: UAC-0056


[^4]: Lorec53


[^5]: Storm-0587


[^6]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)


