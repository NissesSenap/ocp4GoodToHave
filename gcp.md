# GCP stuff

## Auth

```shell
# login
gcloud auth login
# List your current account
gcloud auth list
# List your config
gcloud config list
# Set your default project
gcloud config set project project1
```

## GKE

GKE specific stuff

### describe clusters

This command gives an overview of all settings that you have on your cluster.

```shell
gcloud beta container clusters describe --region europe-west1 cluster-example
```
