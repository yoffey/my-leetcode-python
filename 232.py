# -*- coding: utf-8 -*
class MyQueue(object):
    _stack1, _stack2 = None, None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack1 = []
        self._stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self._stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self._stack2) == 0:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
        return self._stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self._stack2) == 0:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
        return self._stack2[len(self._stack2) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self._stack1) == 0 and len(self._stack2) == 0


q = MyQueue()
q.push(1)
q.push(2)
print q.peek()      # 1
print q.pop()       # 1
print q.empty()     # false
print q.pop()       # 2
print q.empty()     # true
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()