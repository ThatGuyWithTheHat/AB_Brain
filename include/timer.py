#include files
import sys
sys.path.insert(0, '../include')
import threading
from queue import Queue
import time


#END INCLUDE
class timer:
	#set up variables
	endTime = 0 #holds the timer end variable
	startTime = 0
	on = False #tells us if the timer is running
	#set up the timer by passing an end time
	def __init__(self, endingTime, de):
		self.endTime = endingTime * 60
		de.debugPrint("debug mode in timer")
		de.debugPrint("end time: " + str(self.endTime))



	def isRunning(self):
		return self.on

	def timing(self):
		self.on = True #we are running now
		startTime = time.time()
		while(1):
			deltaTime = time.time() - startTime #how much time has ellapsed
			if deltaTime >= self.endTime:
				break
			time.sleep(0.5)
		self.on = False #not running
		#print("complete")


