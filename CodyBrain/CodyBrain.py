import socket
import dccode
import threading

HOST = '10.10.16.214' # Cody IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client port aka laptop
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#managing error exception
try:
    s.bind((HOST, PORT))
except:
    print 'Bind failed '

s.listen(5)
print 'Socket awaiting messages'
(conn, addr) = s.accept()
print 'Connected'

#Global Variables
MPower = 'Off'
MDirection = 'Fwd'
MSpeed = 0.0
shutdwn = False

def motorcontrol():
	while True:
		if shutdwn == True:
			break
		#Do motor stuff
		if MPower == 'On':
			if MDirection == 'Fwd':
				dccode.forwardDrive(MSpeed)
			elif MDirection == 'Rev':
				dccode.reverseDrive(MSpeed)
		elif MPower == 'Off':
				dccode.allStop()

def commands():
	# awaiting for message
	while True:
		data = conn.recv(1024)
		print 'I sent a message back in response to: ' + data
		reply = ''
		command = data.split(", ")
		
		global MPower
		global MDirection
		global MSpeed
		global shutdwn
		
		#Running commands
		if command[0] == 'Mo': #Motor commands
			MPower = command[1]
			MDirection = command[2]
			MSpeed = float(command[3])
			reply = 'Motor ' + MPower
			
		elif command[0] == 'LA' : #Linear Actuator commands
			LA_control(command[1], command[2])
			
		elif command[0] == 'Se' : #Servo commands
			servo_control(command[1], command[2])
			
		elif command[0] == 'quit':
			conn.send('Terminating')
			shutdwn = True
			break
		else:
			reply = 'Unknown command'

		# Sending reply
		conn.send(reply)
	conn.close() # Close connections

t1 = threading.Thread(name='motorcontrol',target=motorcontrol)
t2 = threading.Thread(name='commands',target=commands)

t1.start()
t2.start()

t1.join()
t2.join()

    
#def LA_Control(Power, Speed):
    #Do Linear Actuator stuff
    
#def servo_control(Power, Pos):
    #Do Servo stuff
