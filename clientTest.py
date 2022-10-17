import socket

def run_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('192.168.170.154', 8080))
	client.sendall('I am CLIENT\n'.encode())
	from_server = client.recv(4096)
	client.close()
	print(from_server)

if __name__ == '__main__':
	run_client()
