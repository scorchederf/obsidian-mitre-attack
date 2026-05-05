---
aliases: 
    - M1029
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/type/mitigation
    
mitre-attack: kb/mitre/attack/mitigations/M1029-Remote_Data_Storage
---

## Description

Remote Data Storage focuses on moving critical data, such as security logs and sensitive files, to secure, off-host locations to minimize unauthorized access, tampering, or destruction by adversaries. By leveraging remote storage solutions, organizations enhance the protection of forensic evidence, sensitive information, and monitoring data. This mitigation can be implemented through the following measures:<br><br>Centralized Log Management:<br><br>- Configure endpoints to forward security logs to a centralized log collector or SIEM.<br>- Use tools like Splunk Graylog, or Security Onion to aggregate and store logs.<br>- Example command (Linux): `sudo auditd | tee /var/log/audit/audit.log | nc <remote-log-server> 514`<br><br>Remote File Storage Solutions:<br><br>- Utilize cloud storage solutions like AWS S3, Google Cloud Storage, or Azure Blob Storage for sensitive data.<br>- Ensure proper encryption at rest and access control policies (IAM roles, ACLs).<br><br>Intrusion Detection Log Forwarding:<br><br>- Forward logs from IDS/IPS systems (e.g., Zeek/Suricata) to a remote security information system.<br>- Example for Suricata log forwarding:<br>`outputs:<br>  - type: syslog<br>    protocol: tls<br>    address: <remote-syslog-server>`<br><br>Immutable Backup Configurations:<br><br>- Enable immutable storage settings for backups to prevent adversaries from modifying or deleting data.<br>- Example: AWS S3 Object Lock.<br><br>Data Encryption:<br><br>- Ensure encryption for sensitive data using AES-256 at rest and TLS 1.2+ for data in transit.<br>Tools: OpenSSL, BitLocker, LUKS for Linux.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1070-Indicator_Removal\|T1070]] | Indicator Removal | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.  |
| [[kb/mitre/attack/techniques/T1070.003-Clear_Command_History\|T1070.003]] | Clear Command History | Forward logging of historical data to remote data store and centralized logging solution to preserve historical command line log data. |
| [[kb/mitre/attack/techniques/T1070.007-Clear_Network_Connection_History_and_Configurations\|T1070.007]] | Clear Network Connection History and Configurations | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system. |
| [[kb/mitre/attack/techniques/T1070.008-Clear_Mailbox_Data\|T1070.008]] | Clear Mailbox Data | Automatically forward mail data and events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.  |
| [[kb/mitre/attack/techniques/T1070.009-Clear_Persistence\|T1070.009]] | Clear Persistence | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system.  |
| [[kb/mitre/attack/techniques/T1072-Software_Deployment_Tools\|T1072]] | Software Deployment Tools | If the application deployment system can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the application deployment system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled. |
| [[kb/mitre/attack/techniques/T1119-Automated_Collection\|T1119]] | Automated Collection | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. |
| [[kb/mitre/attack/techniques/T1565-Data_Manipulation\|T1565]] | Data Manipulation | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups. |
| [[kb/mitre/attack/techniques/T1565.001-Stored_Data_Manipulation\|T1565.001]] | Stored Data Manipulation | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data.[^1]  Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups. |
| [[kb/mitre/attack/techniques/T1685.005-Clear_Windows_Event_Logs\|T1685.005]] | Clear Windows Event Logs | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system. |
| [[kb/mitre/attack/techniques/T1685.006-Clear_Linux_or_Mac_System_Logs\|T1685.006]] | Clear Linux or Mac System Logs | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system. |



> [!info]- References
> [^1]: [Ready.gov IT DRP](https://www.ready.gov/business/implementation/IT)


