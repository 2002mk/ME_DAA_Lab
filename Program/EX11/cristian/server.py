import socket
import time

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen(1)
    print("Server is listening...")
    conn, addr = s.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024).decode()
        if data == 'TIME':
            conn.send(str(time.time()).encode())
        elif data == 'EXIT':
            break

    conn.close()
    print("Server closed")

if __name__ == "__main__":
    server()
