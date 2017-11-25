
# -*- coding: UTF-8 -*- 

import unittest

class MyDict(dict):
	pass

class TestMyDict(unittest.TestCase):

	def setUp(self):
		print("setUp setUp")

	def tearDown(self):
		print("tearDown tearDown")

	def test_init(self):
		d = MyDict(one = 1, two = 2)
		self.assertEqual(d["one"],1)
		self.assertEqual(d["two"],2)

	def test_nothing(self):
		pass

if __name__ == "__main__":
	unittest.main()

