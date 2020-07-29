### Implements a simple HTTP/1.0 Server

# Imports the necessary "socket" module to implement the HTTP server.
import socket

# Defines the socket's address (IP) and port number (TCP)
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Creates a new socket object for the user/server and takes two arguments 
# which set the socket's protocols to IPv4 & TCP, respectively.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Sets options for the socket we just created. The 1st argument sets an option
# at the socket's API level. The 2nd argument allows the socket to bypass time
# delays that are set by defult. The 3rd argument
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Binds the address and port number to the socket, giving it the option to
# receive data.
server_socket.bind((SERVER_HOST, SERVER_PORT))
# Enables the server to accept connections (and now receive data). The
# argument specifies the number of unaccepted connections it'll allow before
# refusing new connections.
server_socket.listen(1)
# Let's the user know that this server is capable of accepting connections on
# a specific port.
print(f'Listening on port {str(SERVER_PORT)} ...')

while True:
	# Accepts a new connection from a client. This returns the (conn, address)
	# value pair which are a new socket object & address for the client and
	# assigns them each to a different variable.
	client_connection, client_address = server_socket.accept()

	# Receives the data from the client's socket in the form of a bytes-like
	# object, decodes it as a string, assigns it to a variable, and prints it.
	# The argument for the socket object method .recv() specifies the maximum
	# amount of data to be received at once.
	request = client_connection.recv(1024).decode()
	print(request)

	# Splits the client's HTTP request into a list of values.
	headers = request.split('\n')
	# Splits the first value from the previous list (ie 'GET / HTTP/1.1' into
	# its own list, and assigns the second value from that new list (ie '/' to
	# the variable 'filename'. This is the page the client is requesting.
	filename = (headers[0].split())[1]

	# Check to see if the requested page is '/' (aka the root) or '/index' and
	# replaces that value with '/index.html' (aka the index). root == index
	if filename == '/' or filename == '/index':
		filename = '/index.html'

	try:
		# Returns an object representing the requested page's file and assigns
		# it to the variable 'fin'. The file contents are returned as a string
		# & assigned to the variable 'content'. Note: "with" opens and then
		# closes the file immediately to prevent data corruption.
		with open(f'htdocs{filename}') as fin:
			content = fin.read()
		# Assigns data to be sent to client to a variable.
		response = f'HTTP/1.0 200 OK\n\n{content}'
	# If the requested page does not exist in the server's directory, then a
	# '404 error' message is assigned to the variable instead.
	except FileNotFoundError:
		response = f'HTTP/1.0 404 NOT FOUND \n\nFile Not Found'
	# Encodes data from variable 'response' and sends it to the client.
	client_connection.sendall(response.encode())
	# Closes the connection to the client by marking its socket closed.
	client_connection.close()

# Closes the server my marking its socket closed.
server_socket.close()