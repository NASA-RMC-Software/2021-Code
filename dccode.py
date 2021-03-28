from gpiozero import PWMOutputDevice
from time import sleep
 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD = 6    # IN1 - Forward Drive
PWM_REVERSE = 19    # IN2 - Reverse Drive
 
# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forward = PWMOutputDevice(PWM_FORWARD, True, 0, 1000)
reverse = PWMOutputDevice(PWM_REVERSE, True, 0, 1000)
 
 
def allStop():
    forward.value = 0
    reverse.value = 0
 
def forwardDrive(x):
    forward.value = x
    reverse.value = 0

def reverseDrive(x):
    forward.value = 0
    reverse.value = x


