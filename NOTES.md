# Notes

The recomendation in the docs is to use dpeloyment instead of deploymentconfig (dc).

[ODO](https://github.com/openshift/odo) already does this, oc new-app ... dosen't. Probably won't change maybe ocp5...

## StatefulSet

Is a normal kind in k8s.

https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/

https://blog.openshift.com/kubernetes-statefulset-in-action/

Each pod get there own PVC that is directed to a PV.
In the application layer you have to set up the replication betwenn the different pods to share the data.
