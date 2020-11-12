import socket

HOST = '10.10.16.214' # Enter IP of Cody
PORT = 12345 # Pick an open Port (1000+ recommended), must match the Cody port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = input('Enter your command: ')
	mes = bytes(command, 'utf-8')
	s.send(mes)
	reply = s.recv(1024)
	if reply == 'Terminating':
		break
	print(reply)