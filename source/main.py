#!/bin/env python3.6


global DEBUG #debug flag
#include files
import sys
sys.path.insert(0, '../include')
from timer import *
from debugger import *


#END INCLUDE

myDe = debugger()
print_lock = threading.Lock()
timers = []
def main():
	arguments = sys.argv #pull in arguments
	counter = 0
	for item in arguments:	
		#print(item)
		if(item == "-D" or item == "-d"):
			myDe.activate()
		myDe.debugPrint(item, "input " + str(counter))
		counter = counter + 1


	i = timer(.2, myDe)
	#myDe.debugPrint("Debugger Activated")
	timers.append(i)
	t = threading.Thread(target = beginTimer, args=(0,))
	t.daemon = True
	t.start()
	time.sleep(1)

	while(i.on):
		anyActive = False
		time.sleep(1)

def beginTimer(index):
	myDe.debugPrint("testing")
	timers[index].timing()


	




#print("test failed")

if __name__ == '__main__':
	DEBUG = False
	main()
