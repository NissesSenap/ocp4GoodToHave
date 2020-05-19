# Monitoring

These instructions assume that you are running OCP 4.3 this will probably apply in OCP 4.4 as well but who knows...
The initial configmap will probably have new config variabels.

## Using built in prometheus for application checks

Who want's to take care of your own prometheus setup? I know i don't so lets use the built in one.
In OCP 4.3 this is a tech preview and I don't know what this do to your support of your cluster.
If you have conserns about that reach out to RedHat to get clarity. My guess is that the cluster will be supported but
not this feature.

For official [documentation](https://docs.openshift.com/container-platform/4.3/monitoring/monitoring-your-own-services.html)

```shell
# Check the current config, might be dumb to overwrite it ^^
oc get -n openshift-monitoring cm cluster-monitoring-config -o yaml

# Apply config if it looks okay
oc apply -f cluster-monitoring-config.yaml
```

This will start an operator in the openshift-user-workload-monitoring namespace + two prometheus instances.
I have no idea how to scale these if it's even possible in the techpreview
and it's not documented due to it's current status.

```oc get pods -n openshift-user-workload-monitoring```

Now you are ready to monitor your own services.

### RBAC to edit prometheus

If you want to enable your developers to be able to setup there own monitoring perform

oc apply -f rbac-mon.yaml

### Exampel app

Verify that your monitoring works, deploy a app in namepsace ns1 and create a scarper for it.

```shell
oc apply -f random_prom.yaml
oc apply -f service-monitor.yaml
```

Go in to the GUI enter developer mode -> advanced -> metrics -> pick ns1 as project

In the prometheus query search for:

http_requests_total{job="prometheus-example-app",code="200",method="get"}

The graf is more fun if you hit the url a few times

```shell
# Expose the app
oc expose svc prometheus-example-app

# Hit the endpoint
curl $(oc get route prometheus-example-app -o jsonpath='{.spec.host}')

# Show the metrics
curl $(oc get route prometheus-example-app -o jsonpath='{.spec.host}')/metrics
```

## Grafana

First of all big cred to [C Hatmarch](https://github.com/hatmarch/cdc-and-debezium-demo) for explaning this.
When it comes to Grafna I have stolen everything from him more or less.

So prometheus is a gret tool but it's not built to show data in a nice way, in enters grafana.
Currently we can't use the built in grafana for this and my guess is that it will take a long time for that to happen.

Sadly our built in prometheus have rather limited configuration possabilities so we can't expose the prometheus
to listen to any other port then 127.0.0.1.

To workaround this we will use the Thanos querier, Thanos expose data between multiple prometheus instances and
makes it possible to just use one grafana to monitor multiple clusters.

There is an operator in operatorhub.io/olm maintained by RedHat but it's kind of an old version and to be able to
use Thanos we need a newer version.

### Install Grafana operator

Clone the upstream

```shell
git clone https://github.com/integr8ly/grafana-operator.git
cd grafana-operator
# I tested with this revision and I know it works.
# My recomendation is that you use master and adapt to the correct file names.
git checkout e7b281959853a1857fefcb710d6d1fef483f15c0
```

#### Install the operator

Assuming that you are in the grafana-operator repo

```shell
export PROJECT_NAME="grafana"
oc new-project $PROJECT_NAME

oc create -f deploy/crds
oc create -f deploy/roles -n ${PROJECT_NAME}
oc create -f deploy/cluster_roles
oc create -f deploy/operator.yaml -n ${PROJECT_NAME}
# Verify that the operator is up and running
```

### Setup a grafana instance

Time to jump back to my repo

```shell
export PROJECT_NAME="grafana"
export ADMIN_PASSWORD="superHardPassword"
# create an instance of grafana
oc process -f prometheus/grafana/grafana-instance-template.yaml PROJECT_NAME="${PROJECT_NAME}" \
    ADMIN_PASSWORD="${ADMIN_PASSWORD}" -o yaml | oc apply -f -

# grant cluster-monitoring-view to the service account that the operator created
oc adm policy add-cluster-role-to-user cluster-monitoring-view -z grafana-serviceaccount

# Create a tenant based datasource (using kube_rbac_proxy) to query openshift-monitoring
# NOTE: This will also create the configmap to mirror the GrafanaDataSource CR
oc process -f prometheus/grafana/openshift-metrics-datasource-template.yaml \
    PROJECT_NAME="${PROJECT_NAME}" DATASOURCE_NAME=prometheus TOKEN=$(oc serviceaccounts get-token grafana-serviceaccount) | oc apply -f -
```

Now you will have a Grafna using thanos-querier as your default data source.
It enabels us to get data from both the internal prometheus instance and the one for our own apps.

Now all you need to do is to set up a grafanadashboards crd or do it manually inside your grafna instance.
How to do that is something that i won't cover here. But i recomend checking out the kuberhealthy part of this repo.
