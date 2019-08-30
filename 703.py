# -*- coding: utf-8 -*
import Queue
class KthLargest(object):
    _pq, _size = None, 0

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self._pq = Queue.PriorityQueue(k)
        self._size = k
        for num in nums:
            self.add(num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self._pq.qsize() == self._size:
            k = self._pq.get()
            if val > k:
                self._pq.put(val)
            else:
                self._pq.put(k)
        else:
            self._pq.put(val)
        res = self._pq.get()
        self._pq.put(res)
        return res


# 网上优秀代码 heapq是二叉堆
import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]