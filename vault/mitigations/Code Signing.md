---
aliases: 
    - M1045
    
mitre-attack: https://attack.mitre.org/mitigations/M1045
---

## M1045

Code Signing is a security process that ensures the authenticity and integrity of software by digitally signing executables, scripts, and other code artifacts. It prevents untrusted or malicious code from executing by verifying the digital signatures against trusted sources. Code signing protects against tampering, impersonation, and distribution of unauthorized or malicious software, forming a critical defense against supply chain and software exploitation attacks. This mitigation can be implemented through the following measures:<br><br>Enforce Signed Code Execution:<br><br>- Implementation: Configure operating systems (e.g., Windows with AppLocker or Linux with Secure Boot) to allow only signed code to execute.<br>- Use Case: Prevent the execution of malicious PowerShell scripts by requiring all scripts to be signed with a trusted certificate.<br><br>Vendor-Signed Driver Enforcement:<br><br>- Implementation: Enable kernel-mode code signing to ensure that only drivers signed by trusted vendors can be loaded.<br>- Use Case: A malicious driver attempting to modify system memory fails to load because it lacks a valid signature.<br><br>Certificate Revocation Management:<br><br>- Implementation: Use Online Certificate Status Protocol (OCSP) or Certificate Revocation Lists (CRLs) to block certificates associated with compromised or deprecated code.<br>- Use Case: A compromised certificate used to sign a malicious update is revoked, preventing further execution of the software.<br><br>Third-Party Software Verification:<br><br>- Implementation: Require software from external vendors to be signed with valid certificates before deployment.<br>- Use Case: An organization only deploys signed and verified third-party software to prevent supply chain attacks.<br><br>Script Integrity in CI/CD Pipelines:<br><br>- Implementation: Integrate code signing into CI/CD pipelines to sign and verify code artifacts before production release.<br>- Use Case: A software company ensures that all production builds are signed, preventing tampered builds from reaching customers.<br><br>**Key Components of Code Signing**<br><br>- Digital Signature Verification: Verifies the authenticity of code by ensuring it was signed by a trusted entity.<br>- Certificate Management: Uses Public Key Infrastructure (PKI) to manage signing certificates and revocation lists.<br>- Enforced Policy for Unsigned Code: Prevents the execution of unsigned or untrusted binaries and scripts.<br>- Hash Integrity Check: Confirms that code has not been altered since signing by comparing cryptographic hashes.<br>

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Server Software Component\|T1505]] | Server Software Component | Ensure all application component binaries are signed by the correct application developers. |
| [[Malicious Image\|T1204.003]] | Malicious Image | Utilize a trust model such as Docker Content Trust with digital signatures to ensure runtime verification of the integrity and publisher of specific image tags.[^2] [^6]  |
| [[Implant Internal Image\|T1525]] | Implant Internal Image | Several cloud service providers support content trust models that require container images be signed by trusted sources.[^6] [^2]  |
| [[AppleScript\|T1059.002]] | AppleScript | Require that all AppleScript be signed by a trusted developer ID before being executed - this will prevent random AppleScript code from executing.[^1]  This subjects AppleScript code to the same scrutiny as other .app files passing through Gatekeeper. |
| [[Command and Scripting Interpreter\|T1059]] | Command and Scripting Interpreter | Where possible, only permit execution of signed scripts. |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | Require signed binaries and images. |
| [[Invalid Code Signature\|T1036.001]] | Invalid Code Signature | Require signed binaries. |
| [[PowerShell Profile\|T1546.013]] | PowerShell Profile | Enforce execution of only signed PowerShell scripts. Sign profiles to avoid them from being modified. |
| [[Masquerading\|T1036]] | Masquerading | Require signed binaries. |
| [[Compromise Host Software Binary\|T1554]] | Compromise Host Software Binary | Ensure all application component binaries are signed by the correct application developers. |
| [[Patch System Image\|T1601.001]] | Patch System Image | Many vendors provide digitally signed operating system images to validate the integrity of the software used on their platform.  Make use of this feature where possible in order to prevent and/or detect attempts by adversaries to compromise the system image. [^5]  |
| [[Downgrade System Image\|T1601.002]] | Downgrade System Image | Many vendors provide digitally signed operating system images to validate the integrity of the software used on their platform.  Make use of this feature where possible in order to prevent and/or detect attempts by adversaries to compromise the system image. [^5]  |
| [[Windows Service\|T1543.003]] | Windows Service | Enforce registration and execution of only legitimately signed service drivers where possible. |
| [[PowerShell\|T1059.001]] | PowerShell | Set PowerShell execution policy to execute only signed scripts. |
| [[SQL Stored Procedures\|T1505.001]] | SQL Stored Procedures | Ensure all application component binaries are signed by the correct application developers.  |
| [[Create or Modify System Process\|T1543]] | Create or Modify System Process | Enforce registration and execution of only legitimately signed service drivers where possible. |
| [[Modify System Image\|T1601]] | Modify System Image | Many vendors provide digitally signed operating system images to validate the integrity of the software used on their platform.  Make use of this feature where possible in order to prevent and/or detect attempts by adversaries to compromise the system image. [^5]  |
| [[IIS Components\|T1505.004]] | IIS Components | Ensure IIS DLLs and binaries are signed by the correct application developers. |
| [[LC_LOAD_DYLIB Addition\|T1546.006]] | LC_LOAD_DYLIB Addition | Enforce that all binaries be signed by the correct Apple Developer IDs. |
| [[vSphere Installation Bundles\|T1505.006]] | vSphere Installation Bundles | Enabling the `execInstalledOnly` feature prevents unsigned binaries from being run on ESXi hosts.[^4]  |
| [[Transport Agent\|T1505.002]] | Transport Agent | Ensure all application component binaries are signed by the correct application developers.  |
| [[ClickOnce\|T1127.002]] | ClickOnce | Enforce binary and application integrity with digital signature verification to prevent untrusted code from executing.[^3]  |


## References

[^1]: [applescript signing](https://www.engadget.com/2013/10/23/applescript-and-automator-gain-new-features-in-os-x-mavericks/)


[^2]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)


[^3]: [Microsoft Learn ClickOnce and Authenticode](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022)


[^4]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)


[^5]: [Cisco IOS Software Integrity Assurance - Deploy Signed IOS](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)


[^6]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)


