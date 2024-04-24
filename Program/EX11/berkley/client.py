import socket
import time

HOST = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Get client timestamp before sending
client_timestamp = time.time()

# Send client timestamp
client_socket.sendall(str(client_timestamp).encode())

# Receive server response (server timestamp and RTT)
data = client_socket.recv(1024).decode()
server_timestamp, rtt = data.split(',')

# Convert server timestamp to float
server_timestamp = float(server_timestamp)

# Convert RTT to float before subtraction
rtt = float(rtt)

# Calculate estimated server time (offset)
estimated_server_time = server_timestamp - rtt

# Print estimated server time
print('Estimated server time:', estimated_server_time)

client_socket.close()
