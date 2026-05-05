---
aliases: 
    - S0683
    
tags: 
    - attack/domain/enterprise_attack
    
    - attack/software/tool
    
    - attack/type/software
    
mitre-attack: kb/mitre/attack/software/S0683-Peirates
---

## Description

[[kb/mitre/attack/software/S0683-Peirates\|Peirates]] is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1046-Network_Service_Discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can initiate a port scan against a given IP address.[^1]  |
| [[kb/mitre/attack/techniques/T1078.004-Cloud_Accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can use stolen service account tokens to perform its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1528-Steal_Application_Access_Token\|T1528]] | Steal Application Access Token | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] gathers Kubernetes service account tokens using a variety of techniques.[^1]  |
| [[kb/mitre/attack/techniques/T1530-Data_from_Cloud_Storage\|T1530]] | Data from Cloud Storage | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.[^1]  |
| [[kb/mitre/attack/techniques/T1550.001-Application_Access_Token\|T1550.001]] | Application Access Token | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can use stolen service account tokens to perform its operations. It also enables adversaries to switch between valid service accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1552.005-Cloud_Instance_Metadata_API\|T1552.005]] | Cloud Instance Metadata API | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can query the query AWS and GCP metadata APIs for secrets.[^1]  |
| [[kb/mitre/attack/techniques/T1552.007-Container_API\|T1552.007]] | Container API | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can query the Kubernetes API for secrets.[^1]  |
| [[kb/mitre/attack/techniques/T1609-Container_Administration_Command\|T1609]] | Container Administration Command | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can use `kubectl` or the Kubernetes API to run commands.[^1]  |
| [[kb/mitre/attack/techniques/T1610-Deploy_Container\|T1610]] | Deploy Container | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.[^1]  |
| [[kb/mitre/attack/techniques/T1611-Escape_to_Host\|T1611]] | Escape to Host | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can gain a reverse shell on a host node by mounting the Kubernetes hostPath.[^1]  |
| [[kb/mitre/attack/techniques/T1613-Container_and_Resource_Discovery\|T1613]] | Container and Resource Discovery | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can enumerate Kubernetes pods in a given namespace.[^1]  |
| [[kb/mitre/attack/techniques/T1619-Cloud_Storage_Object_Discovery\|T1619]] | Cloud Storage Object Discovery | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can list AWS S3 buckets.[^1]  |





> [!info]- References
> [^1]: [Peirates GitHub](https://github.com/inguardians/peirates)


