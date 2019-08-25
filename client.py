#Sachinam Srivastava
from socket import *
from threading import *
client_socket=socket()
client_socket.connect(('127.0.0.1',1234))
def read():
	while(True):
		msg=client_socket.recv(50000).decode()
		print('Server : ',msg)
def write():
	while(True):
		client_socket.send(input().encode())
readThread=Thread(target=read)
writeThread=Thread(target=write)
readThread.start()
writeThread.start()
readThread.join()
writeThread.join()
client_socket.close()
