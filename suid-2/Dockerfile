FROM --platform=linux/amd64 fedora:24

RUN useradd -m user

COPY --chmod=4755 hello /home/user/hello
COPY --chmod=444 hello.c /home/user/hello.c

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
