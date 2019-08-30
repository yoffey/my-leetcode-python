# -*- coding: utf-8 -*
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        map, vals, res = {}, [], []
        for word in words:
            map[word] = map.get(word, 0) + 1
        for word in map.iterkeys():
            if len(vals) < k:
                heapq.heappush(vals, Val(word, map[word]))
            else:
                val = Val(word, map[word])
                if cmp(val, vals[0]) > 0:
                    heapq.heapreplace(vals, val)
        while vals:
            res.insert(0, heapq.heappop(vals).word)
        return res


class Val(object):
    def __init__(self, word, num):
        self.word = word
        self.num = num

    def __cmp__(self, other):
        if self.num == other.num:
            return cmp(other.word, self.word)
        else:
            return cmp(self.num, other.num)


s = Solution()
for s in s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4):
    print s