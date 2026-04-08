import socket
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on port {PORT}...")

while True:
    conn, addr = server_socket.accept()
    print('Connected by', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            print("Connection closed by client.")
            break

        message = data.decode()
        print("Received:", message)

        # رد تلقائي بدل input
        reply = f"Server received: {message}"
        conn.sendall(reply.encode())

    conn.close()