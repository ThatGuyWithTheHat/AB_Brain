import RPi.GPIO as GPIO
import time


timeToHaveMotorRunning = 5
class motor:
	pinNum = -1
	de = None
	numDes = -1
	def __init__(self, pin, deb, motorNum):
		"""!@brief Creates a new motor object
                software which controls the motors

                @param pin defines which pin this motor is in relation to the whole thingy"""
		self.de = deb
		self.numDes = motorNum
                
		self.pinNum = pin

		self.de.debugPrint("pin number for motor #" + str(self.numDes) + "is " + str(self.pinNum))
		GPIO.setup(self.pinNum, GPIO.OUT)  # set up pin 17

	def activate(self):
                GPIO.output(self.pinNum, 1)
                time.sleep(timeToHaveMotorRunning)
                GPIO.output(self.pinNum, 0)
                
		
