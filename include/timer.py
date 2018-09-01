
import time
class timer:
	#set up variables
	endTime = 0 #holds the timer end variable
	startTime = 0
	on = False #tells us if the timer is running
	#set up the timer by passing an end time
	def __init__(self, endingTime):
		self.endTime = endingTime * 60
		print("end time: " + str(self.endTime))



	def isRunning(self):
		return self.on

	def timing(self):
		print(self.endTime)
		self.on = True #we are running now
		startTime = time.time()
		while(1):
			deltaTime = time.time() - startTime #how much time has ellapsed
			print(str(deltaTime))
			if deltaTime >= self.endTime:
				break
			time.sleep(0.5)
		self.on = False #not running
		print("complete")

