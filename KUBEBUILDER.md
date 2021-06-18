# Getting started kubebuilder

Now a days etcd etcd is downloaded using the make file, you don't need to download it manually any more.

## With kind

If you are running kubebuilder with kind I recomend that you update the makefile.

Update the Makefile with the following info

Due to kind you can't use :latest

```Makefile
IMG ?= docker.io/flagger/tester:0.0.1

kind-load:
	kind load docker-image ${IMG}

```

The deployment manifest needs to be uppdated as well.
Edit: config/manager/manager.yaml

Add:

```yaml
        imagePullPolicy: IfNotPresent
```

I'm unsure if you need to define docker.io or not, it seems like kind used it by default but it should probably be solved
by setting the IfNotPresent.

It looks like the manager.yaml doesen't get updated unless you do some specific things.
It would probably be good to have a special kustomize patch command to use instead and call on it if you want to use the
kind style deployment so you don't destory the default way of deploying...

An excellent blog about kind and it's [load image](https://iximiuz.com/en/posts/kubernetes-kind-load-docker-image/)

