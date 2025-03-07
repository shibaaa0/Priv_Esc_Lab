import os
import socket
import pty
import pwd

USERNAME = "ptit"
HOST = "0.0.0.0"
PORT = 1234
SCRIPT_PATH = "/home/ptit.sh"

def setup_system():
    if os.system(f"id {USERNAME} >/dev/null 2>&1") != 0:
        os.system(f"sudo useradd -m -s /bin/bash {USERNAME} && sudo passwd -d {USERNAME}")
    
    with open("temp.sh", "w") as f:
        f.write("#!/bin/bash\necho 'Hack me,please'\n")
    os.system(f"sudo mv temp.sh {SCRIPT_PATH} && sudo chmod 777 {SCRIPT_PATH}")
 
def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Server is running {HOST}:{PORT}")
    
    while True:
        client, addr = s.accept()
        print(f"Kết nối từ {addr}")
        
        pid, fd = pty.fork()
        if pid == 0:
            s.close()
            os.setuid(pwd.getpwnam(USERNAME).pw_uid)  
            os.execl("/bin/bash", "bash")
        else:
            while True:
                try:
                    data = client.recv(1024)
                    if not data: break
                    os.write(fd, data)
                    client.send(os.read(fd, 1024))
                except:
                    break
            client.close()
            print(f"Đóng kết nối từ {addr}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Cần quyền sudo!")
        exit(1)
    setup_system()
    start_server()
