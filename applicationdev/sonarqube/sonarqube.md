# Sonarqube

So much fun

https://github.com/wkulhanek/docker-openshift-sonarqube

```bash

# Create postgres
oc new-app postgresql-persistent \
--param POSTGRESQL_USER=sonar --param POSTGRESQL_PASSWORD=sonar --param POSTGRESQL_DATABASE=sonar --param VOLUME_CAPACITY=4Gi -lapp=sonarqube_db

# Create sonar
oc new-app quay.io/gpte-devops-automation/sonarqube:7.9.1 -e SONARQUBE_JDBC_USERNAME=sonar -e SONARQUBE_JDBC_PASSWORD=sonar -e SONARQUBE_JDBC_URL=jdbc:postgresql://postgresql/sonar

oc rollout pause dc sonarqube

oc expose svc sonarqube

echo "apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: sonarqube-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi" | oc create -f -

oc set volume dc/sonarqube --add --overwrite --name=sonarqube-volume-1 --mount-path=/opt/sonarqube/data/ --type persistentVolumeClaim --claim-name=sonarqube-pvc

oc set resources dc sonarqube --limits=memory=3Gi,cpu=2 --requests=memory=2Gi,cpu=1

oc patch dc sonarqube --patch='{ "spec": { "strategy": { "type": "Recreate" }}}'

oc label dc sonarqube tuned.openshift.io/elasticsearch=true


oc patch dc sonarqube --type=merge --patch='{"spec": {"template": {"metadata": {"labels": {"tuned.openshift.io/elasticsearch": "true"}}}}}'

oc rollout resume dc sonarqube

```
