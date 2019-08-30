# -*- coding: utf-8 -*
class Solution(object):
    # 暴力破解 O(n^2)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # dict O(n)
    def twoSumDict(self, nums, target):
        res = []; dict = {}
        for i in range(len(nums)):
            need_val = target - nums[i]
            if dict.has_key(need_val):
                return [i, dict[need_val]]
            dict[nums[i]] = i
        return res


s = Solution()
n = [2, 7, 11, 15]; t = 9
print s.twoSum(n, t)
print s.twoSumDict(n, t)
