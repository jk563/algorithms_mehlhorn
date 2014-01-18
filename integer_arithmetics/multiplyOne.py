import unittest
import helpers.helper as helper

def multiplyOneListsToList(a,b):
	return None


class MultiplyOneTests(unittest.TestCase):
	
	def testReturnsNoneIfSecondArgumentIsMoreThanOneDigit(self):
		a = [3]
		b = [2,6]
		expected = None
		actual = multiplyOneListsToList(a,b)
		self.assertTrue(expected==actual)

	def testReturnsCorrectAnswerForTwoSingleDigits(self):
		a = [4]
		b = [6]
		expected = [2,4]
		actual = multiplyOnListsToList(a,b)
		self.assertTrue(expected==actual)
	

def main():
    unittest.main()

if __name__ == '__main__':
    main()
