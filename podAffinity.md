# Pod Affinity & Anti-affinity

In some use cases it's good to have the same pods on the same nodes.
To make the apps as fast as possible, for example in the case of a redis cache to a web server.

## Create ns and apps

```bash
oc new-project scheduler
oc new-app openshift/hello-openshift:v3.10 --name=cache     -n scheduler
oc new-app openshift/hello-openshift:v3.10 --name=webserver -n scheduler
```

## Add AntiAffinity to cache

Lets make sure our app dosen't get schedueld on the same server

```oc edit dc cache```

```yaml
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - cache
              topologyKey: kubernetes.io/hostname
      containers:
```

## Add Affinity to webserver

Put webserver on the same server as the cache.
But not all of the web servers on the same node.

```oc edit dc webserver```

```yaml
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - cache
            topologyKey: kubernetes.io/hostname
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - webserver
              topologyKey: kubernetes.io/hostname
            weight: 100
      containers:
```
