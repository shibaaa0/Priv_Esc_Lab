FROM --platform=linux/amd64 python:3.13.5-bookworm

RUN useradd -m user

COPY --chmod=755 app /home/user/app
COPY --chmod=4755 runner /home/user/runner
COPY --chmod=444 runner.c /home/user/runner.c

WORKDIR /home/user

USER user
ENTRYPOINT ["/bin/sh"]
