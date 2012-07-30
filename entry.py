import time

# an item in the cache
class Entry:

	def __init__(self,key,value,size):
		self.key = key
		self.value = value
		self.size = size
		self.epochtimestamp  = 0
		self.touch()
		return

	def touch(self):
		self.epochtimestamp = (time.time())	
		
	# def __str__(self):
	# 	return self.value
		
	def __cmp__(self, other):
		return cmp(self.epochtimestamp, other.epochtimestamp)
