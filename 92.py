# -*- coding: utf-8 -*
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        borrow = ListNode(0)
        borrow.next = head
        start = borrow
        for i in range(0, m - 1):
            start = start.next
        p = start.next
        for i in range(m, n):
            if p == None or p.next == None:
                break
            target = p.next
            p.next = target.next
            target.next = start.next
            start.next = target
        return borrow.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
head = ListNode(1)
next2 = ListNode(2)
next3 = ListNode(3)
next4 = ListNode(4)
next5 = ListNode(5)
head.next = next2
next2.next = next3
next3.next = next4
next4.next = next5
next5.next = None
res = s.reverseBetween(head, 2, 4)
while res:
    print res.val
    res = res.next