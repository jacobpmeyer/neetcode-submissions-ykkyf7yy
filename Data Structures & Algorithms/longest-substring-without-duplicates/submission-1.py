class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        ml = 0
        l = 0
        r = 0
        while l < len(s) and r < len(s):
            if s[r] in st:
                ml = max(ml, r - l)
                st.remove(s[l])
                l += 1
            else:
                st.add(s[r])
                r += 1
        ml = max(ml, r - l)

        return ml