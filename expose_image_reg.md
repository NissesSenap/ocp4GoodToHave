# Expose image registry

So what is the need for this?
To be honest i personally don't think you should.
Instead i would say that you should have an external registry like quay and you push **TO** it and not the other way around.
Using your CI/CD solution.

I can understand that you want your admins to do it from a debug point of view... Good and bad stuff as allways.

## Expose registry

```oc patch configs.imageregistry.operator.openshift.io/cluster --type=merge --patch '{"spec":{"defaultRoute":true}}'```

If you want a shorter image registry

```oc patch configs.imageregistry.operator.openshift.io/cluster --type=merge --patch '{"spec":{"routes":[{"name":"image-registry", "hostname":"image-registry.'$INGRESS_DOMAIN'"}]}}'```
