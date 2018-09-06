#Jyoti Singh
#Sachinam Srivastava
from socket import *
from threading import *
server_socket=socket()
server_socket.bind(('',1234))
server_socket.listen(50)
print('server started and waiting for connection.....')
client_socket,client_ip=server_socket.accept()
print('connection created with ip',client_ip)
def read():
	while(True):
		msg=client_socket.recv(50000).decode()
		print('Sachinam : ',msg)
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
server_socket.close()
