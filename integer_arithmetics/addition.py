import unittest
import helpers.helper as helper

def addNumbers(a,b):
	aList = helper.numberToList(a)
	bList = helper.numberToList(b)
	cList = [0]
	sList = []
	
	n = len(aList)
	if len(bList) > n:
		n = len(bList)
	
	helper.prependZeros(aList,n + 1)
	helper.prependZeros(bList,n + 1)
	
	for i in range(n + 1):
		nSum = aList[i] + bList[i] + cList[i]
		nList = helper.numberToList(nSum)
		helper.prependZeros(nList, 2)
		sList.append(nList[1])
		cList.append(nList[0])
	
	return sList


class AdditionTests(unittest.TestCase):
	
	def testSingleDigitAdditionSingleDigitAnswer(self):
		a = 2
		b = 6
		expected = [0,8]
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)

	def testDingleDigitAdditionDoubleDigitAnswer(self):
		a = 7
		b = 8
		expected = [1,5]
		actual = addNumbers(a,b)
		self.assertTrue(expected==actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
