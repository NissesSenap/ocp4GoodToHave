# Image service account

Service accounts is used for programmatic access.

```bash
oc create serviceaccount registry-admin -n openshift-config

oc adm policy add-cluster-role-to-user registry-admin system:serviceaccount:openshift-config:registry-admin

oc create imagestream ubi8 -n openshift

sudo yum install -y skopeo

REGISTRY_ADMIN_TOKEN=$(oc sa get-token -n openshift-config registry-admin)

UBI8_IMAGE_REPO=$(oc get is -n openshift ubi8 -o jsonpath='{.status.publicDockerImageRepository}')

export SSL_CERT_FILE=$HOME/ca/cacert.pem

skopeo copy docker://registry.access.redhat.com/ubi8:latest docker://$UBI8_IMAGE_REPO:latest --dest-creds -:$REGISTRY_ADMIN_TOKEN
```

If you have used a self signed cert you need to add a funny flag in your scope command...

--dest-tls-verify=false
