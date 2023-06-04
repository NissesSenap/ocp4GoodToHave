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

## Security professional

```shell
# create vm with apache2
gcloud compute instances create us-web-vm \
--machine-type=e2-micro \
--zone=us-east1-b \
--network=default \
--subnet=default \
--tags=http-server \
--metadata=startup-script='#! /bin/bash
 apt-get update
 apt-get install apache2 -y
 echo "Page served from: US-EAST1" | \
 tee /var/www/html/index.html
 systemctl restart apache2'
# get the ip address of a vm
export EUROPE_WEB_IP=$(gcloud compute instances describe europe-web-vm --zone=europe-west2-a --format="value(networkInterfaces.networkIP)")
# create private dn
gcloud dns managed-zones create example --description=test --dns-name=example.com --networks=default --visibility=private
# dns route policy
gcloud dns record-sets create geo.example.com \
--ttl=5 --type=A --zone=example \
--routing-policy-type=GEO \
--routing-policy-data="us-east1=$US_WEB_IP;europe-west2=$EUROPE_WEB_IP"
# List dns routes
gcloud dns record-sets list --zone=example
# firewall http opening, don't use
gcloud compute --project=project1 firewall-rules create allow-http-web-server --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=web-server
```

### Hybrid network

In this task you create VPN tunnels between the two gateways. For HA VPN setup, you add two tunnels from each gateway to the remote setup. You create a tunnel on interface0 and connect to interface0 on the remote gateway. Next, you create another tunnel on interface1 and connect to interface1 on the remote gateway.

When you run HA VPN tunnels between two Google Cloud VPCs, you need to make sure that the tunnel on interface0 is connected to interface0 on the remote VPN gateway. Similarly, the tunnel on interface1 must be connected to interface1 on the remote VPN gateway.

> Note: In your own environment, if you run HA VPN to a remote VPN gateway on-premises for a customer, you can connect in one of the following ways:
Two on-premises VPN gateway devices: Each of the tunnels from each interface on the Cloud VPN gateway must be connected to its own peer gateway.
A single on-premises VPN gateway device with two interfaces: Each of the tunnels from each interface on the Cloud VPN gateway must be connected to its own interface on the peer gateway.
A single on-premises VPN gateway device with a single interface: Both of the tunnels from each interface on the Cloud VPN gateway must be connected to the same interface on the peer gateway.
