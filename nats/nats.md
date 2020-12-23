# Nats

Nats is a CNCF pub/sub project, they are currently not avaliable as a operator on OLM/operatorhub.io but hopefully that will change soon.

In the mean time i have written down my own getting started.

## Installing nats on k8s

The current installation files wants you to use default namespace. Sadly that isn't something that works in the long run so I just wget them and edit them.
If you don't feel like it you can use mine.
Of course I don't promise to keep these updated in any way, it's always best to look directly at the [operator repo](https://github.com/nats-io/nats-operator).

```shell
wget https://github.com/nats-io/nats-operator/releases/latest/download/00-prereqs.yaml
wget https://github.com/nats-io/nats-operator/releases/latest/download/10-deployment.yaml
```

### Install pre-req

```shell
oc new-project nats
oc apply -f 00-prereqs.yaml
oc apply -f 10-deployment.yaml
```

### Install nats cluster

```shell
cat <<EOF | kubectl apply -f -
apiVersion: nats.io/v1alpha2
kind: NatsCluster
metadata:
  name: example-nats-cluster
spec:
  extraRoutes:
  - cluster: nats-v2-0
  pod:
    enableConfigReload: true
    resources:
      limits:
        cpu: 200m
        memory: 500Mi
      requests:
        cpu: 100m
        memory: 100Mi
  size: 3
  version: 2.0.0
EOF
```

### External connection

For those of us that run OCP 4.4 on-prem we are running a rather old haproxy and I don't have any cool LB avaliable.
To workaround this I create a nodePort using my haproxy LB to point to the correct nodePort and make sure that it's get forwarded easily.

To do the expose do:

```oc expose pod example-nats-cluster-1 --type=NodePort```

One of the problems with this is that we can't point on a deployment instead, we have to point to a pod.

I will do some more research and see how I can configure the service with the operator instead.
Think to check if your firewall is open if you hit any issues.

## Verification

Better explained [at](https://docs.nats.io/nats-server/clients#if-you-have-go-installed) you can ether download the binaries or you can do it using go.

go get github.com/nats-io/go-nats-examples/

cd go-nats-examples/tools/nats-pub

### Subscribe msg

```go run nats-sub.go -s nats://<your-domain>:<your-port> hej```

### Publish msg

```go run nats-pub.go -s nats://<your-domain>:<your-port> hej msg2```
