#!/bin/env python3.6

import sys
sys.path.insert(0, '../include')

import threading
from queue import Queue
import time
from timer import *

i = timer(.2)
print_lock = threading.Lock()
timers = []
def main():
	print("hello world")

	
	t = threading.Thread(target = beginTimer, args=(0,))
	t.daemon = True
	t.start()
	time.sleep(1)
	while(i.on):
		anyActive = False
		time.sleep(1)


def beginTimer(index):
	print("begin count down")
	i.timing()
	timers.append(i)


	




#print("test failed")

if __name__ == '__main__':
	main()