# -*- coding: utf-8 -*
class Solution(object):
    # 迭代法 时间复杂度O(n) 空间复杂度O(n)
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set([])
        while head and head.next:
            if s.__contains__(head):
                return head
            s.add(head)
            head = head.next
        return None

    # 迭代法 时间复杂度O(n) 空间复杂度O(1)
    def detectCycle2(self, head):
        turtle = rabbit = finder = head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                while finder != turtle:
                    turtle = turtle.next
                    finder = finder.next
                return finder
        return None


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
print s.detectCycle2(head)