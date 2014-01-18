import unittest
import addition
import multiplyOne
import helpers.helper as helper

def multiplyListsReturnList(listA,listB):
	a = list(listA)
	b = (listB)
	s = []
	n = len(a)
	if len(b) > n:
		n = len(b)
	
	helper.prependZeros(a,n)
	helper.prependZeros(b,n)
	
	position = 0

	b.reverse()

	for i in range(n):
		partial = multiplyOne.multiplyOneListsReturnList(a,[b[i]])
		partial.reverse()
		adjustmentForBase = len(helper.numberToList(helper.listToNumber(partial))) + position
		helper.prependZeros(partial, adjustmentForBase)
		partial.reverse()
		s = addition.addListsReturnList(s,partial)
		position = position + 1

	return s

class MultiplyTests(unittest.TestCase):
	
	def testMultiplySingleDigits(self):
		a = [3]
		b = [8]
		expected = [0,0,2,4]
		actual = multiplyListsReturnList(a,b)
		self.assertTrue(expected==actual)

	def testMultiplyDoubleDigits(self):
		a = [3,4]
		b = [8,7]
		expected = [0,0,2,9,5,8]
		actual = multiplyListsReturnList(a,b)
		self.assertTrue(expected==actual)


	def testMultiplyMultipleDigits(self):
		a = [1,4,3,3]
		b = [8,5,7,9,2,4,7]
		expected = [0,0,0,0,0,1,2,2,9,4,0,6,0,9,5,1]
		actual = multiplyListsReturnList(a,b)
		self.assertTrue(expected==actual)
		

def main():
	unittest.main()

if __name__ == '__main__':
	main()
