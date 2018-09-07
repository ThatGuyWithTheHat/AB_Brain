#!/bin/env python3.6

import sys
sys.path.insert(0, '../include')
from include import *



i = timer(.2)
print_lock = threading.Lock()
timers = []
def main():
	print("hello world")
	arguments = sys.argv
	for item in arguments:
		print(item)

	
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