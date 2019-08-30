# -*- coding: utf-8 -*
class MyStack(object):
    _queue1, _queue2 = None, None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue1 = []
        self._queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self._queue1:
            self._queue1.insert(0, x)
        else:
            self._queue2.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self._queue1:
            for i in range(0, len(self._queue1) - 1):
                self._queue2.insert(0, self._queue1.pop())
            return self._queue1.pop()
        else:
            for i in range(0, len(self._queue2) - 1):
                self._queue1.insert(0, self._queue2.pop())
            return self._queue2.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self._queue1:
            for i in range(0, len(self._queue1) - 1):
                self._queue2.insert(0, self._queue1.pop())
            res = self._queue1.pop()
            self._queue2.insert(0, res)
            return res
        else:
            for i in range(0, len(self._queue2) - 1):
                self._queue1.insert(0, self._queue2.pop())
            res = self._queue2.pop()
            self._queue1.insert(0, res)
            return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._queue1) == 0 and len(self._queue2) == 0


s = MyStack()
s.push(1)
s.push(2)
print s.top()       # 2
print s.pop()       # 2
print s.empty()     # false
print s.pop()       # 1
print s.empty()     # true
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()