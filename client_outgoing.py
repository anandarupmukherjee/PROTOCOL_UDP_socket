import socket

# define the IP address and port number of the remote machine
IP_ADDRESS = '192.168.1.100'
PORT = 12345

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the remote machine
client_socket.connect((IP_ADDRESS, PORT))

# send a message to the remote machine
message = 'Hello, world!'
client_socket.send(message.encode())

# send values to the remote machine
values = [1, 2, 3, 4, 5]
for value in values:
    client_socket.send(str(value).encode())

# close the socket connection
client_socket.close()
