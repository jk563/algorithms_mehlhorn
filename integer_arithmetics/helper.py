#!/usr/bin/env python

import unittest

def numberToArray(number):
	return [3]

class numberToArrayTests(unittest.TestCase):

	def testSingleDigit(self):
	  number = 3
	  actual = numberToArray(number)
	  expected = [3]
	  self.failUnless(expected==actual)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
