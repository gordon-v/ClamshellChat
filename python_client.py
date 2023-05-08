import asyncio
import socket
import threading
import bot
import creds
#TODO integrate bot.py with client.py 
#Make the bot a client, the bot connects to the server as a client
#and sends messages to the server who broadcasts the message to
#all the other connections

def init_client(nickname):
    global server_socket
    global hostname
    global NICKNAME
    global recieve_thread

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = '127.0.0.1' #socket.gethostname()
    NICKNAME = str(nickname)

    print(f"'{NICKNAME}' Client launched")

    server_socket.connect((hostname,8888))

    print(f"'{NICKNAME}' Client Connected")

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

    recieve_thread = threading.Thread(target=recieve)
    #recieve_thread.start()
    # MOVED TO BOT.PY
   

def write(msg):
        message = f'client {NICKNAME}: {str(msg)}'
        #FIX
        server_socket.send(message.encode('ascii')) # FIX: THIS WILL BREAK IF NON ASCII CHARACTER IS SENT!

        #ovoj e the person who connects to server. moze da si izbere nickname. i discord bot se povrze na server.
        #i si izbere nickname automatically. like this. OK sg ke ti ga pokazu best part ke ga run server
        # i posle ke open up. java flipphone application. i oni ke connect. GLAD U ASKED