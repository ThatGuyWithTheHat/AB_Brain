

import threading
import sys
from termcolor import colored


class debugger:
	on = False
	def __init__(self):
		self.on = False

	def activate(self):
		self.on = True

	def debugPrint(self, msg, header = ""):
		print_lock = threading.Lock()
		#print(str(self.on))
		if(self.on):
			print(colored('DEBUGGER:', 'red'))
			print(colored(header, 'yellow'))
			print(colored('\t' + msg,'green'))