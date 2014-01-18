import unittest
import addition
import multiplyOne
import helpers.helper as helper

def multiplyListsReturnList(a,b):
	return None


class MultiplyTests(unittest.TestCase):
	
	def testMultiplySingleDigits(self):
		a = [3]
		b = [8]
		expected = [0,0,2,4]
		actual = multiplyListsReturnList(a,b)
		self.assertTrue(expected==actual)

	def testMultiplyMultipleDigits(self):
		pass

def main():
	unittest.main()

if __name__ == '__main__':
	main()
