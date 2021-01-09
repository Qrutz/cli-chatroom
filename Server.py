import socket
import sys
import time

# creating socket and retrieving hostname

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080


# binding the host and port

new_socket.bind((host_name, port))
print("Binding succesfull!")
print("Your IP is ", s_ip)

# listen for connections

name = input("Enter your name: ")
new_socket.listen(1)

# accepting incoming connections

conn, add = new_socket.accept()
print("Received connection from ", add[0])
print("Connection Established, Connecting from: ", add[0])

# storing incoming connection data

client = (conn.recv(1024)).decode()
print(client + " has connected. ")
conn.send(name.encode())


# delivering packets and messages

while True:
    message = input("Me : ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)
