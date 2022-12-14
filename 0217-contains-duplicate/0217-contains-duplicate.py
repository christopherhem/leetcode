class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_dup = set()
        for i in nums:
            if i in check_dup:
                return True
            check_dup.add(i)
        return False


        