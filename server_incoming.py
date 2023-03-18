import socket

HOST = 'localhost'  # The hostname or IP address of the server
PORT = 1234        # The port used by the server

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(f'Listening on {HOST}:{PORT}')
    # Accept incoming connection
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        # Receive and process incoming messages
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f'Received message: {message}')
