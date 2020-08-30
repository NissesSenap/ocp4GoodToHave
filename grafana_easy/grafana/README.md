# Grafana

This repo have more or less been completley taken [from](https://github.com/kborup-redhat/grafana-openshift).

He in turn have taken most of it from the official grafana [operator](https://github.com/integr8ly/grafana-operator)

## Upgrade Grafana operator

So if you want the latest version of Gafana operator go to [https://github.com/integr8ly/grafana-operator](https://github.com/integr8ly/grafana-operator)
and grab the latest config.

Copy those changes in to: charts/grafana-operator

There might be some minor changes that needs to be done but thats the gist of it.

## Reasons for not using OLM

At the time writing this document the Grafana operator version avaliable at OLM/operatorhub.io is ancient.
Due to that we need a few new features to be able to talk to Thanos we need to manage the Grafana operator our self.

This might change in the future, keep your self update on [https://operatorhub.io](https://operatorhub.io).

## Getting the values needed

As you can see in values.yaml we need two values to be able to use this chart.

openshift_prometheus_htpasswd_auth:
openshift_prometheus_basic_auth_pass:

These values can be gotten by perfroming the following:

*NOTE THE SED MAC USERS*, I don't have a mac so I can't test this but I know that mac got some differences from linux when it comes to sed.

```yaml
# openshift_prometheus_basic_auth_pass=$GRAFANA_DATASOURCE_PASSWORD
export GRAFANA_DATASOURCE_PASSWORD=$(oc get secret grafana-datasources -n openshift-monitoring -o jsonpath='{.data.prometheus\.yaml}' | base64 --decode | jq .datasources[0].basicAuthPassword | sed 's/"//g' )
echo $GRAFANA_DATASOURCE_PASSWORD

# openshift_prometheus_htpasswd_auth=$PROMETHEUS_HTPASSWD_AUTH
export PROMETHEUS_HTPASSWD_AUTH=$(oc get secret prometheus-k8s-htpasswd -n openshift-monitoring -o jsonpath='{.data.auth}')
echo $PROMETHEUS_HTPASSWD_AUTH
```

The reason why we can't hard code them for each cluster is that they get generated for every new cluster.
