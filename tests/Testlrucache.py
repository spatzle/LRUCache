from lrucache import LRUCache
from entry import Entry
from nose.tools import *

class TestLRUCache(object):

	def setup(self):
		self.lruc = LRUCache(10)
		self.lruc2 = LRUCache(10)

	def test_init(self):
		assert 0 == self.lruc._curSize
		assert 10 == self.lruc.maxSize

	def test_exceedesMaxSize(self):
		assert True == self.lruc._willExceedesMaxSize(41)
		assert False == self.lruc._willExceedesMaxSize(1)

	def test_isInCache(self):
		self.lruc2._add(Entry('b','boy',3))
		assert True==self.lruc2._isInCache('b')
		assert False==self.lruc2._isInCache('a') # we didn't put 'a' in this cache
		self.lruc2.store('c','cat',3)
		assert True ==self.lruc2._isInCache('c')

	def test_add(self):
		ent = Entry('a','apple',5)
		self.lruc._add(ent);
		assert self.lruc._curSize == 5
		assert self.lruc._cache['a']=='apple'


