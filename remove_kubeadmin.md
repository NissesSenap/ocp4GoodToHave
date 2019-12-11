# Remove kubeadmin

So it's time to remove your default kubeadmin account.
For ease of use lets use htpasswd

## Create users

Generate a htpasswd file for a few users

```bash
cd
touch htpasswd
htpasswd -Bb htpasswd andrew openshift
htpasswd -Bb htpasswd david openshift
htpasswd -Bb htpasswd karla openshift
```

oc create secret generic htpasswd --from-file=htpasswd -n openshift-config

```bash
 oc apply -f - <<EOF
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: Local Password
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpasswd
EOF
```

### Delete kubeadmin

Yes you should!

oc delete secret kubeadmin -n kube-system
