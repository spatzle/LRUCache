from lrucache import LRUCache
from entry import Entry
import heapq
import time
from nose.tools import *

class TestLRUCache(object):

	def setup(self):
		self.lruc = LRUCache(10)
		self.lruc2 = LRUCache(10)
		self.lruc3 = LRUCache(10)
		self.lruc4 = LRUCache(10)

	def test_init(self):
		assert 0 == self.lruc._curSize
		assert 10 == self.lruc.maxSize

	##############################
	# test private methods
	##############################	
	def test_exceedesMaxSize(self):
		assert True == self.lruc._willExceedesMaxSize(41)
		assert False == self.lruc._willExceedesMaxSize(1)

	def test_isInCache(self):
		self.lruc2._add(Entry('b','boy',3))
		assert True==self.lruc2._isInCache('b')
		assert False==self.lruc2._isInCache('a') # we didn't put 'a' in this cache
		self.lruc2.store('c','cat',3)
		assert True ==self.lruc2._isInCache('c')

	def test_add_entry(self):
		beforeCacheLen  = len(self.lruc._cache)
		beforePQLen  = len(self.lruc._ordering)
		ent = Entry('a','apple',5)
		self.lruc._add_entry(ent);
		assert self.lruc._curSize == 5
		assert self.lruc._cache['a']=='apple'
		afterCacheLen  = len(self.lruc._cache)
		afterPQLen  = len(self.lruc._ordering)
		assert beforeCacheLen == beforePQLen ==0
		assert afterCacheLen ==afterPQLen ==1

	def test_add_entry_correct_priority(self):
		ent = Entry('a','apple',5)	
		ent2 = Entry('b','cat',3)	
		# add some entries to the cache
		self.lruc3._add_entry(ent)
		self.lruc3._add_entry(ent2)
		# test that they are in the right order
		smallest = heapq.heappop(self.lruc3._ordering)
		assert smallest == ent

	def test_update_entry_correct_priority(self):
		ent = Entry('a','apple',5)	
		time.sleep(0.001)
		ent2 = Entry('b','cat',3)	
		self.lruc4._add_entry(ent)
		self.lruc4._add_entry(ent2)
		time.sleep(0.001)
		ent.touch()
		self.lruc4._update_entry(ent)
		smallest = heapq.heappop(self.lruc4._ordering)
		assert smallest == ent2


	# def test_update_entry(self):

	##############################
	# test public methods
	##############################
