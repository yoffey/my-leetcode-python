# -*- coding: utf-8 -*
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, left = [], set(['(', '{', '['])
        for c in s:
            if left.__contains__(c):
                if c == '(':
                    stack.append(')')
                elif c == '{':
                    stack.append('}')
                elif c == '[':
                    stack.append(']')
            else:
                l = len(stack)
                if l == 0 or stack[l - 1] != c:
                    return False
                stack.pop()
        return True if len(stack) == 0 else False


s = Solution()
str = "{[]}"
print s.isValid(str)