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
	command = data.split(", ")

	#Running commands
	if command[0] == 'Mo': #Motor commands
		motor_control(command[1], command[2], command[3])
		
    elif command[0] == 'LA' : #Linear Actuator commands
        LA_control(command[1], command[2])
		
    elif command[0] == 'Se' : #Servo commands
        servo_control(command[1], command[2])
		
	elif command[0] == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	# Sending reply
	conn.send(reply)
	conn.close() # Close connections
	
def motor_control(Power, Direction, Speed)
	#Do motor stuff

def LA_Control(Power, Speed)
	#Do Linear Actuator stuff
	
def servo_control(Power, Pos)
	#Do Servo stuff