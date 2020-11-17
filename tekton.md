# Tekton

Using openshift-pipelines

## cli

### list pipelines

tkn pipeline ls

### list resources

tkn resource ls

### Start pipeline

tkn -n basic-spring-boot-build pipeline start basic-spring-boot-pipeline -r basic-spring-boot-git=basic-spring-boot-git -s tekton

### list pipelineruns

tkn pipelinerun ls

### delete pipelinerun

tkn pipelinerun delete python-example-pipeline-run-kpljl
