import unittest

def addNumbers(a,b):
	return None


class AdditionTests(unittest.TestCase):
	
	def testSingleDigitAdditionSingleDigitAnswer(self):
		a = 2
		b = 6
		expected = 8
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
