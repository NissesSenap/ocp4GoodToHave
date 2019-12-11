# Tekton

Download your tkn cli

oc new-project c0e7-tekton

oc create serviceaccount tekton

oc policy add-role-to-user edit -z tekton -n c0e7-tekton

oc apply -f build.yml

tkn pipeline start openshift-tasks-pipeline
