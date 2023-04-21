from email.header import Header
import socket

HEADERSIZE = 50

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
print("Client launched")
server_socket.connect((hostname,8888))
print("Connected")
