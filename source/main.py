#!/bin/env python3.6


global DEBUG #debug flag
#include files
import sys
sys.path.insert(0, '../include')
from timer import *
from debugger import *
import RPi.GPIO
from motor import *



#END INCLUDE
#define pin numbers for the motors
MOTOR1 = 8
MOTOR2 = 10
MOTOR3 = 12
MOTOR4 = 16
MOTOR5 = 18

GPIO.setmode(GPIO.BOARD)  # set board mode to Broadcom

motorPins = [MOTOR1,MOTOR2,MOTOR3,MOTOR4,MOTOR5]
motors = []

myDe = debugger()
print_lock = threading.Lock()
timers = []
times = []
def main():
	arguments = sys.argv #pull in arguments
	counter = 0
	numExpected = False

        
	for item in arguments:
            if (numExpected):
                data = item.split('/')
                times.append(float(data[1]))
                myDe.debugPrint(times)
                mtrNum = int(data[0])
                motors.append(motor(motorPins[mtrNum-1], myDe, mtrNum))
                print(times)
                print(mtrNum)
                numExpected = False
                
		#print(item)  
            if(item == "-D" or item == "-d"):
                myDe.activate()
                myDe.debugPrint(item, "input " + str(counter))
                counter = counter + 1
            if(item.startswith("-t")):
                myDe.debugPrint("found timer input in minutes")
                numExpected = True
	count = 0
	for tm in times:
            newTimer = timer(tm, myDe, motors[count])
            timers.append(newTimer)
            count += 1
	#myDe.debugPrint("Debugger Activated")
	for i in range(0, len(timers)):
            t = threading.Thread(target = beginTimer, args=(i,))
            t.daemon = True
            t.start()
	activeTimers = True
	time.sleep(3)
	while(activeTimers):
            activeTimers = False
            for tmr in timers:
                print(tmr.isRunning())
                if (tmr.isRunning()):
                    activeTimers = True

            time.sleep(1)


def beginTimer(index):
	myDe.debugPrint("testing")
	timers[index].timing()







#print("test failed")

if __name__ == '__main__':
	DEBUG = False
	main()
