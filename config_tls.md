# Configure TLS for your OCP 4 cluster

Pre-req is that you got your certificates, for example from: https://letsencrypt.org/

In some commands you might see stuff like $GUID or $API_HOSTNAME, this should ofc point to your own information.

## Add TLS to secret

This will trigger an update within the operators

oc create secret tls cluster-apiserver-tls --cert=<path-to-cert>.cert.pem --key=private/<path-to-private-cert>.key.pem -n openshift-config

### Make the apiserver use the secret

```oc patch apiservers.config.openshift.io cluster --type=merge -p '{"spec":{"servingCerts": {"namedCertificates": [{"names": ["'$API_HOSTNAME'"], "servingCertificate": {"name": "cluster-apiserver-tls"}}]}}}'```

### Watch the changes

watch oc get co

### Update kubeconfig

Update kubeconfig to use the new certificate.

```oc config set-cluster $GUID --certificate-authority=<path-to-ca>/cacert.pem```

Verify that you can login to the server

## Add TLS to ingress default cert

### Create secret

```oc create secret tls default-ingress-tls --cert=$HOME/ca/certs/$INGRESS_DOMAIN.cert.pem --key=$HOME/ca/private/$INGRESS_DOMAIN.key.pem -n openshift-ingress```

### Path ingresscontroller

```oc patch ingresscontroller.operator default --type=merge -p '{"spec":{"defaultCertificate": {"name": "default-ingress-tls"}}}' -n openshift-ingress-operator```

### Verifiy ingresscontroller

```curl $(oc whoami --show-console) --cacert $HOME/ca/cacert.pem -v | head -1```

```openssl s_client -showcerts -servername test.$INGRESS_DOMAIN -connect test.$INGRESS_DOMAIN:443```

oc patch machineconfig 99-worker-ssh --type=json --patch="[{\"op\":\"add\", \"path\":\"/spec/config/passwd/users/1/sshAuthorizedKeys/-\", \"value\":\"$(cat $HOME/.ssh/node.id_rsa.pub)\"}]"
