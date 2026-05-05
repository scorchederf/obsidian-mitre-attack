---
aliases: 
    - S9008
    
mitre-attack: https://attack.mitre.org/software/S9008
---

## S9008

[Shai-Hulud](https://attack.mitre.org/software/S9008) is a supply chain worm, first reported in September 2025, that spreads through code repositories, including GitHub and NPM packages. It exploits CI/CD pipeline dependencies to propagate to victims and poisons the supply chain by publishing malicious packages. Once inside a victim environment, [Shai-Hulud](https://attack.mitre.org/software/S9008) steals credentials and access tokens from compromised repository accounts and exfiltrates them to attacker-controlled servers via encoded GitHub Actions workflows.[^5] [^2] [^3] [^6] [^4] [^1] [^7] <br>

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Obfuscated Files or Information\|T1027]] | Obfuscated Files or Information | [Shai-Hulud](https://attack.mitre.org/software/S9008) has utilized double-base64 encoding to store stolen secrets within the Github Action Logs within the victim account.[^4] [^1] [^7] [^6]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also leveraged three layers of base64 encoding of exfiltrated data for anti-forensic purposes.[^3]  |
| [[Sudo and Sudo Caching\|T1548.003]] | Sudo and Sudo Caching | [Shai-Hulud](https://attack.mitre.org/software/S9008) has attempted to gain root access by leveraging `sudo` and `/etc/sudoers.d`.[^3]  |
| [[Systemd Service\|T1543.002]] | Systemd Service | [Shai-Hulud](https://attack.mitre.org/software/S9008) has stopped `systemd-resolved` in order to manipulate DNS and firewalls.[^3]  |
| [[Delay Execution\|T1678]] | Delay Execution | [Shai-Hulud](https://attack.mitre.org/software/S9008) has delayed execution of its larger payloads by forking itself into background process.[^5]  |
| [[Poisoned Pipeline Execution\|T1677]] | Poisoned Pipeline Execution | [Shai-Hulud](https://attack.mitre.org/software/S9008) has also leveraged GitHub actions from stolen accounts in order to create a malicious Github workflow within `.github/workflows/discussion.yaml`.[^4] [^1] [^5] [^3]  |
| [[Data Destruction\|T1485]] | Data Destruction | [Shai-Hulud](https://attack.mitre.org/software/S9008) has destroyed the victim’s home directory by overwriting and deleting every writable file within the user's home folder.[^5] [^3]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also utilized the `shred` command on Linux devices.[^2]  |
| [[Credentials In Files\|T1552.001]] | Credentials In Files | [Shai-Hulud](https://attack.mitre.org/software/S9008) has gathered sensitive data stored in the Node.JS file `process.env` to include credentials and API keys.[^4] [^3] [^6]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has harvested credentials stored in config files and credential files in victim environments to include `~/.aws/credentials`, `application_default_credentials.json`, and `azureProfile.json`.[^1] [^5] [^3] [^6]   [Shai-Hulud](https://attack.mitre.org/software/S9008) has also targeted credentials and tokens stored in NPM files `.npmrc` and GitHub config files.[^1] [^5] [^3] [^6]   |
| [[Disable or Modify Tools\|T1685]] | Disable or Modify Tools | [Shai-Hulud](https://attack.mitre.org/software/S9008) has replaced DNS configuration from `/tmp/resolved.conf` in order to gain control of network-level control within CI environments and has flushed iptables rules using `sudo iptables -F OUTPUT` and `sudo iptables -F DOCKER-USER`.[^3]  |
| [[Compromise Software Dependencies and Development Tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | [Shai-Hulud](https://attack.mitre.org/software/S9008) has published itself on compromised code repository maintainers within infected packages in attempts to propagate to other victims.[^4] [^1] [^7] [^2] [^3]   [Shai-Hulud](https://attack.mitre.org/software/S9008) has also modified versions of code packages.[^4] [^1] [^7] [^3]  |
| [[Ingress Tool Transfer\|T1105]] | Ingress Tool Transfer | [Shai-Hulud](https://attack.mitre.org/software/S9008) has downloaded packages from code repositories.[^4] [^7] [^3] [^6]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also downloaded and executed the secrets-discovery tool [TruffleHog](https://attack.mitre.org/software/S9009) to gather sensitive data.[^1] [^7] [^2] [^3] [^6]  |
| [[Unix Shell\|T1059.004]] | Unix Shell | [Shai-Hulud](https://attack.mitre.org/software/S9008) has utilized Linux shell commands to modify configuration files.[^3]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [Shai-Hulud](https://attack.mitre.org/software/S9008) has leveraged compromised accounts to log into cloud services to access cloud hosted repositories.[^4] [^1] [^5] [^7] [^2]  |
| [[Cloud Secrets Management Stores\|T1555.006]] | Cloud Secrets Management Stores | [Shai-Hulud](https://attack.mitre.org/software/S9008) has gathered secrets from AWS Secrets and GCP Secret Manager.[^4] [^1] [^3]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also gathered data from Azure Key Vault.[^1] [^3]  |
| [[Ignore Process Interrupts\|T1564.011]] | Ignore Process Interrupts | [Shai-Hulud](https://attack.mitre.org/software/S9008) has suppressed NPM warnings by silently exiting through the use of the NPM success code that has a setting that all errors exit with `code 0`.[^3]  |
| [[Automated Collection\|T1119]] | Automated Collection | [Shai-Hulud](https://attack.mitre.org/software/S9008) has the ability to automatically collect host data, secrets, system information, and endpoints.[^4] [^1] [^2]  |
| [[Web Protocols\|T1071.001]] | Web Protocols | [Shai-Hulud](https://attack.mitre.org/software/S9008) has utilized curl to install Bun over HTTPS.[^2]  |
| [[Code Repositories\|T1593.003]] | Code Repositories | [Shai-Hulud](https://attack.mitre.org/software/S9008) has the ability to search open sites and code repositories for compromised credentials.[^4] [^2]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has discovered packages associated with compromised accounts.[^1]   [Shai-Hulud](https://attack.mitre.org/software/S9008) has also searched code repositories for other compromised repositories that include predefined parameters or markers to include “Second Coming” combined with an 18-character alphanumeric string.[^1]  |
| [[Exfiltration to Code Repository\|T1567.001]] | Exfiltration to Code Repository | [Shai-Hulud](https://attack.mitre.org/software/S9008) has created a repository named `Shai-Hulud` under the compromised account that commits a JSON dump that contains system information, environment variables and collected secrets.[^4] [^1] [^7]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also posted stolen credentials to public GitHub repositories.[^5] [^2] [^3] [^6]  |
| [[Break Process Trees\|T1036.009]] | Break Process Trees | [Shai-Hulud](https://attack.mitre.org/software/S9008) has augmented its installation process by having its original install process exit cleanly to provide the user with the illusion that the service is installed normally.[^5] [^3]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [Shai-Hulud](https://attack.mitre.org/software/S9008) has stolen access tokens and API tokens from with CI/CD pipeline solutions and repositories.[^1] [^5] [^7] [^3]  |
| [[Account Manipulation\|T1098]] | Account Manipulation | [Shai-Hulud](https://attack.mitre.org/software/S9008) has modified GitHub account settings for private repositories and changed them to public.[^4] [^1] [^7] [^2]  |
| [[Subvert Trust Controls\|T1553]] | Subvert Trust Controls | [Shai-Hulud](https://attack.mitre.org/software/S9008) has suppressed victim NPM warnings using `process[“exit’](0x0);` which results in having all errors exit with code 0.[^3]  |
| [[Match Legitimate Resource Name or Location\|T1036.005]] | Match Legitimate Resource Name or Location | [Shai-Hulud](https://attack.mitre.org/software/S9008) has masqueraded as a legitimate Bun installer.[^5] [^3]  |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | [Shai-Hulud](https://attack.mitre.org/software/S9008) has used POST to exfiltrate secrets from the victim environment to an attacker-controlled URL.[^4] [^5] [^7]  |
| [[Installer Packages\|T1546.016]] | Installer Packages | [Shai-Hulud](https://attack.mitre.org/software/S9008) has inserted a new lifecycle hook to include `postinstall`.[^4] [^5] [^7] [^3]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also leveraged the NPM lifecycle hook `preinstall`.[^1] [^5] [^2] [^3]  |
| [[Upload Malware\|T1608.001]] | Upload Malware | [Shai-Hulud](https://attack.mitre.org/software/S9008) has published malicious gzip-compressed tarball (.tgz) following modification of packages within compromised accounts.[^4] [^6]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also modified packages within compromised accounts.[^1] [^7]  |
| [[Exfiltration Over Webhook\|T1567.004]] | Exfiltration Over Webhook | [Shai-Hulud](https://attack.mitre.org/software/S9008) has exfiltrated repository secrets to `webhook[.]site`.[^7]  |
| [[Code Repositories\|T1213.003]] | Code Repositories | [Shai-Hulud](https://attack.mitre.org/software/S9008) has downloaded existing packages from code repositories and extracted data stored within them.[^4]  |
| [[PowerShell\|T1059.001]] | PowerShell | [Shai-Hulud](https://attack.mitre.org/software/S9008) has utilized PowerShell `Invoke-WebRequest` to download and install the malicious payload.[^2]  |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | [Shai-Hulud](https://attack.mitre.org/software/S9008) has queried the AWS and GCP metadata endpoints for instances and service credentials.[^4]  |
| [[System Information Discovery\|T1082]] | System Information Discovery | [Shai-Hulud](https://attack.mitre.org/software/S9008) has gathered victim system information.[^4] [^3]  |
| [[Application Access Token\|T1550.001]] | Application Access Token | [Shai-Hulud](https://attack.mitre.org/software/S9008) has leveraged captured valid NPM tokens to enumerate and update packages on compromised accounts.[^4] [^3] [^6]  [Shai-Hulud](https://attack.mitre.org/software/S9008) has also utilized stolen GitHub access tokens to access compromised accounts.[^3] [^6]  |
| [[JavaScript\|T1059.007]] | JavaScript | [Shai-Hulud](https://attack.mitre.org/software/S9008) has used JavaScript to create JSON file output and run scripts using node.js.[^4] [^1] [^5] [^7] [^2] [^3] [^6]  |




## References

[^1]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)


[^2]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)


[^3]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)


[^4]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)


[^5]: [Palo Alto Unit 42 Shai-Hulud November 2025](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)


[^6]: [Socket Shai-Hulud Trufflehog September 2025](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)


[^7]: [Wiz Shai-Hulud September 2025](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)


