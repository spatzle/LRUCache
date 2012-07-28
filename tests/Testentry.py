from entry import Entry
from nose.tools import *

class Testentry(object):

	def test_init(self):
		ent = Entry('a','apple',5)
		assert 5 == ent.size
		assert 'a' == ent.key