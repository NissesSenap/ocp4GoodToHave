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

### Change accounts

```shell
gcloud config configurations list
gcloud config configurations activate default
```

## GKE

GKE specific stuff

### Get login creds

```shell
gcloud container clusters get-credentials cluster-name --region europe-west1 --project project1
```

### describe clusters

This command gives an overview of all settings that you have on your cluster.

```shell
gcloud beta container clusters describe --region europe-west1 cluster-example
```
