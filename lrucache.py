

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

	# is this key in cache
	def isInCache(self,key):
		return self._cache.has_key(key)


	# what should be cached, and the size of the item to be cached
	def _add_entry(self,entry):
		self._cache[entry.key] = entry.value;
		self._curSize += entry.size;
		self._ordering.append(entry); # add to end of the list


	def add(self,entry):
		# if 
		if(not self.isInCache(entry.key)):
			if (self.willExceedesMaxSize(entry.size)):
				self.evictLRU()
			self._add_entry(entry)

		""" update ordering of the entry """


 	# when no more space on the LRU cache, LRU entry needs to be evicted
	def evictLRU(self):
		" "



