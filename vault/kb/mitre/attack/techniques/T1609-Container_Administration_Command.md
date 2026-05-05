---
aliases: 
    - T1609
tags: 
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
mitre-attack: kb/mitre/attack/techniques/T1609-Container_Administration_Command
tactic: 
     - Execution
platforms:
     - Containers
permissions required:
     - none
---

## Description

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.[^3] [^5] [^13] <br><br>In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as `docker exec` to execute a command within a running container.[^7] [^4]  In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as `kubectl exec`.[^14] 


## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0683-Peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-Peirates\|Peirates]] can use `kubectl` or the Kubernetes API to run commands.[^10]  |




## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-User_Account_Management\|M1018]] | User Account Management | Enforce authentication and role-based access control on the container service to restrict users to the least privileges required.[^12]  When using Kubernetes, avoid giving users wildcard permissions or adding users to the `system:masters` group, and use `RoleBindings` rather than `ClusterRoleBindings` to limit user privileges to specific namespaces.[^6]  |
| [[kb/mitre/attack/mitigations/M1026-Privileged_Account_Management\|M1026]] | Privileged Account Management | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers and using the `NodeRestriction` admission controller to deny the kublet access to nodes and pods outside of the node it belongs to.[^12]  [^2]  |
| [[kb/mitre/attack/mitigations/M1035-Limit_Access_to_Resource_Over_Network\|M1035]] | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^15] [^11]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^9]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^8]  |
| [[kb/mitre/attack/mitigations/M1038-Execution_Prevention\|M1038]] | Execution Prevention | Use read-only containers, read-only file systems, and minimal images when possible to prevent the execution of commands.[^12]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-Disable_or_Remove_Feature_or_Program\|M1042]] | Disable or Remove Feature or Program | Remove unnecessary tools and software from containers. |






> [!info]- References
> [^1]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

> [^2]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)

> [^3]: [Docker Daemon CLI](https://docs.docker.com/engine/reference/commandline/dockerd/)

> [^4]: [Docker Exec](https://docs.docker.com/engine/reference/commandline/exec/)

> [^5]: [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

> [^6]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)

> [^7]: [Docker Entrypoint](https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime)

> [^8]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)

> [^9]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)

> [^10]: [Peirates GitHub](https://github.com/inguardians/peirates)

> [^11]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)

> [^12]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

> [^13]: [Kubernetes Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)

> [^14]: [Kubectl Exec Get Shell](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/)

> [^15]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)


