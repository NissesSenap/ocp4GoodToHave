# Build

So lets do some usefull stuff in s2i

## Start a new app and put a secret so you can pull git repo behind password.

```bash
oc new-app --template=eap72-basic-s2i --param APPLICATION_NAME=tasks --param SOURCE_REPOSITORY_URL=http://gogs-gogs.${GUID}-gogs.svc.cluster.local:3000/CICDLabs/openshift-tasks-private.git --param SOURCE_REPOSITORY_REF=master --param CONTEXT_DIR=/ --param MAVEN_MIRROR_URL=http://nexus.${GUID}-nexus.svc.cluster.local:8081/repository/maven-all-public

oc create secret generic gogs-secret --from-literal=username=enorling-redhat.com --from-literal=password=Hejsan123

oc set build-secret --source bc/tasks gogs-secret

oc start-build tasks
```

## Let's use artifacts to make the build faster

```bash
oc patch bc tasks --patch='{"spec":{"strategy": {"sourceStrategy": {"forcePull": false}}}}'

oc patch bc/tasks --patch='{"spec": {"strategy": {"sourceStrategy": {"incremental": true}}}}'

```

## Build through is

oc new-app --image-stream=redhat-openjdk18-openshift:1.2 https://github.com/redhat-gpte-devopsautomation/ola.git

## Build from binary

First create the image-stream
Then push up the binary from your local repo
In this example we assume that you have a jar built from:
https://github.com/redhat-gpte-devopsautomation/ola.git

```bash
oc new-build --binary=true --name=ola-binary --image-stream=redhat-openjdk18-openshift:1.2

oc start-build ola-binary --from-file=$HOME/ola/target/ola.jar --follow

# Wait for jar to uploaded and perfrom
oc new-app ola-binary
```

Instead of doing this check out: https://github.com/openshift/odo

## Set build config limits

The set api currently don't allow buildconfig to be updated using set.

*NOTE* Bellow command don't work!
```oc set resources bc builder --limits=memory=3Gi,cpu=2 --requests=memory=2Gi,cpu=1```

error: buildconfigs/builder the object is not a pod or does not have a pod template: *v1.BuildConfig

There is a system wide build config that you can make: build.config.openshift.io/cluster
https://docs.openshift.com/container-platform/4.1/builds/build-configuration.html#builds-configuration-file_build-configuration

That should overwrite your default limits.

If your admin don't want to do that perform your favorite patch command:

oc patch bc builder --patch='{"spec":{"resources": {"limits": {"cpu": "1", "memory": "2Gi"},"requests": {"cpu": "500m","memory": "1Gi"}}}}'

## Chained builds

```bash
# Create a new is, don't ask me why the default golang one isn't a good option.
oc import-image jorgemoralespou/s2i-go --confirm

# Use the s2i-go is and create a build
oc new-build s2i-go~https://github.com/tonykay/ose-chained-builds --context-dir=/go-scratch/hello_world --name=builder

oc new-build --name=runtime \
   --source-image=builder \
   --source-image-path=/opt/app-root/src/go/src/main/main:. \
   --dockerfile=$'FROM scratch\nCOPY main /main\nEXPOSE 8080\nUSER 9696\nENTRYPOINT ["/main"]'

# Start the app when the build is ready
oc new-app runtime --name=my-application

```
