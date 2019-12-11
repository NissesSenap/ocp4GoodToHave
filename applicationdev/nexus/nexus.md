# Nexus

```bash

oc new-project ${GUID}-nexus --display-name "${GUID} Shared Nexus"

oc new-app sonatype/nexus3:latest --name=nexus
oc expose svc nexus
oc rollout pause dc nexus

oc patch dc nexus --patch='{ "spec": { "strategy": { "type": "Recreate" }}}'
oc set resources dc nexus --limits=memory=2Gi,cpu=2 --requests=memory=1Gi,cpu=500m

oc set volume dc/nexus --add --overwrite --name=nexus-volume-1 --mount-path=/nexus-data/ --type persistentVolumeClaim --claim-name=nexus-pvc --claim-size=10Gi

oc set probe dc/nexus --liveness --failure-threshold 3 --initial-delay-seconds 60 -- echo ok
oc set probe dc/nexus --readiness --failure-threshold 3 --initial-delay-seconds 60 --get-url=http://:8081/

oc rollout resume dc nexus


# Create the svc that will be used to push images port 5000
oc create -f svc.yaml

# Create the route
oc create route edge --service=nexus-registry --insecure-policy=""
```
