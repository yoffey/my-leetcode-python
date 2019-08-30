# -*- coding: utf-8 -*
class Solution(object):
    # 迭代法 O(n)
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, res = None, head
        while head and head.next:
            if pre:
                pre.next = head.next
            else:
                res = head.next
            temp = head.next.next
            head.next.next = head
            head.next = temp
            pre = head
            head = head.next
        return res

    # 递归法 O(n)
    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        res = head.next
        temp = head.next.next
        head.next.next = head
        head.next = temp
        head.next = self.swapPairs2(temp)
        return res


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
head = ListNode(1)
next2 = ListNode(2)
next3 = ListNode(3)
next4 = ListNode(4)
head.next = next2
next2.next = next3
next3.next = next4
next4.next = None
head = s.swapPairs2(head)
while head:
    print head.val
    head = head.next