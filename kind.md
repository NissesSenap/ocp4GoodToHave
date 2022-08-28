# Kind on fedora

Recently there is some changed in firewalld that creates issues with [kind](https://kind.sigs.k8s.io/docs/user/known-issues/#fedora).

## Grafana-operator

For my own shitty memory.

To run the grafana-operator I have started to use a [ingress](https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx).

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

Update deploy/examples/Grafana.yaml to set spec.client.preferService: false

```shell
yq -i '.spec.client.preferService = false' deploy/examples/Grafana.yaml
```
