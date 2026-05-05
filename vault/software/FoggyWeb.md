---
aliases: 
    - S0661
    
mitre-attack: https://attack.mitre.org/software/S0661
---

## S0661

[FoggyWeb](https://attack.mitre.org/software/S0661) is a passive and highly-targeted backdoor capable of remotely exfiltrating sensitive information from a compromised Active Directory Federated Services (AD FS) server. It has been used by [APT29](https://attack.mitre.org/groups/G0016) since at least early April 2021.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Deobfuscate／Decode Files or Information\|T1140]] | Deobfuscate／Decode Files or Information | [FoggyWeb](https://attack.mitre.org/software/S0661) can be decrypted in memory using a Lightweight Encryption Algorithm (LEA)-128 key and decoded using a XOR key.[^1]  |
| [[Archive via Custom Method\|T1560.003]] | Archive via Custom Method | [FoggyWeb](https://attack.mitre.org/software/S0661) can use a dynamic XOR key and a custom XOR methodology to encode data before exfiltration. Also, [FoggyWeb](https://attack.mitre.org/software/S0661) can encode C2 command output within a legitimate WebP file.[^1]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [FoggyWeb](https://attack.mitre.org/software/S0661) can remotely exfiltrate sensitive information from a compromised AD FS server.[^1]  |
| [[Compile After Delivery\|T1027.004]] | Compile After Delivery | [FoggyWeb](https://attack.mitre.org/software/S0661) can compile and execute source code sent to the compromised AD FS server via a specific HTTP POST.[^1]  |
| [[Data from Local System\|T1005]] | Data from Local System | [FoggyWeb](https://attack.mitre.org/software/S0661) can retrieve configuration data from a compromised AD FS server.[^1]  |
| [[Encrypted／Encoded File\|T1027.013]] | Encrypted／Encoded File | [FoggyWeb](https://attack.mitre.org/software/S0661) has been XOR-encoded.[^1]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [FoggyWeb](https://attack.mitre.org/software/S0661) has the ability to communicate with C2 servers over HTTP GET/POST requests.[^1]  |
| [[Private Keys\|T1552.004]] | Private Keys | [FoggyWeb](https://attack.mitre.org/software/S0661) can retrieve token signing certificates and token decryption certificates from a compromised AD FS server.[^1]  |
| [[Masquerading\|T1036]] | Masquerading | [FoggyWeb](https://attack.mitre.org/software/S0661) can masquerade the output of C2 commands as a fake, but legitimately formatted WebP file.[^1]  |
| [[Process Discovery\|T1057]] | Process Discovery | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can enumerate all Common Language Runtimes (CLRs) and running Application Domains in the compromised AD FS server's `Microsoft.IdentityServer.ServiceHost.exe` process.[^1]  |
| [[Use Alternate Authentication Material\|T1550]] | Use Alternate Authentication Material | [FoggyWeb](https://attack.mitre.org/software/S0661) can allow abuse of a compromised AD FS server's SAML token.[^1]  |
| [[Native API\|T1106]] | Native API | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can use API functions to load the [FoggyWeb](https://attack.mitre.org/software/S0661) backdoor into the same Application Domain within which the legitimate AD FS managed code is executed.[^1]  |
| [[Shared Modules\|T1129]] | Shared Modules | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can call the `load()` function to load the [FoggyWeb](https://attack.mitre.org/software/S0661) dll into an Application Domain on a compromised AD FS server.[^1]  |
| [[Network Sniffing\|T1040]] | Network Sniffing | [FoggyWeb](https://attack.mitre.org/software/S0661) can configure custom listeners to passively monitor all incoming HTTP GET and POST requests sent to the AD FS server from the intranet/internet and intercept HTTP requests that match the custom URI patterns defined by the actor.[^1]  |
| [[Archive via Library\|T1560.002]] | Archive via Library | [FoggyWeb](https://attack.mitre.org/software/S0661) can invoke the `Common.Compress` method to compress data with the C# GZipStream compression class.[^1]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [FoggyWeb](https://attack.mitre.org/software/S0661) can receive additional malicious components from an actor controlled C2 server and execute them on a compromised AD FS server.[^1]  |
| [[DLL\|T1574.001]] | DLL | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader has used DLL Search Order Hijacking to load malicious code instead of the legitimate `version.dll` during the `Microsoft.IdentityServer.ServiceHost.exe` execution process.[^1]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [FoggyWeb](https://attack.mitre.org/software/S0661) can be disguised as a Visual Studio file such as `Windows.Data.TimeZones.zh-PH.pri` to evade detection. Also, [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can mimic a genuine `dll` file that carries out the same import functions as the legitimate Windows `version.dll` file.[^1]  |
| [[File and Directory Discovery\|T1083]] | File and Directory Discovery | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader can check for the [FoggyWeb](https://attack.mitre.org/software/S0661) backdoor .pri file on a compromised AD FS server.[^1]  |
| [[Reflective Code Loading\|T1620]] | Reflective Code Loading | [FoggyWeb](https://attack.mitre.org/software/S0661)'s loader has reflectively loaded .NET-based assembly/payloads into memory.[^1]  |
| [[Symmetric Cryptography\|T1573.001]] | Symmetric Cryptography | [FoggyWeb](https://attack.mitre.org/software/S0661) has used a dynamic XOR key and custom XOR methodology for C2 communications.[^1]    |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[APT29\|G0016]] | APT29 |



## References

[^1]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)


