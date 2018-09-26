import RPi.GPIO as GPIO



class motor:
	pinNum = -1
	def __init__(self, pin):
			 """!@brief Creates a new motor object

    software which controls the motors

    @param pin defines which pin this motor is in relation to the whole thingy
    """
		self.pinNum = pin
		if(DEBUG):
			print("pin# " + str(pin))
		GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
		GPIO.setup(17, GPIO.OUT)  # set up pin 17
		GPIO.setup(18, GPIO.OUT)  # set up pin 18 
		GPIO.output(17, 1)  # turn on pin …