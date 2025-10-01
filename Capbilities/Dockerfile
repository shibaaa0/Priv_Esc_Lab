FROM --platform=linux/amd64 fedora:24

RUN useradd -m user && setcap 'cap_dac_override+ep' /usr/bin/python3.5 

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
