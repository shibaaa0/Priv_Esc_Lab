FROM --platform=linux/amd64 fedora:24

RUN dnf -y install cronie && dnf clean all \
 && useradd -m user \
 && echo -e '#!/bin/sh\necho $(date) >> /var/log/check.log' > /tmp/check.sh \
 && chmod 777 /tmp/check.sh \
 && echo '* * * * * root /tmp/check.sh' >> /etc/crontab

WORKDIR /home/user
ENTRYPOINT ["/bin/bash","-c","/usr/sbin/crond -n & exec su - user"]
