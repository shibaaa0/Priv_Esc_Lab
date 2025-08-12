FROM --platform=linux/amd64 fedora:24

RUN useradd -m user && chmod u+s /usr/bin/find

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
