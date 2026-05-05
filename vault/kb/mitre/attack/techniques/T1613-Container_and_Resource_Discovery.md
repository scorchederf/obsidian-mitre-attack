---
aliases: 
    - T1613
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/containers
mitre-attack: kb/mitre/attack/techniques/T1613-Container_and_Resource_Discovery
tactic: 
     - Discovery
platforms:
     - Containers
permissions required:
     - none
---

## Description

Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.<br><br>These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.[^6] [^1]  In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution. 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0683-Peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can enumerate Kubernetes pods in a given namespace.[^5]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Enforce the principle of least privilege by limiting dashboard visibility to only the required users. When using Kubernetes, avoid giving users wildcard permissions or adding users to the `system:masters` group, and use `RoleBindings` rather than `ClusterRoleBindings` to limit user privileges to specific namespaces.[^2]  |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^8] [^7]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^4]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |






> [!info]- References
> [^1]: [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

> [^2]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

> [^3]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)

> [^4]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)

> [^5]: [Peirates GitHub](https://github.com/inguardians/peirates)

> [^6]: [Docker API](https://docs.docker.com/engine/api/v1.41/)

> [^7]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)

> [^8]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


