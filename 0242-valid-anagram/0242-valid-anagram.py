class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_co, t_co = {}, {}

        for i in range(len(s)):
            s_co[s[i]] = 1 + s_co.get(s[i], 0)
            t_co[t[i]] =  1 + t_co.get(t[i], 0)

        return s_co == t_co