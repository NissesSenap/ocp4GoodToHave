# Velero

PVC backup for k8s clusters.
In this file i assume that you have setup your s3 storage using OCS and using noobaa to create your bucket.

## Noobaa create bucket

noobaa obc create velero --exact=true -n openshift-storage

## CLI

Hmm i haven't downloaded a new cli the last 10 hours...

Download the cli
https://github.com/vmware-tanzu/velero/releases/download/v1.2.0/velero-v1.2.0-linux-amd64.tar.gz

For zsh users add the following to your .zshrc file.

source <(velero completion zsh)

## Velero plugin

https://velero.io/docs/v1.2.0/overview-plugins/

I don't understand why it dosen't feel this when defining aws as the provider or at least use it as a default.
You HAVE to perform the bellow command.

### AWS s3 bucket storage plugin

velero plugin add velero/velero-plugin-for-aws:v1.0.0

## Create install config

You have to define a region even if you don't use one in noobaa.

velero install --bucket velero --provider aws --secret-file ./credentials-velero --plugins=velero/velero-plugin-for-aws:v1.0.0 --backup-location-config region="eu1",s3Url="https://s3-openshift-storage.apps.ocp67.ajco.se",insecureSkipTLSVerify="true",s3ForcePathStyle="true" --use-volume-snapshots=false --velero-pod-mem-limit=1024Mi --velero-pod-cpu-limit=1000 --dry-run -o yaml > velero.yaml

## Restic

Add "--use-restic" to your velero install command.
This will make it possible to run file by file backup of a pvc and store it in a s3 bucket.

The problem is that currently can't disable the certificate verification on the restic [pod](https://github.com/vmware-tanzu/velero/blob/master/design/)custom-ca-support.md

Work on this is onging from veleros point of view.

A potential workaround is to add your own ca certificate to the velero pod.
Push the file to your own container repo and update the daemonset with the new image.
And it should be able to talk to your storage bucket.

```Dockerfile
FROM velero/velero:v1.3.0
COPY my-own.crt /usr/share/ca-certificates/ 
COPY ca-certificates.conf /etc/ca-certificates.conf
USER root
RUN /usr/sbin/update-ca-certificates
USER nobody:nogroup
# ENTRYPOINT /bin/bash

```

Example ca-certificates.conf

```shell
$ cat ca-certificates.conf

my-own.crt

```

The container dosen't contain curl or wget (can ofc install it)
or you can use:

```openssl s_client -connect s3-openshift-storage.apps.test01.mydomain.com:443```
Look for "Verify return code: 0 (ok)"

This will indicate that your ca cert is added correctly and the restic backup should work.

## Snapshot

**Vsphere** currently don't support snapshoting in it's csi. Until that is fixed the snapshoting won't work.
But if you are using one of the big cloud providers it should look something like this.

### How to maybe do it

I put a lots of time in to this reserach so i don't want to remove it.
But this is probably how you will do it in the future for vshpere and if you have a csi that supports snapshot together with the correct
velero plugin something like this should work.

I first need to add velero to be able to create root containers.

oc adm policy add-scc-to-user anyuid -z velero

velero snapshot-location create default --provider velero.io/vsphere

edit deployment/velero -n velero

spec.template.spec.args:

      - args:
        - server
        - --default-volume-snapshot-locations
        - velero.io/vsphere:example-default

Update image on the velero deployment:
vsphereveleroplugin/velero-plugin-for-vsphere

Also add:
      hostNetwork: true
Under 
spec:
  template:
    spec:
      containers:
And not what it says in the documentation directly under spec.teamplte.spec.

#### Crete secret

You also need to create a secret for vshpere, this isn't documentated...
    username: username1
    password: supersecretpassword

secret-name: cloud-credentials
It currently says the aws credentials...

The input should be in gcp and aws:
data": {
        "cloud": "SECRET KEY"
    },

And if i read the go code for vsphere it should be the same.

#### Verfiy snapshot location creation

velero snapshot-location get

## CRD

oc get backupstoragelocations default

## Example nginx

Nginx runs as root but it's a simple example, live with it. It's a poc :).

oc apply -f nginx-example.yaml

oc project nginx-example
oc create serviceaccount useroot
oc adm policy add-scc-to-user anyuid -z useroot
oc patch  deployment nginx-deploy --patch '{"spec":{"template":{"spec":{"serviceAccountName": "useroot"}}}}'

Create some traffi and verify the output of the logs:
kubectl exec -it nginx-deploy-6fcdc96c8-q46c2 --namespace nginx-example -- cat /var/log/nginx/access.log

## Create backup

velero backup create nginx-backup --selector app=nginx --include-namespaces nginx-example

velero backup create nginx-backup --snapshot-volumes=true --volume-snapshot-locations=aws-default --selector app=nginx --include-namespaces nginx-example

View the created backup

oc get backup nginx-backup -n velero

### View backup through velero

velero backup describe nginx-backup --insecure-skip-tls-verify --details

## Restore

Time to testout the restore procedure

### Deleteoc adm policy add-scc-to-user privileged -z velero -n velero

velero restore create --from-backup nginx-backup

#### info about restore

velero restore describe nginx-backup-20200228104915 --insecure-skip-tls-verify

velero restore logs nginx-backup-20200228104915 --insecure-skip-tls-verify

The backup won't work perfectly due to missing serviceaccount.
Patch your resource again and it will jump up once again.
