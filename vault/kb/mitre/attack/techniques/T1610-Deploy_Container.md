---
aliases: 
    - T1610
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
mitre-attack: kb/mitre/attack/techniques/T1610-Deploy_Container
tactic: 
     - Execution
platforms:
     - Containers
permissions required:
     - none
---

## Description

Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt to deploy a privileged or vulnerable container into a specific node in order to [[kb/mitre/attack/techniques/T1611-Escape_to_Host\|Escape to Host]] and access other containers running on the node. [^3] <br><br>Containers can be deployed by various means, such as via Docker's `create` and `start` APIs or via a web application such as the Kubernetes dashboard or Kubeflow. [^5] [^4] [^2]  In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets, which can allow containers to be deployed across multiple nodes.[^1]  Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.[^9] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0683-Peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.[^11]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Enforce the principle of least privilege by limiting container dashboard access to only the necessary users. When using Kubernetes, avoid giving users wildcard permissions or adding users to the `system:masters` group, and use `RoleBindings` rather than `ClusterRoleBindings` to limit user privileges to specific namespaces.[^6]  |
| [[kb/mitre/attack/mitigations/M1030-Network_Segmentation\|M1030]] | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API, Kubernetes API Server, and container orchestration web applications.[^12] [^10]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^8]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^7]  |
| [[kb/mitre/attack/mitigations/M1047-Audit\|M1047]] | Audit | Scan images before deployment, and block those that are not in compliance with security policies. In Kubernetes environments, the admission controller can be used to validate images after a container deployment request is authenticated but before the container is deployed.[^13]  |






> [!info]- References
> [^1]: [Kubernetes Workload Management](https://kubernetes.io/docs/concepts/workloads/controllers/)

> [^2]: [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/overview/pipelines-overview/)

> [^3]: [AppSecco Kubernetes Namespace Breakout 2020](https://blog.appsecco.com/kubernetes-namespace-breakout-using-insecure-host-path-volume-part-1-b382f2a6e216)

> [^4]: [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

> [^5]: [Docker Container](https://docs.docker.com/reference/cli/docker/container/create/)

> [^6]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

> [^7]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)

> [^8]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)

> [^9]: [Aqua Build Images on Hosts](https://blog.aquasec.com/malicious-container-image-docker-container-host)

> [^10]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)

> [^11]: [Peirates GitHub](https://github.com/inguardians/peirates)

> [^12]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)

> [^13]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)


