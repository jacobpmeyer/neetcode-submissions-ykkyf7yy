class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        output = []
        for s in strs:
            t = "".join(sorted(s))
            hm.setdefault(t, []).append(s)
        for v in hm.values():
            output.append(v)
        return output
        