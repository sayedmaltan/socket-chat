import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 50000))
server_socket.listen()

print("Server listening on port 50000...")

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