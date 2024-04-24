import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))

    while True:
        cmd = input("Enter TIME to get server time, or EXIT to quit: ").upper()
        s.send(cmd.encode())
        if cmd == 'EXIT':
            break
        elif cmd == 'TIME':
            server_time = float(s.recv(1024).decode())
            print(f"Server time: {server_time}")

    s.close()

if __name__ == "__main__":
    client()
