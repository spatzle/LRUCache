# an item in the cache
class Entry:

	def __init__(self,key,value,size):
		self.key = key
		self.value = value
		self.size = size
		self.ordering = 0
