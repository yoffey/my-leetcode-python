# -*- coding: utf-8 -*
class Solution(object):
    # 栈 时间复杂度 O(n*k) 空间复杂度 O(n)
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        stack = []
        while True:
            count = 0
            tmp = head
            while tmp and count < k:
                stack.append(tmp)
                tmp = tmp.next
                count += 1
            if count != k:
                p.next = head
                break
            while len(stack):
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            head = tmp
        return dummy.next

    # 递归 时间复杂度 O(n*k) 空间复杂度 O(1)
    def reverseKGroup2(self, head, k):
        count = 0
        tmp = head
        while tmp and count < k:
            tmp = tmp.next
            count += 1
        if count == k:
            pre, end = None, head
            while count > 0:
               target = head.next
               head.next = pre
               pre = head
               head = target
               count -= 1
            end.next = self.reverseKGroup2(tmp, k)
            return pre
        else:
            return head


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
res = s.reverseKGroup2(head, 2)
while res:
    print res.val
    res = res.next