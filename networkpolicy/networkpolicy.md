# Network policy

A good way to increase your secuirty is to set a networkpolicy that denys all communication then whitelist the things that you need.

For more exampels check out: https://github.com/ahmetb/kubernetes-network-policy-recipes

## Base template for projects/ns

Set up a base template that will get applied to all projects/namespaces that you have.

Do the following...

## Allow communication between specific ns and pods

Lets set up a basic use case. Communicate between two pods in two seperate namespaces, for example a backend to a database.

Create two namespaces:

```yaml
oc new-project DATABASE_NAMESPACE
oc new-project BACKEND_NAMESPACE
```

Read through [backend_to_db.yml](backend_to_db.yml)

```oc create -f backend_to_db.yml```

Just as it sounds:

- "deny-by-default" will remove all communications between pods in a ns
- "allow-same-namespace" will allow communication between pods.
- "allow-backend-to-database" will allow a pod in the backend namespace to talk to the database service in the db namespace.

A general tip that i got when writing network policys is to make it as simple as possible.

Sure we could define on pod level in the back that should be able to talk to the db service but this will create so many networkpolicys. So i would recomend doing it on namepsace level.

To my knowladge there is currently no easy way to vizualice networkpolicy rules. If you do please create an issue/PR and provide that information :)
