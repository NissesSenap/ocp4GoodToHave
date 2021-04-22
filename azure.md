# Azure

I'm doing a OCP 4.3 IPI install on Azure.
In this file I will post a bunch of az commands, hopefull I will have time to convert some of these tasks in to code as well.

## My account

### Login

az login

Starts a external browser where you login.

### Active account

az account show

Shows the account that you are currently logged in as.

### List accounts

az account list --refresh

### Change account

az account set -s <id>

## OCP pre-req

My version of the [re-req](https://docs.openshift.com/container-platform/4.3/installing/installing_azure/installing-azure-account.html) documentation.

### quota limits

You have to increase your quota!

https://docs.openshift.com/container-platform/4.3/installing/installing_azure/installing-azure-account.html#installation-azure-limits_installing-azure-account

https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits

Pain in the ass "helping" users not to increase there billing to much.

### Get id & tenantId

To be able to perfrom a IPI install you need to record the id & tenantId

You can do:

az account show

Or show my non existing jq skills and do:

export ID=$(az account show |jq .id)

export tenatID=$(az account show |jq .tenantId)

### Create Service Principal SP

Aka service account

az ad sp create-for-rbac --role Contributor --name ocpIPI

Write down the output somewhere

#### List SP

List the specific SP that you just created, this won't show you the password

az ad sp list --display-name ocpIPI

### Grant aditional access for SP

```shell
# Get appId
export appId=$(az ad sp list --display-name ocpIPI |jq '.[0].appId' -r)

az role assignment create --role "User Access Administrator" \
    --assignee-object-id $(az ad sp list --filter "appId eq '$appId'" \
       | jq '.[0].objectId' -r)

az ad app permission add --id $appId \
     --api 00000002-0000-0000-c000-000000000000 \
     --api-permissions 824c81eb-e3f8-4ee6-8f6d-de7f50d565b7=Role

az ad app permission grant --id $appId \
     --api 00000002-0000-0000-c000-000000000000
```

### Strange regions

If you are running your deployment in a region where you normally don't have access.
You might need to perfrom the following command to get access to public ip.
Don't ask me why, i don't know :D

az provider register --subscription <subscription-id> -n Microsoft.Network

or

az provider register --subscription $ID -n Microsoft.Network

## OCP quick install

```shell
mkdir ipi

openshift-install create cluster --dir=ipi \
    --log-level=debug

```

From another terminal

```shell
# azure subscription id:
az account show |jq .id -r

# tenant id
az account show |jq .tenantId -r

# appId
az ad sp list --display-name ocpIPI |jq '.[0].appId' -r

# secret
Something that you wrote down when you created the SP :)
```

## OCP custom install

This is probably the thing that you will do most of the [time.](https://docs.openshift.com/container-platform/4.4/installing/installing_azure/installing-azure-customizations.html#installing-azure-customizations)
Here you can find a list of all azure [regions](https://azure.microsoft.com/en-us/global-infrastructure/locations/)

When writing this document it's a DSv3 vCPU that you should ask access [for](https://docs.microsoft.com/en-us/azure/virtual-machines/dv3-dsv3-series)

```shell
mkdir ipi_custom

./openshift-install create install-config --dir=ipi_custom

# Perfrom your changes before running the following command
./openshift-install create cluster --dir=ipi_custom \
    --log-level=debug

```

## Setup Azure AD login

https://www.arctiq.ca/our-blog/2020/1/30/ocp4-auth-with-azure-ad/

Also read Samúel Jón Gunnarsson dm on k8s-slack.

## Azure File Storage

If you want to be able to do ReadWriteMany you need to create a new SC with Azure Files share
Orig docs can be found here: https://docs.microsoft.com/en-us/azure/aks/azure-files-volume

```shell
# Change these four parameters as needed for your own environment
export AKS_PERS_STORAGE_ACCOUNT_NAME=mystorageaccount$RANDOM
export AKS_PERS_RESOURCE_GROUP=myOCPShare
export AKS_PERS_LOCATION=norwaywest
export AKS_PERS_SHARE_NAME=ocpshare

# Create a resource group
az group create --name $AKS_PERS_RESOURCE_GROUP --location $AKS_PERS_LOCATION

# Create a storage account
az storage account create -n $AKS_PERS_STORAGE_ACCOUNT_NAME -g $AKS_PERS_RESOURCE_GROUP -l $AKS_PERS_LOCATION --sku Standard_LRS

# Export the connection string as an environment variable, this is used when creating the Azure file share
export AZURE_STORAGE_CONNECTION_STRING=$(az storage account show-connection-string -n $AKS_PERS_STORAGE_ACCOUNT_NAME -g $AKS_PERS_RESOURCE_GROUP -o tsv)

# Create the file share
az storage share create -n $AKS_PERS_SHARE_NAME --connection-string $AZURE_STORAGE_CONNECTION_STRING

# Get storage account key
STORAGE_KEY=$(az storage account keys list --resource-group $AKS_PERS_RESOURCE_GROUP --account-name $AKS_PERS_STORAGE_ACCOUNT_NAME --query "[0].value" -o tsv)

# Echo storage account name and key
echo Storage account name: $AKS_PERS_STORAGE_ACCOUNT_NAME
echo Storage account key: $STORAGE_KEY
```

Create secret
```shell
kubectl create secret generic azure-secret --from-literal=azurestorageaccountname=$AKS_PERS_STORAGE_ACCOUNT_NAME --from-literal=azurestorageaccountkey=$STORAGE_KEY
```

### Create the PV

```yaml
apiVersion: "v1"
kind: "PersistentVolume"
metadata:
  name: "pv0001"
spec:
  capacity:
    storage: "5Gi"
  accessModes:
    - "ReadWriteMany"
  storageClassName: azurefile
  azureFile:
    secretName: azure-secret
    shareName: ocpshare
    readOnly: false
  mountOptions:
  - dir_mode=0777
  - file_mode=0777
```

### Create PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: rstudio-pvc
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: azurefile
  resources:
    requests:
      storage: 5Gi
```

## AZ commands

### resource update

Force Azure to look for resources it has. Can be good if you can see vm:s in VMSS but not in kubernetes.
This will tell AKS to check over it's resources.

az resource update --id /subscriptions/your-sub-id/resourceGroups/rg-dev-we-aks/providers/Microsoft.ContainerService/managedClusters/aks-dev-we-aks1

To get the string it's easiest to go in to the azure portal under AKS to the cluster you want to force and update on and look at the URI.
