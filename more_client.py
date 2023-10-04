import socket
import tkinter as tk
host = "127.0.0.1"
port = 2050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
while True:
    request = str(input(": "))
    client_socket.send(request.encode())
