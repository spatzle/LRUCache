import time

# an item in the cache
class Entry:

	def __init__(self,key,value,size):
		self.key = key
		self.value = value
		self.size = size
		self.touch()
		return

	def touch(self):
		self.epochtimestamp = (time.time())	
		
	def __cmp__(self, other):
		return cmp(self.epochtimestamp, other.epochtimestamp)
