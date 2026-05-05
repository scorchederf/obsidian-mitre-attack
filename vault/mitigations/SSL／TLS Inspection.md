---
aliases: 
    - M1020
    
mitre-attack: https://attack.mitre.org/mitigations/M1020
---

## M1020

SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures:<br><br>Deploy SSL/TLS Inspection Appliances:<br><br>- Implement SSL/TLS inspection solutions to decrypt and inspect encrypted traffic.<br>- Ensure appliances are placed at critical network choke points for maximum coverage.<br><br>Configure Decryption Policies:<br><br>- Define rules to decrypt traffic for specific applications, ports, or domains.<br>- Avoid decrypting sensitive or privacy-related traffic, such as financial or healthcare websites, to comply with regulations.<br><br>Integrate Threat Intelligence:<br><br>- Use threat intelligence feeds to correlate inspected traffic with known indicators of compromise (IOCs).<br><br>Integrate with Security Tools:<br><br>- Combine SSL/TLS inspection with SIEM and NDR tools to analyze decrypted traffic and generate alerts for suspicious activity.<br>- Example Tools: Splunk, Darktrace<br><br>Implement Certificate Management:<br><br>- Use trusted internal or third-party certificates for traffic re-encryption after inspection.<br>- Regularly update certificate authorities (CAs) to ensure secure re-encryption.<br><br>Monitor and Tune:<br><br>- Continuously monitor SSL/TLS inspection logs for anomalies and fine-tune policies to reduce false positives.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Domain Fronting\|T1090.004]] | Domain Fronting | If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting. |
| [[Asymmetric Cryptography\|T1573.002]] | Asymmetric Cryptography | SSL/TLS inspection can be used to see the contents of encrypted sessions to look for network-based indicators of malware communication protocols. |
| [[Encrypted Channel\|T1573]] | Encrypted Channel | SSL/TLS inspection can be used to see the contents of encrypted sessions to look for network-based indicators of malware communication protocols. |
| [[Proxy\|T1090]] | Proxy | If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting. |


## References

