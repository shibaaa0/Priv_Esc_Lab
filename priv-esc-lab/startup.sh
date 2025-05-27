#!/bin/bash

useradd -m -s /bin/bash ctf
echo "ctf:ctf" | chpasswd

sudo chmod u+s /usr/bin/find

su - ctf
