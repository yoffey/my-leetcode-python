# -*- coding: utf-8 -*
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.fix(S) == self.fix(T)

    def fix(self, s):
        stack, res = [], ''
        for c in s:
            stack.append(c)
        count = 0
        while len(stack):
            c = stack.pop()
            if c == '#':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                   res += c
        return res


s = Solution()
print s.backspaceCompare("a##c", "#a#c")