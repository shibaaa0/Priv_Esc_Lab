# 🛡️ Privilege Escalation Labs

**Author:** shibaaa  

---

## 🎯 Mục tiêu
Mục tiêu của các bài lab này là **thực hành leo thang đặc quyền** nhằm đọc được một trong hai tệp sau:
- `/flag.txt`
- `/etc/shadow`

---

## 🛠️ Yêu cầu hệ thống
- **Docker**: Phiên bản mới nhất (có thể kiểm tra bằng `docker --version`)
- **Bash Shell** (Linux/MacOS) hoặc Git Bash/WSL (Windows)

---

## 🚀 Cách sử dụng
1. **Cài đặt Docker**  
   - Linux (Debian/Ubuntu):
     ```sh
     sudo apt update && sudo apt install docker.io -y
     ```
   - MacOS / Windows: [Tải Docker Desktop](https://www.docker.com/products/docker-desktop)

2. **Build và run lab**
    ```sh
    ./run.sh
    ```