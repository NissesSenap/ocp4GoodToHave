# Kafka

AMQ Streams or strimzi is nice

All the yaml is written without defning namespace, so jump in to the correct one before creating your stuff.
Except for namespace selectors in the monitoring section for example: [strimzi-pod-monitor.yaml](./monitoring/strimzi-pod-monitor.yaml).
I want to show an example on how to do this and It looks like a good idea :) I assume that you have a namespace=kafka in there.
Please change so it fites your needs.

Sorry about not writing a helm/kustomize for this instead.

Most of the exampls is take from [strimzi operator repo](https://github.com/strimzi/strimzi-kafka-operator/) or for random blogs and chat groups.

For a detailed explination on how Strimzi work with OCP [routes](https://strimzi.io/2019/04/30/accessing-kafka-part-3.html)

## Example files

Kafka-cluster.yaml contains the cluster specification.
Notice the metrics and listeners part

hello-world.yaml creates two apps that consums and prduces stuff on my-topic

## Kafka commands

### Jump in to a kafka host

oc exec -ti my-cluster-kafka-0 -- bash

or use rsh dosen't matter.

### Describe all topics

bin/kafka-topics.sh --zookeeper localhost:2181 --describe

### List all under-replicated partitions

bin/kafka-topics.sh --zookeeper localhost:2181 --describe --under-replicated-partitions

Hopefully this is empty.

### List unavailable partitions

bin/kafka-topics.sh --zookeeper localhost:2181 --describe --unavailable-partitions

Should also hopefully be empty

### List consumer groups

bin/kafka-consumer-groups.sh --bootstrap-server my-cluster-kafka-bootstrap:9092 --list

### Show consumer group details

bin/kafka-consumer-groups.sh --bootstrap-server my-cluster-kafka-bootstrap:9092 --describe --group my-hello-world-consumer

## Kafka externally

To be able to reach the environment externally you need to setup a few things and since it's alwas good test lets do it.

### Fix keystore and crt

#### Get crt

oc extract secret/my-cluster-cluster-ca-cert --keys=ca.crt --to=- > ca.crt

#### Create keystore

keytool -import -trustcacerts -alias root -file ca.crt -keystore keystore.jks -storepass password -noprompt

#### Verify keystore

keytool -list -v -keystore keystore.jks

### Verify topic externally using keystore

#### Download kafka

You will need a a bin or two from kafka on your client.

Download [kafka](https://kafka.apache.org/downloads)

#### Create client.properties

Take the ssl truestore location from where you create the keystore and same with passowrd.
In my example the password is password :)

```shell
cat client.properties
security.protocol=SSL
ssl.truststore.location=kafka.server.truststore.jks
ssl.truststore.password=XXX
```

#### Start consumer

In terminal 1

NOTE the :443

./kafka-console-consumer.sh --bootstrap-server my-cluster-kafka-bootstrap-kafka.apps.ocp67.ajco.se:443 --from-beginning --topic my-topic --consumer.config client.properties

And if you have something to produce towards this topic you will see something

### Verify topic through java app

Yes I know java :(

NOTE: You need to create a topic called my-topic

```shell
git clone https://github.com/hguerrero/amq-examples.git

cd camel-kafka-demo

oc extract secret/my-cluster-cluster-ca-cert --keys=ca.crt --to=- > src/main/resources/ca.crt

keytool -import -trustcacerts -alias root -file src/main/resources/ca.crt -keystore src/main/resources/keystore.jks -storepass password -noprompt

# To stat this app takes around 5 min due to the need to download half of all the mvn packages in the world.
mvn -Drun.jvmArguments="-Dbootstrap.server=`oc get routes my-cluster-kafka-bootstrap -o=jsonpath='{.status.ingress[0].host} {"\n"}'`:443" clean package spring-boot:run
```

You should now see messages being sent with the help of camel.

## Kafka Connect

Assuming that you want to use a [external connector](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_rhel/assembly-kafka-connect-str#ref-kafka-connect-distributed-connector-configuration-str)

then you can restart it independeitly instead of restarting the entire pod.

### Restart connector using API

Assuming that you rsh in to the connector pod

curl -i -X POST localhost:8083/connectors/<name>/restart

## Monitoring

Of course we should monitor our kafka [env:](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_openshift/assembly-deployment-configuration-str#assembly-kafka-exporter-configuration-deployment-configuration-kafka)

In your Kafka crd enable the kafka exporter as you can see in: [kafka-cluster.yaml](./kafka-cluster.yaml)

## Service-registry

Also called [schema-registry](https://access.redhat.com/documentation/en-us/red_hat_integration/2019-12/html/getting_started_with_service_registry/intro-to-the-registry)

### Install

[Official documentation](https://access.redhat.com/documentation/en-us/red_hat_integration/2019-12/html/getting_started_with_service_registry/installing-the-registry#installing-registry-kafka-kubernetes-storage)

```shell
# Downloda the OCP template or use the file in the repo
wget https://github.com/Apicurio/apicurio-registry/blob/1.0.x-redhat/distro/openshift-template/service-registry-template.yml

# Deploy the service-registry
oc new-app service-registry-template.yml -p KAFKA_BOOTSTRAP_SERVERS=my-cluster-kafka-bootstrap:9092 -p REGISTRY_ROUTE=my-cluster-service-registry-kafka.apps.ocp67.ajco.se
```

### Verfiy

```curl -i -k -X POST -H "Content-type: application/json; artifactType=AVRO" -H "X-Registry-ArtifactId: prices-value" --data '{"type":"record","name":"price","namespace":"com.redhat","fields":[{"name":"symbol","type":"string"},{"name":"price","type":"string"}]}' https://my-cluster-service-registry-kafka.apps.ocp67.ajco.se/artifacts```

## Conenct

To be able to add more features like s3 or jdbc to the kafkaConnect you need to add those jar files to the image.

You can download a bunch of open-source jars from confluent or write your own.
Download the jars manually and put in a random folder:

https://www.confluent.io/hub/confluentinc/kafka-connect-s3

https://www.confluent.io/hub/confluentinc/kafka-connect-jdbc

### Create a s2i build

You can defently do this in a easier way, but I have tried this and it works.

You can find the official documentation [here.](https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/using_amq_streams_on_openshift/getting-started-str#using-kafka-connect-with-plug-ins-str)

This since we need a number of custom apps

We will need to download a AMQ streams base image from registry.redhat.io and to do this we need to give our builder
SA (ServiceAccount) access to do so.
You should already have a secret like this from when setting up the AMQ [service registry](#service-registry).

In my case it's called: 11009103-kafka-serviceaccount2020-pull-secret

Edit the builder service account and add the secret name, it should look something like this:
oc edit sa builder

```yaml
apiVersion: v1
imagePullSecrets:
- name: builder-dockercfg-plm2x
kind: ServiceAccount
metadata:
  name: builder
  namespace: kafka
secrets:
- name: builder-token-4hzn4
- name: builder-dockercfg-plm2x
- name: 11009103-kafka-serviceaccount2020-pull-secret
```

Create a dockerfile and put in the base folder of your plugin files.

```Dockerfile
FROM registry.redhat.io/amq7/amq-streams-kafka-24-rhel7:1.4.0
USER root:root
COPY ./my-plugins/ /opt/kafka/plugins/
USER 1001
```

Your folder structure containing the jar files should look something like this.

```shell
tree ./my-plugins/
./my-plugins/
|__ Dockerfile
|
├── debezium-connector-mongodb
│   ├── bson-3.4.2.jar
│   ├── CHANGELOG.md
│   ├── CONTRIBUTE.md
│   ├── COPYRIGHT.txt
│   ├── debezium-connector-mongodb-0.7.1.jar
│   ├── debezium-core-0.7.1.jar
│   ├── LICENSE.txt
│   ├── mongodb-driver-3.4.2.jar
│   ├── mongodb-driver-core-3.4.2.jar
│   └── README.md
├── debezium-connector-mysql
│   ├── CHANGELOG.md
│   ├── CONTRIBUTE.md
│   ├── COPYRIGHT.txt
│   ├── debezium-connector-mysql-0.7.1.jar
│   ├── debezium-core-0.7.1.jar
│   ├── LICENSE.txt
│   ├── mysql-binlog-connector-java-0.13.0.jar
│   ├── mysql-connector-java-5.1.40.jar
│   ├── README.md
│   └── wkb-1.0.2.jar
```

Then you area ready to setup the build.

```shell
oc new-build --name=jdbc-amq-connect registry.redhat.io/amq7/amq-streams-kafka-24-rhel7:1.4.0 --binary=true

# The --from-dir should be the folder where you store the jar and Dockerfile.
oc start-build jdbc-amq-connect --from-dir=my-plugins --follow

oc new-app jdbc-amq-connect
```

#### S2i second path

The camel documentation explains how to use the s2i solution in a [better way](https://camel.apache.org/camel-kafka-connector/latest/try-it-out-on-openshift-with-strimzi.html)

The Camel project have recently created a bunch of kafka connectors that they already have.
Take a look at this [blog post](https://strimzi.io/blog/2020/05/07/camel-kafka-connectors/) for more info.

### Verfiy plugin list

rsh in to the connect pod and run:

```curl http://localhost:8083/connector-plugins```

This will give you a list of all the plugins

### Get schema definition

If you want to get the definition of what values you can put in the connector you can perfrom the following.

curl -X PUT -d "{}" localhost:8083/connector-plugins/JdbcSourceConnector/config/validate --header "connect-Type:application/json" |python -m json.tool

Notice the python part is only to make the output more readable.

## Connector

Just like we can use Strimzi CRD for connect we can also use it for connectors.

A connector is something that uses the connect to read the actual source data that you define.

You can read more about it [here.](https://strimzi.io/docs/latest/#kafkaconnector_resources)

## KSQLdb

Using the open-source version of confluent ksql.
The helm chart dosen't seem to work and I had to do changes to get ksql to start. I hopefully will document this later.

For now ignore this section.

### Deploy basic

helm install -n kafka ksql .
