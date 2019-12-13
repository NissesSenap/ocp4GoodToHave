# Project template

oc adm create-bootstrap-project-template -o yaml > template.yaml

Edit the template to your needs, for example template.yaml

oc create -f template.yaml -n openshift-config

Edit:

oc edit project.config.openshift.io/cluster

Add:
```yaml
spec:
  projectRequestTemplate:
    name: <template_name>
```

TODO: Add patch version
