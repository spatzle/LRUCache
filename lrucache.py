from entry import Entry
import heapq
import Queue

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
		print "maxSize of cache: "+self.maxSize

	# will new item's size exceed max size
	def _willExceedesMaxSize(self,newSize):
		return (self._curSize + newSize) >= self.maxSize

	# is this key in cache
	def _isInCache(self,key):
		return self._cache.has_key(key)

	##########################
	# store item in the cache
	############################
	# what should be cached, and the size of the item to be cached
	def _add_entry(self,entry):
		self._cache[entry.key] = entry.value
		self._curSize += entry.size
		heapq.heappush(self._ordering, entry)

	def _update_entry(self,entry):
		heapq.heapreplace(self._ordering, entry)

	def _add(self,entry):
		# if not already in cache can add it
		if(not self._isInCache(entry.key)):
			# if no more space, make some space first
			if (self._willExceedesMaxSize(entry.size)):
				self._evict()
			self._add_entry(entry)
		else: # just update the time
			entry.touch()
			heapq.heapreplace(self._ordering, entry)

	def store(self,key,value,size):
		self._add(Entry(key,value,size)) 

	##########################
	# fetch item from the cache
	# return the value of the key
	############################
	def fetch(self,key):
		return self._cache[key]

	############################################################
	# delete item that is least frequently used cache
	#############################################################
 	# when no more space on the LRU cache, LRU entry needs to be evicted
	def _evict(self):
		entry = heapq.heappop(self._ordering)
		del self._cache[entry.key]
