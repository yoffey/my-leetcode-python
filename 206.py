# -*- coding: utf-8 -*
class Solution(object):
    # 迭代法 O(n)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    # 递归法 O(n)
    def reverseList2(self, head):
        if head == None or head.next == None:
            return head
        tail = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return tail


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


tail = ListNode(5); tail.next = None
n4 = ListNode(4); n4.next = tail
n3 = ListNode(3); n3.next = n4
n2 = ListNode(2); n2.next = n3
head = ListNode(1); head.next = n2

res = Solution().reverseList2(head)
while res:
    print res.val
    res = res.next

