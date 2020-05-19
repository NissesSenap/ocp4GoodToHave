# Kuberhealthy

I will try to explain how to install kuberhealthy on OCP 4.3.

I currently use the prometheus operator built in to OCP 4.3 and using a tech preview feature there. If you don't want to enable this tech preview you can just as well use the operator avaliabile in OLM/operatorhub.io or the upstream operator.

When writing this v2.1.2 is the latest tag and work from that.
Currently work is ongoing to mitegate a number of these issues, for example issues 400

## Deploy

If you want to use helm that is also an option, I currently don't.

```shell
git clone https://github.com/Comcast/kuberhealthy

cd kuberhealthy
oc new-project kuberhealthy

# This contains all the CRD, rbac etc.
oc apply -f deploy/kuberhealthy-prometheus-operator.yaml
```

### Give access to sa

Currently all of the pods run as root, this will be fixed in the next release.

oc adm policy add-scc-to-user anyuid -z kuberhealthy
oc adm policy add-scc-to-user anyuid -z daemonset-khcheck

#### Deployment check

Due to OCP scc the deployment that deployment-check creates it won't have rights to create it due it's nginx running in the pod and it needs root.

To mitigate this perform the following:

```shell
oc create sa khcheck-deployment-sa
oc adm policy add-scc-to-user anyuid -z khcheck-deployment-sa

# Add the following env variable
# TODO write this as a patch instead.
oc -n kuberhealthy edit khc deployment
      - name: CHECK_SERVICE_ACCOUNT
        value: khcheck-deployment-sa
```

It should look something like this.
spec:
  podSpec:
    containers:
    - env:
      - name: CHECK_TIME_LIMIT
        value: 15m
      - name: CHECK_DEPLOYMENT_REPLICAS
        value: "4"
      - name: CHECK_DEPLOYMENT_ROLLING_UPDATE
        value: "true"
      - name: CHECK_SERVICE_ACCOUNT
        value: khcheck-deployment-sa

#### Daemonset

Sadly Daemonset isn't as easy to fix.
This due to that daemonset currently hard codes securityContext.runAsUser=1000 which creates the following error when it runs:

Error creating: pods "ds-check-daemonset-1586258527-1586258534-" is forbidden: unable to validate against any security context constraint: [spec.containers[0].securityContext.securityContext.runAsUser: Invalid value: 1000: must be in the ranges: [1000550000, 1000559999]]

We are currently discussion solitions about this in issue 400 but it will take a bigger rewrite if we wan't a long term solution.

I currently do a **bad** solution which is I change it manually in the code and push it to one of my private repos.
The thing is:

The admission plug-in will look for the openshift.io/sa.scc.uid-range annotation on the current project to populate range fields, as it does not provide this range. In the end, a container will have runAsUser equal to the first value of the range that is hard to predict because every project has different ranges."

Which makes it differ in every project that you create, fun with fun, in short it won't work between
clusters and you will have to manage a container per kuberhealthy deployment.

Depending on how long the desission for a long term solution takes I might fix this with a environment variable.

To build your own release of kuberhealthy/daemonset-check:v2.2.1 perfrom the following from the kubrhealthy repo:

```shell
cd cmd/daemonset-check/
# TODO fix a sed
edit main.go
# search for runAsUser := int64(1000) and adapt the number to your range.
# For example: 1000550001 in my case this time...

make build
# Example how to login to quay.io
export QUAY_ID=nissessenap
export QUAY_PASSWORD='Super!!!Secret'
podman login -u ${QUAY_ID} -p ${QUAY_PASSWORD} quay.io  

# Tag the release for example to quay
podman tag localhost/kuberhealthy/daemonset-check:v2.1.1 quay.io/${QUAY_ID}/daemonset-check:v2.1.2
podman push quay.io/${QUAY_ID}/daemonset-check:v2.1.2

# Update your daemonset to match your image
oc edit -n kuberhealthy khc daemonset
oc get khc daemonset -o jsonpath='{.spec.podSpec.containers[*].image}'

```

Now all checks should work.

#### Can get the patch to work right now, will fix it later

oc -n kuberhealthy patch khchecks daemonset --patch '{"spec": {"podSpec": {"containers": [{"name": "main","image": "quay.io/nissessenap/daemonset-check:v2.1.3"}]}}}'

## Fix monitoring

The ServiceMonitor object that we deployed with kuberhealthy-prometheus-operator.yaml
contains:
spec:
  jobLabel: component

I didn't manage to find my service due to it.
Im 100% sure this isn't anything wrong it's just that I don't know how to search in prometheus good enough any more.
Due to this I removed it in my setup and I assume that you have done so as well, else
the pre defined grafana dashboard won't work.

So for now remove it.
```oc edit ServiceMonitor kuberhealthy -n kuberhealthy```

So now you can search the metrics in your prometheus dashboard, for example: kuberhealthy_running
or kuberhealthy_check_duration_seconds{check="kuberhealthy/deployment"}

If you want a list of all the avliable metrics you can do it a bunch of ways.
One easy way is to perfrom the following:

```shell
oc expose svc kuberhealthy
curl $(oc -n kuberhealthy get route kuberhealthy -o jsonpath='{.spec.host}')/metrics
oc delete route kuberhealthy
```

You can just as easily go in localy to the pod and curl localhost, expose the service with port-forward go in to prometheus and look and I'm sure there is many more.

### Grafana

So all this data but no dashboard, lets fix it.
I assume that you have followed my instructions on how to setup prometheus or something
similar and you have a grafana instance up and running.

You can be lazy and login to the instance and copy the grafana dashboard
that you will find under deploy/grafana/dashboard.json in the kuberhealthy repo.
Don't do that, we do everything as code :=)

```oc apply -f prometheus/grafana/grafana-dasboard-kuberhealthy.yaml```
