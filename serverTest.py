import socket

def run_server():
	# Add TCP/IP to the endpoint
	serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Assigns a port for the server that listens to clients connecting to this port
	serv.bind(('0.0.0.0', 8080))
	serv.listen(5)
	while True:
		conn, addr = serv.accept()
		from_client = ''
		while True:
			data = conn.recv(4096)
			if not data: break
			from_client += data.decode('utf_8')
			print(from_client)
			conn.send('I am SERVER\n'.encode())
		conn.close()
		print('client disconnected')

if __name__ == '__main__':
	run_server()
