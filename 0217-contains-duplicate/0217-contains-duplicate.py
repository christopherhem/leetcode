class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_dup = {}
        for i in nums:
            if i in check_dup:
                return True
            check_dup[i] = True
        return False


        