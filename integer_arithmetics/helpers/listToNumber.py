import unittest

def listToNumber(originalList):
	localList = list(originalList)
        number = 0
        base = 10
        place = 0
        localList.reverse()
        for digit in localList:
                number = number + (digit * (base ** place))
                place = place + 1
        return number


class listToNumberTests(unittest.TestCase):

        def testSingleDigit(self):
                list = [4]
                actual = listToNumber(list)
                expected = 4
                self.assertTrue(expected==actual)

        def testDoubleDigit(self):
                list = [3,7]
                actual = listToNumber(list)
                expected = 37
                self.assertTrue(expected==actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

