import os

class Protocol:

	_ = []

	def __bool__(self):
		return bool(len(self._)) 

	def __getitem__(self, key):
		return self._[key]

	def append(self, value):
		if len(self._) == 10:
			self._.pop(0)
		self._.append(value)

def cls():
	_ = os.system("clear") if os.name == "posix" else os.system("cls")