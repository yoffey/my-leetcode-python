# -*- coding: utf-8 -*
class Solution(object):
    # 迭代法 时间复杂度O(n) 空间复杂度O(n)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set([])
        while head and head.next:
            if s.__contains__(head):
                return True
            s.add(head)
            head = head.next
        return False

    # 龟兔赛跑法 时间复杂度O(n) 空间复杂度O(1)
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        turtle = rabbit = head
        while rabbit and rabbit.next:
            turtle, rabbit = turtle.next, rabbit.next.next
            if turtle == rabbit:
                return True
        return False


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
head = ListNode(3)
next2 = ListNode(2)
next3 = ListNode(0)
next4 = ListNode(-4)
head.next = next2
next2.next = next3
next3.next = next4
next4.next = next2
print s.hasCycle2(head)