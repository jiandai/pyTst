from unittest import TestCase

import pythonPlayGround
class Test_pythonPlayGround(TestCase):
	def test_is_string(self):
		s = pythonPlayGround.tst()
		self.assertTrue(isinstance(s[0], basestring))
		self.assertTrue(isinstance(s[1], basestring))
