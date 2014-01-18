#!/usr/bin/env python

import unittest

def numberToList(number):
	numberList = map(int, str(number))
	return numberList

def listToNumber(list):
	number = 0
	base = 10
	place = 0
	list.reverse()
	for digit in list:
		number = number + (digit * (base ** place))
		place = place + 1
	return number

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

	def testSingleDigit(self):
		list = [4]
		actual = listToNumber(list)
		expected = 4
		self.assertTrue(expected==actual)

	def testDoubleDigit(self):
		list = [3,7]
		actual = listToNumber(list)
		expected = 37
		self.assertTrue(expected==actual)

class prependZerosTests(unittest.TestCase)

	def testAddLeadingZeros(self):
		list = [2,3]
		newLength = 4
		prependZeros(list, newLength)
		actual = list
		expected = [0,0,2,3]
		self.assertTrue(expected, actual)
	
def main():
    unittest.main()

if __name__ == '__main__':
    main()
