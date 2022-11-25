class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        for i, j in enumerate(nums):
            if left == (total - left - j):
                return i
            left += j
        return -1