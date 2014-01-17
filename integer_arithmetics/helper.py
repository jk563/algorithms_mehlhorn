#!/usr/bin/env python

import unittest

def numberToList(number):
	return [3]

class numberToListTests(unittest.TestCase):

	def testSingleDigit(self):
	  	number = 3
	  	actual = numberToList(number)
	  	expected = [3]
	  	self.failUnless(expected==actual)

	def testDoubleDigit(self):
		number = 84
		actual = numberToList(number)
		expected = [8,4]
		self.failUnless(expected=value)
	
def main():
    unittest.main()

if __name__ == '__main__':
    main()
