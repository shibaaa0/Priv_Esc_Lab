#CVE-2023-22809
FROM --platform=linux/amd64 fedora:24

# cài sudo + editor, tạo user, đặt pass (tùy chọn) và cấp sudoedit NOPASSWD
RUN dnf -y install sudo vim && dnf clean all \
 && useradd -m -s /bin/bash user \
 && echo "user:password" | chpasswd \            
 && printf "user ALL=(ALL) NOPASSWD: sudoedit /home/user/test.txt\n" > /etc/sudoers.d/user \
 && chmod 440 /etc/sudoers.d/user \
 && touch /home/user/test.txt && chown user:user /home/user/test.txt

WORKDIR /home/user
USER user
ENTRYPOINT ["/bin/sh"]
