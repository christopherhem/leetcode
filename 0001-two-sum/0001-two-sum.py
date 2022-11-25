class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]  
            if remaining in d:
                return[d[remaining], i]
            d[value]= i
        