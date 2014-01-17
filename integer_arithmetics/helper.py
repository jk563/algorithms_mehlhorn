#!/usr/bin/env python

import unittest

def numberToList(number):
	numberList = map(int, str(number))
	return numberList

def listToNumber(list, base):
	return None

class numberToListTests(unittest.TestCase):

	def testSingleDigit(self):
	  	number = 3
	  	actual = numberToList(number)
	  	expected = [3]
	  	self.assertTrue(expected==actual)

	def testDoubleDigit(self):
		number = 84
		actual = numberToList(number)
		expected = [8,4]
		self.assertTrue(expected==actual)
	
	def test15Digit(self):
		number = 384958273428695
		actual = numberToList(number)
		expected = [3,8,4,9,5,8,2,7,3,4,2,8,6,9,5]
		self.assertTrue(expected==actual)

class listToNumberTests(unittest.TestCase):

	def testSingleDigitBaseTen(self):
		list = [4]
		base = 10
		actual = listToNumber(list, base)
		expected = 4
		self.assertTrue(expected==actual)
	
def main():
    unittest.main()

if __name__ == '__main__':
    main()
