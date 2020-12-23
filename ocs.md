# OCS

## Noobaa

### Download from git or through rpm

``` shell
subscription-manager repos --enable=rh-ocs-4-for-rhel-8-x86_64-rpms
yum install mcg
```

wget https://github.com/noobaa/noobaa-operator/releases/download/v2.0.10/noobaa-linux-v2.0.10

curl -s https://api.github.com/repos/noobaa/noobaa-operator/releases/latest | grep "linux" | cut -d : -f 2,3 | tr -d \" | wget -qi - ; mv noobaa-linux-* noobaa ; chmod +x noobaa; sudo mv noobaa /usr/bin/

### Create your bucket

noobaa obc create something -n openshift-storage

When creating a noobba bucket you will see something like [noobaa_instrcutions.txt](noobaa_instrcutions.txt)

## s3

I think there is two cli tools for s3.
s3 and s3cmd described in the [ceph.md](ceph.md) file.

### Install s3

There is multiple ways to do this.

From epel:

sudo yum install libs3-4.1-0.6.20190408git287e4be.el8.x86_64

### Sync a folder

In my case it's called ocs

s3 sync ocs s3://something-ec909d91-5794-4acd-ba49-53ec2e2c1f56/

### List files

s3 ls s3://something-ec909d91-5794-4acd-ba49-53ec2e2c1f56/

## General admin

### Show master pod

In OCS there is always a failover pod for the different resource management systems like the CNI.
To be able to know where to look for logs you need to know which one is the master, perform:

oc get leases

### CSINode

oc get CSINode

### csidriver

Rook creates the drivers

oc get csidriver
