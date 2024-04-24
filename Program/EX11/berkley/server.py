import socket
import time

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Server started and listening on port:', PORT)

while True:
    conn, addr = server_socket.accept()
    print('Connected by', addr)

    # Receive timestamp from client
    data = conn.recv(1024).decode()
    client_timestamp = float(data)

    # Get server timestamp
    server_timestamp = time.time()

    # Calculate round trip time (RTT)
    rtt = (server_timestamp - client_timestamp) / 2

    # Send server timestamp and RTT
    response = str(server_timestamp) + ',' + str(rtt)
    conn.sendall(response.encode())

    conn.close()

server_socket.close()
