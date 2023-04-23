import socket
import threading
HEADERSIZE = 50

#TODO integrate bot.py with client.py
#Make the bot a client, the bot connects to the server as a client
#and sends messages to the server who broadcasts the message to
#all the other connections

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
print("Client launched")
server_socket.connect((hostname,8888))
print("Connected")

#server_socket.send(bytes('test','ascii'))

NICKNAME = input('choose a nickname: ')

def recieve():
    while True:
        try:
            message = server_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                server_socket.send(NICKNAME.encode('ascii'))
            else:
                print(message)
        except:
            print("error occurred!")
            server_socket.close()
            break;

def write():
    while True:
        message = f'{NICKNAME}: {input("")}'
        server_socket.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()