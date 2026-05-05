---
aliases: 
    - M1057
    
mitre-attack: https://attack.mitre.org/mitigations/M1057
---

## M1057

Data Loss Prevention (DLP) involves implementing strategies and technologies to identify, categorize, monitor, and control the movement of sensitive data within an organization. This includes protecting data formats indicative of Personally Identifiable Information (PII), intellectual property, or financial data from unauthorized access, transmission, or exfiltration. DLP solutions integrate with network, endpoint, and cloud platforms to enforce security policies and prevent accidental or malicious data leaks. [^2]  This mitigation can be implemented through the following measures:<br><br>Sensitive Data Categorization:<br><br>- Use Case: Identify and classify data based on sensitivity (e.g., PII, financial data, trade secrets).<br>- Implementation: Use DLP solutions to scan and tag files containing sensitive information using predefined patterns, such as Social Security Numbers or credit card details.<br><br>Exfiltration Restrictions:<br><br>- Use Case: Prevent unauthorized transmission of sensitive data.<br>- Implementation: Enforce policies to block unapproved email attachments, unauthorized USB usage, or unencrypted data uploads to cloud storage.<br><br>Data-in-Transit Monitoring:<br><br>- Use Case: Detect and prevent the transmission of sensitive data over unapproved channels.<br>- Implementation: Deploy network-based DLP tools to inspect outbound traffic for sensitive content (e.g., financial records or PII) and block unapproved transmissions.<br><br>Endpoint Data Protection:<br><br>- Use Case: Monitor and control sensitive data usage on endpoints.<br>- Implementation: Use endpoint-based DLP agents to block copy-paste actions of sensitive data and unauthorized printing or file sharing.<br><br>Cloud Data Security:<br><br>- Use Case: Protect data stored in cloud platforms.<br>- Implementation: Integrate DLP with cloud storage platforms like Google Drive, OneDrive, or AWS to monitor and restrict sensitive data sharing or downloads.

### Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[Exfiltration Over Physical Medium\|T1052]] | Exfiltration Over Physical Medium | Data loss prevention can detect and block sensitive data being copied to physical mediums. |
| [[Transfer Data to Cloud Account\|T1537]] | Transfer Data to Cloud Account | Data loss prevention can prevent and block sensitive data from being shared with individuals outside an organization.[^1]  [^3]  |
| [[Data from Local System\|T1005]] | Data from Local System | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |
| [[Exfiltration Over Alternative Protocol\|T1048]] | Exfiltration Over Alternative Protocol | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |
| [[Exfiltration Over Web Service\|T1567]] | Exfiltration Over Web Service | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |
| [[Exfiltration Over Unencrypted Non-C2 Protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |
| [[Exfiltration Over C2 Channel\|T1041]] | Exfiltration Over C2 Channel | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |
| [[Data from Removable Media\|T1025]] | Data from Removable Media | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |
| [[Exfiltration over USB\|T1052.001]] | Exfiltration over USB | Data loss prevention can detect and block sensitive data being copied to USB devices. |
| [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |
| [[Exfiltration Over Webhook\|T1567.004]] | Exfiltration Over Webhook | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |
| [[Traffic Duplication\|T1020.001]] | Traffic Duplication | Implement Data Loss Prevention (DLP) solutions to monitor, detect, and control the flow of sensitive information. DLP tools can be configured to block unauthorized attempts to exfiltrate data, such as preventing emails from being forwarded to external recipients or monitoring for suspicious data transfers. By creating email flow rules and applying policies to detect anomalies, DLP solutions help mitigate the risk of data exfiltration over alternative protocols. |


## References

[^1]: [Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)


[^2]: [PurpleSec Data Loss Prevention](https://purplesec.us/data-loss-prevention/)


[^3]: [Google Workspace Data Loss Prevention](https://support.google.com/a/answer/9646351)


