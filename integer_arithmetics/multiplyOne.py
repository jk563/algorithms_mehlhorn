import unittest
import helpers.helper as helper
import addition

def multiplyOneListsReturnList(listA,listB):
	a = list(listA)
	b = list(listB)

	if len(b)!= 1:
		return None

	n = len(a)
	c = [0]
	d = []

	a.reverse()

	for i in range(n):
		cAndDNum = a[i] * b[0]
		cAndD = helper.numberToList(cAndDNum)
		helper.prependZeros(cAndD,2)
		c.append(cAndD[0])
		d.append(cAndD[1])
	
	c.reverse()
	d.reverse()	
	
	return addition.addListsReturnList(c,d)


class MultiplyOneTests(unittest.TestCase):
	
	def testReturnsNoneIfSecondArgumentIsMoreThanOneDigit(self):
		a = [3]
		b = [2,6]
		expected = None
		actual = multiplyOneListsReturnList(a,b)
		self.assertTrue(expected==actual)

	def testReturnsCorrectAnswerForTwoSingleDigits(self):
		a = [4]
		b = [6]
		expected = [0,2,4]
		actual = multiplyOneListsReturnList(a,b)
		self.assertTrue(expected==actual)
	
	def testMultiplyMultipleDigitsbyOneDigit(self):
		a = [2,5,2,7,6,4,3]
		b = [7]
		expected = [0,1,7,6,9,3,5,0,1]
		actual = multiplyOneListsReturnList(a,b)
                self.assertTrue(expected==actual)	


def main():
    unittest.main()

if __name__ == '__main__':
    main()
