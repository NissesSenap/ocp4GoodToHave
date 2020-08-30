# Grafana easy

I have created this folder to make life easier.
It will never be updated and I would really recommend you using the [official grafana operator repo](https://github.com/integr8ly/grafana-operator/) instead.

Read through the instructions in [grafana/README.md](grafana/README.md) and update the values.yaml file

But this should do the job.

```bash
oc new-project grafana
oc apply -f grafana-operator
cd grafana
# Update the values.yaml
sleep 5 # Giving the operator some time to start
helm install grafana .
```
