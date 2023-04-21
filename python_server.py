import socket

HEADERSIZE = 50

def run_server():
	# CREDIT: https://gist.github.com/lichard49/abbe8b6877b259da128682db0a81a13e
	# data settings
	data_size = 16 # sending 16 bytes = 128 bits (binary touch states, for example)

	# server settings
	server_name = socket.gethostname()
	#str([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]) # https://stackoverflow.com/a/1267524
	server_port = 8888
	server_address = (server_name, server_port)

	# start up server
	print('SERVER: Setting up server on:', server_address)
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(server_address)
	server_socket.listen(1)

	# wait for connection
	print('SERVER: Waiting for a client connection...')
	connection, client_address = server_socket.accept()
	print('SERVER: Connected to:', client_address)


	

	# data formatting
	def data2binary(data):
		return ' '.join([format(ord(i), 'b').zfill(8) for i in data])

	# listen for data for forever
	#while True:
		data = connection.recv(data_size)
		#connection.send("a")

		print('SERVER: Received', data) # print as raw bytes
		#print 'Received', data2binary(data) # print in binary

		# process data


