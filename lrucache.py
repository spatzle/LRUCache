

# least recently used cache datastructure removes least frequently used item 
# once it's full

class LRUCache:
	
	def __init__(self,maxsz=1000):
		self.maxSize = maxsz;
		self._curSize = 0; # the current size of the cache on initialization
		self._cache = {}
		self._ordering = []

	# pretty prints the content of the datastructure
	def __str__():
		print "maxSize: "+self.maxSize

	# will new item's size exceed max size
	def willExceedesMaxSize(self,newSize):
		return (self._curSize + newSize) >= self.maxSize

	# what should be cached, and the size of the item to be cached
	def _add_entry(self,entry):
		self._cache[entry.key] = entry.value;
		self._curSize += entry.size;
		# add ordering

	def add(self,entry):
		if (self.lruc.willExceedesMaxSize(entry.size)):
			self.evictLRU()
		else:
			self._add_entry(entry)

 	# when no more space on the LRU cache, LRU entry needs to be evicted
	def evictLRU(self):
		" "



