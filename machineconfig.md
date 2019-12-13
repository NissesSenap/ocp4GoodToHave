# Machineconfig

Since ignite is rather limited you might want to perfrom some changes to the local config on the node.

For example add another ssh key
This will trigger a restart of your machinesets that match the machineconfig.

## So much machineconfig

Generate a ssh-key that you want to use. In my case $HOME/.ssh/node.id_rsa.pub

### What machineconfigs exists

oc get machineconfig -n openshift-machine-api

## Add ssh config

oc patch machineconfig 99-worker-ssh --type=json --patch="[{\"op\":\"add\", \"path\":\"/spec/config/passwd/users/0/sshAuthorizedKeys/-\", \"value\":\"$(cat $HOME/.ssh/node.id_rsa.pub)\"}]"

This will create a rendered-worker machineconfig and you should see it when performing get machineconfig

### Which machineconfig we are running on and status

Use:

oc get machineconfigpool

Updated should become True when all your machinesets that match worker have been updated.
Last time i did this we saw a number of errors, this was due to that we tainted our infra nodes.

To workaround this issue you need to allow a number of operators to go to the node, like the machineconfig operator. In our case we put the taint on the daemon set.

More can be read about it in the [bugzilla](https://bugzilla.redhat.com/show_bug.cgi?id=1780318)
