# OpenShift

- [OpenShift](#openshift)
  - [OC CLI](#oc-cli)
    - [Start shell in pod](#start-shell-in-pod)
    - [Login](#login)
    - [export output as template (openshift templates)](#export-output-as-template-openshift-templates)
    - [rsync to pod](#rsync-to-pod)
    - [port-forward](#port-forward)
    - [Get OC API token](#get-oc-api-token)
    - [nodes show-labels](#nodes-show-labels)
    - [Apply/process template](#applyprocess-template)
    - [oc --as](#oc---as)
    - [explain api](#explain-api)
    - [api-resources](#api-resources)
    - [field-selector](#field-selector)
    - [curl spec.host](#curl-spechost)
    - [Get clusterversion](#get-clusterversion)
    - [Get a specific pod log](#get-a-specific-pod-log)
    - [Crete taints](#crete-taints)
    - [Apply taints on pod](#apply-taints-on-pod)
    - [Taint cluster repo](#taint-cluster-repo)
    - [Get node ip](#get-node-ip)
    - [Login oc internal container repo](#login-oc-internal-container-repo)
    - [podman login file](#podman-login-file)
    - [View OCP root credentials](#view-ocp-root-credentials)
    - [simple go-template](#simple-go-template)
  - [Namespace/project](#namespaceproject)
    - [List all the ns](#list-all-the-ns)
    - [Switch ns](#switch-ns)
    - [Project vs Namespace](#project-vs-namespace)
    - [Openshift 3.11 new-project](#openshift-311-new-project)
    - [Admin access within a project](#admin-access-within-a-project)
    - [get specific value secret](#get-specific-value-secret)
  - [Access](#access)
    - [Give admin access](#give-admin-access)
    - [Allow root pod for service account](#allow-root-pod-for-service-account)
      - [Bad way of doing it root access](#bad-way-of-doing-it-root-access)
    - [Change service account for running deploymentconfig](#change-service-account-for-running-deploymentconfig)
    - [User manage all projects](#user-manage-all-projects)
    - [Create user from scratch OCP3](#create-user-from-scratch-ocp3)
    - [Removal for auth users to create projects](#removal-for-auth-users-to-create-projects)
    - [List role bindings](#list-role-bindings)
    - [Role applicability](#role-applicability)
    - [OC default roles](#oc-default-roles)
    - [Security Context Constraints (SCCs)](#security-context-constraints-sccs)
    - [View user access](#view-user-access)
    - [View "policys"/rolebindings](#view-policysrolebindings)
    - [Delete kubeadmin](#delete-kubeadmin)
    - [rotate service account](#rotate-service-account)
    - [Check SA monitor agent can list pods](#check-sa-monitor-agent-can-list-pods)
  - [Applications](#applications)
    - [Create app using cli multiple options](#create-app-using-cli-multiple-options)
      - [Create app using standard repo with a bunch of variabels](#create-app-using-standard-repo-with-a-bunch-of-variabels)
      - [To create an application based on an image from a private registry](#to-create-an-application-based-on-an-image-from-a-private-registry)
      - [To create an application based on source code stored in a Git repository](#to-create-an-application-based-on-source-code-stored-in-a-git-repository)
      - [To create an application based on source code stored in a Git repository and referring to an image stream](#to-create-an-application-based-on-source-code-stored-in-a-git-repository-and-referring-to-an-image-stream)
    - [Delete app](#delete-app)
    - [Scale application](#scale-application)
    - [Autoscaling HorizontalPodAutoscaler (HPA)](#autoscaling-horizontalpodautoscaler-hpa)
    - [Restart pod](#restart-pod)
    - [Set nodeSelector](#set-nodeselector)
    - [Set nodeSelector way 2](#set-nodeselector-way-2)
    - [Cancel failed rollout](#cancel-failed-rollout)
    - [Redeploy application](#redeploy-application)
    - [Get image name from pod](#get-image-name-from-pod)
    - [Get all none quay image in OCP cluster](#get-all-none-quay-image-in-ocp-cluster)
  - [Ansible](#ansible)
    - [Install openshift ansible scripts](#install-openshift-ansible-scripts)
    - [Ansible-playbook prerequisites](#ansible-playbook-prerequisites)
    - [Ansible-playbook deploy_cluster](#ansible-playbook-deploy_cluster)
    - [Verift the installation](#verift-the-installation)
    - [Ansible playbook metrics](#ansible-playbook-metrics)
    - [Ansinble uninstall metrics](#ansinble-uninstall-metrics)
  - [Openshift-install](#openshift-install)
    - [Install logs](#install-logs)
    - [Get pending node requests](#get-pending-node-requests)
    - [Approve all pending nodes](#approve-all-pending-nodes)
  - [Network](#network)
    - [Different routes](#different-routes)
    - [Route/expose without any TLS](#routeexpose-without-any-tls)
    - [Wildcard](#wildcard)
    - [External route example](#external-route-example)
      - [Create a private key using the openssl command](#create-a-private-key-using-the-openssl-command)
      - [Create a certificate signing request (CSR) using the generated private key](#create-a-certificate-signing-request-csr-using-the-generated-private-key)
      - [Generate a certificate using the key and CSR](#generate-a-certificate-using-the-key-and-csr)
      - [create an edge-terminated route](#create-an-edge-terminated-route)
    - [HA route metrics](#ha-route-metrics)
      - [Get env in pod](#get-env-in-pod)
      - [Grab the metric](#grab-the-metric)
  - [Certificates docker](#certificates-docker)
    - [registry requiere cert](#registry-requiere-cert)
    - [docker sarch command](#docker-sarch-command)
    - [docker load](#docker-load)
  - [Diagnostics](#diagnostics)
    - [Finalizers errors](#finalizers-errors)
    - [RedHat debugging tool](#redhat-debugging-tool)
    - [Grab events from cluster or ns](#grab-events-from-cluster-or-ns)
    - [Systemctl](#systemctl)
    - [oc adm diagnostics](#oc-adm-diagnostics)
    - [cloud provider config](#cloud-provider-config)
    - [Insights verification](#insights-verification)
    - [Debbuging machineconfig](#debbuging-machineconfig)
    - [kubernetes api feature gates](#kubernetes-api-feature-gates)
  - [Storage](#storage)
    - [NFS for PV](#nfs-for-pv)
    - [Example NFS PV](#example-nfs-pv)
  - [Admin tasks](#admin-tasks)
    - [Mantience of a node](#mantience-of-a-node)
    - [Label nodes](#label-nodes)
  - [Template](#template)
    - [Add template](#add-template)
    - [template to projects](#template-to-projects)
    - [Template overwrite variables in project](#template-overwrite-variables-in-project)
  - [Quoatas](#quoatas)
    - [Quota using cli](#quota-using-cli)
    - [Get quota](#get-quota)
    - [Pod resource limitation](#pod-resource-limitation)
  - [Limites](#limites)
    - [Typical limits file](#typical-limits-file)
    - [get limitrange](#get-limitrange)
  - [ClusterResources](#clusterresources)
    - [ClusterQuota on env label](#clusterquota-on-env-label)
    - [ClusterQuota on user](#clusterquota-on-user)
  - [Openshift upgrades](#openshift-upgrades)
    - [Hooks](#hooks)
    - [Verification](#verification)
      - [Verify the nodes](#verify-the-nodes)
      - [Verify router/images](#verify-routerimages)
    - [Run diagnostics](#run-diagnostics)
  - [Debug](#debug)
    - [view all roles for a user](#view-all-roles-for-a-user)
    - [View node load](#view-node-load)
    - [View all pods resource usage](#view-all-pods-resource-usage)
    - [Ansible health check](#ansible-health-check)
    - [Debug OCP4 nodes](#debug-ocp4-nodes)
    - [ca cert debubging](#ca-cert-debubging)
      - [Verify ok certificates](#verify-ok-certificates)
      - [curl with cert](#curl-with-cert)
      - [openssl connect](#openssl-connect)
  - [installation debugging](#installation-debugging)
    - [Verify dns srv etcd](#verify-dns-srv-etcd)
    - [Check logs on nodes](#check-logs-on-nodes)
    - [Check running containers on node](#check-running-containers-on-node)
    - [etcd storage verification](#etcd-storage-verification)
  - [Jenkins pipeline](#jenkins-pipeline)
    - [Setup jenkins master](#setup-jenkins-master)
    - [Jenkins service account access](#jenkins-service-account-access)
    - [Jenkins service account pull image](#jenkins-service-account-pull-image)
  - [OSCP4 specific](#oscp4-specific)
    - [Machine operator](#machine-operator)
    - [Machinesets](#machinesets)
    - [Follow machine operator log](#follow-machine-operator-log)
    - [Scale number of nodes in a machineset](#scale-number-of-nodes-in-a-machineset)
    - [network operator](#network-operator)
    - [SDN opeartor](#sdn-opeartor)
    - [Create user httpasswd OCP4](#create-user-httpasswd-ocp4)
  - [Operators](#operators)
  - [Get clusteroperators](#get-clusteroperators)
  - [Openshift 4 course overview](#openshift-4-course-overview)
    - [General notes](#general-notes)
    - [Autolabel nodes](#autolabel-nodes)
    - [Set nodeselector on crd](#set-nodeselector-on-crd)
    - [Cluster version operator](#cluster-version-operator)
    - [Cluster Network Operator CNO](#cluster-network-operator-cno)
  - [openshift-marketplace](#openshift-marketplace)
    - [Avliable operators in marketplace](#avliable-operators-in-marketplace)
    - [Describe operator](#describe-operator)
    - [Create subscription](#create-subscription)
    - [Create nfd](#create-nfd)
    - [Cluster Service Versions](#cluster-service-versions)
    - [Operator provides](#operator-provides)
    - [View opeartor dependencies](#view-opeartor-dependencies)
  - [Machine config](#machine-config)
    - [disable machineconfigpool](#disable-machineconfigpool)
  - [Day2 stuff](#day2-stuff)
    - [Backup](#backup)
      - [Velero](#velero)
  - [Image pruning](#image-pruning)
    - [View iamge pruning status](#view-iamge-pruning-status)
  - [Upgrade paths](#upgrade-paths)
    - [Install upgrade path tools](#install-upgrade-path-tools)
    - [Example upgrade path](#example-upgrade-path)
    - [OCP upgrade errors](#ocp-upgrade-errors)
      - [Debuging upgrade](#debuging-upgrade)
  - [Podman](#podman)
    - [Podman clean error refreshing container](#podman-clean-error-refreshing-container)
  - [cli](#cli)
    - [Extract tls.key from secret](#extract-tlskey-from-secret)

## OC CLI

### Start shell in pod

oc rsh <podname>

### Login

oc login https://master.lab.example.com -u developer -p redhat

### export output as template (openshift templates)

oc export svc,dc docker-registry --as-template=docker-registry

This feature have been depricated due to reasons.
If you want to get rid of similar metadata and status like the export command did you can do the following:

```bash
cat filter.jq
del(.. | select(. == "" or . == null or . == "None")) |
walk(if type == "object" then del(.status,.annotations,.creationTimestamp,.generation,.selfLink,.uid,.resourceVersion) else . end) |
del(.. | select(. == {}))

# Run the above parsing on your yaml output. Notice the yq command that is a wrapper on jq.
kubectl get -o=yaml | yq --yaml-output "$(cat filter.jq)"
```

For more info see [PR](https://github.com/kubernetes/kubernetes/pull/73787)

OCP 4
This is also depricated, don't know how to do it in the future

oc get --export svc -o yaml

### rsync to pod

oc rsync <pod>:<pod_dir> <local_dir> -c <container>

### port-forward

oc port-forward <pod> 3306:3306

### Get OC API token

TOKEN=$(oc whoami -t)

### nodes show-labels

View the labels of nodes

oc get nodes --show-labels

### Apply/process template

oc process -f templates/build.yml | oc apply -f-

### oc --as

If you want to perfrom a "sudo" command or a runas (run-as) command
Perfrom the following:

oc --as=system:serviceaccount:python-example-build:tekton get imagestreams -n python-example-dev

### explain api

Get detailed infomration about k8s API.

oc explain pod.spec.containers

You can also perfrom --recursive to get all info bellow.

oc explain machineset.spec --recursive

### api-resources

This will list all avliable api objects in your cluster.
Use explain to see how to configure them.

oc api-resources

### field-selector

Is it needed? Grep does a good job but probably good when writing scripts.

oc get pods --field-selector status.phase=Running

### curl spec.host

Get the hostname of a route

export ROUTE=$(oc get route bluegreen -o jsonpath='{.spec.host}')

curl $ROUTE/version

### Get clusterversion

oc get clusterversion

### Get a specific pod log

oc logs -n istio-operator $(oc -n istio-operator get pods -l name=istio-operator --output=jsonpath={.items..metadata.name})

### Crete taints

Taint a node manually to do tests, don't forget to update the machineset after.

oc adm taint node infra-1a-t2vsp infra=reserved:NoSchedule

oc adm taint node infra-1a-t2vsp infra=reserved:NoExecute

### Apply taints on pod

```yaml
spec:
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/infra: ""
    tolerations:
    - effect: NoSchedule
      key: infra
      value: reserved
    - effect: NoExecute
      key: infra
      value: reserved
```

For the ingresscontroller

oc patch ingresscontroller default -n openshift-ingress-operator --type=merge --patch='{"spec":{"nodePlacement": {"nodeSelector": {"matchLabels": {"node-role.kubernetes.io/infra": ""}},"tolerations": [{"effect":"NoSchedule","key": "infra","value": "reserved"},{"effect":"NoExecute","key": "infra","value": "reserved"}]}}}'

### Taint cluster repo

oc patch config cluster --type=merge --patch='{"spec":{"nodeSelector": {"node-role.kubernetes.io/infra": ""},"tolerations": [{"effect":"NoSchedule","key": "infra","value": "reserved"},{"effect":"NoExecute","key": "infra","value": "reserved"}]}}'

### Get node ip

If you want to check the ip of the node where you pod is runinng you can perfrom.

oc get pods -o wide

Check the name of the node where you are running and perform:

oc get nodes -o wide

And match that name with the nodes ip.
Or you can write

$ oc get pods $(oc get pod -l app=node-ssh -o jsonpath='{.itea.name}') -o jsonpath='{.status.hostIP}'

### Login oc internal container repo

sudo podman login -u dosentmatter -p $(oc whoami -t) external-route-url-for-internal-docker-repo

The default route for OCP4 docker registry is:
default-route-openshift-image-registry.apps.<clustername>

### podman login file

Podman dosen't store it's login files in $HOME/.docker/config.json
Instea it stores it in $XDG_RUNTIME_DIR/containers/auth.json

### View OCP root credentials

Where can i find my cloud credentials?
Like AWS, Azure, vspehere, openstack etc.

oc get secrets -n kube-system | grep cred

You will see aws-creds if you run aws.

### simple go-template

Sometimes we are in environments that dosen't have jq by default... windows...
Then another good option is go-template.

oc get secret prod-db-secret -o go-template --template='{{.data.username}}'

## Namespace/project

### List all the ns

oc projects

### Switch ns

oc project default

### Project vs Namespace

Projects can have a separate name, display name, and description:

    The mandatory name is a unique identifier for the project and is most visible when using the CLI tools or API. The maximum name length is 63 characters.

    The optional display name is how the project is displayed in the web console (defaults to name).

    The optional description can be a more detailed description of the project and is also visible in the web console.

The following components apply to projects:

    Objects : Pods, services, replication controllers, and more.

    Policies : Rules that determine which actions users can or cannot perform on objects.

    Constraints : Quotas for each kind of object that can be limited.

### Openshift 3.11 new-project

Bellow is not possible in openshift 3.9, the --admin flag is not avaliable.

oc adm new-project resourcemanagement --admin=andrew --node-selector='node-role.kubernetes.io/compute=true'

### Admin access within a project

oc adm policy add-role-to-user admin <user_name> -n <project_name>

### get specific value secret

kubectl get secret sg-token-7rclm --template={{.data.token}} |base64 --decode

## Access

oc whoami

### Give admin access

You have to login on the master node as root to be able to perfrom this command

```bash
ssh root@master
oc whoami
# Give access to admin user
oc adm policy add-cluster-role-to-user cluster-admin admin
```

### Allow root pod for service account

```shell
oc create serviceaccount useroot
oc create role useroot --verb=use --resource=securitycontextconstraints --resource-name=anyuid
oc create rolebinding useroot --role=useroot --serviceaccount=<namespace>:<sa>
```

#### Bad way of doing it root access

Earlier I have been thought that this was a okay way to assign an scc to a user.
There is a bug when upgrading from 4.3.8 -> 4.3.10 or something like that. That looks to see if the scc is completley untouched.
Even if you just assign a user to a scc you will still "modify" it.

Don't do it, I just have this to remember how I did it and to share how not to do it now!

```oc adm policy add-scc-to-user anyuid -z useroot```

### Change service account for running deploymentconfig

oc patch dc/nginx --patch '{"spec":{"template":{"spec":{"serviceAccountName": "useroot"}}}}'

### User manage all projects

This was good enough when getting asked to do the following:
"Allow the developer user access to this project. Allow the developer user to create new applications in this project"

oc policy add-role-to-user edit developer -n todoapp

### Create user from scratch OCP3

A basic way to create users if you are using htpasswd solution.

ssh root@master

oc create user demo-user

htpasswd /etc/origin/openshift-passwd demo-user

oc policy add-role-to-user edit demo-user

### Removal for auth users to create projects

oc adm policy remove-cluster-role-from-group self-provisioner system:authenticated system:authenticated:oauth

### List role bindings

oc describe clusterPolicyBindings :default

oc describe policyBindings :default

### Role applicability

| Command                                             | Description                                                |
| --------------------------------------------------- | ---------------------------------------------------------- |
| oc adm policy who-can verb resource                 | Indicates which users can perform an action on a resource. |
| oc adm policy add-role-to-user role username        | Binds a given role to specified users.                     |
| oc adm policy remove-role-from-user role username   | Removes a given role from specified users.                 |
| oc adm policy remove-user username                  | Removes specified users and all of their roles.            |
| oc adm policy add-role-to-group role groupname      | Binds a given role to specified groups.                    |
| oc adm policy remove-role-from-group role groupname | Removes a given role from specified groups.                |
| oc adm policy remove-group groupname                | Removes specified groups and all of their roles.           |

### OC default roles

| Default Roles    | Description                                                                                                                                                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| edit             | Users in the role can create, change and delete common application resources from the project, such as services and deployment configurations. But cannot act on management resources such as limit ranges and quotas, and cannot manage access permissions to the project. |
| basic-user       | Users in the role have read access to the project.                                                                                                                                                                                                                          |
| self-provisioner | Users in the role can create new projects. This is a cluster role, not a project role.                                                                                                                                                                                      |
| admin            | Users in the role can manage all resources in a project, including granting access to other users to the project.                                                                                                                                                           |

### Security Context Constraints (SCCs)

SCC which control the actions a pod can perform and what resources it can access.

oc get scc

oc describe scc scc_name

### View user access

Having issues with this one...
oc policy who-can * *

### View "policys"/rolebindings

Instead of oc adm policy get rolebinding the syntax is:
oc get clusterrolebinding.rbac
This is due to rbac came after RHOCP (RedHat Openshift Container Platform)...

oc describe clusterrolebinding.rbac self-provisioner

### Delete kubeadmin

NOTE: *Don't* do this before you have created some other admin user.

oc delete secret kubeadmin -n kube-system

It's not possible to create the secret again to create a new password.

### rotate service account

To rotate service account token, delete token secret:

$ oc delete secret SECRET -n NAMESPACE

Deleted token immediately disabled in cluster API

Pods using deleted secret need to be restarted

External services need updated credentials

### Check SA monitor agent can list pods

oc get pods -n monitored-project \
    --as=system:serviceaccount:monitor:monitor-agent \
    --as-group=system:serviceaccounts:monitor

## Applications

### Create app using cli multiple options

#### Create app using standard repo with a bunch of variabels

oc new-app mysql MYSQL_USER=user MYSQL_PASSWORD=pass MYSQL_DATABASE=testdb -l db=mysql

#### To create an application based on an image from a private registry

oc new-app --docker-image=myregistry.com/mycompany/myapp --name=myapp

#### To create an application based on source code stored in a Git repository

oc new-app https://github.com/openshift/ruby-hello-world --name=ruby-hello

#### To create an application based on source code stored in a Git repository and referring to an image stream

oc new-app https://mygitrepo/php-hello -i php:7.0 --name=php-hello

### Delete app

There is no delete-new-app command so use the label of the application that you created

oc delete all -l app=node-hello

### Scale application

oc scale --replicas=5 dc myapp

### Autoscaling HorizontalPodAutoscaler (HPA)

oc autoscale dc/myapp --min 1 --max 10 --cpu-percent=80

### Restart pod

Can be done on dc level as well.

oc scale deployment kube-state-metrics --replicas=0

### Set nodeSelector

Set label on a pod to only run on a specific node.

oc export dc/version -o yaml > version-dc.yml

Add the following under the second spec: above the containers, think on the indentation
nodeSelector:
  region: apps

Random example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd
```

Apply the changes

oc replace -f version-dc,yml

### Set nodeSelector way 2

oc edit dc/version

Perfrom the same changes as above

### Cancel failed rollout

If s2i isn't rolling out as it should and you want to delete it:

oc rollout cancel dc/<name>

### Redeploy application

oc rollout latest dc/<name>

### Get image name from pod

oc get pod cakephp-ex-1-2vdtk -o jsonpath='{.spec.containers[*].image}'

or

oc get pod cakephp-ex-1-2vdtk -o jsonpath='{..image}'

Checkout: https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/

### Get all none quay image in OCP cluster

 kubectl get pods --all-namespaces -o=jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort |grep -v quay

## Ansible

### Install openshift ansible scripts

sudo yum install atomic-openshift-utils

Look in ansible.cfg to see what inventory files it points to.
Prepare the nodes by installing all needed packages, making sure you have some
dedicated docker storage.

Set labels on your nodes, example:
[nodes]
node1.lab.example.com openshift_node_labels="{'region':'infra', 'node-role.kubernetes.io/compute':'true'}"

Under OSEv3:vars you will define openshift release and image tag it should look like this:

openshift_deployment_type=openshift-enterprise
openshift:release=v3.9
openshift_image_tag=v3.9.14

NOTE THE STUPID ASS "v"

### Ansible-playbook prerequisites

From where you have a ansible.cfg file perfrom the following:

ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/prerequisites.yml

### Ansible-playbook deploy_cluster

From where you have a ansible.cfg file perfrom the following:

ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/deploy_cluster.yml

### Verift the installation

After running deploy_cluster.yml

- Login to the web-console and verify that your username and passowrd works
  - NOTE you won't be able to do anything since you are a normal user
- Give admin [root](#give-admin-access) access to cluster
- oc get nodes = ready?
- Verify that the docker-registry and router = ready?
  - oc get pods -n default
- Verify  s2i
  - Create a new project using your normal deploy user
  - oc new-app --name=hello php:5.6~http://services.lab.example.com/php-helloworld

### Ansible playbook metrics

This will deploy as pods to project openshift-infra

ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/openshift-metrics/config.yml -e openshift_metrics_install_metrics=True3

### Ansinble uninstall metrics

ansible-playbook /usr/share/ansible/openshift-ansible/playbooks/openshift-metrics/config.yml -e openshift_metrics_install_metrics=False

## Openshift-install

This is OCP 4 specific.

In short follow the instructions in the documentation. When i do a more advanced documentation I will try to put the time in to document it.

Here is a link for [aws](https://docs.openshift.com/container-platform/4.2/installing/installing_aws/installing-aws-default.html) if you don't want to google.

### Install logs

<installation_folder>/.openshift_install.log

### Get pending node requests

oc get csr

### Approve all pending nodes

oc get csr -ojson | jq -r '.items[] | select(.status == {} ) | .metadata.name' | xargs oc adm certificate approve

## Network

### Different routes

Edge Termination

    With edge termination, TLS termination occurs at the router, before the traffic gets routed to the pods. TLS certificates are served by the router, so they must be configured into the route, otherwise the router’s default certificate is used for TLS termination. Because TLS is terminated at the router, connections from the router to the endpoints over the internal network are not encrypted.

Pass-through Termination

    With pass-through termination, encrypted traffic is sent straight to the destination pod without the router providing TLS termination. No key or certificate is required. The destination pod is responsible for serving certificates for the traffic at the endpoint. This is currently the only method that can support requiring client certificates (also known as two-way authentication).

Re-encryption Termination

    Re-encryption is a variation on edge termination, where the router terminates TLS with a certificate, then re-encrypts its connection to the endpoint, which might have a different certificate. Therefore the full path of the connection is encrypted, even over the internal network. The router uses health checks to determine the authenticity of the host.

### Route/expose without any TLS

oc expose svc/hello --hostname=hello.apps.lab.example.com

### Wildcard

    A wildcard policy allows a user to define a route that covers all hosts within a domain. A route can specify a wildcard policy as part of its configuration using the wildcardPolicy field. The OpenShift router has support for wildcard routes, which are enabled by setting the ROUTER_ALLOW_WILDCARD_ROUTES environment variable to true .

### External route example

#### Create a private key using the openssl command

openssl genrsa -out example.key 2048

#### Create a certificate signing request (CSR) using the generated private key

openssl req -new -key example.key -out example.csr \-subj "/C=US/ST=CA/L=Los Angeles/O=Example/OU=IT/CN=test.example.com"

#### Generate a certificate using the key and CSR

openssl x509 -req -days 366 -in example.csr \-signkey example.key -out example.crt

#### create an edge-terminated route

oc create route edge --service=test \--hostname=test.example.com \--key=example.key --cert=example.crt

### HA route metrics

#### Get env in pod

Openshift 3

oc env pod <podname> --list

Openshift 4

oc set env pod/ocp-probe-1-4bx8x --list

#### Grab the metric

curl <user>:<password>@<router_IP>:<STATS_PORT>

Got some issues with getting a extenral route... In the end I rsh in to the pod and used localhost for test

## Certificates docker

### registry requiere cert

If you docker registry requiere a login you can perform the following:

```bash
  scp -q root@master.lab.example.com:/etc/origin/master/registry.crt .
  sudo cp registry.cr /etc/pki/ca-trust/source/anochors/docker-registry-default.apps.lab.example.com.crt
  sudo update-ca-trust

  sudo systemctl restart docker
```

### docker sarch command

docker-registry-cli registry.lab.example.com search metrics-cassandra ssl

### docker load

If you get a tar file to import to docker (Don't ask me why you ever would do this in 2019) use the command.

docker load -i phpmyadmin-latest.tar

DO **NOT** USE
docker import

You can get a funny error that looks something like: "Error response from daemon: No command specified."
For more information look at:
https://serverfault.com/questions/757210/no-command-specified-from-re-imported-docker-image-container/797619

## Diagnostics

### Finalizers errors

If a k8s objects is stuck deleting the most common reason is due to finalizers.
Andrew Block have written a great explination on how to [debug it](https://www.openshift.com/blog/the-hidden-dangers-of-terminating-namespaces)

Bellow you can find a simple patch that will remove finalizers from a secret.
don't use unless you know what you are doing.

oc patch secret test-secret -n finalizer-example -p '{"metadata":{"finalizers":[]}}' --type=merge

### RedHat debugging tool

Gathers logs from host and docker
sosreport -k docker.all=on -k docker.logs=on

OCP4

oc adm must-gather

### Grab events from cluster or ns

oc get events -n default

oc get event --sort-by='.metadata.creationTimestamp'

### Systemctl

Remember that systemctl is running everything from kubernetes to etcd

rpm -qa |grep atomic

journalctl -u atomic-openshift-master-api.service

### oc adm diagnostics

Good to use before oc upgrades

oc adm diagnostics

### cloud provider config

Due to reasons your cloud provider sa can be changed.
To see what is currently is look at:

oc get controllerconfig machine-config-controller -o yaml

### Insights verification

Your customer might ask does what data does insight gather from us?

INSIGHTS_OPERATOR_POD=$(oc get pods --namespace=openshift-insights -o custom-columns=:metadata.name --no-headers  --field-selector=status.phase=Running)
oc cp openshift-insights/$INSIGHTS_OPERATOR_POD:/var/lib/insights-operator ./insights-data

### Debbuging machineconfig

In my case my worker nodes don't get the latest cri-o image installed on it after an upgrade.
So time for some debugging:

```shell
# Is all pools okay?
oc get machineconfigpool
# In my case it's in a degraded state.

# Look at the worker machineconfigpool, look under status and see what's wrong
oc get machineconfigpool worker -o yaml

# Look at the specific machineconfig that can't donsen't work.
oc get machineconfig rendered-worker-4ec48b44c2322a10cbe7cbd6ee819203 -oyaml

oc project openshift-machine-config-operator

# Find the pod that have the issue (in my case all of the workers so I start with one)
oc get pods -o wide

# logs
oc logs machine-config-daemon-7zb6v -c machine-config-daemon
```

I got error:

E0507 14:02:38.944558 1033717 writer.go:135] Marking Degraded due to: unexpected on-disk state validating against rendered-worker-4ec48b44c2322a10cbe7cbd6ee819203

The following article seems to solve my [issue](https://access.redhat.com/solutions/4264181)

### kubernetes api feature gates

To view the config of the kubernetes api server, you will be able to features like feature gates.

oc get kubeapiserver cluster -o yaml

## Storage

### NFS for PV

The NFS mount needs to be configured the following way:

Owned by the nfsnobody user and group.

Having rwx------ permissions (expressed as 0700 using octal).

Exported using the all_squash option.

Example /etc/exports

```/var/export/vol *(rw,async,all_squash)```

### Example NFS PV

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
 name: mysql-pv
spec:
 capacity:
  storage: 2Gi
 accessModes:
  - ReadWriteMany
 nfs:
  path: /var/export/dbvol
  server: services.lab.example.com
```

## Admin tasks

### Mantience of a node

oc adm manage-node --schedulable=false node2.lab.example.com

oc adm drain node2.lab.example.com --delete-local-data

oc adm manage-node --schedulable=true node2.lab.example.com

### Label nodes

oc label node node2.something.internal perftest=true

## Template

If you want to add a template to your oc environment send in to open-shift namepsace.
Else it won't be visiable from web-gui.
oc get teamplate -n open-shift

### Add template

oc apply -n openshift -f nodejs-mysql-template.yaml

### template to projects

Instead of importing a template you can create it directly in your project.

oc new-app -f examples/sample-app/application-template-stibuild.json

### Template overwrite variables in project

oc new-app ruby-helloworld-sample -p ADMIN_USERNAME=admin -p ADMIN_PASSWORD=mypassword

## Quoatas

Restrict the number of resources a project is allowed to use.

### Quota using cli

oc create quota dev-quota --hard=services=10,cpu=1300m,memory=1.5Gi

### Get quota

oc get resourcequota

### Pod resource limitation

If a quota that restricts usage of compute resources for a project is set, OpenShift refuses to create pods that do not specify resource requests or resource limits for that compute resource.

## Limites

To understand the difference between a limit range and a resource quota resource, consider that a limit range defines valid ranges and default values for a single pod, while a resource quota defines only top values for the sum of all pods in a project.
Limites is like a resource quota but is more granual and can set max and min values.

### Typical limits file

```yaml

apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "dev-limits"
spec:
  limits:
    - type: "Pod"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "200m"
        memory: "6Mi"
    - type: "Container"
      default:
        cpu: "1"
        memory: "512Mi"
```

```yaml
  spec:
    limits:
    - default:
        cpu: 100m
        memory: 100Mi
      defaultRequest:
        cpu: 500m
        memory: 500Mi
      max:
        cpu: 1
        memory: 1Gi
      type: Container
```

### get limitrange

oc get limitranges

## ClusterResources

Is the qutoa for the entire cluster and not project

### ClusterQuota on env label

oc create clusterquota env-qa \--project-label-selector environment=qa \--hard pods=10 \--hard services=5

### ClusterQuota on user

oc create clusterquota user-qa \--project-annotation-selector openshift.io/requester=qa \--hard pods=12 \--hard secrets=20

## Openshift upgrades

If you run openshift 3.7 and want to go to 3.9 you have to land on 3.8 first.

To perform the upgrade add both 3.8 and 3.9 rhel repos.

### Hooks

You can define ansible hooks to run before and after you openshift upgrades.

How to call on a ansible script:
openshift_master_upgrade_pre_hook=/usr/share/custom/pre_master.yml

openshift_master_upgrade_hook=/usr/share/custom/master.yml

openshift_master_upgrade_post_hook=/usr/share/custom/post_master.yml

### Verification

#### Verify the nodes

oc get nodes

#### Verify router/images

oc get -n default dc/docker-registry -o json | grep image

oc get -n default dc/router -o json | grep image

### Run diagnostics

oc adm diagnostics

And verify that you have no errors.

## Debug

### view all roles for a user

We will see both clusterroles and roles for the user flux in this case.

kubectl get rolebinding,clusterrolebinding --all-namespaces -o jsonpath='{range .items[?(@.subjects[0].name=="flux")]}[{.roleRef.kind},{.roleRef.name}]{end}'

### View node load

oc adm top node

### View all pods resource usage

oc adm top pod -A

### Ansible health check

ansible-playbook -i <inventory_file> \
    /usr/share/ansible/openshift-ansible/playbooks/openshift-checks/health.yml

### Debug OCP4 nodes

Verify nodes port_range

In OCP 4 this should be defined in the tuned crd:

oc get tuned -n openshift-cluster-node-tuning-operator

for i in $(oc get nodes --no-headers -o=custom-columns=NAME:.metadata.name); do echo $i; oc debug node/$i -- chroot /host sysctl net.ipv4.ip_local_port_range; done

### ca cert debubging

This is not my strong suite and but during a redhat case I picked up a few things.
The certificates are X509 pem format and they don't have any encryption at all.

#### Verify ok certificates

Using the CA file and see that the tls.crt is okay.

```bash
openssl verify -CAfile ca-bundle.crt tls.crt
openssl x509 -in broken-external.crt -text
```

Check to see how your ca looks like:

openssl x509 -in apps/prod/client-cert.crt -text -noout

#### curl with cert

Of course it won't be able to create a https connection to a kafka endpoint but it's a simple way to send traffic.

curl -vvv https://broker1-kafka1.domain:9093/ --cacert ca-bundle.crt --key tls.key --cert tls.crt

#### openssl connect

```bash
# How I created the secrets
# oc create secret key dosen't support a ca-bundle.crt file but only tls.crt & tls.key
oc create secret generic secret-generic3 --from-file=tls.key --from-file=tls.crt --from-file=ca-bundle.crt --from-file=ca-intermediate.crt

oc rsh <fluentd pod>
cd /var/run/ocp-collector/secrets/<path to secret>

# Use openssl to connect to the endpoint, in this case kafka.
sh-4.4# echo Q | openssl s_client -showcerts -connect broker1-kafka1.domain:9093 -servername broker1-kafka1.domain -key tls.key
-cert tls.crt -CAfile ca-bundle.crt
```

Or a simple openssl without certs

openssl s_client -connect ns1.domain:443
## installation debugging

### Verify dns srv etcd

dig srv _etcd-server-ssl._tcp.<your-domain>

### Check logs on nodes

Debug

journalctl -u release-image.service

journalctl -b -f -u bootkube.service

https://docs.openshift.com/container-platform/4.3/installing/installing-gather-logs.html

### Check running containers on node

sudo crictl ps

### etcd storage verification

Is your storage is Fast Enough for Etcd?
Here you can find a ibm blog about how to test [it](https://www.ibm.com/cloud/blog/using-fio-to-tell-whether-your-storage-is-fast-enough-for-etcd)

Or look at this redhat [doc](https://access.redhat.com/solutions/4885641)
From a master:

sudo podman run --volume /var/lib/etcd:/var/lib/etcd:Z quay.io/openshift-scale/etcd-perf

## Jenkins pipeline

### Setup jenkins master

oc new-app jenkins-persistent -p ENABLE_OAUTH=false -e JENKINS_PASSWORD=openshiftpipelines -n pipeline-${GUID}-dev

### Jenkins service account access

The jenkins service account created in dev need access to your test and prod namespaces to be able to run CD tasks.

oc policy add-role-to-user edit system:serviceaccount:pipeline-${GUID}-dev:jenkins -n pipeline-${GUID}-prod

### Jenkins service account pull image

oc policy add-role-to-group system:image-puller system:serviceaccounts:pipeline-${GUID}-prod -n pipeline-${GUID}-dev
oc policy add-role-to-user system:image-puller

oc policy add-role-to-user edit system:serviceaccount:tekton -n python-example-dev
oc policy add-role-to-group system:image-puller system:serviceaccounts:python-example-build:tekton -n python-example-dev
oc policy add-role-to-user system:image-puller

## OSCP4 specific

### Machine operator

View machines currently in your cluster

oc get machines -n openshift-machine-api

### Machinesets

A machineset is a generic defenition on how a worker node should look.
Like defining if a GPU should be avaliable or in which reagion of a cloud provider it should recide.

oc get machinesets -n openshift-machine-api

### Follow machine operator log

oc logs \
$(oc -n openshift-machine-api get pods -l k8s-app=controller --output=jsonpath={.items..metadata.name}) \
-c machine-controller -n openshift-machine-api -f

### Scale number of nodes in a machineset

oc scale machineset cluster-ba50-z759k-worker-us-east-2c --replicas=1 -n openshift-machine-api

### network operator

The Cluster Network Operator (CNO) deploys and manages the cluster network components on an OpenShift Container Platform cluster, including the Container Network Interface (CNI) Software Defined Networking (SDN) plug-in selected for the cluster during installation.

oc get -n openshift-network-operator deployment/network-operator

oc get clusteroperator/network

### SDN opeartor

The SDN is built up on deamonsets that is run on each server and a sdn-controller that seems to be deployed to each master.

oc project -n openshift-sdn

### Create user httpasswd OCP4

https://suraj.pro/post/user-on-os4/

htpasswd -cb users.htpasswd user1 user1pass

As admin go to -> Administration > Cluster Settings > Global Configuration -> Oauth

Overview, under Identity Providers section, Click on Add and select HTPasswd and upload your file.

oc login -u user1 -p user1pass

## Operators

## Get clusteroperators

oc get clusteroperators

## Openshift 4 course overview

### General notes

master = coreos

worker/infra can be both rhel 7 or coreos. Coreos recomended.
The biggest reason why people want to run rhel 7 is that they want to install a bunch of crap on the server like secuirty scanning and other tools.

1000 node cluster is enough to use 3 masters in most cases, you can increase to 5 masters but normally not needed.
7 is to much due to etcd corum stuff.

Not worth putting quay as the internal OCP registry, use something like nexus instead.

OCP looks for ingress objects, when created the "route" operator grabs it and translates it in to a route object.
This way you can use helm charts that is written for k8s.

AWS EBS can only be in a single avalability zone, in a IPI installation we by default set up nodes in zone A, B and C this will create
issues if a zone goes down since it's read write once. This makes it that you need recreate as your rollout startegy.
In short you can't use PVC in AWS in a good way unless you want to do some black magic for your PVC.

### Autolabel nodes

With the help of an operator you can get labels automatically on nodes.

This is called: node-feature-operator

### Set nodeselector on crd

When defining a nodeselector for a crd in openshift you can't just use nodeselector. Instead you nede to define nodeplacment that calls on nodeselector.
This is good to know when you are configuering stuff to only run on infra node for example.

oc patch ingresscontroller/default -n openshift-ingress-operator --type=merge --patch '{"spec": {"nodePlacement": {"nodeSelector": {"matchLabels": {"node-role.kubernetes.io/infra":""}}}}}'

Verify pods on the infra nodes:

oc get pod -n openshift-ingress -o wide

```yaml
spec:
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/infra: ""
```

Example patch command:

oc patch configs.imageregistry.operator.openshift.io/cluster -n openshift-image-registry --type=merge --patch '{"spec":{"nodeSelector":{"node-role.kubernetes.io/infra":""}}}'

 oc get pods -n openshift-image-registry -o wide

https://docs.openshift.com/container-platform/4.2/machine_management/creating-infrastructure-machinesets.html#moving-resources-to-infrastructure-machinesets

### Cluster version operator

The "mother operator" this is the operator that contains all versions of the rest of the operators. So more or less call this one to create the rest.

### Cluster Network Operator CNO

CIDR is the internal network and the range defined is which ip range the pods will get.
This can't be changed after the installation.

ServiceNetwork defines the range where your services will be avliable.

## openshift-marketplace

You can do a bunch of things through the GUI but why would you want to do that?

### Avliable operators in marketplace

oc get packagemanifests -n openshift-marketplace

### Describe operator

This will give you information of how to install the operator

oc describe packagemanifests nfd -n openshift-marketplace

### Create subscription

Example on how to create a subscription

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nfd
  namespace: openshift-operators
spec:
  channel: "4.2"
  installPlanApproval: Automatic
  name: nfd
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```

### Create nfd

Don't forget to create the crd

```yaml
apiVersion: nfd.openshift.io/v1alpha1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-master-server
  namespace: openshift-operators
spec:
  namespace: openshift-nfd
```

### Cluster Service Versions

oc get csv | grep mesh

### Operator provides

Find out what recources an operator provides/listens to.

oc get csv servicemeshoperator.v1.0.2 -o json | jq '.spec.customresourcedefinitions.owned[].kind'

### View opeartor dependencies

oc get csv servicemeshoperator.v1.0.2 -o json | jq '.spec.customresourcedefinitions.required[].kind'

## Machine config

https://openshift.tips/machine-config/

### disable machineconfigpool

For every machineconfig you update all the nodes will be restarted.
To hinder this perfrom:

oc patch --type=merge --patch='{"spec":{"paused":true}}' machineconfigpool/master

## Day2 stuff

### Backup

Who needs it? No one ever runs storage stuff and none gitops in k8s right? :)

A easy way to setup backups of etcd.

https://github.com/sushilsuresh/ocp4-ansible-roles/tree/master/roles/etcd-backup

Sadly this isn't enough if you wan't to backup the data in your pvc.
In enters velero

#### Velero

Have written [velero.md](velero.md) on how to use it.

## Image pruning

To make sure that you image registry don't become ful you should
delete some old images that is saved in the internal [registry.](https://docs.openshift.com/container-platform/4.4/applications/pruning-objects.html#pruning-images_pruning-objects)

### View iamge pruning status

oc get imagepruner cluster -o yaml

The automatic feature was enabled in OCP 4.4

## Upgrade paths

Due to some bugs in OCP 4.2 you coulden't always go onwards from OCP 4.2 to next minor release.
The patch/upgrade path is described [here](https://access.redhat.com/solutions/4583231)

There is a simple graphical tool that you can use but you need to download a few tools.

### Install upgrade path tools

```shell
sudo dnf install graphviz
wget https://raw.githubusercontent.com/openshift/cincinnati/master/hack/graph.sh
chmod 755 graph.sh
```

### Example upgrade path

curl -sH 'Accept:application/json' 'https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable-4.4&arch=amd64' | ./graph.sh | dot -Tsvg > graph.svg

### OCP upgrade errors

When using the UI or cli upgrading the OCP 4.3 up until 4.3.13 you can get funny errors about scc issues.
But overall check the clusterversion and you will see the errors message.

#### Debuging upgrade

```oc get clusterversion -o yaml```

In there I found the following reason:

message: 'Precondition "ClusterVersionUpgradeable" failed because of "DefaultSecurityContextConstraints_Mutated":
Cluster operator kube-apiserver cannot be upgraded: DefaultSecurityContextConstraintsUpgradeable:
Default SecurityContextConstraints object(s) have mutated [anyuid]'
reason: UpgradePreconditionCheckFailed
status: "True"
type: Failing

So how do I know what have changed in anyuid from the [default?](https://access.redhat.com/solutions/4972291)

## Podman

This dosen't have anything to do with OCP but this is currently my favorit file to write nice to have stuff.

### Podman clean error refreshing container

ERRO[0000] Error refreshing container f7db993e6fa423475035277f88cc09f0154dee13b257914719c18c8e62639002: error acquiring lock 0 for container f7db993e6fa423475035277f88cc09f0154dee13b257914719c18c8e62639002: file exists

rm -rf ~/.local/share/containers/storage/overlay-containers/*/userdata/*

## cli

Good to have commands

### Extract tls.key from secret

Coulden't find the way to get jq to ignore the . in tls.key

k get secret secret-name -o jsonpath={.data."tls\.crt"} |base64 -d > tls.crt

k get secret secret-name -o jsonpath={.data."tls\.key"} |base64 -d > tls.key
