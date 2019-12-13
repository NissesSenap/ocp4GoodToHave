# Jenkins

So lets set up a basic pipeline that builds stuff in dev and pushes in using a blue-green deployment to prod.

## Setup dev env

```bash
# Set up Dev Project
oc new-project ${GUID}-tasks-dev --display-name "${GUID} Tasks Development"
oc policy add-role-to-user edit system:serviceaccount:${GUID}-jenkins:jenkins -n ${GUID}-tasks-dev

# Set up Dev Application
oc new-build --binary=true --name="tasks" jboss-eap72-openshift:1.0 -n ${GUID}-tasks-dev

# NOTICE --allow-missing-imagestream-tags=true
oc new-app ${GUID}-tasks-dev/tasks:0.0-0 --name=tasks --allow-missing-imagestream-tags=true -n ${GUID}-tasks-dev

oc set triggers dc/tasks --remove-all -n ${GUID}-tasks-dev

oc expose dc tasks --port 8080 -n ${GUID}-tasks-dev

oc expose svc tasks -n ${GUID}-tasks-dev

oc set probe dc/tasks -n ${GUID}-tasks-dev --readiness --failure-threshold 3 --initial-delay-seconds 60 --get-url=http://:8080/

oc create configmap tasks-config --from-literal="application-users.properties=Placeholder" --from-literal="application-roles.properties=Placeholder" -n ${GUID}-tasks-dev

oc set volume dc/tasks --add --name=jboss-config --mount-path=/opt/eap/standalone/configuration/application-users.properties --sub-path=application-users.properties --configmap-name=tasks-config -n ${GUID}-tasks-dev

oc set volume dc/tasks --add --name=jboss-config1 --mount-path=/opt/eap/standalone/configuration/application-roles.properties --sub-path=application-roles.properties --configmap-name=tasks-config -n ${GUID}-tasks-dev
```

## Setup prod

```bash
# Set up Production Project
oc new-project ${GUID}-tasks-prod --display-name "${GUID} Tasks Production"
oc policy add-role-to-group system:image-puller system:serviceaccounts:${GUID}-tasks-prod -n ${GUID}-tasks-dev
oc policy add-role-to-user edit system:serviceaccount:${GUID}-jenkins:jenkins -n ${GUID}-tasks-prod

# Create Blue Application
oc new-app ${GUID}-tasks-dev/tasks:0.0 --name=tasks-blue --allow-missing-imagestream-tags=true -n ${GUID}-tasks-prod
oc set triggers dc/tasks-blue --remove-all -n ${GUID}-tasks-prod
oc expose dc tasks-blue --port 8080 -n ${GUID}-tasks-prod
oc set probe dc tasks-blue -n ${GUID}-tasks-prod --readiness --failure-threshold 3 --initial-delay-seconds 60 --get-url=http://:8080/
oc create configmap tasks-blue-config --from-literal="application-users.properties=Placeholder" --from-literal="application-roles.properties=Placeholder" -n ${GUID}-tasks-prod
oc set volume dc/tasks-blue --add --name=jboss-config --mount-path=/opt/eap/standalone/configuration/application-users.properties --sub-path=application-users.properties --configmap-name=tasks-blue-config -n ${GUID}-tasks-prod
oc set volume dc/tasks-blue --add --name=jboss-config1 --mount-path=/opt/eap/standalone/configuration/application-roles.properties --sub-path=application-roles.properties --configmap-name=tasks-blue-config -n ${GUID}-tasks-prod

# Create Green Application
oc new-app ${GUID}-tasks-dev/tasks:0.0 --name=tasks-green --allow-missing-imagestream-tags=true -n ${GUID}-tasks-prod
oc set triggers dc/tasks-green --remove-all -n ${GUID}-tasks-prod
oc expose dc tasks-green --port 8080 -n ${GUID}-tasks-prod
oc set probe dc tasks-green -n ${GUID}-tasks-prod --readiness --failure-threshold 3 --initial-delay-seconds 60 --get-url=http://:8080/
oc create configmap tasks-green-config --from-literal="application-users.properties=Placeholder" --from-literal="application-roles.properties=Placeholder" -n ${GUID}-tasks-prod
oc set volume dc/tasks-green --add --name=jboss-config --mount-path=/opt/eap/standalone/configuration/application-users.properties --sub-path=application-users.properties --configmap-name=tasks-green-config -n ${GUID}-tasks-prod
oc set volume dc/tasks-green --add --name=jboss-config1 --mount-path=/opt/eap/standalone/configuration/application-roles.properties --sub-path=application-roles.properties --configmap-name=tasks-green-config -n ${GUID}-tasks-prod

# Expose Blue service as route to make blue application active
oc expose svc/tasks-blue --name tasks -n ${GUID}-tasks-prod
```

## Setup pipline Jenkins

If you want to use jenkins to run your pipeline go in to jenkins create a pipline item.
Under Pipeline klick Definition and pick Pipline script from SCM and fill in your requiered info.

## Setup OCP pipeline

So if you want to be able to view your pipeline within openshift you can create a BuildConfig with type "JenkinsPipeline".
This need to be created in the same namespace as your jenkins master.

```bash
oc apply -f Buildconfig.yaml -n c0e7-jenkins
oc create secret generic gogs-secret --from-literal=<user_name> --from-literal=password=<password> -n c0e7-jenkins
oc set build-secret --source bc/tasks-pipeline gogs-secret -n c0e7-jenkins
```

You will now see your pipeline under Builds → Build Configs in your jenkins project.
