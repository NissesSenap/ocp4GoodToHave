#!/usr/bin/env python

# A good to have script created by one of my co-workers, steeling with pride

import argparse
import json
import requests
import sys

parser = argparse.ArgumentParser(description='Backup Pod Creation Script.')
parser.add_argument("-t", "--token",
                    help="OpenShift Token", required=True)
parser.add_argument("-a", "--api", help="OpenShift API", required=True)
parser.add_argument("-lk", "--label-key", help="Label Key", required=True)
parser.add_argument("-lv", "--label-value", help="Label value", required=True)
parser.add_argument("-n", "--namespace", help="Namespace", required=True)
parser.add_argument("-p", "--pod_name", help="Pod Name", default="pv-backup")
args = parser.parse_args()

namespace = args.namespace
token = args.token
api = args.api
label_key = args.label_key
label_value = args.label_value
pod_name = args.pod_name


session = requests.Session()
session.verify = False
session.headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer {0}'.format(token),
}

namespace_pvc = session.get(
    "{0}/api/v1/namespaces/{1}/persistentvolumeclaims?labelSelector={2}%3D{3}".format(api, namespace, label_key, label_value))
namespace_pvc.raise_for_status()

if namespace_pvc.status_code != 200:
    print("Failed to query OpenShift API. Status code: {0}".format(
        namespace_pvc.status_code))
    sys.exit(1)

result_json = namespace_pvc.json()

pvc_names = [str(pvc['metadata']['name']) for pvc in result_json['items']]

pod = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": pod_name,
        "namespace": namespace,
        "annotations": {
            "backup.velero.io/backup-volumes": ",".join(pvc_names)
        },
        "labels": {
            label_key: label_value
        }
    },
    "spec": {
        "containers": [
            {
                "command": [
                    "/bin/bash",
                    "-c",
                    "while true; do sleep 10; done"
                ],
                "image": "registry.redhat.io/ubi7/ubi:latest",
                "imagePullPolicy": "IfNotPresent",
                "name": pod_name,
                "resources": {
                    "requests": {
                        "cpu": "200m",
                        "memory": "256Mi"
                    },
                    "limits": {
                        "cpu": "500m",
                        "memory": "512Mi"
                    }
                },
                "volumeMounts": []
            }
        ],
        "volumes": [],
        "restartPolicy": "Always"
    }
}

for pvc_name in pvc_names:
    pod['spec']['containers'][0]['volumeMounts'].append(
        {"name": pvc_name, "mountPath": "/tmp/{0}".format(pvc_name)})

    pod['spec']['volumes'].append(
        {"name": pvc_name, "persistentVolumeClaim": {"claimName": pvc_name}})

pod_create = session.post(
    url="{0}/api/v1/namespaces/{1}/pods".format(api, namespace), json=pod)

if pod_create.status_code != 201:
    print("Error Creating Pod. Status code: {0}".format(
        pod_create.status_code))
    sys.exit(1)

print("Pod Created. Name: {0}. Number of Volumes: {1}".format(
    pod_name, len(pvc_names)))
