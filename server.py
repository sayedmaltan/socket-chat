# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 50000))
server_socket.listen()

print("Server listening on port 65432...")
conn, addr = server_socket.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("Connection closed by client.")
            break

        print("Received from client:", data.decode())

       
        reply = input("Enter your message : ")
        conn.sendall(reply.encode())
        