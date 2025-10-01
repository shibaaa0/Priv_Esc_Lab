FROM --platform=linux/amd64 fedora:24

RUN useradd -m user && chmod u+s /usr/bin/date && echo "RAT{su1d_1s_v3ry_fun!!!}" >/flag.txt && chmod 400 /flag.txt

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
