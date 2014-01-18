import unittest
import helpers.helper as helper

def addNumberLists(a,b):
	c = [0]
	s = []
	
	n = len(a)
	if len(b) > n:
		n = len(b)
	
	helper.prependZeros(a,n + 1)
	helper.prependZeros(b,n + 1)

	a.reverse()
	b.reverse()
	
	for i in range(n + 1):
		nSum = a[i] + b[i] + c[i]
		nSumList = helper.numberToList(nSum)
		helper.prependZeros(nSumList, 2)
		s.append(nSumList[1])
		c.append(nSumList[0])
	
	s.reverse()
	return s

def addNumbers(a,b):
	aList = helper.numberToList(a)
	bList = helper.numberToList(b)
	return addNumberLists(aList,bList)
		

class AdditionTests(unittest.TestCase):
	
	def testSingleDigitAdditionSingleDigitAnswer(self):
		a = 2
		b = 6
		expected = [0,8]
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)

	def testSingleDigitAdditionDoubleDigitAnswer(self):
		a = 7
		b = 8
		expected = [1,5]
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)

	def testDoubleDigitAdditionDoubleDigitAnswer(self):
		a = 15
		b = 49
		expected = [0,6,4]
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)

	def testBigNumber(self):
		a = 46346774636
		b = 5455465642675236
		expected = [5,4,5,5,5,1,1,9,8,9,4,4,9,8,7,2]
		actual = addNumbers(a,b)
		self.assertTrue(expected,actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
