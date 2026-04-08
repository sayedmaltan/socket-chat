# client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('41.36.230.132', 50000))

while True:
   
    message = input("Enter your message (type 'exit' to quit): ")

    if message.lower() == 'exit':
        print("Closing connection.")
        break  # ينهي الجلسة ويغلق الاتصال
    
    # يرسل الرسالة
    client_socket.sendall(message.encode())

    # يستقبل الرد من الخادم
    data = client_socket.recv(1024)
    print('Received from server:', data.decode())
    
client_socket.close()