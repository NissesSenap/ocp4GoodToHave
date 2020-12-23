# CEPH

Following CEPH125R

- [CEPH](#ceph)
  - [Overview](#overview)
  - [Architecture](#architecture)
    - [Ceph's Storage Back end Components](#cephs-storage-back-end-components)
  - [Commands](#commands)
    - [ceph status](#ceph-status)
    - [osd tree](#osd-tree)
    - [osd stat](#osd-stat)
    - [osd disk usage](#osd-disk-usage)
    - [List pools in cluster](#list-pools-in-cluster)
    - [Set pool-quota](#set-pool-quota)
    - [Add/remove snapshot](#addremove-snapshot)
    - [List snapshots](#list-snapshots)
    - [roll-back snapshot](#roll-back-snapshot)
    - [Increase replica of pool](#increase-replica-of-pool)
    - [Pool details](#pool-details)
    - [View specific config](#view-specific-config)
    - [Cleanup disks](#cleanup-disks)
  - [Ansbile](#ansbile)
    - [limited ansible run](#limited-ansible-run)
    - [Keyring issues](#keyring-issues)
  - [Replica pools](#replica-pools)
    - [Create osd pool](#create-osd-pool)
    - [Enable application on pool](#enable-application-on-pool)
    - [Delete pool](#delete-pool)
    - [Write to pool using rados](#write-to-pool-using-rados)
    - [List obecjts in pool using rados](#list-obecjts-in-pool-using-rados)
    - [List all objects in all namespaces](#list-all-objects-in-all-namespaces)
    - [CEPH PG:s per pool calculator](#ceph-pgs-per-pool-calculator)
  - [Erasure pools](#erasure-pools)
    - [Create erasure coded pool](#create-erasure-coded-pool)
    - [list erasure profile](#list-erasure-profile)
    - [Details erasure profile](#details-erasure-profile)
  - [Cephx](#cephx)
    - [Create user](#create-user)
    - [View users/access](#view-usersaccess)
    - [Get auth details](#get-auth-details)
    - [Export user](#export-user)
    - [Import user](#import-user)
    - [Update user access](#update-user-access)
  - [RBD](#rbd)
    - [Create rbd pool](#create-rbd-pool)
    - [Set pool app to rbd](#set-pool-app-to-rbd)
    - [Create a RBD SA](#create-a-rbd-sa)
    - [cephx set default id](#cephx-set-default-id)
    - [Create rbd image](#create-rbd-image)
    - [View rbd](#view-rbd)
    - [rbd info](#rbd-info)
    - [Map rbd to server](#map-rbd-to-server)
    - [rbd showmapped](#rbd-showmapped)
    - [Create and map filesystem](#create-and-map-filesystem)
    - [Rbd usage](#rbd-usage)
  - [RBD snapshots](#rbd-snapshots)
    - [fsfreeze mount](#fsfreeze-mount)
    - [create snapshot](#create-snapshot)
    - [unfreeze mount](#unfreeze-mount)
    - [protect snap](#protect-snap)
    - [list pool snaps](#list-pool-snaps)
    - [clone snap](#clone-snap)
    - [unprotect snap](#unprotect-snap)
    - [remove snap](#remove-snap)
  - [RBD mirror for DR](#rbd-mirror-for-dr)
    - [scp config files](#scp-config-files)
    - [Cluster mirror health](#cluster-mirror-health)
    - [enable pool mirror](#enable-pool-mirror)
    - [Peer account for mirroring](#peer-account-for-mirroring)
    - [Verify mirroring status](#verify-mirroring-status)
    - [Create rbd img in mirror pool](#create-rbd-img-in-mirror-pool)
    - [Mirror image status](#mirror-image-status)
    - [Remove mirror img](#remove-mirror-img)
  - [RBD export/import](#rbd-exportimport)
    - [rbd export](#rbd-export)
    - [rbd import](#rbd-import)
    - [Import remote with cat](#import-remote-with-cat)
  - [RGW S3 API](#rgw-s3-api)
    - [Create S3 user](#create-s3-user)
    - [s3cmd config](#s3cmd-config)
    - [Create S3 bucket](#create-s3-bucket)
    - [List S3 buckets](#list-s3-buckets)
    - [Add object to S3](#add-object-to-s3)
    - [Get file using http](#get-file-using-http)
    - [Status big S3 files](#status-big-s3-files)
    - [Create S3 admin](#create-s3-admin)
    - [View RGW buckets](#view-rgw-buckets)
    - [Get metadata bucket](#get-metadata-bucket)
  - [RGW OpenStack Swift](#rgw-openstack-swift)
    - [Create swift user](#create-swift-user)
    - [Install swiftclient](#install-swiftclient)
    - [Verify swift access](#verify-swift-access)
    - [Swift list containers](#swift-list-containers)
    - [Create swift container](#create-swift-container)
    - [Swift upload object](#swift-upload-object)
  - [Multisite RGW](#multisite-rgw)
    - [Create realm](#create-realm)
    - [Delete zonegroup](#delete-zonegroup)
    - [Create zonegroup](#create-zonegroup)
    - [Configure main zone](#configure-main-zone)
    - [Create replication user](#create-replication-user)
    - [Commit period changes](#commit-period-changes)
    - [Secondary server, pull realm](#secondary-server-pull-realm)
    - [Secondary server, pull period](#secondary-server-pull-period)
    - [Secondary server, set default realm/zone](#secondary-server-set-default-realmzone)
    - [Secondary server, create fallback zone](#secondary-server-create-fallback-zone)
    - [Secondary server, commit fallback](#secondary-server-commit-fallback)
    - [Sync status](#sync-status)
      - [test sync](#test-sync)
  - [CephFS](#cephfs)
    - [Verify cephfs df](#verify-cephfs-df)
    - [Save auth-key to file](#save-auth-key-to-file)
    - [mount cephfs client way](#mount-cephfs-client-way)
    - [Enable snapshot cephfs](#enable-snapshot-cephfs)
    - [Create snapshot](#create-snapshot)
  - [CRUSH SSD pool configuration](#crush-ssd-pool-configuration)
    - [List crush classes](#list-crush-classes)
    - [show crush tree](#show-crush-tree)
    - [Create crush rule](#create-crush-rule)
    - [List crush rules](#list-crush-rules)
    - [Create pool with crush rule](#create-pool-with-crush-rule)
    - [Get CRUSH id](#get-crush-id)
    - [Verify crush pool usage](#verify-crush-pool-usage)
  - [CRUSH conf on location](#crush-conf-on-location)
    - [Create CRUSH buckets](#create-crush-buckets)
    - [build CRUSH hierarchy](#build-crush-hierarchy)
    - [Verify CRUSH hierarchy](#verify-crush-hierarchy)
    - [Verify supplied script](#verify-supplied-script)
    - [Add CRUSH hook to config](#add-crush-hook-to-config)
  - [Opeartions](#opeartions)
    - [Osd dump](#osd-dump)
    - [Change osd affinity](#change-osd-affinity)
    - [Check multiple osd](#check-multiple-osd)
    - [Determine file osd location](#determine-file-osd-location)
    - [Performance per osd](#performance-per-osd)
    - [Benchmark test](#benchmark-test)
    - [Verfiy keyring usage](#verfiy-keyring-usage)

## Overview

Red Hat Ceph Storage focuses on providing a unified storage solution for:

- block-based
- object-based
- file-based

 The design of Ceph is designed to achieve the following goals:

- Be scalable for every component
- Provide no single point of failure
- Be software-based (not an appliance) and open source (no vendor lock-in)
- Run on readily available hardware
- Be self-managed wherever possible, minimizing user intervention

## Architecture

RADOS: (Reiliable Autonomous Distributed Object Store) is a object storage back end.

LIBRADOS: A libary to directly access RADOS (C, C++, JAVA, Python, Ruby)

The following is the 3 avaliable way to interact with CEPH unless you use LIBRADOS

- RBD (RADOS Block Device): Block storage good when you use Vm-ware to create
- RGW (RADOS Gateway): Object storage, S3 and open-stack swift compatible
- CephFS (Ceph File System): File-system based storage for POSIX based systems, it's supported but the snapshot function is still in technical preview.

### Ceph's Storage Back end Components

RADOS, the Ceph storage back end, is based on the following daemons, which can be scaled out to meet the requirements of the architecture being deployed:

Monitors (MONs) , which maintain maps of the cluster state and are used to help the other daemons coordinate with each other.

Object Storage Devices (OSDs) , which store data and handle data replication, recovery and rebalancing.

Managers (MGRs) , which keep track of runtime metrics and expose cluster information through a web browser-based dashboard and REST API.

Metadata Servers (MDSs) , which store metadata used by CephFS (but not object storage or block storage) to allow efficient POSIX command execution by clients.

## Commands

### ceph status

ceph -s

### osd tree

Shows the disk used in your osd on your nodes

ceph osd tree

### osd stat

Only check osd, but the same info as ceph -s

ceph osd stat

### osd disk usage

ceph osd df

### List pools in cluster

ceph osd lspools

or

ceph osd pool ls detail

### Set pool-quota

ceph osd pool set-quota myfirstpool max_objects 1000

to remove quota set max_objects=0

### Add/remove snapshot

ceph osd pool mksnap pool-namesnap-name

ceph osd pool rmsnap pool-namesnap-name

### List snapshots

rados -p pool-name -s snap-name get object-namefile

### roll-back snapshot

rados -p pool-name rollback object-namesnap-name

### Increase replica of pool

ceph osd pool set mypool size 3

### Pool details

ceph osd pool ls detail

### View specific config

ceph daemon osd.0 config show

ceph daemon mds.servera config get mds_data

### Cleanup disks

If you have had old disks that is "dirty" from old partitions.
Use the following to delete everything from them.

ceph-disk zap /dev/vdb

## Ansbile

Requiered rpm package to get ansible scripts:

sudo yum install -y ceph-ansible

Ansible path:

/usr/share/ceph-ansible

### limited ansible run

**NOTE** This command will use /etc/ansible/hosts

cd /usr/share/ceph-ansible

ansible-playbook --limit=clients site.yml

### Keyring issues

If you get issues with the keyring not being put to your client for example. You can copy it over to your client (probably not good).
if you run ceph -s

The real command that happens is:

ceph -n client.admin --keyring=/etc/ceph/ceph.client.admin.keyring health

https://docs.ceph.com/docs/mimic/rados/operations/user-management/

## Replica pools

Before you can store anything on your brand new CEPH installation.
You need to create a Pool, this pool contains multiple OSD and CEPH with the help of CRUSH (Controlled Replication Under Scalable Hashing) sends out the different objects to different OSD.

The number of placement groups in a pool has a major impact on performance. If you configure too few placement groups in a pool, too much data will need to be stored in each PG and Ceph will not perform well. If you configure too many placement groups in a pool, the OSDs will require a large amount of RAM and CPU time and Ceph will not perform well. Typically, a pool should be configured to contain 100 - 200 placement groups per OSD.

### Create osd pool

ceph osd pool create pool-namepg-num [pgp-num]  \ 
[replicated] [crush-ruleset-name] [expected-num-objects]

**Where:**

- pool-name is the name of the new pool.

- pg-num is the total number of Placement Groups (PGs) for this pool.

- pgp-num is the effective number of placement groups for this pool. Normally, this should be equal to the total number of placement groups.

- replicated specifies that this is a replicated pool, and is normally the default if not included in the command.

- crush-ruleset-name is the name of the CRUSH rule set you want to use for this pool. The osd_pool_default_crush_replicated_ruleset configuration parameter sets the default value.

- expected-num-objects is the expected number of objects in the pool. If you know this number in advance, Ceph can prepare a folder structure on the OSD's XFS file system at pool creation time. Otherwise, Ceph reorganizes this directory structure at runtime as the number of objects increases. This reorganization has a latency impact.

**Example:**

ceph osd pool create myfirstpool 50 50

### Enable application on pool

We must assign the pool so it knows what it will be used for.

- cephfs: Ceph File System

- rbd: Ceph Block Device

- rgw: Ceph Object Gateway (S3)

ceph osd pool application enable pool-nameapp

**Example:**

ceph osd pool application enable myfirstpool rbd

### Delete pool

ceph osd pool delete pool-namepool-name --yes-i-really-really-mean-it

**NOTE**

In Red Hat Ceph Storage 3, for extra protection, Ceph sets the mon_allow_pool_delete configuration parameter to false.
With this directive, and even with the --yes-i-really-really-mean-it option, the ceph osd pool delete command does not result in the deletion of the pool.

You can set the mon_allow_pool_delete parameter to true and restart the mon services to allow pool deletion.

### Write to pool using rados

Store the file /etc/services in srv object in namespace system in the mytestpool pool.

rados -p mytestpool -N system put srv /etc/services

### List obecjts in pool using rados

rados -p mytestpool -N system ls

### List all objects in all namespaces

rados -p mytestpool --all ls --format=json | python -m json.tool

### CEPH PG:s per pool calculator

https://access.redhat.com/labs/cephpgc/

## Erasure pools

We save disk
but calculation of the coding chunks adds CPU and memory overhead for erasure coded pools, reducing performance.
In addition, in Red Hat Ceph Storage 3, operations that require partial object writes are not supported for erasure coded pools.

Red Hat Ceph Storage currently only supports erasure coded pools accessed through the Ceph Object Gateway.

### Create erasure coded pool

ceph osd pool create pool-name pg-num [pgp-num] erasure [erasure-code-profile] [crush-ruleset-name] [expected_num_objects]

**Where:**

- pool-name is the name for the new pool.

- pg-num is the total number of Placement Groups (PGs) for this pool.

- pgp-num is the effective number of placement groups for this pool. Normally, this should be equal to the total number of placement groups.

- erasure specifies that this is an erasure coded pool.

- erasure-code-profile is the name of the profile to use. You can create new profiles with the ceph osd erasure-code-profile set command as described below. A profile defines the k and m values and the erasure code plug-in to use. By default, Ceph uses the default profile.

- crush-ruleset-name is the name of the CRUSH rule set to use for this pool. If not set, Ceph uses the one defined in the erasure code profile.

- expected-num-objects is the expected number of objects in the pool. If you know this number in advance, Ceph can prepare a folder structure on the OSD's XFS file system when it creates the pool. Otherwise, Ceph reorganizes this directory structure at runtime as the number of objects increases. This reorganization has a latency impact.

**Example:**

ceph osd pool create mysecondpool 50 50 erasure

### list erasure profile

ceph osd erasure-code-profile ls

### Details erasure profile

ceph osd erasure-code-profile get default

## Cephx

Authentication time.

Cephx is installed by default, it's the keyring solution.

CEPH uses user accounts for several purposes:

- Internal communication between Ceph daemons
- Client applications accessing the Red Hat Ceph Storage cluster through the librados library
- Ceph administrators

### Create user

ceph auth get-or-create client.formyapp2 mon 'allow r' osd 'allow rw pool=myapp'

### View users/access

ceph auth list

### Get auth details

ceph auth get client.admin

### Export user

ceph auth export client.operator1 > ~/operator1.export

### Import user

ceph auth import -i ~/operator1.export

### Update user access

ceph auth caps client.application1 mon 'allow r' osd 'allow rw pool=myapp'

## RBD

How to create a block devide for linux clients.

### Create rbd pool

ceph osd pool create pool-rbd 32

### Set pool app to rbd

Shortcut:

rbd pool init pool-rbd

Normal way:
ceph osd pool application enable pool-rbd rbd

### Create a RBD SA

ceph auth get-or-create client.rbd.servera \
mon 'profile rbd' osd 'profile rbd' \
 -o /etc/ceph/ceph.client.rbd.servera.keyring

### cephx set default id

This to not be forced to add --id etc everytime you write a command.

export CEPH_ARGS='--id=rbd.servera'

### Create rbd image

rbd create rbd/test --size=128M

### View rbd

rbd ls

### rbd info

rbd info rbd/test

### Map rbd to server

sudo rbd --id rbd.servera map rbd/test

### rbd showmapped

rbd showmapped

### Create and map filesystem

``` bash
sudo mkfs.ext4 /dev/rbd0
sudo mkdir /mnt/rbd
sudo mount /dev/rbd0 /mnt/rbd
sudo chown ceph:ceph /mnt/rbd
```

### Rbd usage

rbd du rbd/test

## RBD snapshots

Follow these commands if you want to perfrom a snapshot of a mounted rbd image.

### fsfreeze mount

sudo fsfreeze --freeze /mnt/source

### create snapshot

rbd snap create rbd/clonetest@clonesnap

### unfreeze mount

sudo fsfreeze --unfreeze /mnt/source

### protect snap

rbd snap protect rbd/clonetest@clonesnap

### list pool snaps

rbd snap ls rbd/clonetest

### clone snap

rbd clone rbd/clonetest@clonesnap rbd/realclone

### unprotect snap

rbd snap unprotect rbd/clonetest@clonesnap

### remove snap

rbd snap purge rbd/clonetest

## RBD mirror for DR

**RBD Mirroring supports two configurations:**

- One-way mirroring or active-passive
  - Client only needs to reach one cluster and a mirror client acts as middle man.
- Two-way mirroring or active-active
  - Client needs to reach both clusters.

**Supported Mirroring Modes:**

- Pool mode
- Image mode

### scp config files

scp over the keyrings and config files the followign for the different clusters:

**serverc:**

- /etc/ceph/prod.conf
- /etc/ceph/prod.client.admin.keyring

**serverf:**

- /etc/ceph/bup.conf
- /etc/ceph/bup.client.admin.keyring

### Cluster mirror health

ceph -s --cluster prod

ceph -s --cluster bup

### enable pool mirror

rbd mirror pool enable rbd pool --cluster bup

rbd mirror pool enable rbd pool --cluster prod

### Peer account for mirroring

rbd mirror pool peer add rbd client.admin@prod --cluster bup

### Verify mirroring status

rbd mirror pool info rbd --cluster bup

rbd mirror pool status rbd --cluster bup

### Create rbd img in mirror pool

rbd create rbd/prod1 --size=128M \
--image-feature=exclusive-lock,journaling --cluster prod

### Mirror image status

rbd mirror image status rbd/prod1 --cluster bup

### Remove mirror img

rbd rm rbd/prod1 --cluster prod

## RBD export/import

You can import exmport images.

### rbd export

rbd export rbd/test ~/export.dat

### rbd import

rbd import rbd/test ~/export.dat

### Import remote with cat

cat ~/export.dat | ssh ceph@serverf rbd import - rbd/test

## RGW S3 API

### Create S3 user

radosgw-admin user create --uid="operator" \
--display-name="S3 Operator" --email="operator@example.com" \ --access_key="12345" --secret="67890"

### s3cmd config

s3cmd --configure

After going through the guide update the following values to match your server:

[student@servera ~]$ grep -r host_ ~/.s3cfg
host_base = servera
host_bucket = %(bucket)s.servera

### Create S3 bucket

s3cmd mb s3://my-bucket

### List S3 buckets

s3cmd ls

### Add object to S3

s3cmd put --acl-public /tmp/10MB.bin s3://my-bucket/10MB.bin

### Get file using http

wget -O /dev/null http://my-bucket.servera/10MB.bin

or

wget -O /dev/null http://servera/my-bucket/10MB.bin

### Status big S3 files

If you upload a big file to s3 it might take a long time.
To view status of the upload and potential stuck uploads.

s3cmd multipart s3://nano

### Create S3 admin

radosgw-admin user create --uid=admin \
--display-name="Admin User" \
--caps="users=read,write;usage=read,write; \
buckets=read,write;zone=read,write" \
--access-key="abcde" --secret="qwerty"

### View RGW buckets

radosgw-admin bucket list

### Get metadata bucket

radosgw-admin metadata get bucket:my-bucket

## RGW OpenStack Swift

Swift uses multi-tier design, built around tenants and users for auth.

While S3 uses single-tier design.
A single user account may have multiple access keys and secrets which are used to provide different types of access in the same account.

Due to this when creating a Swift user you create "subusers".

### Create swift user

radosgw-admin subuser create --uid="operator" \
--subuser="operator:swift" --access="full" \
--secret="opswift"

### Install swiftclient

sudo yum -y install python-swiftclient

### Verify swift access

swift -V 1.0 -A http://servera/auth/v1 -U operator:swift -K opswift stat

### Swift list containers

swift -V 1.0 -A http://servera/auth/v1 -U operator:swift -K opswift list

### Create swift container

swift -V 1.0 -A http://servera/auth/v1 -U operator:swift -K opswift create my-container

### Swift upload object

swift -V 1.0 -A http://servera/auth/v1 -U operator:swift -K opswift upload my-container /tmp/swift.dat

## Multisite RGW

### Create realm

radosgw-admin realm create --rgw-realm=ceph125 --default

### Delete zonegroup

radosgw-admin zonegroup delete --rgw-zonegroup=default

### Create zonegroup

And make it default

radosgw-admin zonegroup create --rgw-zonegroup=classroom \
--endpoints=http://servera:80 --master --default

### Configure main zone

export SYSTEM_ACCESS_KEY=replication
export SYSTEM_SECRET_KEY=secret

radosgw-admin zone create --rgw-zonegroup=classroom \
--rgw-zone=main --endpoints=http://servera:80 \
--access-key=$SYSTEM_ACCESS_KEY --secret=$SYSTEM_SECRET_KEY

### Create replication user

Create a system user named repl.user to access the zone pools.
The keys for the repl.user user must match the keys configured for the zone.

radosgw-admin user create --uid="repl.user" \
 --display-name="Replication User" \
 --access-key=$SYSTEM_ACCESS_KEY --secret=$SYSTEM_SECRET_KEY \
 --system

### Commit period changes

radosgw-admin period update --commit

### Secondary server, pull realm

**From serverf:**

radosgw-admin realm pull --url=http://servera:80 \
--access-key=$SYSTEM_ACCESS_KEY --secret=$SYSTEM_SECRET_KEY

### Secondary server, pull period

**From serverf:**

radosgw-admin period pull --url=http://servera:80 \ --access-key=$SYSTEM_ACCESS_KEY --secret=$SYSTEM_SECRET_KEY

### Secondary server, set default realm/zone

**From serverf:**

radosgw-admin realm default --rgw-realm=ceph125

radosgw-admin zonegroup default --rgw-zonegroup=classroom

### Secondary server, create fallback zone

**From serverf:**

radosgw-admin zone create --rgw-zonegroup=classroom \
--rgw-zone=fallback  --endpoints=http://serverf:80 \
--access-key=$SYSTEM_ACCESS_KEY --secret=$SYSTEM_SECRET_KEY \
--default

### Secondary server, commit fallback

**From serverf:**

radosgw-admin period update --commit --rgw-zone=fallback

### Sync status

**From serverf:**

radosgw-admin sync status

#### test sync

**From servera:**

radosgw-admin user create --uid="s3user" \
--display-name="S3 User" --id rgw.servera \
--access-key="s3user" --secret-key="password"

radosgw-admin user list

**From serverf:**
radosgw-admin user list

You should now see the s3user on serverf as well.

## CephFS

CephFS isn't NFS.

You can mount CephFS two ways:

- kernel client (available starting with RHEL 7.3)
- FUSE client (available starting with RHEL 7.2)

As allways there are good and bad things with both.
**Example:**

- Kernel client does not support quotas but may be faster.
- FUSE client supports quotas and ACLs, but they have to be enabled explicitly

As allways install using ansible.

### Verify cephfs df

ceph df

You should see among other things:

cephfs_data
cephfs_metadata

### Save auth-key to file

ceph auth get-key client.admin | sudo tee /root/asecret

### mount cephfs client way

sudo mount -t ceph serverc:/ /mnt/cephfs \
-o name=admin,secretfile=/root/asecret

### Enable snapshot cephfs

Exprimental feature, don't use in prod.
(Don't know why they teach none supported features)

sudo ceph mds set allow_new_snaps true --yes-i-really-mean-it

### Create snapshot

Just like EMC and netapp users can restore their own files from snapshot.
Just go in to the .snap folder and you will find all the snapshots.
You can even create a snapshot by creating a folder with a random name.

mkdir /mnt/cephfs/.snap/mysnap

## CRUSH SSD pool configuration

Let's assign a pool to only use SSD disks

### List crush classes

I think this is the different types of disks that is found in your osd:s.

ceph osd crush class ls

output:
[
    "hdd",
    "ssd"
]

### show crush tree

List your osd disks and classes together with it's CRUSH weight.

ceph osd crush tree

### Create crush rule

ceph osd crush rule create-replicated onssd default host ssd

### List crush rules

ceph osd crush rule ls

### Create pool with crush rule

ceph osd pool create myfast 32 32 onssd

### Get CRUSH id

List all the pools ID:s. In my case myfast have id: 18

ceph osd lspools

### Verify crush pool usage

List PG (PoolGroups), and see how the PG is spread out on which disks.

From **ceph osd crush tree** we know the osd disk id:s that have ssh.
We should see only those disks id:s used from bellow command:

ceph pg dump pgs_brief | grep -F 18.

## CRUSH conf on location

Let's define how data should be spread over the cluster depending on where they
are physically located.

We will create the following:

```txt
default-ceph125    (root bucket)
    rackblue       (rack bucket)
        hostc      (host bucket)
            osd.4
            osd.6
            osd.8

    rackgreen      (rack bucket)
        hostd      (host bucket)
            osd.0
            osd.1
            osd.2

    rackpink       (rack bucket)
        hoste      (host bucket)
            osd.3
            osd.5
            osd.7
```

### Create CRUSH buckets

```bash
ceph osd crush add-bucket default-ceph125 root
ceph osd crush add-bucket rackblue rack
ceph osd crush add-bucket hostc host
ceph osd crush add-bucket rackgreen rack
ceph osd crush add-bucket hostd host
ceph osd crush add-bucket rackpink rack
ceph osd crush add-bucket hoste host
```

### build CRUSH hierarchy

```bash
ceph osd crush move rackblue root=default-ceph125
ceph osd crush move hostc rack=rackblue
ceph osd crush move rackgreen root=default-ceph125
ceph osd crush move hostd rack=rackgreen
ceph osd crush move rackpink root=default-ceph125
ceph osd crush move hoste rack=rackpink
```

### Verify CRUSH hierarchy

ceph osd crush tree

### Verify supplied script

In CEPH125 course we have gotten my-crush-location script.
It more or less talks to ceph ask how we have configured the CRUSH map.
We will use this script as a hook

/usr/local/bin/my-crush-location --cluster ceph --type osd --id 0

### Add CRUSH hook to config

To all osd hosts edit /etc/ceph/ceph.conf

[osd]
crush_location_hook = /usr/local/bin/my-crush-location

Don't forget to restart ceph-osd.target

sudo systemctl restart ceph-osd.target

Can ofc be done in Ansbile under ceph_config_overrides.

## Opeartions

### Osd dump

You can get a easy overview of the cluster looking at the OSD map

ceph osd dump

The epoch values changes when a event have happend (like a osd shutdown)
You can also view the status of each OSD

### Change osd affinity

To my understanding affinity is the definition of the disk that get's read from.
If you do matinance on a disk you can change this for example.

The id of the disk is 3 and is gatherd from the ceph osd dump command.

When setting it to 0 it won't read anything.

**NOTE** I'm not 100% on this

ceph osd primary-affinity 3 1.0

### Check multiple osd

ceph tell osd.* version

### Determine file osd location

ceph osd map rbd file00

### Performance per osd

ceph osd perf

### Benchmark test

CEPH got a built in bench mark tool

rados -p rbd bench 300 write

### Verfiy keyring usage

In the bottom of the strace you will see which keyring that you use.

strace -e stat,open rados -p rbd ls
