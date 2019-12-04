# Taintis

All of this can be done in k8s as well.

## Taint infra node in OCP

This file goes through how to only run ceartin workloads
on a specific machine. In this case a infra node.

### Taint node

```bash
oc adm taint node infra-1a-fxb5b infra=reserved:NoSchedule
oc adm taint node infra-1a-fxb5b infra=reserved:NoExecute
```

This generates the following output in the node

```yaml
spec:
  providerID: openstack://269dc19f-ff7d-4d27-bd20-60d15dd5d616
  taints:
  - effect: NoExecute
    key: infra
    value: reserved
  - effect: NoSchedule
    key: infra
    value: reserved
```

### Taint MachineSet

If you are using a MachineSet don't forget to add your taint

```oc patch machineset infra-1a -n openshift-machine-api --type='merge' --patch='{"spec": {"template": {"spec": {"taints": [{"key": "infra","value": "reserved","effect": "NoSchedule"},{"key": "infra","value": "reserved","effect": "NoExecute"}]}}}}'```

### NodeSelector pod

This will match the above node

#### Ingresscontroller

Patching a CRD, note the "nodePlacement".

```oc patch ingresscontroller default -n openshift-ingress-operator --type=merge --patch='{"spec":{"nodePlacement": {"nodeSelector": {"matchLabels": {"node-role.kubernetes.io/infra": ""}},"tolerations": [{"effect":"NoSchedule","key": "infra","value": "reserved"},{"effect":"NoExecute","key": "infra","value": "reserved"}]}}}'```

#### Imageregistry

```oc patch configs.imageregistry.operator.openshift.io/cluster -n openshift-image-registry --type=merge --patch '{"spec":{"nodeSelector":{"node-role.kubernetes.io/infra":""}}}'```

### Openshift-monitoring operator

To taint the openshift-monitoring operator aka prometheus you need to a create a configmap.

See [config.yaml](config.yaml) to see how it looks.
