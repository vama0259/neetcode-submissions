class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        for a in range(len(s)):
            if s[a] != t[a]:
                return False
        return True