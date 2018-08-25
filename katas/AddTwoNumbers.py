class ListNode():

    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if (self is None or other is None):
            return False
        elif (self.next is None and other.next is None):
            return self.val == other.val
        else:
            return self.val == other.val and self.next == other.next

    def __repr__(self):
        value = f'{self.val}'
        if self.next is None:
            return value
        else:
            return f'{value}->{repr(self.next)}'


class Solution():

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = ListNode(0)

        carry = 0
        current_node = result_list
        while True:
            first_value = 0 if l1 is None else l1.val
            second_value = 0 if l2 is None else l2.val

            sum = carry + first_value + second_value
            current_node.val = sum % 10
            carry = int(sum / 10)

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            if l1 is None and l2 is None and carry == 0:
                current_node.next = None
                break
            current_node.next = ListNode(0)
            current_node = current_node.next

        return result_list
