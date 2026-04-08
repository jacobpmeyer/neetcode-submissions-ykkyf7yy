class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
        
        for c in t:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1

        for k in d1.keys():
            if k not in d2 or d1[k] != d2[k]:
                return False

        return True