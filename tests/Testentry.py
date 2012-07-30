from entry import Entry
import time
from nose.tools import *

class Testentry(object):

	def test_init(self):
		ent = Entry('a','apple',5)
		assert 5 == ent.size
		assert 'a' == ent.key

	# test that time stamps are working
	def test_timestamp(self):
		ent = Entry('b','boy',3)
		time.sleep(0.001)
		ent2 = Entry('c','cat',4)
		assert ent.epochtimestamp < ent2.epochtimestamp
