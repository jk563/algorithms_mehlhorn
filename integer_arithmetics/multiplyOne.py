import unittest
import helpers.helper as helper
import addition

def multiplyOneListsToList(a,b):
	if len(b)!= 1:
		return None

	n = len(a)
	c = [0]
	d = []

	a.reverse()

	print a
	print b
	print c
	print d

	for i in range(n):
		cAndDNum = a[i] * b[0]
		cAndD = helper.numberToList(cAndDNum)
		helper.prependZeros(cAndD,2)
		c.append(cAndD[0])
		d.append(cAndD[1])
		print cAndDNum
		print cAndD
		print c 
		print d
	
	c.reverse()
	d.reverse()	
	s = addition.addListsReturnList(c,d)
	print s
	return s	


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
		expected = [0,2,4]
		actual = multiplyOneListsToList(a,b)
		self.assertTrue(expected==actual)
		

def main():
    unittest.main()

if __name__ == '__main__':
    main()
