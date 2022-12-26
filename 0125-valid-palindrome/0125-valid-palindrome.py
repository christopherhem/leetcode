class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = "abcdefghijklmnopqrstuvwxyz0123456789"
        pal = ""
        for i in s.lower():
            if i in char:
                pal += i

        rev_pal = pal[::-1]

        return pal == rev_pal

    