import socket
import sys
import time

# creating socket and accpeting user input hostname


socket_server = socket.socket()
server_host = socket.gethostbyname()
ip = socket.gethostbyname(server_host)
sport = 8080

# Connecting to server

print('This is your IP address: ', ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name: ')

socket_server.connect((server_host, sport))

# receiving packets / messages from server


socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
