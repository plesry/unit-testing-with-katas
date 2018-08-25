import unittest
from katas.AddTwoNumbers import ListNode, Solution

def linkedList(*args):
    list_of_nodes = [ListNode(arg) for arg in args]
    for cur_node, next_node in zip(list_of_nodes[:-1], list_of_nodes[1:]):
        cur_node.next = next_node
    return list_of_nodes[0]

class TestAddTwoNumbers(unittest.TestCase):

    def TestEqual(self):
        l1 = linkedList(1)
        l2 = linkedList(2)
        l12 = linkedList(1, 2)
        l21 = linkedList(2, 1)
        l123 = linkedList(1, 2, 3)
        l121 = linkedList(1, 2, 1)

        self.assertEqual(l1, l1)
        self.assertEqual(l12, l12)
        self.assertEqual(l123, l123)

        self.assertNotEqual(l1, l2)
        self.assertNotEqual(l12, l21)
        self.assertNotEqual(l123, l121)

        self.assertNotEqual(l1, l12)
        self.assertNotEqual(l21, l123)
        self.assertNotEqual(l121, l12)

    def TestZeroAddZero(self):
        self.assertEqual(
            linkedList(0), Solution().addTwoNumbers(linkedList(0), linkedList(0))
        )

    def TestTwoAddTwo(self):
        self.assertEqual(
            linkedList(4), Solution().addTwoNumbers(linkedList(2), linkedList(2))
        )

    def TestFiveAddFive(self):
        self.assertEqual(
            linkedList(0, 1), Solution().addTwoNumbers(linkedList(5), linkedList(5))
        )

    def TestTwentyOneAddThirtyTwo(self):
        self.assertEqual(
            linkedList(3, 5), Solution().addTwoNumbers(linkedList(1, 2), linkedList(2, 3))
        )

    def TestOneAddOneHundred(self):
        self.assertEqual(
            linkedList(1, 0, 1), Solution().addTwoNumbers(linkedList(1), linkedList(0, 0, 1))
        )

    def TestOneHundredAddOne(self):
        self.assertEqual(
            linkedList(1, 0, 1), Solution().addTwoNumbers(linkedList(0, 0, 1), linkedList(1))
        )

    def TestOthers(self):
        self.assertEqual(
            linkedList(7, 0, 8), Solution().addTwoNumbers(linkedList(2, 4, 3), linkedList(5, 6, 4))
        )
        self.assertEqual(
            linkedList(0, 0, 0, 1), Solution().addTwoNumbers(linkedList(9, 9, 9), linkedList(1))
        )
        self.assertEqual(
            linkedList(9, 9, 9), Solution().addTwoNumbers(linkedList(1, 6, 7), linkedList(8, 3, 2))
        )
        self.assertEqual(
            linkedList(7, 2, 5, 9), Solution().addTwoNumbers(linkedList(0, 1, 3, 9), linkedList(7, 1, 2))
        )
        self.assertEqual(
            linkedList(7, 9, 8, 1), Solution().addTwoNumbers(linkedList(9, 9, 8), linkedList(8, 9, 9))
        )


if __name__ == '__main__':
    unittest.main()