FROM debian:bullseye-slim

RUN apt update && apt install -y sudo passwd

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]
