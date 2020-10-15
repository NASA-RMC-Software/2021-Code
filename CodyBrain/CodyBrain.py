import socket
HOST = '192.168.1.132' # Cody IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client port aka laptop
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#managing error exception
try:
	s.bind((HOST, PORT))
	except
	print 'Bind failed '

	s.listen(5)
	print 'Socket awaiting messages'
	(conn, addr) = s.accept()
	print 'Connected'

# awaiting for message
while True:
	data = conn.recv(1024)
	print 'I sent a message back in response to: ' + data
	reply = ''

	# Testing Connection
	if data == 'Ping':
		reply = 'Pong'
    elif data == 'Motor On'
        reply = 'Motor is On'
        #Do motor stuff
    elif data == 'Servo On'
        reply = 'Servo is On'
        #Do servo stuff
    elif data == 'LA On'
        reply = 'LA is On'
        #Do linear actuator stuff
	#and so on and on until...
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	# Sending reply
	conn.send(reply)
	conn.close() # Close connections