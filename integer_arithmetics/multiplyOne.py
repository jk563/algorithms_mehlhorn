import unittest
import helpers.helper as helper

def multiplyOneListsToList(a,b):
	return None


class MultiplyOneTests(unittest.TestCase):
	
	def testReturnsNoneIfSecondArgumentIsMoreThanOneDigit(self):
		a = [1,2,3]
		b = [2,6]
		expected = None
		actual = multiplyOneListsToList(a,b)
		self.assertTrue(expected==actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
