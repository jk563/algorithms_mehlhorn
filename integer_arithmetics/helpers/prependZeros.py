import unittest

def prependZeros(originalList,newLength):
	originalList.reverse()
        if len(originalList) is newLength:
                pass
        else:
                zerosToPrepend = newLength - len(originalList)
                for _ in range(zerosToPrepend):
                        originalList.append(0)
        originalList.reverse()


class prependZerosTests(unittest.TestCase):

        def testAddLeadingZeros(self):
                list = [2,3]
                newLength = 4
                prependZeros(list, newLength)
                actual = list
                expected = [0,0,2,3]
                self.assertTrue(expected == actual)

        def testDontAlterList(self):
                list = [3,5,6,2]
                newLength = 4
                prependZeros(list,newLength)
                actual = list
                expected = [3,5,6,2]
                self.assertTrue(expected==actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
