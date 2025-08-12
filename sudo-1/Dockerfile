FROM --platform=linux/amd64 fedora:24

RUN useradd -m user
RUN dnf install -y sudo && dnf clean all

COPY --chmod=555 hello /home/user/hello

RUN echo "user ALL=(root) NOPASSWD: /home/user/hello" > /etc/sudoers.d/python3-server \
    && chmod 440 /etc/sudoers.d/python3-server

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
