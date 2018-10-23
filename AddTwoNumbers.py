# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t = 0
        while (l1 != None or l2 != None):
            print( "start l1.val is %s, l2.val is %s" %(l1.val,l2.val))
            l1.val = l1.val + l2.val + t
            print( "after l1.val is %s, l2.val is %s"  %(l1.val,l2.val))
            if l1.val >= 10:
                l1.val = l1.val - 10
                print( "if >=10 l1.val is %s"  %(l1.val))
                t = 1
                l1 = l1.next
                l2 = l2.next
                print( "next l1.val is %s, l2.val is %s"  %(l1.val,l2.val))
            else:
                l1.val = l1.val
                print( "else l1.val is %s"  %(l1.val))
                t = 0
                l1 = l1.next
                l2 = l2.next
                #print( "next l1.val is %s, l2.val is %s" %(l1.val,l2.val))
                print(l11.val, l12.val, l13.val)
        return l1

l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13
l13.next = None

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l21.next = l22
l22.next = l23
l23.next = None

s = Solution()
s.addTwoNumbers(l11,l21)
