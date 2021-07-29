# kubernetes

This file will contain some kubernetes commands.
Most of them will be kept in [oc.md](oc.md).
Instead of writing `kubectl`everywhere I use a `alias k=kubectl`so in the docs you will see k in a bunch of places.
Instead of writing kubernetes i normally write k8s.


## Debug

### Debug pod

There are a few things i miss from OCP in kubernetes and this is among them. In OCP you can write `oc debug node/ip-10-0-141-105.ec2.internal`.
And it will start a debug pod on your node that can mount the root dir for you. This enables you to debug nodes without having to ssh in to them.

I k8s you can solve it this way.
> Notice the nodeSelector at the bottom of the yaml.

debug.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: debug
  namespace: default
spec:
  containers:
    - command:
        - /bin/sh
      resources:
        requests:
          memory: "16Mi"
          cpu: "10m"
        limits:
          memory: "64Mi"
          cpu: "100m"
      image: alpine:latest
      name: container-00
      securityContext:
        privileged: true
        runAsUser: 0
      tty: true
      volumeMounts:
        - mountPath: /host
          name: host
  volumes:
    - hostPath:
        path: /
        type: Directory
      name: host
  hostNetwork: true
  nodeSelector:
    kubernetes.io/hostname: your-host-name
```

And lets jump in to the host

```shell
k apply -f debug.yaml
k exec -it debug -n default -- /bin/sh
# To become root on the node from the pod:
chroot /host
```
