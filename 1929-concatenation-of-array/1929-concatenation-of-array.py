class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # One liner Solution #
#         return nums+nums
        
        
        # For Loop Solution #
        result = []
        n = len(nums)
        
        for i in range(2 * n):
            result.append(nums[i%n])
        return result
    
        