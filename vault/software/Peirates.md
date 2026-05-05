---
aliases: 
    - S0683
    
mitre-attack: https://attack.mitre.org/software/S0683
---

## S0683

[Peirates](https://attack.mitre.org/software/S0683) is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.[^1] 

### Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[Container and Resource Discovery\|T1613]] | Container and Resource Discovery | [Peirates](https://attack.mitre.org/software/S0683) can enumerate Kubernetes pods in a given namespace.[^1]  |
| [[Container Administration Command\|T1609]] | Container Administration Command | [Peirates](https://attack.mitre.org/software/S0683) can use `kubectl` or the Kubernetes API to run commands.[^1]  |
| [[Escape to Host\|T1611]] | Escape to Host | [Peirates](https://attack.mitre.org/software/S0683) can gain a reverse shell on a host node by mounting the Kubernetes hostPath.[^1]  |
| [[Application Access Token\|T1550.001]] | Application Access Token | [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations. It also enables adversaries to switch between valid service accounts.[^1]  |
| [[Data from Cloud Storage\|T1530]] | Data from Cloud Storage | [Peirates](https://attack.mitre.org/software/S0683) can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.[^1]  |
| [[Network Service Discovery\|T1046]] | Network Service Discovery | [Peirates](https://attack.mitre.org/software/S0683) can initiate a port scan against a given IP address.[^1]  |
| [[Deploy Container\|T1610]] | Deploy Container | [Peirates](https://attack.mitre.org/software/S0683) can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.[^1]  |
| [[Container API\|T1552.007]] | Container API | [Peirates](https://attack.mitre.org/software/S0683) can query the Kubernetes API for secrets.[^1]  |
| [[Cloud Storage Object Discovery\|T1619]] | Cloud Storage Object Discovery | [Peirates](https://attack.mitre.org/software/S0683) can list AWS S3 buckets.[^1]  |
| [[Cloud Instance Metadata API\|T1552.005]] | Cloud Instance Metadata API | [Peirates](https://attack.mitre.org/software/S0683) can query the query AWS and GCP metadata APIs for secrets.[^1]  |
| [[Steal Application Access Token\|T1528]] | Steal Application Access Token | [Peirates](https://attack.mitre.org/software/S0683) gathers Kubernetes service account tokens using a variety of techniques.[^1]  |
| [[Cloud Accounts\|T1078.004]] | Cloud Accounts | [Peirates](https://attack.mitre.org/software/S0683) can use stolen service account tokens to perform its operations.[^1]  |



### Groups That Use This Software
| ID | Name |
| --- | --- |
| [[TeamTNT\|G0139]] | TeamTNT |



## References

[^1]: [Peirates GitHub](https://github.com/inguardians/peirates)


[^2]: [TeamTNT Cloud Enumeration](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments)


